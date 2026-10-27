import sympy as s

def test_exact_two_by_two_determinant_shift():
    a,b,c,d,x,y,z,w=s.symbols("a b c d x y z w")
    T=s.Matrix([[a,b],[c,d]])
    E=s.Matrix([[x,y],[z,w]])
    derivative=s.trace(T.adjugate()*E)
    assert s.expand((T+E).det()-T.det()-derivative-E.det())==0

def test_scalar_mass_changes_along_identity_shift():
    t,m=s.symbols("t m",real=True)
    T=s.eye(2)
    E=t*s.eye(2)
    M=2*m*(T+E).det()
    assert s.diff(M,t).subs(t,0)==4*m

def test_hermitian_slice_determinant_is_lorentz_norm():
    x0,x1,x2,x3=s.symbols("x0 x1 x2 x3",real=True)
    T=s.Matrix([[x0+x3,x1-s.I*x2],[x1+s.I*x2,x0-x3]])
    assert s.simplify(T.det()-(x0*x0-x1*x1-x2*x2-x3*x3))==0
