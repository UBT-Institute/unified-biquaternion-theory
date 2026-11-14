"""Restricted symbolic gates for full complex Theta, Lorentz pair and a composite relative one-form.

Only algebra and kinematics are tested, NOT Maxwell dynamics or the full UBT action.
"""
import sympy as sp

SIGMA = [
    sp.eye(2),
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.diag(1, -1),
]
ETA = sp.diag(1, -1, -1, -1)


def sigma_vector(v):
    return sum((v[j] * SIGMA[j] for j in range(4)), sp.zeros(2))


def minkowski_square(v):
    return (v.T * ETA * v)[0]


def test_two_real_fourvectors_quadratic_signature():
    A = sp.Matrix(sp.symbols("a0:4", real=True))
    C = sp.Matrix(sp.symbols("c0:4", real=True))
    X = sp.I * sigma_vector(A) - sigma_vector(C)
    adj = sp.Matrix([[X[1, 1], -X[0, 1]], [-X[1, 0], X[0, 0]]])
    assert sp.simplify(sp.trace(adj * X.H) - 2 * (minkowski_square(A) + minkowski_square(C))) == 0
    assert sp.simplify(sp.re(sp.expand(X.det())) - (minkowski_square(C) - minkowski_square(A))) == 0
    assert sp.diag(*([1, -1, -1, -1] * 2)).eigenvals() == {1: 2, -1: 6}
    assert sp.diag(*([-1, 1, 1, 1, 1, -1, -1, -1])).eigenvals() == {1: 4, -1: 4}


def test_pure_pair_keeps_two_hermiticity_parities_separate():
    a, b, c, d, e, f = sp.symbols("a b c d e f", real=True)
    omega = (a + sp.I * b) * SIGMA[1] + (c + sp.I * d) * SIGMA[2] + (e + sp.I * f) * SIGMA[3]
    aa = sp.Matrix(sp.symbols("u0:4", real=True))
    cc = sp.Matrix(sp.symbols("v0:4", real=True))
    d_aa = sp.Matrix(sp.symbols("du0:4", real=True))
    d_cc = sp.Matrix(sp.symbols("dv0:4", real=True))
    X = sp.I * sigma_vector(aa) - sigma_vector(cc)
    DX = sp.I * sigma_vector(d_aa) - sigma_vector(d_cc) + omega * X + X * omega.H
    DC = sigma_vector(d_cc) + omega * sigma_vector(cc) + sigma_vector(cc) * omega.H
    assert (DX + DX.H + 2 * DC).applyfunc(sp.simplify) == sp.zeros(2)


def test_metric_compatible_gradient_soldered_potential_is_exact():
    a = sp.Matrix(sp.symbols("a0:4", real=True))
    d_a = sp.Matrix(sp.symbols("da0:4", real=True))
    w01, w02, w03, w12, w13, w23 = sp.symbols("w01 w02 w03 w12 w13 w23", real=True)
    omega_lower = sp.Matrix(
        [[0, w01, w02, w03],
         [-w01, 0, w12, w13],
         [-w02, -w12, 0, w23],
         [-w03, -w13, -w23, 0]]
    )
    omega = ETA * omega_lower
    e = d_a + omega * a
    assert sp.simplify((a.T * ETA * e)[0] - (a.T * ETA * d_a)[0]) == 0


def test_derived_relative_connection_generates_constant_b_on_regular_tetrad():
    t, x, y, z, k, B = sp.symbols("t x y z k B", real=True, nonzero=True)
    h = sp.sqrt(1 + t**2 - x**2 - z**2 - (B / k) * y)
    A = sp.Matrix([t, x, h, z])
    f = sp.exp(k * x)
    theta = f * sp.eye(2) + sp.I * sigma_vector(A)
    w = [0, -k, 0, 0]
    coords = [t, x, y, z]
    Ds = [sp.diff(theta, coords[mu]) + w[mu] * theta for mu in range(4)]

    # Work on the real local patch where the radicand of h is positive.
    # There the Pauli coefficients of the anti-Hermitian piece are real.
    assert sp.simplify(sp.diff(f, x) + w[1] * f) == 0
    e = sp.Matrix(
        4, 4,
        lambda mu, a: sp.simplify(sp.trace(SIGMA[a] * Ds[mu]) / (2 * sp.I))
    )
    assert sp.simplify(e.det().subs({t: 0, x: 0, y: 0, z: 0}) + B / (2 * k)) == 0
    potential = sp.simplify(e * ETA * A)
    fxy = sp.simplify(sp.diff(potential[2], x) - sp.diff(potential[1], y))
    assert fxy == B
    assert sp.simplify(minkowski_square(A) - ((B / k) * y - 1)) == 0
    assert sp.simplify(-sp.Rational(1, 2) * sp.diff(sp.log(f**2), x) + k) == 0
