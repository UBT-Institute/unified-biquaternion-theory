import sympy as s

def test_complex_projector_imaginary_rank_and_gravity_hessian():
    G=s.diag(1,-1,-1,-1)
    e0=s.Matrix([1,0,0,0])
    y=s.symbols("y0:4",real=True)
    v=s.Matrix([s.I*yi for yi in y])
    dP=v*e0.T*G+e0*s.conjugate(v).T*G
    entries=list(dP)
    J=s.Matrix([[s.diff(s.re(z),w) for w in y] for z in entries]+[[s.diff(s.im(z),w) for w in y] for z in entries])
    assert J.rank()==3
    assert J.nullspace()==[s.Matrix([1,0,0,0])]
    assert s.simplify(dP.subs(dict(zip(y,[0,0,0,0]))))==s.zeros(4)
    # Conditional action L_g=L_g(X, dot(X), auxiliaries) cannot depend on dot(Y).
    dx=s.symbols("dx0:4")
    dy=s.symbols("dy0:4")
    L=sum(d*d for d in dx) # representative X-only kinetic polynomial
    H=s.hessian(L,(*dx,*dy))
    assert H[4:8, :]==s.zeros(4,8)
    assert H[:,4:8]==s.zeros(8,4)
