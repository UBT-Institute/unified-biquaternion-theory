"""Verified algebraic regression gates for the conditional UBT Dirac benchmark."""
import sympy as sp

def extmul(a, b):
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            if ma & mb:
                continue
            swaps = sum(1 for i in range(4) if ma & (1<<i)
                        for j in range(i) if mb & (1<<j))
            key = ma | mb
            out[key] = sp.expand(out.get(key, 0) + (-1 if swaps%2 else 1)*ca*cb)
    return {k:v for k,v in out.items() if v!=0}

def extadd(*items):
    out={}
    for item in items:
        for k,v in item.items():
            out[k]=sp.expand(out.get(k,0)+v)
    return {k:v for k,v in out.items() if v!=0}

def extneg(a):
    return {k:-v for k,v in a.items()}

def test_graded_mass_is_antisymmetric_weyl_pairing_not_naive_det():
    u0,u1,v0,v1=({1<<i:sp.Integer(1)} for i in range(4))
    B=extadd(extmul(u0,v1),extneg(extmul(u1,v0)))
    RdL=extadd(extmul(v1,u0),extneg(extmul(v0,u1)))
    assert extadd(B,RdL)=={}
    naive=extadd(extmul(u0,v1),extneg(extmul(v0,u1)))
    assert naive!=B
    t=sp.symbols('t')
    u0p=extadd(u0,{2:t})
    v0p=extadd(v0,{8:t})
    Bp=extadd(extmul(u0p,v1),extneg(extmul(u1,v0p)))
    naivep=extadd(extmul(u0p,v1),extneg(extmul(v0p,u1)))
    assert Bp==B
    assert extadd(naivep,extneg(naive))=={10:2*t}

def test_SL2_singlet_identity():
    a,b,c=sp.symbols('a b c',nonzero=True)
    S=sp.Matrix([[a,b],[c,(1+b*c)/a]])
    eps=sp.Matrix([[0,1],[-1,0]])
    assert sp.simplify(S.T*eps*S-eps)==sp.zeros(2)

def test_dirac_mass_shell_operator():
    sx=sp.Matrix([[0,1],[1,0]])
    sy=sp.Matrix([[0,-sp.I],[sp.I,0]])
    sz=sp.diag(1,-1)
    alpha=[sp.kronecker_product(sp.diag(-1,1),sig) for sig in (sx,sy,sz)]
    z=sp.zeros(2)
    beta=sp.BlockMatrix([[z,sp.eye(2)],[sp.eye(2),z]]).as_explicit()
    p=sp.symbols('p1:4',real=True)
    m=sp.symbols('m',real=True)
    H=sum((p[i]*alpha[i] for i in range(3)),sp.zeros(4))+m*beta
    assert sp.simplify(H*H-(sum(x*x for x in p)+m*m)*sp.eye(4))==sp.zeros(4)

def test_pure_odd_tetrad_metric_obstruction():
    e0={1:sp.Integer(1)}
    e1={2:sp.Integer(1)}
    assert extadd(extmul(e0,e1),extmul(e1,e0))=={}
    assert extmul(e0,e0)=={}
    assert extmul(e1,e1)=={}
