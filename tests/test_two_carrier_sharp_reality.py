"""Exact checks for the two-carrier comparison with a real sharp metric."""

import pytest
import sympy as sp


ETA = sp.diag(-1, 1, 1, 1)
V0 = sp.Matrix([1, 0, 0, 0])
W0 = sp.Matrix([sp.Rational(1, 2), 1, 0, 0])
GENERATOR = sp.Matrix([
    [0, 0, 1, 0],
    [0, 0, 0, -1],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
])
SYMMETRIC_INDICES = [(row, col) for row in range(4) for col in range(row, 4)]


def _flatten_symmetric(matrix):
    return sp.Matrix([matrix[row, col] for row, col in SYMMETRIC_INDICES])


def _connection_response(epsilon):
    """Differentiate the complex bilinear Gram tensor before imposing reality."""
    tetrad = sp.eye(4) + sp.I * epsilon * GENERATOR
    theta = V0 + sp.I * W0
    columns = []
    for mu in range(4):
        for first in range(4):
            for second in range(first + 1, 4):
                generator = sp.zeros(4)
                generator[first, second] = 1
                generator[second, first] = -1
                delta_tetrad = sp.zeros(4)
                delta_tetrad[:, mu] = ETA * generator * theta
                delta_metric = delta_tetrad.T * ETA * tetrad + tetrad.T * ETA * delta_tetrad
                columns.append(_flatten_symmetric(delta_metric))
    real, imaginary = sp.Matrix.hstack(*columns).as_real_imag()
    return tetrad, real, imaginary


def test_affine_family_real_metric_rank_condition_and_eikonal():
    x = sp.Matrix(sp.symbols("x0:4", real=True))
    kappa = sp.Symbol("kappa", positive=True)
    epsilon = sp.Symbol("epsilon", real=True)
    lam = epsilon * GENERATOR
    assert lam.T * ETA + ETA * lam == sp.zeros(4)
    v = V0 + kappa * x
    w = W0 + kappa * lam * x
    theta = v + sp.I * w
    tetrad = theta.jacobian(x) / kappa
    metric = (tetrad.T * ETA * tetrad).applyfunc(sp.simplify)
    assert metric == sp.diag(-1 - epsilon**2, 1 - epsilon**2, 1 + epsilon**2, 1 - epsilon**2)
    assert sp.Matrix.hstack(V0, W0, lam * V0, lam * W0).det() == epsilon**2

    square = (theta.T * ETA * theta)[0]
    gradient = sp.Matrix([sp.diff(square, coordinate) for coordinate in x])
    eikonal = (gradient.T * metric.inv() * gradient)[0]
    assert sp.cancel(eikonal - 4 * kappa**2 * square) == 0


def test_parallel_affine_transport_commutes_on_invariant_scalars():
    x = sp.Matrix(sp.symbols("x0:4", real=True))
    kappa = sp.Symbol("kappa", positive=True)
    v = V0 + kappa * x
    c = (x[0] - x[1] / 2)**2 * x[2] + x[3]**2
    gradient = sp.Matrix([sp.diff(c, coordinate) for coordinate in x])
    amplitude = sp.expand(v.dot(gradient) / kappa - c)
    assert amplitude != 0
    assert sp.expand(W0.dot(gradient)) == 0
    assert sp.expand(W0.dot(sp.Matrix([sp.diff(amplitude, coordinate) for coordinate in x]))) == 0


def test_parallel_affine_curvature_obeys_exact_transport():
    x = sp.Matrix(sp.symbols("x0:4", real=True))
    v = V0 + x
    w = W0
    invariant = v[0] - v[1] / 2
    alpha = sp.Matrix([-v[1], v[0], 0, 0])
    beta = sp.Matrix([0, 0, 1, 0])
    gamma = sp.Matrix([-v[3], v[3] / 2, 0, invariant])
    h = alpha * alpha.T * (invariant + x[2]) + x[1] * (beta * gamma.T + gamma * beta.T)
    assert sp.expand((v.T * h * v)[0]) == 0
    assert sp.expand((v.T * h * w)[0]) == 0
    amplitude = sp.expand((w.T * h * w)[0])

    def derivative(field, direction):
        return sum(direction[j] * sp.diff(field, x[j]) for j in range(4))

    def second_partial(first, second):
        return sum(
            (first[i] * second[j] * h.diff(x[i], x[j]) for i in range(4) for j in range(4)),
            sp.zeros(4),
        )

    mixed = (v.T * second_partial(v, w) * w)[0]
    along_v = (w.T * second_partial(v, v) * w)[0]
    along_w = (v.T * second_partial(w, w) * v)[0]
    twice_tidal = sp.expand(2 * mixed - along_v - along_w)
    first_derivative = derivative(amplitude, v)
    assert twice_tidal != 0
    assert sp.expand(twice_tidal + derivative(first_derivative, v) + first_derivative) == 0
    assert sp.expand(derivative(twice_tidal, w)) == 0


