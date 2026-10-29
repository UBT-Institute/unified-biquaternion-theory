"""1+1 Dirac causal support, operational Fisher information, and nonselection gates.

The symbolic tests do not certify a physical UBT Hamiltonian. hbar=1 except
where the mass estimate is written dimensionfully.
"""
import sympy as s

sx=s.Matrix([[0,1],[1,0]])
sz=s.diag(1,-1)
I2=s.eye(2)


def test_dirac_mass_does_not_change_characteristic_cone():
    c,k,w,mu=s.symbols('c k w mu',real=True,positive=True)
    principal=s.I*(c*k*sx-w*I2)
    assert s.simplify(principal.det()-(c*k-w)*(c*k+w))==0
    full=c*k*sx+mu*sz
    assert s.expand(full*full-(c*c*k*k+mu*mu)*I2)==s.zeros(2)


def test_dirac_probability_conservation_any_mass():
    c,mu=s.symbols('c mu',real=True)
    u,v,ux,vx=s.symbols('u v ux vx',complex=True)
    psi=s.Matrix([u,v]); dx=s.Matrix([ux,vx])
    dpsi=-c*sx*dx-s.I*mu*sz*psi
    dt_density=s.expand((dpsi.conjugate().T*psi+psi.conjugate().T*dpsi)[0])
    dx_flux=s.expand(c*(dx.conjugate().T*sx*psi+psi.conjugate().T*sx*dx)[0])
    assert s.simplify(dt_density+dx_flux)==0
    rho=(psi.conjugate().T*psi)[0]
    j=(c*psi.conjugate().T*sx*psi)[0]
    assert s.simplify(c*rho+j-c*(u+v)*s.conjugate(u+v))==0
    assert s.simplify(c*rho-j-c*(u-v)*s.conjugate(u-v))==0


def test_local_measurements_distinguish_allowed_masses():
    mu,t=s.symbols('mu t',real=True)
    state=s.Matrix([1,1])/s.sqrt(2)
    U=s.cos(mu*t)*I2-s.I*s.sin(mu*t)*sz
    assert s.simplify(U.conjugate().T*U-I2)==s.zeros(2)
    x_exp=s.simplify((state.conjugate().T*U.conjugate().T*sx*U*state)[0])
    assert s.simplify(s.expand_trig(x_exp-s.cos(2*mu*t)))==0
    assert s.simplify(x_exp.subs(mu,0)-1)==0
    assert s.simplify(x_exp.subs(mu,1).subs(t,s.pi/4))==0


def test_mass_fisher_information_scales_with_speed_not_unique():
    m,c,t,hbar=s.symbols('m c t hbar',positive=True,real=True)
    theta=m*c**2*t/hbar
    p=s.cos(theta)**2
    dp=s.diff(p,m)
    fisher=s.trigsimp(dp**2/(p*(1-p)))
    assert s.simplify(fisher-4*c**4*t**2/hbar**2)==0


def test_observer_past_cone_obeys_light_speed():
    c=s.symbols('c',positive=True)
    def visible(event,observer):
        t,x=event; to,xo=observer
        return (to>=t) and abs(xo-x)<=c*(to-t)
    assert visible((0,0),(2,0))
    assert visible((0,4),(2,0)).subs(c,1) is s.false
    assert visible((0,1),(2,0)).subs(c,1) is s.true


def test_shared_local_record_consistency_nonunique_hamiltonian():
    mu,t=s.symbols('mu t',real=True)
    state=s.Matrix([1,1])/s.sqrt(2)
    U=s.cos(mu*t)*I2-s.I*s.sin(mu*t)*sz
    rho=s.simplify(U*state*state.conjugate().T*U.conjugate().T)
    assert s.simplify(s.trace(rho)-1)==0
    common=s.simplify(s.trace(rho*sx))
    assert s.simplify(common-s.cos(2*mu*t))==0
    assert common.subs({mu:0,t:s.pi/4})==1
    assert common.subs({mu:1,t:s.pi/4})==0


def test_horizon_restriction_can_hide_distinct_global_states():
    outside_zero=s.diag(1,0,0,0)
    outside_one=s.diag(0,1,0,0)
    def accessible_restriction(rho):
        return s.Matrix(2,2,lambda a,b:rho[2*a,2*b]+rho[2*a+1,2*b+1])
    assert accessible_restriction(outside_zero)==accessible_restriction(outside_one)==s.diag(1,0)
    assert outside_zero!=outside_one
    hidden=s.kronecker_product(I2,sz)
    assert s.trace(outside_zero*hidden)==1
    assert s.trace(outside_one*hidden)==-1
