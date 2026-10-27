import sympy as s

def test_dirac_mass_equals_biquaternion_determinant():
    u0,u1,v0,v1=s.symbols("u0 u1 v0 v1",complex=True)
    e=s.Matrix([[0,1],[-1,0]])
    u=s.Matrix([u0,u1]);v=s.Matrix([v0,v1])
    theta=s.Matrix.hstack(u,v)
    right=e*v.conjugate()
    assert s.simplify((right.conjugate().T*u)[0]-theta.det())==0

def test_phase_charge_two():
    phi=s.symbols("phi",real=True)
    u0,u1,v0,v1=s.symbols("u0 u1 v0 v1")
    theta=s.Matrix([[u0,v0],[u1,v1]])
    assert s.simplify((s.exp(s.I*phi)*theta).det()-s.exp(2*s.I*phi)*theta.det())==0

def test_spin_sl2_invariance_of_determinant():
    a,b,c=s.symbols("a b c",nonzero=True)
    S=s.Matrix([[a,b],[c,(1+b*c)/a]])
    theta=s.Matrix(s.symbols("t0:4")).reshape(2,2)
    assert s.simplify((S*theta).det()-theta.det())==0
