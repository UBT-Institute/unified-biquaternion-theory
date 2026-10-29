import sympy as s

def test_su3_frame_cannot_undo_splitjet_carrier_replacement():
    G=s.diag(1,-1,-1,-1)
    n=s.Matrix([1,0,0,0])
    m=s.Matrix([s.sqrt(2),1,0,0])
    assert (n.T*G*n)[0]==1
    assert (m.T*G*m)[0]==1
    P=lambda x:x*x.T*G
    assert P(n)[0,1]==0
    assert P(m)[0,1]==-s.sqrt(2)
    assert P(n)!=P(m)
    assert P(n)*P(n)==P(n)
    assert s.simplify(P(m)*P(m)-P(m))==s.zeros(4)

def test_geometry_can_be_fixed_during_carrier_change():
    old, new, cov_old, cov_new, q=s.symbols("old new cov_old cov_new q")
    qprime=q+cov_old-cov_new
    assert s.simplify(cov_new+qprime-(cov_old+q))==0
