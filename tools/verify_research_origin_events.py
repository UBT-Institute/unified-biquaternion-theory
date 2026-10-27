#!/usr/bin/env python3
"""Validate public research-origin event records, not the truth of their claims."""
from __future__ import annotations

import datetime as dt
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DIR = ROOT / "provenance" / "events"
TEMPLATE = ROOT / "provenance" / "event_template.json"
MODES = {"human_initiated", "ai_initiated", "iterative_human_ai",
         "independent_rediscovery", "undetermined"}
ATTESTATIONS = {"not_attested", "human_review_recorded_elsewhere"}
ATTRIBUTIONS = {"provisional", "evidence_linked", "undetermined"}
EVENT_TYPES = {"human_proposal", "ai_proposal", "human_critique",
               "ai_critique", "human_architecture_decision", "ai_refinement",
               "human_refinement", "mathematical_derivation", "verification",
               "failed_route", "literature_comparison", "independent_rediscovery",
               "publication_decision", "undetermined"}
EVIDENCE_CLASSES = {"primary_document", "indexed_primary", "repository_artifact",
                    "repository_retrospective", "author_recollection",
                    "discussion_context", "external_publication", "undetermined"}

def validate_record(value: dict) -> list[str]:
    errors = []
    if not isinstance(value, dict):
        return ["root must be an object"]
    if value.get("schema") != "ubt-research-event/v1":
        errors.append("invalid schema")
    try:
        dt.date.fromisoformat(value["recorded_on"])
    except (KeyError, ValueError, TypeError):
        errors.append("recorded_on must be ISO date YYYY-MM-DD")
    for name in ("claim_or_decision_id", "summary"):
        if not isinstance(value.get(name), str) or not value[name].strip():
            errors.append(f"{name} must be nonempty text")
    if value.get("development_mode") not in MODES:
        errors.append("invalid development_mode")
    if value.get("attribution_status") not in ATTRIBUTIONS:
        errors.append("invalid attribution_status")
    if value.get("human_attestation") not in ATTESTATIONS:
        errors.append("human_attestation is not a sign-off field")
    if value.get("private_sources_publicly_disclosed") is not False:
        errors.append("raw private sources cannot be published by the agent")
    evid = value.get("evidence")
    if not isinstance(evid, list):
        errors.append("evidence must be a list")
        evid = []
    ids = set()
    for idx, entry in enumerate(evid):
        if not isinstance(entry, dict):
            errors.append(f"evidence[{idx}] must be an object")
            continue
        key = entry.get("id")
        if not isinstance(key, str) or not key or key in ids:
            errors.append(f"evidence[{idx}] missing or duplicate id")
        else:
            ids.add(key)
        if entry.get("class") not in EVIDENCE_CLASSES:
            errors.append(f"evidence[{idx}] invalid class")
        for field in ("locator", "supports", "limitations"):
            if not isinstance(entry.get(field), str) or not entry[field].strip():
                errors.append(f"evidence[{idx}] missing {field}")
        if not isinstance(entry.get("original_checked"), bool):
            errors.append(f"evidence[{idx}] original_checked must be boolean")
    stages = value.get("stage_events")
    if not isinstance(stages, list):
        errors.append("stage_events must be a list")
        stages = []
    for idx, event in enumerate(stages):
        if not isinstance(event, dict):
            errors.append(f"stage_events[{idx}] must be an object")
            continue
        if event.get("kind") not in EVENT_TYPES:
            errors.append(f"stage_events[{idx}] invalid kind")
        if event.get("actor") not in {"human", "ai", "collaborative", "undetermined"}:
            errors.append(f"stage_events[{idx}] invalid actor")
        if not isinstance(event.get("description"), str) or not event["description"].strip():
            errors.append(f"stage_events[{idx}] missing description")
        links = event.get("evidence_ids", [])
        if not isinstance(links, list) or any(not isinstance(link, str) for link in links):
            errors.append(f"stage_events[{idx}] invalid evidence_ids")
        elif any(link not in ids for link in links):
            errors.append(f"stage_events[{idx}] references unknown evidence id")
    if not isinstance(value.get("rejected_alternatives"), list):
        errors.append("rejected_alternatives must be a list")
    verification = value.get("verification")
    if not isinstance(verification, dict) or verification.get("status") not in {
        "not_checked", "pending", "partial", "verified_with_scope", "failed"}:
        errors.append("verification.status invalid")
    elif not isinstance(verification.get("limitations"), str):
        errors.append("verification.limitations missing")
    if value.get("development_mode") == "independent_rediscovery" and not any(
        x.get("class") == "external_publication" for x in evid if isinstance(x, dict)
    ):
        errors.append("independent_rediscovery requires referenced antecedent publication; otherwise use undetermined")
    return errors

def main() -> int:
    paths = sorted(DIR.glob("*.json")) if DIR.exists() else []
    failures = 0
    for path in paths:
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
            errors = validate_record(value)
        except (ValueError, OSError) as exc:
            errors = [str(exc)]
        for err in errors:
            print(f"{path.relative_to(ROOT)}: {err}", file=sys.stderr)
            failures += 1
    if not paths:
        print("No historical event records yet; only the provisional reconstruction exists.")
    print(f"Validated {len(paths)} event file(s); {failures} validation issue(s).")
    return 1 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
