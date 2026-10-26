import sympy as s

def test_radial_primitive_of_four_form():
    y=s.symbols("y0:4",real=True)
    lam=s.symbols("lam",real=True)
    radius2=sum(z*z for z in y)
    F=1+lam*radius2
    G=s.Rational(1,4)+lam*radius2/s.Integer(6)
    assert s.simplify(sum(s.diff(G*y[i],y[i]) for i in range(4))-F)==0

def test_det_temporal_row_is_affine():
    v=s.symbols("v0:4")
    xs=s.Matrix([[1,2,3,4],[2,1,0,1],[0,1,1,2],[1,0,2,1]])
    rates=s.symbols("p0:4")
    for i,p in enumerate(rates):
        xs[0,i]=p
    h=s.hessian(xs.det(),rates)
    assert h==s.zeros(4)
