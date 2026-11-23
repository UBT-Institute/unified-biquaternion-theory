"""Exact scoped Jacobi-mode projective-dynamics algebra regressions."""
from pathlib import Path
import runpy

SCRIPT = (
    Path(__file__).resolve().parents[3]
    / "tools"
    / "verify_jacobi_projective_mode_dynamics_gate_2026_11_24.py"
)


def test_outer_product_differential_ranks():
    gate = runpy.run_path(str(SCRIPT))["differential_rank_gate"]
    for n in (2, 3, 4):
        assert gate(n) == (2 * n - 1, 2 * n - 2)


def test_same_sign_2d_fft_is_not_density_basis_change():
    runpy.run_path(str(SCRIPT))["dft_two_axis_vs_density_gate"]()


def test_jacobi_heat_vs_physical_phase_fs_gate():
    runpy.run_path(str(SCRIPT))["projective_heat_vs_phase_gate"]()


def test_same_projective_kinematics_two_positive_generators():
    runpy.run_path(str(SCRIPT))["distinct_positive_generators_gate"]()
