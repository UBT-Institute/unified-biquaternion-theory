import sympy as s

def test_radial_oscillator_boundary_levels():
    t,m=s.symbols('t m',real=True,positive=True)
    k=s.symbols('k',integer=True,nonnegative=True)
    hbar=s.symbols('hbar',positive=True)
    r2=s.cos(m*t)**2
    assert s.trigsimp(s.diff(r2,t,2)+4*m*m*(r2-s.Rational(1,2)))==0
    E=lambda n:hbar*m*(n+s.Rational(1,2))
    assert s.simplify(E(2*k+1)-hbar*m*(2*k+s.Rational(3,2)))==0
    assert s.simplify(E(2*k)-hbar*m*(2*k+s.Rational(1,2)))==0
    assert s.simplify(E(2*k+2)-E(2*k))==2*hbar*m
