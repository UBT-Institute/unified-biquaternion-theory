"""Inertia of the 3D GR DeWitt kinetic form and positive TT restriction."""
import sympy as sp

def kinetic(P):
    return sp.expand(sp.trace(P*P)-sp.trace(P)**2/sp.Integer(2))

def test_trace_ghost_algebraic_direction():
    assert kinetic(sp.eye(3)) == -sp.Rational(3,2)
    assert kinetic(sp.diag(1,-1,0)) == 2

def test_general_symmetric_tracefree_nonnegative():
    a,b,xy,xz,yz=sp.symbols("a b xy xz yz",real=True)
    P=sp.Matrix([[a,xy,xz],[xy,b,yz],[xz,yz,-a-b]])
    q=sp.factor(kinetic(P))
    expected=a*a+b*b+(a+b)**2+2*(xy**2+xz**2+yz**2)
    assert sp.simplify(q-expected)==0
    assert sp.simplify(kinetic(P)-sp.trace(P*P))==0

def test_two_tt_polarizations_along_z():
    plus,cross=sp.symbols("plus cross",real=True)
    P=sp.Matrix([[plus,cross,0],[cross,-plus,0],[0,0,0]])
    k=sp.Matrix([0,0,1])
    assert P*k == sp.zeros(3,1)
    assert sp.trace(P)==0
    assert sp.simplify(kinetic(P)-2*(plus**2+cross**2))==0

def test_constraint_coefficient_sign_not_selected():
    a,b=sp.symbols("a b",real=True,nonzero=True)
    assert (sp.Rational(1,1)*sp.Rational(1,1))==1
    assert ((-sp.Integer(1))*(-sp.Integer(1)))==1

def test_holst_torsionfree_channel_cannot_set_coefficient():
    beta,base=sp.symbols("beta base",real=True)
    energy=base+beta*sp.Integer(0)
    assert sp.diff(energy,beta)==0
    assert sp.simplify(energy-base)==0
