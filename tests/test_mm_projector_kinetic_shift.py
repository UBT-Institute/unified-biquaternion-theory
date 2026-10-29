import sympy as s

def test_projector_kinetic_has_nonzero_rank_on_old_shift_directions():
    G=s.diag(1,-1,-1,-1)
    e=s.Matrix([1,0,0,0])
    u=s.symbols("u0:3",real=True)
    z=s.Matrix([0,*u])
    dP=z*e.T*G+e*z.T*G
    assert s.simplify(-s.trace(dP*dP)-2*sum(t*t for t in u))==0
    c=s.symbols("c",positive=True)
    L=c*sum(t*t for t in u)/2
    assert s.hessian(L,u)==c*s.eye(3)
    eps=s.symbols("eps0:3",real=True)
    change=s.expand(L.subs({u[i]:u[i]+eps[i] for i in range(3)})-L)
    assert s.simplify(change.subs({u[i]:0 for i in range(3)})-c*sum(t*t for t in eps)/2)==0

def test_full_complex_projector_tangent_rank_six():
    u=s.symbols("u0:6",real=True)
    c=s.symbols("c",positive=True)
    H=s.hessian(c*sum(v*v for v in u)/2,u)
    assert H.rank()==6
    J=s.eye(6)[:,:3]
    assert (J.T*H*J).rank()==3
