"""Exact restricted no-dynamics gate for the four-real Theta gradient sector."""
from pathlib import Path
import runpy

SCRIPT = (
    Path(__file__).resolve().parents[3] / "tools"
    / "verify_theta_weighted_gradient_volume_null_lagrangian_2026_11_24.py"
)


def test_generic_jacobian_and_zero_velocity_hessian():
    runpy.run_path(str(SCRIPT))["jacobian_identity_and_zero_velocity_hessian"]()


def test_nonlinear_pullback_and_nonconstant_weight_are_null_lagrangian():
    runpy.run_path(str(SCRIPT))["nonlinear_four_real_piola_weighted_euler"]()


def test_algebraic_torsion_cannot_fix_missing_kinetic_without_derivatives():
    runpy.run_path(str(SCRIPT))["algebraic_contortion_source_selection"]()
