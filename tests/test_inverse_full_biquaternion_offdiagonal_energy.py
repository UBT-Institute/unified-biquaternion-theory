"""General complex 2x2 biquaternion matrix: off-diagonal norms and caveats."""
import sympy as sp

def adj2(X):
    return sp.Matrix([[X[1,1],-X[0,1]],[-X[1,0],X[0,0]]])

def hermitian_size(X):
    return sp.expand(sp.trace(X.conjugate().T*X))

def adjugate_hermitian_pair(X):
    return sp.expand(sp.trace(adj2(X)*X.conjugate().T))

def test_all_complex_offdiagonal_terms():
    a,b,c,d=[sp.Symbol(x,complex=True) for x in "abcd"]
    X=sp.Matrix([[a,b],[c,d]])
    assert sp.simplify(hermitian_size(X)-
        (a*sp.conjugate(a)+b*sp.conjugate(b)+c*sp.conjugate(c)+d*sp.conjugate(d)))==0
    target=2*sp.re(a*sp.conjugate(d)-b*sp.conjugate(c))
    assert sp.simplify(sp.expand_complex(adjugate_hermitian_pair(X)-target))==0

def test_negative_is_from_full_offdiagonal_coupling():
    X=sp.Matrix([[1,2],[2,1]])
    assert hermitian_size(X)==10
    assert adjugate_hermitian_pair(X)==-6

def test_nondiagonal_shear_alters_hs_not_determinant():
    X=sp.eye(2)
    A=sp.Matrix([[1,2],[0,1]])
    X2=A*X*A.conjugate().T
    assert X2.det()==X.det()==1
    assert hermitian_size(X2)==34
    assert hermitian_size(X)==2
    # For Hermitian matrices the adjugate pairing equals twice determinant.
    assert adjugate_hermitian_pair(X2)==adjugate_hermitian_pair(X)==2

def test_determinant_magnitude_is_semidefinite_not_norm():
    X=sp.Matrix([[1,1],[1,1]])
    assert X != sp.zeros(2)
    assert X.det()==0
    assert hermitian_size(X)==4
    assert abs(X.det())**2==0
