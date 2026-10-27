"""Regression checks for the machine-readable scientific origin event contract."""
import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("origin_events", ROOT / "tools" / "verify_research_origin_events.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def template():
    return json.loads((ROOT / "provenance" / "event_template.json").read_text(encoding="utf-8"))

def test_example_contract():
    assert module.validate_record(template()) == []

def test_no_fabricated_human_approval():
    record = template()
    record["human_attestation"] = "approved_by_author"
    assert any("sign-off" in x for x in module.validate_record(record))

def test_no_unlinked_evidence():
    record = template()
    record["stage_events"][0]["evidence_ids"] = ["fake-evidence"]
    assert any("unknown evidence" in x for x in module.validate_record(record))

def test_rediscovery_needs_antecedent():
    record = template()
    record["development_mode"] = "independent_rediscovery"
    assert any("antecedent publication" in x for x in module.validate_record(record))
    record["evidence"].append({"id": "prior-art", "class": "external_publication",
      "locator": "https://example.org/paper", "supports": "Antecedent identified",
      "limitations": "Not an authorship determination", "original_checked": False})
    assert module.validate_record(record) == []

def test_all_event_files_follow_contract():
    event_dir = ROOT / "provenance" / "events"
    for path in sorted(event_dir.glob("*.json")) if event_dir.exists() else []:
        record = json.loads(path.read_text(encoding="utf-8"))
        assert module.validate_record(record) == [], path.as_posix()
