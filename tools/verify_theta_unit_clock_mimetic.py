#!/usr/bin/env python3
"""Exact independent metric and FLRW checks of the conditional unit-clock branch.

This verifier covers a constrained tetrad / assumed Einstein-Hilbert functional,
not the complete UBT composite-field action or its Dirac algebra.
"""
from __future__ import annotations

import json
import sympy as sp


def verify() -> dict:
    rho = sp.symbols("rho", positive=True)
    eta = sp.diag(-1, 1, 1, 1)
    # Exact rational tetrad with e0=d(rho), an invertible spatial/boost frame.
    # The nonzero timelike spatial coframe component prevents relying on
    # a trivial diagonal-metric special case.
    boost = sp.Matrix([
        [1, 1, 0, 0],
        [0, 0, 2, 1],
        [0, 0, 0, 3],
    ])
    e = sp.Matrix.vstack(sp.Matrix([[1, 0, 0, 0]]), rho * boost)
    metric = e.T * eta * e
    n_cov = e.row(0).T
    n_con = metric.inv() * n_cov
    assert sp.factor(e.det()) == 6 * rho**3
    assert sp.simplify((n_cov.T * n_con)[0]) == -1
    assert sp.simplify(n_cov.T * metric.inv() * n_cov) == sp.Matrix([[-1]])
    L = sp.symbols("L", real=True)
    projected = L * n_con * n_con.T
    for i in range(1, 4):
        assert sp.simplify(projected * e.row(i).T) == sp.zeros(4, 1)

    t, x, y, z = sp.symbols("t x y z", positive=True, real=True)
    coordinates = (t, x, y, z)
    scale = t ** sp.Rational(2, 3)
    g = sp.diag(-1, scale**2, scale**2, scale**2)
    inverse = g.inv()
    dim = 4
    connection = [
        [
            [
                sp.simplify(
                    sum(
                        inverse[a, k] *
                        (sp.diff(g[k, j], coordinates[i])
                         + sp.diff(g[k, i], coordinates[j])
                         - sp.diff(g[i, j], coordinates[k]))
                        for k in range(dim)
                    ) / 2
                )
                for j in range(dim)
            ]
            for i in range(dim)
        ]
        for a in range(dim)
    ]
    ricci = sp.Matrix(dim, dim, lambda i, j: sp.simplify(sum(
        sp.diff(connection[k][i][j], coordinates[k])
        - sp.diff(connection[k][i][k], coordinates[j])
        + sum(
            connection[k][k][l] * connection[l][i][j]
            - connection[k][j][l] * connection[l][i][k]
            for l in range(dim)
        )
        for k in range(dim)
    )))
    scalar = sp.simplify(
        sum(inverse[i, j] * ricci[i, j]
            for i in range(dim) for j in range(dim))
    )
    einstein = sp.simplify(ricci - g * scalar / 2)
    assert scalar == sp.Rational(4, 3) / t**2
    assert einstein == sp.diag(sp.Rational(4, 3) / t**2, 0, 0, 0)
    # lambda=-M^2 G^{00}/2; its dust current has identically zero divergence.
    mass2 = sp.symbols("M2", positive=True)
    lam = -2 * mass2 / (3 * t**2)
    assert sp.simplify(sp.diff(scale**3 * lam, t)) == 0
    assert sp.simplify(scale**3 * lam) == -sp.Rational(2, 3) * mass2
    assert sp.simplify((t * (scale/t)**3)) != 0  # nonzero coframe volume
    hubble = sp.diff(scale, t) / scale
    # Canonical EH Hamiltonian density in the flat FLRW, shift-free frame.
    # pi^{ij} = -M2*sqrt(h)*H*h^{ij}; the 3-curvature vanishes.
    h_perp = sp.simplify(-3 * mass2 * scale**3 * hubble**2)
    assert sp.simplify(h_perp - 2 * scale**3 * lam) == 0
    assert sp.simplify(h_perp + sp.Rational(4, 3) * mass2) == 0

    return {
        "unit_clock_identity": "PASS",
        "projected_metric_equations": "PASS",
        "nondegenerate_example": "PASS",
        "FLRW_curvature_and_Einstein_tensor": "PASS",
        "dust_current_conservation": "PASS",
        "Einstein_vacuum_counterexample": "PASS",
        "ADM_lapse_constraint_not_imposed": "PASS",
        "scope": "assumed Einstein-Hilbert functional, independent boost coframe, local timelike patch",
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
