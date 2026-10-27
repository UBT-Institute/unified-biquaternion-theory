import sympy as s

def test_rotational_commutant_is_singlet_plus_triplet():
    I=s.I
    e=s.LeviCivita
    generators=[]
    for a in range(3):
        M=s.zeros(4)
        for j in range(3):
            for k in range(3):
                M[j+1,k+1]=-I*e(a,j,k)
        generators.append(M)
    coeff=s.symbols('h0:16')
    H=s.Matrix(4,4,coeff)
    equations=[]
    for J in generators:
        equations.extend(list(H*J-J*H))
    A,_=s.linear_eq_to_matrix(equations,coeff)
    null=A.nullspace()
    assert len(null)==2
    basis=[s.Matrix(4,4,list(v)) for v in null]
    expected=[s.diag(1,0,0,0),s.diag(0,1,1,1)]
    assert s.Matrix.hstack(*[s.Matrix(v).reshape(16,1) for v in basis]).rank()==2
    for E in expected:
        assert all(E*J==J*E for J in generators)
    assert all(J.conjugate().T==J for J in generators)

def test_rotations_do_not_fix_singlet_triplet_gap():
    a,b=s.symbols('a b',real=True)
    H=s.diag(a,b,b,b)
    assert H[1,1]-H[0,0]==b-a
    assert H != s.zeros(4)
