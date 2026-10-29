"""Exact coefficients and a separately discretized full-spatial bracket."""
import numpy as np
import pytest

from tools.verify_spatial_constraint_closure import (
    numerical_checks, scalar_curvature, symbolic_checks,
)


@pytest.mark.parametrize("name", sorted(symbolic_checks()))
def test_exact_spatial_closure_identity(name):
    assert symbolic_checks()[name], name


def test_independent_torus_functional_bracket():
    report = numerical_checks()
    assert all(report["checks"].values()), report


def test_curvature_implementation_on_nonconstant_conformal_metric():
    # R[e^(2u) delta] = e^(-2u) (-4 Delta u - 2 |grad u|^2) in d=3.
    n = 24
    x, y, z = np.meshgrid(*([np.arange(n)*2*np.pi/n]*3), indexing="ij")
    u = .03*(np.cos(x)+np.cos(y)+np.cos(z))
    metric = np.exp(2*u)[..., None, None]*np.eye(3)
    expected = np.exp(-2*u)*(4*u-2*.03**2*(np.sin(x)**2+np.sin(y)**2+np.sin(z)**2))
    assert np.max(np.abs(scalar_curvature(metric)-expected)) < 1e-10
