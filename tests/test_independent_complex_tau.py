"""Reproduce the bounded C5 research calculations without changing evidence."""
from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import sys

import pytest


TRACK = Path(__file__).resolve().parents[1] / "research_tracks" / "independent_complex_tau"


@pytest.mark.parametrize(
    "script, output, expected_count",
    [
        ("verify_c5.py", "c5_verification_results.json", 51),
        ("verify_c5_dynamics.py", "c5_dynamics_results.json", 32),
        ("verify_auxiliary_action.py", "auxiliary_action_results.json", 22),
        ("verify_wave_dynamics.py", "wave_dynamics_results.json", 21),
        ("verify_curvature_waves.py", "curvature_waves_results.json", 33),
    ],
)
def test_exact_research_derivations(tmp_path, script, output, expected_count):
    target = tmp_path / script
    shutil.copyfile(TRACK / script, target)
    completed = subprocess.run(
        [sys.executable, str(target)],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        timeout=180,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr
    result = json.loads((tmp_path / output).read_text(encoding="utf-8"))
    assert result["passed"] is True
    assert result["checks_count"] == expected_count == len(result["checks"])
    assert all(check["passed"] is True for check in result["checks"])
    stored = json.loads((TRACK / output).read_text(encoding="utf-8"))
    assert result["checks"] == stored["checks"]
    if script in {"verify_auxiliary_action.py", "verify_wave_dynamics.py", "verify_curvature_waves.py"}:
        assert {check["channel"] for check in result["checks"]} == {
            "SymPy", "Python Fraction"
        }
