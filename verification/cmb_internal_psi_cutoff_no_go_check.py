#!/usr/bin/env python3
"""Kinematic regression check for the internal-circle CMB IR-cutoff no-go."""
import sympy as sp

k, R, m0 = sp.symbols('k R m0', positive=True)
n = sp.symbols('n', integer=True)

omega2 = k**2 + m0**2 + n**2/R**2
assert sp.simplify(omega2.subs(n, 0) - (k**2 + m0**2)) == 0
assert sp.diff(omega2.subs(n, 0), R) == 0
mn2 = sp.simplify(omega2 - k**2)
assert mn2 == m0**2 + n**2/R**2

print('PASS: S1_psi compactification yields a KK mass tower, not a spatial k_min')
