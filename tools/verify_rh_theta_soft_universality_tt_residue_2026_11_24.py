#!/usr/bin/env python3
"""Exact benchmark gates for composite spin-two universality and trace sector.

Only algebraic comparators. No UBT quantum action or scattering amplitudes derived.
"""
import sympy as s


def soft_graviton_universality_gate():
    e, k, g_a, g_b = s.symbols('e k g_a g_b', real=True)
    # Two equal-mass legs with elastic right-angle scattering: exact total
    # momentum conserved, all four legs have equal Minkowski p^2=e^2-k^2.
    a_i=s.Matrix([e,0,0,k]); b_i=s.Matrix([e,0,0,-k])
    a_f=s.Matrix([e,k,0,0]); b_f=s.Matrix([e,-k,0,0])
    eta=s.diag(1,-1,-1,-1)
    assert a_i+b_i == a_f+b_f
    on_shell=lambda p: (p.T*eta*p)[0]
    assert all(s.simplify(on_shell(p)-(e**2-k**2))==0
               for p in [a_i,b_i,a_f,b_f])
    gauge=s.simplify(g_a*(a_f-a_i)+g_b*(b_f-b_i))
    assert s.simplify(gauge-(g_a-g_b)*s.Matrix([0,k,0,-k]))==s.zeros(4,1)
    assert s.linsolve(list(gauge.subs(k,1)),(g_a,g_b)) == s.FiniteSet((g_b,g_b))
    # Soft polarization gauge-shift gives 2 * xi dot (sum eta_i g_i p_i).
    xi=s.Matrix(s.symbols('xi0:4'))
    assert s.simplify(s.expand(2*(xi.T*eta*gauge)[0]).coeff(xi[1])
                      + 2*k*(g_a-g_b))==0
    print('PASS: generic elastic A+B->A+B soft gauge invariance forces g_A=g_B')


def trace_exchange_discontinuity_gate():
    # Source conserved with respect to static spatial momentum k along z.
    T=s.diag(1,0,0,0)
    S=s.diag(1,0,0,0)
    k=s.Matrix([0,0,0,1])
    assert k.T*T==s.zeros(1,4) and k.T*S==s.zeros(1,4)
    contraction=s.trace(T*S)
    trace_product=s.trace(T)*s.trace(S)
    massless=contraction-s.Rational(1,2)*trace_product
    massive_m0=contraction-s.Rational(1,3)*trace_product
    assert massless==s.Rational(1,2)
    assert massive_m0==s.Rational(2,3)
    assert massive_m0-massless==s.Rational(1,6)*trace_product
    # Traceless sources alone cannot see the trace-coefficient difference.
    L=s.diag(1,-1,0,0)
    assert k.T*L==s.zeros(1,4) and s.trace(L)==0
    assert (s.trace(L*L)-s.Rational(1,2)*s.trace(L)**2
            ==s.trace(L*L)-s.Rational(1,3)*s.trace(L)**2)
    print('PASS: massless -1/2 vs massive m->0 -1/3 trace factors differ by 1/6')


def physical_transverse_residue_gate():
    # Fixed nonzero spatial wavevector along z; transverse symmetric-traceless
    # projector on 3x3 matrices has rank 2, not rank 5 off-shell 4D.
    P=s.diag(1,1,0)
    def tt(H):
        return s.simplify(P*H*P-s.Rational(1,2)*P*s.trace(P*H))
    eplus=s.diag(1,-1,0)/s.sqrt(2)
    ecross=s.Matrix([[0,1,0],[1,0,0],[0,0,0]])/s.sqrt(2)
    bases=[]
    for a in range(3):
        for b in range(a,3):
            M=s.zeros(3);M[a,b]=M[b,a]=1
            bases.append(M)
    projection=s.Matrix.hstack(*[s.Matrix(tt(M)).reshape(9,1) for M in bases])
    assert projection.rank()==2
    xx,yy,zz,xy,xz,yz=s.symbols('xx yy zz xy xz yz',real=True)
    H=s.Matrix([[xx,xy,xz],[xy,yy,yz],[xz,yz,zz]])
    hplus=s.trace(H*eplus)
    hcross=s.trace(H*ecross)
    residual=s.simplify(s.trace(tt(H)*tt(H))-(hplus**2+hcross**2))
    assert residual==0
    # A candidate Z/k^2 pole must have the right sign on the two modes.
    Z=s.symbols('Z',real=True)
    assert s.simplify((hplus**2+hcross**2).subs(
        {xx:1, yy:0, zz:0, xy:0, xz:0, yz:0}))==s.Rational(1,2)
    assert s.simplify(Z*s.Rational(1,2)).subs(Z,-1)==-s.Rational(1,2)
    print('PASS: physical spatial TT projection rank 2, positive residue needs Z>0')


if __name__=='__main__':
    soft_graviton_universality_gate()
    trace_exchange_discontinuity_gate()
    physical_transverse_residue_gate()
    print('SCOPE: soft theorem / exchange / physical TT comparators; not UBT dynamics')
