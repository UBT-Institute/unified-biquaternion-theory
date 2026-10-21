#!/usr/bin/env python3
"""Exact first-variation chain-rule certificate for composite radial Theta tetrad.

S[e, boost, rho] is a *generic* independent-tetrad parent action.
e0=d(rho)/sqrt(N0), ei=rho*b_i/sqrt(N0).  The reduced connection
equation contains E_i*rho/sqrt(N0), i.e. it is not simply Cartan C_i=0.
A 0+1 dimensional polynomial toy density verifies both Euler derivatives.
No candidate fundamental UBT action is finalized by this identity.
"""
import sympy as sp


def verify_composite_variation_chain() -> dict[str,bool]:
    t=sp.symbols("t",real=True)
    q=sp.symbols("q",positive=True) # q=sqrt(N0)
    rho=sp.Function("rho")(t)
    b=[sp.Function(f"b{i}")(t) for i in range(3)]
    e=sp.symbols("e0:4")
    phi=sp.symbols("phi",real=True)
    lam=sp.symbols("lam",real=True)
    U=sp.Function("U")
    # Parent Lagrangian in independent variables. The explicit boost
    # term is the Cartan "direct" contribution at fixed tetrad.
    Lparent=U(phi)*sp.prod(e)+lam*b[0]**2
    E=[sp.diff(Lparent,z) for z in e]
    C=[sp.diff(Lparent,z) for z in b]
    Erho=sp.diff(Lparent,phi)
    replacement={
        e[0]:sp.diff(rho,t)/q,
        e[1]:rho*b[0]/q,
        e[2]:rho*b[1]/q,
        e[3]:rho*b[2]/q,
        phi:rho
    }
    Lcomp=Lparent.subs(replacement)
    results={}
    for i in range(3):
        lhs=sp.diff(Lcomp,b[i])
        rhs=(C[i]+rho*E[i+1]/q).subs(replacement)
        results[f"boost_chain_rule_{i}"]=sp.simplify(lhs-rhs)==0
    # Functional derivative of rho includes integrated-by-parts
    # derivative of E0 from exact d(rho) coframe component.
    euler=sp.diff(Lcomp,rho)-sp.diff(sp.diff(Lcomp,sp.diff(rho,t)),t)
    right=(Erho
           +sum(b[i]*E[i+1]/q for i in range(3))
           -sp.diff(E[0].subs(replacement)/q,t))
    right=right.subs(replacement)
    results["scalar_Euler_chain_rule_with_total_derivative"]=(
        sp.simplify(sp.expand(euler-right))==0
    )
    # In particular, even when independent Cartan C_b=0, a nonzero
    # tetrad variation E_i drives a nonzero composite connection eq.
    simple_b=sp.symbols("b",real=True)
    simple_e=sp.symbols("e",real=True)
    Ltoy=simple_e**2/2 # no direct b term, so C_b=0
    composed=Ltoy.subs(simple_e,rho*simple_b/q)
    results["composite_boost_variation_not_Cartan_alone"]=(
        sp.diff(Ltoy,simple_b)==0
        and sp.simplify(sp.diff(composed,simple_b)
                        -rho**2*simple_b/q**2)==0
    )
    return results


def main():
    checks=verify_composite_variation_chain()
    for name,ok in checks.items():
        print(("PASS" if ok else "FAIL")+" "+name)
    if not all(checks.values()):raise SystemExit(1)
    print("PASS",len(checks),"composite functional-chain checks")


if __name__=="__main__":
    main()
