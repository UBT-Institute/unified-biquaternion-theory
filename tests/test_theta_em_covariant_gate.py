"""Scoped SymPy gates for a full-complex Theta EM candidate.

Verifies kinematic identities only, not physical photons/Maxwell/Einstein dynamics.
"""
import sympy as sp


def pfaffian(F):
    return sp.factor(
        F[0, 1] * F[2, 3]
        - F[0, 2] * F[1, 3]
        + F[0, 3] * F[1, 2]
    )


def test_covariant_phase_twoform_is_decomposable():
    p = sp.symbols("p0:4", real=True)
    r = sp.symbols("r0:4", real=True)
    F = sp.Matrix(4, 4, lambda i, j: p[i] * r[j] - p[j] * r[i])
    assert pfaffian(F) == 0


def test_raw_phase_current_is_non_simple_but_covariant_one_is_simple():
    t, x, y, z, a, b = sp.symbols("t x y z a b", real=True)
    coords = [t, x, y, z]
    eta = sp.diag(1, -1, -1, -1)
    A = sp.Matrix([t, x, y, z])
    C = sp.Matrix([1, a * y, 0, b * t])
    dot = lambda p, q: (p.T * eta * q)[0]
    u, v, ell = dot(C, C), dot(A, A), dot(A, C)
    norm = u + v
    raw = sp.Matrix([
        (dot(C, A.diff(q)) - dot(A, C.diff(q))) / norm
        for q in coords
    ])
    Fraw = sp.Matrix(
        4, 4, lambda i, j: sp.diff(raw[j], coords[i])
        - sp.diff(raw[i], coords[j])
    )
    origin = {t: 0, x: 0, y: 0, z: 0}
    assert pfaffian(Fraw.subs(origin)) == -4 * a * b

    # D C = 0 in the induced Lorentz+Weyl connection implies
    # a_cov=(u/norm)*d(ell/u), so F_cov=d(u/norm) wedge d(ell/u).
    p, r = u / norm, ell / u
    dp = [sp.diff(p, q).subs(origin) for q in coords]
    dr = [sp.diff(r, q).subs(origin) for q in coords]
    Fcov_origin = sp.Matrix(
        4, 4, lambda i, j: sp.simplify(
            dp[i] * dr[j] - dp[j] * dr[i]
        )
    )
    assert Fcov_origin == sp.zeros(4)


def test_composite_connection_enforces_entire_reality_constraint():
    t, y, a, b = sp.symbols("t y a b", real=True)
    sig1 = sp.Matrix([[0, 1], [1, 0]])
    sig3 = sp.diag(1, -1)
    H = sp.eye(2) + a * y * sig1 + b * t * sig3
    for coordinate in (t, y):
        dH = H.diff(coordinate)
        trace = sp.trace(H.inv() * dH)
        omega = -sp.Rational(1, 2) * dH * H.inv() + (
            sp.Rational(1, 4) * trace * sp.eye(2)
        )
        w = -sp.Rational(1, 2) * trace
        assert sp.simplify(sp.trace(omega)) == 0
        assert (dH + omega * H + H * omega.H + w * H).applyfunc(
            sp.simplify
        ) == sp.zeros(2)
    assert sp.simplify(H.det() - (1 - a**2 * y**2 - b**2 * t**2)) == 0


def test_relative_traceless_channel_has_non_simple_value_but_same_flat_tetrad():
    t, x, y, z, T = sp.symbols("t x y z T", real=True, nonzero=True)
    sig = [
        sp.eye(2),
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -sp.I], [sp.I, 0]]),
        sp.diag(1, -1),
    ]
    bar_theta = sp.I * (
        (T + t) * sig[0] + x * sig[1] + y * sig[2] + z * sig[3]
    )
    desired = (1 + sp.I) * sp.I * sig[3]
    constant_offset = desired * (sp.I * T * sig[0])
    theta = bar_theta + constant_offset

    for coord in (t, x, y, z):
        assert theta.diff(coord) == bar_theta.diff(coord)
        assert (theta.diff(coord) + theta.diff(coord).H) == sp.zeros(2)

    origin = {t: 0, x: 0, y: 0, z: 0}
    relative = theta.subs(origin) * bar_theta.subs(origin).inv()
    traceless = relative - sp.trace(relative) / 2 * sp.eye(2)
    assert sp.simplify(traceless - desired) == sp.zeros(2)

    # Conventional real two-form for E_z=B_z=1; nonzero F wedge F.
    F = sp.zeros(4)
    F[0, 3], F[3, 0] = 1, -1
    F[1, 2], F[2, 1] = 1, -1
    assert pfaffian(F) == 1
