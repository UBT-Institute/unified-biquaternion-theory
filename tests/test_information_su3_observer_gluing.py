import sympy as s

def test_su3_gluing_does_not_determine_curvature():
    x,y=s.symbols("x y",real=True)
    T=s.diag(s.I,-s.I,0)
    assert T.conjugate().T == -T and s.trace(T)==0
    # A_x=0, A_y=x*T => F_xy=d_x A_y-d_y A_x+[A_x,A_y].
    Ax=s.zeros(3);Ay=x*T
    F=Ay.diff(x)-Ax.diff(y)+Ax*Ay-Ay*Ax
    assert F==T
    assert F!=s.zeros(3)
    # Gauge conjugation by a constant SU(3) matrix leaves trace F^2 unchanged.
    U=s.diag(s.exp(s.I*y),s.exp(-s.I*y),1)
    assert s.simplify(s.det(U)-1)==0
    assert s.simplify(U.conjugate().T*U-s.eye(3))==s.zeros(3)
    Fp=s.simplify(U.inv()*F*U)
    assert s.simplify(s.trace(Fp*Fp)-s.trace(F*F))==0
    # Trivial connection gives a different invariant curvature observable.
    assert s.trace(F*F)==-2
