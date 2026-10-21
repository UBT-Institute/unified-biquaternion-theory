#!/usr/bin/env python3
"""Exact Clifford 16-grade and Cartan axial/trace parity-sector identities.

Scope: kinematic Cl(1,3) and an algebraic irreducible-torsion comparator.
No full UBT single-action solution, healthy Hamiltonian or physical CMB claim.
"""
from __future__ import annotations

from collections import Counter
import sympy as sp


def clifford_product(a, b, eta=(1,-1,-1,-1)):
    sign=1
    for i in range(4):
        if a & (1 << i):
            for j in range(4):
                if b & (1 << j) and i>j:
                    sign=-sign
    for i in range(4):
        if a & b & (1 << i):
            sign*=eta[i]
    return sp.Integer(sign),a^b


def add(*forms):
    o={}
    for f in forms:
        for k,v in f.items():o[k]=sp.expand(o.get(k,0)+v)
    return {k:v for k,v in o.items() if v!=0}


def mul(c,f):
    return {k:sp.expand(c*v) for k,v in f.items() if sp.expand(c*v)!=0}


def wedge(f,g):
    out={}
    for a,ca in f.items():
        for b,cb in g.items():
            if set(a)&set(b):continue
            k=tuple(sorted((*a,*b)))
            inv=sum(i>j for i in a for j in b)
            out[k]=sp.expand(out.get(k,0)+(-1)**inv*ca*cb)
    return {k:v for k,v in out.items() if v!=0}


def verify():
    out={}
    counts=Counter(mask.bit_count() for mask in range(16))
    out["Clifford_grades_1_4_6_4_1"]=[counts[i] for i in range(5)]==[1,4,6,4,1]
    out["even_biquaternion_has_eight_real_components"]=sum(counts[i] for i in (0,2,4))==8
    out["odd_vector_pseudovector_outside_even"]=sum(counts[i] for i in (1,3))==8
    I=15
    out["pseudoscalar_square_minus_one"]=clifford_product(I,I)==(-1,0)
    out["I_commutes_even_and_anticommutes_odd"]=all(
        clifford_product(I,b)[0]==(-1)**b.bit_count()*clifford_product(b,I)[0]
        for b in range(16))
    e=[{(i,):sp.Integer(1)} for i in range(4)]
    t=sp.symbols("t0:4",real=True)
    tf={(i,):t[i] for i in range(4)}
    T=[mul(sp.Rational(1,3),wedge(tf,e[i])) for i in range(4)]
    signature=(1,-1,-1,-1)
    et=add(*(mul(signature[i],wedge(e[i],T[i])) for i in range(4)))
    tt=add(*(mul(signature[i],wedge(T[i],T[i])) for i in range(4)))
    out["trace_only_e_a_wedge_Ta_vanishes"]=not et
    out["trace_only_Ta_wedge_Ta_vanishes"]=not tt
    out["Nieh_Yan_Holst_4forms_zero_on_trace_sector"]=not et and not tt
    # Introduce axial 2-form T^1+=k e^2^e^3;
    # it gives nonzero dP ^ e_a ^ T^a for dP=e^0.
    k=sp.symbols("axial_k",real=True)
    Ta=list(T)
    Ta[1]=add(Ta[1],{(2,3):k})
    axial=add(*(mul(signature[i],wedge(e[i],Ta[i])) for i in range(4)))
    out["axial_Nieh_Yan_derivative_coupling_nonzero"]=sp.simplify(
        wedge(e[0],axial).get((0,1,2,3),0)+k)==0
    # With timelike trace t0 and isotropic axial 3-form,
    # T^a ^ T_a contains a nonzero trace-axial cross term.
    t0=sp.symbols("t0_nonzero",nonzero=True)
    tset={t[0]:t0,**{t[i]:0 for i in (1,2,3)}}
    iso=[{key:v.subs(tset) for key,v in f.items() if v.subs(tset)!=0} for f in T]
    iso[1]=add(iso[1],{(2,3):k})
    iso[2]=add(iso[2],{(1,3):-k})
    iso[3]=add(iso[3],{(1,2):k})
    square=add(*(mul(signature[i],wedge(iso[i],iso[i])) for i in range(4)))
    out["Holst_torsion_4form_first_variation_nonzero"]=(
        sp.diff(square.get((0,1,2,3),0),k).subs(k,0)!=0)
    ct,ca,beta,Jt,Ja=sp.symbols("ct ca beta Jt Ja",real=True)
    delta=ct*ca-beta**2
    tsol=(-ca*Jt+beta*Ja)/delta
    asol=(beta*Jt-ct*Ja)/delta
    out["mixed_trace_vector_Euler_equation"]=sp.factor(ct*tsol+beta*asol+Jt)==0
    out["mixed_axial_vector_Euler_equation"]=sp.factor(beta*tsol+ca*asol+Ja)==0
    out["trace_current_can_induce_axial_torsion"]=sp.factor(asol.subs(Ja,0)-beta*Jt/delta)==0
    out["mixed_algebraic_Hessian_determinant"]=(
        sp.det(sp.Matrix([[ct,beta],[beta,ca]]))==delta)
    S,P=sp.symbols("S P",real=True)
    c,s=sp.Rational(3,5),sp.Rational(4,5)
    Snew,Pnew=c*S-s*P,s*S+c*P
    out["isolated_pseudoscalar_breaks_phase_U1"]=Pnew!=P
    out["scalar_pseudoscalar_norm_phase_neutral"]=sp.expand(
        Snew**2+Pnew**2-S**2-P**2)==0
    return out


if __name__=="__main__":
    result=verify()
    for key,valid in result.items():
        print(("PASS" if valid else "FAIL"),key)
    if not all(result.values()):raise SystemExit(1)
    print(f"PASS all {len(result)} exact conditional checks")
