#!/usr/bin/env python3
"""Exact quadratic elimination of auxiliary phase/boost connections at X0=i*r*I.

This is a fixed-background, independent-connection calculation. It is not a
Dirac analysis of a composite metric, dynamical torsion, or the full UBT action.
"""
from __future__ import annotations

import json
import sympy as sp


def verify() -> dict:
    r, c = sp.symbols("r c", real=True, nonzero=True)
    lam1 = sp.symbols("lambda1", nonnegative=True)
    lam2 = sp.symbols("lambda2", positive=True)

    I2 = sp.eye(2)
    pauli = (
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -sp.I], [sp.I, 0]]),
        sp.diag(1, -1),
    )
    X0 = sp.I*r*I2
    assert sp.I*X0 == -r*I2  # U(1) phase tangent
    for sigma in pauli:
        boost = sigma/2
        rotation = sp.I*sigma/2
        assert sp.simplify(boost*X0+X0*boost.conjugate().T-sp.I*r*sigma) == sp.zeros(2)
        assert sp.simplify(rotation*X0+X0*rotation.conjugate().T) == sp.zeros(2)

    # One fixed spacetime derivative direction; every mu factorizes in the
    # fixed-metric quadratic action, with the corresponding metric sign.
    dt = sp.Matrix(sp.symbols("dt0:4", real=True))  # phase/boost tangential derivatives
    dn = sp.Matrix(sp.symbols("dn0:4", real=True))  # scalar/vector normal derivatives
    a = sp.Matrix(sp.symbols("a0:4", real=True))    # independent auxiliary connections
    K4 = sp.diag(2, -2, -2, -2)
    tangent_cov = sp.Matrix([dt[0]-r*a[0], *(dt[i]+r*a[i] for i in range(1, 4))])
    L_kin = sp.expand(c/2*((tangent_cov.T*K4*tangent_cov)[0]+(dn.T*K4*dn)[0]))

    connection_equations = [sp.diff(L_kin, a[i]) for i in range(4)]
    solution = sp.solve(connection_equations, list(a), dict=True)
    assert len(solution) == 1
    assert solution[0] == {a[0]: dt[0]/r, a[1]: -dt[1]/r,
                           a[2]: -dt[2]/r, a[3]: -dt[3]/r}
    assert all(sp.simplify(e.subs(solution[0])) == 0 for e in connection_equations)
    assert tangent_cov.subs(solution[0]) == sp.zeros(4, 1)

    reduced = sp.expand(L_kin.subs(solution[0]))
    expected = c*(dn[0]**2-dn[1]**2-dn[2]**2-dn[3]**2)
    assert sp.simplify(reduced-expected) == 0
    assert sp.hessian(reduced, dn) == c*K4
    assert sp.simplify((c*K4).det()+16*c**4) == 0

    # The already-derived transverse potential Hessian remains untouched by
    # the algebraic connection elimination (potential contains no connection).
    M4 = sp.diag(8*(4*lam1+lam2)*r**2, 8*lam2*r**2,
                 8*lam2*r**2, 8*lam2*r**2)
    generalized = (c*K4).inv()*M4
    expected_generalized = sp.diag(
        4*(4*lam1+lam2)*r**2/c,
        -4*lam2*r**2/c, -4*lam2*r**2/c, -4*lam2*r**2/c
    )
    assert (generalized-expected_generalized).applyfunc(sp.simplify) == sp.zeros(4)

    return {
        "vacuum_phase_and_boost_generators": "PASS",
        "unbroken_rotation_generators_at_vacuum": 3,
        "auxiliary_connection_equations": "four algebraic equations, unique solution for phase and boosts",
        "eliminated_tangent_covariant_derivatives": 4,
        "remaining_normal_kinetic_signature_c_positive": [1, 3],
        "remaining_normal_velocity_hessian_determinant": "-16*c**4",
        "remaining_normal_generalized_mass_squared": [
            "4*(4*lambda1+lambda2)*r**2/c",
            "-4*lambda2*r**2/c (multiplicity 3)",
        ],
        "conclusion": "Auxiliary phase/boost connections alone do not cure the transverse ghost/IR instability.",
        "scope": "Quadratic fixed-background minimal family, independent connections without curvature terms; full composite Dirac analysis OPEN.",
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
