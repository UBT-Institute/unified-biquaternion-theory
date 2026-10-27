#!/usr/bin/env python3
"""Experimental local Qwen backend for the existing fail-closed bilingual verifier."""
import json
import subprocess
import sys
import urllib.request
from pathlib import Path
from datetime import datetime, timezone
sys.path.insert(0, str(Path(__file__).resolve().parent))
import verify_bilingual_semantics as v

class OllamaReviewer:
    def __init__(self, model="qwen2.5:3b", timeout=300):
        self.model, self.timeout = model, timeout
    def __call__(self, batch):
        payload=json.dumps({"model":self.model,"prompt":v.make_prompt(batch),
                            "stream":False,"format":"json",
                            "options":{"temperature":0,"num_ctx":16384,"num_predict":8192}}).encode()
        req=urllib.request.Request("http://127.0.0.1:11434/api/generate",
                                   payload,{"Content-Type":"application/json"})
        try:
            with urllib.request.urlopen(req,timeout=self.timeout) as response:
                result=json.load(response)
        except Exception as exc:
            raise v.ReviewError(f"local Ollama unavailable: {type(exc).__name__}") from exc
        if not result.get("done") or not result.get("response"):
            raise v.ReviewError("incomplete local model response")
        return result["response"]

def main():
    root=Path(".").resolve()
    all_pairs='--all-pairs' in sys.argv[1:]
    base=next((arg for arg in sys.argv[1:] if not arg.startswith('--')),None)
    if all_pairs and base:
        raise SystemExit('Choose either --all-pairs or a changed-base SHA')
    report={"schema":v.SCHEMA,"status":"blocked","verification":"experimental-local-machine-review",
            "model":"qwen2.5:3b","cli_version":"none",
            "created_at":datetime.now(timezone.utc).isoformat(),"base":base,
            "sources":[],"reviews":[],"calibration":{"status":"not_run"},
            "verifier_sha256":v.sha256(Path(v.__file__).read_bytes()),
            "prompt_sha256":v.sha256(v.PROMPT.encode()),
            "structure_verifier_sha256":v.sha256(Path(v.parity.__file__).read_bytes()),
            "policy_sha256":{}}
    try:
        report["commit"]=subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip()
        for name in ("BILINGUAL_CONTENT_POLICY.en.md","BILINGUAL_CONTENT_POLICY.cs.md","AGENTS.md"):
            report["policy_sha256"][name]=v.sha256((root/name).read_bytes())
        docs=v.load_documents(root,None if all_pairs else base)
        report["sources"]=[{k:value for k,value in item.items() if k not in ("en","cs")} for item in docs]
        v.run_review(docs,OllamaReviewer(),report,workers=1)
        v.verify_sources(root,docs)
        report["status"]="passed"
    except (v.ReviewError,OSError,UnicodeError,subprocess.SubprocessError,ValueError) as exc:
        report["error"]=str(exc)
        print(f"Qwen semantic gate blocked: {exc}",file=sys.stderr)
    finally:
        v.write_report(Path("build/bilingual/qwen-semantic-review.json"),report)
    return 0 if report["status"]=="passed" else 1

if __name__=="__main__":
    raise SystemExit(main())
