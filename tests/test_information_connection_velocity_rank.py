import sympy as s

def test_composite_connection_jacobian_inertia_examples():
    G=s.diag(1,1,-1,-1,-1,-1,-1,-1)
    I=s.eye(8)
    def W(M): return M.T*G*M
    assert W(I)==G
    assert G.rank()==8
    proj=s.diag(1,1,0,0,0,0,0,0)
    assert W(proj).rank()==2
    assert W(proj)==proj
    mixed=s.diag(1,0,1,0,0,0,0,0)
    assert W(mixed).rank()==2
    assert W(mixed)[2,2]==-1
    u=s.Matrix(s.symbols("u0:8",real=True))
    scale=s.diag(2,3,4,5,6,7,8,9)
    L=(u.T*scale.T*G*scale*u)[0]/2
    assert s.hessian(L,list(u))==W(scale)
