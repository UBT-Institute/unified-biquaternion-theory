#!/usr/bin/env python3
"""Experimental local Qwen backend for the existing fail-closed bilingual verifier."""
import argparse
import json
import os
import subprocess
import sys
import urllib.request
from pathlib import Path
from datetime import datetime, timezone
sys.path.insert(0, str(Path(__file__).resolve().parent))
import verify_bilingual_semantics as v

LOCAL_MAX_CHARS = 24000
LOCAL_MAX_PARAGRAPHS = 6
LOCAL_MAX_PREDICT = 4096

# Constrain JSON structure at decoding time; semantic checks remain fail-closed.
REVIEW_SCHEMA = {
    "type": "object", "additionalProperties": False,
    "required": ["schema", "reviews"],
    "properties": {
        "schema": {"type": "string", "enum": [v.SCHEMA]},
        "reviews": {"type": "array", "items": {
            "type": "object", "additionalProperties": False,
            "required": ["id", "en_sha256", "cs_sha256", "verdict", "checks", "alignments"],
            "properties": {
                "id": {"type": "string"},
                "en_sha256": {"type": "string"},
                "cs_sha256": {"type": "string"},
                "verdict": {"type": "string", "enum": ["pass", "fail", "uncertain"]},
                "checks": {"type": "object", "additionalProperties": False,
                    "required": list(v.CHECKS),
                    "properties": {key: {"type": "boolean"} for key in v.CHECKS}},
                "alignments": {"type": "array", "items": {
                    "type": "object", "additionalProperties": False,
                    "required": ["en", "cs", "verdict", "reason"],
                    "properties": {
                        "en": {"type": "array", "items": {"type": "string"}},
                        "cs": {"type": "array", "items": {"type": "string"}},
                        "verdict": {"type": "string", "enum": ["pass", "fail", "uncertain"]},
                        "reason": {"type": "string"}
                    }}}
            }}}
    }
}

class InferenceTimeout(v.ReviewError):
    """Ollama did not return a complete response within the request timeout."""


