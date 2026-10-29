#!/usr/bin/env python3
"""Exact symbolic check of the S1 heat-kernel/Jacobi parameter map."""

import sympy as sp

n, L, s, dpsi = sp.symbols("n L s dpsi", nonzero=True)
pi = sp.pi
I = sp.I

z_theta = dpsi / L
tau_theta = 4*pi*I*s / L**2

jacobi_exponent = pi*I*n**2*tau_theta + 2*pi*I*n*z_theta
heat_exponent = -(2*pi*n/L)**2*s + 2*pi*I*n*dpsi/L

assert sp.simplify(jacobi_exponent - heat_exponent) == 0
assert sp.simplify(tau_theta.subs(L, 2*pi*sp.Symbol("R", positive=True))
                   - I*s/(pi*sp.Symbol("R", positive=True)**2)) == 0

print("PASS: S1 heat-kernel theta argument and modulus match exactly.")
