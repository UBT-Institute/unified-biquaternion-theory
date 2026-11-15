"""Exact conditional tests for Theta Dirac current, projected right U1 and real-tetrad intertwiner.

No test proves that UBT has a single fundamental quantum+gravity action, graded
fermions, Gauss-law constraints, Maxwell equations or physical photons.
"""
import sympy as sp

I = sp.I
P = [
    sp.eye(2),
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.diag(1, -1),
]
eps = I * P[2]
U = sp.Matrix([
    [sp.Symbol("u0", complex=True), sp.Symbol("v0", complex=True)],
    [sp.Symbol("u1", complex=True), sp.Symbol("v1", complex=True)],
])


def zero(m):
    return m.applyfunc(sp.simplify) == sp.zeros(*m.shape)


def sharp(a):
    return sp.trace(a) * P[0] - a


def test_flat_dirac_local_charge_conservation_including_mass():
    mass = sp.symbols("m", real=True)
    derivatives = [
        sp.Matrix(2, 2, lambda row, col: sp.Symbol(
            "d%d_%d_%d" % (j, row, col), complex=True))
        for j in range(3)
    ]
    source = eps * U.conjugate() * P[1]
    assert sp.simplify(sp.trace(U.H * source)) == 0
    time_derivative = sum(
        (P[i + 1] * derivatives[i] for i in range(3)), sp.zeros(2)
    ) - I * mass * source
    continuity = sp.trace(time_derivative.H * U + U.H * time_derivative)
    continuity -= sum(
        sp.trace(derivatives[i].H * P[i + 1] * U +
                 U.H * P[i + 1] * derivatives[i])
        for i in range(3)
    )
    assert sp.simplify(sp.expand_complex(continuity)) == 0


def test_causal_current_exact_determinant_norm():
    k = U * U.H
    density = sp.trace(k)
    fluxes = [-sp.trace(k * P[i]) for i in range(1, 4)]
    assert sp.simplify(
        density**2 - sum(f**2 for f in fluxes)
        - 4 * U.det() * sp.conjugate(U.det())
    ) == 0


def test_right_vector_phase_preserves_current_and_dirac_mass():
    alpha = sp.symbols("alpha", real=True)
    r = sp.diag(sp.exp(I * alpha), sp.exp(-I * alpha))
    assert zero((U * r) * (U * r).H - U * U.H)
    assert sp.simplify((U * r).det() - U.det()) == 0
    assert zero(eps * (U * r).conjugate() * P[1]
                - (eps * U.conjugate() * P[1]) * r)


def test_independent_right_u1_fails_real_tetrad_but_corotation_preserves_it():
    alpha = sp.symbols("alpha", real=True)
    r = sp.diag(sp.exp(I * alpha), sp.exp(-I * alpha))
    l = r.H
    assert (I * r + (I * r).H).subs(alpha, sp.pi / 2) != sp.zeros(2)
    for e in [I * m for m in P]:
        transformed = l * e * r
        assert zero(transformed + transformed.H)
    # Real-slice failure is independent from sharp metric preservation.
    for e in [I * m for m in P]:
        for f in [I * m for m in P]:
            original = (sharp(e)*f + sharp(f)*e)/2
            transformed = (sharp(e*r)*(f*r) + sharp(f*r)*(e*r))/2
            assert zero(transformed - original)


def test_theta_projected_right_charge_connection_nonflat_and_gauge_covariant():
    x, y, charge = sp.symbols("x y charge", real=True)
    u1 = sp.cos(x)*P[0] + I*sp.sin(x)*P[1]
    u2 = sp.cos(y)*P[0] + I*sp.sin(y)*P[2]
    theta = u1*u2

    def projected_connection(m, variable):
        return sp.trigsimp(sp.simplify(
            sp.im(sp.trace(P[3] * m.inv() * m.diff(variable))) / 2
        ))

    a_x, a_y = projected_connection(theta, x), projected_connection(theta, y)
    assert sp.trigsimp(a_x + sp.sin(2*y)) == 0
    assert a_y == 0
    assert sp.trigsimp(sp.diff(a_y, x) - sp.diff(a_x, y)
                       - 2*sp.cos(2*y)) == 0
    rotation = sp.diag(sp.exp(I*charge*x), sp.exp(-I*charge*x))
    assert sp.trigsimp(sp.expand_complex(
        projected_connection(theta*rotation, x) - a_x - charge
    )) == 0
    assert sp.trigsimp(sp.expand_complex(
        projected_connection(theta*rotation, y) - a_y
    )) == 0
    assert zero(theta*theta.H - P[0])


def test_projected_curvature_has_no_linear_mode_about_constant_matrix_vacuum():
    x, y, amplitude = sp.symbols("x y amplitude", real=True)
    theta = (
        (sp.cos(amplitude*x)*P[0] + I*sp.sin(amplitude*x)*P[1])
        * (sp.cos(amplitude*y)*P[0] + I*sp.sin(amplitude*y)*P[2])
    )

    def a(variable):
        return sp.trigsimp(sp.simplify(
            sp.im(sp.trace(P[3]*theta.inv()*theta.diff(variable))) / 2
        ))

    f = sp.trigsimp(sp.diff(a(y), x) - sp.diff(a(x), y))
    assert sp.trigsimp(f - 2*amplitude**2*sp.cos(2*amplitude*y)) == 0
    assert sp.diff(f, amplitude).subs(amplitude, 0) == 0


def test_flat_canonical_soldering_and_scalar_gradient_comparator():
    t, x, y, z, c = sp.symbols("t x y z c", real=True, positive=True)
    h = (c+t)*P[0] + x*P[1] + y*P[2] + z*P[3]
    theta = I*h
    assert zero(theta*theta.H - h*h)
    legs = [theta.diff(v) for v in (t, x, y, z)]
    metric = sp.diag(-1, 1, 1, 1)
    for a in range(4):
        for b in range(4):
            assert zero((sharp(legs[a])*legs[b]+sharp(legs[b])*legs[a])/2
                        - metric[a, b]*P[0])
    wave_number = sp.symbols("wave_number", real=True)
    right = sp.diag(sp.exp(I*wave_number*x),
                    sp.exp(-I*wave_number*x))
    scalar_orbit = I*c*right
    trial_kinetic = sp.trace(scalar_orbit.diff(x).H*scalar_orbit.diff(x))
    assert sp.simplify(trial_kinetic - 2*c*c*wave_number**2) == 0
