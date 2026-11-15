"""Conditional one-Theta flat Dirac vector U1 vs canonical sharp tetrad gate.

These tests are algebraic. They do NOT establish local QED dynamics or the
physical UBT gauge quotient.
"""
import sympy as sp

I = sp.I
sigma0 = sp.eye(2)
sigma1 = sp.Matrix([[0, 1], [1, 0]])
sigma2 = sp.Matrix([[0, -I], [I, 0]])
sigma3 = sp.diag(1, -1)
eps = I*sigma2
swap = sigma1
alpha = sp.symbols("alpha", real=True)
R = sp.diag(sp.exp(I*alpha), sp.exp(-I*alpha))
u0, u1, v0, v1 = sp.symbols("u0 u1 v0 v1", complex=True)
Theta = sp.Matrix([[u0, v0], [u1, v1]])


def zero(M):
    return M.applyfunc(lambda value: sp.simplify(sp.expand_complex(value))) == sp.zeros(*M.shape)


def sharp(M):
    return sp.Matrix([[M[1, 1], -M[0, 1]],
                      [-M[1, 0], M[0, 0]]])


def test_opposite_columns_are_dirac_vector_phase():
    transformed = Theta*R
    psi_l = Theta[:, 0]
    psi_r = eps*Theta[:, 1].conjugate()
    assert zero(transformed[:, 0] - sp.exp(I*alpha)*psi_l)
    assert zero(eps*transformed[:, 1].conjugate() - sp.exp(I*alpha)*psi_r)
    assert zero(eps*(sp.exp(I*alpha)*Theta[:, 1]).conjugate()
                - sp.exp(-I*alpha)*psi_r)


def test_mass_and_antilinear_dirac_map_equivariance():
    assert sp.simplify(R.det() - 1) == 0
    assert sp.simplify((Theta*R).det() - Theta.det()) == 0
    assert zero(R.conjugate()*swap - swap*R)
    J = eps*Theta.conjugate()*swap
    J_transformed = eps*(Theta*R).conjugate()*swap
    assert zero(J_transformed-J*R)


def test_right_sl2_phase_preserves_central_sharp_metric():
    assert zero(sharp(R)*R-sigma0)
    E = [I*sigma0, I*sigma1, I*sigma2, I*sigma3]
    for em in E:
        for en in E:
            before = (sharp(em)*en + sharp(en)*em)/2
            after = (sharp(em*R)*(en*R) + sharp(en*R)*(em*R))/2
            assert zero(after-before)


def test_right_vector_phase_fails_canonical_real_lorentz_slice():
    E0 = I*sigma0
    E0prime = E0*R
    assert zero(E0prime + E0prime.H + 2*sp.sin(alpha)*sigma3)
    assert (E0prime + E0prime.H).subs(alpha, sp.pi/2) != sp.zeros(2)


def test_right_charge_commutes_left_spin_but_not_lorentz_congruence():
    b = sp.symbols("b", real=True)
    S = sp.cos(b/2)*sigma0 + I*sp.sin(b/2)*sigma1
    assert zero(S*(Theta*R)-(S*Theta)*R)
    assert not zero(S.H*R-R*S.H)
    assert zero((S.H*R-R*S.H).subs({alpha:0}))


def test_formal_local_right_gauge_transport_only():
    x, q = sp.symbols("x q", real=True)
    a = sp.Function("a")(x)
    phi = sp.Function("phi")(x)
    F = sp.Matrix([[sp.Function("f0")(x),sp.Function("f1")(x)],
                   [sp.Function("f2")(x),sp.Function("f3")(x)]])
    rot = sp.diag(sp.exp(I*q*phi),sp.exp(-I*q*phi))
    derivative = F.diff(x)-I*q*a*F*sigma3
    transformed = (F*rot).diff(x)-I*q*(a+phi.diff(x))*(F*rot)*sigma3
    assert zero(transformed-derivative*rot)


def test_alternative_bilinear_soldering_flat_lorentz_metric_and_right_u2_blindness():
    t, x, y, z, c = sp.symbols("t x y z c", real=True)
    K = (c+t)*sigma0 + x*sigma1 + y*sigma2 + z*sigma3
    assert zero(K-K.H)
    assert sp.simplify(K.det()-((c+t)**2-x**2-y**2-z**2)) == 0
    # This K has a positive-definite patch c+t>sqrt(x^2+y^2+z^2)
    # and hence a local Theta=positive_sqrt(K) with K=Theta Theta^dagger.
    E = [I*K.diff(q) for q in (t, x, y, z)]
    eta = sp.diag(-1, 1, 1, 1)
    for a in range(4):
        assert zero(E[a]+E[a].H)
        for b in range(4):
            metric = (sharp(E[a])*E[b]+sharp(E[b])*E[a])/2
            assert zero(metric-eta[a,b]*sigma0)
    assert zero(R*R.H-sigma0)
    # More than EM U1 survives: any right U(2) is invisible to K.
    beta = sp.symbols("beta", real=True)
    U = sp.cos(beta)*sigma0+I*sp.sin(beta)*sigma1
    assert zero(U*U.H-sigma0)
    assert zero(U*U.H-R*R.H)
