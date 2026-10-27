import sympy as s

def test_einstein_vacuum_ricci_has_no_unique_eigenline():
    L=s.symbols("Lambda",real=True)
    R=L*s.eye(4)
    assert R.eigenvals()=={L:4}
    G=s.diag(1,-1,-1,-1)
    a=s.Matrix([1,0,0,0])
    b=s.Matrix([s.Rational(5,4),s.Rational(3,4),0,0])
    assert (a.T*G*a)[0]==(b.T*G*b)[0]==1
    assert R*a==L*a and R*b==L*b
    P=lambda n:n*n.T*G
    assert P(a)!=P(b)
    assert P(a)[0,1]==0
    assert P(b)[0,1]==-s.Rational(15,16)
