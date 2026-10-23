#!/usr/bin/env python3
"""Exact conditional causal-cone and holomorphy checks for the UBT kinetic family.

This verifies a fixed-background eight-real-component principal symbol, NOT
the reduced physical symbol of a completed constrained/composite UBT action.
c_light denotes the measured light speed; kappa is kinetic normalization.
"""
from __future__ import annotations

import json
import sympy as sp


def verify() -> dict:
    omega, k = sp.symbols("omega k", real=True)
    c_light, a = sp.symbols("c_light a", positive=True)
    kappa = sp.symbols("kappa", real=True, nonzero=True)
    K = sp.diag(2, -2, -2, -2, 2, -2, -2, -2)
    Q = k**2 - omega**2/c_light**2
    assert K.det() == 256

    # Principal symbol of the fixed-background two-derivative family.
    principal = kappa*K*Q
    assert sp.factor(principal.det() - 256*kappa**8*Q**8) == 0
    # Flipping kinetic energy signs does NOT change the characteristic cone.
    assert sp.factor(principal.det() - (-principal).det()) == 0
    assert K[1, 1] < 0 and K[0, 0] > 0

    # A separate two-mode illustrative operator, NOT a UBT prediction.
    s = sp.symbols("s", positive=True)
    P2 = sp.diag(k**2-omega**2/c_light**2,
                 s**2*k**2-omega**2/c_light**2)
    assert sp.factor(P2.det() - (k**2-omega**2/c_light**2) *
                     (s**2*k**2-omega**2/c_light**2)) == 0

    # Holomorphic z1=a*(t+i*psi) satisfies Cauchy--Riemann but its
    # physical t-derivative lies along a negative K direction.
    t, psi = sp.symbols("t psi", real=True)
    u, v = a*t, a*psi
    assert sp.diff(u, t) == sp.diff(v, psi)
    assert sp.diff(u, psi) == -sp.diff(v, t)
    qdot = sp.Matrix([0, a, 0, 0, 0, 0, 0, 0])
    assert sp.expand((qdot.T*K*qdot)[0]) == -2*a**2
    qdot_positive = sp.Matrix([a, 0, 0, 0, 0, 0, 0, 0])
    assert sp.expand((qdot_positive.T*K*qdot_positive)[0]) == 2*a**2

    return {
        "eight_real_principal_determinant":
            "256*kappa**8*(k**2-omega**2/c_light**2)**8",
        "principal_characteristic_speed":
            "c_light (multiplicity 8 before constraints)",
        "kinetic_inertia_kappa_positive": [2, 6],
        "kinetic_inertia_kappa_negative": [6, 2],
        "kinetic_sign_changes_characteristic_cone": False,
        "two_mode_toy_characteristic_speeds": ["c_light", "s*c_light"],
        "holomorphic_negative_kinetic_example": "z1=a*(t+i*psi)",
        "holomorphy_alone_implies_ghost_freedom": False,
        "status":
            "Exact algebra for fixed-background family; not a physical UBT cone prediction.",
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
