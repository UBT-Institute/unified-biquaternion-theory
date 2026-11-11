"""Kinematic full-rank split-jet witness is not a dynamical stability theorem."""
import sympy as sp

def test_nondegenerate_flrw_jet_at_all_real_times_symbolically():
    t=sp.symbols("t",real=True)
    a=1+t*t
    E=sp.diag(1,a,a,a)
    metric=E.T*sp.diag(-1,1,1,1)*E
    assert sp.factor(E.det())==a**3
    assert sp.factor(metric.det())==-a**6
    assert metric==sp.diag(-1,a*a,a*a,a*a)
    assert E.subs(t,0).rank()==4

def test_rank_gate_contrast_with_scalar_branch():
    t=sp.symbols("t",real=True)
    a=1+t*t
    E4=sp.diag(1,a,a,a)
    Erad=sp.zeros(4)
    Erad[0,0]=1
    assert E4.det().subs(t,0)==1
    assert Erad.rank()==1
    assert Erad.det()==0
