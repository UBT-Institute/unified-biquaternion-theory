"""Finite matrix controls for the conditional multi-observer Z2 winding result.

No full UBT action, physical observer instrument or gravitational stability is proved.
"""
import sympy as sp

I2 = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.diag(1, -1)
N0 = I2
N1 = sp.diag(2, sp.Rational(1, 2))
N2 = sp.Matrix([[2, 1], [1, 1]])


def clock_inverse_sqrt(n):
    return (I2 + n.inv()) / sp.sqrt(sp.trace(n) + 2)


def rho(theta, n):
    b = clock_inverse_sqrt(n)
    t = b * theta * b
    q = sp.simplify(t * t.H)
    return sp.simplify(q / sp.trace(q))


def test_three_clocks_are_genuine_positive_unit_det():
    for n in (N0, N1, N2):
        assert n.det() == 1
        assert n[0, 0] > 0
        assert n.is_symmetric()
    assert N2.eigenvals()


def test_complex_scalar_is_invisible_for_all_observer_clocks():
    theta = sp.Matrix([[1, 1 + sp.I], [2 - sp.I, 3]])
    assert theta.det() != 0
    for n in (N0, N1, N2):
        assert sp.simplify(rho(theta, n) - rho((2 + 3 * sp.I) * theta, n)) == sp.zeros(2)


def test_exact_even_shift_of_determinant_winding():
    m, k, angle = sp.symbols("m k angle", integer=True)
    th = sp.diag(sp.exp(sp.I * k * angle), 1)
    cth = sp.exp(sp.I * m * angle) * th
    assert sp.simplify(cth.det() / th.det() - sp.exp(2 * sp.I * m * angle)) == 0


def test_sl2_lift_ends_with_winding_parity_sign():
    for n in (-3, -2, -1, 0, 1, 2, 3, 4):
        lift_at_end = sp.diag(sp.exp(sp.I * n * sp.pi), sp.exp(-sp.I * n * sp.pi))
        assert lift_at_end == sp.Integer(-1) ** n * I2


def test_n0_n1_blind_to_odd_diagonal_winding_but_n2_responds():
    theta = sp.diag(sp.I, 1)
    for n in (N0, N1):
        assert rho(theta, n) == rho(I2, n)
    assert sp.simplify(sp.trace(SY * (rho(theta, N2) - rho(I2, N2)))) == sp.Rational(2, 5)


def test_exact_second_clock_bloch_y_formula():
    x, y = sp.symbols("x y", real=True)
    theta = sp.diag(x + sp.I * y, 1)
    by = sp.simplify(sp.trace(SY * rho(theta, N2)))
    assert sp.simplify(by - 2 * y / (x * x + y * y + 2 * x + 4)) == 0


def test_six_outcome_strictly_positive_informationally_complete_povm():
    kappa = sp.Rational(1, 2)
    effects = [
        (I2 + sign * kappa * sigma) / 6
        for sigma in (SX, SY, SZ) for sign in (-1, 1)
    ]
    assert sp.simplify(sum(effects, sp.zeros(2)) - I2) == sp.zeros(2)
    for effect in effects:
        assert set(effect.eigenvals()) == {sp.Rational(1, 12), sp.Rational(1, 4)}
    a, b, c = sp.symbols("a b c", real=True)
    density = (I2 + a * SX + b * SY + c * SZ) / 2
    fisher = sp.zeros(3)
    for effect in effects:
        p = sp.simplify(sp.trace(effect * density))
        v = sp.Matrix([sp.diff(p, x) for x in (a, b, c)])
        fisher += v * v.T / p.subs({a: 0, b: 0, c: 0})
    assert sp.simplify(fisher - kappa * kappa * sp.eye(3) / 3) == sp.zeros(3)


def test_exact_local_fisher_of_phase_winding_goes_to_zero():
    r, phase, kappa, n, R = sp.symbols(
        "r phase kappa n R", real=True, positive=True
    )
    by = 2 * r * sp.sin(phase) / (4 + r * r + 2 * r * sp.cos(phase))
    p = (1 + kappa * by) / 2
    fisher = sp.simplify((sp.diff(p, phase) * n / R) ** 2 / (p * (1 - p)))
    at_zero = sp.simplify(fisher.subs(phase, 0))
    expected = (n / R) ** 2 * kappa ** 2 * (2 * r / (4 + 2 * r + r ** 2)) ** 2
    assert sp.simplify(at_zero - expected) == 0
    assert sp.limit(at_zero, r, 0, dir="+") == 0


def test_uniform_fisher_bound_for_phase_on_fixed_three_clock_protocol():
    r, kappa, n, R = sp.symbols("r kappa n R", positive=True)
    upper = sp.Rational(8, 9) * kappa ** 2 * n ** 2 * r ** 2 / R ** 2
    assert sp.limit(upper, r, 0, dir="+") == 0
    # For 0<r<=1/2: denominator >=3, |b_y|<=2r/3,
    # |db_y/dphase| <= 2r/3+4r^2/9 <=8r/9.
    left = (2 * r / 3 + 4 * r ** 2 / 9).subs(r, sp.Rational(1, 2))
    right = (8 * r / 9).subs(r, sp.Rational(1, 2))
    assert sp.simplify(left - right) == 0


def test_finite_sampling_does_not_certify_loop_parity():
    # phi(0)=0, phi(pi)=2pi, phi(2pi)=2pi yet winding=1.
    for angle in (sp.Rational(0), sp.pi, 2 * sp.pi):
        phi = angle + sp.pi * (1 - sp.cos(angle)) / 2
        assert sp.simplify(sp.exp(sp.I * phi)) == 1


def test_rank_one_limit_has_density_but_winding_number_disappears():
    theta = sp.diag(0, 1)
    assert theta.det() == 0
    for n in (N0, N1, N2):
        state = rho(theta, n)
        assert sp.simplify(sp.trace(state) - 1) == 0
        assert sp.simplify(state.det()) == 0


def test_joint_informational_fisher_vanishes_quadratically_near_rank_drop():
    import numpy as np

    effects = [
        np.array((I2 + sign * sp.Rational(1, 2) * sigma) / 6, dtype=complex)
        for sigma in (SX, SY, SZ) for sign in (-1, 1)
    ]
    clocks = [
        np.array(clock_inverse_sqrt(n), dtype=complex) for n in (N0, N1, N2)
    ]

    def fisher(r, phi):
        th = np.diag([r * np.exp(1j * phi), 1])
        dth = np.diag([1j * r * np.exp(1j * phi), 0])
        total = 0.
        for b in clocks:
            t = b @ th @ b
            dt = b @ dth @ b
            q = t @ t.conj().T
            dq = dt @ t.conj().T + t @ dt.conj().T
            trace_q = np.trace(q).real
            state = q / trace_q
            dstate = dq / trace_q - state * np.trace(dq).real / trace_q
            for effect in effects:
                p = np.trace(state @ effect).real
                dp = np.trace(dstate @ effect).real
                assert p >= 1 / 12 - 1e-12
                total += dp ** 2 / p
        return total

    for phi in (0., 0.3, 1.2, 2.9):
        assert fisher(0., phi) < 1e-28
        assert 0 <= fisher(1e-4, phi) < 2000 * 1e-8
        assert 0 <= fisher(5e-5, phi) < 2000 * 2.5e-9
