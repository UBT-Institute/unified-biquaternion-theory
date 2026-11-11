"""Full-rank composite split-jet tetrad with conditional positive TT sector."""
import sympy as sp


ETA = sp.diag(-1, 1, 1, 1)
X = sp.Matrix([1, 0, 0, 0])


def make_jets(E, omega=None):
    """Exact algebraic right inverse at constant non-null X=e0, s=1."""
    if omega is None:
        omega = [sp.zeros(4) for _ in range(4)]
    kjets = []
    dilations = []
    for mu in range(4):
        target = E.row(mu).T - omega[mu] * X
        w = sp.expand(target[0])
        K = sp.zeros(4)
        for j in range(1, 4):
            K[j, 0] = sp.expand(target[j])
            K[0, j] = sp.expand(target[j])
        kjets.append(K)
        dilations.append(w)
    return kjets, dilations


def composite_tetrad(kjets, dilations, omega=None):
    if omega is None:
        omega = [sp.zeros(4) for _ in range(4)]
    return sp.Matrix.vstack(*[(omega[mu]*X+kjets[mu]*X+dilations[mu]*X).T
                               for mu in range(4)])


def test_exact_flat_full_rank_and_lorentz_jets():
    E = sp.eye(4)
    K, w = make_jets(E)
    assert w == [1, 0, 0, 0]
    for j in range(1,4):
        assert K[j][j,0] == K[j][0,j] == 1
    for J in K:
        assert sp.simplify(J.T*ETA+ETA*J)==sp.zeros(4)
    assert composite_tetrad(K,w)==E
    assert E.det()==1
    assert (E*ETA*E.T)==ETA


def test_full_rank_TT_lift_and_exact_determinant():
    p,q=sp.symbols("p q",real=True)
    E=sp.eye(4)
    E[1,1]+=p/2
    E[2,2]-=p/2
    E[1,2]=q/2
    E[2,1]=q/2
    K,w=make_jets(E)
    assert composite_tetrad(K,w)==E
    det=sp.factor(E.det())
    assert sp.expand(det-(1-(p*p+q*q)/4))==0
    h=sp.Matrix([[p,q,0],[q,-p,0],[0,0,0]])
    assert sp.trace(h)==0
    assert h[2,0]==h[2,1]==h[2,2]==0
    delta_metric=E*ETA*E.T-ETA
    assert sp.simplify(delta_metric[1,1]-p-p*p/4-q*q/4)==0
    assert sp.simplify(delta_metric[2,2]+p-p*p/4-q*q/4)==0
    assert sp.simplify(delta_metric[1,2]-q)==0
    assert det.subs({p:sp.Rational(1,4),q:sp.Rational(1,3)})>0


def test_arbitrary_physical_connection_can_be_compensated():
    E=sp.eye(4)
    a,b=sp.symbols("a b",real=True)
    O=sp.zeros(4)
    O[1,0]=O[0,1]=a
    O[2,0]=O[0,2]=b
    assert O.T*ETA+ETA*O==sp.zeros(4)
    omega=[sp.zeros(4),O,sp.zeros(4),sp.zeros(4)]
    K,w=make_jets(E,omega)
    assert composite_tetrad(K,w,omega)==E
    for J in K:
        assert sp.simplify(J.T*ETA+ETA*J)==sp.zeros(4)


def test_TT_positive_wave_hamiltonian_and_dispersion():
    M2,k2,p,q,vp,vq=sp.symbols("M2 k2 p q vp vq",positive=True)
    tt= M2/4*(vp*vp+vq*vq+k2*(p*p+q*q))
    assert sp.simplify(tt.subs({vp:0,vq:0,p:0,q:0}))==0
    assert tt.subs({M2:4,k2:9,p:2,q:1,vp:3,vq:4})==70
    # Canonical quadratic L=M²/4 sum((dot h)^2-k² h²)
    u=sp.symbols("u",real=True)
    vd=sp.symbols("vd",real=True)
    L=M2/4*(vd*vd-k2*u*u)
    momentum=sp.diff(L,vd)
    H=sp.expand((momentum*vd-L).subs(vd,2*sp.Symbol("mom")/M2))
    mom=sp.Symbol("mom",real=True)
    assert sp.simplify(H-(mom*mom/M2+M2*k2*u*u/4))==0
    assert sp.simplify(sp.diff(L,u)/(-M2/2)-k2*u)==0
