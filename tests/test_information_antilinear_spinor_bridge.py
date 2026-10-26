import sympy as s

def test_epsilon_lorentz_conjugate_identity():
    z,w=s.symbols("z w", nonzero=True)
    # S is generic determinant-one matrix parametrized by a,b,c,d=(1+bc)/a
    a,b,c=s.symbols("a b c",complex=True, nonzero=True)
    S=s.Matrix([[a,b],[c,(1+b*c)/a]])
    eps=s.Matrix([[0,1],[-1,0]])
    assert s.simplify(eps*S.conjugate()*eps.inv()-(S.conjugate().T).inv())==s.zeros(2)
    assert eps*eps.conjugate()==-s.eye(2)

def test_chiral_phase_is_axial():
    phi=s.symbols('phi',real=True)
    eps=s.Matrix([[0,1],[-1,0]])
    v=s.Matrix(s.symbols('v0:2',complex=True))
    J=lambda x:eps*x.conjugate()
    assert s.simplify(J(s.exp(s.I*phi)*v)-s.exp(-s.I*phi)*J(v))==s.zeros(2)

def test_real_linear_bijection_via_inverse():
    eps=s.Matrix([[0,1],[-1,0]])
    v=s.Matrix(s.symbols('v0:2',complex=True))
    right=eps*v.conjugate()
    recovered=eps.inv()*right.conjugate()
    assert s.simplify(recovered-v)==s.zeros(2)
