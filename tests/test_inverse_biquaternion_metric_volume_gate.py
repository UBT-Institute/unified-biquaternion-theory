"""Biquaternion central-Jordan identity and fixed-volume rank gate."""
import sympy as sp


def qmul(a,b):
    a0,a1,a2,a3=a
    b0,b1,b2,b3=b
    return sp.Matrix([
        a0*b0-a1*b1-a2*b2-a3*b3,
        a0*b1+a1*b0+a2*b3-a3*b2,
        a0*b2-a1*b3+a2*b0+a3*b1,
        a0*b3+a1*b2-a2*b1+a3*b0,
    ])


def sharp(a):
    return [a[0],-a[1],-a[2],-a[3]]


def test_complex_biquaternion_jordan_centrality():
    a=sp.symbols("a0:4")
    b=sp.symbols("b0:4")
    joint=(qmul(sharp(a),b)+qmul(sharp(b),a))/2
    metric=sum(a[i]*b[i] for i in range(4))
    assert all(sp.expand(joint[i]-(metric if i==0 else 0))==0
               for i in range(4))


def test_lorentz_real_slice_signature():
    t,x,y,z=sp.symbols("t x y z",real=True)
    u,v,w,r=sp.symbols("u v w r",real=True)
    a=(sp.I*t,x,y,z)
    b=(sp.I*u,v,w,r)
    metric=sum(a[i]*b[i] for i in range(4))
    assert sp.expand(metric-(-t*u+x*v+y*w+z*r))==0


def test_tetrad_metric_determinant():
    E=sp.Matrix([[1,1,0,0],[0,2,1,0],[0,0,3,1],[0,0,0,4]])
    eta=sp.diag(-1,1,1,1)
    g=E*eta*E.T
    assert g.det()==-E.det()**2


def test_full_tetrad_rank_ten_and_volume_restricted_rank_nine():
    # At E=I, δg=δE η + η δEᵀ. Its 10 symmetric outputs
    # span all Sym_4 and the 6-dimensional kernel is Lorentz.
    x=sp.symbols("x0:16")
    dE=sp.Matrix(4,4,x)
    eta=sp.diag(-1,1,1,1)
    dg=dE*eta+eta*dE.T
    y=sp.Matrix([dg[i,j] for i in range(4) for j in range(i,4)])
    J=y.jacobian(x)
    dvol=sp.trace(dE)  # δ|det E| at E=I
    v=sp.Matrix([dvol]).jacobian(x)
    assert J.rank()==10
    assert sp.Matrix.vstack(J,v).rank()==10
    # The constrained tangent has dimension 15; trace-free
    # symmetric metric perturbations have dimension 9.
    assert (16-1)-(16-J.rank())==9
