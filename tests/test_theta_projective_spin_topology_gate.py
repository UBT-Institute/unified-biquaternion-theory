"""Exact scoped PGL(2,C), polar observer quotient, and Z2 spin-cover checks.

These are kinematic comparison identities, not an emergent QED/GR action.
"""
import sympy as s

I=s.I
ID=s.eye(2)
s1=s.Matrix([[0,1],[1,0]])
s2=s.Matrix([[0,-I],[I,0]])
s3=s.diag(1,-1)


def zero(A):
    return A.applyfunc(s.simplify)==s.zeros(*A.shape)


def test_polar_factorization_gives_positive_observer_and_right_unitary_fiber():
    theta=s.Matrix([[2,1+I],[0,1]])
    K=theta*theta.H
    t=s.symbols('t',real=True)
    U=s.diag(s.exp(I*t),s.exp(-I*t))
    assert zero((theta*U)*(theta*U).H-K)
    assert zero(K/s.trace(K)-(theta*U)*(theta*U).H/s.trace((theta*U)*(theta*U).H))
    assert all(K[i,i]>0 for i in range(2))
    assert s.det(K)==abs(s.det(theta))**2


def test_projective_center_removes_two_real_parameters_not_three_or_six():
    lam=s.symbols('lam',positive=True, real=True)
    phi=s.symbols('phi',real=True)
    theta=s.Matrix([[2,1],[0,1+I]])
    c=lam*s.exp(I*phi)
    rho=theta*theta.H/s.trace(theta*theta.H)
    rho2=(c*theta)*(c*theta).H/s.trace((c*theta)*(c*theta).H)
    assert zero(rho-rho2)
    assert s.simplify(s.det(c*theta)-c*c*s.det(theta))==0
    assert s.det(theta)!=0


def test_observer_density_differential_rank_three_from_eight_real_components():
    a=s.symbols('a0:4',real=True)
    b=s.symbols('b0:4',real=True)
    eps=s.symbols('eps',real=True)
    P=ID+eps*sum(((a[k]+I*b[k])*M for k,M in enumerate((ID,s1,s2,s3))),s.zeros(2))
    Q=P*P.H
    rho=Q/s.trace(Q)
    first=rho.diff(eps).subs(eps,0).applyfunc(s.simplify)
    assert zero(first-(a[1]*s1+a[2]*s2+a[3]*s3))
    dr=s.Matrix([s.trace(M*first) for M in (s1,s2,s3)])
    assert dr.jacobian(a+b).rank()==3


def test_pgl_projective_loop_lifts_to_minus_identity_in_sl2():
    phi=s.symbols('phi',real=True)
    theta=s.diag(s.exp(I*phi),1)
    spin=s.diag(s.exp(I*phi/2),s.exp(-I*phi/2))
    assert s.simplify(spin.det())==1
    assert zero(spin-s.exp(-I*phi/2)*theta)
    assert spin.subs(phi,0)==ID
    assert spin.subs(phi,2*s.pi)==-ID
    assert theta.subs(phi,0)==theta.subs(phi,2*s.pi)==ID


def test_determinant_phase_connection_is_flat_but_has_z2_holonomy():
    phi=s.symbols('phi',real=True)
    theta=s.diag(s.exp(I*phi),1)
    a=s.simplify(s.im(s.trace(theta.inv()*theta.diff(phi)))/2)
    assert a==s.Rational(1,2)
    integral=s.integrate(a,(phi,0,2*s.pi))
    assert integral==s.pi
    assert s.simplify(s.exp(I*integral))==-1
    x,y=s.symbols('x y',real=True)
    M=s.diag(s.exp(I*x),s.exp(I*y))
    ax=s.simplify(s.im(s.trace(M.inv()*M.diff(x)))/2)
    ay=s.simplify(s.im(s.trace(M.inv()*M.diff(y)))/2)
    assert ax==ay==s.Rational(1,2)
    assert s.simplify(s.diff(ay,x)-s.diff(ax,y))==0


def test_projective_loop_even_determinant_winding_has_trivial_sign():
    phi=s.symbols('phi',real=True)
    theta=s.diag(s.exp(2*I*phi),1)
    spin=s.diag(s.exp(I*phi),s.exp(-I*phi))
    assert spin.subs(phi,0)==spin.subs(phi,2*s.pi)==ID
    a=s.simplify(s.im(s.trace(theta.inv()*theta.diff(phi)))/2)
    assert a==1
    assert s.simplify(s.exp(I*s.integrate(a,(phi,0,2*s.pi))))==1


def test_central_phase_representatives_change_integral_only_by_two_pi():
    phi=s.symbols('phi',real=True)
    n=s.symbols('n',integer=True)
    theta=s.diag(s.exp(I*phi),1)
    theta2=s.exp(I*n*phi)*theta
    a=s.simplify(s.im(s.trace(theta.inv()*theta.diff(phi)))/2)
    a2=s.simplify(s.im(s.trace(theta2.inv()*theta2.diff(phi)))/2)
    assert s.simplify(a2-a-n)==0
    assert s.simplify(s.exp(2*s.pi*I*n))==1


def test_matrix_to_lorentz_action_preserves_minkowski_determinant():
    a,b,c,d=s.symbols('a b c d',real=True)
    X=a*ID+b*s1+c*s2+d*s3
    theta=s.Matrix([[1,1],[0,1]])
    Y=theta*X*theta.H
    assert s.simplify(Y.det()-X.det())==0
    assert s.simplify(X.det()-(a*a-b*b-c*c-d*d))==0
    assert zero(Y-Y.H)


