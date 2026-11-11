"""Conditional positive TT energy for the already-postulated split-jet Palatini comparator."""
import sympy as sp


def test_transverse_traceless_polarizations_for_z_wave():
    plus,cross=sp.symbols("plus cross",real=True)
    h=sp.Matrix([[plus,cross,0],[cross,-plus,0],[0,0,0]])
    kvec=sp.Matrix([0,0,1])
    assert sp.trace(h)==0
    assert h*kvec==sp.zeros(3,1)
    assert h==h.T
    assert sp.simplify(sp.trace(h.T*h)-2*(plus**2+cross**2))==0


def test_tt_energy_positive_and_legendre():
    kappa=sp.symbols("kappa",positive=True)
    v,g=sp.symbols("v g",real=True)
    L=(v*v-g*g)/(8*kappa)
    momentum=sp.diff(L,v)
    P=sp.symbols("P",real=True)
    H=sp.factor((momentum*v-L).subs(v,4*kappa*P))
    assert sp.simplify(H-(2*kappa*P*P+g*g/(8*kappa)))==0


def test_nonzero_mode_hamilton_flow_conserves_energy():
    omega,q,p=sp.symbols("omega q p",positive=True)
    energy=(p*p+omega**2*q*q)/2
    derivative=sp.diff(energy,q)*p+sp.diff(energy,p)*(-omega**2*q)
    assert sp.simplify(derivative)==0


def test_wave_frequency_real_for_nonzero_k():
    k=sp.symbols("k",positive=True)
    t,A,B=sp.symbols("t A B",real=True)
    q=A*sp.cos(k*t)+B*sp.sin(k*t)
    assert sp.simplify(sp.diff(q,t,2)+k*k*q)==0
    assert sp.simplify((sp.diff(q,t)**2+k*k*q*q)/2
        -k*k*(A*A+B*B)/2)==0


def test_zero_momentum_mode_is_not_claimed_as_strictly_stable():
    t,p0,q0=sp.symbols("t p0 q0",real=True)
    q=q0+p0*t
    assert sp.diff(q,t,2)==0
    assert sp.diff(q,t)==p0
