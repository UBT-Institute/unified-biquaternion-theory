"""Local inference bounds must preserve every paragraph and fail closed.

Protocol fixtures below test transport/coverage only, never certify an actual
translation or stand in for the independent model's calibration.
"""
from __future__ import annotations

import importlib.util
import io
import json
from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("qwen_limits", ROOT / "tools/verify_bilingual_semantics_qwen.py")
QWEN = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(QWEN)
V = QWEN.v


def sample(count=2):
    return V.document("fixture.en.md", "\n\n".join(f"Statement {n}." for n in range(count)).encode(),
                      "\n\n".join(f"Výrok {n}." for n in range(count)).encode())


def model_fixture(item):
    return {"schema": V.SCHEMA, "reviews": [{
        "id": item["id"], "en_sha256": item["en_sha256"], "cs_sha256": item["cs_sha256"],
        "verdict": "pass", "checks": {key: True for key in V.CHECKS},
        "alignments": [{"en": [p["id"] for p in item["en"]],
                        "cs": [p["id"] for p in item["cs"]], "verdict": "pass", "reason": "fixture"}],
    }]}


def test_local_chunking_keeps_raw_hashes_and_all_paragraphs_exactly_once():
    item = sample(37)
    parts = V.split_oversized_pair(item, max_chars=QWEN.LOCAL_MAX_CHARS,
                                   max_paragraphs=QWEN.LOCAL_MAX_PARAGRAPHS)
    assert len(parts) == 7
    for lang in ("en", "cs"):
        assert [p for part in parts for p in part[lang]] == item[lang]
        assert all(part[f"{lang}_sha256"] == item[f"{lang}_sha256"] for part in parts)
    assert all(len(V.make_prompt([part])) <= QWEN.LOCAL_MAX_CHARS for part in parts)
    assert all(max(len(p["en"]), len(p["cs"])) <= QWEN.LOCAL_MAX_PARAGRAPHS for p in parts)


def test_unequal_paragraph_split_and_oversized_single_paragraph_fail_closed():
    item = sample(20)
    item["cs"].pop()
    with pytest.raises(V.ReviewError, match="split into paired sources"):
        V.split_oversized_pair(item, max_paragraphs=12)
    item = V.document("oversized", b"x"*30000, b"y"*30000)
    with pytest.raises(V.ReviewError, match="split into paired sources"):
        V.split_oversized_pair(item, max_chars=24000)


def test_schema_bounds_identifiers_not_the_model_verdict(monkeypatch):
    item, requests = sample(), []

    def urlopen(req, timeout):
        requests.append(json.loads(req.data))
        return io.BytesIO(json.dumps({"done": True, "response": json.dumps(model_fixture(item))}).encode())

    monkeypatch.setattr(QWEN.urllib.request, "urlopen", urlopen)
    reviewer = QWEN.OllamaReviewer()
    V.validate_response(reviewer([item]), [item])
    payload = requests[0]
    assert payload["options"]["num_predict"] == 4096
    review = payload["format"]["properties"]["reviews"]
    assert review["minItems"] == review["maxItems"] == 1
    assert review["items"]["properties"]["verdict"]["enum"] == ["pass", "fail", "uncertain"]
    for lang in ("en", "cs"):
        ids = review["items"]["properties"]["alignments"]["items"]["properties"][lang]
        assert ids["items"]["enum"] == [p["id"] for p in item[lang]]
        assert ids["uniqueItems"] is True


def test_actual_network_budget_counts_each_recursive_pair(monkeypatch):
    item, requests = sample(), []

    def urlopen(req, timeout):
        requests.append(req)
        return io.BytesIO(json.dumps({"done": True, "response": json.dumps(model_fixture(item))}).encode())

    monkeypatch.setattr(QWEN.urllib.request, "urlopen", urlopen)
    monkeypatch.setattr(V, "MAX_CALLS", 1)
    with pytest.raises(V.ReviewError, match="request budget"):
        QWEN.OllamaReviewer()([item, item])
    assert len(requests) == 1


def test_timeout_and_unbounded_request_cannot_issue_approval(monkeypatch):
    def timeout(*args, **kwargs):
        raise TimeoutError("fixture")

    monkeypatch.setattr(QWEN.urllib.request, "urlopen", timeout)
    reviewer = QWEN.OllamaReviewer()
    with pytest.raises(V.ReviewError, match="TimeoutError"):
        reviewer([sample()])
    with pytest.raises(V.ReviewError, match="paragraph budget"):
        reviewer([sample(13)])
    assert reviewer.last_response is None


@pytest.mark.parametrize("failure", ["incomplete", "duplicate", "timeout"])
def test_retry_reviews_every_paragraph_with_fresh_model_evidence(monkeypatch, failure):
    item = sample(4)
    requests = []

    def request(part):
        requests.append(part)
        if len(requests) == 1 and failure == "timeout":
            raise QWEN.InferenceTimeout("fixture timeout")
        result = model_fixture(part)
        alignment = result["reviews"][0]["alignments"][0]
        if len(requests) == 1:
            if failure == "incomplete":
                alignment["en"].pop()
            else:
                alignment["en"].append(alignment["en"][0])
        return json.dumps(result)

    reviewer = QWEN.OllamaReviewer()
    monkeypatch.setattr(reviewer, "_request", request)
    review, = V.validate_response(reviewer([item]), [item])
    assert review["verdict"] == "pass"
    assert [len(request["en"]) for request in requests] == [4, 2, 2]
    assert reviewer.retry_partitions[0]["parts"] == [request["id"] for request in requests[1:]]
    for lang in ("en", "cs"):
        assert all(request[f"{lang}_sha256"] == item[f"{lang}_sha256"] for request in requests)
        assert [value for part in review["alignments"] for value in part[lang]] == [
            paragraph["id"] for paragraph in item[lang]
        ]


@pytest.mark.parametrize("verdict", ["fail", "uncertain"])
def test_retry_does_not_discard_an_existing_negative_verdict(monkeypatch, verdict):
    item = sample(4)
    result = model_fixture(item)
    review = result["reviews"][0]
    review["verdict"] = verdict
    review["alignments"][0]["en"].pop()
    reviewer = QWEN.OllamaReviewer()
    monkeypatch.setattr(reviewer, "_request", lambda part: json.dumps(result))
    with pytest.raises(V.ReviewError, match="coverage"):
        reviewer([item])
    assert reviewer.retry_partitions == []


def test_uncertain_retry_part_keeps_original_document_unapproved(monkeypatch):
    item = sample(4)
    requests = []

    def request(part):
        requests.append(part)
        result = model_fixture(part)
        review = result["reviews"][0]
        if len(requests) == 1:
            review["alignments"][0]["en"].pop()
        if len(requests) == 2:
            review["verdict"] = "uncertain"
            review["checks"]["claims"] = False
            review["alignments"][0].update(verdict="uncertain", reason="Ambiguous claim")
        return json.dumps(result)

    reviewer = QWEN.OllamaReviewer()
    monkeypatch.setattr(reviewer, "_request", request)
    review, = V.validate_response(reviewer([item]), [item])
    assert review["verdict"] == "uncertain"
    assert review["checks"]["claims"] is False
