import sympy as s

def test_projector_differential_real_ranks():
    # At Theta=r e_0, the linearized projector off-diagonal entries
    # contain all three complex spatial variations and no time variation.
    a=s.symbols("a0:4", real=True)
    b=s.symbols("b0:4", real=True)
    u=[a[j]+s.I*b[j] for j in range(4)]
    G=s.diag(1,-1,-1,-1)
    e0=s.Matrix([1,0,0,0])
    uperp=s.Matrix([0,u[1],u[2],u[3]])
    dP=uperp*e0.T*G+e0*s.conjugate(uperp).T*G
    entries=list(dP)
    variables=list(a)+list(b)
    Jacobian=s.Matrix([[s.diff(s.re(z),v) for v in variables] for z in entries]+[[s.diff(s.im(z),v) for v in variables] for z in entries])
    assert Jacobian.rank()==6
    assert Jacobian.nullspace()==[s.eye(8)[:,0],s.eye(8)[:,4]]
    assert Jacobian[:,0:4].rank()==3
    assert s.simplify(s.trace(dP*dP)+2*sum(s.expand_complex(s.conjugate(u[j])*u[j]) for j in range(1,4)))==0
