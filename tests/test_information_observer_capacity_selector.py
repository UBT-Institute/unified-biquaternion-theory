"""Observer information capacity, noisy readout and Hamiltonian identifiability."""
import sympy as s

X=s.Matrix([[0,1],[1,0]])
Z=s.diag(1,-1)
I=s.eye(2)

def test_colocated_capable_and_incapable_observers():
    mu,t=s.symbols('mu t',real=True)
    phi=s.Matrix([1,1])/s.sqrt(2)
    U=s.cos(mu*t)*I-s.I*s.sin(mu*t)*Z
    psi=U*phi
    p_z=s.simplify((psi.conjugate().T*(I+Z)/2*psi)[0])
    p_x=s.simplify((psi.conjugate().T*(I+X)/2*psi)[0])
    assert p_z==s.Rational(1,2)
    assert s.trigsimp(p_x-s.cos(mu*t)**2)==0
    assert s.simplify(p_x.subs({mu:0,t:1})-p_x.subs({mu:s.pi/4,t:1}))!=0

def test_noisy_detector_fisher_information_reduced():
    epsilon,mu,t=s.symbols('epsilon mu t',real=True)
    phase=mu*t
    p=s.cos(phase)**2
    out=epsilon+(1-2*epsilon)*p
    d=s.diff(out,mu)
    fisher=s.trigsimp(d*d/(out*(1-out)))
    at_balanced=s.trigsimp(fisher.subs(mu,s.pi/(4*t)))
    assert s.simplify(at_balanced-4*t*t*(1-2*epsilon)**2)==0
    assert s.simplify(at_balanced.subs(epsilon,s.Rational(1,2)))==0
    assert s.simplify(at_balanced.subs(epsilon,0)-4*t*t)==0

def test_data_processing_fisher_inequality_exact():
    p,e,dp=s.symbols('p e dp',real=True)
    noisy=e+(1-2*e)*p
    ideal=dp**2/(p*(1-p))
    reduced=(1-2*e)**2*dp**2/(noisy*(1-noisy))
    gap=s.factor(ideal-reduced)
    expected=e*(1-e)*dp**2/(p*(1-p)*noisy*(1-noisy))
    assert s.simplify(gap-expected)==0

def test_binary_record_has_at_most_one_bit_of_information():
    import math
    possibilities=[(a,b) for a in range(2) for b in range(2)]
    parity=[a^b for a,b in possibilities]
    assert len(set(parity))==2
    entropy_raw=math.log2(len(possibilities))
    entropy_parity=-sum((parity.count(r)/4)*math.log2(parity.count(r)/4) for r in (0,1))
    assert entropy_raw==2 and entropy_parity==1

def test_empirical_equivalence_refines_with_new_measurement():
    t=s.pi/4
    mu0,mu1=0,1
    z=lambda mu:s.Rational(1,2)
    x=lambda mu:s.simplify(s.cos(mu*t)**2)
    assert z(mu0)==z(mu1)
    assert x(mu0)!=x(mu1)

def test_information_is_not_directly_hamiltonian_uniqueness():
    mu=s.symbols('mu',real=True)
    H=mu*Z
    assert s.simplify(H*Z-Z*H)==s.zeros(2)
    assert s.simplify(H*X-X*H)!=s.zeros(2)