def test_parallel_fixed_carrier_rank_and_transverse_lock():
    _, real, imaginary = _connection_response(0)
    image = real * sp.Matrix.hstack(*imaginary.nullspace())
    assert imaginary.rank() == 9
    assert image.rank() == 7
    for entry in [(0, 0), (0, 1), (1, 1)]:
        assert image.row(SYMMETRIC_INDICES.index(entry)) == sp.zeros(1, image.cols)


@pytest.mark.parametrize("epsilon", [sp.Rational(1, 3), sp.Rational(-2, 5)])
def test_complex_fixed_carrier_rank_and_two_eikonal_constraints(epsilon):
    tetrad, real, imaginary = _connection_response(epsilon)
    image = real * sp.Matrix.hstack(*imaginary.nullspace())
    assert imaginary.rank() == 10
    assert image.rank() == 8
    assert sp.Matrix.vstack(real, imaginary).rank() == 18

    t = tetrad.inv() * (V0 + sp.I * W0)
    t_real, t_imaginary = t.as_real_imag()
    assert sp.Matrix.hstack(t_real, t_imaginary).rank() == 2
    metric = tetrad.T * ETA * tetrad
    assert (t_real.T * metric * t_real)[0] < 0
    contractions = sp.Matrix([
        (1 if row == col else 2) * t[row] * t[col] for row, col in SYMMETRIC_INDICES
    ])
    assert (contractions.T * image).applyfunc(sp.simplify) == sp.zeros(1, image.cols)


def _ricci_symbol(h, metric_inverse, p):
    raised_p = metric_inverse * p
    h_p = h * raised_p
    return (
        p.dot(raised_p) * h
        + sp.trace(metric_inverse * h) * p * p.T
        - p * h_p.T
        - h_p * p.T
    ) / 2


@pytest.mark.parametrize("plus,cross", [(1, 0), (0, 1)])
def test_transverse_einstein_amplitudes_have_exact_connection_lifts(plus, cross):
    epsilon = sp.Rational(1, 3)
    tetrad, real, imaginary = _connection_response(epsilon)
    metric_inverse = (tetrad.T * ETA * tetrad).inv()
    t = tetrad.inv() * (V0 + sp.I * W0)
    p = sp.Matrix([1, 0, 1, 0])
    assert p.dot(metric_inverse * p) == 0

    h_tt = sp.zeros(4)
    h_tt[1, 1] = (1 - epsilon**2) * plus
    h_tt[3, 3] = -h_tt[1, 1]
    h_tt[1, 3] = h_tt[3, 1] = (1 - epsilon**2) * cross
    target = sp.simplify(-(t.T * h_tt * t)[0] / (2 * p.dot(t)))
    t_real, t_imaginary = t.as_real_imag()
    xi, free = sp.Matrix.vstack(t_real.T, t_imaginary.T).gauss_jordan_solve(
        sp.Matrix(target.as_real_imag())
    )
    xi = xi.subs(dict.fromkeys(free, 0))
    h = h_tt + p * xi.T + xi * p.T

    response = sp.Matrix.vstack(real, imaginary)
    delta_connection, free = response.gauss_jordan_solve(
        sp.Matrix.vstack(_flatten_symmetric(h), sp.zeros(10, 1))
    )
    delta_connection = delta_connection.subs(dict.fromkeys(free, 0))
    assert imaginary * delta_connection == sp.zeros(10, 1)
    assert real * delta_connection == _flatten_symmetric(h)
    assert _ricci_symbol(h, metric_inverse, p) == sp.zeros(4)
    # p_1=p_3=0, so these Riemann amplitudes are exactly p_0^2 h_ij/2.
    assert h[1, 1] / 2 == (1 - epsilon**2) * plus / 2
    assert h[1, 3] / 2 == (1 - epsilon**2) * cross / 2


def test_transverse_plus_lift_is_singular_at_fixed_carriers_in_parallel_limit():
    epsilon = sp.Symbol("epsilon", real=True)
    tetrad = sp.eye(4) + sp.I * epsilon * GENERATOR
    a, b, c, d, e, f = sp.symbols("a b c d e f", real=True)
    generator = ETA * sp.Matrix([
        [0, a, b, c],
        [-a, 0, d, e],
        [-b, -d, 0, f],
        [-c, -e, -f, 0],
    ])
    p = generator * V0
    q = generator * W0
    response = 2 * (tetrad[:, 1].T * ETA * (p + sp.I * q))[0]
    real, imaginary = response.as_real_imag()
    assert sp.expand(real - 2 * imaginary + 4 * epsilon * p[3] + 2 * epsilon * q[3]) == 0
