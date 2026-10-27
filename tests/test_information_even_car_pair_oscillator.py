"""Exact finite-state low-energy projection of an entangled even-CAR pair Hamiltonian."""
import sympy as s

I=s.eye(2)
X=s.Matrix([[0,1],[1,0]])
Y=s.Matrix([[0,-s.I],[s.I,0]])
Z=s.diag(1,-1)

def kron(*xs):
    a=s.eye(1)
    for x in xs:
        a=s.kronecker_product(a,x)
    return a

def pair():
    return s.Matrix([s.sqrt(3)/2,0,0,s.Rational(1,2)])

def low():
    g=pair()
    e=s.Matrix([0,1/s.sqrt(2),1/s.sqrt(2),0])
    W=s.Matrix.hstack(g,e)
    H=-2*s.sqrt(3)*kron(X,X)-(kron(Z,I)+kron(I,Z))
    Q=(kron(X,I)+kron(I,X))/2
    P=(kron(Y,I)+kron(I,Y))/2
    return W,H,Q,P

def test_ground_excited_gapped_pair_projection():
    W,H,Q,P=low()
    assert W.T.conjugate()*W==s.eye(2)
    assert W.T.conjugate()*H*W==s.diag(-4,-2*s.sqrt(3))
    assert H*W==W*s.diag(-4,-2*s.sqrt(3))

def test_projected_quadratures_and_commutator():
    W,H,Q,P=low()
    q=(s.sqrt(3)+1)/(2*s.sqrt(2))
    b=(s.sqrt(3)-1)/(2*s.sqrt(2))
    qmat=s.simplify(W.conjugate().T*Q*W)
    pmat=s.simplify(W.conjugate().T*P*W)
    assert s.simplify(qmat-q*X)==s.zeros(2)
    assert s.simplify(pmat-b*Y)==s.zeros(2)
    assert s.simplify(2*q*b-s.Rational(1,2))==0
    assert s.simplify(qmat*pmat-pmat*qmat-s.I*s.Rational(1,2)*Z)==s.zeros(2)

def test_projection_not_algebra_homomorphism():
    W,H,Q,P=low()
    comm_projection=s.simplify(W.conjugate().T*(Q*P-P*Q)*W)
    projected_comm=s.simplify(
        (W.conjugate().T*Q*W)*(W.conjugate().T*P*W)
        -(W.conjugate().T*P*W)*(W.conjugate().T*Q*W))
    assert comm_projection!=projected_comm
    assert s.simplify(comm_projection-s.I*s.diag(s.Rational(1,2),0))==s.zeros(2)
    assert s.simplify(projected_comm-s.I*s.diag(s.Rational(1,2),-s.Rational(1,2)))==s.zeros(2)

def test_two_pair_low_effective_hamiltonian_and_bosonization():
    W,H,Q,P=low()
    q=(s.sqrt(3)+1)/(2*s.sqrt(2))
    b=(s.sqrt(3)-1)/(2*s.sqrt(2))
    M=2
    Qlow=sum((kron(X,I) if j==0 else kron(I,X) for j in range(M)),s.zeros(4))*q/s.sqrt(M)
    Plow=sum((kron(Y,I) if j==0 else kron(I,Y) for j in range(M)),s.zeros(4))*b/s.sqrt(M)
    K=(M*s.eye(4)-(kron(Z,I)+kron(I,Z)))/2
    r=s.Rational(1,2)
    assert s.simplify((Qlow*Plow-Plow*Qlow)/r-s.I*(s.eye(4)-2*K/M))==s.zeros(4)
    w=4-2*s.sqrt(3)
    Heff=w*K
    assert Heff.eigenvals()=={0:1,w:2,2*w:1}
    A=(Qlow/q+s.I*Plow/b)/2
    assert s.simplify(Heff*A-A*Heff+w*A)==s.zeros(4)

def test_low_occupation_ccr_error_scales_inverse_number_of_pairs():
    q=(s.sqrt(3)+1)/(2*s.sqrt(2))
    b=(s.sqrt(3)-1)/(2*s.sqrt(2))
    r=s.Rational(1,2)
    for M in (1,2,3):
        xx=sum((kron(*[X if j==k else I for j in range(M)])
                for k in range(M)),s.zeros(2**M))
        yy=sum((kron(*[Y if j==k else I for j in range(M)])
                for k in range(M)),s.zeros(2**M))
        zz=sum((kron(*[Z if j==k else I for j in range(M)])
                for k in range(M)),s.zeros(2**M))
        Q=q*xx/s.sqrt(M)
        P=b*yy/s.sqrt(M)
        K=(M*s.eye(2**M)-zz)/2
        bracket=s.simplify((Q*P-P*Q)/(s.I*r))
        assert s.simplify(bracket-(s.eye(2**M)-2*K/M))==s.zeros(2**M)
        for k in range(M+1):
            basis=s.zeros(2**M,1)
            basis[2**k-1]=1
            deviation=(bracket-s.eye(2**M))*basis
            assert s.simplify(deviation+2*s.Rational(k,M)*basis)==s.zeros(2**M,1)
