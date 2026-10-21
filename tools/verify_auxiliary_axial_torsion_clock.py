#!/usr/bin/env python3
"""Exact auxiliary trace/axial torsion elimination and normal-clock obstruction.

Scope: first-order metric-compatible *independent-field comparator*:
Laux = sqrt(-g)[ 1/2 ct t² + beta t.A + 1/2 ca A²
                   + f(r) dr.t + h(r) dr.A].
On the nondegenerate positive-Hermitian single-Theta clock branch,
g^-1(dr,dr)=-N0. With det K !=0, eliminating algebraic auxiliary
torsion gives a pure potential W(r) (no new lapse constraint).
This does NOT prove an on-shell result for the complete composite UBT
connection, whose variation also changes e=DTheta/sqrt(N0).

External parity requirements: beta is a pseudoscalar or explicit parity
breaking; h(r) dr is a pseudovector source only if h has appropriate
pseudoscalar transformation. No new axion is constructed.
"""
from __future__ import annotations
import sympy as sp


def verify_auxiliary_torsion_no_normal_constraint():
    ct,ca,be,f,h,q=sp.symbols("ct ca beta f h q", real=True,nonzero=True)
    t,a=sp.symbols("t a",real=True)
    K=sp.Matrix([[ct,be],[be,ca]])
    J=sp.Matrix([f,h])
    vec=sp.Matrix([t,a])
    delta=ct*ca-be**2
    L=sp.expand(sp.Rational(1,2)*(vec.T*K*vec)[0]+(J.T*vec)[0])
    sol=-sp.simplify(K.inv()*J)
    checks={}
    checks["torsion_algebraic_Hessian"]=sp.hessian(L,(t,a))==K
    checks["torsion_Hessian_determinant"]=sp.simplify(sp.det(K)-delta)==0
    checks["torsion_equations_solved"]=all(
        sp.simplify(eq.subs({t:sol[0],a:sol[1]}))==0
        for eq in [sp.diff(L,t),sp.diff(L,a)])
    quadratic_on_shell=sp.factor(L.subs({t:sol[0],a:sol[1]}))
    expected=-(ca*f**2-2*be*f*h+ct*h**2)/(2*delta)
    checks["complete_square_exact"]=sp.simplify(quadratic_on_shell-expected)==0

    # The actual fields are one-forms; sol multiplies dr. Since
    # g^-1(dr,dr)=-q², elimination yields purely scalar W(r).
    W=sp.simplify(-q**2*quadratic_on_shell)
    expectedW=q**2*(ca*f**2-2*be*f*h+ct*h**2)/(2*delta)
    checks["unit_clock_elimination_yields_potential_only"]=sp.simplify(W-expectedW)==0

    # Explicit nontrivial axial torsion with nonzero trace current;
    # the effective term remains a potential (no new normal equation).
    values={ct:2,ca:3,be:1,f:2,h:0}
    checks["explicit_mixed_axial_solution"]=(
        sp.simplify(sol[0].subs(values)+sp.Rational(6,5))==0
        and sp.simplify(sol[1].subs(values)-sp.Rational(2,5))==0)
    checks["explicit_pure_clock_effective_value"]=(
        sp.simplify(W.subs(values)-sp.Rational(6,5)*q**2)==0)
    checks["axial_vanishes_when_no_mixing_or_axial_source"]=(
        sp.simplify(sol[1].subs({be:0,h:0}))==0)
    checks["no_current_nonsingular_torsion_vanishes"]=(
        sp.simplify(sol.subs({f:0,h:0}))==sp.zeros(2,1))

    # Singular det K case: a source must be orthogonal to the kernel.
    ct0,ca0,be0=sp.symbols("ct0 ca0 be0",nonzero=True,real=True)
    Ksing=sp.Matrix([[ct0,be0],[be0,be0**2/ct0]])
    null=sp.Matrix([be0,-ct0])
    checks["singular_Hessian_null_vector"]=Ksing*null==sp.zeros(2,1)
    checks["singular_source_compatibility_condition"]=sp.expand(
        (null.T*J)[0]-(be0*f-ct0*h))==0
    checks["singular_compatible_underdetermined_example"]=(
        Ksing.subs({ct0:2,be0:2}).rank()==1
        and (Ksing.subs({ct0:2,be0:2})*sp.Matrix([1,-1])==sp.zeros(2,1))
    )

    # Exact conservation source: a³*lambda has a freely set initial
    # value even if source is a fixed scalar function of the clock.
    z,t0,t1=sp.symbols("z t0 t1",real=True)
    af=sp.Function("scale")
    src=sp.Function("src")
    free=sp.symbols("lambda_initial",real=True)
    lam=(free-sp.Rational(1,2)*q*sp.Integral(
        af(z)**3*src(z),(z,t0,t1)))/af(t1)**3
    checks["sourced_clock_current_preserves_free_initial_value"]=(
        sp.simplify(sp.diff(af(t1)**3*lam,t1)
                    +q*af(t1)**3*src(t1)/2)==0)
    checks["sourced_clock_current_initial_constant_is_free"]=(
        sp.simplify(sp.diff(lam,free)-af(t1)**(-3))==0)
    return checks


if __name__=="__main__":
    tests=verify_auxiliary_torsion_no_normal_constraint()
    for k,v in tests.items():
        print(("PASS" if v else "FAIL"),k)
    if not all(tests.values()):
        raise SystemExit(1)
    print(f"PASS {len(tests)} exact restricted torsion/clock identities")
