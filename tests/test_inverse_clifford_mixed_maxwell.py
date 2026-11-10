"""Exact finite algebra checks: mixed even-odd first-order Maxwell counterexample.

Verifies flat-background algebra, not the full dynamical UBT constraints.
"""
import sympy as s
from itertools import combinations


def test_first_order_maxwell_elimination():
    b = s.symbols("b0:6", real=True)
    f = s.symbols("f0:6", real=True)
    metric = [1, -1, -1, -1]
    signs = [metric[i] * metric[j] for i, j in combinations(range(4), 2)]
    L = sum(signs[k] * (b[k] ** 2 / s.Integer(2) - b[k] * f[k])
            for k in range(6))
    for k in range(6):
        assert s.diff(L, b[k]) == signs[k] * (b[k] - f[k])
    reduced = s.expand(L.subs(dict(zip(b, f))))
    assert s.expand(reduced + sum(signs[k] * f[k] ** 2 / s.Integer(2)
                                  for k in range(6))) == 0


def test_bilinear_grade_flip_not_invariant():
    b, f = s.symbols("b f")
    L = b * b / s.Integer(4) - b * f / s.Integer(2)
    assert s.simplify(L.subs(f, -f) - L) == b * f


def test_mixed_hessian_induces_kinetic():
    a, p = s.symbols("a p", nonzero=True)
    H = s.Matrix([[a, p], [p, 0]])
    assert s.simplify(-H[1, 0] * H[0, 0] ** -1 * H[0, 1]
                      + p * p / a) == 0
    assert H.det() == -p * p


def test_antisymmetric_bivector_gives_conserved_euler_current():
    q = s.symbols("q0:4")
    B = s.Matrix(4, 4, lambda i, j: 0 if i == j else
                 s.Symbol(f"B{min(i, j)}{max(i, j)}") *
                 (1 if i < j else -1))
    current = [sum(q[mu] * B[mu, nu] for mu in range(4))
               for nu in range(4)]
    assert s.expand(sum(q[nu] * current[nu] for nu in range(4))) == 0
