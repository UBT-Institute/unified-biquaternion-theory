#!/usr/bin/env python3
"""Exact Lorentz-real timelike gauge reduction and emergent-tetrad rank obstruction.

Prescribed metric, independent auxiliary sl(2,C) connection, no F^2 term.
The result is conditional and does not replace the full composite variation.
"""
from __future__ import annotations

import json
import sympy as sp


def verify() -> dict:
    rho, c, N0 = sp.symbols("rho c N0", positive=True)
    r, lam2 = sp.symbols("r lambda2", positive=True)
    lam1 = sp.symbols("lambda1", nonnegative=True)
    U0 = sp.symbols("U0", real=True)
    I2 = sp.eye(2)
    pauli = (
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -sp.I], [sp.I, 0]]),
        sp.diag(1, -1),
    )

    # Gauge-fixed positive Hermitian cone: X=i*rho*I, rho=sqrt(det(-iX))>0.
    X = sp.I*rho*I2
    assert sp.expand(sp.trace(X.adjugate()*X.conjugate().T)-2*rho**2) == 0
    assert sp.expand(X.det()+rho**2) == 0
    U = U0-(4*lam1+lam2)*r**2*(2*rho**2)+(4*lam1+lam2)*rho**4
    completed = U0+(4*lam1+lam2)*(rho**2-r**2)**2-(4*lam1+lam2)*r**4
    assert sp.expand(U-completed) == 0
    assert sp.simplify(sp.diff(U, rho).subs(rho, r)) == 0
    assert sp.simplify(sp.diff(U, rho, 2).subs(rho, r)
                       -8*(4*lam1+lam2)*r**2) == 0

    # For each mu, A_mu+A_mu^dagger = sum_j b_{mu,j} sigma_j.
    # D_mu X = i (partial_mu rho I + rho sum_j b_{mu,j} sigma_j).
    d = sp.Matrix(sp.symbols("d0:4", real=True))
    b = sp.Matrix(4, 3, sp.symbols("b0:12", real=True))
    eta = (-1, 1, 1, 1)
    kinetic = sp.Integer(0)
    for mu in range(4):
        D = sp.I*(d[mu]*I2+rho*sum(
            (b[mu, j]*pauli[j] for j in range(3)), sp.zeros(2)
        ))
        invariant = sp.expand(sp.trace(D.adjugate()*D.conjugate().T))
        expected = 2*(d[mu]**2-rho**2*sum(b[mu, j]**2 for j in range(3)))
        assert sp.simplify(invariant-expected) == 0
        # Lorentz signature (-+++) and action L=-c/2 eta^{mu nu} K(Dmu,Dnu).
        kinetic += -c*eta[mu]*(d[mu]**2-rho**2*sum(
            b[mu, j]**2 for j in range(3)
        ))

    # Each independent boost connection has a unique algebraic equation.
    for mu in range(4):
        for j in range(3):
            eq = sp.diff(kinetic, b[mu, j])
            assert sp.simplify(eq - 2*c*eta[mu]*rho**2*b[mu, j]) == 0
    reduced = sp.expand(kinetic.subs({
        b[mu, j]: 0 for mu in range(4) for j in range(3)
    }))
    assert sp.simplify(reduced+c*sum(eta[mu]*d[mu]**2 for mu in range(4))) == 0

    # On shell, D_mu X = i*(partial_mu rho)*I: only one internal direction.
    tetrad = sp.Matrix(4, 4, lambda mu, a: d[mu] if a == 0 else 0)
    assert tetrad.rank() == 1
    assert tetrad.det() == 0
    g_composite = -d*d.T/N0
    assert g_composite.rank() == 1
    assert g_composite.det() == 0

    return {
        "timelike_lorentz_real_potential_reduction": "PASS",
        "auxiliary_boost_connection_equations": 12,
        "unique_auxiliary_solution": "all boost components zero in unitary gauge",
        "reduced_radial_kinetic_energy_for_c_positive": "positive",
        "radial_potential_second_derivative_at_r": "8*(4*lambda1+lambda2)*r**2",
        "on_shell_composite_tetrad_rank": 1,
        "on_shell_composite_metric_determinant": 0,
        "conclusion": "Stable radial fixed-metric reduction cannot simultaneously generate a nondegenerate UBT tetrad in this minimal auxiliary-connection branch.",
        "scope": "Timelike Lorentz-real gauge slice, prescribed nondegenerate metric, independent auxiliary sl2C connection without curvature terms; full composite metric variation OPEN.",
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
