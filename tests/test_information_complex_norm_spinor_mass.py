import sympy as s

def test_real_norm_fixed_while_complex_mass_changes():
    t,m=s.symbols("t m",real=True)
    X=s.eye(2)
    T=(1+s.I)*s.eye(2)
    D=s.I*t*s.diag(1,0)
    assert X.det()==1
    assert s.simplify(s.re(s.expand((T+D).det()))+t)==0
    assert s.diff(2*m*s.re(s.expand((T+D).det())),t)==-2*m

def test_det_real_imag_constraints_independent_generically():
    a,b=s.symbols("a b",real=True)
    T=s.eye(2)
    delta=s.diag(a+s.I*b,0)
    z=s.trace(T.adjugate()*delta)
    j=s.Matrix([s.re(z),s.im(z)]).jacobian([a,b])
    assert j==s.eye(2)
