"""Exact regression of the auxiliary gauge-connection reduction at X0=i*r*I.

Conditional fixed-background result, not a full composite UBT Dirac proof.
"""
from tools.verify_theta_auxiliary_connection_reduction import verify


def test_phase_boost_connection_elimination_is_algebraic():
    result = verify()
    assert result["vacuum_phase_and_boost_generators"] == "PASS"
    assert result["unbroken_rotation_generators_at_vacuum"] == 3
    assert result["eliminated_tangent_covariant_derivatives"] == 4


def test_auxiliary_connections_do_not_remove_normal_instability():
    result = verify()
    assert result["remaining_normal_kinetic_signature_c_positive"] == [1, 3]
    assert result["remaining_normal_velocity_hessian_determinant"] == "-16*c**4"
    assert "do not cure" in result["conclusion"]
