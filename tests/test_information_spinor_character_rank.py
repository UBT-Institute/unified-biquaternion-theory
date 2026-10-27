import sympy as s

def test_left_doublet_dirac_character_obstruction():
    t,th=s.symbols("t th",real=True)
    z=s.exp(t+s.I*th)
    S=s.diag(z,1/z)
    right=(S.conjugate().T).inv()
    left=2*s.trace(S)
    dr=s.trace(S)+s.trace(right)
    difference=s.simplify(s.expand_complex(left-dr))
    assert s.simplify(difference-4*s.I*s.sinh(t)*s.sin(th))==0 or s.simplify(difference+4*s.I*s.sinh(t)*s.sin(th))==0
    assert difference!=0

def test_theta_to_positive_vector_real_kernel_four():
    # At Theta=I, d(Theta Theta^dagger)=dTheta+dTheta^dagger.
    xs=s.symbols("x0:8",real=True)
    d=s.Matrix([[xs[0]+s.I*xs[1],xs[2]+s.I*xs[3]],
                [xs[4]+s.I*xs[5],xs[6]+s.I*xs[7]]])
    dx=d+d.conjugate().T
    real_outputs=[s.re(dx[0,0]),s.re(dx[1,1]),s.re(dx[0,1]),s.im(dx[0,1])]
    jac=s.Matrix(real_outputs).jacobian(xs)
    assert jac.rank()==4
    assert len(jac.nullspace())==4
