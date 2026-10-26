import sympy as s

def test_two_carrier_first_jet_is_blind_to_so2_stabilizer():
    eta=s.diag(-1,1,1,1)
    v=s.Matrix([1,0,0,0])
    w=s.Matrix([0,1,0,0])
    J=s.zeros(4)
    J[2,3]=1; J[3,2]=-1
    params=s.symbols("alpha0:4")
    assert J.T*eta+eta*J==s.zeros(4)
    assert J*v==s.zeros(4,1) and J*w==s.zeros(4,1)
    # In a comparison configuration with a prescribed invertible tetrad E
    # and prescribed derivatives dv, the stabilizer contribution to Dv vanishes.
    E=s.eye(4)
    for p in params:
        assert p*J*v==s.zeros(4,1)
        assert p*J*w==s.zeros(4,1)
    volume=s.det(E)
    assert volume==1
    assert all(s.diff(volume,p)==0 for p in params)
