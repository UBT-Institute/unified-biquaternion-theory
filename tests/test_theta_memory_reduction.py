"""Conditional mode-memory reduction; no microscopic UBT action is inferred."""
import math

import numpy as np
import pytest
import sympy as s

x, y, a, c = s.symbols('x y a c', real=True)
k, lam, kap = s.symbols('k lam kap', positive=True)


def test_static_square_completion_and_coefficients():
    energy = a*x*x/2 + lam*x**4/4 + k*y*y/2-c*x*y
    effective = energy.subs(y,c*x/k)
    assert s.expand(effective-((a-c*c/k)*x*x/2+lam*x**4/4)) == 0
    assert s.expand(energy-(k*(y-c*x/k)**2/2+effective)) == 0
    assert s.diff(energy,x,4)/6 == lam
    assert s.diff(energy,x,y) == -c


def test_minima_and_barrier_symbolically():
    potential = -kap*x*x/2+lam*x**4/4
    minimum=s.sqrt(kap/lam)
    for point in (minimum,-minimum):
        assert s.simplify(s.diff(potential,x).subs(x,point)) == 0
        assert s.simplify(s.diff(potential,x,2).subs(x,point)-2*kap) == 0
        assert s.simplify(potential.subs(x,0)-potential.subs(x,point)-kap**2/(4*lam)) == 0
    assert s.diff(potential,x,2).subs(x,0) == -kap


@pytest.mark.parametrize('coefficients', [(1.,2.,2.,.7),(-1.,1.,.4,2.),(.2,3.,2.,1.5)])
def test_full_hessian_stability_independent_numeric(coefficients):
    av,kv,cv,lv=coefficients
    effective_k=cv*cv/kv-av
    assert effective_k>0
    minimum=math.sqrt(effective_k/lv)
    hessian=np.array([[av+3*lv*minimum**2,-cv],[-cv,kv]])
    assert np.linalg.eigvalsh(hessian).min()>0
    assert np.linalg.eigvalsh(np.array([[av,-cv],[-cv,kv]])).min()<0
    energy=lambda xv,yv: av*xv*xv/2+lv*xv**4/4+kv*yv*yv/2-cv*xv*yv
    assert math.isclose(energy(0,0)-energy(minimum,cv*minimum/kv),effective_k**2/(4*lv))


def test_strictly_convex_comparator_does_not_store_a_bistable_bit():
    # a=2, k=1, c=1, lambda=1: the reduced potential is x²/2+x⁴/4.
    derivative=x+x**3
    assert s.solveset(derivative,x,domain=s.S.Reals)==s.FiniteSet(0)
    assert s.diff(derivative,x)==1+3*x*x


def test_zero_quadratic_case_has_one_minimum():
    assert s.solveset(lam*x**3,x,domain=s.S.Reals)==s.FiniteSet(0)


def test_write_threshold_is_a_saddle_node():
    force=2*kap**s.Rational(3,2)/(3*s.sqrt(3*lam))
    saddle=-s.sqrt(kap/(3*lam))
    assert s.simplify((lam*x**3-kap*x-force).subs(x,saddle))==0
    assert s.simplify((3*lam*x*x-kap).subs(x,saddle))==0


def test_storage_error_solves_master_equation():
    rate,time=s.symbols('rate time', positive=True)
    p=(1-s.exp(-2*rate*time))/2
    assert s.simplify(s.diff(p,time)-rate*(1-2*p))==0
    assert p.subs(time,0)==0
    # Endpoint error is not probability of ever leaving the starting well.
    assert s.simplify((1-s.exp(-rate*time))-p) != 0


@pytest.mark.parametrize('error,time,attempt',[(.01,100.,1.),(.1,10.,5.),(.001,1e4,100.)])
def test_retention_bound_saturates_independently(error,time,attempt):
    beta_barrier=math.log(2*attempt*time/(-math.log1p(-2*error)))
    rate=attempt*math.exp(-beta_barrier)
    actual=-math.expm1(-2*rate*time)/2
    assert math.isclose(actual,error,rel_tol=1e-12)
    worse=-math.expm1(-2*rate*math.exp(.1)*time)/2
    assert worse>error


