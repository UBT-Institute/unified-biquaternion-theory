#!/usr/bin/env python3
"""Exact restricted scalar-curvature/torsion matching identities.

This is a standard independent metric-compatible Einstein-Cartan scalar-
tensor comparator, NOT a derivation of the fundamental UBT action.
Requires SymPy. Convention T^l_(m,n)=Gamma^l_(m,n)-Gamma^l_(n,m),
t_m=T^n_(m,n), signature (-+++), and Riemann convention stated in notes.
"""
from __future__ import annotations
import sympy as sp


def verify_trace_torsion_bridge() -> dict[str, bool]:
    checks: dict[str, bool] = {}
    x = sp.symbols("x", real=True)
    tau = sp.Function("trace_t")(x)
    flat = sp.diag(-1, 1, 1, 1)
    t_lower = sp.Matrix([tau, 0, 0, 0])
    t_upper = flat.inv() * t_lower

    def k(lam: int, mu: int, nu: int):
        return sp.simplify(
            (flat[mu, nu] * t_upper[lam] -
             (1 if lam == mu else 0)*t_lower[nu])/3)

    checks["metric_compatibility"] = all(
        sp.simplify(flat[l, l]*k(l,m,n) + flat[n,n]*k(n,m,l))==0
        for l in range(4) for m in range(4) for n in range(4))
    checks["torsion_trace_convention"] = all(
        sp.simplify(sum(k(n,mu,n)-k(n,n,mu) for n in range(4))
                    -t_lower[mu]) == 0
        for mu in range(4))

    def derivative(v: sp.Expr, coord: int):
        return sp.diff(v,x) if coord==0 else sp.S.Zero

    # Calculate scalar R(gamma) directly from the complete connection
    # Gamma=K in inertial Minkowski coordinates (Levi-Civita=0).
    Ric = sp.Matrix(4,4,lambda m,n: sp.expand(
        sum(derivative(k(l,n,m),l)-derivative(k(l,l,m),n)
        +sum(k(l,l,j)*k(j,n,m)-k(l,n,j)*k(j,l,m)
             for j in range(4)) for l in range(4))
    ))
    scalar=sp.simplify(sp.trace(flat.inv()*Ric))
    div_t=-sp.diff(tau,x)
    t_sq=-tau**2
    checks["ricci_scalar_from_direct_affine_curvature"] = (
        sp.simplify(scalar-2*div_t+sp.Rational(2,3)*t_sq)==0)
    checks["explicit_curvature_difference"] = (
        sp.simplify(scalar-(sp.Rational(2,3)*tau**2-2*sp.diff(tau,x)))==0)

    # After integrating 2F divergence(t) by parts, the trace-dependent
    # Lagrangian is -2 gradF dot t - (2/3)F t_m t^m.
    F, Fdot, tracevar=sp.symbols("F Fdot tracevar",real=True,nonzero=True)
    Ltrace=2*Fdot*tracevar+sp.Rational(2,3)*F*tracevar**2
    t_on_shell=-sp.Rational(3,2)*Fdot/F
    checks["connection_Euler_equation_and_trace_solution"] = (
        sp.simplify(sp.diff(Ltrace,tracevar).subs(tracevar,t_on_shell))==0)
    checks["eliminated_torsion_conformal_kinetic_coefficient"] = (
        sp.simplify(Ltrace.subs(tracevar,t_on_shell)
                    +sp.Rational(3,2)*Fdot**2/F)==0)

    # Curved FLRW gamma and time-dependent t_0 only; 3H dilution:
    H=sp.symbols("H",real=True)
    Ftime=sp.Function("Ftime")(x)
    tstar=-sp.Rational(3,2)*sp.diff(Ftime,x)/Ftime
    # t0=3(H-1/V) in the canonical FLRW representer.
    V=sp.symbols("V",positive=True)
    checks["UBT_trace_matching_equation"] = (
        sp.simplify((3*(H-1/V)-tstar)
            .subs(H,1/V-sp.diff(Ftime,x)/(2*Ftime)))==0
    )
    a=sp.Function("a")(x)
    integrated_factor=Ftime*a**2/V**2
    # Along the chosen representation V=x and H=a'/a, the condition
    # H=1/V-F'/2F is exactly d/dV [F*a^2/V^2]=0.
    d_integral=sp.diff(integrated_factor,x).subs(x,V)
    log_eq=(sp.diff(a,x)/a-1/x
            +sp.diff(Ftime,x)/(2*Ftime))
    checks["trace_matching_exact_integrating_factor"] = (
        sp.simplify(sp.diff(Ftime*a**2/x**2,x)
                    -2*Ftime*a**2/x**2*log_eq)==0
    )

    # For F(V)=F0+beta*V^2, beta=xi*N0, the selected a(V) is
    # nonaccelerating if F0,beta,C,V positive.
    v0, ff0, beta, cc=sp.symbols("v0 F0 beta C",positive=True)
    scale=cc*v0/sp.sqrt(ff0+beta*v0**2)
    checks["positive_quadratic_F_has_negative_cosmic_acceleration"] = (
        sp.simplify(sp.diff(scale,v0,2)
             +3*cc*ff0*beta*v0/(ff0+beta*v0**2)**sp.Rational(5,2))==0)
    checks["pure_quadratic_F_yields_constant_scale"] = (
        sp.simplify(scale.subs(ff0,0)-cc/sp.sqrt(beta))==0)

    # Pure curvature comparator transforms (up to divergence)
    # to EH with hbar=F*g: no independent F kinetic in that frame.
    # A generic potential becomes U/F^2 and supplies an algebraic
    # scalar equation, not an independently derived perturbation.
    rho=sp.symbols("rho",positive=True)
    Fr=sp.Function("Fr")(rho)
    Ur=sp.Function("Ur")(rho)
    Einstein_potential=Ur/Fr**2
    checks["Einstein_frame_scalar_potential_variation"] = (
        sp.simplify(sp.diff(Einstein_potential,rho)
        -(sp.diff(Ur,rho)*Fr-2*Ur*sp.diff(Fr,rho))/Fr**3)==0)
    return checks


def main() -> None:
    checks=verify_trace_torsion_bridge()
    for k,ok in checks.items():
        print(("PASS" if ok else "FAIL")+" "+k)
    if not all(checks.values()):
        raise SystemExit(1)
    print(f"PASS {len(checks)} exact restricted comparison identities")


if __name__ == "__main__":
    main()
