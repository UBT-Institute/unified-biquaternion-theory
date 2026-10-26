import sympy as s

def test_su3_fundamental_commutant_of_1_plus_3():
    # Three diagonal/offdiagonal fundamental SU(3) generators suffice
    i=s.I
    mats=[]
    for a,b in [(0,1),(1,2)]:
        x=s.zeros(3);x[a,b]=x[b,a]=1
        y=s.zeros(3);y[a,b]=-i;y[b,a]=i
        mats.extend([x,y])
    z=s.diag(1,-1,0)
    mats.append(z)
    gens=[s.diag(0,0,0,0) for _ in mats]
    for k,m in enumerate(mats):
        gens[k][1:4,1:4]=m
    vars=s.symbols('h0:16')
    H=s.Matrix(4,4,vars)
    eq=[v for T in gens for v in list(H*T-T*H)]
    A,_=s.linear_eq_to_matrix(eq,vars)
    assert len(A.nullspace())==2
    assert all((s.diag(1,0,0,0)*T-T*s.diag(1,0,0,0))==s.zeros(4) for T in gens)
    assert all((s.diag(0,1,1,1)*T-T*s.diag(0,1,1,1))==s.zeros(4) for T in gens)

def test_su3_rules_out_spatial_momentum_polarization_splitting_at_fixed_k():
    k=s.symbols('k',real=True)
    T=s.zeros(4);T[1,2]=T[2,1]=1
    H=s.diag(0,0,0,k*k)
    assert H*T==T*H  # this particular generator does not mix index 3
    T2=s.zeros(4);T2[2,3]=T2[3,2]=1
    assert H*T2!=T2*H
