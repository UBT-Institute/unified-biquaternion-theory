import sympy as s

def test_relative_entropy_stationary_quadratic_binary():
    eps,p=s.symbols("eps p",positive=True)
    # Two outcomes, reference (p,1-p); local perturbation (+eps,-eps)
    D=(p+eps)*s.log((p+eps)/p)+(1-p-eps)*s.log((1-p-eps)/(1-p))
    assert s.simplify(s.diff(D,eps).subs(eps,0))==0
    assert s.simplify(s.diff(D,eps,2).subs(eps,0)-1/(p*(1-p)))==0

def test_first_law_binary_at_reference():
    eps,p=s.symbols("eps p",positive=True)
    S=-(p+eps)*s.log(p+eps)-(1-p-eps)*s.log(1-p-eps)
    K=s.log((1-p)/p)
    assert s.simplify(s.diff(S,eps).subs(eps,0)-K)==0
