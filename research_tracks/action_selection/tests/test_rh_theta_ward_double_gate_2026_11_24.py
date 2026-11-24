"""Scoped local Ward/TT-access tests; NOT a physical UBT graviton proof."""
from pathlib import Path
import runpy

SCRIPT = (
    Path(__file__).resolve().parents[3] / "tools"
    / "verify_rh_theta_ward_double_gate_2026_11_24.py"
)


def test_local_selfadjoint_fierz_pauli_ward_selection():
    runpy.run_path(str(SCRIPT))["test_selfadjointness_and_ward_select_fp"]()


def test_no_local_analytic_mass_term_with_metric_gauge_ward():
    runpy.run_path(str(SCRIPT))["test_no_local_analytic_mass_term"]()


def test_nonlocal_spin_two_projector_evades_mass_protection():
    runpy.run_path(str(SCRIPT))["test_transverse_ward_alone_not_mass_protection"]()


def test_isotropic_biquaternion_vector_bilinear_no_linear_metric_gauge_lift():
    runpy.run_path(str(SCRIPT))["test_quadratic_theta_composite_has_no_linear_diff_lift"]()
