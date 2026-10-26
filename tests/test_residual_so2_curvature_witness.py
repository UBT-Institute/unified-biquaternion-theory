import sympy as s

def test_nonflat_residual_so2_is_not_locally_pure_gauge():
    x,y=s.symbols("x y",real=True)
    J=s.zeros(4)
    J[2,3]=1
    J[3,2]=-1
    eta=s.diag(-1,1,1,1)
    v=s.Matrix([1,0,0,0])
    w=s.Matrix([0,1,0,0])
    assert J.T*eta+eta*J==s.zeros(4)
    assert J*v==s.zeros(4,1) and J*w==s.zeros(4,1)
    # alpha_x=0, alpha_y=x; so F_xy = d_x alpha_y - d_y alpha_x = 1.
    alpha_x=s.Integer(0)
    alpha_y=x
    Fxy=s.diff(alpha_y,x)-s.diff(alpha_x,y)
    assert Fxy==1
    Rxy=Fxy*J
    assert Rxy != s.zeros(4)
    # Adding d chi changes alpha but leaves curvature invariant.
    chi=x*x*y
    transformed_x=alpha_x+s.diff(chi,x)
    transformed_y=alpha_y+s.diff(chi,y)
    assert s.simplify(s.diff(transformed_y,x)-s.diff(transformed_x,y))==Fxy
