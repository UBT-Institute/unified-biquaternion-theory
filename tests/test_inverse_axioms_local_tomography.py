"""Exact finite algebra checks for inverse-axiom local tomography (research-only)."""

import sympy as sp


def dim(field, n):
    return {
        "R": n * (n + 1) // 2,
        "C": n * n,
        "H": n * (2 * n - 1),
    }[field]


def test_dimension_gap():
    assert [(f, dim(f, 2), dim(f, 4), dim(f, 2)**2) for f in "RCH"] == [
        ("R", 3, 10, 9),
        ("C", 4, 16, 16),
        ("H", 6, 28, 36),
    ]


def test_complex_tomography_for_general_composites():
    for n in range(2, 8):
        for m in range(2, 8):
            assert dim("C", n * m) == dim("C", n) * dim("C", m)


def test_real_local_tomography_witness():
    J = sp.Matrix([[0, -1], [1, 0]])
    K = sp.kronecker_product(J, J)
    assert K == K.T and sp.trace(K * K) == 4
    for A in [sp.Matrix([[a, b], [b, c]]) for a, b, c in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]]:
        for B in [sp.Matrix([[a, b], [b, c]]) for a, b, c in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]]:
            assert sp.trace(K * sp.kronecker_product(A, B)) == 0

    # Distinct positive real 4x4 density matrices invisible to local product tests.
    rho_plus = sp.eye(4) / 4 + K / 8
    rho_minus = sp.eye(4) / 4 - K / 8
    assert sorted(rho_plus.eigenvals().keys()) == [sp.Rational(1, 8), sp.Rational(3, 8)]
    assert all(mult == 2 for mult in rho_plus.eigenvals().values())
    assert sorted(rho_minus.eigenvals().keys()) == [sp.Rational(1, 8), sp.Rational(3, 8)]
    assert rho_plus != rho_minus


def test_quaternion_dimension_mismatch():
    # This applies to the naive H_4(H) model, not every quaternionic composite.
    assert dim("H", 4) != dim("H", 2) * dim("H", 2)
