#!/usr/bin/env python3
"""Exact symbolic check of pure-gradient UBT restricted Dirac constraints.

Standalone standard SymPy dependency. Mathematical scope:
L = F(y) det(d_mu y^a), restricted field-only gradient tetrad, fixed
positive orientation and no spatial-boundary terms. NOT a proof of full
single-Theta UBT gravitational constraint closure.
"""
from __future__ import annotations

import sympy as sp


def verify_flat_gradient_dirac() -> dict[str, bool]:
    # Completely general 4x4 first derivative, with temporal velocities v_a
    v = sp.symbols("v0:4")
    spatial = sp.Matrix(3, 4, lambda i, a: sp.Symbol(f"s{i+1}{a}"))
    J = sp.Matrix.vstack(sp.Matrix([list(v)]), spatial)
    detJ = J.det(method="berkowitz")
    minors = [sp.diff(detJ, va) for va in v]

    checks: dict[str, bool] = {
        "velocity_hessian_zero": sp.hessian(detJ, v) == sp.zeros(4),
        "determinant_linear_in_velocities":
            sp.simplify(detJ - sum(v[a]*minors[a] for a in range(4))) == 0,
    }
    for i in range(3):
        checks[f"cofactor_annihilates_spatial_gradient_{i+1}"] = (
            sp.simplify(sum(minors[a]*spatial[i,a] for a in range(4))) == 0
        )

    # Independent formal fields and unrestricted spatial first/second jets.
    u=sp.symbols("u0:4")
    # One nontrivial polynomial F tests the variational operator identity;
    # the accompanying note proves the general F(y) statement with forms.
    F = 1 + u[0]**2 + 2*u[1]*u[2]
    G = u[0] + u[0]**3/sp.Integer(3) + 2*u[0]*u[1]*u[2]
    checks["primitive_dG_du0_equals_F"] = sp.expand(sp.diff(G,u[0])-F)==0

    s3=sp.Matrix(3,3,lambda i,j:spatial[i,j+1])
    W_density=G*s3.det(method="berkowitz")
    # Enforce symmetric spatial second derivatives y_(ij)^a.
    second = {
        (i,j,a):sp.Symbol(f"q{min(i,j)}{max(i,j)}_{a}")
        for i in range(3) for j in range(3) for a in range(4)
    }
    def D(expr: sp.Expr, i:int)->sp.Expr:
        return sp.expand(
            sum(sp.diff(expr,u[a])*spatial[i,a] for a in range(4))
            +sum(sp.diff(expr,spatial[j,a])*second[i,j,a]
                 for j in range(3) for a in range(4))
        )

    for a in range(4):
        euler = sp.diff(W_density,u[a])-sum(
            D(sp.diff(W_density,spatial[i,a]),i) for i in range(3)
        )
        checks[f"functional_gradient_equals_F_cofactor_{a}"] = (
            sp.simplify(sp.expand(euler - F*minors[a])) == 0
        )

    # Symmetry of functional second variation follows analytically from
    # W[y] and the absence of a spatial boundary; not inferred from this
    # finite collection of pointwise symbolic identities.
    return checks


def main() -> None:
    checks=verify_flat_gradient_dirac()
    for name, passed in checks.items():
        print(f"{'PASS' if passed else 'FAIL'} {name}")
    if not all(checks.values()):
        raise SystemExit(1)
    print(f"PASS all {len(checks)} conditional exact jet identities")


if __name__=="__main__":
    main()
