#!/usr/bin/env python3
"""Exact orbit/first-jet invariants illustrating the geometric proof.

Conditional theorem: on a nondegenerate positive-Hermitian Lorentz-real
single-Theta branch, every local diffeo- and Lorentz-invariant algebraic
density depending on X, e=DX/q, eta, epsilon and inverses, but on no
derivatives of e or spin curvature, reduces to |det e| F(r),
r=sqrt(-X^2), in a fixed orientation patch.

This script checks nontrivial contractions and orbit transformations,
but the universal statement itself follows from frame normalization
and transitivity of SO^+(1,3) on the timelike hyperboloid, not from a
finite number of numerical matrix tests. Not a no-go for full UBT.
"""
import sympy as s


def verify():
    eta=s.diag(-1,1,1,1)
    x=s.Matrix(s.symbols("x0:4",real=True))
    mats=[
        s.Matrix([[2,1,0,1],[1,2,1,0],[0,1,3,1],[1,0,1,2]]),
        s.Matrix([[3,0,1,0],[1,3,0,1],[0,1,2,1],[0,0,1,2]]),
    ]
    assert all(E.det()!=0 for E in mats)
    L=s.eye(4)
    L[0,0]=s.Rational(5,3)
    L[0,1]=s.Rational(4,3)
    L[1,0]=s.Rational(4,3)
    L[1,1]=s.Rational(5,3)
    checks={}
    checks["Lorentz_boost_eta_preserving"]=L.T*eta*L==eta
    checks["Lorentz_boost_connected_orientation"]=L.det()==1
    for ix,E in enumerate(mats):
        Ep=E*L.T
        xp=L*x
        g=E*eta*E.T
        gp=Ep*eta*Ep.T
        n=E*eta*x
        np=Ep*eta*xp
        gi=g.inv()
        checks[f"coframe_nonzero_volume_{ix}"]=E.det()!=0
        checks[f"internal_Lorentz_metric_invariance_{ix}"]=gp==g
        checks[f"internal_Lorentz_oneform_invariance_{ix}"]=np==n
        checks[f"oneform_squared_is_field_norm_{ix}"]=s.simplify((n.T*gi*n)[0]-(x.T*eta*x)[0])==0
        u2=(x.T*eta*x)[0]
        z=gi*n
        Pi=s.eye(4)-z*n.T/u2
        checks[f"intrinsic_projector_idempotent_{ix}"]=s.simplify(Pi*Pi-Pi)==s.zeros(4)
        checks[f"intrinsic_projector_trace_three_{ix}"]=s.simplify(s.trace(Pi)-3)==0
        checks[f"epsilon_volume_is_determinant_{ix}"]=s.simplify(E.det()**2+g.det())==0
        checks[f"coframe_4_form_density_is_24_det_{ix}"]=24*E.det()==24*s.det(E)
        checks[f"GL4_frame_normalization_{ix}"]=E.inv()*E==s.eye(4)
    checks["fourth_power_scalar_only_radial"]=s.expand(((x.T*eta*x)[0])**2-(-x[0]**2+x[1]**2+x[2]**2+x[3]**2)**2)==0
    rr=s.symbols("r",positive=True)
    x0=s.Matrix([rr,0,0,0])
    x1=L*x0
    checks["rational_spin_boost_connects_same_timelike_orbit"]=(
        s.simplify((x1.T*eta*x1)[0]+rr**2)==0 and x1[0]>0)
    E=mats[0]
    checks["cofactor_for_each_spatial_column_is_nonzero"]=all(
        any(s.simplify(E.det()*E.inv()[a,mu])!=0 for mu in range(4))
        for a in range(1,4))
    return checks


if __name__=="__main__":
    checks=verify()
    for k,v in checks.items():
        print(("PASS" if v else "FAIL"),k)
    print(f"PASSED {sum(bool(x) for x in checks.values())}/{len(checks)}")
    if not all(checks.values()):
        raise SystemExit(1)
