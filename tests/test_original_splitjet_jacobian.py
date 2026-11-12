"""Exact timelike split-jet measure factor in the rest-frame chart.

This tests a local finite Jacobian, not the continuum functional measure.
"""
import sympy as sp


def test_one_column_jacobian():
    r = sp.symbols("r", positive=True)
    b1, b2, b3, w, z12, z13, z23 = sp.symbols(
        "b1 b2 b3 w z12 z13 z23"
    )
    old = sp.Matrix([b1, b2, b3, w, z12, z13, z23])
    new = sp.Matrix([r*b1, r*b2, r*b3, r*w, z12, z13, z23])
    assert sp.factor(new.jacobian(old).det()) == r**4


def test_four_column_jacobian_and_tetrad():
    r, s = sp.symbols("r s", positive=True)
    J_image = sp.diag(*([r]*4 + [1]*3))
    J_four = sp.diag(*([r]*4 + [1]*3)*4)
    assert J_image.det() == r**4
    assert sp.factor(J_four.det()) == r**16
    assert sp.factor((s**16)/J_four.det()) == (s/r)**16


def test_carrier_dependent_block_triangularity():
    r, x, b, z = sp.symbols("r x b z", positive=True)
    # A toy carrier-dependent boost coordinate: the off-diagonal derivative
    # does not enter the determinant when carrier x is retained.
    new = sp.Matrix([x, r*b + x*z, z])
    old = sp.Matrix([x, b, z])
    assert new.jacobian(old).det() == r
