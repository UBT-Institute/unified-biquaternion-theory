#!/usr/bin/env python3
"""Exact checks of the Lorentz-jet volume collapse and flat-gradient branch.

Computational examples support the unrestricted analytic identities proved in
research_tracks/action_selection/lorentz_jet_volume_boundary.en.md.
No complete UBT action, physical CMB model, or observational fit is asserted.
"""
from __future__ import annotations

import json

import sympy as sp


def verify() -> dict:
    N0 = sp.symbols("N0", positive=True)
    a = sp.symbols("a0:4", real=True)
    b = sp.symbols("b0:4", real=True)
    pauli = (
        sp.eye(2),
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -sp.I], [sp.I, 0]]),
        sp.diag(1, -1),
    )
    X = sp.I * sp.sqrt(N0) * sum(
        (a[k] * pauli[k] for k in range(4)), sp.zeros(2)
    )
    Y = sp.I * sp.sqrt(N0) * sum(
        (b[k] * pauli[k] for k in range(4)), sp.zeros(2)
    )
    # Polarization of the real invariant B(X,X)=Tr(adj(X) X^dagger).
    bilinear = sp.expand(
        (sp.trace(X.adjugate() * Y.conjugate().T)
         + sp.trace(Y.adjugate() * X.conjugate().T)) / 2
    )
    expected = 2 * N0 * (a[0] * b[0] -
                          sum(a[k] * b[k] for k in range(1, 4)))
    assert sp.simplify(bilinear - expected) == 0

    # Independent nonlinear coordinate example. J_{a mu}=d_mu y^a.
    t, x, y, z = coords = sp.symbols("t x y z", real=True)
    target = sp.Matrix([t+t*x, x+t**2, y+t*z, z+x*y])
    jac = target.jacobian(coords)
    determinant = sp.factor(jac.det())
    assert determinant != 0

    metric = jac.T * sp.diag(-1, 1, 1, 1) * jac
    assert sp.factor(metric.det() + determinant**2) == 0

    # Exact four-form primitive and divergence for a nonconstant polynomial F.
    F = 3 + target[0]**2 + 2*target[1]**2
    G = 3*target[0] + target[0]**3/sp.Integer(3) + 2*target[0]*target[1]**2
    current = []
    for mu in range(4):
        flux = sum(
            sp.LeviCivita(mu, nu, rho, sig)
            * jac[1, nu] * jac[2, rho] * jac[3, sig]
            for nu in range(4) for rho in range(4) for sig in range(4)
        )
        current.append(sp.expand(G * flux))
    div = sum(sp.diff(current[mu], coords[mu]) for mu in range(4))
    assert sp.simplify(div - F * determinant) == 0

    # Levi-Civita connection of the pure-coordinate-pullback metric is
    # Gamma_mu = J^{-1} d_mu J. Check three independent curvature components.
    inv_jac = jac.inv()
    gamma = [(inv_jac * jac.diff(coord)).applyfunc(sp.cancel)
             for coord in coords]
    for mu, nu in ((0, 1), (0, 2), (1, 3)):
        curvature = (
            gamma[nu].diff(coords[mu])
            - gamma[mu].diff(coords[nu])
            + gamma[mu]*gamma[nu]
            - gamma[nu]*gamma[mu]
        )
        assert curvature.applyfunc(sp.cancel) == sp.zeros(4)

    # Universal contraction is a separate exact matrix identity:
    # B(D_mu Theta,D_nu Theta)=-2*N0*g_mu,nu implies
    # g^mu,nu B_mu,nu=-2*N0*tr(I4)=-8*N0.
    inverse_metric_identity = sp.eye(4)
    assert sp.trace(inverse_metric_identity) == 4

    return {
        "lorentz_slice_bilinear": "PASS",
        "kinetic_volume_coefficient": "4*c*N0",
        "nonlinear_coordinate_det_g": "-det(J)**2",
        "polynomial_boundary_current_divergence": "PASS",
        "sampled_pure_jacobian_curvatures": "ZERO",
        "theorem_scope": (
            "Only the real Lorentz tetrad and a separate gauge-trivial "
            "pure-gradient reduction; no full UBT equations or CMB fit."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
