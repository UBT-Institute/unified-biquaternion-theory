"""Exact algebra tests for restricted full-Clifford odd-sector quadratic comparison.

Finite symbolic identities only; do not imply UBT action closure or ghost-freedom.
"""
import sympy as sp


def test_restricted_odd_principal_polynomial():
    kv, ka, kx, mv, ma, mu, p = sp.symbols("kv ka kx mv ma mu p", real=True)
    C = sp.Matrix([[mv + kv*p, mu + kx*p], [mu + kx*p, ma + ka*p]])
    det = sp.expand(C.det())
    assert sp.simplify(det - ((mv + kv*p)*(ma + ka*p) - (mu + kx*p)**2)) == 0
    assert det.coeff(p, 2) == kv*ka-kx**2


def test_parity_decoupled_still_has_derivatives():
    kv, ka, mv, ma, p = sp.symbols("kv ka mv ma p", real=True)
    C = sp.diag(mv + kv*p, ma + ka*p)
    assert sp.simplify(C.det() - (mv+kv*p)*(ma+ka*p)) == 0
    assert sp.expand(C.det()).coeff(p, 2) == kv*ka


def test_exact_auxiliary_odd_elimination():
    a, b, c, u, v = sp.symbols("a b c u v", real=True, nonzero=True)
    L = a*u*u/2 + b*u*v + c*v*v/2
    v_star = sp.solve(sp.diff(L, v), v)[0]
    assert v_star == -b*u/c
    assert sp.simplify(L.subs(v, v_star) - (a-b*b/c)*u*u/2) == 0


def test_symmetric_odd_action_does_not_force_odd_zero():
    a, c, lam, u, v = sp.symbols("a c lam u v", real=True)
    L = a*u*u/2 + c*v*v/2 + lam*u*u*v*v
    assert sp.expand(L.subs(v, -v)-L) == 0
    assert sp.simplify(sp.diff(L,v).subs(v,0)) == 0
    assert sp.diff(L,v,2).subs(v,0) == c+2*lam*u*u
