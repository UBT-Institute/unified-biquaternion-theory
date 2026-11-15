"""L0 exact representation and observer-projective spin lift checks.

No claim of dynamical fermions, Fock statistics, Maxwell photons or a UBT action.
"""
import sympy as sp

I = sp.I
ID = sp.eye(2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -I], [I, 0]])
sz = sp.diag(1, -1)


def zero(m):
    return m.applyfunc(lambda v: sp.simplify(sp.expand_trig(v))) == sp.zeros(*m.shape)


def test_spin_center_is_invisible_on_canonical_congruence_and_jets():
    t, x = sp.symbols("t x", real=True)
    theta = sp.Matrix([[1+I*t, 2+x], [I+x, 1-I*t]])
    minus = -ID
    assert zero(minus*theta*minus.H-theta)
    assert zero(minus*theta.diff(t)*minus.H-theta.diff(t))
    assert zero(minus*theta.diff(x)*minus.H-theta.diff(x))
    assert zero(minus*theta.diff(x, t)*minus.H-theta.diff(x, t))
    psi = sp.Matrix([1, I])
    assert minus*psi == -psi and psi != sp.zeros(2, 1)


def test_no_nonzero_equivariant_map_from_tensorial_data_to_weyl_vector():
    # The central Spin element -I fixes all Lorentz-tensor input data.
    # An equivariant Weyl F must satisfy F=(-I)F, so F=0.
    f0, f1 = sp.symbols("f0 f1")
    f = sp.Matrix([f0, f1])
    constraints = f - (-ID)*f
    assert constraints == 2*f
    assert sp.solve(list(constraints), (f0, f1)) == {f0: 0, f1: 0}


def test_k_theta_theta_dagger_is_not_lorentz_vector_under_congruence_boost():
    beta = sp.symbols("beta", real=True)
    S = sp.diag(sp.exp(beta/2), sp.exp(-beta/2))
    theta = ID
    transformed = S*theta*S.H
    actual = sp.simplify(transformed*transformed.H)
    expected = sp.simplify(S*(theta*theta.H)*S.H)
    assert zero(actual-sp.diag(sp.exp(2*beta), sp.exp(-2*beta)))
    assert zero(expected-sp.diag(sp.exp(beta), sp.exp(-beta)))
    assert actual.subs(beta, 1) != expected.subs(beta, 1)


def test_observer_clock_restores_su2_covariance_on_boost_comparison():
    beta = sp.symbols("beta", real=True)
    S = sp.diag(sp.exp(beta/2), sp.exp(-beta/2))
    N = ID
    Nprime = S*N*S.H
    Np_invhalf = sp.diag(sp.exp(-beta/2), sp.exp(beta/2))
    U = Np_invhalf*S
    theta = ID+sx+I*sy
    T = theta
    theta_prime = S*theta*S.H
    Tprime = sp.simplify(Np_invhalf*theta_prime*Np_invhalf)
    assert zero(U.H*U-ID)
    assert sp.simplify(U.det()) == 1
    assert zero(Tprime-U*T*U.H)
    assert zero(Tprime*Tprime.H-U*(T*T.H)*U.H)


def test_equatorial_projector_returns_after_2pi_but_spinor_changes_sign():
    phi, r = sp.symbols("phi r", real=True, positive=True)
    S = sp.diag(sp.exp(I*phi/2), sp.exp(-I*phi/2))
    K0 = ID+r*sx
    K = sp.simplify(S*K0*S.H)
    P = sp.simplify((K-(1-r)*ID)/(2*r))
    plus = sp.Matrix([1, 1])/sp.sqrt(2)
    psi = sp.simplify(S*plus)
    assert zero(P-psi*psi.H)
    assert zero(P.subs(phi, 2*sp.pi)-P.subs(phi, 0))
    assert zero(psi.subs(phi, 2*sp.pi)+psi.subs(phi, 0))
    assert zero(P**2-P)


def test_projective_berry_holonomy_minus_one_without_global_spinor_selection():
    phi = sp.symbols("phi", real=True)
    v = sp.Matrix([sp.exp(I*phi), 1])/sp.sqrt(2)
    a = sp.simplify(-I*(v.H*v.diff(phi))[0])
    assert a == sp.Rational(1, 2)
    loop = sp.integrate(a, (phi, 0, 2*sp.pi))
    assert loop == sp.pi
    assert sp.simplify(sp.exp(I*loop)) == -1
    assert zero(v.subs(phi, 2*sp.pi)-v.subs(phi, 0))


def test_projective_cp1_curvature_has_unit_chern_integral():
    theta, phi = sp.symbols("theta phi", real=True)
    v = sp.Matrix([sp.cos(theta/2), sp.exp(I*phi)*sp.sin(theta/2)])
    a_phi = sp.trigsimp(-I*(v.H*v.diff(phi))[0])
    a_theta = sp.trigsimp(-I*(v.H*v.diff(theta))[0])
    curv = sp.trigsimp(sp.diff(a_phi, theta)-sp.diff(a_theta, phi))
    assert sp.trigsimp(curv-sp.sin(theta)/2) == 0
    flux = sp.integrate(curv, (theta, 0, sp.pi), (phi, 0, 2*sp.pi))
    assert flux == 2*sp.pi
    assert flux/(2*sp.pi) == 1
