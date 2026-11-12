"""Finite-dimensional quantum split-jet measure regression.

Exact algebra only; not a continuum path integral or anomaly calculation.
"""
import sympy as sp


def test_parent_constraint_shift_and_jacobians():
    E = sp.Matrix(sp.symbols("e0:3"))
    X = sp.Matrix(sp.symbols("x0:2"))
    Q = sp.Matrix(sp.symbols("q0:3"))
    eps = sp.Matrix(sp.symbols("eps0:2"))
    s = sp.symbols("s", nonzero=True)
    D = sp.Matrix([[1, 2], [0, 3], [4, 5]])
    chi = s * E - D * X - Q

    assert chi.jacobian(Q) == -sp.eye(3)
    assert abs(chi.jacobian(Q).det()) == 1
    assert chi.jacobian(E).det() == s**3

    shifted = s * E - D * (X + eps) - (Q - D * eps)
    assert sp.simplify(shifted - chi) == sp.zeros(3, 1)

    # Gauge X=0 under X -> X+eps has a field-independent FP determinant.
    assert (X + eps).jacobian(eps).det() == 1


def test_image_reparametrization_has_no_intrinsic_q_factor():
    s = sp.symbols("s", positive=True)
    e, x, q = sp.symbols("e x q")
    # Replacing q by chi at fixed (e,x) has absolute Jacobian one.
    chi = s * e - x - q
    assert sp.diff(chi, q) == -1
    # Replacing e by chi at fixed (q,x) instead has Jacobian s.
    assert sp.diff(chi, e) == s
