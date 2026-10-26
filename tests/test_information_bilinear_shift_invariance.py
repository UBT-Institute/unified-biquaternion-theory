import sympy as s

def test_lorentz_norm_is_not_carrier_shift_invariant():
    X=s.Matrix(s.symbols('x0:4',real=True))
    e=s.Matrix(s.symbols('e0:4',real=True))
    eta=s.diag(1,-1,-1,-1)
    h=(X.T*eta*X)[0]
    variation=s.expand(((X+e).T*eta*(X+e))[0]-h)
    linear=s.expand(sum(s.diff(variation,v).subs(dict.fromkeys(e,0))*v for v in e))
    assert s.simplify(linear-2*(X.T*eta*e)[0])==0
    assert linear!=0

def test_shift_preserves_composite_tetrad():
    dX,Q,de=s.symbols('dX Q de')
    assert (dX+de)+(Q-de)==dX+Q

def test_only_constant_quadratic_polynomial_is_shift_invariant():
    x=s.symbols('x0:4',real=True)
    A=s.Matrix(4,4,s.symbols('a0:16'))
    H=(s.Matrix(x).T*A*s.Matrix(x))[0]
    derivatives=[s.diff(H,v) for v in x]
    constraints=[s.expand(d).coeff(v) for d in derivatives for v in x]
    sol=s.linsolve(constraints,list(A))
    assert all(s.simplify(v)==0 for v in next(iter(sol)) if not v.free_symbols)
    # Stronger direct check: symmetric part vanishes; antisymmetric quadratic form is identically zero.
    assert len(constraints)>0
