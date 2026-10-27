"""Observer-specific Hamiltonians by relativistic time calibration (reference identities)."""
import sympy as s

I=s.eye(2)
SX=s.Matrix([[0,1],[1,0]])

def test_lorentz_mass_shell():
    E,p,v,c=s.symbols("E p v c",real=True)
    gamma=1/s.sqrt(1-v*v/c**2)
    Eprime=gamma*(E-v*p)
    pprime=gamma*(p-v*E/c**2)
    assert s.simplify(Eprime**2-c*c*pprime**2-(E**2-c*c*p*p))==0

def test_observer_hamiltonian_derivative():
    v,c=s.symbols("v c",positive=True)
    H,P=s.symbols("H P",real=True)
    gamma=1/s.sqrt(1-v*v/c**2)
    hv=gamma*(H-v*P)
    assert s.simplify(s.diff(hv,v)-gamma**3*(v*H/c**2-P))==0

def test_distance_not_changing_generator():
    d,p0,p1,h0,h1=s.symbols("d p0 p1 h0 h1",real=True)
    H=s.diag(h0,h1)
    T=s.diag(s.exp(-s.I*d*p0),s.exp(-s.I*d*p1))
    assert s.simplify(T*H*T.conjugate().T-H)==s.zeros(2)

def test_rindler_modular_rescaling():
    B,r1,r2=s.symbols("B r1 r2",positive=True)
    K=2*s.pi*B
    assert s.simplify((B/r1)*2*s.pi*r1-K)==0
    assert s.simplify((B/r1)/(B/r2)-r2/r1)==0

def test_same_dirac_cone_different_mass():
    omega,p,c,m1,m2=s.symbols("omega p c m1 m2",real=True)
    z=s.diag(1,-1)
    eye=s.eye(2)
    principal=omega*eye-c*p*SX
    assert s.simplify(principal.det()-(omega**2-c**2*p**2))==0
    assert c*p*SX+m1*c*c*z != c*p*SX+m2*c*c*z
