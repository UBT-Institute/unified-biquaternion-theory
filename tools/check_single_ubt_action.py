#!/usr/bin/env python3
"""Reject competing DECLARATIONS of S_UBT, not prose references.
The authoritative file currently defines S_Theta (a FAMILY), not a finalized
S_UBT. Therefore zero S_UBT declarations is legal until the ADR is accepted.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = Path("canonical/THEORY/canonical/canonical_action.tex")
SKIP = {".git", ".venv", "venv", "node_modules", "__pycache__", ".pytest_cache", "build", "dist"}
EXT = {".tex", ".md", ".py"}
# Structured declaration forms only; ordinary text "S_UBT" and formula references
# without explicit declaration marker are intentionally ignored.
MARK = re.compile(r"(?m)^\s*(?:\\(?:newcommand|def|DeclareMathOperator)\s*\{?\\S_UBT\}?|(?:fundamental_action\s*[:=]\s*|DEFINE_S_UBT\s*[:=]\s*)S_UBT\b|\\underbrace\{S_UBT\}.*%\s*UBT_ACTION_DEFINITION)")
def declarations(relative: Path, data: str) -> list[int]:
    return [data.count("\n", 0, m.start()) + 1 for m in MARK.finditer(data)]
def scan(root: Path = ROOT) -> list[str]:
    errors = []
    for file in root.rglob("*"):
        if not file.is_file() or file.suffix not in EXT or any(p in SKIP for p in file.parts):
            continue
        rel = file.relative_to(root)
        content = file.read_text(encoding="utf-8", errors="replace")
        if rel == Path("tools/check_single_ubt_action.py"):
            continue
        for line in declarations(rel, content):
            if rel != CANONICAL:
                errors.append(f"{rel}:{line}: S_UBT declaration outside {CANONICAL}")
    return errors
if __name__ == "__main__":
    problems = scan()
    for issue in problems: print(issue, file=sys.stderr)
    print("Single-action declaration gate: " + ("FAIL" if problems else "PASS"))
    raise SystemExit(bool(problems))
