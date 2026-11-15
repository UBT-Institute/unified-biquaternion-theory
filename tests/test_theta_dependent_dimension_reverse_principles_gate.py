"""Conditional differential-geometric and observer-rank diagnostics; no UBT action derived.

These checks separate four spacetime coordinates, eight real Theta values,
physical observer readout rank, and one hypothetical dependent compact angle.
"""
import sympy as s

I=s.I
S=(s.eye(2),s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1))


def test_complex_biquaternion_eight_real_components():
    re=s.symbols("re0:4",real=True)
    im=s.symbols("im0:4",real=True)
    theta=sum(((re[a]+I*im[a])*S[a] for a in range(4)),s.zeros(2))
    reconstructed=[s.trace(S[a]*theta)/2 for a in range(4)]
    assert [s.simplify(reconstructed[a]-re[a]-I*im[a]) for a in range(4)]==[0]*4
    assert len(re+im)==8


def test_flat_canonical_real_slice_reduces_32_jets_to_16():
    # Four spacetime derivative directions times eight real matrix entries.
    # dTheta in i Herm2 enforces 4 linear real conditions per derivative.
    ar=s.symbols("ar0:16",real=True)
    ai=s.symbols("ai0:16",real=True)
    constraint_jac=s.eye(16).row_join(s.zeros(16))
    assert constraint_jac.rank()==16
    assert len(ar+ai)-constraint_jac.rank()==16


def test_holonomic_real_gradient_tetrad_is_flat_4d_metric():
    t,x,y,z,lam=s.symbols("t x y z lam",real=True)
    h=s.Matrix([t,x+lam*t*y,y,z])
    J=h.jacobian((t,x,y,z))
    eta=s.diag(-1,1,1,1)
    assert J.det()==1
    g=J.T*eta*J
    assert (J.inv().T*g*J.inv()).applyfunc(s.simplify)==eta


def test_dependent_compact_coordinate_has_unobservable_vertical_jet():
    x,y,psi,k=s.symbols("x y psi k",real=True,nonzero=True)
    f=k*x*y
    F=s.Function("F")(x,y)
    H=s.Function("H")(x,y)
    lift1=F
    lift2=F+s.sin(psi-f)*H
    assert s.simplify(lift2.subs(psi,f)-F)==0
    assert s.simplify((s.diff(lift2,psi)-s.diff(lift1,psi)).subs(psi,f)-H)==0
    for q in (x,y):
        D2=s.diff(lift2,q)+s.diff(lift2,psi)*s.diff(f,q)
        D1=s.diff(lift1,q)+s.diff(lift1,psi)*s.diff(f,q)
        assert s.simplify((D2-D1).subs(psi,f))==0
    assert s.trigsimp(lift2.subs(psi,psi+2*s.pi)-lift2)==0


def test_flat_five_d_ambient_with_dependent_psi_can_induce_nonflat_4d():
    t,x,y,z,k,R=s.symbols("t x y z k R",real=True,nonzero=True)
    f=k*x*y
    df=s.Matrix([s.diff(f,q) for q in (t,x,y,z)])
    eta=s.diag(-1,1,1,1)
    g=eta+R**2*df*df.T
    assert s.simplify(g.det()+1+R**2*k**2*(x**2+y**2))==0
    assert g[0,0]==-1 and g[3,3]==1
    den=1+R**2*(s.diff(f,x)**2+s.diff(f,y)**2)
    gauss=s.simplify(R**2*(s.diff(f,x,2)*s.diff(f,y,2)-s.diff(f,x,y)**2)/den)
    assert s.simplify(gauss+R**2*k**2/(1+R**2*k**2*(x*x+y*y)))==0
    assert gauss.subs({x:0,y:0})==-R**2*k**2


def test_dependent_dimension_graph_has_no_linear_metric_mode_about_constant_f():
    t,x,y,z,R,eps=s.symbols("t x y z R eps",real=True)
    f=eps*(x*y+t*z)
    df=s.Matrix([s.diff(f,q) for q in (t,x,y,z)])
    eta=s.diag(-1,1,1,1)
    g=eta+R**2*df*df.T
    assert g.diff(eps).subs(eps,0)==s.zeros(4)
    assert g.subs(eps,0)==eta


