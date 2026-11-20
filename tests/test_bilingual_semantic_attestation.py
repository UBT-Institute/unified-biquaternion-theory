"""Synthetic attestation tests validate evidence plumbing, never translation quality."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "qwen_attestation_test", ROOT / "tools/attest_bilingual_semantic_shards.py"
)
assert SPEC and SPEC.loader
A = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = A
SPEC.loader.exec_module(A)


def valid_review(item, verdict="pass"):
    return {
        "id": item["id"], "en_sha256": item["en_sha256"],
        "cs_sha256": item["cs_sha256"], "verdict": verdict,
        "checks": {key: verdict == "pass" for key in A.v.CHECKS},
        "alignments": [{
            "en": [part["id"] for part in item["en"]],
            "cs": [part["id"] for part in item["cs"]],
            "verdict": verdict, "reason": "" if verdict == "pass" else "Known mismatch",
        }],
    }


def build_fixture(tmp_path, monkeypatch):
    en, cs = b"Claim.", "Tvrzení.".encode()
    (tmp_path / "proof.en.md").write_bytes(en)
    (tmp_path / "proof.cs.md").write_bytes(cs)
    item = A.v.document("proof.en.md", en, cs)
    item["paths"] = {"en": "proof.en.md", "cs": "proof.cs.md"}
    monkeypatch.setattr(A.v, "load_documents", lambda root, base: [item])
    monkeypatch.setattr(A.subprocess, "check_output", lambda *a, **kw: "fixture-commit\n")
    for name in ("BILINGUAL_CONTENT_POLICY.en.md",
                 "BILINGUAL_CONTENT_POLICY.cs.md", "AGENTS.md"):
        (tmp_path / name).write_text("fixture", encoding="utf-8")
    units, shards = A.q.shard_review_units([item], 2)
    manifest = [
        {"id": unit["id"], "en_sha256": unit["en_sha256"],
         "cs_sha256": unit["cs_sha256"]} for unit in units
    ]
    digest = A.v.sha256(
        json.dumps(manifest, sort_keys=True, ensure_ascii=False).encode("utf-8")
    )
    calibration, expected = A.v.calibration()
    calib_reviews = [valid_review(part, expected[part["id"]]) for part in calibration]
    policy_sha = {
        name: A.v.sha256((tmp_path / name).read_bytes())
        for name in ("BILINGUAL_CONTENT_POLICY.en.md",
                     "BILINGUAL_CONTENT_POLICY.cs.md", "AGENTS.md")
    }
    artifacts = tmp_path / "shards"
    for index, subset in enumerate(shards):
        data = {
            "schema": A.v.SCHEMA, "status": "passed", "model": "qwen2.5:7b",
            "commit": "fixture-commit", "prompt_sha256": A.v.sha256(A.v.PROMPT.encode()),
            "verifier_sha256": A.v.sha256(Path(A.v.__file__).read_bytes()),
            "backend_sha256": A.v.sha256(Path(A.q.__file__).read_bytes()),
            "structure_verifier_sha256": A.v.sha256(Path(A.v.parity.__file__).read_bytes()),
            "policy_sha256": policy_sha,
            "sharding": {
                "index": index, "count": 2, "original_pair_count": 1,
                "total_review_units": len(units), "selected_review_units": len(subset),
                "manifest_sha256": digest,
            },
            "sources": [
                {k: value for k, value in part.items() if k not in ("en", "cs")}
                for part in subset
            ],
            "reviews": [valid_review(part) for part in subset],
            "calibration": {"status": "passed", "reviews": calib_reviews},
        }
        folder = artifacts / f"shard-{index}"
        folder.mkdir(parents=True)
        (folder / "qwen-semantic-review.json").write_text(json.dumps(data), encoding="utf-8")
    return artifacts


def test_attestor_accepts_exact_complete_calibrated_evidence(tmp_path, monkeypatch):
    artifacts = build_fixture(tmp_path, monkeypatch)
    result = A.attest(tmp_path, artifacts, base="fixture-base", expected_shards=2)
    assert result["status"] == "passed"
    assert result["source_pairs"] == result["review_units"] == 1
    assert len(result["shards"]) == 2


@pytest.mark.parametrize("damage", ["missing_shard", "bad_calibration", "stale_source",
                                     "wrong_commit", "missing_review"])
def test_attestor_fails_closed_for_missing_or_stale_evidence(tmp_path, monkeypatch, damage):
    artifacts = build_fixture(tmp_path, monkeypatch)
    reports = sorted(artifacts.glob("*/qwen-semantic-review.json"))
    if damage == "missing_shard":
        reports[1].unlink()
    elif damage == "stale_source":
        (tmp_path / "proof.cs.md").write_bytes(b"Changed content")
    else:
        path = reports[0]
        data = json.loads(path.read_text(encoding="utf-8"))
        if damage == "bad_calibration":
            data["calibration"]["status"] = "failed"
        elif damage == "wrong_commit":
            data["commit"] = "stale-head"
        elif damage == "missing_review":
            data["reviews"] = []
        path.write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(A.v.ReviewError):
        A.attest(tmp_path, artifacts, base="fixture-base", expected_shards=2)
