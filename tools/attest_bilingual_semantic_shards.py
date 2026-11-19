#!/usr/bin/env python3
"""Attest all Qwen CI shards against one exact checkout, failing closed."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import verify_bilingual_semantics as v
import verify_bilingual_semantics_qwen as q


def attest(root: Path, artifact_dir: Path, base: str | None, expected_shards: int) -> dict:
    if not 1 <= expected_shards <= 16:
        raise v.ReviewError("invalid shard count")
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    documents = v.load_documents(root, base)
    all_units, assignments = q.shard_review_units(documents, expected_shards)
    manifest = [
        {"id": part["id"], "en_sha256": part["en_sha256"], "cs_sha256": part["cs_sha256"]}
        for part in all_units
    ]
    manifest_sha = v.sha256(
        json.dumps(manifest, sort_keys=True, ensure_ascii=False).encode("utf-8")
    )
    expected_verifier_sha = v.sha256(Path(v.__file__).read_bytes())
    expected_backend_sha = v.sha256(Path(q.__file__).read_bytes())
    expected_structure_sha = v.sha256(Path(v.parity.__file__).read_bytes())
    expected_policy_sha = {
        name: v.sha256((root / name).read_bytes())
        for name in ("BILINGUAL_CONTENT_POLICY.en.md", "BILINGUAL_CONTENT_POLICY.cs.md", "AGENTS.md")
    }
    calibration, calibration_expectation = v.calibration()
    reports = list(artifact_dir.glob("*/qwen-semantic-review.json"))
    if len(reports) != expected_shards:
        raise v.ReviewError(
            f"expected {expected_shards} shard artifacts, found {len(reports)}"
        )
    seen = set()
    details = []
    for path in sorted(reports):
        report = json.loads(path.read_text(encoding="utf-8"))
        shard_info = report.get("sharding", {})
        index = shard_info.get("index")
        if type(index) is not int or index not in range(expected_shards) or index in seen:
            raise v.ReviewError("missing, duplicate or invalid semantic shard")
        seen.add(index)
        subset = assignments[index]
        if (
            report.get("status") != "passed"
            or report.get("schema") != v.SCHEMA
            or report.get("commit") != commit
            or shard_info.get("count") != expected_shards
            or shard_info.get("manifest_sha256") != manifest_sha
            or shard_info.get("original_pair_count") != len(documents)
            or shard_info.get("total_review_units") != len(all_units)
            or shard_info.get("selected_review_units") != len(subset)
            or report.get("verifier_sha256") != expected_verifier_sha
            or report.get("backend_sha256") != expected_backend_sha
            or report.get("structure_verifier_sha256") != expected_structure_sha
            or report.get("prompt_sha256") != v.sha256(v.PROMPT.encode())
            or report.get("policy_sha256") != expected_policy_sha
        ):
            raise v.ReviewError(f"shard {index} has stale or mismatched provenance")
        expected_sources = [
            {k: value for k, value in part.items() if k not in ("en", "cs")}
            for part in subset
        ]
        if report.get("sources") != expected_sources:
            raise v.ReviewError(f"shard {index} changed or omitted source units")
        calibration_data = report.get("calibration", {})
        if calibration_data.get("status") != "passed":
            raise v.ReviewError(f"shard {index} did not pass calibration")
        calibration_reviews = v.validate_response(
            json.dumps({"schema": v.SCHEMA, "reviews": calibration_data.get("reviews")}),
            calibration,
        )
        if any(r["verdict"] != calibration_expectation[r["id"]] for r in calibration_reviews):
            raise v.ReviewError(f"shard {index} failed independent calibration")
        reviews = v.validate_response(
            json.dumps({"schema": v.SCHEMA, "reviews": report.get("reviews")}), subset
        ) if subset else []
        if len(reviews) != len(subset) or any(r["verdict"] != "pass" for r in reviews):
            raise v.ReviewError(f"shard {index} contains uncertainty or incomplete review")
        for part in subset:
            for lang, source_path in part["paths"].items():
                if v.sha256((root / source_path).read_bytes()) != part[f"{lang}_sha256"]:
                    raise v.ReviewError(f"source mutated: {source_path}")
        details.append({
            "index": index,
            "review_units": len(subset),
            "model": report.get("model"),
            "calibration": "passed",
        })
    if seen != set(range(expected_shards)):
        raise v.ReviewError("not all required semantic shards were attested")
    models = {record["model"] for record in details}
    if len(models) != 1 or not next(iter(models)):
        raise v.ReviewError("semantic shards used different or absent models")
    return {
        "schema": "ubt-bilingual-semantic-attestation/v1",
        "status": "passed",
        "commit": commit,
        "base": base,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "manifest_sha256": manifest_sha,
        "source_pairs": len(documents),
        "review_units": len(all_units),
        "model": next(iter(models)),
        "shards": sorted(details, key=lambda record: record["index"]),
        "notice": "Machine-reviewed EN/CS meaning, not a proof of scientific validity.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--artifacts", type=Path, required=True)
    parser.add_argument("--base")
    parser.add_argument("--shard-count", type=int, default=12)
    parser.add_argument("--output", type=Path, default=Path("build/bilingual/semantic-attestation.json"))
    args = parser.parse_args()
    try:
        result = attest(args.root.resolve(), args.artifacts.resolve(), args.base, args.shard_count)
    except (v.ReviewError, OSError, ValueError, subprocess.SubprocessError, KeyError, TypeError) as error:
        print(f"Qwen shard attestation BLOCKED: {error}", file=sys.stderr)
        return 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Qwen semantic attestation PASSED: {result['review_units']} review units "
          f"across {len(result['shards'])} shards and {result['source_pairs']} source pairs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
