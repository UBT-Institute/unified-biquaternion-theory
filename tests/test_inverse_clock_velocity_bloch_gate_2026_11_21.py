"""Pytest entrypoints for conditional inverse clock/velocity bridge.

The tester imports the standalone exact SymPy checker by its repository path.
"""
from pathlib import Path
import runpy

SOURCE = (
    Path(__file__).resolve().parents[1]
    / "tools"
    / "verify_inverse_clock_velocity_bloch_gate_2026_11_21.py"
)


def test_clock_relative_speed_spectrum_and_covariance():
    runpy.run_path(str(SOURCE))["test_clock_velocity_spectrum"]()


def test_geometric_null_pure_and_comoving_mixed_distinction():
    runpy.run_path(str(SOURCE))["test_null_pure_and_comoving_mixed"]()


def test_qfi_beltrami_klein_conformal_relation():
    runpy.run_path(str(SOURCE))["test_qfi_klein_conformal_factor"]()