class OllamaReviewer:
    last_response = None
    def __init__(self, model=None, timeout=600):
        self.model, self.timeout = model or os.environ.get("OLLAMA_MODEL", "qwen2.5:7b"), timeout
        self.calls = 0
        self.retry_partitions: list[dict] = []

    def __call__(self, batch: list[dict]) -> str:
        reviews = [self._review_item(item) for item in batch]
        return json.dumps({"schema": v.SCHEMA, "reviews": reviews}, ensure_ascii=False)

    def _review_item(self, item: dict) -> dict:
        try:
            return v.validate_response(self._request(item), [item])[0]
        except (v.ParagraphCoverageError, InferenceTimeout) as error:
            count = len(item["en"])
            if count < 2 or count != len(item["cs"]):
                raise
            parts = v.split_oversized_pair(
                item,
                max_chars=LOCAL_MAX_CHARS,
                max_paragraphs=(count + 1) // 2,
            )
            self.retry_partitions.append({
                "source": item["id"],
                "reason": str(error),
                "parts": [part["id"] for part in parts],
            })

        # The failed request supplies no approval. Each smaller request must
        # independently cover its exact paragraphs against the same raw hashes.
        reviews = [self._review_item(part) for part in parts]
        verdicts = {review["verdict"] for review in reviews}
        verdict = next(value for value in ("fail", "uncertain", "pass") if value in verdicts)
        return {
            "id": item["id"],
            "en_sha256": item["en_sha256"],
            "cs_sha256": item["cs_sha256"],
            "verdict": verdict,
            "checks": {key: all(review["checks"][key] for review in reviews) for key in v.CHECKS},
            "alignments": [alignment for review in reviews for alignment in review["alignments"]],
        }

    def _request(self, item: dict) -> str:
        batch = [item]
        # Constrain source identifiers and hashes to the exact input batch.
        # Never repair or overwrite model-generated evidence after decoding.
        schema=json.loads(json.dumps(REVIEW_SCHEMA))
        schema["properties"]["reviews"]["items"]["properties"]["id"]["enum"]=[item["id"] for item in batch]
        for lang in ("en", "cs"):
            schema["properties"]["reviews"]["items"]["properties"][f"{lang}_sha256"]["enum"]=[item[f"{lang}_sha256"] for item in batch]
        # A single-paragraph pair has exactly one valid alignment on each side.
        # Constrain identifiers at decoding time rather than repairing model output.
        # Multi-paragraph pairs retain the original strict coverage validator.
        schema["properties"]["reviews"]["minItems"] = 1
        schema["properties"]["reviews"]["maxItems"] = 1
        alignment = schema["properties"]["reviews"]["items"]["properties"]["alignments"]
        alignment["minItems"] = 1
        alignment["maxItems"] = len(item["en"]) + len(item["cs"])
        for lang in ("en", "cs"):
            ids = alignment["items"]["properties"][lang]
            ids["items"]["enum"] = [p["id"] for p in item[lang]]
            ids["maxItems"] = len(item[lang])
            ids["uniqueItems"] = True
        if len(item["en"]) == 1 and len(item["cs"]) == 1:
            alignment = schema["properties"]["reviews"]["items"]["properties"]["alignments"]
            alignment["minItems"] = 1
            alignment["maxItems"] = 1
            for lang in ("en", "cs"):
                ids = alignment["items"]["properties"][lang]
                ids["minItems"] = 1
                ids["maxItems"] = 1
                ids["items"]["enum"] = [item[lang][0]["id"]]
        payload=json.dumps({"model":self.model,"prompt":v.make_prompt(batch),
                            "stream":False,"format":schema,
                            "options":{"temperature":0,"num_ctx":16384,"num_predict":LOCAL_MAX_PREDICT}}).encode()
        if len(v.make_prompt(batch)) > LOCAL_MAX_CHARS:
            raise v.ReviewError("local model context budget exceeded; no content truncated")
        if max(len(item["en"]),len(item["cs"])) > LOCAL_MAX_PARAGRAPHS:
            raise v.ReviewError("local model paragraph budget exceeded; split before review")
        if self.calls >= v.MAX_CALLS:
            raise v.ReviewError("local model request budget exceeded; no approval issued")
        self.calls += 1
        self.last_response = None
        print(f"Ollama request {self.calls}: {item['id']} ({len(item['en'])}/{len(item['cs'])} paragraphs)",flush=True)
        req=urllib.request.Request("http://127.0.0.1:11434/api/generate",
                                   payload,{"Content-Type":"application/json"})
        try:
            with urllib.request.urlopen(req,timeout=self.timeout) as response:
                result=json.load(response)
        except TimeoutError as exc:
            raise InferenceTimeout(f"local Ollama unavailable: TimeoutError ({item['id']})") from exc
        except Exception as exc:
            raise v.ReviewError(f"local Ollama unavailable: {type(exc).__name__}") from exc
        if not result.get("done") or not result.get("response"):
            raise v.ReviewError("incomplete local model response")
        self.last_response = result["response"]
        return self.last_response

