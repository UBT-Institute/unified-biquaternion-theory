import sympy as s

def test_two_carrier_algebraic_stabilizer_obstruction():
    v=s.Matrix([1,0,0,0])
    w=s.Matrix([1,1,0,0])
    J=s.zeros(4)
    J[2,3]=1
    J[3,2]=-1
    eta=s.diag(-1,1,1,1)
    assert J.T*eta+eta*J==s.zeros(4)
    assert J*v==s.zeros(4,1) and J*w==s.zeros(4,1)
    assert J.rank()==2
    assert s.Matrix.hstack(v,w).rank()==2
    assert all(J*z==s.zeros(4,1) for z in [v,w])
    assert J.nullspace()[0] in [s.Matrix([1,0,0,0]),s.Matrix([0,1,0,0])]
