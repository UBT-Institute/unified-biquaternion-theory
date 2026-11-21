"""Exact restricted single-biquaternion helicity-2 dynamics gate."""
from pathlib import Path
import runpy

SOURCE = (
    Path(__file__).resolve().parents[3]
    / "tools"
    / "verify_inverse_spin2_little_group_gate_2026_11_21.py"
)


def test_no_linear_spin2_intertwiner():
    runpy.run_path(str(SOURCE))["little_group_intertwiner"]()


def test_pauli_rotation_representation():
    runpy.run_path(str(SOURCE))["pauli_rotation_check"]()


def test_quadratic_composite_tt():
    runpy.run_path(str(SOURCE))["quadratic_spin2_gate"]()


def test_independent_connection_comparator():
    runpy.run_path(str(SOURCE))["independent_connection_counterexample"]()


def test_free_gaussian_fock_number_gate():
    runpy.run_path(str(SOURCE))["gaussian_two_particle_gate"]()
