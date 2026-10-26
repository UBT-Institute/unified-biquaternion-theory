import sympy as s

def test_joint_su3_u1_commutant_has_two_complex_dimensions():
    i=s.I
    generators=[]
    for a,b in [(1,2),(2,3)]:
        x=s.zeros(4);x[a,b]=x[b,a]=1
        y=s.zeros(4);y[a,b]=-i;y[b,a]=i
        generators.extend([x,y])
    generators.append(s.diag(0,1,-1,0))
    qs,qt=s.symbols('qs qt')
    generators.append(s.diag(qs,qt,qt,qt))
    h=s.symbols('h0:16')
    H=s.Matrix(4,4,h)
    eq=[z for T in generators for z in (H*T-T*H)]
    A,_=s.linear_eq_to_matrix(eq,h)
    assert len(A.nullspace())==2
    Ps=s.diag(1,0,0,0);Pt=s.diag(0,1,1,1)
    assert all(Ps*T==T*Ps and Pt*T==T*Pt for T in generators)

def test_nonzero_momentum_rotational_coupling_not_su3_invariant():
    k=s.symbols('k',real=True)
    H=s.zeros(4)
    H[0,3]=H[3,0]=k
    T=s.zeros(4);T[1,3]=T[3,1]=1
    assert H*T!=T*H
    a,b,c=s.symbols('a b c',real=True)
    Ps=s.diag(1,0,0,0);Pt=s.diag(0,1,1,1)
    assert (a*Ps+b*Pt+c*s.eye(4))==(a+c)*Ps+(b+c)*Pt
