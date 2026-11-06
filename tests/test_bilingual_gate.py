"""Keep provenance maintenance distinct from substantive bilingual edits."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import subprocess
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "bilingual_gate", ROOT / "tools/check_bilingual_pairs.py"
)
assert SPEC and SPEC.loader
GATE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = GATE
SPEC.loader.exec_module(GATE)


def git(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=root, text=True).strip()


def commit(root: Path) -> str:
    git(root, "add", ".")
    git(
        root, "-c", "user.name=Gate Test", "-c", "user.email=gate@example.invalid",
        "commit", "-qm", "fixture",
    )
    return git(root, "rev-parse", "HEAD")


@pytest.mark.parametrize("suffix,prefix", [("md", ""), ("tex", "% ")])
def test_header_only_maintenance_is_not_a_prose_edit(tmp_path: Path, suffix: str, prefix: str) -> None:
    git(tmp_path, "init", "-q")
    path = tmp_path / f"legacy.{suffix}"
    original = "Existing unpaired migration debt.\n"
    path.write_text(original, encoding="utf-8")
    base = commit(tmp_path)
    marker = "\n".join(
        prefix + line for line in (
            "UBT-AI-PROVENANCE-BEGIN", "schema: ubt-ai-provenance/v1",
            "tier: C_working", "UBT-AI-PROVENANCE-END",
        )
    )
    if suffix == "md":
        marker = f"<!--\n{marker}\n-->"
    path.write_text(f"{marker}\n\n{original}", encoding="utf-8")
    commit(tmp_path)
    assert GATE.changed_paths(tmp_path, base) == []

    path.write_text(f"{marker}\n\nA materially different claim.\n", encoding="utf-8")
    commit(tmp_path)
    assert GATE.changed_paths(tmp_path, base) == [path]


def test_new_unpaired_source_still_requires_migration(tmp_path: Path) -> None:
    git(tmp_path, "init", "-q")
    (tmp_path / "seed.py").write_text("", encoding="utf-8")
    base = commit(tmp_path)
    path = tmp_path / "new.en.md"
    path.write_text("# New claim\n", encoding="utf-8")
    commit(tmp_path)
    assert GATE.changed_paths(tmp_path, base) == [path]
    assert GATE.check_pair(path, tmp_path / "new.cs.md") == [
        f"missing language pair: {tmp_path / 'new.cs.md'}"
    ]


def test_generated_separator_after_copyright_is_not_content() -> None:
    copyright_line = "<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->\n"
    original = copyright_line + "# Existing note\n\nSame claim.\n"
    normalized = copyright_line + "\n# Existing note\n\nSame claim.\n"
    assert GATE.governed_content(original) == GATE.governed_content(normalized)
    assert GATE.governed_content(original) != GATE.governed_content(
        normalized.replace("Same claim.", "Different claim.")
    )


def test_equation_drift_remains_a_failure(tmp_path: Path) -> None:
    en, cs = tmp_path / "note.en.md", tmp_path / "note.cs.md"
    en.write_text("# Note\n\\[a=1\\]\n", encoding="utf-8")
    cs.write_text("# Poznámka\n\\[a=2\\]\n", encoding="utf-8")
    assert any(error.startswith("math mismatch:") for error in GATE.check_pair(en, cs))


@pytest.mark.parametrize("suffix,content", [
    ("tex", r"\input{note.en.tex}"),
    ("md", "- [en](note.en.md)\n- [cs](note.cs.md)"),
])
def test_prose_free_router_requires_both_real_editions(tmp_path, suffix, content):
    router = tmp_path / f"note.{suffix}"
    router.write_text(content)
    assert not GATE.language_router(router)
    for lang in ("en", "cs"):
        (tmp_path / f"note.{lang}.{suffix}").write_text("\\[a=1\\]\n")
    assert GATE.language_router(router)
    router.write_text(content + "\nPROVED")
    assert not GATE.language_router(router)
    router.write_text(content)
    (tmp_path / f"note.cs.{suffix}").write_text("\\[a=2\\]\n")
    assert not GATE.language_router(router)
