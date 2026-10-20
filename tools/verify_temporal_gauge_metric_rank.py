#!/usr/bin/env python3
"""Exact pointwise metric-rank/ADM-projectability audit for radial Theta gauge.

Not an on-shell UBT degree-of-freedom count.  Boost variables are free
first-jet variables only before connection, torsion and field equations.
Requires sympy.
"""
import sympy as sp


def verify_temporal_rank():
    u=sp.symbols("u", real=True)
    w=sp.Matrix(4,3,lambda r,c:sp.Symbol(f"w{r}{c}",real=True))
    e=sp.Matrix.hstack(sp.Matrix([u,0,0,0]),w)
    g=sp.expand(e*sp.diag(-1,1,1,1)*e.T)
    variables=[u]+list(w)
    pairs=[(i,j) for i in range(4) for j in range(i,4)]
    metric_vector=sp.Matrix([g[i,j] for i,j in pairs])
    jac=metric_vector.jacobian(variables)
    at_flat={u:sp.Integer(1)}
    at_flat.update({w[r,c]:int(r==c+1) for r in range(4) for c in range(3)})
    linear=jac.subs(at_flat)
    results={
        "jacobian_ten_by_thirteen":linear.shape==(10,13),
        "pointwise_metric_rank_ten":linear.rank()==10,
        "three_metric_null_rotations":len(linear.nullspace())==3,
    }
    h=sp.Matrix(10,1,lambda i,j:sp.Symbol(f"h{pairs[i][0]}{pairs[i][1]}"))
    inverse={u:-h[pairs.index((0,0))]/2}
    for r in range(4):
        for c in range(3):
            inverse[w[r,c]]=(h[pairs.index((0,c+1))] if r==0
                            else h[pairs.index((r,r))]/2 if r==c+1
                            else h[pairs.index(tuple(sorted((r,c+1))))]/2)
    tangent=sp.Matrix([inverse[v] for v in variables])
    results["all_ten_metric_perturbations_right_inverse"]=(linear*tangent==h)
    for index,(r,c) in enumerate(((1,2),(1,3),(2,3))):
        null=sp.zeros(13,1)
        null[variables.index(w[r,c-1])]=1
        null[variables.index(w[c,r-1])]=-1
        results[f"SO3_rotation_null_{index}"]=(linear*null==sp.zeros(10,1))

    # A homogeneous isotropic ansatz never probes the general ten-parameter map.
    n,a=sp.symbols("n a",positive=True)
    mini=sp.diag(-n*n,a*a,a*a,a*a)
    minivec=sp.Matrix([mini[i,j] for i,j in pairs])
    results["FLRW_minisuperspace_rank_only_two"]=(minivec.jacobian([n,a]).rank()==2)

    # In the specifically auxiliary zero-boost model all spatial columns
    # of e vanish; the emergent metric then has rank one, not ten.
    at_zero=jac.subs({w[r,c]:0 for r in range(4) for c in range(3)}).subs(u,1)
    results["auxiliary_zero_boost_map_rank_one"]=(at_zero.rank()==1)

    # For invertible spatial triad W, beta_i=W_{ij} b_j and
    # gamma_ij=(WW^T)_ij. Thus beta^T gamma^-1 beta=b^T b.
    # With g_00=-u^2+b^T b, N_ADM^2=-g_00+beta^T gamma^-1 beta=u^2.
    W=sp.Matrix(3,3,lambda r,c:sp.Symbol(f"s{r}{c}",real=True))
    b=sp.Matrix(sp.symbols("b0:3",real=True))
    gamma=W*W.T
    shift=W*b
    results["exact_ADM_lapse_squared_equals_u_squared"]=(
        sp.simplify((shift.T*gamma.inv()*shift)[0]-(b.T*b)[0])==0
    )
    # Two-cell miniature of the local-vs-integrated lapse constraint:
    # with one projectable multiplier local residuals may cancel.
    N=sp.symbols("N", positive=True, real=True)
    k0,k1,v0,v1=sp.symbols("k0 k1 v0 v1", real=True)
    l0=k0/N-N*v0
    l1=k1/N-N*v1
    sample={k0:1,k1:1,v0:0,v1:-2,N:1}
    local0=sp.diff(l0,N).subs(sample)
    local1=sp.diff(l1,N).subs(sample)
    results["global_projectable_constraint_not_local_constraint"]=(
        local0!=0 and local1!=0 and sp.simplify(local0+local1)==0
    )
    return results


def main():
    checks=verify_temporal_rank()
    for name,passed in checks.items():
        print(("PASS" if passed else "FAIL")+" "+name)
    if not all(checks.values()):
        raise SystemExit(1)
    print("PASS all",len(checks),"conditional first-jet identities")


if __name__=="__main__":
    main()
