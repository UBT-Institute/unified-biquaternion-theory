"""Tests for parity-respecting entangled CAR references and emergent bosonic fluctuations."""
import sympy as s

I2=s.eye(2)
sx=s.Matrix([[0,1],[1,0]])
sy=s.Matrix([[0,-s.I],[s.I,0]])
sz=s.diag(1,-1)

def kron(*factors):
    out=s.eye(1)
    for m in factors:
        out=s.kronecker_product(out,m)
    return out

def one(M,j,N):
    return kron(*(M if k==j else I2 for k in range(N)))

def pair(p):
    return s.Matrix([s.sqrt(p),0,0,s.sqrt(1-p)])

def collective(N):
    Q=sum((one(sx,i,N) for i in range(N)),s.zeros(2**N))/s.sqrt(2*N)
    P=sum((one(sy,i,N) for i in range(N)),s.zeros(2**N))/s.sqrt(2*N)
    Z=sum((one(sz,i,N) for i in range(N)),s.zeros(2**N))/N
    return Q,P,Z

def expect(state,M):
    return s.simplify((state.conjugate().T*M*state)[0])

def test_single_cell_pure_parity_either_null_or_unpolarized():
    b,g=s.symbols('b g',complex=True)
    Codd=s.Matrix([[b*s.conjugate(b),b*s.conjugate(g)],
                   [g*s.conjugate(b),g*s.conjugate(g)]])
    assert s.simplify(Codd.det())==0
    d=s.symbols('d',real=True,nonnegative=True)
    Ceven=d*s.eye(2)
    assert s.simplify(Ceven.det()-d**2)==0
    assert s.trace(sz*Ceven)==0

def test_entangled_two_cell_reference_has_timelike_polarized_C():
    p=s.Rational(3,4)
    state=pair(p)
    assert expect(state,one(sz,0,2))==s.Rational(1,2)
    assert expect(state,one(sz,1,2))==s.Rational(1,2)
    assert expect(state,one(sx,0,2))==0
    C=s.diag(p,1-p)
    assert C.det()==s.Rational(3,16)
    assert s.trace(sz*C)==s.Rational(1,2)
    assert s.simplify(C.det()-(1-s.trace(sz*C)**2)/4)==0

def test_collective_exact_bracket_and_mean_square_bound():
    p=s.Rational(3,4)
    r=2*p-1
    for M in (1,2):
        N=2*M
        phi=kron(*([pair(p)]*M))
        Q,P,Z=collective(N)
        assert s.simplify(Q*P-P*Q-s.I*Z)==s.zeros(2**N)
        assert expect(phi,Z)==r
        discrepancy=Z/r-s.eye(2**N)
        expected=s.Rational(2,N)*(1-r*r)/(r*r)
        assert s.simplify(expect(phi,discrepancy*discrepancy)-expected)==0

def test_squeezed_minimum_uncertainty_collective_vacuum():
    p=s.Rational(3,4)
    r=2*p-1
    for M in (1,2):
        N=2*M
        state=kron(*([pair(p)]*M))
        Q,P,Z=collective(N)
        assert expect(state,Q)==expect(state,P)==0
        vq=expect(state,Q*Q)
        vp=expect(state,P*P)
        assert s.simplify(vq-(s.Rational(1,2)+s.sqrt(p*(1-p))))==0
        assert s.simplify(vp-(s.Rational(1,2)-s.sqrt(p*(1-p))))==0
        assert s.simplify(vq*vp-r*r/4)==0
        assert s.simplify(vq*vp/(r*r)-s.Rational(1,4))==0
        assert expect(state,(Q*P+P*Q)/2)==0

def test_lorentz_boost_erases_internal_spatial_polarization():
    p=s.Rational(3,4);q=1-p
    C=s.diag(p,q)
    boost=s.diag((q/p)**s.Rational(1,4),(p/q)**s.Rational(1,4))
    transformed=s.simplify(boost*C*boost.conjugate().T)
    assert s.simplify(transformed-s.sqrt(p*q)*I2)==s.zeros(2)
    assert s.simplify(boost.det()-1)==0
    assert s.simplify(boost*boost.conjugate().T-I2)!=s.zeros(2)

def test_full_su2_invariance_does_not_select_spin_axis():
    aa,bb,cc,dd=s.symbols('aa bb cc dd')
    J=s.Matrix([[aa,bb],[cc,dd]])
    constraints=[]
    for t in [sx,sy,sz]: constraints.extend(list(J*t-t*J))
    assert list(s.linsolve(constraints,[aa,bb,cc,dd]))==[(dd,0,0,dd)]

def test_even_car_pair_hamiltonian_selects_correlated_ground_state():
    p=s.Rational(3,4)
    J=2*s.sqrt(3)
    h=s.Integer(1)
    H=-J*kron(sx,sx)-h*(kron(sz,I2)+kron(I2,sz))
    target=pair(p)
    assert H*target==-4*target
    assert H.eigenvals()=={-4:1,-2*s.sqrt(3):1,2*s.sqrt(3):1,4:1}
    assert s.simplify(2*h/s.sqrt(4*h*h+J*J)-(2*p-1))==0
    gap=s.simplify((-2*s.sqrt(3))-(-4))
    assert gap.is_positive

def test_independent_even_pair_ground_state_remains_finitely_gapped():
    J=2*s.sqrt(3)
    Hp=-J*kron(sx,sx)-(kron(sz,I2)+kron(I2,sz))
    H=kron(Hp,s.eye(4))+kron(s.eye(4),Hp)
    state=kron(pair(s.Rational(3,4)),pair(s.Rational(3,4)))
    assert H*state==-8*state
    ev=H.eigenvals()
    assert ev[-8]==1
    assert sum(ev.values())==16
