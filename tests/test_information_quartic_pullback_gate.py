"""Exact fixed-coframe representative-principal-symbol regression.

Conditional positive-H derived-center graded comparator only. Does not establish
physical UBT constraints, gauge-quotient dynamics, or ghost spectrum.
"""
import sympy as sp

I2 = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.diag(1, -1)


def full_theta(h, x):
    """H=hI+X for real X=i(x0 I - xj sigmaj)."""
    return (h + sp.I * x[0]) * I2 - sp.I * (
        x[1] * SX + x[2] * SY + x[3] * SZ
    )


def invariants(t):
    sharp = sp.trace(t) * I2 - t
    H = sp.simplify(sp.trace(sharp * t.H))
    d = sp.expand(t.det())
    J = sp.factor(sp.expand(d * sp.conjugate(d) - H * H / 4))
    return H, J


def pullback(r, u, v, s):
    """Fixed-Minkowski-coframe derived-H inverse; v is one spatial gradient."""
    k = v**2 - u**2
    h2 = 4 * s * s * r / k
    H = 2 * h2 * (1 - r)
    J = sp.factor((h2**3 / s**2) * v * v)
    return k, h2, H, J


def test_generic_full_theta_invariant_identity_positive_H_chart():
    h, t, x, y, z = sp.symbols("h t x y z", real=True)
    H, J = invariants(full_theta(h, (t, x, y, z)))
    assert sp.factor(H - 2 * (h*h + t*t - x*x - y*y - z*z)) == 0
    assert sp.factor(J - 4 * h*h * (x*x + y*y + z*z)) == 0


def test_reconstructed_label_invariants():
    r, u, v, s = sp.symbols("r u v s", real=True, nonzero=True)
    _, h2, H, J = pullback(r, u, v, s)
    assert sp.factor(H - 8*s*s*r*(1-r)/(v*v-u*u)) == 0
    assert sp.factor(J - 64*s**4*r**3*v*v/(v*v-u*u)**3) == 0


def test_reconstruction_on_real_affine_boost_lift():
    h, b, s = sp.symbols("h b s", positive=True)
    C = sp.sqrt(1 + b*b)
    r = -s*s / h**2
    u = 2*s*s*C / h**2
    v = 2*s*s*b / h**2
    _, h2, _, J = pullback(r, u, v, s)
    assert sp.simplify(h2 - h*h) == 0
    assert sp.simplify(J - 4*h*h*s*s*b*b) == 0


def test_general_quartic_quadratic_principal_coefficients():
    r, u, v, s, m2, l1, l2 = sp.symbols(
        "r u v s m2 l1 l2", real=True, nonzero=True
    )
    _, _, H, J = pullback(r, u, v, s)
    # V=m2 H + l1 H² + l2 |det Theta|², |det|²=J+H²/4.
    V = m2*H + (l1 + l2/4)*H*H + l2*J
    L = -V
    A = 8*s*s*r*(1-r)
    beta = l1 + l2/4
    expected_tt = 6*m2*A/u**4 - 20*beta*A*A/u**6
    expected_xx = 2*m2*A/u**4 - 4*beta*A*A/u**6 + 128*l2*s**4*r**3/u**6
    assert sp.factor(sp.diff(L, u, 2).subs(v, 0) - expected_tt) == 0
    assert sp.factor(sp.diff(L, v, 2).subs(v, 0) - expected_xx) == 0


def test_universal_sign_contradiction_independent_of_mass():
    r, u, v, s, m2, l1, l2 = sp.symbols(
        "r u v s m2 l1 l2", real=True, nonzero=True
    )
    _, _, H, J = pullback(r, u, v, s)
    L = -m2*H - (l1 + l2/4)*H*H - l2*J
    tt = sp.factor(sp.diff(L, u, 2).subs(v, 0))
    xx = sp.factor(sp.diff(L, v, 2).subs(v, 0))
    expected = -128*s**4*r*r*(
        4*l1*(1-r)**2 + l2*(1+r+r*r)
    )/u**6
    assert sp.factor(tt - 3*xx - expected) == 0


def test_independent_quartic_sign_witnesses():
    t = sp.symbols("t", real=True)
    X1 = sp.Matrix([[0, 1], [0, 0]])  # det zero, H=-t²
    X2 = sp.diag(1, sp.I)              # H zero, |det|²=t^4
    H1, J1 = invariants(t*X1)
    H2, J2 = invariants(t*X2)
    assert H1 == -t*t and J1 == -t**4/4
    assert H2 == 0 and J2 == t**4
    assert sp.factor(H1**2 - t**4) == 0


