import sympy as sp

def test_mm_eh_wald_entropy_normalization():
    kappa,gG,ell,area=sp.symbols("kappa gG ell area",positive=True)
    G=kappa/(8*sp.pi)
    S=area/(4*G)
    assert sp.simplify(S-2*sp.pi*area/kappa)==0
    assert sp.simplify(S.subs(kappa,gG**2*ell**2/2)-4*sp.pi*area/(gG**2*ell**2))==0
    assert sp.simplify(sp.diff(S,area)-2*sp.pi/kappa)==0

def test_modular_first_law_in_two_level_example():
    p,epsilon=sp.symbols("p epsilon",real=True,positive=True)
    S=lambda q:-q*sp.log(q)-(1-q)*sp.log(1-q)
    K0=-sp.log(p);K1=-sp.log(1-p)
    assert sp.simplify(sp.diff(S(p+epsilon),epsilon).subs(epsilon,0)-(K0-K1))==0
