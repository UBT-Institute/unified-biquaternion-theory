import sympy as s

def test_only_zero_vector_fixed_by_spatial_rotations_and_boost():
    v=s.Matrix(s.symbols("v0:4"))
    generators=[]
    for i,j in [(1,2),(2,3),(3,1)]:
        M=s.zeros(4)
        M[i,j]=1
        M[j,i]=-1
        generators.append(M)
    boost=s.zeros(4)
    boost[0,1]=1
    boost[1,0]=1
    generators.append(boost)
    equations=sum((list(g*v) for g in generators),[])
    assert s.solve(equations,list(v))==dict(zip(list(v),[0]*4))

def test_timelike_projector_breaks_boost_invariance():
    G=s.diag(1,-1,-1,-1)
    n=s.Matrix([1,0,0,0])
    B=s.eye(4)
    # Exact boost with cosh = 5/4, sinh = 3/4
    B[0,0]=s.Rational(5,4);B[1,1]=s.Rational(5,4)
    B[0,1]=s.Rational(3,4);B[1,0]=s.Rational(3,4)
    assert B.T*G*B==G
    P=lambda x:x*x.T*G
    assert P(B*n)!=P(n)
