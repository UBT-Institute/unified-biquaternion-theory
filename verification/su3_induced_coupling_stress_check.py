#!/usr/bin/env python3
"""Exact/numeric checks for the minimal induced SU(3) coupling benchmark."""
import sympy as sp

pi=sp.pi
Tfund=sp.Rational(1,2)

# Complex scalar triplet: heat-kernel coefficient and canonical 1/(4g^2) match.
C = Tfund / (12*(4*pi)**2)
inv_g2 = sp.simplify(4*C)
assert sp.simplify(inv_g2 - 1/(96*pi**2)) == 0

# Required logarithm for g=1.
required = sp.N(96*pi**2, 20)
assert required > 947 and required < 948

# Representative hierarchy logs.
for N in (1,10,100):
    L = sp.N(96*pi**2/N, 20)
    log10_ratio = sp.N(L/(2*sp.log(10)), 20)
    assert L > 0
    assert log10_ratio > 0

print("PASS: one complex fundamental triplet gives 1/g_ind^2 = I0/(96*pi^2)")
