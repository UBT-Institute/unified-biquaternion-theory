import sympy as s

def test_induced_metric_contraction_reduces_to_volume():
    t0,t1,t2,t3=s.symbols("t0:4",real=True)
    E=s.Matrix([[t0,t1,t2,t3],[1,0,0,0],[0,1,0,0],[0,0,1,1]])
    eta=s.diag(-1,1,1,1)
    g=E*eta*E.T
    assert s.simplify(s.det(g)+s.det(E)**2)==0
    contracted=s.trace(g.inv()*E*eta*E.T)
    assert s.simplify(contracted-4)==0
    assert s.hessian(E.det(),(t0,t1,t2,t3))==s.zeros(4)
    assert s.simplify(s.det(E))!=0
