import sympy as s

def test_radial_legendre_transform_positive():
    r,v,p,m=s.symbols('r v p m', real=True, nonnegative=True)
    L=v*v-m*m*r*r
    momentum=s.diff(L,v)
    assert momentum==2*v
    H=s.simplify((p*v-L).subs(v,p/2))
    assert H==p*p/4+m*m*r*r

def test_su3_orbit_stabilizer_dimension():
    # su(3) dim 8, stabilizer of e1 is su(2) dim 3.
    assert 8-3==5
    # Six real triplet components minus orbit five = one radial coordinate.
    assert 6-(8-3)==1
