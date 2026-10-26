import sympy as s

def test_su3_singlet_reduction():
    # Amplitudes on fundamental triplet times antifundamental triplet.
    C=s.eye(3)/s.sqrt(3)
    rho=C*C.conjugate().T
    assert rho==s.eye(3)/3
    assert s.simplify(-sum(rho[i,i]*s.log(rho[i,i]) for i in range(3))-s.log(3))==0
    assert s.trace(rho*rho)==s.Rational(1,3)

def test_entropy_coefficient_is_unfixed_without_cell_area():
    g,ell,a=s.symbols("g ell a",positive=True)
    G=g**2*ell**2/(16*s.pi)
    assert s.solve(s.log(3)/a-1/(4*G),a)==[g**2*ell**2*s.log(3)/(4*s.pi)]
