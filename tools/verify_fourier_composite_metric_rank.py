#!/usr/bin/env python3
"""Exact Fourier first-jet metric reachability on a timelike Lorentz-real branch.

This is the symbol of the COMPOSITE FIELD-TO-METRIC MAP, NOT the
Euler-Lagrange/Dirac principal symbol of an UBT action.

At a locally flat nondegenerate coframe e_mu^a=delta_mu^a and a point
with X^a=(r,0,0,0), r>0, q=sqrt(N0)>0:
 delta e_mu^0 = k_mu xi^0/q,
 delta e_mu^i = (k_mu xi^i+r beta_mu^i)/q.
The 12 rotations of omega annihilate X. Real Fourier momenta have
their common imaginary unit suppressed because rank is unaffected.

Nonzero temporal frequency k0: metric Jacobian 10, coframe 13.
Exactly static k0=0: metric Jacobian 9, coframe still 13 for k!=0.
Uniform k=0: metric 9, coframe 12.
The missing exactly static metric mode is h00. This does NOT forbid
static physical metrics from time-dependent field representatives and
does not prove the full field equations lose their normal constraint.
"""
import sympy as sp


def verify():
    q,r=sp.symbols("q r",nonzero=True,real=True)
    k=sp.symbols("k0:4",real=True)
    xi=sp.symbols("xi0:4",real=True)
    boosts=sp.symbols("b0:12",real=True)
    rotations=sp.symbols("rot0:12",real=True)
    variables=(*xi,*boosts,*rotations)
    eta=sp.diag(-1,1,1,1)
    de=sp.Matrix(4,4,lambda mu,a:
        (k[mu]*xi[a]+(r*boosts[3*mu+a-1] if a else 0))/q)
    dg=de*eta+eta*de.T
    metric=sp.Matrix([dg[i,j] for i in range(4) for j in range(i,4)])
    jm=metric.jacobian(variables)
    je=sp.Matrix(list(de)).jacobian(variables)
    checks={}
    checks["metric_is_symmetric"]=dg==dg.T
    checks["Fourier_metric_Jacobian_10x28"]=jm.shape==(10,28)
    checks["Fourier_tetrad_Jacobian_16x28"]=je.shape==(16,28)
    checks["rotations_do_not_change_composite_tetrad"]=all(
        je[:,j]==sp.zeros(16,1) for j in range(16,28))
    configurations={
        "temporal":(1,0,0,0),
        "static_spatial":(0,1,2,0),
        "null":(1,1,0,0),
        "zero":(0,0,0,0)}
    ranks={}
    for label,kk in configurations.items():
        values={**dict(zip(k,kk)),q:1,r:1}
        ranks[label]=(jm.subs(values).rank(),je.subs(values).rank())
    checks["time_dependent_metric_rank_ten"]=ranks["temporal"][0]==10
    checks["null_mode_metric_rank_ten"]=ranks["null"][0]==10
    checks["strictly_static_metric_rank_nine"]=ranks["static_spatial"][0]==9
    checks["static_tetrad_rank_thirteen"]=ranks["static_spatial"][1]==13
    checks["time_dependent_tetrad_rank_thirteen"]=ranks["temporal"][1]==13
    checks["zero_momentum_metric_rank_nine"]=ranks["zero"][0]==9
    checks["zero_momentum_tetrad_rank_twelve"]=ranks["zero"][1]==12
    checks["static_missing_component_is_h00"]=(
        jm.subs({k[0]:0})[0,:]==sp.zeros(1,28))
    checks["exact_metric_clock_constraint"]=(
        sp.simplify(dg[0,0]+2*k[0]*xi[0]/q)==0)
    # Construct explicit right-inverse of the metric symbol at k0 != 0.
    h=sp.Matrix(4,4,lambda i,j:sp.Symbol(f"h{min(i,j)}{max(i,j)}"))
    chosen={xi[0]:-q*h[0,0]/(2*k[0])}
    chosen.update({xi[i]:0 for i in (1,2,3)})
    chosen.update({v:0 for v in (*boosts,*rotations)})
    for i in (1,2,3):
        chosen[boosts[i-1]]=(q*h[0,i]+k[i]*chosen[xi[0]])/r
        chosen[boosts[3*i+i-1]]=q*h[i,i]/(2*r)
    for i in (1,2,3):
        for j in range(i+1,4):
            chosen[boosts[3*i+j-1]]=q*h[i,j]/r
    checks["right_inverse_for_nonzero_frequency"]=all(
        sp.simplify(v)==0 for v in (dg.subs(chosen)-h))
    # For static fields, h00 vanishes; the remaining nine metric
    # directions are freely realized, including shift and spatial shear.
    static={**chosen,xi[0]:0}
    for i in (1,2,3):
        static[boosts[i-1]]=q*h[0,i]/r
    checks["static_all_other_nine_metric_modes_reachable"]=all(
        sp.simplify(v)==0 for v in
        (dg.subs(static).subs(k[0],0)-h.subs(h[0,0],0)))
    checks["static_spatial_left_null_dim_one"]=(
        len(jm.subs({**dict(zip(k,(0,1,0,0))),q:1,r:1})
            .T.nullspace())==1)
    return checks


if __name__=="__main__":
    checks=verify()
    for name,ok in checks.items():print(("PASS " if ok else "FAIL ")+name)
    print("TOTAL",len(checks),"PASSED",sum(checks.values()))
    if not all(checks.values()):raise SystemExit(1)
