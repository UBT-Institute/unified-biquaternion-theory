"""Conditional kinematic gates for the right-vector U(1) projected connection.

Background: Theta=i[(c+t)I+x sigma1+y sigma2+z sigma3], Omega=0.
No claim about physical photons or the full composite one-Theta action.
"""
import sympy as sp

I=sp.I
sig=(sp.eye(2),sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-I],[I,0]]),sp.diag(1,-1))
t,x,y,z=sp.symbols('t x y z', real=True)
c=sp.symbols('c',real=True,positive=True)
coords=(t,x,y,z)
h=(c+t)*sig[0]+x*sig[1]+y*sig[2]+z*sig[3]
theta=I*h
point={t:0,x:0,y:0,z:0}

def proj(m):
    return sp.simplify(sp.im(sp.trace(sig[3]*m))/2)

def test_locked_flat_tetrad_and_exact_holonomic_coordinate_map():
    legs=[theta.diff(q) for q in coords]
    metric=sp.diag(-1,1,1,1)
    for i in range(4):
        assert legs[i]==I*sig[i]
        assert legs[i]+legs[i].H==sp.zeros(2)
        for j in range(4):
            sharp_i=sp.trace(legs[i])*sig[0]-legs[i]
            sharp_j=sp.trace(legs[j])*sig[0]-legs[j]
            assert sp.simplify((sharp_i*legs[j]+sharp_j*legs[i])/2)==metric[i,j]*sig[0]
    carrier=sp.Matrix([c+t,x,y,z])
    j=carrier.jacobian(coords)
    assert j.det()==1
    assert j.T*metric*j==metric


def test_affine_background_projected_curvature_not_zero():
    a=[proj(theta.inv()*theta.diff(q)) for q in coords]
    delta=(c+t)**2-x*x-y*y-z*z
    assert sp.simplify(a[0])==0
    assert sp.simplify(a[1]-y/delta)==0
    assert sp.simplify(a[2]+x/delta)==0
    assert sp.simplify(a[3])==0
    fxy=sp.simplify(sp.diff(a[2],x)-sp.diff(a[1],y))
    assert sp.simplify(fxy.subs(point)+2/c**2)==0


def test_all_eight_real_theta_tangents_have_rank_two_first_derivative_symbol():
    # Theta -> Theta(I+epsilon Y); exact variation of B is dY+[B,Y].
    # The projected dY is an exact 1-form and drops from f=d a.
    yre=sp.symbols('r0:4',real=True)
    yim=sp.symbols('im0:4',real=True)
    Y=sum(((yre[j]+I*yim[j])*sig[j] for j in range(4)),sp.zeros(2))
    b=[(theta.inv()*theta.diff(q)).subs(point).applyfunc(sp.simplify) for q in coords]
    q=[proj(b[i]*Y-Y*b[i]) for i in range(4)]
    q=[sp.simplify(sp.expand_complex(v)) for v in q]
    assert q==[0,2*yre[2]/c,-2*yre[1]/c,0]
    jac=sp.Matrix(4,8,lambda i,j:sp.diff(q[i],(yre+yim)[j]))
    assert jac.rank()==2


def test_missing_z_polarization_for_wave_moving_in_x_direction():
    rx,ry,rz,omega,k=sp.symbols('rx ry rz omega k',real=True)
    # Principal first order change of a modulo exact gradient from test above
    a=sp.Matrix([0,2*ry/c,-2*rx/c,0])
    p=sp.Matrix([-omega,k,0,0])
    f=sp.Matrix(4,4,lambda mu,nu:sp.expand(p[mu]*a[nu]-p[nu]*a[mu]))
    assert f[0,3]==0 # no electric F_tz polarization
    assert f[0,2]==2*omega*rx/c # y transverse polarization remains
    assert f[0,1]==-2*omega*ry/c # x-longitudinal, constrained for Maxwell
    # For a wave moving along z, both x and y directions are present.
    pz=sp.Matrix([-omega,0,0,k])
    fz=sp.Matrix(4,4,lambda mu,nu:sp.expand(pz[mu]*a[nu]-pz[nu]*a[mu]))
    assert fz[0,1]==-2*omega*ry/c
    assert fz[0,2]==2*omega*rx/c


def test_massless_flat_one_theta_dirac_not_solved_by_affine_tetrad():
    # Existing assumed flat comparator: dot Theta = sigma_j d_j Theta - i m eps conj(Theta) sigma1.
    mismatch=theta.diff(t)-sum((sig[j]*theta.diff(coords[j]) for j in range(1,4)),sp.zeros(2))
    assert mismatch==-2*I*sig[0]
    mass=sp.symbols('mass',real=True)
    epsilon=I*sig[2]
    mass_source=(-I*mass*epsilon*theta.conjugate()*sig[1]).subs(point)
    assert sp.trace(mass_source)==0
    assert sp.trace(mismatch.subs(point))==-4*I
    # Therefore no real mass can repair the matrix mismatch at this point.


def test_pure_real_gradient_tetrad_fluctuations_are_diffeomorphisms():
    # For any invertible h^a(x) the metric is eta_ab dh^a dh^b;
    # its curvature vanishes because h^a themselves are local coordinates.
    lam=sp.symbols('lam',real=True)
    hfield=sp.Matrix([c+t,x+lam*t*y,y,z])
    E=hfield.jacobian(coords)
    assert E.det()==1
    eta=sp.diag(-1,1,1,1)
    g=E.T*eta*E
    xi=sp.Matrix([0,lam*t*y,0,0])
    # At lam=0, δg=L_xi eta, hence δRiemann=0 (pure gauge).
    dmetric=g.diff(lam).subs(lam,0)
    expected=sp.Matrix(4,4,lambda mu,nu:
        sum(eta[a,nu]*sp.diff(xi[a],coords[mu])+
            eta[a,mu]*sp.diff(xi[a],coords[nu]) for a in range(4)) / lam)
    assert sp.simplify(dmetric-expected)==sp.zeros(4)
