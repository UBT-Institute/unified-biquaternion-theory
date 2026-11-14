"""Exact, restricted quantum-observer Theta-to-QED benchmark tests.

No fundamental Theta action, Maxwell dynamics, or physical photon is derived.
"""
import sympy as sp

I = sp.I
SIG = [
    sp.eye(2),
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.diag(1, -1),
]
t, x, y, z = sp.symbols("t x y z", real=True)
coords = (t, x, y, z)
THETA_FLAT = SIG[0] + I * sum(
    (c * m for c, m in zip(coords, SIG)), sp.zeros(2)
)


def imaginary_overlap_connection(theta):
    """Normalized Hilbert-Schmidt Berry one-form in an N=I frame."""
    norm_sq = sp.simplify(sp.trace(theta.H * theta))
    return [
        sp.simplify(sp.im(sp.trace(theta.H * theta.diff(q))) / norm_sq)
        for q in coords
    ]


def test_flat_theta_gravity_is_exactly_minkowski():
    E = [THETA_FLAT.diff(q) for q in coords]
    eta = sp.diag(-1, 1, 1, 1)
    assert all((em + em.H) == sp.zeros(2) for em in E)
    for a in range(4):
        for b in range(4):
            sharp_a = sp.trace(E[a]) * SIG[0] - E[a]
            sharp_b = sp.trace(E[b]) * SIG[0] - E[b]
            center = sp.simplify((sharp_a * E[b] + sharp_b * E[a]) / 2)
            assert center == eta[a, b] * SIG[0]


def test_bare_observer_phase_curvature_not_zero_on_flat_reference():
    a = imaginary_overlap_connection(THETA_FLAT)
    R2 = 1 + t*t + x*x + y*y + z*z
    assert [sp.simplify(c) for c in a] == [1/R2, 0, 0, 0]
    fxt = sp.factor(sp.diff(a[0], x) - sp.diff(a[1], t))
    assert sp.simplify(fxt + 2*x/R2**2) == 0
    assert fxt.subs({t: 0, x: 1, y: 0, z: 0}) == -sp.Rational(1, 2)


def test_reference_ratio_phase_has_no_linear_curvature():
    epsilon = sp.symbols("epsilon", real=True)
    phi = (x + I*y) * SIG[1]
    theta = (SIG[0] + epsilon*phi) * THETA_FLAT
    X = sp.simplify(theta * THETA_FLAT.inv())
    assert sp.simplify(X - (SIG[0] + epsilon*phi)) == sp.zeros(2)
    a = imaginary_overlap_connection(X)
    D = 1 + epsilon**2 * (x*x+y*y)
    assert sp.simplify(a[1] + epsilon**2*y/D) == 0
    assert sp.simplify(a[2] - epsilon**2*x/D) == 0
    fxy = sp.factor(sp.diff(a[2], x) - sp.diff(a[1], y))
    assert sp.simplify(fxy - 2*epsilon**2/D**2) == 0
    assert sp.simplify(sp.diff(fxy, epsilon).subs(epsilon, 0)) == 0
    assert sp.limit(fxy**2/epsilon**4, epsilon, 0) == 4


def test_naive_global_u1_rotation_is_not_canonical_tetrad_gauge():
    theta_prime = sp.exp(I * sp.pi/2) * THETA_FLAT
    leg_t = theta_prime.diff(t)
    assert leg_t == -SIG[0]
    assert leg_t + leg_t.H != sp.zeros(2)


def test_observer_induced_lorentz_unitary_has_no_central_generator():
    beta, chi = sp.symbols("beta chi", real=True)
    S = sp.diag(sp.exp(beta/2), sp.exp(-beta/2))
    N = sp.diag(2, sp.Rational(1, 2))
    N_prime = S * N * S.H
    N_prime_inv_sqrt = sp.diag(
        sp.exp(-beta/2)/sp.sqrt(2), sp.sqrt(2)*sp.exp(beta/2)
    )
    U = N_prime_inv_sqrt * S * sp.diag(sp.sqrt(2), 1/sp.sqrt(2))
    assert sp.simplify(U - sp.eye(2)) == sp.zeros(2)
    assert sp.simplify(U.det()-1) == 0
    R = sp.diag(sp.exp(I*chi), sp.exp(-I*chi))
    assert sp.simplify(sp.trace(R.H * R.diff(chi))) == 0


def test_full_projective_complex_theta_allows_non_simple_berry_curvature():
    """An invertible complex matrix can induce f wedge f != 0."""
    Z = sp.Matrix([[1, x + I*t], [y + I*z, 1]])
    assert Z.det().subs({q: 0 for q in coords}) == 1
    a = imaginary_overlap_connection(Z)
    F = sp.Matrix(
        4, 4,
        lambda mu, nu: sp.simplify(
            sp.diff(a[nu], coords[mu]) - sp.diff(a[mu], coords[nu])
        ),
    )
    F0 = sp.simplify(F.subs({q: 0 for q in coords}))
    assert F0[0, 1] == -1
    assert F0[2, 3] == 1
    assert all(F0[i, j] == 0 for i, j in ((0, 2), (0, 3), (1, 2), (1, 3)))
    pf = F0[0, 1]*F0[2, 3] - F0[0, 2]*F0[1, 3] + F0[0, 3]*F0[1, 2]
    assert pf == -1  # F wedge F = 2*pf dt wedge dx wedge dy wedge dz.


def test_full_projective_response_still_quadratic_around_identity():
    epsilon = sp.symbols("epsilon", real=True)
    Z = sp.eye(2) + epsilon * sp.Matrix([[0, x+I*t], [y+I*z, 0]])
    a = imaginary_overlap_connection(Z)
    Ftx = sp.simplify(sp.diff(a[1], t) - sp.diff(a[0], x))
    Fyz = sp.simplify(sp.diff(a[3], y) - sp.diff(a[2], z))
    assert Ftx.subs({q: 0 for q in coords}) == -epsilon**2
    assert Fyz.subs({q: 0 for q in coords}) == epsilon**2
    assert sp.diff(Ftx, epsilon).subs(epsilon, 0) == 0