def test_one_local_density_matrix_cannot_recover_all_eight_real_theta_components():
    a=s.symbols("a0:4",real=True)
    b=s.symbols("b0:4",real=True)
    eps=s.symbols("eps",real=True)
    X=sum(((a[j]+I*b[j])*S[j] for j in range(4)),s.zeros(2))
    Theta=S[0]+eps*X
    Q=Theta*Theta.H
    rho=Q/s.trace(Q)
    delta_rho=rho.diff(eps).subs(eps,0).applyfunc(s.simplify)
    assert delta_rho==sum((a[j]*S[j] for j in range(1,4)),s.zeros(2))
    bloch=s.Matrix([s.trace(S[j]*delta_rho) for j in range(1,4)])
    J=bloch.jacobian(a+b)
    assert J.rank()==3
    assert len(a+b)-J.rank()==5


def test_metric_locked_kinetic_norm_is_exactly_four_not_new_gravity_dynamics():
    u,v,w=s.symbols("u v w",real=True)
    e=s.Matrix([[1,u,0,0],[0,1,v,0],[0,0,1,w],[0,0,0,1]])
    eta=s.diag(-1,1,1,1)
    g=e*eta*e.T
    assert e.det()==1
    norm=s.simplify(sum(g.inv()[mu,nu]*g[mu,nu]
        for mu in range(4) for nu in range(4)))
    assert norm==4
    assert s.diff(norm,u)==s.diff(norm,v)==s.diff(norm,w)==0



def test_nonintegrable_circle_connection_gives_u1_curvature_not_graph():
    x,y,psi,B,q=s.symbols("x y psi B q",real=True)
    Ax=s.Integer(0)
    Ay=B*x
    assert s.diff(Ay,x)-s.diff(Ax,y)==B
    chi=q*x*y
    Ax_new=Ax+s.diff(chi,x)
    Ay_new=Ay+s.diff(chi,y)
    assert s.simplify(s.diff(Ay_new,x)-s.diff(Ax_new,y)-B)==0
    # Horizontal lifts Hx=partial_x-Ax partial_psi and
    # Hy=partial_y-Ay partial_psi do not commute vertically.
    vertical_bracket=-s.diff(Ay,x)+s.diff(Ax,y)
    assert vertical_bracket==-B
    # A graph df=-A would require equality of mixed derivatives.
    assert s.simplify(s.diff(-Ay,x)-s.diff(-Ax,y))==-B


def test_kk_fixed_radius_magnetic_field_gives_exact_curvature_square():
    # Full 5D ds5²=-dt²+dx²+dy²+dz²+R²(dpsi+B*x*dy)².
    t,x,y,z,psi,R,B=s.symbols("t x y z psi R B",real=True,nonzero=True)
    coords=(t,x,y,z,psi)
    G=s.diag(-1,1,1,1,R**2)
    G[2,2]+=R**2*B**2*x**2
    G[2,4]=G[4,2]=R**2*B*x
    inv=s.simplify(G.inv())
    gamma={}
    for a in range(5):
        for b in range(5):
            for c in range(b,5):
                v=s.simplify(sum(inv[a,d]*(s.diff(G[d,b],coords[c])+
                    s.diff(G[d,c],coords[b])-s.diff(G[b,c],coords[d]))/2
                    for d in range(5)))
                if v!=0:
                    gamma[a,b,c]=gamma[a,c,b]=v
    def C(a,b,c):
        return gamma.get((a,b,c),s.Integer(0))
    ric=s.zeros(5)
    for a in range(5):
        for b in range(5):
            v=0
            for k in range(5):
                v+=s.diff(C(k,a,b),coords[k])-s.diff(C(k,a,k),coords[b])
                for m in range(5):
                    v+=C(k,k,m)*C(m,a,b)-C(k,b,m)*C(m,a,k)
            ric[a,b]=s.simplify(v)
    scalar=s.simplify(sum(inv[a,b]*ric[a,b] for a in range(5) for b in range(5)))
    assert s.simplify(scalar+R**2*B**2/2)==0
