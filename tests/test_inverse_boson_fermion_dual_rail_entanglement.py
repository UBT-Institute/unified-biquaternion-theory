"""Matched fixed-number boson/fermion dual-rail logical Bell correlations.

Tests the common logical subspace, not the distinct microscopic CAR/CCR algebras.
"""
import sympy as sp


def _state():
    return sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)


def _expect(A, B):
    psi = _state()
    return sp.simplify((psi.T * sp.kronecker_product(A, B) * psi)[0])


def test_bell_state_normalized():
    psi = _state()
    assert (psi.T * psi)[0] == 1


def test_local_state_maximally_mixed():
    psi = _state()
    rho = psi * psi.T
    reduced = sp.Matrix(2, 2, lambda i, j:
                        sum(rho[2*i+k, 2*j+k] for k in range(2)))
    assert reduced == sp.eye(2) / 2


def test_equal_logical_correlations():
    X = sp.Matrix([[0, 1], [1, 0]])
    Z = sp.diag(1, -1)
    assert _expect(X, X) == 1
    assert _expect(Z, Z) == 1


def test_chsh_reaches_quantum_maximum():
    X = sp.Matrix([[0, 1], [1, 0]])
    Z = sp.diag(1, -1)
    B0 = (Z+X)/sp.sqrt(2)
    B1 = (Z-X)/sp.sqrt(2)
    s = _expect(Z, B0)+_expect(Z, B1)+_expect(X, B0)-_expect(X, B1)
    assert sp.simplify(s-2*sp.sqrt(2)) == 0
