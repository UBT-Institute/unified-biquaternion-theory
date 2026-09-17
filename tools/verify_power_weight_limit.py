#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
"""Independent diagnostics of the conditional power-weight transfer."""
import json
import mpmath as mp
import sympy as sp


def verify():
    x, R, d = sp.symbols('x R d', positive=True)
    s = sp.symbols('s')
    assert sp.simplify(sp.diff(x**(-s),x)+s*x**(-s-1)) == 0
    assert sp.simplify(sp.integrate(x**(-d-1),(x,R,sp.oo))-R**(-d)/d) == 0
    mp.mp.dps = 80
    count = 0
    for sv in (mp.mpc('0.3','2'),mp.mpc('0.75','0.4'),mp.mpc('2.5','1.7')):
        target = mp.altzeta(sv)
        for N in (1,3,32,256):
            direct = sum(((-1)**(n-1)*mp.power(n,-sv) for n in range(1,N+1)),mp.mpc(0))
            transformed = sum((mp.power(n,-sv)-mp.power(n+1,-sv)
                               for n in range(1,N+1) if n%2),mp.mpc(0))
            boundary = (N%2)*mp.power(N+1,-sv)
            assert abs(direct-transformed-boundary) < mp.mpf('1e-70')
            bound = (1+abs(sv)/sv.real)*mp.power(N,-sv.real)
            assert abs(direct-target) <= bound
            count += 1
    for sv in (mp.mpc('1.5','0.4'),mp.mpc('2.25','1.7')):
        for N in (1,3,32,256):
            direct = sum((mp.power(n,-sv) for n in range(1,N+1)),mp.mpc(0))
            bound = (1+abs(sv)/(sv.real-1))*mp.power(N,1-sv.real)
            assert abs(direct-mp.zeta(sv)) <= bound
            count += 1
    # Context check: an exponential cutoff, not an ordinary divergent sum.
    t,q=sp.symbols('t q')
    F=sp.exp(-t)/(1-sp.exp(-t))**2
    assert sp.series(F,t,0,4).removeO().expand() == t**(-2)-sp.Rational(1,12)+t**2/240
    assert sp.cancel(q/(1-q)**2-(1/q)/(1-1/q)**2) == 0
    return dict(result='PASS',sympy=sp.__version__,mpmath=mp.__version__,
                precision_digits=80,nonreal_cases=count,
                cutoff_constant='-1/12',cutoff_scope='CAS only; regularized finite part, not ordinary summation',
                scope='conditional transfer diagnostics; no Mobius cancellation bound or RH proof')

if __name__ == '__main__':
    print(json.dumps(verify(),indent=2))
