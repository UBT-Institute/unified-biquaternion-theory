import sympy as s

def test_schur_and_old_shift():
    a,b,c=s.symbols('a b c', real=True, nonzero=True)
    H=s.Matrix([[a,b],[b,c]])
    assert H.det()==a*c-b*b
    assert H*s.Matrix([0,1])==s.Matrix([b,c])
    assert s.simplify((c-b*b/a)-(H.det()/a))==0
    assert (H.subs(c,b*b/a)*s.Matrix([-b/a,1])).applyfunc(s.simplify)==s.zeros(2,1)

def test_coupled_positive_and_degenerate():
    a,b,c=s.symbols('a b c',real=True)
    v,w=s.symbols('v w',real=True)
    L=a*v*v/2+b*v*w+c*w*w/2
    assert s.hessian(L,(v,w))==s.Matrix([[a,b],[b,c]])
    assert s.simplify(L.subs(c,b*b/a)-a*(v+b*w/a)**2/2)==0
