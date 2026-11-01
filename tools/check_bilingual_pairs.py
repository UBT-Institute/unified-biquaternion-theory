#!/usr/bin/env python3
"""Fail closed when paired English/Czech documents drift structurally."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


LANG_RE = re.compile(r"^(?P<stem>.+)\.(?P<lang>en|cs)(?P<suffix>\.(?:md|tex|rst))$")
TEXT_SUFFIXES = {".md", ".tex", ".rst"}
EXCLUDED_PARTS = {
    ".git",
    "ARCHIVE",
    "archive_legacy",
    "generated",
    "build",
    "vendor",
    "node_modules",
}
GOVERNANCE_FILES = {
    "AGENTS.md",
    "CONTRIBUTING.md",
    ".github/pull_request_template.md",
}
SHARED_LANGUAGE_NEUTRAL_FILES = {
    "CLAIMS_MATRIX.md",
    "docs/textbook/main.tex",
    "docs/textbook/chapters/04_covariant_tetrad_geometry.tex",
    # Existing English-only legacy notes; keep stable public paths during lint cleanup.
    "research_tracks/T2_GAUGE/su3_flat_affine_vacuum_no_go.md",
    "research_tracks/T2_GAUGE/su3_raw_carrier_lie_closure.md",
    "research_tracks/theta_complex_time_classification/README.md",
}

MATH_RE = re.compile(
    r"\$\$(.*?)\$\$|\\\[(.*?)\\\]|\\\((.*?)\\\)|"
    r"\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\}(.*?)"
    r"\\end\{\4\}",
    re.DOTALL,
)
LABEL_RE = re.compile(r"\\(?:label|ref|eqref|autoref)\{([^}]+)\}")
CITE_RE = re.compile(r"\\cite[a-zA-Z*]*\{([^}]+)\}|\[@([^\]]+)\]")
TEX_STRUCTURE_RE = re.compile(
    r"\\(part|chapter|section|subsection|subsubsection|paragraph|"
    r"begin|end|theoremstyle|newtheorem)\b(?:\{([^}]+)\})?"
)
MD_HEADING_RE = re.compile(r"^(#{1,6})\s+", re.MULTILINE)
FENCE_RE = re.compile(r"^```[^\n]*\n(.*?)^```\s*$", re.MULTILINE | re.DOTALL)
NUMBER_RE = re.compile(r"(?<![A-Za-z])[-+]?\d+(?:[.,]\d+)?(?:[eE][-+]?\d+)?")
STATUS_RE = re.compile(
    r"\b(?:GAP-[A-Za-z0-9*_-]+|OPEN|NARROWED|CLOSED(?:\s+CONDITIONALLY)?|"
    r"PROVED|UNPROVED|SPECULATIVE|HISTORICAL|L[0-9])\b"
)
UNIT_RE = re.compile(r"BILINGUAL-UNIT:\s*([A-Za-z0-9_.:-]+)")
PROVENANCE_RE = re.compile(
    r"^<!--\nUBT-AI-PROVENANCE-BEGIN\n.*?^UBT-AI-PROVENANCE-END\n-->\n?"
    r"|^% UBT-AI-PROVENANCE-BEGIN\n.*?^% UBT-AI-PROVENANCE-END\n?",
    re.MULTILINE | re.DOTALL,
)


def compact(value: str) -> str:
    return re.sub(r"\s+", "", value)


def matches(pattern: re.Pattern[str], text: str) -> list[str]:
    result: list[str] = []
    for match in pattern.finditer(text):
        groups = [group for group in match.groups() if group is not None]
        result.append("|".join(compact(group) for group in groups))
    return result


@dataclass(frozen=True)
class Signature:
    units: tuple[str, ...]
    structure: tuple[str, ...]
    math: tuple[str, ...]
    labels: tuple[str, ...]
    citations: tuple[str, ...]
    code: tuple[str, ...]
    numbers: tuple[str, ...]
    statuses: tuple[str, ...]


def signature(path: Path) -> Signature:
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".tex":
        structure = []
        for match in TEX_STRUCTURE_RE.finditer(text):
            command, argument = match.groups()
            structure.append(
                command if command in {"part", "chapter", "section", "subsection", "subsubsection", "paragraph"}
                else f"{command}|{compact(argument or '')}"
            )
        code: list[str] = []
    else:
        structure = [str(len(marker)) for marker in MD_HEADING_RE.findall(text)]
        code = [compact(block) for block in FENCE_RE.findall(text)]
    return Signature(
        units=tuple(UNIT_RE.findall(text)),
        structure=tuple(structure),
        math=tuple(matches(MATH_RE, text)),
        labels=tuple(LABEL_RE.findall(text)),
        citations=tuple(matches(CITE_RE, text)),
        code=tuple(code),
        numbers=tuple(NUMBER_RE.findall(text)),
        statuses=tuple(STATUS_RE.findall(text)),
    )


def pair_for(path: Path) -> Path | None:
    match = LANG_RE.match(path.name)
    if not match:
        return None
    other = "cs" if match.group("lang") == "en" else "en"
    return path.with_name(f"{match.group('stem')}.{other}{match.group('suffix')}")


def excluded(path: Path) -> bool:
    return any(part in EXCLUDED_PARTS for part in path.parts)


def all_pairs(root: Path) -> set[tuple[Path, Path]]:
    pairs: set[tuple[Path, Path]] = set()
    for path in root.rglob("*"):
        if not path.is_file() or excluded(path.relative_to(root)):
            continue
        other = pair_for(path)
        if other is not None:
            en = path if ".en." in path.name else other
            cs = path if ".cs." in path.name else other
            pairs.add((en, cs))
    return pairs


def governed_content(text: str) -> str:
    """Ignore generated provenance metadata, not the surrounding source prose.

    Header normalization has its own fail-closed provenance gate. Adding that
    generated metadata alone does not materially edit a legacy document and
    must not turn the bilingual migration policy into an unrelated PR blocker.
    """
    text = PROVENANCE_RE.sub("", text)
    # Inserting a marker after an existing copyright comment can add a blank
    # separator there. Preserve the comment itself, while ignoring that gap.
    text = re.sub(r"(?m)^(<!-- © [^\n]* -->)\n(?:[ \t]*\n)+", r"\1\n", text)
    return re.sub(r"\n(?:[ \t]*\n)+", "\n\n", text).strip()


def changed_paths(root: Path, base: str) -> list[Path]:
    comparison_base = subprocess.check_output(
        ["git", "merge-base", base, "HEAD"], cwd=root, text=True
    ).strip()
    command = [
        "git", "diff", "--name-only", "-z", "--diff-filter=AM",
        comparison_base, "HEAD",
    ]
    output = subprocess.check_output(command, cwd=root, text=True)
    paths: list[Path] = []
    for relative in filter(None, output.split("\0")):
        path = root / relative
        if path.suffix in TEXT_SUFFIXES:
            previous = subprocess.run(
                ["git", "show", f"{comparison_base}:{relative}"],
                cwd=root, text=True, capture_output=True,
            )
            if previous.returncode == 0 and governed_content(previous.stdout) == governed_content(
                path.read_text(encoding="utf-8")
            ):
                continue
        paths.append(path)
    return paths


def check_pair(en: Path, cs: Path) -> list[str]:
    errors: list[str] = []
    if not en.is_file() or not cs.is_file():
        missing = en if not en.is_file() else cs
        return [f"missing language pair: {missing}"]
    en_sig, cs_sig = signature(en), signature(cs)
    for field in Signature.__dataclass_fields__:
        if getattr(en_sig, field) != getattr(cs_sig, field):
            errors.append(f"{field} mismatch: {en} != {cs}")
    return errors


def language_router(path: Path) -> bool:
    """Accept only prose-free legacy entry points resolving to a complete pair.

    This does not exempt the target editions from structural/semantic review.
    No scientific assertion, arbitrary TeX command or extra link is allowed.
    """
    text = governed_content(path.read_text(encoding="utf-8"))
    text = re.sub(r"(?m)^%[^\n]*$", "", text).strip()
    if path.suffix == ".tex":
        match = re.fullmatch(r"\\input\{([A-Za-z0-9_-]+)\.en\.tex\}", text)
        if not match:
            return False
        targets = [path.with_name(f"{match[1]}.{lang}.tex") for lang in ("en", "cs")]
    elif path.suffix == ".md":
        match = re.fullmatch(r"- \[en\]\(([A-Za-z0-9_-]+)\.en\.md\)\s*\n- \[cs\]\(\1\.cs\.md\)", text)
        if not match:
            return False
        targets = [path.with_name(f"{match[1]}.{lang}.md") for lang in ("en", "cs")]
    else:
        return False
    return all(target.is_file() for target in targets) and not check_pair(*targets)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--changed-base")
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []

    pairs = all_pairs(root)
    for en, cs in sorted(pairs):
        errors.extend(check_pair(en, cs))

    if args.changed_base:
        for path in changed_paths(root, args.changed_base):
            relative = path.relative_to(root)
            if (
                path.suffix not in TEXT_SUFFIXES
                or excluded(relative)
                or relative.as_posix() in GOVERNANCE_FILES
                or relative.as_posix() in SHARED_LANGUAGE_NEUTRAL_FILES
                or (path.is_file() and language_router(path))
            ):
                continue
            other = pair_for(path)
            if other is None:
                errors.append(
                    f"governed text must use an .en/.cs pair: {relative.as_posix()}"
                )
            else:
                en = path if ".en." in path.name else other
                cs = path if ".cs." in path.name else other
                errors.extend(check_pair(en, cs))

    if errors:
        print("Bilingual document gate failed:", file=sys.stderr)
        for error in sorted(set(errors)):
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Bilingual document gate passed ({len(pairs)} pair(s) checked).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
