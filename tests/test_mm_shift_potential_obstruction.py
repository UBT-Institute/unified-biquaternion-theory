import sympy as s

def test_lorentz_real_quartic_shift_condition():
    r,m,l1,l2=s.symbols("r m l1 l2",real=True)
    V=2*m*r+(4*l1+l2)*r**2
    conditions=s.Poly(s.diff(V,r),r).all_coeffs()
    assert s.solve(conditions,(m,l2))=={m:0,l2:-4*l1}

def test_independent_kinetic_term_breaks_shift():
    a,b,eps=s.symbols("a b eps",real=True)
    # dX=a; shift changes dX while auxiliary Q compensates to keep E=a+b.
    assert s.expand((a+eps)+(b-eps)-(a+b))==0
    assert s.expand((a+eps)**2-a**2)!=0
