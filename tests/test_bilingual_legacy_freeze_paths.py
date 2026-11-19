"""Frozen bilingual migration debt must not become a semantic-review bypass."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "bilingual_semantics_legacy_test", ROOT / "tools/verify_bilingual_semantics.py"
)
assert SPEC and SPEC.loader
SEM = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SEM)


def git(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=root, text=True).strip()


def commit(root: Path) -> str:
    git(root, "add", ".")
    git(root, "-c", "user.name=Test", "-c", "user.email=gate@example.invalid",
        "commit", "-qm", "test fixture")
    return git(root, "rev-parse", "HEAD")


def inventory(root: Path, path: Path) -> None:
    rel = path.relative_to(root).as_posix()
    entry = {
        "existing": rel,
        "expected": rel.replace(".en.md", ".cs.md"),
        "git_blob_sha": git(root, "hash-object", rel),
    }
    target = root / "reports/bilingual_legacy_gap_freeze_2026_11_19.json"
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps({
        "schema": "ubt-frozen-legacy-unpaired/v1",
        "count": 1, "entries": [entry],
    }), encoding="utf-8")


def fixture(root: Path) -> tuple[Path, Path]:
    git(root, "init", "-q")
    textbook = root / "docs/textbook"
    textbook.mkdir(parents=True)
    (textbook / "chapter.en.md").write_text("# Chapter\n\\[x=1\\]\n")
    (textbook / "chapter.cs.md").write_text("# Kapitola\n\\[x=1\\]\n")
    legacy = textbook / "legacy.en.md"
    legacy.write_text("# Historical\n\nOriginal claim.\n")
    inventory(root, legacy)
    return textbook, legacy


def test_scoped_textbook_gate_uses_repository_ledger_and_checks_hash(tmp_path: Path) -> None:
    textbook, legacy = fixture(tmp_path)
    commit(tmp_path)
    args = [sys.executable, str(ROOT / "tools/check_bilingual_pairs.py"),
            "--root", str(textbook)]
    valid = subprocess.run(args, cwd=tmp_path, capture_output=True, text=True)
    assert valid.returncode == 0, valid.stderr
    assert "1 exact-content-frozen" in valid.stdout

    legacy.write_text("# Historical\n\nChanged claim.\n")
    invalid = subprocess.run(args, cwd=tmp_path, capture_output=True, text=True)
    assert invalid.returncode != 0
    assert "missing language pair" in invalid.stderr


def test_semantic_gate_defers_only_metadata_changes_not_substantive_changes(tmp_path: Path) -> None:
    _, legacy = fixture(tmp_path)
    base = commit(tmp_path)
    header = ("<!--\nUBT-AI-PROVENANCE-BEGIN\n"
              "schema: ubt-ai-provenance/v1\n"
              "tier: C_working\nUBT-AI-PROVENANCE-END\n-->\n\n")
    legacy.write_text(header + legacy.read_text())
    inventory(tmp_path, legacy)
    commit(tmp_path)

    # No translation approval is issued for the unpaired historical text.
    assert SEM.load_documents(tmp_path, base) == []

    # Even an updated inventory SHA cannot bless a changed scientific claim.
    legacy.write_text(header + "# Historical\n\nDifferent scientific claim.\n")
    inventory(tmp_path, legacy)
    commit(tmp_path)
    with pytest.raises(SEM.ReviewError, match="substantively changed"):
        SEM.load_documents(tmp_path, base)
