#!/usr/bin/env python3
"""Exact tests for wave_dynamics.en.md / wave_dynamics.cs.md.

Checks bounded local identities, not a selected UBT action or physical spectrum.
The independent Fraction channel uses separate determinant and exterior-symbol
implementations. Analytic proofs, including local exactness, are in the notes.
"""
import itertools
import json
import platform
from fractions import Fraction as Q
from pathlib import Path

import sympy as s


def permutation_sign(values):
    if len(set(values)) != len(values):
        return 0
    return (-1) ** sum(values[i] > values[j]
                      for i in range(len(values)) for j in range(i+1, len(values)))


def determinant(matrix):
    """Leibniz determinant in rational arithmetic; independent of SymPy."""
    total = Q(0)
    for p in itertools.permutations(range(len(matrix))):
        term = Q(permutation_sign(p))
        for i, j in enumerate(p):
            term *= Q(matrix[i][j])
        total += term
    return total


def verify():
    checks = []

    def exact(name, expression, channel="SymPy"):
        values = list(expression) if isinstance(expression, (s.MatrixBase, list, tuple)) else [expression]
        passed = all(s.simplify(v) == 0 for v in values) if channel == "SymPy" else all(v == 0 for v in values)
        checks.append({"name": name, "channel": channel, "passed": passed})
        if not passed:
            raise AssertionError(name)

    # A common-coordinate first-jet Lorentz/central composite remains M(X)dX.
    eta = s.diag(-1, 1, 1, 1)
    X = s.Matrix(s.symbols("X0:4"))
    P = s.Matrix(s.symbols("P0:4"))
    f, h, b = s.symbols("f h b")
    q, xp = (X.T*eta*X)[0], (X.T*eta*P)[0]
    lx, lp = eta*X, eta*P
    K = f*(lx*lp.T-lp*lx.T)
    target = (1-f*q)*P+(f+b)*X*xp
    exact("common_coordinate_composite_factorization", P+eta*K*X+b*xp*X-target)
    dual = s.Matrix(4, 4, lambda a, c: h*sum(
        s.LeviCivita(a,c,d,e)*X[d]*P[e] for d in range(4) for e in range(4)))
    exact("dual_Lorentz_term_annihilates_field", dual*X)

    # Every E=M(X,s)dX+N(X,s)ds gives a pulled-back volume, on a fixed branch.
    M = s.Matrix([[2,1,0,0], [0,3,1,0], [0,0,2,1], [1,0,0,2]])
    p = s.Matrix(4,4,s.symbols("p0:16"))
    tail = s.Matrix([s.symbols("r0:4")])
    n = s.Matrix(s.symbols("n0:4"))
    u = s.Matrix([0,0,0,0,1])
    E = p.col_join(tail)*M.T+u*n.T
    exact("completed_composite_volume_factor", E.row_join(u).det()-M.det()*p.det())

    # Realification of the existing field-space form and its Lorentz slice.
    G = s.Matrix([[0,0,0,1], [0,-1,0,0], [0,0,-1,0], [1,0,0,0]])
    C = s.Matrix([[s.I,0,0,-s.I], [0,-s.I,-1,0], [0,-s.I,1,0], [s.I,0,0,s.I]])
    J = C.applyfunc(s.re).col_join(C.applyfunc(s.im))
    N = (-C.applyfunc(s.im)).col_join(C.applyfunc(s.re))
    Omega = s.zeros(4).row_join(G).col_join((-G).row_join(s.zeros(4)))
    H = -2*eta
    dxi = s.Matrix(4,4,s.symbols("d0:16"))  # internal, coordinate
    eps, f0, f1 = s.symbols("eps f0 f1")
    perturbed = J+eps*N*dxi
    Qeps = perturbed.T*Omega*perturbed
    da = H*dxi-dxi.T*H
    exact("normal_field_variation_Q_is_da", Qeps-eps*da)
    pf = lambda a: a[0,1]*a[2,3]-a[0,2]*a[1,3]+a[0,3]*a[1,2]
    exact("normal_quadratic_density", s.expand((f0+eps*f1)*pf(Qeps)).coeff(eps,2)-f0*pf(da))

    # Full Euler differentiation of F da wedge da / 2: second jets cancel.
    coords = s.symbols("t x y z")
    a = [s.Function("a"+str(i))(*coords) for i in range(4)]
    F = s.Function("F")(*coords)
    curvature = s.Matrix(4,4,lambda i,j: s.diff(a[j],coords[i])-s.diff(a[i],coords[j]))
    density = F*pf(curvature)
    for nu in range(4):
        euler = -sum(s.diff(s.diff(density,s.diff(a[nu],coords[mu])),coords[mu]) for mu in range(4))
        expected = sum(s.LeviCivita(nu,r,t,l)*s.diff(F,coords[r])*curvature[t,l]/2
                       for r,t,l in itertools.product(range(4), repeat=3))
        exact("normal_full_Euler_"+str(nu), euler-expected)

    v = s.Matrix(s.symbols("v0:4"))
    k = s.Matrix(s.symbols("k0:4"))
    A = s.Matrix(4,4,lambda mu,nu: sum(s.LeviCivita(mu,nu,r,t)*v[r]*k[t]
                                     for r,t in itertools.product(range(4),repeat=2)))
    exact("normal_symbol_antisymmetric", A+A.T)
    exact("normal_symbol_kernel_gradient", A*k)
    exact("normal_symbol_kernel_dF", A*v)
    exact("normal_symbol_Pfaffian_zero", pf(A))
    exact("normal_symbol_rank_two_witness", A.subs(dict(zip(list(v)+list(k),[1,0,0,0,0,1,0,0]))).rank()-2)

    for idx, (vv,kk) in enumerate([
        ([1,0,0,0],[0,1,0,0]), ([1,2,3,4],[2,-1,0,3]), ([0,0,0,1],[1,2,3,0])
    ]):
        aa = [[Q(sum(permutation_sign([mu,nu,r,t])*vv[r]*kk[t]
                    for r,t in itertools.product(range(4),repeat=2)))
               for nu in range(4)] for mu in range(4)]
        residues = [sum(aa[i][j]*z[j] for j in range(4))
                    for z in [vv,kk] for i in range(4)]
        residues.append(determinant(aa))
        exact("fraction_normal_symbol_"+str(idx),residues,"Python Fraction")

    for idx, pp in enumerate([
        [[1,2,0,0],[0,1,1,0],[0,0,2,1],[1,0,0,3]],
        [[2,0,1,0],[0,3,0,1],[1,0,2,0],[0,1,0,2]],
    ]):
        mm = [[int(M[i,j]) for j in range(4)] for i in range(4)]
        ee = [[sum(Q(pp[i][l])*mm[j][l] for l in range(4)) for j in range(4)]+[0]
              for i in range(4)]
        ee.append([Q(2),Q(-3),Q(5),Q(7),Q(1)])
        exact("fraction_volume_pullback_"+str(idx),determinant(ee)-determinant(mm)*determinant(pp),"Python Fraction")

    # Conditional diagnostic operator, explicitly not derived from UBT here.
    t,x,y,z,r = s.symbols("t x y z r", real=True)
    omega,kx,ky,kz,ks,m,sigma = s.symbols("omega kx ky kz ks m sigma", real=True)
    mode = s.exp(s.I*(-omega*t+kx*x+ky*y+kz*z+ks*r))
    op = s.diff(mode,t,2)-sum(s.diff(mode,c,2) for c in [x,y,z])-sigma*s.diff(mode,r,2)+m*m*mode
    polynomial = -omega**2+kx**2+ky**2+kz**2+sigma*ks**2+m*m
    exact("conditional_dispersion_polynomial", op/mode-polynomial)
    gamma = s.symbols("gamma", positive=True)
    growing = s.exp(gamma*t+s.I*gamma*r)
    exact("extra_timelike_high_frequency_growth", s.diff(growing,t,2)+s.diff(growing,r,2))

    return {"date":"2026-10-10", "passed":all(c["passed"] for c in checks),
            "checks_count":len(checks), "checks":checks,
            "python":platform.python_version(), "sympy":s.__version__,
            "scope":"Common-coordinate composite volume; flat Lorentz-slice normal Hessian of the existing symplectic action; conditional propagation/signature diagnostics.",
            "not_tested":"Selected microscopic action, general derivative/composite curved connection, nonlinear constraint quotient, global/boundary modes, full C5 reality prescription, observations.",
            "lean_status":"LEAN-PENDING: no Lean/Lake executables in this runtime and no checked formalization of the local exterior/PDE theorem supplied."}


if __name__ == "__main__":
    result = verify()
    Path(__file__).with_name("wave_dynamics_results.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({key:result[key] for key in ["passed","checks_count","python","sympy"]}))
