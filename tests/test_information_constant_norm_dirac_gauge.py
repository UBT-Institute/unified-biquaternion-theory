import sympy as s

def test_norm_constraint_has_rank_one_at_timelike_point():
    x=s.Matrix(s.symbols("x0:4",real=True));G=s.diag(1,-1,-1,-1)
    chi=(x.T*G*x)[0]-s.symbols("h0",positive=True)
    jac=s.Matrix([chi]).jacobian(list(x))
    assert jac.rank()==1
    r=s.symbols("r",positive=True)
    J=jac.subs({x[0]:r,x[1]:0,x[2]:0,x[3]:0})
    assert J==s.Matrix([[2*r,0,0,0]])
    assert len(J.nullspace())==3

def test_radial_gauge_fixing_bracket():
    x=s.Matrix(s.symbols("x0:4",real=True));p=s.Matrix(s.symbols("p0:4",real=True))
    h0=s.symbols("h0",positive=True)
    G=s.diag(1,-1,-1,-1)
    chi=(x.T*G*x)[0]-h0
    cr=(x.dot(p))/(2*h0)
    pb=sum(s.diff(chi,x[j])*s.diff(cr,p[j])-s.diff(chi,p[j])*s.diff(cr,x[j]) for j in range(4))
    assert s.simplify(pb.subs({x[0]:s.sqrt(h0),x[1]:0,x[2]:0,x[3]:0})-1)==0
