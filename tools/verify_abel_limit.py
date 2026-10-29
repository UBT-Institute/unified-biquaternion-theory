#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
"""Independent exact/numerical checks; no extrapolation to RH."""
import json
from fractions import Fraction
import mpmath as mp
import sympy as sp


def verify():
    # Infinite geometric example: a(n)=1, w(n)=q^n, 0<q<1.
    # B(k)=(k+1)(1-q)q^(k+1); its sum is q/(1-q).
    q = sp.symbols('q', positive=True)
    n = sp.symbols('n', integer=True, nonnegative=True)
    L = q/(1-q)
    S = q*(1-q**n)/(1-q)
    boundary = n*q**(n+1)
    tail = q**(n+1)*((n+1)-n*q)/(1-q)
    assert sp.simplify(S-L-boundary+tail) == 0
    x, R, delta = sp.symbols('x R delta', positive=True)
    s = sp.symbols('s')
    assert sp.simplify(sp.diff(x**(-s), x) + s*x**(-s-1)) == 0
    assert sp.simplify(sp.integrate(x**(-delta-1), (x,R,sp.oo)) - R**(-delta)/delta) == 0
    rational_cases = 0
    for qv in (Fraction(1,4), Fraction(1,2), Fraction(3,4)):
        for N in (0, 1, 2, 7, 31):
            partial = sum((qv**k for k in range(1,N+1)), Fraction(0))
            limit = qv/(1-qv)
            B = N*qv**(N+1)
            T = qv**(N+1)*((N+1)-N*qv)/(1-qv)
            assert partial-limit == B-T
            assert abs(partial-limit) <= abs(B)+T
            rational_cases += 1
    # Conditional original series: a(n)=(-1)^(n-1), w(n)=1/n.
    # A(n) is 1 for odd n and 0 for even n. Transformed terms are
    # nonnegative; their tail is at most sum_{n>N} 1/(n(n+1))=1/(N+1).
    mp.mp.dps = 70
    errors = []
    for N in (0, 1, 2, 7, 32, 129):
        S = sum((Fraction((-1)**(k-1),k) for k in range(1,N+1)),Fraction(0))
        err = abs(mp.mpf(S.numerator)/S.denominator-mp.log(2))
        bound = Fraction(N%2, N+1)+Fraction(1,N+1)
        assert err <= mp.mpf(bound.numerator)/bound.denominator
        errors.append(float(err))
    # Why the boundary hypothesis cannot be dropped: a(n)=w(n)=1.
    # All transformed terms vanish, but S_N=N diverges.
    for N in (1, 2, 10):
        assert sum([1]*N) == N
        assert sum(k*(1-1) for k in range(1,N+1)) == 0
    return dict(result='PASS',sympy=sp.__version__,mpmath=mp.__version__,
                rational_cases=rational_cases,alternating_cases=len(errors),
                precision_digits=70,boundary_counterexample=True,power_weight_calculus='symbolic derivative and tail integral PASS; not Lean verified',
                scope='finite diagnostics and symbolic identities; infinite transfer proved in Lean; no RH proof')

if __name__ == '__main__':
    print(json.dumps(verify(),indent=2))