def test_detailed_balance_and_relaxation():
    beta,gap,rate,time=s.symbols('beta gap rate time',positive=True)
    p0=s.symbols('p0',real=True)
    eq=1/(1+s.exp(beta*gap))
    up,down=rate*eq,rate*(1-eq)
    assert s.simplify(up/down-s.exp(-beta*gap))==0
    p=eq+(p0-eq)*s.exp(-rate*time)
    assert s.simplify(s.diff(p,time)-(up*(1-p)-down*p))==0
    assert s.simplify(p.subs(time,0)-p0)==0


def test_reset_work_integrand_and_heat_derivative():
    beta,gap=s.symbols('beta gap',positive=True)
    eq=1/(1+s.exp(beta*gap))
    work=(s.log(2)-s.log(1+s.exp(-beta*gap)))/beta
    assert s.simplify(s.diff(work,gap)-eq)==0
    assert work.subs(gap,0)==0
    heat=work-gap*eq
    # At fixed T, the entropy-balance derivative is -dS/beta.
    entropy=-eq*s.log(eq)-(1-eq)*s.log(1-eq)
    assert s.simplify(s.expand_log(s.diff(heat+entropy/beta,gap),force=True))==0


@pytest.mark.parametrize('beta,gap',[(.5,.2),(1.,2.),(2.,5.)])
def test_closed_reset_cycle_against_numerical_quadrature(beta,gap):
    grid=np.linspace(0,gap,100001)
    p=1/(1+np.exp(beta*grid))
    raised=np.sum((p[1:]+p[:-1])*np.diff(grid)/2)
    error=1/(1+math.exp(beta*gap))
    entropy=-error*math.log(error)-(1-error)*math.log1p(-error)
    heat=raised-gap*error
    assert abs(heat-(math.log(2)-entropy)/beta)<1e-9
    assert 0<heat<math.log(2)/beta
    assert raised>heat  # Raising work alone is not cycle heat.


def test_same_barrier_does_not_select_memory_dynamics():
    scale=s.symbols('scale',positive=True)
    barrier=kap**2/(4*lam)
    assert s.simplify((scale*kap)**2/(4*scale**2*lam)-barrier)==0
    assert s.simplify(s.sqrt(scale*kap/(scale**2*lam))-s.sqrt(kap/lam)/s.sqrt(scale))==0
    assert (2*kap).subs(kap,scale*kap) != 2*kap


def test_full_complex_phase_bypasses_the_real_axis_barrier():
    v=s.symbols('v',positive=True)
    phase=s.symbols('phase',real=True)
    mass2,l1,l2,V0=s.symbols('mass2 l1 l2 V0',real=True)
    theta=v*s.exp(s.I*phase)*s.eye(2)
    # For a scalar biquaternion, sharp leaves the scalar unchanged.
    invariant=s.simplify(s.trace(theta*theta.H))
    determinant_square=s.simplify(theta.det()*s.conjugate(theta.det()))
    assert invariant==2*v*v and determinant_square==v**4
    potential=s.expand(V0+mass2*invariant+l1*invariant**2+l2*determinant_square)
    assert s.diff(potential,phase)==0
    assert theta.subs(phase,0)==v*s.eye(2)
    assert s.simplify(theta.subs(phase,s.pi)+v*s.eye(2))==s.zeros(2)
    assert s.expand(potential-(V0+2*mass2*v*v+(4*l1+l2)*v**4))==0


def test_raw_normalized_readout_cannot_distinguish_the_sign_bit():
    theta=s.Matrix([[2,s.I],[1-s.I,1]])
    density=lambda field:s.simplify(field*field.H/s.trace(field*field.H))
    assert density(theta)==density(-theta)
