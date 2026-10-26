import sympy as s

def test_so2_trial_euler_and_auxiliary_limit():
    t,x=s.symbols("t x",real=True)
    a,b=s.symbols("a b",real=True,nonzero=True)
    A0=s.Function("A0")(t,x)
    A1=s.Function("A1")(t,x)
    B0,B1,j0,j1=s.symbols("B0 B1 j0 j1")
    F=s.diff(A1,t)-s.diff(A0,x)
    # 1+1 Minkowski: F_{01}=F, F^{01}=-F;
    # L = +a/2 F² + b/2(-[A0-B0]²+[A1-B1]²)+(-A0*j0+A1*j1)
    L=a*F**2/s.Integer(2)+b*(-(A0-B0)**2+(A1-B1)**2)/2-A0*j0+A1*j1
    E0=s.diff(L,A0)-s.diff(s.diff(L,s.diff(A0,x)),x)
    E1=s.diff(L,A1)-s.diff(s.diff(L,s.diff(A1,t)),t)
    assert s.simplify(E0 + b*(A0-B0)+j0-a*s.diff(F,x))==0
    assert s.simplify(E1 - b*(A1-B1)-j1+a*s.diff(F,t))==0
    solution=s.solve([E0.subs(a,0),E1.subs(a,0)],[A0,A1])
    expected={A0:B0-j0/b,A1:B1-j1/b}
    assert solution.keys()==expected.keys()
    assert all(s.simplify(solution[field]-value)==0 for field,value in expected.items())
