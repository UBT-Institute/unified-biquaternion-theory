import sympy as s

def test_four_component_dirac_factorization():
    I=s.I
    sig=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
    zero=s.zeros(2)
    alpha=[s.BlockMatrix([[x,zero],[zero,-x]]).as_explicit() for x in sig]
    beta=s.BlockMatrix([[zero,s.eye(2)],[s.eye(2),zero]]).as_explicit()
    for i in range(3):
        assert alpha[i]*beta+beta*alpha[i]==s.zeros(4)
        for j in range(3):
            assert alpha[i]*alpha[j]+alpha[j]*alpha[i]==2*(i==j)*s.eye(4)
    p=s.symbols('p0:3',real=True)
    m=s.symbols('m',real=True)
    H=sum((p[i]*alpha[i] for i in range(3)),s.zeros(4))+m*beta
    assert s.simplify(H*H-(sum(v*v for v in p)+m*m)*s.eye(4))==s.zeros(4)

def test_symmetrized_flat_dirac_primary_momentum_coefficients():
    x,xb,dx,dxb=s.symbols('x xb dx dxb')
    L=s.I*s.Rational(1,2)*(xb*dx-dxb*x)
    assert s.diff(L,dx)==s.I*xb/2
    assert s.diff(L,dxb)==-s.I*x/2
