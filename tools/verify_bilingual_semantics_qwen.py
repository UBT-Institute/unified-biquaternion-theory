#!/usr/bin/env python3
"""Experimental local Qwen backend for the existing fail-closed bilingual verifier."""
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
LOCAL_MAX_PARAGRAPHS = 12
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

class OllamaReviewer:
    last_response = None
    def __init__(self, model=None, timeout=600):
        self.model, self.timeout = model or os.environ.get("OLLAMA_MODEL", "qwen2.5:7b"), timeout
        self.calls = 0
    def __call__(self, batch):
        # Small local models omit reviews in multi-pair requests. Review each
        # pair independently, validate it immediately, then combine evidence.
        if len(batch) > 1:
            reviews = []
            for item in batch:
                raw = self([item])
                reviews.extend(v.validate_response(raw, [item]))
            return json.dumps({"schema": v.SCHEMA, "reviews": reviews}, ensure_ascii=False)
        # Constrain source identifiers and hashes to the exact input batch.
        # Never repair or overwrite model-generated evidence after decoding.
        schema=json.loads(json.dumps(REVIEW_SCHEMA))
        schema["properties"]["reviews"]["items"]["properties"]["id"]["enum"]=[item["id"] for item in batch]
        for lang in ("en", "cs"):
            schema["properties"]["reviews"]["items"]["properties"][f"{lang}_sha256"]["enum"]=[item[f"{lang}_sha256"] for item in batch]
        # A single-paragraph pair has exactly one valid alignment on each side.
        # Constrain identifiers at decoding time rather than repairing model output.
        # Multi-paragraph pairs retain the original strict coverage validator.
        item = batch[0]
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
        print(f"Ollama request {self.calls}: {item['id']} ({len(item['en'])}/{len(item['cs'])} paragraphs)",flush=True)
        req=urllib.request.Request("http://127.0.0.1:11434/api/generate",
                                   payload,{"Content-Type":"application/json"})
        try:
            with urllib.request.urlopen(req,timeout=self.timeout) as response:
                result=json.load(response)
        except Exception as exc:
            raise v.ReviewError(f"local Ollama unavailable: {type(exc).__name__}") from exc
        if not result.get("done") or not result.get("response"):
            raise v.ReviewError("incomplete local model response")
        self.last_response = result["response"]
        return self.last_response

def main():
    root=Path(".").resolve()
    all_pairs='--all-pairs' in sys.argv[1:]
    base=next((arg for arg in sys.argv[1:] if not arg.startswith('--')),None)
    if all_pairs and base:
        raise SystemExit('Choose either --all-pairs or a changed-base SHA')
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
        docs=v.load_documents(root,None if all_pairs else base)
        report["sources"]=[{k:value for k,value in item.items() if k not in ("en","cs")} for item in docs]
        reviewer=OllamaReviewer()
        try:
            v.run_review(docs,reviewer,report,workers=1,
                         max_batch_chars=LOCAL_MAX_CHARS,max_paragraphs=LOCAL_MAX_PARAGRAPHS)
        except v.ReviewError:
            # Keep raw model evidence for debugging, never convert invalid output to approval.
            if reviewer.last_response is not None:
                report['invalid_model_response']=reviewer.last_response[:16000]
            raise
        finally:
            report["model_requests"] = reviewer.calls
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
