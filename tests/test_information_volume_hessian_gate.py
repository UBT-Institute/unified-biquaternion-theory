import sympy as s

def test_volume_term_does_not_modify_velocity_hessian():
    p=s.symbols("p0:8", real=True)
    lam=s.symbols("lam",real=True)
    spatial=s.Matrix([[1,2,3,4],[0,1,1,2],[1,0,2,1]])
    E=s.Matrix.vstack(s.Matrix(1,4,list(p[:4])),spatial)
    G=s.diag(1,1,-1,-1,-1,-1,-1,-1)
    P=s.Matrix(p)
    L=(P.T*G*P)[0]/2+lam*E.det()
    assert s.hessian(E.det(),p)==s.zeros(8)
    assert s.hessian(L,p)==G
    assert G.det()!=0
    assert [G[i,i] for i in range(8)].count(-1)==6
