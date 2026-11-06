"""Regression checks for provenance-aware publication workflows."""
import json
import subprocess
from datetime import date
from pathlib import Path

from tools.verify_release_attestation import attestation_errors

ROOT = Path(__file__).resolve().parent.parent


def test_latex_publication_requires_human_signoff() -> None:
    text = (ROOT / ".github/workflows/latex_build.yml").read_text(encoding="utf-8")
    assert "Enforce signed provenance release gate" in text
    assert "test_tier_map_is_signed_off" in text
    assert "tools/apply_provenance_headers.py --check" in text
    assert "tools/verify_provenance_review.py" in text
    assert "tests/test_provenance_review.py" in text
    assert "poppler-utils" in text


def test_publication_does_not_run_after_failed_gate() -> None:
    text = (ROOT / ".github/workflows/latex_build.yml").read_text(encoding="utf-8")
    publish = text.index("- name: Publish curated canonical PDFs")
    upload = text.index("- name: Upload all successful PDFs")
    block = text[publish:upload]
    assert "if: success()" in block
    assert "verify_pdf_provenance.py --require-all" in block
    assert "regenerate_sha256sums.py" in block
    assert "tools/verify_sha256sums.py --quiet" in block


def test_automated_commit_is_success_only_and_includes_checksums() -> None:
    text = (ROOT / ".github/workflows/latex_build.yml").read_text(encoding="utf-8")
    commit = text.index("- name: Commit report and curated PDFs")
    block = text[commit:]
    assert "if: success() && github.event_name == 'push'" in block
    # Policy: explicit whitelist of exactly two tracked PDFs; general
    # 'git add docs/pdfs' is forbidden because it would stage milestone PDFs.
    assert "git add -f docs/pdfs/UBT_canonical_main.pdf docs/pdfs/UBT_GR_Submission.pdf" in block
    assert "git add docs/pdfs SHA256SUMS.txt" not in block
    assert "if: always() && github.event_name == 'push'" not in block
    assert "git add SHA256SUMS.txt SHA256SUMS_PDFS.txt" in block


def test_publication_verifies_reviewed_bytes_before_commit() -> None:
    text = (ROOT / ".github/workflows/latex_build.yml").read_text(encoding="utf-8")
    gate = text.index("- name: Verify reviewed Tier-A content before publication")
    commit = text.index("- name: Commit report and curated PDFs")
    assert gate < commit
    assert "python3 tools/verify_release_attestation.py" in text[gate:commit]


def test_release_attestation_detects_stale_date_and_content_drift(tmp_path: Path) -> None:
    def git(*args: str) -> str:
        return subprocess.check_output(["git", *args], cwd=tmp_path, text=True).strip()

    policy = tmp_path / "PROVENANCE_TIERS.yaml"
    policy.write_text(
        "signed_off_by: Author\n"
        "signed_off_date: 2026-08-01\n"
        "attested_as_of: 2026-08-01\n"
        "tiers:\n"
        "  A_attested: [PROVENANCE_TIERS.yaml, CLAIMS.yaml]\n",
        encoding="utf-8",
    )
    claims = tmp_path / "CLAIMS.yaml"
    claims.write_text("claim: reviewed\n", encoding="utf-8")
    git("init", "--quiet")
    git("add", "PROVENANCE_TIERS.yaml", "CLAIMS.yaml")
    git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.test",
        "commit", "--quiet", "-m", "Reviewed content")
    record = tmp_path / ".github/tier_a_attestation.json"
    record.parent.mkdir()
    record.write_text(json.dumps({"reviewed_commit": git("rev-parse", "HEAD")}), encoding="utf-8")

    assert attestation_errors(tmp_path, date(2026, 10, 30)) == []
    assert "91 days old" in attestation_errors(tmp_path, date(2026, 10, 31))[0]
    assert "future" in attestation_errors(tmp_path, date(2026, 7, 31))[0]

    claims.write_text("claim: edited\n", encoding="utf-8")
    assert attestation_errors(tmp_path, date(2026, 8, 2)) == [
        "Tier-A content changed since reviewed revision: CLAIMS.yaml"
    ]


def test_full_verify_workflow_installs_yaml_dependency() -> None:
    text = (ROOT / ".github/workflows/verify.yml").read_text(encoding="utf-8")
    assert "pip install -r requirements.txt" in text
    assert "pytest -q" in text


def test_checksum_verification_is_platform_independent() -> None:
    apply_text = (ROOT / "APPLY_AI_PROVENANCE_ART50_2026-08-01.sh").read_text(encoding="utf-8")
    release_text = (ROOT / "APPLY_PROVENANCE_RELEASE_GATE_2026-08-01.sh").read_text(encoding="utf-8")
    workflow = (ROOT / ".github/workflows/latex_build.yml").read_text(encoding="utf-8")
    for text in (apply_text, release_text, workflow):
        assert "tools/verify_sha256sums.py" in text
        assert "sha256sum -c" not in text
