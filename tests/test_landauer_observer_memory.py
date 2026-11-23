"""Effective finite-memory diagnostics; not a derivation of UBT dynamics."""
import itertools
from fractions import Fraction

import numpy as np
import pytest
import sympy as s


def entropy(rho):
    ev = np.linalg.eigvalsh(rho)
    assert ev.min() > -1e-12
    ev = ev[ev > 1e-14]
    return -np.dot(ev, np.log(ev))


def marginals(rho):
    tensor = rho.reshape(2, 2, 2, 2)
    return np.trace(tensor, axis1=1, axis2=3), np.trace(tensor, axis1=0, axis2=2)


def mutual(rho):
    memory, reservoir = marginals(rho)
    return entropy(memory) + entropy(reservoir) - entropy(rho)


@pytest.mark.parametrize('population', [0.2, 0.5, 0.8])
@pytest.mark.parametrize('angle', [0.0, 0.37, np.pi / 2])
@pytest.mark.parametrize('coherence', [0.0, 0.1])
def test_thermal_balance_with_coherent_memory(population, angle, coherence):
    beta, gap = 1.7, 0.9
    thermal = np.diag([1.0, np.exp(-beta * gap)])
    thermal /= np.trace(thermal)
    memory = np.array([[1-population, 1j*coherence], [-1j*coherence, population]])
    initial = np.kron(memory, thermal)
    swap = np.array([[1,0,0,0], [0,0,1,0], [0,1,0,0], [0,0,0,1]])
    unitary = np.cos(angle)*np.eye(4) - 1j*np.sin(angle)*swap
    final = unitary @ initial @ unitary.conj().T
    after_m, after_r = marginals(final)
    heat = gap * (after_r[1,1].real-thermal[1,1])
    relative = -entropy(after_r) - np.dot(np.diag(after_r).real, np.log(np.diag(thermal)))
    decrease = entropy(memory)-entropy(after_m)
    assert abs(beta*heat-decrease-mutual(final)-relative) < 1e-12
    assert beta*heat >= decrease-1e-12
    assert abs(entropy(initial)-entropy(final)) < 1e-12
    # A full-rank finite example never implements an exact pure reset.
    assert np.linalg.eigvalsh(after_m).min() > 0


def test_balance_algebra_independent_symbolic_channel():
    mi,mf,ri,rf,joint_i,joint_f,beta_heat = s.symbols('mi mf ri rf joint_i joint_f beta_heat')
    information_i, information_f = mi+ri-joint_i, mf+rf-joint_f
    relative = beta_heat-(rf-ri)
    rhs = mi-mf+information_f-information_i+relative
    assert s.expand(rhs.subs(joint_f,joint_i)-beta_heat) == 0


def test_correlations_pay_for_zero_heat_reset():
    # Thermal reservoir H_R=0, but initial MR is correlated, not a product.
    initial = np.diag([0.5,0,0,0.5])
    # CNOT with R controlling M: 00->00, 11->01.
    unitary = np.zeros((4,4))
    for m,r in itertools.product(range(2), repeat=2):
        unitary[2*(m^r)+r,2*m+r]=1
    final = unitary @ initial @ unitary.T
    mi,ri = marginals(initial)
    mf,rf = marginals(final)
    assert np.allclose(mf, np.diag([1,0]))
    assert np.allclose(ri, np.eye(2)/2) and np.allclose(rf,ri)
    decrease=entropy(mi)-entropy(mf)
    assert decrease > 0
    # Q=0, D=0: the product-state lower bound fails, generalized equality holds.
    assert abs(decrease + mutual(final)-mutual(initial)) < 1e-12


def pushforward(distribution, transform):
    output={}
    for state,weight in distribution.items():
        image=transform(state)
        output[image]=output.get(image,Fraction(0))+weight
    return output


def test_erasure_hides_distinct_joint_histories_exactly():
    half=Fraction(1,2)
    same={(0,0):half,(1,1):half}
    opposite={(0,1):half,(1,0):half}
    assert same != opposite
    for axis in (0,1):
        assert pushforward(same,lambda x:x[axis]) == pushforward(opposite,lambda x:x[axis])
    assert pushforward(same,lambda x:(x[0],0)) == pushforward(opposite,lambda x:(x[0],0))


def test_erasure_hides_classical_extension_obstruction():
    # Any positive mass must obey all three almost-sure pair constraints.
    states=list(itertools.product(range(2), repeat=3))
    assert not [x for x in states if x[0]==x[1] and x[1]==x[2] and x[0]!=x[2]]
    half=Fraction(1,2)
    # Before reset: AB and BC are correlated; AC is anticorrelated.
    correlated={(0,0):half,(1,1):half}
    anticorrelated={(0,1):half,(1,0):half}
    ab_after=pushforward(correlated,lambda x:(x[0],0))
    bc_after=pushforward(correlated,lambda x:(0,x[1]))
    extension={(0,0,1):half,(1,0,0):half}
    assert pushforward(extension,lambda x:x[:2])==ab_after
    assert pushforward(extension,lambda x:x[1:])==bc_after
    assert pushforward(extension,lambda x:(x[0],x[2]))==anticorrelated
