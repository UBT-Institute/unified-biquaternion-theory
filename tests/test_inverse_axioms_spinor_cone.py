"""Algebraic regression tests for the inverse-axioms SR/qubit intersection.

These tests verify finite matrix identities, not a theorem of physical uniqueness.
Run: python -m pytest -q tests/test_inverse_axioms_spinor_cone.py
"""
import sympy as sp


def test_pauli_biquaternion_basis_products():
    I = sp.I
    p = (
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -I], [I, 0]]),
        sp.Matrix([[1, 0], [0, -1]]),
    )
    q = tuple(-I * a for a in p)
    for a in range(3):
        for b in range(3):
            rhs = (-sp.eye(2) if a == b else sp.zeros(2))
            rhs += sum((sp.LeviCivita(a, b, c) * q[c] for c in range(3)), sp.zeros(2))
            assert q[a] * q[b] == rhs


def test_hermitian_determinant_is_lorentz_form():
    t, x, y, z = sp.symbols("t x y z", real=True)
    X = sp.Matrix([[t + z, x - sp.I * y], [x + sp.I * y, t - z]])
    assert sp.simplify(X.det() - (t**2 - x**2 - y**2 - z**2)) == 0
    assert X == X.conjugate().T


def test_qubit_bloch_ball_determinant():
    x, y, z = sp.symbols("x y z", real=True)
    rho = sp.Matrix([[1 + z, x - sp.I * y], [x + sp.I * y, 1 - z]]) / 2
    assert sp.simplify(rho.det() - (1 - x**2 - y**2 - z**2)/4) == 0
    assert sp.trace(rho) == 1


def test_sl2c_preserves_det_but_boost_not_qubit_trace():
    a = sp.symbols("a", real=True)
    A = sp.diag(sp.exp(a / 2), sp.exp(-a / 2))
    X = sp.eye(2)
    transformed = A * X * A.conjugate().T
    assert sp.simplify(A.det() - 1) == 0
    assert sp.simplify(transformed.det() - X.det()) == 0
    assert sp.simplify(sp.trace(transformed) - 2 * sp.cosh(a)) == 0
    assert sp.simplify(sp.trace(transformed) - sp.trace(X)) != 0
