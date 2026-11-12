"""Exact regression witnesses for Theta spectral speeds versus ghost energy.

These are finite toy principal symbols, not an on-shell UBT action.
"""
import sympy as sp


def generalized_speed_squares(z, g):
    x = sp.symbols("x", real=True)
    return sp.factor((g - x * z).det())


def test_healthy_split_speeds():
    z = sp.eye(2)
    g = sp.diag(1, sp.Rational(1, 4))
    x = sp.symbols("x", real=True)
    assert generalized_speed_squares(z, g) == (x - 1) * (x - sp.Rational(1, 4))
    assert all(v > 0 for v in z.eigenvals())


def test_same_speed_does_not_exclude_ghost():
    z = sp.diag(1, -1)
    g = z
    x = sp.symbols("x", real=True)
    assert generalized_speed_squares(z, g) == -(x - 1) ** 2
    assert z[1, 1] < 0


def test_zero_spatial_speed_keeps_positive_time_kinetic():
    z = sp.eye(2)
    g = sp.diag(1, 0)
    x = sp.symbols("x", real=True)
    assert generalized_speed_squares(z, g) == x * (x - 1)
    assert z[1, 1] == 1


def test_zero_temporal_kinetic_not_zero_propagation_speed_limit():
    epsilon = sp.symbols("epsilon", positive=True)
    z = sp.diag(1, epsilon)
    g = sp.eye(2)
    x = sp.symbols("x", real=True)
    assert generalized_speed_squares(z, g) == (x - 1) * (epsilon * x - 1)
    assert sp.det(z.subs(epsilon, 0)) == 0


def test_original_full_theta_comparator_equal_speed_with_ghosts():
    z = sp.diag(2, -2, -2, -2, 2, -2, -2, -2)
    g = z
    x = sp.symbols("x", real=True)
    assert sp.factor(generalized_speed_squares(z, g)) == 256 * (1 - x) ** 8
    assert sum(z[i, i] < 0 for i in range(8)) == 6
    assert z.det() == 256


def test_gravity_mixing_cannot_repair_negative_theta_block():
    a = sp.Matrix([[2]])
    b = sp.Matrix([[3, 0]])
    c = sp.diag(-1, 1)
    schur = c - b.T * a.inv() * b
    assert schur == sp.diag(sp.Rational(-11, 2), 1)
    k = a.row_join(b).col_join(b.T.row_join(c))
    assert k.det() == a.det() * schur.det()
    assert len([v for v in schur.eigenvals() if v < 0]) == 1


def test_zero_gradient_branch_has_positive_k4_dispersion():
    epsilon, beta, k = sp.symbols("epsilon beta k", positive=True)
    omega2 = beta * k**4 / epsilon
    assert sp.simplify(omega2 / k**4 - beta / epsilon) == 0
    # group velocity d omega / dk tends to zero as k tends to zero
    omega = sp.sqrt(beta / epsilon) * k**2
    assert sp.limit(sp.diff(omega, k), k, 0, dir="+") == 0


def test_zero_time_kinetic_limit_is_singular_not_slow():
    epsilon, g, k = sp.symbols("epsilon g k", positive=True)
    omega2 = g * k**2 / epsilon
    assert sp.limit(omega2, epsilon, 0, dir="+") == sp.oo


def test_canonical_cubic_coupling_diverges_in_zero_kinetic_limit():
    epsilon, lam = sp.symbols("epsilon lam", positive=True)
    canonical_coupling = lam / epsilon**sp.Rational(3, 2)
    assert sp.limit(canonical_coupling, epsilon, 0, dir="+") == sp.oo
