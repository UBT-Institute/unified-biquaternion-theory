import sympy as s

def test_theta_T_squared_and_unitary_recurrence():
    n=s.symbols('n',integer=True)
    t,R,eps=s.symbols('t R eps',real=True,positive=True)
    T=2*s.pi*R**2
    theta_tau=(-t+s.I*eps)/(s.pi*R**2)
    phase=s.exp(s.pi*s.I*n*n*theta_tau)
    shifted=s.exp(s.pi*s.I*n*n*(theta_tau-2))
    assert s.simplify(shifted/phase-1)==0
    U=s.exp(-s.I*t*n*n/R**2)
    U_after=s.exp(-s.I*(t+T)*n*n/R**2)
    assert s.simplify(U_after/U-1)==0

def test_scale_and_gap_not_selected():
    hbar,R,alpha=s.symbols('hbar R alpha',positive=True)
    T=2*s.pi*hbar*R**2/alpha
    n=s.symbols('n',integer=True)
    assert s.simplify(s.exp(-s.I*(alpha*n*n/R**2)*T/hbar)-1)==0
    assert s.diff(T,alpha)!=0
