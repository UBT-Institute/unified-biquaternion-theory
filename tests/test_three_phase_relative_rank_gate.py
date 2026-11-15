"""Exact algebraic gates for a proposed three-commuting-phase UBT track.

This verifies linear algebra only; it does not prove an emergent QED sector.
"""
import sympy as sp


def test_relative_phase_rank_and_common_kernel():
    B = sp.Matrix([[1, -1, 0], [0, 1, -1]])
    assert B.rank() == 2
    assert B.nullspace() == [sp.Matrix([1, 1, 1])]


def test_three_phase_laplacian_spectrum():
    K = sp.Matrix([[2, -1, -1], [-1, 2, -1], [-1, -1, 2]])
    assert K.eigenvals() == {sp.Integer(0): 1, sp.Integer(3): 2}
    assert K * sp.Matrix([1, 1, 1]) == sp.zeros(3, 1)


def test_relative_quadratic_identity():
    x, y, z = sp.symbols("x y z")
    v = sp.Matrix([x, y, z])
    K = sp.Matrix([[2, -1, -1], [-1, 2, -1], [-1, -1, 2]])
    assert sp.expand((v.T * K * v)[0] - ((x-y)**2+(y-z)**2+(z-x)**2)) == 0


def test_balanced_120_degree_roots():
    omega = sp.exp(2 * sp.pi * sp.I / 3)
    assert sp.simplify(sp.expand_complex(1 + omega + omega**2)) == 0
