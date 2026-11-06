"""Conditional full-Theta information/colour/multiplex discriminants.

Finite exact checks only. Not a derived UBT action, particle colour or a physical channel.
"""
from __future__ import annotations

import sympy as sp

I = sp.I
E2 = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -I], [I, 0]])
SZ = sp.diag(1, -1)
SIGMAS = (SX, SY, SZ)
G = sp.diag(1, -1, -1, -1)


def theta(h, vec):
    C = sp.sqrt(1 + sum(b*b for b in vec))
    return (h - I*C)*E2 - I*sum((vec[j]*SIGMAS[j] for j in range(3)), sp.zeros(2))


def invariant_H(t):
    sharp = sp.trace(t)*E2 - t
    return sp.simplify(sp.trace(sharp*t.H))


def delta(t):
    d = sp.expand(t.det())
    return sp.simplify(sp.expand(d*sp.conjugate(d) - invariant_H(t)**2/4))


def color_projector(h, vec):
    C = sp.sqrt(1 + sum(b*b for b in vec))
    z = sp.Matrix([h - I*C, *[-I*b for b in vec]])
    norm = sp.simplify((z.conjugate().T*G*z)[0])
    return sp.simplify(z*(z.conjugate().T*G)/norm), norm


def test_quadratic_and_quartic_invariants_full_three_direction_chart():
    h,a,b,c=sp.symbols('h a b c',real=True,positive=True)
    s=(a,b,c)
    t=theta(h,s)
    C=sp.sqrt(1+a*a+b*b+c*c)
    assert sp.simplify(invariant_H(t)-2*(h*h+1)) == 0
    assert sp.simplify(t.det()-(h*h-1-2*I*h*C)) == 0
    assert sp.simplify(delta(t)-4*h*h*(a*a+b*b+c*c)) == 0


def test_global_quartic_invariants_survive_lorentz_and_u1():
    t=theta(sp.Rational(3,2), (sp.Rational(3,4),sp.Rational(-1,3),sp.Rational(2,5)))
    S=sp.Matrix([[1,1],[0,1]])
    tp=S*t*S.H
    for other in (tp, I*tp):
        assert sp.simplify(invariant_H(other)-invariant_H(t)) == 0
        assert sp.simplify(delta(other)-delta(t)) == 0


def test_fixed_origin_quadratic_invariant_does_not_select_boost():
    a,b,c=sp.symbols('a b c',real=True)
    t=theta(1,(a,b,c))
    assert sp.simplify(invariant_H(t)-4)==0
    assert sp.simplify(delta(t)-4*(a*a+b*b+c*c))==0


def test_unique_quartic_coefficient_controls_local_vertical_hessian():
    a,b,c,lmb=sp.symbols('a b c lmb',real=True)
    t=theta(1,(a,b,c))
    F=lmb*delta(t)
    variables=(a,b,c)
    H=sp.hessian(F,variables)
    assert sp.simplify(H-8*lmb*sp.eye(3)) == sp.zeros(3)
    assert sp.simplify(H.subs(lmb,sp.Rational(1,24))-sp.eye(3)/3)==sp.zeros(3)


def test_quartic_candidate_is_not_globally_bounded_on_full_theta():
    t=sp.symbols('t',real=True)
    original=sp.Rational(1,2)*E2+SX+I*SY
    assert original.det()==sp.Rational(1,4)
    assert sp.simplify(delta(t*original)+3*t**4)==0


def test_colour_normal_and_moving_rank_three_projector_really_change():
    P0,N0=color_projector(1,(0,0,0))
    P1,N1=color_projector(1,(sp.Rational(3,4),0,0))
    assert N0==N1==2
    assert P0==sp.diag(1,0,0,0)
    assert sp.simplify(P1[0,1]+sp.Rational(15,32)+3*I/8)==0
    assert P0!=P1
    assert sp.simplify(P1*P1-P1)==sp.zeros(4)
    assert sp.trace(P1)==1


def test_su3_frame_change_preserves_projector_not_boost_shift():
    P0,_=color_projector(1,(0,0,0))
    U=sp.diag(1,sp.exp(I*sp.pi/3),sp.exp(-I*sp.pi/3),1)
    assert sp.simplify(U.H*G*U-G)==sp.zeros(4)
    assert sp.simplify(U*P0*U.inv()-P0)==sp.zeros(4)
    P1,_=color_projector(1,(sp.Rational(3,4),0,0))
    assert P1!=P0


def test_conditional_raw_binary_information_exists_only_with_extra_readout():
    r=sp.Rational(3,4)
    q1=theta(1,(r,0,0))
    q2=theta(1,(-r,0,0))
    readout=lambda t:sp.simplify(t*t.H/sp.trace(t*t.H))
    Eplus=(E2+SX)/2
    p1=sp.simplify(sp.trace(readout(q1)*Eplus))
    p2=sp.simplify(sp.trace(readout(q2)*Eplus))
    assert p1==sp.Rational(4,5) and p2==sp.Rational(1,5)
    MI=sp.log(2)+p1*sp.log(p1)+(1-p1)*sp.log(1-p1)
    assert abs(float(MI/sp.log(2))-0.2780719051126377)<1e-12


def test_conditional_quotient_record_is_exactly_zero_information():
    p=sp.symbols('p',real=True,positive=True)
    assert sp.simplify((sp.Rational(1,2)*p+sp.Rational(1,2)*p)-p)==0
    prior=sp.Rational(1,2)
    MI=sum(prior*q*sp.log(q/q) for q in (p,1-p))*2
    assert sp.simplify(MI)==0


def test_fixed_observer_fisher_cannot_be_constant_potential_hessian():
    t=sp.symbols('t',real=True,nonzero=True)
    C=sp.sqrt(1+t*t)
    v=t/C
    tetra=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
    fv=sp.zeros(3)
    for a in tetra:
        u=sp.Matrix(a)/sp.sqrt(3)
        p=(1+u[0]*v)/4
        fv+= (u*u.T)/(16*p)
    assert sp.simplify(fv[0,0]-fv[1,1])==0
    J=sp.diag(C**(-3),C**(-1),C**(-1))
    F=sp.simplify(J.T*fv*J)
    assert sp.simplify(F[0,0]/F[1,1]-C**(-4))==0
    assert sp.simplify(C**(-4)-1)!=0
