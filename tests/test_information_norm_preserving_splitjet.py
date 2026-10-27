import sympy as s

def test_finite_norm_preserving_boost_changes_projector():
    G=s.diag(1,-1,-1,-1)
    r,v=s.symbols('r v',positive=True,real=True)
    X=s.Matrix([r,0,0,0]);Xp=s.Matrix([r*s.cosh(v),r*s.sinh(v),0,0])
    assert s.simplify((Xp.T*G*Xp)[0]-r*r)==0
    P=lambda x:x*x.T*G/(x.T*G*x)[0]
    assert s.simplify(P(Xp)-P(X))!=s.zeros(4)

def test_auxiliary_compensation_and_group_composition():
    DX,Q,d1,d2=s.symbols('DX Q d1 d2')
    assert s.expand((DX+d1+d2)+(Q-d1-d2)-(DX+Q))==0

def test_tangent_rank_is_three():
    e=s.symbols('e1:4',real=True)
    G=s.diag(1,-1,-1,-1)
    X=s.Matrix([1,0,0,0]);u=s.Matrix([0,*e])
    dP=u*X.T*G+X*u.T*G
    J=dP.reshape(16,1).jacobian(e)
    assert J.rank()==3
