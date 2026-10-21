#!/usr/bin/env python3
"""Exact Lorentz-invariant clock identity for ALL positive-Hermitian timelike X.

X=rho*I+s_i*sigma_i (det X=rho**2-|s|**2>0), Theta=i X.
The genuine traceless SL(2,C) spin lift D X=d X+Omega X+X Omega^dagger
with Omega=1/2(beta+i omega)*sigma gives
D rho = d rho+beta.s and D s=d s+rho beta-omega cross s.
Thus eta(X,D X)=-1/2 d(det X), so the metric from E=D X/q
obeys g^{-1}(d sqrt(det X),d sqrt(det X))=-q**2 whenever E invertible.
This is a purely kinematic statement; no UBT on-shell action follows.
"""
from __future__ import annotations
import sympy as sp


def verify_timelike_orbit_clock():
    rho=sp.symbols("rho",positive=True,real=True)
    s=sp.Matrix(sp.symbols("s0:3",real=True))
    ds=sp.Matrix(sp.symbols("ds0:3",real=True))
    b=sp.Matrix(sp.symbols("b0:3",real=True))
    omega=sp.Matrix(sp.symbols("omega0:3",real=True))
    drho=sp.symbols("drho",real=True)
    dx0=drho+b.dot(s)
    dxs=ds+rho*b-omega.cross(s)
    results={}
    results["Lorentz_generator_preserves_internal_norm"]=(
        sp.expand(-rho*dx0+s.dot(dxs)+rho*drho-s.dot(ds))==0
    )
    eta=sp.diag(-1,1,1,1)
    x=sp.Matrix([rho,*s])
    Dx=sp.Matrix([dx0,*dxs])
    results["Lorentz_scalar_determinant_gradient"]=(
        sp.expand((x.T*eta*Dx)[0]+rho*drho-s.dot(ds))==0
    )
    I=sp.I
    pauli=[
        sp.Matrix([[0,1],[1,0]]),
        sp.Matrix([[0,-I],[I,0]]),
        sp.Matrix([[1,0],[0,-1]])
    ]
    X=rho*sp.eye(2)+sum((s[i]*pauli[i] for i in range(3)),sp.zeros(2))
    Om=sum(((b[i]+I*omega[i])*pauli[i]/2 for i in range(3)),sp.zeros(2))
    dX=drho*sp.eye(2)+sum((ds[i]*pauli[i] for i in range(3)),sp.zeros(2))
    DX=sp.expand(dX+Om*X+X*Om.conjugate().T)
    reconstructed=dx0*sp.eye(2)+sum((dxs[i]*pauli[i] for i in range(3)),sp.zeros(2))
    results["actual_Pauli_spin_derivative_matches_fourvector"]=(
        sp.simplify(DX-reconstructed)==sp.zeros(2)
    )
    results["detX_invariant_Minkowski_norm"]=(
        sp.simplify(X.det()-(rho**2-s.dot(s)))==0
    )
    # Invertible four-coframe explicit example: no imposed radial gauge.
    q=sp.Integer(2)
    Xexample=sp.Matrix([3,1,1,0])
    rexample=sp.sqrt(7)
    E=sp.Matrix([[2,1,0,0],[0,1,1,0],[0,0,2,1],[0,0,0,1]])
    met=E*eta*E.T/q**2
    # d r = - eta(X,D X)/r per spacetime index (r=sqrt(detX)).
    grad_r=-E*eta*Xexample/rexample
    results["nonradial_example_invertible_tetrad"]=(E.det()!=0)
    results["nonradial_example_exact_unit_clock"]=(
        sp.simplify((grad_r.T*met.inv()*grad_r)[0]+q*q)==0
    )
    # Gaussian gauge to positive radial form:
    # S=sqrt(r)*X^(-1/2), det S=1, S X S^dagger=r I
    # For an explicit diagonal SPD X the formula can be certified exactly.
    diagX=sp.diag(4,1)
    r=sp.sqrt(diagX.det())
    S=sp.sqrt(r)*sp.diag(sp.Rational(1,2),1)
    results["radialization_SL2C_determinant_one"]=(sp.simplify(S.det()-1)==0)
    results["radialization_positive_X_to_rI"]=(
        sp.simplify(S*diagX*S.conjugate().T-r*sp.eye(2))==sp.zeros(2)
    )
    return results


def main():
    result=verify_timelike_orbit_clock()
    for name,passed in result.items():
        print(("PASS" if passed else "FAIL")+" "+name)
    if not all(result.values()):
        raise SystemExit(1)
    print(f"PASS {len(result)} exact symbolic timelike-orbit identities")


if __name__=="__main__":
    main()
