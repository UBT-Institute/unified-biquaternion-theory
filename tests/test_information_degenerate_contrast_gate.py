"""Degenerate full-Theta invariant contrast: no pure acceleration and tilted WKB gate.

Exact restricted positive-H derived-center fixed-Minkowski-coframe checks.
No claim of a physical UBT action, full constrained spectrum or transmission.
"""
import sympy as sp


def invariants(r, u, v, s):
    k = v*v - u*u
    H = 8*s*s*r*(1-r)/k
    J = 64*s**4*r**3*v*v/k**3
    q = sp.factor(4*J/H**2)
    T = sp.factor(4*J/H**3)
    return H, J, q, T


def variables():
    return sp.symbols("r u v s", real=True, nonzero=True)


def test_exact_full_theta_invariant_contrast_cancels_timelike_norm():
    r, u, v, s = variables()
    _, _, _, T = invariants(r, u, v, s)
    assert sp.factor(T - v*v/(2*s*s*(1-r)**3)) == 0
    assert sp.diff(T, u) == 0


def test_projective_contrast_and_log_score_have_exact_common_velocity_direction():
    r, u, v, s = variables()
    H, _, q, _ = invariants(r, u, v, s)
    assert sp.factor(
        sp.diff(q, u) - q*sp.diff(H, u)/H
    ) == 0


def test_rank_one_information_metric_has_exact_null_direction():
    q, H, gamma = sp.symbols("q H gamma", real=True, nonzero=True)
    G = gamma/H**2*sp.Matrix([[q*q,-q],[-q,1]])
    assert sp.simplify(G.det()) == 0
    assert sp.simplify(G*sp.Matrix([1,q])) == sp.zeros(2,1)
    assert sp.factor(sp.trace(G) - gamma*(1+q*q)/H**2) == 0


def test_full_three_spatial_gradient_contrast_has_no_time_velocity():
    r, u, s = sp.symbols("r u s",real=True, nonzero=True)
    x,y,z=sp.symbols("x y z",real=True)
    w=x*x+y*y+z*z
    k=w-u*u
    H=8*s*s*r*(1-r)/k
    J=64*s**4*r**3*w/k**3
    T=sp.factor(4*J/H**3)
    assert sp.factor(T-w/(2*s*s*(1-r)**3))==0
    assert sp.diff(T,u)==0


def test_mixed_second_jets_remain_but_ddot_r_does_not():
    r,u,v,s=variables()
    rtt, rtx, rxx=sp.symbols("rtt rtx rxx",real=True)
    _,_,_,T=invariants(r,u,v,s)
    dt=sp.diff(T,r)*u+sp.diff(T,u)*rtt+sp.diff(T,v)*rtx
    dx=sp.diff(T,r)*v+sp.diff(T,u)*rtx+sp.diff(T,v)*rxx
    t_expected=v*rtx/(s*s*(1-r)**3)+3*v*v*u/(2*s*s*(1-r)**4)
    x_expected=v*rxx/(s*s*(1-r)**3)+3*v**3/(2*s*s*(1-r)**4)
    assert sp.factor(dt-t_expected)==0
    assert sp.factor(dx-x_expected)==0
    assert sp.diff(dt,rtt)==0
    assert sp.diff(dx,rtt)==0


def test_degenerate_lagrangian_acceleration_hessian_is_identically_zero():
    r,u,v,s=variables()
    rtt,rtx,rxx,gamma=sp.symbols("rtt rtx rxx gamma",real=True)
    _,_,_,T=invariants(r,u,v,s)
    dt=sp.diff(T,r)*u+sp.diff(T,u)*rtt+sp.diff(T,v)*rtx
    dx=sp.diff(T,r)*v+sp.diff(T,u)*rtx+sp.diff(T,v)*rxx
    L=gamma*(dt*dt-dx*dx)/2
    assert sp.diff(L,rtt,2)==0


def test_tilted_ordinary_velocity_hessian_is_positive_coefficient():
    r,u,v,s=variables()
    mix,gamma=sp.symbols("mix gamma",real=True)
    _,_,_,T=invariants(r,u,v,s)
    dt=sp.diff(T,r)*u+sp.diff(T,v)*mix
    dx=sp.diff(T,r)*v+sp.diff(T,v)*sp.symbols("rxx",real=True)
    L=gamma*(dt*dt-dx*dx)/2
    expected=9*gamma*v**4/(4*s**4*(1-r)**8)
    assert sp.factor(sp.diff(L,u,2)-expected)==0
    assert sp.factor(sp.diff(L,u,2).subs({r:-1,v:1,s:1})-9*gamma/1024)==0


def test_homogeneous_branch_starts_at_higher_perturbation_order():
    r,u,v,s=variables()
    _,_,_,T=invariants(r,u,v,s)
    assert T.subs(v,0)==0
    for parameter in (r,u,v):
        assert sp.factor(sp.diff(T,parameter).subs(v,0))==0


def test_frozen_tilted_WKB_principal_polynomial():
    gamma, A, w, k=sp.symbols("gamma A w k",real=True)
    P=sp.factor(gamma*A*A*k*k*(w*w-k*k))
    assert sp.factor(P/(gamma*A*A)-k*k*(w*w-k*k))==0
    assert sp.factor(P.subs(k,0))==0
    assert sp.factor(P.subs(w,k))==0


def test_scalar_score_excludes_any_independent_psi_kinetic():
    r,u,v,s=variables()
    _,_,_,T=invariants(r,u,v,s)
    psi=sp.symbols("psi",real=True)
    assert psi not in T.free_symbols
