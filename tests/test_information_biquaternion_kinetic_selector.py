import sympy as s

def test_two_parameter_kinetic_and_metric_lock():
    a,b,h,N=s.symbols('a b h N',positive=True,real=True)
    G=s.diag(1,-1,-1,-1)
    n=s.Matrix([1,0,0,0])
    K=-b*G+(a+b)*(G*n)*(n.T*G)
    assert K==s.diag(a,b,b,b)
    c2=s.symbols('c2',real=True)
    # -b <DTheta,DTheta> contraction = 4 b N; radial term is (a+b)c²/h.
    assert s.simplify((4*b*N+(a+b)*c2/h).subs({a:1,b:1})-(4*N+2*c2/h))==0

def test_su3_symmetry_does_not_select_radial_transverse_ratio():
    a,b=s.symbols('a b',positive=True)
    K=s.diag(a,b,b,b)
    T=s.zeros(4)
    T[1,2]=1
    T[2,1]=1
    assert K*T==T*K
    assert K.subs({a:2,b:1})!=K.subs({a:1,b:1})
