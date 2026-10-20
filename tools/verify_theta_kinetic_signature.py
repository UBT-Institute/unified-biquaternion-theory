#!/usr/bin/env python3
"""Exact fixed-background kinetic-signature and vacuum-normal obstruction.

SymPy identities are checks of a conditional model, not a proof that the
complete composite-field UBT theory has ghosts.
"""
from __future__ import annotations

import json
import sympy as sp


def verify() -> dict:
    # Each biquaternion is a generic 2x2 complex matrix, q = (u0,u1,u2,u3,v0,v1,v2,v3).
    u0, u1, u2, u3, v0, v1, v2, v3 = q = sp.symbols("u0 u1 u2 u3 v0 v1 v2 v3", real=True)
    I = sp.I
    pauli = (
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -I], [I, 0]]),
        sp.Matrix([[1, 0], [0, -1]]),
    )
    X = (u0 + I*v0)*sp.eye(2)
    for k, sigma in enumerate(pauli):
        X += (q[k+1] + I*q[k+5])*sigma
    H = sp.expand(sp.trace(X.adjugate() * X.conjugate().T))
    diag = (2, -2, -2, -2, 2, -2, -2, -2)
    K = sp.diag(*diag)
    assert sp.expand(H - (sp.Matrix(q).T*K*sp.Matrix(q))[0]) == 0
    assert sp.hessian(H, q) == 2*K
    assert len([x for x in diag if x > 0]) == 2
    assert len([x for x in diag if x < 0]) == 6

    # At X0 = i r I, phase/boost directions span the four-dimensional orbit.
    # The other 3 rotations fix X0. N spans its K-orthogonal complement.
    eye = sp.eye(8)
    T = eye[:, [0, 5, 6, 7]]  # phase u0; boosts v1,v2,v3
    N = eye[:, [4, 1, 2, 3]]  # scalar v0; spatial-vector u1,u2,u3
    assert T.rank() == N.rank() == 4
    assert T.T*K*N == sp.zeros(4)
    assert T.T*K*T == sp.diag(2, -2, -2, -2)
    assert N.T*K*N == sp.diag(2, -2, -2, -2)

    r, l1, l2 = sp.symbols("r lambda1 lambda2", positive=True)
    mu = -(4*l1+l2)*r*r
    det_sq = sp.expand(X.det()*sp.conjugate(X.det()))
    V = sp.expand(mu*H + l1*H**2 + l2*det_sq)
    minimum = {variable: 0 for variable in q}
    minimum[v0] = r
    assert all(sp.expand(sp.diff(V, qi).subs(minimum)) == 0 for qi in q)
    M = sp.simplify(sp.hessian(V, q).subs(minimum))
    assert M*T == sp.zeros(8, 4)
    M_N = sp.simplify(N.T*M*N)
    assert M_N == sp.diag(8*r*r*(4*l1+l2), *([8*r*r*l2]*3))
    K_N = N.T*K*N
    omega_squared_numerator = sp.simplify(K_N.inv()*M_N)
    assert omega_squared_numerator == sp.diag(4*r*r*(4*l1+l2), *([-4*r*r*l2]*3))

    return {
        "invariant_pairing_signature": {"positive": 2, "negative": 6},
        "orbit_dimension": T.rank(),
        "normal_dimension": N.rank(),
        "normal_kinetic_signature": {"positive": 1, "negative": 3},
        "potential_hessian_on_normal": ["8*r^2*(4*lambda1+lambda2)", "8*r^2*lambda2 (x3)"],
        "linearized_omega_squared_for_c_positive": ["positive scalar", "negative triplet (x3)"],
        "scope": "fixed metric/connection; no full Dirac or composite Theta constraints",
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
