import sympy as s

def test_mm_flrw_legendre_and_friedmann():
    a,N,k,L,v,p=s.symbols("a N k L v p",positive=True)
    lag=-3*a*v*v/(k*N)-L*N*a**3/k
    mom=s.diff(lag,v)
    assert mom==-6*a*v/(k*N)
    H=s.simplify((p*v-lag).subs(v,-k*N*p/(6*a)))
    assert s.simplify(H-N*(-k*p*p/(12*a)+L*a**3/k))==0
    fried=s.simplify((-k*p*p/(12*a)+L*a**3/k).subs(p,mom))
    assert s.simplify(fried-(-3*a*v*v/(k*N*N)+L*a**3/k))==0

def test_mm_couplings_and_cosmological_term():
    g,l,e=s.symbols("g l e",nonzero=True)
    k=g*g*l*l/2
    L=3*e/(l*l)
    assert s.simplify(k*L-s.Rational(3,2)*e*g*g)==0
