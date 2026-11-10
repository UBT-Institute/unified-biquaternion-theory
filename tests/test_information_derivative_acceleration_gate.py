"""Information-first full-Theta derivative-invariant acceleration gate.

Exact finite symbolic checks in the already derived fixed-Minkowski-coframe,
positive-H regular representative chart. No full-UBT Hamiltonian is selected.
"""
import sympy as sp


def reduced_invariants(r, u, v, s):
    k = v * v - u * u
    H = 8 * s * s * r * (1 - r) / k
    J = 64 * s**4 * r**3 * v * v / k**3
    q = sp.factor(4 * J / H**2)
    return H, J, q


def parameters():
    return sp.symbols("r u v s", real=True, nonzero=True)


def test_positive_intensity_domain_has_valid_real_logarithm():
    r, u, v, s = parameters()
    H, _, _ = reduced_invariants(r, u, v, s)
    assert H.subs({r: -1, u: -2, v: 1, s: 1}) > 0
    assert sp.simplify(
        H.subs(v, 0) + 8 * s**2 * r * (1-r) / u**2
    ) == 0


def test_score_gradient_contains_velocity_of_rep_label():
    r, u, v, s = parameters()
    H, _, _ = reduced_invariants(r, u, v, s)
    assert sp.factor(sp.diff(H, u) / H + 2*u/(v*v-u*u)) == 0
    assert sp.factor(
        sp.diff(H, r) / H - (1/r - 1/(1-r))
    ) == 0


def test_homogeneous_score_derivative_contains_acceleration():
    r, u, v, s = parameters()
    a = sp.symbols("a", real=True)
    H, _, _ = reduced_invariants(r, u, v, s)
    f = 1/r - 1/(1-r)
    score_dt = sp.factor(
        (sp.diff(H, r)*u + sp.diff(H, u)*a) / H
    )
    assert sp.factor(score_dt.subs(v, 0) - (f*u - 2*a/u)) == 0


def test_projective_contrast_is_dimensionless_and_correct():
    r, u, v, s = parameters()
    _, _, q = reduced_invariants(r, u, v, s)
    expected = 4*r*v*v / ((1-r)**2 * (v*v-u*u))
    assert sp.factor(q - expected) == 0
    assert s not in q.free_symbols


def test_projective_contrast_time_gradient_matches_tilt_identity():
    r, u, v, s = parameters()
    _, _, q = reduced_invariants(r, u, v, s)
    dqdu = sp.factor(sp.diff(q, u))
    expected = 8*r*u*v*v / ((1-r)**2 * (v*v-u*u)**2)
    assert sp.factor(dqdu - expected) == 0
    assert sp.simplify(dqdu.subs({r:-1,u:-2,v:1})) == sp.Rational(4,9)


def test_projective_contrast_first_jet_zero_on_rest_branch():
    r, u, v, s = parameters()
    _, _, q = reduced_invariants(r, u, v, s)
    assert sp.simplify(q.subs(v, 0)) == 0
    for variable in (r, u, v):
        assert sp.simplify(sp.diff(q, variable).subs(v, 0)) == 0


def test_positive_log_score_metric_gives_nondegenerate_acceleration_hessian():
    r, u, v, s = parameters()
    a, kappa = sp.symbols("a kappa", real=True)
    H, _, _ = reduced_invariants(r, u, v, s)
    chi_t = ((sp.diff(H, r)*u + sp.diff(H, u)*a) / H).subs(v, 0)
    L = sp.expand(kappa * chi_t**2 / 2)
    assert sp.factor(sp.diff(L, a, 2) - 4*kappa/u**2) == 0


def test_general_positive_two_by_two_metric_is_nondegenerate_at_rest():
    r, u, v, s = parameters()
    H, _, q = reduced_invariants(r, u, v, s)
    wchi = sp.factor(sp.diff(H, u) / H)
    wq = sp.factor(sp.diff(q, u))
    G = sp.Matrix([[2, 1], [1, 3]])
    assert G.det() == 5
    w = sp.Matrix([wchi, wq])
    hessian = sp.factor((w.T * G * w)[0])
    assert sp.factor(hessian.subs(v, 0) - 8 / u**2) == 0
    assert hessian.subs({r:-1,u:-2,v:1}) > 0


def test_ostro_hamiltonian_linear_in_lowest_momentum():
    r, u, v, s = parameters()
    acc, kappa, P0, P1 = sp.symbols(
        "acc kappa P0 P1", real=True, nonzero=True
    )
    f = 1/r - 1/(1-r)
    potential = r*r + u*u
    L = kappa * (f*u - 2*acc/u)**2 / 2 - potential
    pi = sp.factor(sp.diff(L, acc))
    assert sp.factor(pi + 2*kappa*f - 4*kappa*acc/u**2) == 0
    ainv = u**2 * (P1 + 2*kappa*f) / (4*kappa)
    assert sp.factor(pi.subs(acc, ainv)-P1) == 0
    Hamiltonian = sp.factor((P0*u + P1*acc-L).subs(acc, ainv))
    expected = P0*u + u*u*P1**2/(8*kappa) + u*u*f*P1/2 + potential
    assert sp.factor(Hamiltonian - expected) == 0
    assert sp.diff(Hamiltonian, P0) == u


def test_algebraic_quartic_potential_cannot_cancel_acceleration_square():
    r, u, v, s = parameters()
    acc, m2, l1, l2 = sp.symbols("acc m2 l1 l2", real=True)
    H, J, _ = reduced_invariants(r, u, v, s)
    V = m2*H + (l1+l2/4)*H**2 + l2*J
    assert sp.diff(V, acc, 2) == 0


def test_q_only_tilted_acceleration_hessian():
    r, u, v, s = parameters()
    kappa_q = sp.symbols("kappa_q", real=True)
    _, _, q = reduced_invariants(r, u, v, s)
    coef = sp.factor(kappa_q * sp.diff(q, u)**2)
    assert sp.simplify(coef.subs({r:-1,u:-2,v:1}) - 16*kappa_q/81) == 0
    assert sp.simplify(coef.subs(v, 0)) == 0


def test_no_independent_psi_kinetic_in_this_four_dimensional_candidate():
    r, u, v, s = parameters()
    _, _, q = reduced_invariants(r, u, v, s)
    psi = sp.symbols("psi")
    assert psi not in q.free_symbols
