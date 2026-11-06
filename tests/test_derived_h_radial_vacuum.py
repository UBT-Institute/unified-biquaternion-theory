"""Exact checks for the positive-H timelike radial-action comparator."""

import sympy as sp


ETA = sp.diag(-1, 1, 1, 1)
T = sp.Symbol("t", positive=True)


def test_radial_coordinate_uses_both_dagger_sectors_and_is_lorentz_invariant():
    h0, h1, h2, h3, x0, x1, x2, x3 = sp.symbols("h0:4 x0:4", real=True)
    boost = sp.diag(2, sp.Rational(1, 2))
    h = sp.Matrix([[h0 + h3, h1 - sp.I * h2], [h1 + sp.I * h2, h0 - h3]])
    x = sp.I * sp.Matrix([[x0 - x3, -x1 + sp.I * x2], [-x1 - sp.I * x2, x0 + x3]])
    theta = h + x
    assert (theta + theta.H) / 2 == h
    assert (theta - theta.H) / 2 == x
    assert sp.expand(x.det()) == -x0**2 + x1**2 + x2**2 + x3**2
    assert (boost * h * boost.H).det() == h.det()
    assert (boost * x * boost.H).det() == x.det()


def test_logarithmic_radial_reconstruction_fixes_invariant_carrier_norm():
    f, s, r_star, lapse = sp.symbols("f s r_star lapse", positive=True)
    phi = sp.Function("phi")(T)
    r = -r_star * sp.exp(2 * phi / f)
    k = -(r.diff(T) / lapse)**2
    z = (phi.diff(T) / lapse)**2 / 2
    h_squared = 4 * s**2 * r / k
    q = h_squared * r
    assert sp.simplify(2 * z * (-q) - s**2 * f**2) == 0


def test_null_metric_variation_gives_exact_focusing_source():
    epsilon, z0, pressure, slope = sp.symbols("epsilon z0 pressure slope", real=True)
    speed = sp.Symbol("speed", positive=True)
    ell = sp.Matrix([1, 1, 0, 0])
    inverse_metric = ETA + epsilon * ell * ell.T
    dphi = sp.Matrix([speed, 0, 0, 0])
    z = -(dphi.T * inverse_metric * dphi)[0] / 2
    assert inverse_metric.det() == -1
    # The volume is one for the whole null variation, including the pressure term.
    density = pressure + slope * (z - z0)
    assert -2 * density.diff(epsilon) == speed**2 * slope
    assert (-2 * density.diff(epsilon)).subs(speed, sp.sqrt(2 * z0)) == 2 * z0 * slope


def test_principal_hessian_and_spatial_degeneracy():
    z0 = sp.Symbol("z0", positive=True)
    slope, curvature = sp.symbols("slope curvature", real=True)
    d0, d1, d2, d3 = sp.symbols("d0:4", real=True)
    perturbation = sp.Matrix([d0, d1, d2, d3])
    dphi = sp.Matrix([sp.sqrt(2 * z0), 0, 0, 0]) + perturbation
    delta_z = -(dphi.T * ETA * dphi)[0] / 2 - z0
    density = slope * delta_z + curvature * delta_z**2 / 2
    hessian = sp.hessian(density, list(perturbation)).subs(dict.fromkeys(perturbation, 0))
    inertia = slope + 2 * z0 * curvature
    assert hessian == sp.diag(inertia, -slope, -slope, -slope)
    assert hessian.det().expand() == (-inertia * slope**3).expand()
    assert hessian.subs(slope, 0).rank() == 1  # generic nonzero curvature
    assert hessian.subs({slope: 0, curvature: 0}).rank() == 0


def assert_regular_tetrad_lift(a, phi, s, f, r_star):
    """Construct the original carrier and boost connection on a homogeneous patch."""
    z = phi.diff(T)**2 / 2
    y0 = sp.sqrt(r_star) * sp.exp(phi / f)
    x0 = s * f / phi.diff(T)
    h = x0 / y0
    x = sp.Matrix([x0, 0, 0, 0])
    r = -y0**2
    assert sp.simplify(2 * z * x0**2 - s**2 * f**2) == 0
    assert sp.simplify(h**2 * (-r.diff(T)**2) - 4 * s**2 * r) == 0

    e = sp.diag(1, a, a, a)
    for mu in range(4):
        connection = sp.zeros(4)
        derivative = sp.zeros(4, 1)
        if mu == 0:
            derivative = x.diff(T) - h.diff(T) * x / h
        else:
            connection[mu, 0] = connection[0, mu] = s * a / x0
        assert connection.T * ETA + ETA * connection == sp.zeros(4)
        assert (derivative + connection * x - s * e[:, mu]).applyfunc(sp.simplify) == sp.zeros(4, 1)
    assert sp.simplify((h**2 + x0**2) / x0**2 - (1 + 1 / y0**2)) == 0


def test_rolling_flat_vacuum_saturates_the_obstruction():
    f, s, r_star, z0, coefficient = sp.symbols("f s r_star z0 coefficient", positive=True)
    z = sp.Symbol("z", real=True)
    pressure = coefficient * (z - z0)**2 / 2
    energy = 2 * z * pressure.diff(z) - pressure
    assert pressure.subs(z, z0) == energy.subs(z, z0) == 0
    assert pressure.diff(z).subs(z, z0) == 0
    assert (pressure.diff(z) + 2 * z * pressure.diff(z, 2)).subs(z, z0) == 2 * z0 * coefficient
    assert_regular_tetrad_lift(sp.S.One, sp.sqrt(2 * z0) * T, s, f, r_star)


def test_canonical_scalar_flrw_solution_lifts_to_the_full_matrix_field():
    mass, s, f, r_star, a0, t0 = sp.symbols("M s f r_star a0 t0", positive=True)
    a = a0 * (T / t0)**sp.Rational(1, 3)
    phi = sp.sqrt(sp.Rational(2, 3)) * mass * sp.log(T / t0)
    z = phi.diff(T)**2 / 2
    hubble = a.diff(T) / a
    assert sp.simplify(3 * mass**2 * hubble**2 - z) == 0
    assert sp.simplify(-mass**2 * (2 * hubble.diff(T) + 3 * hubble**2) - z) == 0
    assert sp.simplify((a**3 * phi.diff(T)).diff(T)) == 0
    assert sp.simplify(2 * z / mass**2) == 2 / (3 * T**2)
    assert_regular_tetrad_lift(a, phi, s, f, r_star)


def test_canonical_scalar_adm_legendre_transform():
    volume = sp.Symbol("volume", positive=True)
    velocity, spatial_norm = sp.symbols("velocity spatial_norm", real=True)
    momentum = sp.Symbol("momentum", real=True)
    density = volume * (velocity**2 - spatial_norm) / 2
    conjugate = density.diff(velocity)
    (solved_velocity,) = sp.solve(conjugate - momentum, velocity)
    hamiltonian = (momentum * velocity - density).subs(velocity, solved_velocity)
    assert sp.simplify(hamiltonian - momentum**2 / (2 * volume) - volume * spatial_norm / 2) == 0
