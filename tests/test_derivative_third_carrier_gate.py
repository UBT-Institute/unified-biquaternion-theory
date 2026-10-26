import sympy as s

def test_metric_gradient_third_direction_does_not_fix_connection():
    eta=s.diag(-1,1,1,1)
    v=s.Matrix([1,0,0,0]); w=s.Matrix([0,1,0,0])
    A=s.Matrix.hstack(v,w)
    gram=A.T*eta*A
    P=s.eye(4)-A*gram.inv()*A.T*eta
    q=s.Matrix([3,4,5,6])
    u=P*q
    assert u==s.Matrix([0,0,5,6])
    assert A.row_join(u).rank()==3
    J=s.zeros(4); J[2,3]=1;J[3,2]=-1
    assert J.T*eta+eta*J==s.zeros(4)
    assert J*v==s.zeros(4,1) and J*w==s.zeros(4,1)
    assert J*u!=s.zeros(4,1)
    assert P*P==P
