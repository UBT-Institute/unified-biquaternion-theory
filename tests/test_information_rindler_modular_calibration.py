import sympy as s

def test_rindler_metric_and_proper_time():
    rho, eta, rho0=s.symbols("rho eta rho0", positive=True, real=True)
    t=rho*s.sinh(eta); x=rho*s.cosh(eta)
    J=s.Matrix([[s.diff(t,rho),s.diff(t,eta)],[s.diff(x,rho),s.diff(x,eta)]])
    metric=s.simplify(J.T*s.diag(-1,1)*J)
    assert metric==s.diag(1,-rho**2)
    beta=2*s.pi*rho0
    accel=1/rho0
    assert s.simplify(beta*accel-2*s.pi)==0

def test_modular_proper_generator_observer_dependence():
    B,r1,r2,Z=s.symbols("B r1 r2 Z",positive=True,real=True)
    K=2*s.pi*B+s.log(Z)
    assert s.simplify((K-s.log(Z))/(2*s.pi*r1)-B/r1)==0
    assert s.simplify((K-s.log(Z))/(2*s.pi*r2)-B/r2)==0
    assert s.simplify((B/r1)/(B/r2)-r2/r1)==0