def test_canonical_congruence_is_not_left_frame_action_on_projective_matrices():
    S=I*s3
    theta=ID
    assert S.det()==1
    assert zero(S*theta*S.H-theta)
    assert S*theta!=theta
    assert S!=ID and S!=-ID


def test_metric_lock_identity_is_independent_of_matrix_value_dimension():
    u,v=s.symbols('u v',real=True)
    e=s.Matrix([[1,u,0,0],[0,1,v,0],[0,0,1,0],[0,0,0,1]])
    eta=s.diag(-1,1,1,1)
    g=e*eta*e.T
    assert s.simplify(s.trace(g.inv()*g))==4
    assert s.simplify(sum(g.inv()[i,j]*g[j,i] for i in range(4) for j in range(4)))==4


def test_two_level_quantum_positivity_is_exact_minkowski_future_cone():
    v0,v1,v2,v3=s.symbols('v0 v1 v2 v3',real=True)
    K=v0*ID+v1*s1+v2*s2+v3*s3
    assert s.simplify(s.det(K)-(v0*v0-v1*v1-v2*v2-v3*v3))==0
    assert zero(K-K.H)
    t=s.symbols('t',positive=True)
    r=s.symbols('r',positive=True)
    spec=(t*ID+r*s3).eigenvals()
    assert set(spec)=={t+r,t-r}
    rho=s.simplify(K/s.trace(K))
    assert s.simplify(s.trace(rho)-1)==0
    assert s.simplify(s.trace(s1*rho)-v1/v0)==0
    assert s.simplify(s.trace(s2*rho)-v2/v0)==0
    assert s.simplify(s.trace(s3*rho)-v3/v0)==0


def test_bilinear_k_is_not_lorentz_vector_under_canonical_congruence_boost():
    beta=s.symbols('beta',real=True)
    boost=s.diag(s.exp(beta/2),s.exp(-beta/2))
    theta=ID
    K=theta*theta.H
    canonical_theta_prime=boost*theta*boost.H
    bilinear_from_canonical=canonical_theta_prime*canonical_theta_prime.H
    vector_covariant=boost*K*boost.H
    assert zero(bilinear_from_canonical-s.diag(s.exp(2*beta),s.exp(-2*beta)))
    assert zero(vector_covariant-s.diag(s.exp(beta),s.exp(-beta)))
    assert bilinear_from_canonical.subs(beta,1)!=vector_covariant.subs(beta,1)



def test_locked_sharp_tetrad_causal_metric_is_negative_determinant_polarization():
    v=s.symbols('v0:4',real=True)
    E=[I*M for M in (ID,s1,s2,s3)]
    X=[-I*M for M in E]
    eta=s.diag(-1,1,1,1)
    def sharp(m):
        return s.trace(m)*ID-m
    for a in range(4):
        for b in range(4):
            sharp_metric=s.simplify((sharp(E[a])*E[b]+sharp(E[b])*E[a])/2)
            determinant_polar=-s.simplify(
                (s.det(X[a]+X[b])-s.det(X[a])-s.det(X[b]))/2)
            assert zero(sharp_metric-eta[a,b]*ID)
            assert determinant_polar==eta[a,b]
    Xv=sum((v[a]*X[a] for a in range(4)),s.zeros(2))
    gvv=s.expand((s.Matrix(v).T*eta*s.Matrix(v))[0])
    assert s.simplify(gvv+s.det(Xv))==0
    # On the future causal cone v0>=sqrt(v1²+v2²+v3²),
    # eigenvalues of Xv are v0 +/- spatial norm.


def test_causal_cone_is_preserved_by_lorentz_congruence_boost():
    r,b=s.symbols('r b',real=True,positive=True)
    X=r*ID
    S=s.diag(s.exp(b/2),s.exp(-b/2))
    Y=S*X*S.H
    assert s.simplify(s.det(S)-1)==0
    assert zero(Y-Y.H)
    assert s.simplify(s.det(Y)-s.det(X))==0
    assert Y[0,0].is_positive and Y[1,1].is_positive


def test_ten_nominal_coordinates_with_one_four_real_tetrad_have_six_null_directions():
    eta=s.diag(-1,1,1,1)
    e=s.eye(4).row_join(s.Matrix(4,6,lambda a,b:s.Integer((a+b)%3)))
    g=e.T*eta*e
    assert e.rank()==4
    assert g.rank()==4
    assert len(g.nullspace())==6
    for z in e.nullspace():
        assert e*z==s.zeros(4,1)
        assert g*z==s.zeros(10,1)
    assert g.det()==0


def test_null_distribution_of_six_dimensional_tetrad_can_be_nonintegrable():
    t,x,y,z,u,v=s.symbols('t x y z u v',real=True)
    eta=s.diag(-1,1,1,1)
    # e0=dt, e1=dx+u dv, e2=dy, e3=dz
    e=s.Matrix([[1,0,0,0,0,0],
                [0,1,0,0,0,u],
                [0,0,1,0,0,0],
                [0,0,0,1,0,0]])
    g=e.T*eta*e
    assert e.rank()==g.rank()==4
    ku=s.Matrix([0,0,0,0,1,0])
    kv=s.Matrix([0,-u,0,0,0,1])
    assert e*ku==e*kv==s.zeros(4,1)
    coords=(t,x,y,z,u,v)
    bracket=s.Matrix([
        sum(ku[j]*s.diff(kv[i],coords[j])-
            kv[j]*s.diff(ku[i],coords[j]) for j in range(6))
        for i in range(6)])
    assert bracket==s.Matrix([0,-1,0,0,0,0])
    assert e*bracket==s.Matrix([0,-1,0,0])
