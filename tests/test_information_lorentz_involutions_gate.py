import sympy as s

def test_involutions_preserve_unfixed_gap():
    a,b=s.symbols('a b',real=True)
    H=s.diag(a,b,b,b)
    P2=s.diag(1,-1,-1,-1)
    P3=s.diag(1,1,-1,-1)
    assert H*P2==P2*H
    assert H*P3==P3*H
    assert H.conjugate()==H
    assert H.subs({a:1,b:2})!=s.eye(4)

def test_lorentz_boost_is_not_unitary_four_vector():
    z=s.symbols('z',real=True)
    B=s.eye(4)
    B[0,0]=B[1,1]=s.cosh(z)
    B[0,1]=B[1,0]=s.sinh(z)
    eta=s.diag(1,-1,-1,-1)
    assert s.simplify(B.T*eta*B)==eta
    assert s.simplify(B.T*B-s.eye(4))!=s.zeros(4)

def test_symmetric_information_state_commutes_with_any_gap():
    p,a,b=s.symbols('p a b',real=True)
    rho=s.diag(p,(1-p)/3,(1-p)/3,(1-p)/3)
    H=s.diag(a,b,b,b)
    assert H*rho-rho*H==s.zeros(4)

def test_coherence_detects_gap_if_observable():
    t,delta=s.symbols('t delta',real=True)
    psi=s.Matrix([1,s.exp(-s.I*delta*t)])/s.sqrt(2)
    sigma_x=s.Matrix([[0,1],[1,0]])
    assert s.trigsimp(s.expand_complex((s.conjugate(psi).T*sigma_x*psi)[0])-s.cos(delta*t))==0
