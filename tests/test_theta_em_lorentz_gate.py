"""Conditional Lorentz representation gates for a single M_2(C) Theta.

These tests do NOT select UBT's physical Lorentz representation or dynamics.
"""
import sympy as sp

b = sp.symbols("b", real=True)
I2 = sp.eye(2)
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3 = sp.diag(1, -1)
e = [sp.I * si for si in (s1, s2, s3)]
S = sp.diag(sp.exp(b / 2), sp.exp(-b / 2))
Sinv = sp.diag(sp.exp(-b / 2), sp.exp(b / 2))


def simplify_matrix(A):
    return A.applyfunc(lambda c: sp.simplify(sp.expand(c)))


def components(X):
    return [sp.simplify(sp.trace(X) / 2)] + [
        sp.simplify(-sp.trace(ek * X) / 2) for ek in e
    ]


def test_similarity_keeps_scalar_and_selfdual_complex_threevector():
    z0, z1, z2, z3 = sp.symbols("z0 z1 z2 z3")
    X = z0 * I2 + z1 * e[0] + z2 * e[1] + z3 * e[2]
    c = components(S * X * Sinv)
    expected = [
        z0,
        sp.cosh(b) * z1 - sp.I * sp.sinh(b) * z2,
        sp.I * sp.sinh(b) * z1 + sp.cosh(b) * z2,
        z3,
    ]
    assert all(
        sp.simplify(sp.expand_trig(x - y).rewrite(sp.exp)) == 0
        for x, y in zip(c, expected)
    )
    assert sp.simplify(
        sp.expand_trig(
            sum(c[i] ** 2 for i in (1, 2, 3)) -
            (z1**2 + z2**2 + z3**2)
        ).rewrite(sp.exp)
    ) == 0
    assert sp.simplify(sp.trace(S * (X - z0 * I2) * Sinv)) == 0


def test_congruence_does_not_preserve_scalar_vector_split():
    transformed_scalar = components(S * I2 * S.H)
    assert transformed_scalar == [
        sp.cosh(b), 0, 0, -sp.I * sp.sinh(b)
    ]
    transformed_vector = components(S * e[2] * S.H)
    assert transformed_vector == [
        sp.I * sp.sinh(b), 0, 0, sp.cosh(b)
    ]


def test_congruence_preserves_lorentz_reality_but_similarity_does_not():
    # W_L = i Herm_2; temporal i I and spatial e_i are anti-Hermitian.
    t, x, y, z = sp.symbols("t x y z", real=True)
    X = sp.I * t * I2 + x * e[0] + y * e[1] + z * e[2]
    transformed = S * X * S.H
    assert simplify_matrix(transformed + transformed.H) == sp.zeros(2, 2)
    transformed_similarity = S * e[0] * Sinv
    assert (
        simplify_matrix(transformed_similarity + transformed_similarity.H)
        != sp.zeros(2, 2)
    )


def test_constant_magnetic_field_can_be_first_jet_of_vector_potential():
    x, y, B = sp.symbols("x y B", real=True)
    A_x = sp.Integer(0)
    A_y = B * x
    F_xy = sp.diff(A_y, x) - sp.diff(A_x, y)
    assert F_xy == B
    lam = sp.sin(x * y) + x**3 * y
    assert sp.simplify(
        sp.diff(A_y + sp.diff(lam, y), x)
        - sp.diff(A_x + sp.diff(lam, x), y) - B
    ) == 0
