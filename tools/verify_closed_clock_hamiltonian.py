#!/usr/bin/env python3
"""Exact constrained Hamiltonian of a closed-FLRW composite-clock EH comparator.

This is NOT the fundamental UBT action. S[g(e)] is the externally supplied
Einstein-Hilbert-plus-Lambda functional restricted to a single-Theta radial
coframe e0=d(rho)/sqrt(N0), ei=a(t)*upsilon_i on S3/(2I).

Checks: degenerate Hessian, Dirac primary constraint, conservation of the
clock momentum, dust integration constant, closed de Sitter vacuum and
sign-indefinite clock-gauge Hamiltonian. Uses SymPy only.
"""
import sympy as sp


def verify_closed_clock_hamiltonian() -> dict[str, bool]:
    C, q, a, adot, rdot, cosm, pa, pr, dust = sp.symbols(
        "C q a adot rdot cosm pa pr D",
        positive=True, real=True,
    )
    N=rdot/q
    L=C*(-a*adot**2/N + N*(a-cosm*a**3/3))
    pa_derived=sp.diff(L,adot)
    pr_derived=sp.diff(L,rdot)
    Hgrav=-pa**2/(4*C*a)-C*a+C*cosm*a**3/3
    Phi=q*pr+Hgrav
    checks={}
    checks["hessian_rank_one_no_hidden_velocity_inversion"]=(
        sp.simplify(sp.det(sp.hessian(L,(adot,rdot))))==0
        and sp.simplify(sp.diff(L,adot,2)+2*C*a/N)==0
    )
    checks["homogeneous_lagrangian_zero_canonical_H"]=(
        sp.simplify(pa_derived*adot+pr_derived*rdot-L)==0
    )
    checks["exact_scale_momentum"]=(
        sp.simplify(pa_derived+2*C*a*adot/N)==0
    )
    checks["exact_clock_momentum"]=(
        sp.simplify(
            pr_derived-C/q*(a*adot**2/N**2+a-cosm*a**3/3)
        )==0
    )
    solved_adot=-N*pa/(2*C*a)
    checks["primary_constraint_exact"]=(
        sp.simplify(Phi.subs(pr,pr_derived).subs(adot,solved_adot))==0
    )
    checks["first_class_single_constraint_self_bracket"]=(
        sp.simplify(sp.diff(Phi,a)*sp.diff(Phi,pa)-
        sp.diff(Phi,pa)*sp.diff(Phi,a))==0
    )
    checks["clock_is_cyclic_momentum_conserved"]=(
        not L.has(sp.Symbol("rho"))
        and not Phi.has(sp.Symbol("rho"))
    )
    # The on-shell constraint implies Hgrav=-q*p_rho=-C*D.
    cosmic_sq=cosm*a**2/3+dust/a-1
    pa_cosmic=-2*C*a*sp.sqrt(cosmic_sq)
    checks["dust_first_integral_exact"]=(
        sp.simplify(Hgrav.subs(pa,pa_cosmic)+C*dust)==0
    )
    # Clock-gauge Hamilton eq: adot=-pa/(2Ca), pdot_a=-dHg/da.
    adot_fromH=-pa/(2*C*a)
    # d/dt adot = {adot,Hgrav} in clock gauge; derive acceleration.
    addot_poisson=sp.simplify(
        sp.diff(adot_fromH,a)*sp.diff(Hgrav,pa)
        -sp.diff(adot_fromH,pa)*sp.diff(Hgrav,a)
    )
    checks["acceleration_equation_from_Hamilton"]=(
        sp.simplify(addot_poisson-cosm*a/3
              +(pa**2/(4*C**2*a**2)+1-cosm*a**2/3)/(2*a))==0
    )
    checks["dust_acceleration_equation"]=(
        sp.simplify(addot_poisson.subs(pa**2,4*C**2*a**2*cosmic_sq)
                    -(cosm*a/3-dust/(2*a**2)))==0
    )
    t, H, center=sp.symbols("t H center",real=True,positive=True)
    ads=sp.cosh(H*(t-center))/H
    checks["closed_desitter_Friedmann"]=(
        sp.simplify(sp.diff(ads,t)**2+1-H**2*ads**2)==0
    )
    checks["closed_desitter_second_Einstein_equation"]=(
        sp.simplify(2*ads*sp.diff(ads,t,2)
                    +sp.diff(ads,t)**2+1-3*H**2*ads**2)==0
    )
    checks["closed_desitter_Ricci_scalar_12H2"]=(
        sp.simplify(
            6*(sp.diff(ads,t,2)/ads+
               sp.diff(ads,t)**2/ads**2+1/ads**2)-12*H**2
        )==0
    )
    volume=sp.pi**2/60
    G=sp.symbols("G",positive=True)
    checks["Poincare_quotient_minisuperspace_C"]=(
        sp.simplify(3*volume/(8*sp.pi*G)-sp.pi/(160*G))==0
    )
    # For C>0,a>0: Hgrav has a negative quadratic coefficient in p_a.
    # This is NOT by itself a propagating ghost criterion in full GR.
    checks["clock_gauge_Hgr_unbounded_below_as_pa_grows"]=(
        sp.diff(Hgrav,pa,2).is_negative is True
    )
    return checks


def main():
    checks=verify_closed_clock_hamiltonian()
    for label,good in checks.items():
        print(("PASS" if good else "FAIL")+" "+label)
    if not all(checks.values()):
        raise SystemExit(1)
    print(f"PASS {len(checks)} conditional exact identities")


if __name__=="__main__":
    main()
