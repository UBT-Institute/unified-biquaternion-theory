#!/usr/bin/env python3
"""Exact Pauli/connection and curvature checks for kinematic closed FLRW UBT.

Checks are conditional identities. They DO NOT show that the configuration
satisfies the full UBT Euler-Lagrange equations or selects the topology.
Requires SymPy, standard mathematical conventions (-+++), unit round S^3.
"""
from __future__ import annotations

import sympy as sp


def check_connection_closed_flrw() -> dict[str, bool]:
    checks: dict[str, bool] = {}
    ii = sp.I
    identity = sp.eye(2)
    pauli = (
        sp.Matrix([[0,1],[1,0]]),
        sp.Matrix([[0,-ii],[ii,0]]),
        sp.Matrix([[1,0],[0,-1]]),
    )
    n0, rho, lapse, scale = sp.symbols(
        "N0 rho lapse scale", positive=True, real=True
    )
    def adj2(x: sp.Matrix) -> sp.Matrix:
        return sp.trace(x)*identity-x
    def pairing(x: sp.Matrix, y: sp.Matrix) -> sp.Expr:
        return sp.expand(sp.trace(
            adj2(x)*y.conjugate().T+adj2(y)*x.conjugate().T
        )/2)
    e0 = ii*sp.sqrt(n0)*lapse*identity
    ei = [ii*sp.sqrt(n0)*scale*v for v in pauli]
    internal = [e0]+ei
    gram=sp.Matrix(4,4, lambda i,j: sp.simplify(
        -pairing(internal[i],internal[j])/(2*n0)
    ))
    checks["exact_pauli_lorentz_central_metric"] = (
        gram == sp.diag(-lapse*lapse, scale*scale, scale*scale, scale*scale)
    )
    f=sp.sqrt(n0)*scale/(2*rho)
    theta=ii*rho*identity
    dtheta0=ii*sp.sqrt(n0)*lapse*identity
    As=[f*sigma for sigma in pauli]
    Bs=[-v for v in As]
    DthetaSpatial=[sp.simplify(As[j]*theta-theta*Bs[j]) for j in range(3)]
    checks["two_sided_connection_generates_spatial_frame"] = all(
        sp.simplify(DthetaSpatial[j]-ei[j])==sp.zeros(2) for j in range(3)
    )
    checks["temporal_gradient_generates_lapse_frame"] = (
        sp.simplify(dtheta0-e0)==sp.zeros(2)
    )

    # d(v^3)=-2 v^1 ^ v^2 from Maurer-Cartan on unit S^3.
    # Component F_{12} in the ordered form v^1 ^ v^2:
    dA12=-2*f*pauli[2]
    dB12=-dA12
    commutator=As[0]*As[1]-As[1]*As[0]
    FA12=dA12+commutator
    FB12=dB12+commutator
    checks["connection_curvature_from_Maurer_Cartan"] = (
        sp.simplify(FA12-(-2*f+2*ii*f*f)*pauli[2]) == sp.zeros(2)
    )
    checks["nonzero_two_sided_integrability_obstruction"] = (
        sp.simplify(
            FA12*theta-theta*FB12 +4*ii*rho*f*pauli[2]
        ) == sp.zeros(2)
        and sp.simplify(-4*ii*rho*f) != 0
    )

    # Independent coordinate-Ricci calculation, hyperspherical chart for
    # the globally round unit-curvature S^3 quotient geometry.
    t, chi, polar, phi = sp.symbols("t chi polar phi", real=True)
    a, n = sp.Function("a")(t), sp.Function("N")(t)
    coords = [t,chi,polar,phi]
    metric = sp.diag(
        -n**2,a**2,a**2*sp.sin(chi)**2,
        a**2*sp.sin(chi)**2*sp.sin(polar)**2
    )
    invmetric = sp.diag(
        -1/n**2,1/a**2,1/(a*sp.sin(chi))**2,
        1/(a*sp.sin(chi)*sp.sin(polar))**2
    )
    gammas:dict[tuple[int,int,int],sp.Expr]={}
    for i in range(4):
        for j in range(4):
            for k in range(4):
                value=sum(
                    invmetric[i,l]*(
                        sp.diff(metric[l,k],coords[j])
                        +sp.diff(metric[l,j],coords[k])
                        -sp.diff(metric[j,k],coords[l])
                    ) for l in range(4)
                )/2
                value=sp.trigsimp(sp.cancel(value))
                if value != 0:
                    gammas[i,j,k]=value
    ricci_diagonal=[]
    for index in range(4):
        value=sum(
            sp.diff(gammas.get((k,index,index),0),coords[k])
            -sp.diff(gammas.get((k,index,k),0),coords[index])
            +sum(
                gammas.get((k,k,l),0)*gammas.get((l,index,index),0)
                -gammas.get((k,index,l),0)*gammas.get((l,index,k),0)
                for l in range(4)
            )
            for k in range(4)
        )
        ricci_diagonal.append(sp.trigsimp(sp.cancel(value)))
    curvature_scalar=sp.simplify(sp.trigsimp(
        sum(invmetric[j,j]*ricci_diagonal[j] for j in range(4))
    ))
    expected=6*(
        sp.diff(a,t,2)/(a*n*n)
        -sp.diff(a,t)*sp.diff(n,t)/(a*n**3)
        +sp.diff(a,t)**2/(a*a*n*n)+1/(a*a)
    )
    checks["independent_christoffel_ricci_scalar_closed_FLRW"] = (
        sp.simplify(curvature_scalar-expected)==0
    )
    checks["static_positive_spacetime_curvature"] = (
        sp.simplify(expected.subs({
            sp.diff(a,t,2):0, sp.diff(a,t):0,
            sp.diff(n,t):0, n:1
        })-6/a**2)==0
    )

    # Standard comparison Einstein-Hilbert action, NOT a UBT derivation.
    gnew, cosm, vel, mom = sp.symbols(
        "G cosm vel mom", nonzero=True, real=True
    )
    V = sp.pi**2/60
    C=sp.simplify(3*V/(8*sp.pi*gnew))
    checks["exact_quotient_gravity_prefactor"] = (
        sp.simplify(C-sp.pi/(160*gnew))==0
    )
    L=C*(-scale*vel**2/lapse
         +lapse*scale-lapse*cosm*scale**3/3)
    p=sp.diff(L,vel)
    checks["closed_EH_minisuperspace_momentum"] = (
        sp.simplify(p+2*C*scale*vel/lapse)==0
    )
    vel_of_p=-lapse*mom/(2*C*scale)
    H=sp.simplify((mom*vel-L).subs(vel,vel_of_p))
    H_expected=lapse*(-mom**2/(4*C*scale)
                      -C*scale+C*cosm*scale**3/3)
    checks["EH_minisuperspace_Hamiltonian"] = (
        sp.simplify(H-H_expected)==0
    )
    constraint=sp.simplify(sp.diff(L,lapse)
                           -C*scale*(vel**2/lapse**2+1
                                    -cosm*scale**2/3))
    checks["lapse_variation_yields_closed_Friedmann_equation"] = (
        constraint==0
    )
    c, u, = sp.symbols("c U", real=True)
    Lminimal=V*lapse*scale**3*(4*c*n0-u)
    checks["minimal_UBT_on_ansatz_has_zero_a_velocity_Hessian"] = (
        sp.diff(Lminimal,vel,2)==0
    )
    return checks


def main()->None:
    checks=check_connection_closed_flrw()
    for name, result in checks.items():
        print(f"{'PASS' if result else 'FAIL'} {name}")
    if not all(checks.values()):
        raise SystemExit(1)
    print(f"PASS all {len(checks)} exact conditional checks")


if __name__=="__main__":
    main()