def test_rest_j_gives_spatial_stiffness_without_time_quadratic():
    r, u, v, s = sp.symbols("r u v s", real=True, nonzero=True)
    _, _, _, J = pullback(r, u, v, s)
    assert sp.factor(sp.diff(J, u, 2).subs(v, 0)) == 0
    assert sp.factor(sp.diff(J, v, 2).subs(v, 0) + 128*s**4*r**3/u**6) == 0


def test_tilt_j_can_have_wrong_sign_fixed_time_kinetic():
    r, u, v, s = sp.symbols("r u v s", real=True, nonzero=True)
    _, _, _, J = pullback(r, u, v, s)
    dt2 = sp.factor(sp.diff(J, u, 2))
    expected = 384*s**4*r**3*v*v*(v*v + 7*u*u)/(v*v-u*u)**5
    assert sp.factor(dt2 - expected) == 0
    assert dt2.subs({r:-1, u:-2, v:1, s:1}) == sp.Rational(3712, 81)


def test_tuned_mass_cannot_fix_both_signs_in_simple_example():
    r, u, v, s, m2, l1, l2 = sp.symbols("r u v s m2 l1 l2", real=True)
    _, _, H, J = pullback(r, u, v, s)
    L = -m2*H - (l1 + l2/4)*H*H - l2*J
    b = {r:-1, u:-2, v:0, s:1, l1:0, l2:1, m2:-5}
    assert sp.factor(sp.diff(L, u, 2).subs(b)) == 10
    assert sp.factor(sp.diff(L, v, 2).subs(b)) == 4
    assert sp.factor(sp.diff(L, u, 2).subs(b) -
                     3*sp.diff(L, v, 2).subs(b)) == -2


def test_det_zero_and_h_zero_rays_force_independent_quartic_signs():
    t = sp.symbols("t", real=True)
    X1 = sp.Matrix([[0, 1], [0, 0]])
    X2 = sp.diag(1, sp.I)
    H1, J1 = invariants(t*X1)
    H2, J2 = invariants(t*X2)
    assert sp.factor(J1 + H1**2/4) == 0
    assert sp.factor(J2 - t**4) == 0


def test_no_internal_compact_psi_derivative_generated():
    r, u, v, s, psi = sp.symbols("r u v s psi", real=True)
    _, _, _, J = pullback(r, u, v, s)
    assert psi not in J.free_symbols


def test_exact_fixed_clock_bloch_vector_is_collinear_with_spatial_gradient():
    h, x0, x, y, z = sp.symbols("h x0 x y z", real=True)
    t = full_theta(h, (x0, x, y, z))
    q = sp.simplify(t * t.H)
    total = h*h + x0*x0 + x*x + y*y + z*z
    assert sp.simplify(q - (
        total*I2 - 2*x0*(x*SX + y*SY + z*SZ)
    )) == sp.zeros(2)
    density = sp.simplify(q / sp.trace(q))
    for sigma, component in ((SX,x), (SY,y), (SZ,z)):
        assert sp.factor(sp.trace(density*sigma) + 2*x0*component/total) == 0


def test_fixed_clock_bloch_frobenius_helcity_and_helical_counterexample():
    x, y, z = sp.symbols("x y z", real=True)
    scalar = sp.Function("r")(x, y, z)
    multiplier = sp.Function("f")(x, y, z)
    v = sp.Matrix([multiplier*sp.diff(scalar, q) for q in (x, y, z)])

    def curl(vector):
        return sp.Matrix([
            sp.diff(vector[2], y) - sp.diff(vector[1], z),
            sp.diff(vector[0], z) - sp.diff(vector[2], x),
            sp.diff(vector[1], x) - sp.diff(vector[0], y),
        ])

    assert sp.simplify(sp.expand(v.dot(curl(v)))) == 0
    helical = sp.Matrix([-y/4, x/4, sp.Rational(1, 4)])
    assert sp.simplify(helical.dot(curl(helical))) == sp.Rational(1, 8)
    assert (helical.dot(helical)).subs({x: 1, y: 1}) < 1


def test_strict_quartic_sign_form():
    r = sp.symbols("r", real=True)
    assert sp.factor(
        1+r+r*r - ((r + sp.Rational(1, 2))**2 + sp.Rational(3, 4))
    ) == 0
