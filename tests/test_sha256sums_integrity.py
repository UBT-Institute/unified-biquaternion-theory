"""Regression guards for checkout and source archive integrity."""

from io import BytesIO
from pathlib import Path
import subprocess
import sys
from zipfile import ZipFile

import pytest


ROOT = Path(__file__).resolve().parents[1]


def test_sha256sums_manifest_matches_repository_files() -> None:
    subprocess.run(
        [sys.executable, "tools/verify_sha256sums.py", "--quiet"],
        cwd=ROOT,
        check=True,
    )


def test_source_archive_matches_its_manifest_and_inventory(tmp_path: Path) -> None:
    if not (ROOT / ".git").exists():
        pytest.skip("creating a Git source archive requires a checkout")
    archive = subprocess.check_output(["git", "archive", "--format=zip", "HEAD"], cwd=ROOT)
    with ZipFile(BytesIO(archive)) as source:
        source.extractall(tmp_path)

    assert not (tmp_path / "SHA256SUMS_PDFS.txt").exists()
    subprocess.run(
        [sys.executable, "tools/verify_sha256sums.py", "--quiet"],
        cwd=tmp_path,
        check=True,
    )
    inventory = subprocess.check_output(
        [sys.executable, "tools/apply_provenance_headers.py", "--report"],
        cwd=tmp_path,
        text=True,
    )
    assert inventory == (tmp_path / "PROVENANCE_INVENTORY_2026-08-01.txt").read_text(
        encoding="utf-8"
    )
