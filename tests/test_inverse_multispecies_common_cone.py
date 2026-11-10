"""Exact two-species Bloch-cone checks; not a UBT geometry derivation."""
import sympy as sp


def test_flavor_exchange_enforces_equal_kinetic_coefficients():
    a, k, va, vb = sp.symbols('a k va vb', positive=True)
    sx = sp.Matrix([[0, 1], [1, 0]])
    H = sp.kronecker_product(sx, sp.diag(va, vb)) * sp.sin(a*k)/a
    F = sp.kronecker_product(sp.eye(2), sx)
    delta = sp.simplify(F*H*F-H)
    assert delta != sp.zeros(4)
    assert delta.subs(vb, va) == sp.zeros(4)
    assert sp.simplify(delta[0,2]) == (vb-va)*sp.sin(a*k)/a


def test_two_cone_polynomial_and_ratio_obstruction():
    w, k, va, vb, lam = sp.symbols('w k va vb lam', positive=True)
    pa, pb = w**2-va**2*k**2, w**2-vb**2*k**2
    assert sp.expand(sp.factor(pa*pb) -
                     (w**2-va**2*k**2)*(w**2-vb**2*k**2)) == 0
    assert sp.simplify((lam*va)/(lam*vb)-va/vb) == 0


def test_group_velocities_and_continuum_limit():
    a,k,va,vb=sp.symbols('a k va vb', positive=True)
    for v in (va,vb):
        E=v*sp.sin(a*k)/a
        assert sp.diff(E,k) == v*sp.cos(a*k)
        assert sp.limit(E/k,k,0)==v
        assert sp.simplify(E.subs(k,sp.pi/a))==0


def test_symmetric_species_matrix_squared():
    a,k,v=sp.symbols('a k v',positive=True)
    sx=sp.Matrix([[0,1],[1,0]])
    H=sp.kronecker_product(sx,sp.eye(2))*v*sp.sin(a*k)/a
    assert sp.simplify(H*H - sp.eye(4)*v**2*sp.sin(a*k)**2/a**2)==sp.zeros(4)
