#!/usr/bin/env python3
"""Exact Lorentz/phase invariant vector-tensor-bivector potential audit.

For X=(u+i v)^mu sigma_mu, u and v transform as real Lorentz
four-vectors, while the existing U(1) phase rotates them as a doublet.
Show that the natural bivector B=u wedge v is phase-neutral but its
degree-four scalar is already a linear combination of H(X)^2 and
|det X|^2, the canonical invariant-potential basis.

Mathematical classification at quartic/derivative-free level ONLY.
No claim that derivative/curvature/torsion couplings are redundant.
"""
import sympy as sp


def verify_bivector_potential() -> dict[str,bool]:
    u=sp.symbols("u0:4",real=True)
    v=sp.symbols("v0:4",real=True)
    eta=[1,-1,-1,-1]
    q=lambda z:sum(eta[i]*z[i]**2 for i in range(4))
    p=sum(eta[i]*u[i]*v[i] for i in range(4))
    Qu,Qv=q(u),q(v)
    H=2*(Qu+Qv)
    absdet2=(Qu-Qv)**2+4*p**2
    biv={(i,j):u[i]*v[j]-u[j]*v[i] for i in range(4) for j in range(i+1,4)}
    B2=2*sum(eta[i]*eta[j]*b**2 for (i,j),b in biv.items())
    results={}
    results["canonical_quartic_bivector_identity"]=(
        sp.expand(B2-H**2/sp.Integer(8)+absdet2/sp.Integer(2))==0
    )
    results["bivector_is_simple_Plucker_identity"]=(
        sp.expand(biv[0,1]*biv[2,3]-biv[0,2]*biv[1,3]
                  +biv[0,3]*biv[1,2])==0
    )
    # Re+Im phase rotation u' = c u-s v, v' = s u+c v
    c,s=sp.Rational(3,5),sp.Rational(4,5)
    pu=[c*u[i]-s*v[i] for i in range(4)]
    pv=[s*u[i]+c*v[i] for i in range(4)]
    results["bivector_phase_U1_neutral"]=all(
        sp.expand(pu[i]*pv[j]-pu[j]*pv[i]-b)==0
        for (i,j),b in biv.items()
    )
    results["H_phase_U1_invariant"]=sp.expand(
        2*(q(pu)+q(pv))-H)==0
    # Symmetric phase-neutral rank-two tensor:
    # S_{mu nu}=u_mu u_nu+v_mu v_nu
    Strace=Qu+Qv
    Ssquared=Qu**2+Qv**2+2*p**2
    results["symmetric_tensor_trace_is_existing_quadratic"]=(
        sp.expand(Strace-H/2)==0
    )
    results["symmetric_tensor_square_is_existing_quartic"]=(
        sp.expand(Ssquared-H**2/sp.Integer(8)
                  -absdet2/sp.Integer(2))==0
    )
    # The entire timelike Hermitian radial orbit uses a single
    # real 4-vector (u=0 or v=0), hence its bivector is zero.
    zero_u={z:0 for z in u}
    results["Hermitian_timelike_slice_bivector_zero"]=all(
        sp.expand(b.subs(zero_u))==0 for b in biv.values()
    )
    results["first_variation_of_B2_zero_at_timelike_slice"]=all(
        sp.expand(sp.diff(B2,z).subs(zero_u))==0 for z in (*u,*v)
    )
    # At X=i r I, B^2=-2 r^2[(delta u1)^2+...]
    # to quadratic order; this can change transverse mass terms
    # but NOT the background equations, and it is already in V4.
    r=sp.symbols("r",positive=True)
    bg={**{u[i]:0 for i in range(4)},
        v[0]:r,**{v[i]:0 for i in range(1,4)}}
    variables=[*u,*v]
    hessian=sp.hessian(B2,variables).subs(bg)
    expected=sp.diag(0,-4*r*r,-4*r*r,-4*r*r,0,0,0,0)
    results["bivector_quadratic_transverse_Hessian"]=(
        hessian==expected
    )
    # One real Lorentz vector gives identically zero wedge.
    results["one_fourvector_cannot_make_bivector"]=all(
        sp.expand(u[i]*u[j]-u[j]*u[i])==0
        for i in range(4) for j in range(i+1,4)
    )
    return results


if __name__=="__main__":
    checks=verify_bivector_potential()
    for key, ok in checks.items():
        print(("PASS" if ok else "FAIL"),key)
    if not all(checks.values()):
        raise SystemExit(1)
    print(f"PASS all {len(checks)} exact quartic/bivector identities")
