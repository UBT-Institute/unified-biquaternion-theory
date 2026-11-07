"""Exact controls for the two-carrier commutator-square comparison."""

from itertools import product

import sympy as sp


def test_reference_torsion_norm_includes_screen_bracket():
    b22, b23, b33, c22, c23, c33, x2, x3 = sp.symbols(
        "b22 b23 b33 c22 c23 c33 x2 x3"
    )
    b = sp.Matrix([[b22, b23], [b23, b33]])
    c = sp.Matrix([[c22, c23], [c23, c33]])
    x = sp.Matrix([x2, x3])
    t = sp.MutableDenseNDimArray.zeros(4, 4, 4)
    for a in range(2):
        for j in range(2):
            t[a + 2, 0, j + 2] = b[a, j]
            t[a + 2, 1, j + 2] = c[a, j]
        t[a + 2, 0, 1] = 2 * x[a]
    for a, j, k in product(range(4), repeat=3):
        if j < k:
            t[a, k, j] = -t[a, j, k]
    sign = (-1, 1, 1, 1)
    contraction = sum(
        sign[a] * sign[j] * sign[k] * t[a, j, k] ** 2
        for a, j, k in product(range(4), repeat=3)
    )
    assert sp.expand(contraction - 2 * (sp.trace(c**2 - b**2) - 4 * x.dot(x))) == 0


def test_legendre_transform_at_general_screen_metric():
    g22, g23, g33, kappa, m, h, nu, rho = sp.symbols("g22 g23 g33 kappa m h nu rho")
    d22, d23, d33, l22, l23, l33 = sp.symbols("d22 d23 d33 l22 l23 l33")
    dz2, dz3, shift2, shift3 = sp.symbols("dz2 dz3 shift2 shift3")
    gamma = sp.Matrix([[g22, g23], [g23, g33]])
    inverse = gamma.inv()
    dot_gamma = sp.Matrix([[d22, d23], [d23, d33]])
    lie_gamma = sp.Matrix([[l22, l23], [l23, l33]])
    dot_z, shift_z = sp.Matrix([dz2, dz3]), sp.Matrix([shift2, shift3])
    b = kappa / 2 * (dot_gamma - lie_gamma) - h * gamma
    f = dot_z - shift_z
    b_norm = sp.trace(inverse * b * inverse * b)
    f_norm = f.dot(gamma * f)
    kinetic = 2 * nu * rho * (b_norm + kappa**2 * m**2 * f_norm)
    p = 2 * nu * rho * kappa * inverse * b * inverse
    pi = 4 * nu * rho * kappa**2 * m**2 * gamma * f
    momenta = (p[0, 0], 2 * p[0, 1], p[1, 1], pi[0], pi[1])
    velocities = (d22, d23, d33, dz2, dz3)
    assert all(
        sp.cancel(kinetic.diff(velocity) - momentum) == 0
        for velocity, momentum in zip(velocities, momenta)
    )
    legendre = sp.trace(p * dot_gamma) + pi.dot(dot_z) - kinetic
    expected = (
        sp.trace(p * gamma * p * gamma) / (2 * nu * rho * kappa**2)
        + pi.dot(inverse * pi) / (8 * nu * rho * kappa**2 * m**2)
        + 2 * h / kappa * sp.trace(p * gamma)
        + sp.trace(p * lie_gamma)
        + pi.dot(shift_z)
    )
    assert sp.cancel(legendre - expected) == 0


def test_affine_screen_diffeomorphism_generator_closes():
    z, y2, y3 = sp.symbols("z y2 y3")
    xi = sp.Matrix([z * y2 + y3**2, y2 * y3 + z**2])
    eta = sp.Matrix([z * y3 + y2**2, y2 - z * y3])
    beta = sp.Matrix([y2 * z + y3, y2**2 - y3 * z])

    def bracket(left, right):
        return right.jacobian((y2, y3)) * left - left.jacobian((y2, y3)) * right

    def action(parameter):
        return parameter.diff(z) + bracket(parameter, beta)

    difference = bracket(xi, action(eta)) - bracket(eta, action(xi)) - action(bracket(xi, eta))
    assert difference.applyfunc(sp.expand) == sp.zeros(2, 1)


def test_principal_gauge_rank_and_three_frequencies():
    k, q2, q3, w = sp.symbols("k q2 q3 w")
    screen = sp.Matrix([[2 * q2, 0], [q3, q2], [0, 2 * q3]])
    gradient = (k * sp.eye(3)).row_join(-screen)
    gauge = screen.col_join(k * sp.eye(2))
    assert gradient * gauge == sp.zeros(3, 2)
    assert gauge[3:5, :].det() == k**2
    assert gauge[:2, :].det() == 2 * q2**2
    assert gauge[1:3, :].det() == 2 * q3**2

    kinetic = sp.diag(1, 2, 1, 4, 4)
    frobenius = sp.diag(1, 2, 1)
    frequency_squared = gradient * kinetic.inv() * gradient.T * frobenius
    q_squared = q2**2 + q3**2
    expected = (w - k**2 - q_squared) * (w - k**2 - q_squared / 2) * (w - k**2)
    assert sp.expand(frequency_squared.charpoly(w).as_expr() - expected) == 0
    assert gradient.subs({k: 0, q2: 1, q3: 0}).rank() == 2
