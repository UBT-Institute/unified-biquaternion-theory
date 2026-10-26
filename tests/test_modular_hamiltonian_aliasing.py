import sympy as s

def test_sampled_two_level_unitary_has_distinct_continuous_generators():
    hbar,T,E0,E1=s.symbols("hbar T E0 E1",positive=True,real=True)
    H=s.diag(E0,E1)
    Hprime=s.diag(E0,E1+2*s.pi*hbar/T)
    U=s.diag(s.exp(-s.I*E0*T/hbar),s.exp(-s.I*E1*T/hbar))
    Up=s.diag(s.exp(-s.I*Hprime[0,0]*T/hbar),s.exp(-s.I*Hprime[1,1]*T/hbar))
    assert s.simplify(Up-U)==s.zeros(2)
    assert Hprime-H != s.eye(2)*s.symbols("c")

def test_modular_thermal_identity():
    beta,E0,E1=s.symbols("beta E0 E1",real=True,positive=True)
    Z=s.exp(-beta*E0)+s.exp(-beta*E1)
    K=s.diag(beta*E0+s.log(Z),beta*E1+s.log(Z))
    H=(K-s.log(Z)*s.eye(2))/beta
    assert s.simplify(H-s.diag(E0,E1))==s.zeros(2)
