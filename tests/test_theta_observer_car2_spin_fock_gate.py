"""Exact conditional spin, CAR and observer projective bridge.

No UBT microscopic action or physical electron/photon is established.
"""
import sympy as s

I=s.I
ID=s.eye(2)
sx=s.Matrix([[0,1],[1,0]])
sy=s.Matrix([[0,-I],[I,0]])
sz=s.diag(1,-1)
ann=s.Matrix([[0,1],[0,0]])
cre=ann.H
Z=sz


def same(a,b):
    return (a-b).applyfunc(lambda v:s.trigsimp(s.expand(v),method="fu"))==s.zeros(*a.shape)


def comm(a,b):
    return a*b-b*a


def anticom(a,b):
    return a*b+b*a


def modes():
    return (s.kronecker_product(ann,ID),s.kronecker_product(Z,ann))


def spin_j():
    cs=modes()
    return [s.simplify(sum((sig[a,b]*cs[a].H*cs[b]/2 for a in range(2) for b in range(2)),s.zeros(4))) for sig in (sx,sy,sz)]


def test_observer_spectral_projector_nonzero_gap():
    theta,r=s.symbols('theta r',real=True)
    n=s.sin(theta)*sx+s.cos(theta)*sz
    rho=(ID+r*n)/2
    Pplus=(ID+n)/2
    Pminus=(ID-n)/2
    assert same(n*n,ID)
    for P in [Pplus,Pminus]:
        assert same(P*P,P)
        assert s.trigsimp(s.trace(P))==1
    assert same(rho,((1+r)*Pplus+(1-r)*Pminus)/2)
    assert same(rho.subs(r,0),ID/2)
    assert same((Pplus-Pminus).subs(theta,0),sz)


def test_single_projector_car_is_adjoint_even_not_spinor():
    theta,phi=s.symbols('theta phi',real=True)
    plus=s.Matrix([s.cos(theta/2),s.exp(I*phi)*s.sin(theta/2)])
    minus=s.Matrix([-s.exp(-I*phi)*s.sin(theta/2),s.cos(theta/2)])
    assert same(plus.H*plus,s.ones(1,1))
    assert same(minus.H*minus,s.ones(1,1))
    assert same(plus.H*minus,s.zeros(1,1))
    c=minus*plus.H
    assert same(c*c,s.zeros(2))
    assert same(anticom(c,c.H),ID)
    assert same(c.H*c,plus*plus.H)
    assert same(c*c.H,minus*minus.H)
    minus_center=-ID
    assert same(minus_center*c*minus_center.H,c)
    assert same(minus_center*plus,-plus)


def test_eigenlines_have_chern_plus_minus_one_car_operator_has_minus_two():
    theta,phi=s.symbols('theta phi',real=True)
    plus=s.Matrix([s.cos(theta/2),s.exp(I*phi)*s.sin(theta/2)])
    minus=s.Matrix([-s.exp(-I*phi)*s.sin(theta/2),s.cos(theta/2)])
    def Berry(v):
        return [s.trigsimp(-I*(v.H*v.diff(q))[0]) for q in (theta,phi)]
    ap=Berry(plus)
    am=Berry(minus)
    fp=s.trigsimp(s.diff(ap[1],theta)-s.diff(ap[0],phi))
    fm=s.trigsimp(s.diff(am[1],theta)-s.diff(am[0],phi))
    assert s.trigsimp(fp-s.sin(theta)/2)==0
    assert s.trigsimp(fm+s.sin(theta)/2)==0
    assert s.trigsimp((fm-fp)+s.sin(theta))==0
    assert s.integrate(fp,(theta,0,s.pi),(phi,0,2*s.pi))/(2*s.pi)==1
    assert s.integrate(fm,(theta,0,s.pi),(phi,0,2*s.pi))/(2*s.pi)==-1
    assert s.integrate(fm-fp,(theta,0,s.pi),(phi,0,2*s.pi))/(2*s.pi)==-2


def test_two_mode_jordan_wigner_car_exact():
    cs=modes()
    for a in range(2):
        for b in range(2):
            assert same(anticom(cs[a],cs[b]),s.zeros(4))
            assert same(anticom(cs[a],cs[b].H),s.eye(4) if a==b else s.zeros(4))


def test_rotations_act_on_one_particle_spinor_and_keep_vacuum_scalar():
    cs=modes()
    Jx,Jy,Jz=spin_j()
    assert same(comm(Jx,Jy),I*Jz)
    assert same(comm(Jy,Jz),I*Jx)
    assert same(comm(Jz,Jx),I*Jy)
    vacuum=s.Matrix([1,0,0,0]);pair=s.Matrix([0,0,0,1])
    for J in (Jx,Jy,Jz):
        assert J*vacuum==s.zeros(4,1)
        assert J*pair==s.zeros(4,1)
    assert Jz==s.diag(0,-s.Rational(1,2),s.Rational(1,2),0)
    assert comm(Jz,cs[0].H)==cs[0].H/2
    assert comm(Jz,cs[1].H)==-cs[1].H/2


def test_2pi_spin_rotation_is_fermion_parity_not_scalar_minus_identity():
    cs=modes()
    Jz=spin_j()[2]
    U2pi=s.diag(*[s.simplify(s.exp(2*s.pi*I*Jz[j,j])) for j in range(4)])
    P=s.kronecker_product(sz,sz)
    assert U2pi==P
    assert U2pi!= -s.eye(4)
    for c in cs:
        assert same(P*c*P,-c)
    assert same(P*P,s.eye(4))


def test_vector_charge_u1_commutes_spin_and_rephases_both_modes_equally():
    alpha=s.symbols('alpha',real=True)
    cs=modes()
    N=sum((c.H*c for c in cs),s.zeros(4))
    Js=spin_j()
    for J in Js:
        assert same(comm(N,J),s.zeros(4))
    Uq=s.diag(*[s.exp(I*alpha*N[i,i]) for i in range(4)])
    for c in cs:
        assert same(Uq*c*Uq.H,s.exp(-I*alpha)*c)


def test_one_mode_odd_space_cannot_contain_su2_spin_doublet():
    n=cre*ann
    odd=n
    even=ID-n
    assert s.trace(odd)==1
    assert s.trace(even)==1
    # Spin-1/2 irreducible rotation module needs a 2D odd subspace.
    cs=modes()
    N=sum((c.H*c for c in cs),s.zeros(4))
    odd2=(s.eye(4)-s.kronecker_product(sz,sz))/2
    assert s.trace(odd2)==2
    assert same(odd2*odd2,odd2)


def test_spin_and_charge_do_not_select_unique_positive_hamiltonian():
    omega, interaction=s.symbols('omega interaction', positive=True)
    cs=modes()
    n1,n2=(c.H*c for c in cs)
    N=n1+n2
    h_free=omega*N
    h_int=h_free+interaction*n1*n2
    for J in spin_j():
        assert same(comm(h_free,J),s.zeros(4))
        assert same(comm(h_int,J),s.zeros(4))
    assert same(comm(h_free,N),s.zeros(4))
    assert same(comm(h_int,N),s.zeros(4))
    assert list(h_free.diagonal())==[0,omega,omega,2*omega]
    assert list(h_int.diagonal())==[0,omega,omega,2*omega+interaction]
    assert h_free!=h_int
