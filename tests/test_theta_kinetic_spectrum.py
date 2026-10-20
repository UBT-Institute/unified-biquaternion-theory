"""Regression guard for the Lorentz-invariant Theta kinetic/potential no-go.

These tests verify a conditional fixed-background result; they do not assert
that the full constrained UBT has ghosts or tachyons.
"""
from tools.verify_theta_kinetic_spectrum import verify


def test_exact_kinetic_signature_and_nonzero_legendre_determinant():
    record = verify()
    assert record["pauli_matrix_invariants"] == "PASS"
    assert record["kinetic_signature_for_c_positive"] == [2, 6]
    assert record["kinetic_signature_for_c_negative"] == [6, 2]
    assert record["velocity_hessian_determinant"] == "256*c**8"
    assert record["theta_only_primary_constraints_on_fixed_background"] == 0


def test_potential_hessian_and_transverse_instability():
    record = verify()
    assert record["vacuum_stationarity"] == "PASS"
    assert record["potential_hessian_rank"] == 4
    assert record["transverse_kinetic_signature_for_c_positive"] == [1, 3]
    assert len(record["transverse_mass_squared"]) == 2
    assert "at least one transverse mode" in record["linearized_result"]
