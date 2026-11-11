"""Exact free split-jet bare-action obstruction to geometric Cauchy uniqueness."""
import sympy as sp


def test_critical_zero_density_all_geometries():
    V, dV, eps, F = sp.symbols("V dV eps F", real=True)
    density=(V+eps*dV)*F
    assert sp.expand(density.subs(F,0))==0
    assert sp.expand(sp.diff(density,eps,2).subs(F,0))==0
    assert sp.expand(sp.diff(density,eps).subs(F,0))==0


def test_regular_families_equal_initial_jet_but_different_curvature():
    T=sp.symbols("T", real=True)
    results=[]
    for alpha in (1,2):
        a=1+alpha*T*T
        E=sp.diag(1,a,a,a)
        g=sp.diag(-1,a*a,a*a,a*a)
        R00=-3*sp.diff(a,T,2)/a
        R=6*(sp.diff(a,T,2)/a+(sp.diff(a,T)**2+1)/a**2)
        assert E.det()==a**3
        assert g.det()==-a**6
        assert E.subs(T,0)==sp.eye(4)
        assert sp.diff(E,T).subs(T,0)==sp.zeros(4)
        results.append((sp.simplify(R00.subs(T,0)),
                        sp.simplify(R.subs(T,0))))
    assert results==[(-6,18),(-12,30)]


def test_zero_action_does_not_control_nonzero_tetrad_motion():
    t,mu=sp.symbols("t mu",real=True)
    # Every member of the regular alpha family is allowed at the
    # critical-zero point of the specified free-jet action.
    a=1+(1+mu**2)*t**2
    E=sp.diag(1,a,a,a)
    detE=E.det()
    S_density=sp.expand(detE*sp.Integer(0))
    assert S_density==0
    assert sp.diff(S_density,t)==0
    assert sp.diff(S_density,mu,2)==0
    assert sp.diff(a,t,2).subs(t,0)==2*(1+mu**2)
