"""Exact symbol and constraint controls for the trace-tuned torsion family."""

import sympy as sp


def test_trace_and_cone_conditions_reduce_to_a_square():
    k, long, lam, odd = sp.symbols("k long lam odd", real=True, nonzero=True)
    screen = k / 2 - lam**2 / (4 * long)
    bracket = long + 2 * k + (lam + 2 * odd) ** 2 / (4 * screen)
    assert sp.factor(4 * k * long * screen * (bracket - 2 * k - 2 * odd**2 / k)) == (
        2 * (k * long + lam * odd) ** 2
    )

    c1, c2, c3, beta, odd = map(sp.Rational, ("-1/8", "-3/4", "1/4", "-3/2", "1"))
    k = 2 * c1 + c2
    long, screen = 4 * c1 - 2 * c2, k + c3
    lam, mu = 2 * beta / 3 + 2 * odd, 2 * beta / 3 + 4 * odd
    trace = c3 + lam**2 / (4 * long)
    bracket = 8 * c1 + mu**2 / (4 * screen)
    assert (k, long, screen, trace, bracket) == (-1, 1, -sp.Rational(3, 4), sp.Rational(1, 2), -4)


def test_shear_gauge_and_shift_schur_complement():
    shear, electric, odd, k, q, w = sp.symbols("shear electric odd k q w", real=True)
    j = sp.Matrix([[0, 1], [-1, 0]])
    screen_squared = 2 * q**2

    # In Frobenius-normalized coordinates the trace-free gauge map is
    # sqrt(2) q times the identity for a transverse covector along e_2.
    n2, n3, z2, z3 = sp.symbols("n2 n3 z2 z3", real=True)
    z = sp.Matrix([z2, z3])
    n_tensor = q * sp.Matrix([[n2, n3], [n3, -n2]])
    z_tensor = q * sp.Matrix([[z2, z3], [z3, -z2]])
    assert sp.expand(sp.trace(n_tensor**2)) == 2 * q**2 * n2**2 + 2 * q**2 * n3**2
    parity = sp.trace(j.T * n_tensor * z_tensor)
    assert sp.expand(parity - 2 * q**2 * (n2 * z3 - n3 * z2)) == 0

    denominator = shear * screen_squared + electric * k**2
    mixed = -electric * w * k * sp.eye(2) - odd * screen_squared * j
    schur = (electric * w**2 - shear * screen_squared) * sp.eye(2) - mixed.T * mixed / denominator
    expected = (
        screen_squared
        * (shear * electric * (w**2 - k**2) - (shear**2 + odd**2) * screen_squared)
        / denominator
    )
    assert (schur - expected * sp.eye(2)).applyfunc(sp.cancel) == sp.zeros(2)

    n = -mixed * z / denominator
    f = w * z - k * n
    expected_norm = (
        screen_squared**2 * (shear**2 * w**2 + odd**2 * k**2) * z.dot(z) / denominator**2
    )
    assert sp.cancel(f.dot(f) - expected_norm) == 0


def test_transverse_cone_example_violates_the_exact_trace_equation():
    z = sp.Matrix(sp.symbols("z2 z3", real=True))
    j = sp.Matrix([[0, 1], [-1, 0]])
    n = j * z
    shear_density = 2 * (n.dot(n) - z.dot(z)) - 4 * n.dot(j * z)
    bracket_density = 4 * z.dot(z)
    scale = sp.symbols("scale", positive=True)
    density = scale * shear_density + scale**2 * bracket_density
    assert sp.expand(density.subs(scale, 1)) == 0
    assert sp.expand(density.diff(scale).subs(scale, 1) - 4 * z.dot(z)) == 0


def test_transverse_null_metric_ricci_conditions():
    q, w, trace, n2, n3, z2, z3 = sp.symbols("q w trace n2 n3 z2 z3")
    metric = sp.diag(-1, 1, 1, 1)
    covector = sp.Matrix([w, 0, q, 0])
    raised = metric * covector
    h = sp.Matrix([
        [0, 0, n2, n3],
        [0, 0, z2, z3],
        [n2, z2, trace / 2, 0],
        [n3, z3, 0, trace / 2],
    ])
    gauge_vector = h * raised - sp.trace(metric * h) * covector / 2
    null_ricci = (covector * gauge_vector.T + gauge_vector * covector.T) / 2
    assert sp.expand(null_ricci[0, 1]) == w * q * z2 / 2
    assert sp.expand(null_ricci[2, 2]) == -w * q * n2
    tidal_nn = covector[0] ** 2 * h[1, 1] - 2 * covector[0] * covector[1] * h[0, 1]
    assert tidal_nn + covector[1] ** 2 * h[0, 0] == 0
