"""Exact algebraic tests for the Maxwell -> single-Theta wave lift and failed converse.

No test here claims UBT's composite covariant field equation, action,
or physical photon degree-of-freedom selection has been proved.
"""
import sympy as sp

I = sp.I
P = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]),
     sp.Matrix([[0, -I], [I, 0]]), sp.diag(1, -1)]
t, x, y, z, k, eps, a = sp.symbols("t x y z k eps a", real=True)
coords = [t, x, y, z]
origin = {q: 0 for q in coords}


def trfree(X):
    return X - (sp.trace(X) / 2) * sp.eye(2)


def Q(X):
    return -X.diff(t) + sum((X.diff(coords[j]) * P[j]
                             for j in (1, 2, 3)), sp.zeros(2))


def box(X):
    return -X.diff(t, 2) + X.diff(x, 2) + X.diff(y, 2) + X.diff(z, 2)


def zero(X):
    return X.applyfunc(sp.simplify) == sp.zeros(*X.shape)


def test_first_order_pauli_operator_is_all_of_source_free_maxwell():
    F = [sp.Function("F%d" % j)(t, x, y, z) for j in range(3)]
    Phi = I * sum((F[j] * P[j+1] for j in range(3)), sp.zeros(2))
    div = F[0].diff(x) + F[1].diff(y) + F[2].diff(z)
    curl = [
        F[2].diff(y) - F[1].diff(z),
        F[0].diff(z) - F[2].diff(x),
        F[1].diff(x) - F[0].diff(y),
    ]
    result = I * div * P[0] + sum(
        ((curl[j] - I * F[j].diff(t)) * P[j+1] for j in range(3)),
        sp.zeros(2))
    assert zero(Q(Phi) - result)


def test_exact_maxwell_plane_wave_lifts_to_box_theta_zero():
    phase = sp.exp(I * k * (z - t))
    Phi = I * phase * (P[1] + I * P[2])
    bar = P[0] + I * sum((coords[j] * P[j] for j in range(4)), sp.zeros(2))
    theta = (P[0] + eps * Phi) * bar
    assert zero(Q(Phi))
    assert zero(box(Phi))
    assert zero(box(theta))
    assert zero(trfree(theta * bar.inv()) - eps * Phi)


def test_composite_hermitian_compensator_gives_real_nondegenerate_tetrad():
    phase = sp.exp(I * k * (z - t))
    Phi = I * phase * (P[1] + I * P[2])
    bar = P[0] + I * sum((coords[j] * P[j] for j in range(4)), sp.zeros(2))
    theta = (P[0] + eps * Phi) * bar
    H = (theta + theta.H) / 2
    H0 = H.subs(origin)
    assert sp.simplify(H0.det() - (1 - eps**2)) == 0
    theta0 = theta.subs(origin)
    E = []
    for coord in coords:
        dh = H.diff(coord).subs(origin)
        trace = sp.trace(H0.inv() * dh)
        omega = -dh * H0.inv()/2 + trace*sp.eye(2)/4
        w = -trace / 2
        Dtheta = theta.diff(coord).subs(origin) + omega*theta0 \
            + theta0*omega.H + w*theta0
        assert zero(Dtheta + Dtheta.H)
        E.append(Dtheta)
    substitutions = {eps: sp.Rational(1, 10), k: 2}
    legs = sp.Matrix(4, 4, lambda mu, j: sp.simplify(
        sp.trace(P[j] * E[mu].subs(substitutions)) / (2 * I)))
    assert legs.det() == sp.Rational(9800, 9801)


def test_box_theta_and_flat_tetrad_do_not_imply_maxwell():
    bar = P[0] + I * sum((coords[j] * P[j] for j in range(4)), sp.zeros(2))
    theta = bar + I * a * P[1]
    assert zero(box(theta))
    assert all(zero(theta.diff(coords[j]) - I * P[j])
               for j in range(4))
    Psi = trfree(theta * bar.inv())
    assert zero(Q(Psi).subs(origin) - a * P[1])


def test_maxwell_symbol_selects_one_complex_helicity_per_frequency_sign():
    u, v, w = sp.symbols("u v w", complex=True)
    k0 = sp.symbols("k0", nonzero=True)
    for omega, expected_v in [(k0, I*u), (-k0, -I*u)]:
        Phi = I * (u*P[1] + v*P[2] + w*P[3])
        symbol = Phi * (omega*P[0] + k0*P[3])
        solutions = sp.solve(list(symbol), [v, w], dict=True)
        assert solutions == [{v: expected_v, w: 0}]
