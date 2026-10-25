#!/usr/bin/env python3
"""Run the scoped Hamiltonian/charge/torsion checks without optional test plugins.

These checks cover conditional statements only, not the full UBT action.
"""
from pathlib import Path
import runpy
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def main():
    suite = unittest.TestSuite()
    directory = ROOT / "research_tracks/action_selection/tests"
    for name in (
        "test_dirac_symplectic_pullback.py",
        "test_dirac_positive_pullback.py",
        "test_desitter_trace_matching.py",
        "test_torsion_trace_dirac_flux.py",
        "test_torsion_trace_integrating_factor.py",
    ):
        suite.addTests(unittest.defaultTestLoader.discover(str(directory), pattern=name))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        return 1
    count = 0
    for relative in (
        "tests/test_phase_central_metric_compatibility.py",
        "tests/test_psi_mode_weak_obstruction.py",
    ):
        for name, function in runpy.run_path(str(ROOT / relative)).items():
            if name.startswith("test_") and callable(function):
                function()
                count += 1
                print("PASS", name)
    print(f"PASS: {result.testsRun + count} focused tests; no claim of full UBT dynamics.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
