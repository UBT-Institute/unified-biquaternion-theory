#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
"""Independent exact finite checks; the all-cutoff proof is in Lean."""
import json
from fractions import Fraction
import sympy as sp
from verify_residue_moebius_argument_principle import check_dirichlet_coefficients, mobius


def verify():
    check_dirichlet_coefficients(500)
    cases = 0
    for n in (0, 1, 2, 3, 8, 31, 100):
        a = [0] + [mobius(k) for k in range(1, n + 1)]
        A = [sum(a[:k + 1]) for k in range(n + 1)]
        for w in (lambda k: Fraction(1, k*k), lambda k: Fraction((-1)**k, k),
                  lambda k: Fraction(3), lambda k: Fraction(0)):
            lhs = sum((a[k]*w(k) for k in range(1, n + 1)), Fraction(0))
            rhs = A[n]*w(n + 1) + sum((A[k]*(w(k)-w(k+1))
                for k in range(1, n + 1)), Fraction(0))
            assert lhs == rhs, (n, lhs, rhs)
            cases += 1
    # Generic noncommuting matrices test multiplication order and endpoints.
    for n in range(5):
        a = [sp.zeros(2)] + [sp.Matrix(2,2,sp.symbols(f'a{k}_0:4')) for k in range(n)]
        w = [sp.zeros(2)] + [sp.Matrix(2,2,sp.symbols(f'w{k}_0:4')) for k in range(n+1)]
        A = [sum(a[:k+1], sp.zeros(2)) for k in range(n+1)]
        lhs = sum((a[k]*w[k] for k in range(1,n+1)), sp.zeros(2))
        rhs = A[n]*w[n+1]+sum((A[k]*(w[k]-w[k+1]) for k in range(1,n+1)),sp.zeros(2))
        assert (lhs-rhs).applyfunc(sp.expand) == sp.zeros(2)
    return dict(result='PASS', coefficient_cutoff=500, rational_abel_cases=cases,
                symbolic_matrix_cases=5, scope='finite independent checks; not an RH proof')

if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
