#!/usr/bin/env python3
"""Exact local axial-torsion/stabilizer and Schwarzschild invariant checks.

Scope: finite-dimensional symbolic identities and a metric invariant, not
a full UBT equation of motion or Lean formalization.
"""

# UBT-AI-PROVENANCE-BEGIN
# schema: ubt-ai-provenance/v1
# tier: B_machine_verified
# ai_assistance: disclosed
# human_review: machine-verified
# editorial_responsibility: Ing. David Jaroš
# policy: ../AI_PROVENANCE.md
# notice: Verifies only the finite identities encoded here.
# UBT-AI-PROVENANCE-END

from itertools import product

import sympy as sp


def run():
    t, x, y, z = sp.symbols("t x y z", real=True)
    v = sp.Matrix([2 + t, x, y, z])
    eta = sp.diag(-1, 1, 1, 1)
    q = (v.T * eta * v)[0]
    for mu, coord in enumerate((t, x, y, z)):
        assert sp.simplify(sp.diff(q, coord) - 2 * (eta * v)[mu]) == 0
    print("PASS: d(V^2)=2 V_flat on the affine tetrad test branch")

    phi = sp.symbols("phi")
    eps = sp.LeviCivita

    # At e_mu^a=delta_mu^a use V instead of normalized u; the overall
    # scale is absorbed in phi, without changing the antisymmetry test.
    def C(c, a, b):
        return phi * sum(eps(a, b, d, c) * v[d] for d in range(4))

    def delta_t(a, b, c):
        return C(b, a, c) - C(c, a, b)

    for a, b, c in product(range(4), repeat=3):
        assert sp.simplify(
            delta_t(a, b, c) -
            2 * phi * sum(eps(a, b, c, d) * v[d] for d in range(4))
        ) == 0
        assert sp.simplify(sum(C(c, a, b) * v[b] for b in range(4))) == 0
    print("PASS: axial stabilizer shift C V=0 and delta torsion is a 3-form")

    # Timelike V(p)=(2,0,0,0): C_{c,a,b}, a,b in spatial 1..3.
    labels = [(c, a, b) for c in range(4)
              for a in range(1, 4) for b in range(a + 1, 4)]
    coeff = sp.symbols("c0:12")

    def c_var(c, a, b):
        if a == b or a == 0 or b == 0:
            return 0
        if a > b:
            return -c_var(c, b, a)
        return coeff[labels.index((c, a, b))]

    def dt_var(a, b, c):
        return c_var(b, a, c) - c_var(c, a, b)

    # T_{a,b,c} is already antisymmetric in b,c.
    constraints = [
        sp.expand(dt_var(a, b, c) + dt_var(b, a, c))
        for a, b, c in product(range(4), repeat=3)
    ]
    matrix, _ = sp.linear_eq_to_matrix(constraints, coeff)
    assert matrix.rank() == 11
    assert len(matrix.nullspace()) == 1
    print("PASS: 12 stabilizer coefficients, 11 axial constraints, 1 free")

    mass, radius = sp.symbols("M r", positive=True)
    kretschmann = 48 * mass**2 / radius**6
    J = sp.simplify(
        (1 - 2 * mass / radius) *
        sp.diff(kretschmann, radius)**2 /
        kretschmann**sp.Rational(5, 2)
    )
    assert sp.simplify(
        J - 3 * sp.sqrt(3) * (radius / mass - 2)
    ) == 0
    assert sp.simplify(sp.diff(J, radius)) != 0
    print("PASS: Schwarzschild scale-invariant diagnostic J=" + str(J))
    print("SymPy version:", sp.__version__)
    print("LEAN-PENDING: no theorem-level formal check was performed")


if __name__ == "__main__":
    run()
