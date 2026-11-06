"""Exact checks for the scoped SU(3) carrier corrections."""

import sympy as sp


def test_period_matrix_dictionary_has_only_five_real_symmetric_directions() -> None:
    a, b, c, d, e = entries = sp.symbols("a b c d e", real=True)
    symmetric = sp.Matrix([[a, b, c], [b, d, e], [c, e, -a - d]])
    assert symmetric.reshape(9, 1).jacobian(entries).rank() == 5

    n = sp.Matrix(sp.symbols("n_1:4", real=True))
    for row, col in ((0, 1), (0, 2), (1, 2)):
        generator = sp.zeros(3)
        generator[row, col] = -sp.I / 2
        generator[col, row] = sp.I / 2
        assert generator.H == generator
        assert generator.T == -generator
        assert sp.expand((n.T * generator * n)[0]) == 0


def test_trace_free_maurer_cartan_curvature_vanishes_for_noncommuting_frame() -> None:
    x, y = sp.symbols("x y", real=True)
    rotation = sp.Matrix([[sp.cos(x), -sp.sin(x), 0], [sp.sin(x), sp.cos(x), 0], [0, 0, 1]])
    phase = sp.diag(sp.exp(sp.I * y), sp.exp(-sp.I * y), 1)
    frame = sp.exp(sp.I * y) * rotation * phase

    def connection(coordinate):
        form = sp.simplify(frame.H * frame.diff(coordinate))
        return form - sp.trace(form) * sp.eye(3) / 3

    a_x, a_y = connection(x), connection(y)
    assert sp.simplify(a_x * a_y - a_y * a_x) != sp.zeros(3)
    curvature = a_y.diff(x) - a_x.diff(y) + a_x * a_y - a_y * a_x
    assert sp.simplify(curvature) == sp.zeros(3)


def test_left_right_covariance_requires_the_right_connection_sign() -> None:
    t = sp.symbols("t", real=True)
    theta = sp.Matrix([[1, t, 2], [t**2, 2, t]])
    left = sp.diag(sp.exp(sp.I * t), sp.exp(-sp.I * t))
    right = sp.diag(sp.exp(-2 * sp.I * t), sp.exp(2 * sp.I * t), 1)
    omega = sp.Matrix([[0, -1], [1, 0]])
    color = sp.Matrix([[0, 1, 0], [-1, 0, 0], [0, 0, 0]])

    transformed = left * theta * right
    omega_prime = left * omega * left.H - left.diff(t) * left.H
    color_prime = right.H * color * right + right.H * right.diff(t)
    target = left * (theta.diff(t) + omega * theta - theta * color) * right
    result = transformed.diff(t) + omega_prime * transformed - transformed * color_prime
    assert sp.simplify(result - target) == sp.zeros(2, 3)

    wrong_target = left * (theta.diff(t) + omega * theta + theta * color) * right
    wrong_result = transformed.diff(t) + omega_prime * transformed + transformed * color_prime
    assert sp.simplify(wrong_result - wrong_target) == sp.simplify(2 * left * theta * right.diff(t))


def test_fixed_flavor_one_loop_running_and_hypercharge_sum() -> None:
    alpha_0, beta_0, log_scale = sp.symbols("alpha_0 beta_0 log_scale")
    alpha = alpha_0 / (1 - 8 * sp.pi * beta_0 * alpha_0 * log_scale)
    assert alpha.subs(log_scale, 0) == alpha_0
    assert sp.simplify(alpha.diff(log_scale) - 8 * sp.pi * beta_0 * alpha**2) == 0
    assert 2 * sp.Rational(1, 6) - sp.Rational(2, 3) + sp.Rational(1, 3) == 0
