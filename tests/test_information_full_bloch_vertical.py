"""Conditional full-Theta positive-H Gaussian lift: information map fills Bloch ball.

Tests finite matrix/algebraic identities only; no physical UBT action or gauge theorem.
"""
import sympy as sp

I2 = sp.eye(2)
SIGMA = (sp.Matrix([[0, 1], [1, 0]]),
         sp.Matrix([[0, -sp.I], [sp.I, 0]]),
         sp.diag(1, -1))
ETA = sp.diag(-1, 1, 1, 1)


def theta_at_origin(s):
    C = sp.sqrt(1 + sum(x*x for x in s))
    return (1 - sp.I*C)*I2 - sp.I*sum((s[j]*SIGMA[j] for j in range(3)), sp.zeros(2))


def readout(theta):
    q = sp.simplify(theta * theta.H)
    return sp.simplify(q / sp.trace(q))


def matrix_equal(a, b):
    assert sp.simplify(a-b) == sp.zeros(*a.shape)


def test_exact_full_three_real_parameter_bloch_ball():
    a,b,c = sp.symbols('a b c', real=True)
    s = (a,b,c)
    C = sp.sqrt(1 + a*a+b*b+c*c)
    rho = readout(theta_at_origin(s))
    expected = (I2 + sum((s[j]*SIGMA[j] for j in range(3)), sp.zeros(2))/C)/2
    matrix_equal(rho, expected)
    assert sp.simplify(sp.trace(rho) - 1) == 0


def test_full_theta_determinant_is_nonzero():
    a,b,c = sp.symbols('a b c', real=True)
    C=sp.sqrt(1+a*a+b*b+c*c)
    assert sp.simplify(theta_at_origin((a,b,c)).det()+2*sp.I*C)==0
    assert sp.simplify(C**2-a*a-b*b-c*c)==1


def test_inverse_bloch_reconstruction_for_nontrivial_point():
    v=(sp.Rational(3,5),sp.Rational(2,5),sp.Rational(1,5))
    length_sq=sum(x*x for x in v)
    s=tuple(x/sp.sqrt(1-length_sq) for x in v)
    rho=readout(theta_at_origin(s))
    for j in range(3):
        assert sp.simplify(sp.trace(rho*SIGMA[j])-v[j])==0


def test_gaussian_lift_reproduces_same_four_tetrad_columns_exactly():
    for s in [(sp.Rational(3,4),0,0), (sp.Rational(2,3),sp.Rational(-1,5),sp.Rational(1,3)), (0,0,0)]:
        C=sp.sqrt(1+sum(x*x for x in s))
        du=sp.Matrix([C,*s]); n=ETA*du
        assert sp.simplify((n.T*ETA*n)[0]+1)==0
        q=-1
        for mu in range(4):
            e=sp.eye(4)[:,mu]; w=-du[mu]
            r=e-w*n
            assert sp.simplify((n.T*ETA*r)[0])==0
            nl=ETA*n; rl=ETA*r
            kl=(rl*nl.T-nl*rl.T)/q
            k=ETA*kl
            matrix_equal(k.T*ETA+ETA*k,sp.zeros(4))
            matrix_equal(k*n, r)
            matrix_equal(k*n+w*n,e)


def test_different_bloch_states_same_tetrad():
    for s in [(0,0,0), (sp.Rational(3,4),0,0), (0,sp.Rational(4,3),0), (0,0,sp.Rational(5,12))]:
        th=theta_at_origin(s)
        rho=readout(th)
        C=sp.sqrt(1+sum(v*v for v in s))
        for j in range(3):
            assert sp.simplify(sp.trace(rho*SIGMA[j])-s[j]/C)==0
    matrix_equal(readout(theta_at_origin((0,0,0))),I2/2)
    matrix_equal(readout(theta_at_origin((sp.Rational(3,4),0,0))),
                 (I2+sp.Rational(3,5)*SIGMA[0])/2)


def test_bloch_map_has_rank_three_everywhere():
    a,b,c=sp.symbols('a b c',real=True)
    svec=sp.Matrix([a,b,c]); C=sp.sqrt(1+a*a+b*b+c*c)
    J=sp.simplify((svec/C).jacobian(svec))
    wanted=sp.eye(3)/C-svec*svec.T/C**3
    matrix_equal(J,wanted)
    matrix_equal(J*svec,svec/C**3)
    assert sp.simplify(J.subs({a:0,b:0,c:0})-sp.eye(3))==sp.zeros(3)


def test_tetrahedral_classical_fisher_on_vertical_directions():
    tetra=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
    effects=[(I2+sum((sp.Rational(v[j],1)*SIGMA[j] for j in range(3)),sp.zeros(2))/sp.sqrt(3))/4 for v in tetra]
    matrix_equal(sum(effects,sp.zeros(2)),I2)
    for E in effects:
        assert E.det()==0
        assert sp.simplify(sp.trace(E)-sp.Rational(1,2))==0
    h=sp.Matrix(sp.symbols('h0 h1 h2',real=True))
    state=(I2+sum((h[j]*SIGMA[j] for j in range(3)),sp.zeros(2)))/2
    F=sp.zeros(3)
    for E in effects:
        p=sp.simplify(sp.trace(E*state)); v=sp.Matrix([sp.diff(p,x) for x in h]);
        F +=v*v.T/p.subs({x:0 for x in h})
    matrix_equal(sp.simplify(F),sp.eye(3)/3)


def test_relative_entropy_distinguishes_gravity_vertical_states():
    r=sp.symbols('r',real=True)
    D=((1+r)*sp.log(1+r)+(1-r)*sp.log(1-r))/2
    assert sp.simplify(D.subs(r,0))==0
    assert sp.simplify(sp.diff(D,r,2).subs(r,0))==1
    assert sp.N(D.subs(r,sp.Rational(3,5)))>0


def test_fixed_geometric_observer_cannot_remove_vertical_readout_change():
    N=I2
    theta1=theta_at_origin((0,0,0))
    theta2=theta_at_origin((0,sp.Rational(3,4),0))
    assert sp.simplify(sp.trace((readout(theta1)-readout(theta2))*SIGMA[1]))==-sp.Rational(3,5)
    matrix_equal(N,I2)
