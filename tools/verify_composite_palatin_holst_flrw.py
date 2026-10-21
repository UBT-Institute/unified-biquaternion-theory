#!/usr/bin/env python3
"""Exact homogeneous composite-Theta Palatini/Holst minisuperspace audit.

Conventions: (-+++) local frame; unit S^3 left-invariant coframe
dv^i=-eps^i_jk dv^j ^ dv^k (sum over ordered pairs);
omega^0_i=omega^i_0=B(t) v^i, omega^i_j=C(t) eps^i_jk v^k;
e^0=N(t)dt, e^i=a(t)v^i; canonical radial representation
Theta=i*q*V(t)*I, N=dV/dt, B=a/V. The rotational C is varied
INDEPENDENTLY; DO NOT set C=-1 before varying.

We use the explicitly defined normalized Palatini + Holst comparator,
not an action derived from the one fundamental UBT Theta family:
L/(constant) = (epsilon e e R)/12 + alpha*(e_lower e_lower R_upper)/3
               - Lambda*N*a**3/3.
The associated normalized cosmological EH sector gives
L_EH= -a*a_dot**2/N+N*a-(Lambda/3)*N*a**3
after independently imposed zero torsion and a boundary integration.
No full unconstrained UBT E-L, ghost-free, or CMB claim follows.
"""
from __future__ import annotations
import itertools
import sympy as s


def simp(x):
    return s.factor(s.expand(x))


def add(*forms):
    d={}
    for f in forms:
        for k,v in f.items():
            d[k]=simp(d.get(k,0)+v)
    return {k:v for k,v in d.items() if v!=0}


def mul(f,c):
    return {k:simp(v*c) for k,v in f.items() if simp(v*c)!=0}


def wedge(f,g):
    out={}
    for I,v in f.items():
        for J,u in g.items():
            if set(I)&set(J):
                continue
            k=tuple(sorted(I+J))
            sig=(-1)**sum(i>j for i in I for j in J)
            out[k]=simp(out.get(k,0)+sig*v*u)
    return {k:v for k,v in out.items() if v!=0}


def wedge_many(*fs):
    result={():s.Integer(1)}
    for f in fs:
        result=wedge(result,f)
    return result


