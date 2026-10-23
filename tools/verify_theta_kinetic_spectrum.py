#!/usr/bin/env python3
"""Exact symbolic spectrum audit of the existing Lorentz-invariant Theta family.

Scope: prescribed flat background, no dynamical gauge or metric constraints.
This verifies a conditional instability; it does not rule out constrained UBT.
"""
from __future__ import annotations

import json
import sympy as sp


def verify() -> dict:
    # Eight independent real components in the Pauli basis:
    # X = (u0+i v0) I + sum_{j=1}^3 (uj+i vj) sigma_j.
    u0, u1, u2, u3, v0, v1, v2, v3 = q = sp.symbols(
        "u0 u1 u2 u3 v0 v1 v2 v3", real=True
    )
    r, l2 = sp.symbols("r lambda2", positive=True)
    l1 = sp.symbols("lambda1", nonnegative=True)
    c = sp.symbols("c", real=True, nonzero=True)

    z = [u0 + sp.I*v0, u1 + sp.I*v1, u2 + sp.I*v2, u3 + sp.I*v3]
    pauli = [
        sp.eye(2),
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -sp.I], [sp.I, 0]]),
        sp.diag(1, -1),
    ]
    X = sum((z[j]*pauli[j] for j in range(4)), sp.zeros(2))
    H = 2*(u0*u0+v0*v0-u1*u1-v1*v1-u2*u2-v2*v2-u3*u3-v3*v3)
    determinant = z[0]**2-z[1]**2-z[2]**2-z[3]**2
    assert sp.expand(sp.trace(X.adjugate()*X.conjugate().T)-H) == 0
    assert sp.expand(X.det()-determinant) == 0

    # Existing classified quartic potential in its proven minimum region.
    mu = -(4*l1+l2)*r**2
    U = sp.expand(mu*H+l1*H**2+l2*determinant*sp.conjugate(determinant))
    vacuum = dict(zip(q, [0, 0, 0, 0, r, 0, 0, 0]))
    assert all(sp.simplify(sp.diff(U, zq).subs(vacuum)) == 0 for zq in q)

    # Polarization H(q)=K_AB q^A q^B; kinetic L=c/2 K_AB dot q^A dot q^B.
    K = sp.hessian(H, q)/2
    expected_K = sp.diag(2, -2, -2, -2, 2, -2, -2, -2)
    assert K == expected_K
    assert K.det() == 256
    Hess = sp.hessian(U, q).subs(vacuum)
    expected_Hess = sp.diag(
        0, 8*l2*r**2, 8*l2*r**2, 8*l2*r**2,
        8*(4*l1+l2)*r**2, 0, 0, 0,
    )
    assert (Hess-expected_Hess).applyfunc(sp.simplify) == sp.zeros(8)
    masses = K.inv()*Hess/c
    expected_masses = sp.diag(
        0, -4*l2*r**2/c, -4*l2*r**2/c, -4*l2*r**2/c,
        4*(4*l1+l2)*r**2/c, 0, 0, 0,
    )
    assert (masses-expected_masses).applyfunc(sp.simplify) == sp.zeros(8)

    # Potential orbit tangent at X0=i r I: phase u0 and boosts v1,v2,v3.
    tangent = sp.Matrix.hstack(*[sp.eye(8).col(i) for i in (0, 5, 6, 7)])
    transverse = sp.Matrix.hstack(*[sp.eye(8).col(i) for i in (4, 1, 2, 3)])
    assert tangent.rank() == transverse.rank() == 4
    assert Hess*tangent == sp.zeros(8, 4)
    assert tangent.T*K*transverse == sp.zeros(4)
    assert tangent.T*K*tangent == sp.diag(2, -2, -2, -2)
    assert transverse.T*K*transverse == sp.diag(2, -2, -2, -2)
    assert (transverse.T*Hess*transverse - sp.diag(
        8*(4*l1+l2)*r**2, 8*l2*r**2, 8*l2*r**2, 8*l2*r**2
    )).applyfunc(sp.simplify) == sp.zeros(4)

    # A nondegenerate Legendre map has no Theta-only primary constraints.
    assert sp.simplify((c*K).det()-256*c**8) == 0
    return {
        "pauli_matrix_invariants": "PASS",
        "vacuum_stationarity": "PASS",
        "kinetic_signature_for_c_positive": [2, 6],
        "kinetic_signature_for_c_negative": [6, 2],
        "velocity_hessian_determinant": "256*c**8",
        "theta_only_primary_constraints_on_fixed_background": 0,
        "potential_hessian_rank": 4,
        "potential_hessian_kernel": "u0,v1,v2,v3 (phase and boosts)",
        "transverse_kinetic_signature_for_c_positive": [1, 3],
        "transverse_mass_squared": [
            "4*(4*lambda1+lambda2)*r**2/c",
            "-4*lambda2*r**2/c (multiplicity 3)",
        ],
        "linearized_result": "For either sign of c, at least one transverse mode has negative squared frequency at k=0.",
        "limits": "Fixed-background unconstrained family; no full composite Theta constraint analysis or fundamental UBT no-go.",
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
