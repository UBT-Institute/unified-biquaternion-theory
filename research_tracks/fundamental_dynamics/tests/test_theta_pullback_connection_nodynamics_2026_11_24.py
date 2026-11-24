"""Exact limited pullback torsion/curvature nondynamics gates."""
from pathlib import Path
import runpy

SCRIPT = (
    Path(__file__).resolve().parents[3] / "tools"
    / "verify_theta_pullback_connection_nodynamics_2026_11_24.py"
)


def test_axial_stabilizer_and_nonzero_invariant():
    runpy.run_path(str(SCRIPT))["axial_stabilizer_and_torsion"]()


def test_nonzero_curvature_without_changing_tetrad_metric():
    runpy.run_path(str(SCRIPT))["curved_connection_with_flat_locked_metric"]()


def test_nonaffine_torsion_square_action_is_null_pullback():
    runpy.run_path(str(SCRIPT))["pullback_torsion_action_zero_bulk_euler"]()
