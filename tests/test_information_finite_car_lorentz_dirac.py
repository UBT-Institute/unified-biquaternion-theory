"""Finite CAR geometry and regulated Dirac benchmark, no Grassmann generators."""
import sympy as s

I=s.eye(2)
sig=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
e1,e2=-s.I*sig[0],-s.I*sig[1]
a=(e1+s.I*e2)/2
ad=a.conjugate().T
parity=I-2*ad*a

def tens(matrices):
    r=s.eye(1)
    for m in matrices:
        r=s.kronecker_product(r,m)
    return r

def modes(n):
    return [tens([parity if k<j else a if k==j else I for k in range(n)]) for j in range(n)]

def bilinear(ops,m):
    z=s.zeros(ops[0].rows)
    for j in range(len(ops)):
        for k in range(len(ops)):
            z+=m[j,k]*ops[j].conjugate().T*ops[k]
    return z

def test_two_mode_even_lorentz_vector():
    c=modes(2)
    sig4=[I]+sig
    B=[bilinear(c,sigx) for sigx in sig4]
    assert all(b==b.conjugate().T for b in B)
    assert s.Matrix.hstack(*[b.reshape(16,1) for b in B]).rank()==4
    states=[s.Matrix([0,0,1,0]),s.Matrix([0,1,0,0])]
    W=s.Matrix.hstack(*states)
    for j,m in enumerate(sig4):
        assert W.conjugate().T*B[j]*W==m
    eta=s.Matrix(4,4,lambda i,j:s.trace(sig4[i]*(sig4[j] if j==0 else -sig4[j]))/2)
    assert eta==s.diag(1,-1,-1,-1)
    x=s.symbols('x0:4',real=True)
    M=sum((x[j]*sig4[j] for j in range(4)),s.zeros(2))
    assert s.expand(M.det()-(x[0]**2-sum(t*t for t in x[1:])))==0

def test_su2_lie_bilinears():
    c=modes(2)
    bx,by,bz=[bilinear(c,ss) for ss in sig]
    assert bx*by-by*bx==2*s.I*bz
    assert by*bz-bz*by==2*s.I*bx
    assert bz*bx-bx*bz==2*s.I*by

def test_nonunitary_boost_fails_naive_car():
    t=s.symbols('t',real=True)
    S=s.diag(s.exp(t/2),s.exp(-t/2))
    assert s.simplify(S*S.conjugate().T-I)!=s.zeros(2)
    assert s.simplify(S*S.conjugate().T-s.diag(s.exp(t),s.exp(-t)))==s.zeros(2)

def test_four_mode_dirac_fock_positive_excitation():
    c=modes(4)
    alphas=[s.kronecker_product(s.diag(-1,1),m) for m in sig]
    zz=s.zeros(2)
    beta=s.BlockMatrix([[zz,I],[I,zz]]).as_explicit()
    h=3*alphas[2]+4*beta
    assert h*h==25*s.eye(4)
    H=bilinear(c,h)
    assert H==H.conjugate().T
    assert H.eigenvals()=={-10:1,-5:4,0:6,5:4,10:1}
    pos=H+10*s.eye(16)
    assert pos.eigenvals()=={0:1,5:4,10:6,15:4,20:1}

def test_two_mode_canonical_car():
    c=modes(2)
    for i in range(2):
        for j in range(2):
            assert c[i]*c[j]+c[j]*c[i]==s.zeros(4)
            assert c[i]*c[j].conjugate().T+c[j].conjugate().T*c[i]==(s.eye(4) if i==j else s.zeros(4))