def verify():
    t=s.symbols("t",real=True)
    aa=s.Function("a")(t)
    nn=s.Function("N")(t)
    bb=s.Function("B")(t)
    cc=s.Function("C")(t)
    v=[{(k,):s.Integer(1)} for k in range(4)]
    eps=lambda i,j,k:s.LeviCivita(i,j,k)
    def exterior_d1(f):
        out={}
        for (i,),coef in f.items():
            out=add(out,wedge(v[0],mul(v[i],s.diff(coef,t))))
            if i>0:
                out=add(out,*(mul(wedge(v[j+1],v[k+1]),
                    -coef*eps(i-1,j,k)) for j in range(3) for k in range(3)))
        return out

    e=[mul(v[0],nn)]+[mul(v[i],aa) for i in range(1,4)]
    omega=[[{} for j in range(4)] for i in range(4)]
    for i in range(1,4):
        omega[0][i]=mul(v[i],bb)
        omega[i][0]=mul(v[i],bb)
    for i in range(1,4):
        for j in range(1,4):
            omega[i][j]=add(*(mul(v[k+1],cc*eps(i-1,j-1,k))
                                for k in range(3)))
    R=[[add(exterior_d1(omega[i][j]),
            *(wedge(omega[i][k],omega[k][j]) for k in range(4)))
         for j in range(4)] for i in range(4)]
    eta=[-1,1,1,1]
    Rraised=[[mul(R[i][j],eta[j]) for j in range(4)] for i in range(4)]
    T=[add(exterior_d1(e[i]),*(wedge(omega[i][j],e[j])
        for j in range(4))) for i in range(4)]
    volume=(0,1,2,3)
    four=lambda *fs:wedge_many(*fs).get(volume,0)
    EC=simp(sum(s.LeviCivita(i,j,k,l)*four(e[i],e[j],Rraised[k][l])
          for i,j,k,l in itertools.permutations(range(4),4)))
    Holst=simp(sum(four(mul(e[i],eta[i]),mul(e[j],eta[j]),Rraised[i][j])
          for i in range(4) for j in range(i+1,4)))
    tor2=simp(sum(eta[i]*wedge(T[i],T[i]).get(volume,0)
                   for i in range(4)))
    checks={}
    checks["spatial_spincurvature_from_exterior_forms"]=(
        simp(R[1][2].get((1,2),0)-(bb**2-cc**2-2*cc))==0)
    checks["boost_spincurvature_from_exterior_forms"]=(
        simp(R[0][1].get((0,1),0)-s.diff(bb,t))==0)
    checks["Cartan_temporal_torsion"]=(
        simp(T[1].get((0,1),0)-(s.diff(aa,t)-nn*bb))==0)
    checks["Cartan_spatial_torsion"]=(
        simp(T[1].get((2,3),0)+2*aa*(cc+1))==0)
    checks["Palatini_fourform_exact"]=(
        simp(EC-12*aa*(nn*(bb**2-cc**2-2*cc)+aa*s.diff(bb,t)))==0)
    checks["Holst_fourform_exact"]=(
        simp(Holst-3*aa*(2*nn*bb*(cc+1)+aa*s.diff(cc,t)))==0)
    # Independent zero torsion reduction reproduces standard EH/GHY
    eh_on=s.simplify((EC/12).subs({bb:s.diff(aa,t)/nn,cc:-1}))
    eh_expected=-aa*s.diff(aa,t)**2/nn+nn*aa
    boundary=s.diff(aa**2*s.diff(aa,t)/nn,t)
    checks["Palatini_torsionfree_EH_up_to_boundary"]=(
        simp(eh_on-eh_expected-boundary)==0)
    checks["Holst_vanishes_on_torsionfree_FLRW"]=(
        simp(Holst.subs({s.diff(cc,t):0,bb:s.diff(aa,t)/nn,cc:-1}).doit())==0)

    V=s.Function("V")(t)
    N=s.diff(V,t)
    lam,alpha=s.symbols("Lambda alpha",real=True)
    B=aa/V
    C=cc
    L=simp((EC/12+alpha*Holst/3-lam*nn*aa**3/3).subs({
        bb:B,nn:N,s.diff(bb,t):s.diff(B,t)}))
    w=C+1
    Leff=N*(aa+aa**3/(3*V**2)-lam*aa**3/3-aa*w**2
           +2*alpha*aa**2*w/V)-2*alpha*aa*s.diff(aa,t)*w
    boundary_total=s.diff(aa**3/(3*V)+alpha*aa**2*w,t)
    checks["composite_action_total_derivative_identity"]=(
        simp(L-Leff-boundary_total)==0)
    eqC=simp(s.diff(Leff,C)-s.diff(s.diff(Leff,s.diff(C,t)),t))
    Wsol=alpha*(aa/V-s.diff(aa,t)/N)
    checks["spin_rotation_EL_solution"]=(
        simp(eqC+2*N*aa*(w-Wsol))==0)
    Leff_reduced=simp(Leff.subs(C,Wsol-1))
    Lrequired=N*(aa+aa**3/(3*V**2)-lam*aa**3/3+
                 alpha**2*aa*(aa/V-s.diff(aa,t)/N)**2)
    checks["spin_rotation_elimination_exact"]=(
        simp(Leff_reduced-Lrequired)==0)
    checks["Holst_generates_radial_kinetic_Hessian"]=(
        simp(s.diff(Leff_reduced,s.diff(aa,t),2)-2*alpha**2*aa/N)==0)
    checks["without_Holst_zero_radial_velocity_Hessian"]=(
        simp(s.diff(Leff_reduced,s.diff(aa,t),2).subs(alpha,0))==0)
    bare=Leff_reduced.subs({alpha:0,lam:0})
    ELa=simp(s.diff(bare,aa)-s.diff(s.diff(bare,s.diff(aa,t)),t))
    checks["zero_Lambda_noHolst_strict_positive_scale_EL"]=(
        simp(ELa-N*(1+aa**2/V**2))==0)
    # Choosing positive V_dot,a,V makes this residual strictly positive:
    vv, av, Nv=s.symbols("vv av Nv",positive=True)
    checks["zero_Lambda_positive_branch_no_solution"]=(
        (Nv*(1+av**2/vv**2)).is_positive is True)
    # Even with a positive cosmological term the reduced equations admit
    # a branch that generically violates the independent vacuum GR constraint.
    vv=s.symbols("v",positive=True)
    witness=vv/s.sqrt(vv**2-1)  # Lambda=1, valid v>1
    ELlambda=simp((s.diff(Leff_reduced.subs(alpha,0),aa)
           -s.diff(s.diff(Leff_reduced.subs(alpha,0),
                       s.diff(aa,t)),t)))
    checks["Lambda_positive_reduced_stationary_branch"]=(
        s.simplify(ELlambda.subs({
           lam:1,aa:witness,V:vv,N:1}))==0)

    # The clock V Euler equation was not discarded: for alpha=0 it is
    # a reparameterization Noether consequence of the scale equation.
    # With F(a,V)=a+a^3/(3V^2)-Lambda*a^3/3 and N=Vdot:
    # EL_V=N F_V-d_t F=-adot F_a, for arbitrary smooth V,a.
    Fbare=aa+aa**3/(3*V**2)-lam*aa**3/3
    ELclock=s.simplify(
        s.diff(N*Fbare,V)-s.diff(s.diff(N*Fbare,N),t)
    )
    Fderiv=s.diff(Fbare,aa)
    checks["clock_EL_is_Noether_consequence_of_scale_EL"]=(
        simp(ELclock+s.diff(aa,t)*Fderiv)==0
    )
    checks["positive_Lambda_stationary_witness_solves_both_reduced_EL"]=(
        s.simplify(Fderiv.subs({lam:1,aa:witness,V:vv}))==0
        and simp(ELclock+s.diff(aa,t)*Fderiv)==0
    )
    residual=s.simplify(s.diff(witness,vv)**2+1-witness**2/3)
    checks["Lambda_stationary_branch_violates_GR_normal_constraint"]=(
        s.simplify(residual.subs(vv,2)-s.Rational(16,27))==0)
    return checks


if __name__=="__main__":
    checks=verify()
    for k,val in checks.items():
        print(("PASS" if val else "FAIL"),k)
    if not all(checks.values()):
        raise SystemExit(1)
    print(f"PASS {len(checks)} exact homogeneous composite-connection checks")