def shard_review_units(documents: list[dict], shard_count: int) -> tuple[list[dict], list[list[dict]]]:
    """Deterministic, lossless partition of *every* paragraph of every pair.

    Sharding improves CPU review throughput; it never grants an exemption.
    Every shard repeats calibration and verifies exact original source hashes.
    The matrix job succeeds only when every shard succeeds.
    """
    if not 1 <= shard_count <= 16:
        raise v.ReviewError("shard count must be in [1,16]")
    units = []
    for item in documents:
        parts = v.split_oversized_pair(
            item, max_chars=LOCAL_MAX_CHARS, max_paragraphs=LOCAL_MAX_PARAGRAPHS,
        )
        for language in ("en", "cs"):
            actual = [paragraph for part in parts for paragraph in part[language]]
            if actual != item[language]:
                raise v.ReviewError("sharding lost source paragraphs: " + item["id"])
        units.extend(parts)
    ids = [item["id"] for item in units]
    if len(ids) != len(set(ids)):
        raise v.ReviewError("sharding produced duplicate review-unit IDs")
    groups = [[] for _ in range(shard_count)]
    loads = [0] * shard_count
    ordering = sorted(range(len(units)), key=lambda i: (
        -(len(v.make_prompt([units[i]])) +
          750 * max(len(units[i]["en"]), len(units[i]["cs"]))),
        units[i]["id"],
    ))
    assignments = {}
    for idx in ordering:
        shard = min(range(shard_count), key=lambda k: (loads[k], k))
        assignments[idx] = shard
        loads[shard] += len(v.make_prompt([units[idx]])) + 750 * max(
            len(units[idx]["en"]), len(units[idx]["cs"])
        )
    for idx, item in enumerate(units):
        groups[assignments[idx]].append(item)
    if sorted(item["id"] for group in groups for item in group) != sorted(item["id"] for item in units):
        raise v.ReviewError("incomplete review-unit partition")
    return units, groups


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("base", nargs="?", help="Changed-base commit SHA")
    parser.add_argument("--all-pairs", action="store_true")
    parser.add_argument("--shard-index", type=int, default=0)
    parser.add_argument("--shard-count", type=int, default=1)
    args = parser.parse_args()
    if args.all_pairs and args.base:
        parser.error("Choose either --all-pairs or a changed-base SHA")
    if not 1 <= args.shard_count <= 16 or not 0 <= args.shard_index < args.shard_count:
        parser.error("Invalid shard index/count")
    root = Path(".").resolve()
    all_pairs = args.all_pairs
    base = args.base
    report={"schema":v.SCHEMA,"status":"blocked","verification":"local-machine-review",
            "model":os.environ.get("OLLAMA_MODEL", "qwen2.5:7b"),"cli_version":"none",
            "created_at":datetime.now(timezone.utc).isoformat(),"base":base,
            "sources":[],"reviews":[],"calibration":{"status":"not_run"},
            "verifier_sha256":v.sha256(Path(v.__file__).read_bytes()),
            "backend_sha256":v.sha256(Path(__file__).read_bytes()),
            "request_limits":{"characters":LOCAL_MAX_CHARS,"paragraphs":LOCAL_MAX_PARAGRAPHS,
                              "predicted_tokens":LOCAL_MAX_PREDICT,"calls":v.MAX_CALLS},
            "prompt_sha256":v.sha256(v.PROMPT.encode()),
            "structure_verifier_sha256":v.sha256(Path(v.parity.__file__).read_bytes()),
            "policy_sha256":{}}
    try:
        report["commit"]=subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip()
        for name in ("BILINGUAL_CONTENT_POLICY.en.md","BILINGUAL_CONTENT_POLICY.cs.md","AGENTS.md"):
            report["policy_sha256"][name]=v.sha256((root/name).read_bytes())
        original_docs = v.load_documents(root, None if all_pairs else base)
        all_units, shards = shard_review_units(original_docs, args.shard_count)
        docs = shards[args.shard_index]
        manifest = [{
            "id": item["id"], "en_sha256": item["en_sha256"],
            "cs_sha256": item["cs_sha256"],
        } for item in all_units]
        report["sharding"] = {
            "index": args.shard_index,
            "count": args.shard_count,
            "original_pair_count": len(original_docs),
            "total_review_units": len(all_units),
            "selected_review_units": len(docs),
            "manifest_sha256": v.sha256(
                json.dumps(manifest, sort_keys=True, ensure_ascii=False).encode("utf-8")
            ),
        }
        report["sources"] = [
            {k: value for k, value in item.items() if k not in ("en", "cs")}
            for item in docs
        ]
        print(f"Qwen shard {args.shard_index+1}/{args.shard_count}: "
              f"{len(docs)}/{len(all_units)} source-bound review units", flush=True)
        reviewer=OllamaReviewer()
        try:
            v.run_review(docs,reviewer,report,workers=1,
                         max_batch_chars=LOCAL_MAX_CHARS,max_paragraphs=LOCAL_MAX_PARAGRAPHS)
        except v.ReviewError as error:
            # A valid fail/uncertain semantic judgment must remain blocking, but
            # must not be mislabeled as a malformed model response in diagnostics.
            # Malformed, incomplete or unavailable output also stays fail-closed.
            if not isinstance(error, v.SemanticMismatchError) and reviewer.last_response is not None:
                report['invalid_model_response'] = reviewer.last_response[:16000]
            raise
        finally:
            report["model_requests"] = reviewer.calls
            report["retry_partitions"] = reviewer.retry_partitions
        v.verify_sources(root,docs)
        report["status"]="passed"
    except (v.ReviewError,OSError,UnicodeError,subprocess.SubprocessError,ValueError) as exc:
        report["error"]=str(exc)
        print(f"Qwen semantic gate blocked: {exc}",file=sys.stderr)
    finally:
        # Keep complete, source-bound calibration verdicts for diagnosing model errors.
        # A calibration failure remains blocking; never convert it to approval.
        if report.get("calibration", {}).get("reviews"):
            expected = v.calibration()[1]
            report["calibration"]["mismatches"] = [
                {"id": item["id"], "expected": expected[item["id"]], "observed": item["verdict"]}
                for item in report["calibration"]["reviews"]
                if item["verdict"] != expected[item["id"]]
            ]
        v.write_report(Path("build/bilingual/qwen-semantic-review.json"),report)
    return 0 if report["status"]=="passed" else 1

if __name__=="__main__":
    raise SystemExit(main())
