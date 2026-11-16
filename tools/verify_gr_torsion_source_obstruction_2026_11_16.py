"""Exact symbolic toy audit of quadratic auxiliary torsion elimination.

This verifies polynomial identities in a 3-channel toy system, not the
canonical UBT 24-component Theta spin current or its composite variation.
"""
import sympy as s

k = s.symbols("k0:3", real=True)
j = s.symbols("j0:3", real=True)
a, b, c = s.symbols("a b c", real=True, nonzero=True)
M = s.diag(a, b, c)
K = s.Matrix(k)
J = s.Matrix(j)
L = (J.T * K)[0] + s.Rational(1, 2) * (K.T * M * K)[0]
gradient = s.Matrix([s.diff(L, v) for v in k])
assert s.simplify(gradient - (J + M * K)) == s.zeros(3, 1)
assert gradient.subs(dict.fromkeys(k, 0)) == J
Kstar = -M.inv() * J
assert s.simplify(
    L.subs(dict(zip(k, Kstar))) +
    s.Rational(1, 2) * (J.T * M.inv() * J)[0]
) == 0
assert s.simplify(M.det() - a * b * c) == 0
print("PASS quadratic elimination and source obstruction (3-channel toy)")
