"""Conditional holomorphic compact imaginary time versus unitary t gates."""
from pathlib import Path
import runpy

SCRIPT = (
    Path(__file__).resolve().parents[3]
    / "tools"
    / "verify_complex_time_unitarity_gate_2026_11_24.py"
)


def test_holomorphic_periodic_fourier_mode_growth():
    runpy.run_path(str(SCRIPT))["analytic_periodic_fourier_forces_real_exponential_time"]()


def test_selfadjoint_periodicity_only_zero_energy():
    runpy.run_path(str(SCRIPT))["selfadjoint_generator_periodicity_obstruction"]()


def test_analytic_jacobi_not_periodic_and_schrodinger_sign():
    runpy.run_path(str(SCRIPT))["holomorphic_jacobi_factor_not_compact_psi"]()


def test_unitary_periodic_nonholomorphic_escape():
    runpy.run_path(str(SCRIPT))["nonholomorphic_escape_witness"]()
