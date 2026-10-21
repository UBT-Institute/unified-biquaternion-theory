#!/usr/bin/env python3
"""Conditional torsion-free vacuum rigidity for a timelike single-Theta coframe.

If e^a=D_omega X^a/q, omega is torsion-free and X is nonzero timelike,
the tetrad postulate yields nabla_mu X^nu=delta_mu^nu. Therefore
R^rho_(sigma mu nu) X^sigma=0. In the local rest frame of X all
R_(ab c0) components vanish. Remaining curvature is a symmetric
3x3 spatial-bivector block (six components); Ricci=0 forces this block
to vanish. Ricci=Lambda*g further requires Lambda=0.

A standard Ricci-flat TT linear wave has electric R_(0i0j)!=0 and is
excluded from the *torsion-free parent Einstein shell*, NOT excluded
from the full composite equations allowing torsion and E_a!=0.
The Lorentz bivector Hodge star satisfies star^2=-1 and real
Palatini/Holst quadratic map has determinant (cH²+cEC²)^3.
"""
import sympy as sp


def verify():
    signature=sp.diag(-1,1,1,1)
    pairs=[(i,j) for i in range(4) for j in range(i+1,4)]
    spatial=list(range(3,6))
    values=sp.symbols("R00 R01 R02 R11 R12 R22",real=True)
    block=sp.zeros(6)
    n=0
    for i in spatial:
        for j in spatial:
            if j>=i:
                block[i,j]=values[n]
                block[j,i]=values[n]
                n+=1
    indices={pair:i for i,pair in enumerate(pairs)}
    def R(a,b,c,d):
        if a==b or c==d:return sp.S.Zero
        parity=(-1 if a>b else 1)*(-1 if c>d else 1)
        return parity*block[
            indices[tuple(sorted((a,b)))],
            indices[tuple(sorted((c,d)))]]
    ricci=sp.Matrix(4,4,lambda b,d:sp.expand(sum(
        signature[a,a]*R(a,b,a,d) for a in range(4))))
    equations=[ricci[i,j] for i in range(1,4) for j in range(i,4)]
    A,_=sp.linear_eq_to_matrix(equations,values)
    checks={}
    checks["vacuum_spatial_Ricci_six_by_six_full_rank"]=A.shape==(6,6) and A.rank()==6
    checks["Ricci_flat_forces_all_spatial_curvature_zero"]=len(A.nullspace())==0
    checks["Riemann_annihilates_rest_frame_timelike_X"]=all(
        R(a,b,c,0)==0 for a in range(4) for b in range(4)
        for c in range(4))
    checks["temporal_Ricci_is_zero"]=ricci[0,0]==0
    lam=sp.symbols("Lambda",real=True)
    checks["nonzero_Einstein_Lambda_cannot_be_concurrent"]=(
        sp.simplify(ricci[0,0]-lam*signature[0,0])==lam)
    checks["spatial_curvature_Ricci_determinant_nonzero"]=sp.simplify(A.det())!=0
    checks["remaining_Riemann_obeys_algebraic_Bianchi"]=all(
        sp.simplify(R(a,b,c,d)+R(a,c,d,b)+R(a,d,b,c))==0
        for a in range(4) for b in range(4)
        for c in range(4) for d in range(4))

    star=sp.Matrix([
        [sp.LeviCivita(*ab,*cd)*signature[cd[0],cd[0]]*
         signature[cd[1],cd[1]] for cd in pairs]
        for ab in pairs])
    ce,ch=sp.symbols("c_EC c_H",real=True)
    checks["Lorentzian_Hodge_star_squared_minus_identity"]=star**2==-sp.eye(6)
    checks["real_Einstein_Cartan_Holst_internal_operator_nondegenerate"]=(
        sp.factor((ch*sp.eye(6)+ce*star).det())==(ch**2+ce**2)**3)

    # A conventional plus-polarized vacuum gravitational wave
    # h_xx=-h_yy=A cos[k(t-z)] is Ricci flat but not Riemann flat.
    t,z,k,ampl=sp.symbols("t z k amplitude",real=True)
    xyz=[t,sp.Symbol("x"),sp.Symbol("y"),z]
    phase=k*(t-z)
    h=sp.zeros(4)
    h[1,1]=ampl*sp.cos(phase)
    h[2,2]=-ampl*sp.cos(phase)
    def RL(a,b,c,d):
        return sp.simplify((sp.diff(h[a,d],xyz[c],xyz[b])
            +sp.diff(h[b,c],xyz[d],xyz[a])
            -sp.diff(h[a,c],xyz[d],xyz[b])
            -sp.diff(h[b,d],xyz[c],xyz[a]))/2)
    rict=sp.Matrix(4,4,lambda b,d:sp.simplify(sum(
        signature[a,a]*RL(a,b,a,d) for a in range(4))))
    checks["standard_TT_plane_wave_linearized_Ricci_zero"]=rict==sp.zeros(4)
    checks["standard_TT_plane_wave_electric_Riemann_nonzero"]=(
        sp.simplify(RL(0,1,0,1)-ampl*k**2*sp.cos(phase)/2)==0)
    checks["standard_TT_other_transverse_polarization_opposite"]=(
        sp.simplify(RL(0,2,0,2)+ampl*k**2*sp.cos(phase)/2)==0)

    q=sp.symbols("q",positive=True)
    X=q*sp.Matrix([t,xyz[1],xyz[2],z])
    checks["affine_flat_composite_representer_has_timelike_open_region"]=(
        sp.expand((X.T*signature*X)[0]
            -q**2*(-t**2+xyz[1]**2+xyz[2]**2+z**2))==0)
    return checks


if __name__=="__main__":
    out=verify()
    for name,passed in out.items():
        print(("PASS " if passed else "FAIL ")+name)
    print(f"{sum(out.values())}/{len(out)} exact checks passed")
    if not all(out.values()):raise SystemExit(1)
