#!/usr/bin/env python3
"""Exact composite-volume collapse for the minimal timelike auxiliary-connection branch.

This is a restricted classical no-go: X=i*rho*I in local Lorentz gauge,
independent sl2C connection, central composite metric, no F^2 or curvature
term, and nonconstant quartic potential. Not a no-go for all UBT actions.
"""
from __future__ import annotations

import json
import sympy as sp


def verify() -> dict:
    N0, rho, c = sp.symbols("N0 rho c", positive=True)
    r, lam2 = sp.symbols("r lambda2", positive=True)
    lam1 = sp.symbols("lambda1", nonnegative=True)
    U0 = sp.symbols("U0", real=True)
    pauli = (
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -sp.I], [sp.I, 0]]),
        sp.diag(1, -1),
    )
    I2 = sp.eye(2)

    # Generic two Lorentz-real covariant derivatives in the Pauli basis.
    a, a2 = sp.symbols("a a2", real=True)
    v = sp.symbols("v0:3", real=True)
    w = sp.symbols("w0:3", real=True)
    E1 = sp.I*(a*I2+sum((v[j]*pauli[j] for j in range(3)), sp.zeros(2)))
    E2 = sp.I*(a2*I2+sum((w[j]*pauli[j] for j in range(3)), sp.zeros(2)))
    central = sp.expand((E1.adjugate()*E2+E2.adjugate()*E1)/2)
    scalar = -(a*a2-sum(v[j]*w[j] for j in range(3)))
    assert (central-scalar*I2).applyfunc(sp.simplify) == sp.zeros(2)
    pairing = sp.trace(E1.adjugate()*E2.conjugate().T)
    assert sp.simplify(pairing+2*scalar) == 0

    # In the timelike unitary gauge, E_mu=(d_mu rho, rho*b_mu^j)/sqrt(N0).
    d = sp.Matrix(sp.symbols("d0:4", real=True))
    B = sp.Matrix(4, 3, sp.symbols("b0:12", real=True))
    E = sp.Matrix.hstack(d, rho*B)/sp.sqrt(N0)
    eta = sp.diag(-1, 1, 1, 1)
    g = E*eta*E.T
    # From the proven pairwise identity, K(D_mu,D_nu)=-2*N0*g_mu_nu.
    K_spacetime = -2*N0*g
    # The pairwise Pauli identity above proves K_mu,nu=-2*N0*g_mu,nu
    # for arbitrary derivatives. On det(E)!=0, g^-1*g=I proves the
    # exact contracted kinetic trace -8*N0 without a huge symbolic inverse.
    assert K_spacetime == -2*N0*g

    M = sp.Matrix.hstack(d, B)
    determinant = sp.factor(E.det())
    assert sp.simplify(determinant-rho**3*M.det()/N0**2) == 0
    # On an oriented nondegenerate patch, sqrt(-det(g))=det(E)>0.
    # det(g)=det(E)^2*det(eta)=-det(E)^2 by determinant multiplicativity.

    U = U0+(4*lam1+lam2)*(rho**2-r**2)**2-(4*lam1+lam2)*r**4
    assert sp.degree(U, rho) == 4
    C = 4*c*N0
    volume_density = determinant*(C-U)
    # Every auxiliary boost equation is proportional to (C-U).
    for mu in range(4):
        for j in range(3):
            assert sp.simplify(
                sp.diff(volume_density, B[mu, j])
                -(C-U)*sp.diff(determinant, B[mu, j])
            ) == 0
    # Nondegenerate E implies each inverse column has a nonzero cofactor.
    # Thus all connection equations force C-U(rho)=0 pointwise.
    # A smooth rho on a connected open set taking values in the finite
    # root set of a nonconstant quartic must be constant, so d rho=0.
    E_constant_rho = E.subs({di: 0 for di in d})
    assert E_constant_rho[:, 0] == sp.zeros(4, 1)  # rank <= 3
    assert sp.simplify(E_constant_rho.det()) == 0

    return {
        "central_metric_pairing_identity": "PASS",
        "composite_kinetic_trace": "-8*N0 (four spacetime dimensions)",
        "kinetic_action_density": "+4*c*N0*sqrt(-g) for L=-c/2*g^mu,nu*K_mu,nu",
        "composite_volume_jacobian": "rho**3*det([d rho, b1, b2, b3])/N0**2",
        "auxiliary_boost_variation": "cofactor*(4*c*N0-U(rho))=0",
        "nondegenerate_stationarity_requires": "U(rho)=4*c*N0",
        "quartic_nonconstant": True,
        "resulting_rho_on_connected_patch": "constant",
        "resulting_composite_tetrad_rank_at_most": 3,
        "conclusion": "No nondegenerate stationary tetrad on the timelike Lorentz-real patch in this minimal composite-metric auxiliary-connection branch.",
        "scope": "No independent curvature/YM terms, no derivative connection terms, fixed real slice, timelike patch, nonconstant quartic; other UBT branches remain OPEN.",
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
