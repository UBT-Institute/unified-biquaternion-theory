"""Regression checks for an analytic Lorentz-jet boundary theorem.

These tests do not establish a finished UBT dynamical action or CMB prediction.
"""
from tools.verify_lorentz_jet_boundary import verify


def test_generic_lorentz_real_pairing():
    result = verify()
    assert result["lorentz_slice_bilinear"] == "PASS"
    assert result["kinetic_volume_coefficient"] == "4*c*N0"


def test_gradient_metric_is_locally_flat():
    result = verify()
    assert result["nonlinear_coordinate_det_g"] == "-det(J)**2"
    assert result["sampled_pure_jacobian_curvatures"] == "ZERO"


def test_derivative_potential_density_is_boundary_in_restricted_branch():
    result = verify()
    assert result["polynomial_boundary_current_divergence"] == "PASS"
    assert "no full UBT" in result["theorem_scope"]
