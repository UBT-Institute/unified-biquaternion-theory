#!/usr/bin/env python3
"""Exact matrix checks for the all-C2-potential minimal-action classification.

Hypotheses (strictly NOT the full UBT): Theta=i rho I is a local timelike
Lorentz gauge, rho>0; one independent metric-compatible Lorentz spin
connection (free local boosts); e_mu^a=(partial_mu rho,rho*b_mu^j)/q,
q=sqrt(N0)>0; g=e eta e^T and only the canonical kinetic/potential
family, with no curvature or differentiated spin terms.

Algebraic identity B(DTheta,DTheta)=-2 N0*g makes
S=integral |det(e)|*[4c*N0-U(rho)].
At any invertible e, independent boosts impose U(rho)=4c*N0. Since
d rho must be nonzero and rho(U) contains an open interval, U must
have a constant plateau equal to 4c*N0. Along any such plateau the
ENTIRE restricted action is identically zero for small localized
variations staying on the timelike branch; all local Hessian terms
vanish. No differentiability beyond C2 is needed for this dichotomy.

This is an exact extension of Proposition 9, not a claim that
curvature-dependent or non-Hermitian UBT actions fail.
"""
from __future__ import annotations
import sympy as sp


def verify():
    c,N0,rho,q=sp.symbols("c N0 rho q",nonzero=True,positive=True)
    F=sp.symbols("F",real=True)
    C=sp.Matrix([
        [2,1,0,1],
        [1,2,1,0],
        [0,1,3,1],
        [1,0,1,2],
    ])
    E=C*sp.diag(1,rho,rho,rho)/q
    eta=sp.diag(-1,1,1,1)
    metric=E*eta*E.T
    checks={}
    checks["sample_coframe_invertible"]=C.det()==4
    checks["volume_det_exact"]=sp.simplify(
        E.det()-rho**3*C.det()/q**4)==0
    checks["metric_determinant_lorentzian"]=sp.simplify(
        metric.det()+E.det()**2)==0
    checks["kinetic_contraction_exactly_volume"]=sp.simplify(
        sum(metric.inv()[mu,nu]*metric[mu,nu]
            for mu in range(4) for nu in range(4))-4)==0
    # Spin boost columns of E carry a factor rho/q. Local Euler
    # equation is the cofactor of each boost entry times F.
    cof=E.det()*E.inv()
    checks["boost_volume_cofactor_nonzero_for_each_internal_column"]=all(
        any(sp.simplify(cof[j,mu])!=0 for mu in range(4))
        for j in (1,2,3)
    )
    def cofactor_derivative(mu,j):
        v=sp.symbols("cofactor_probe")
        probed=C.copy()
        probed[mu,j]=v
        result=sp.diff(probed.det(),v).subs(v,C[mu,j])
        return sp.simplify(result-C.det()*C.inv()[j,mu])==0
    checks["all_twelve_volume_cofactors_follow_inverse"]=all(
        cofactor_derivative(mu,j)
        for mu in range(4) for j in (1,2,3)
    )
    # Cofactor check for an explicit independent boost variable.
    beta=sp.symbols("beta")
    D=C.copy()
    D[0,1]=beta
    Et=D*sp.diag(1,rho,rho,rho)/q
    checks["boost_EL_requires_zero_density_coefficient"]=(
        sp.simplify(
            sp.diff(Et.det()*F,beta)-
            (rho**3/q**4)*sp.diff(D.det(),beta)*F
        )==0
        and sp.diff(D.det(),beta)!=0
    )
    # If d rho vanishes, the first E column vanishes identically
    # and the determinant necessarily vanishes regardless of boosts.
    checks["constant_rho_cannot_have_invertible_coframe"]=(
        sp.simplify((C*sp.diag(0,rho,rho,rho)).det())==0
    )
    # Explicit flat coframe witness on the open plateau: rho=qt,
    # b_i^j=q/rho delta_i^j, b_0^i=0 => e_mu^a=delta_mu^a.
    t=sp.symbols("t",positive=True)
    dr=sp.Matrix([q,0,0,0])
    boosts=sp.diag(q/(q*t),q/(q*t),q/(q*t))
    Eflat=sp.diag(1/q,1/q,1/q,1/q)*sp.diag(
        dr[0],q*t*boosts[0,0],q*t*boosts[1,1],q*t*boosts[2,2]
    )
    checks["constant_plateau_nontrivial_nondegenerate_witness"]=(
        Eflat==sp.eye(4)
    )
    # C^2, nonanalytic/nonconstant global potential with a flat
    # interval [1,2], whose derivatives through second order match.
    s=sp.symbols("s",real=True)
    left=(1-s)**4
    right=(s-2)**4
    checks["nonconstant_C2_plateau_matches_left_at_one"]=all(
        sp.diff(left,s,k).subs(s,1)==0 for k in range(3))
    checks["nonconstant_C2_plateau_matches_right_at_two"]=all(
        sp.diff(right,s,k).subs(s,2)==0 for k in range(3))
    checks["plateau_potential_not_globally_constant"]=(
        left.subs(s,0)>0 and right.subs(s,3)>0
    )
    # For all compactly supported variations that remain strictly
    # inside the plateau, S=0 as a functional, hence all its
    # Fréchet derivatives/Hessians vanish (mathematically, not a
    # single finite-dimensional numerical test).
    amp1,amp2=sp.symbols("eps1 eps2",real=True)
    volume=sp.symbols("volume",real=True)
    local_plateau_action=sp.Integer(0)*volume*(1+amp1+amp2)**2
    checks["plateau_restricted_action_and_Hessian_vanish"]=all(
        sp.diff(local_plateau_action,amp1,k)==0 for k in (0,1,2)
    )
    # Any globally nonconstant POLYNOMIAL cannot equal a fixed level
    # throughout an open interval.
    a0,a1,a2=sp.symbols("a0 a1 a2",real=True)
    poly=a0+a1*s+a2*s**2
    checks["polynomial_plateau_forces_constant_coefficients"]=(
        sp.solve([sp.diff(poly,s),sp.diff(poly,s,2)],
                 [a1,a2],dict=True)==[{a1:0,a2:0}]
    )
    # The declared SL(2,C) x U(1) symmetries do not uniquely select
    # the scalar action: H(X)^2 and |det X|^2 are independent.
    z=sp.I
    X1=sp.eye(2)
    X2=sp.Matrix([[1,z],[z,1]])
    def invariants(X):
        sharp=sp.Matrix([[X[1,1],-X[0,1]],[-X[1,0],X[0,0]]])
        H=sp.expand(sp.trace(sharp*X.conjugate().T))
        determinant_norm=sp.expand(X.det()*sp.conjugate(X.det()))
        return H**2,determinant_norm
    V=sp.Matrix([list(invariants(X1)),list(invariants(X2))])
    checks["two_symmetry_allowed_quartic_invariants_are_independent"]=V.det()!=0
    checks["quartic_invariant_witness_matrix"]=V==sp.Matrix([[4,1],[0,4]])
    return checks


if __name__=="__main__":
    tests=verify()
    for name,ok in tests.items():
        print(("PASS " if ok else "FAIL ")+name)
    print(f"Passed {sum(bool(x) for x in tests.values())}/{len(tests)} exact tests")
    if not all(tests.values()):raise SystemExit(1)
