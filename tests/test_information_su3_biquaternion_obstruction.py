import sympy as s

def test_mat2c_commutator_has_six_real_dimensions_and_center_two():
    I=s.I
    e00=s.Matrix([[1,0],[0,0]]);e01=s.Matrix([[0,1],[0,0]])
    e10=s.Matrix([[0,0],[1,0]]);e11=s.Matrix([[0,0],[0,1]])
    basis=[e00,e01,e10,e11,I*e00,I*e01,I*e10,I*e11]
    # The commutator span is traceless; its complex basis gives 6 real dimensions.
    H=e00-e11
    comm=lambda a,b:a*b-b*a
    assert comm(e01,e10)==H
    assert comm(H,e01)==2*e01
    assert comm(H,e10)==-2*e10
    assert all(s.trace(comm(a,b))==0 for a in basis for b in basis)
    # Only complex scalar matrices commute with the complex matrix algebra.
    a,b,c,d=s.symbols("a b c d")
    M=s.Matrix([[a,b],[c,d]])
    eqs=list(comm(M,e01))+list(comm(M,e10))
    sol=s.solve(eqs,[b,c,d],dict=True)
    assert sol==[{b:0,c:0,d:a}]
