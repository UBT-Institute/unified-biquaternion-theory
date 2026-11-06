#!/usr/bin/env python3
"""Verify Tier-A bytes against the recorded author-reviewed Git revision."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
MAX_AGE_DAYS = 90


def attestation_errors(root: Path, today: date) -> list[str]:
    policy = yaml.safe_load((root / "PROVENANCE_TIERS.yaml").read_text(encoding="utf-8"))
    record = json.loads((root / ".github/tier_a_attestation.json").read_text(encoding="utf-8"))
    revision = record["reviewed_commit"]
    if not isinstance(revision, str) or not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("reviewed_commit must be a full Git commit SHA")
    signer = str(policy.get("signed_off_by") or "")
    if not signer or signer.upper().startswith("PENDING") or not policy.get("signed_off_date"):
        raise ValueError("Tier-A author sign-off is pending")

    attested = date.fromisoformat(str(policy["attested_as_of"]))
    age = (today - attested).days
    errors = []
    if age < 0:
        errors.append(f"Tier-A attestation is dated in the future ({attested})")
    elif age > MAX_AGE_DAYS:
        errors.append(f"Tier-A attestation is {age} days old; author review required")

    ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", revision, "HEAD"],
        cwd=root,
        capture_output=True,
    )
    if ancestor.returncode:
        errors.append(f"Reviewed commit {revision} is unavailable or outside HEAD history")
        return errors

    for relative in policy["tiers"]["A_attested"]:
        candidate = root / relative
        if Path(relative).is_absolute() or ".." in Path(relative).parts:
            raise ValueError(f"Invalid Tier-A path: {relative!r}")
        reviewed = subprocess.run(
            ["git", "show", f"{revision}:{relative}"],
            cwd=root,
            capture_output=True,
        )
        if reviewed.returncode or not candidate.is_file():
            errors.append(f"Tier-A path missing from checkout or reviewed revision: {relative}")
        elif reviewed.stdout != candidate.read_bytes():
            errors.append(f"Tier-A content changed since reviewed revision: {relative}")
    return errors


def main() -> int:
    try:
        errors = attestation_errors(ROOT, date.today())
    except (OSError, KeyError, TypeError, ValueError, yaml.YAMLError) as exc:
        errors = [str(exc)]
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        print(
            "Publication requires author review of the exact Tier-A contents, "
            "a current attestation date, and the reviewed commit in "
            ".github/tier_a_attestation.json.",
            file=sys.stderr,
        )
        return 1
    print("Tier-A contents match the current author attestation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
