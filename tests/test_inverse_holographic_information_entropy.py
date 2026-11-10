"""Checks: observer-local entropy need not imply global entropy production or heat.

An exact two-qubit counterexample, not a holographic gravity derivation.
"""
import sympy as sp


def _marginal_A(rho):
    return sp.Matrix(2, 2, lambda i, j:
                     sum(rho[2*i+k, 2*j+k] for k in range(2)))


def test_bell_entanglement_reduces_local_purity():
    psi=sp.Matrix([1,0,0,1])/sp.sqrt(2)
    rho=psi*psi.T
    local=_marginal_A(rho)
    assert local==sp.eye(2)/2
    assert sp.trace(local*local)==sp.Rational(1,2)
    assert sp.trace(rho*rho)==1


def test_pure_product_has_zero_local_entropy():
    psi=sp.Matrix([1,0,0,0])
    rho=psi*psi.T
    local=_marginal_A(rho)
    assert local==sp.diag(1,0)
    assert sp.trace(local*local)==1


def test_entangling_unitary_preserves_global_purity():
    H=sp.Matrix([[1,1],[1,-1]])/sp.sqrt(2)
    I=sp.eye(2)
    CNOT=sp.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
    U=CNOT*sp.kronecker_product(H,I)
    assert sp.simplify(U.T*U)==sp.eye(4)
    assert U*sp.Matrix([1,0,0,0])==sp.Matrix([1,0,0,1])/sp.sqrt(2)


def test_degenerate_hamiltonian_has_zero_internal_energy_change():
    before=sp.Matrix([1,0,0,0])
    after=sp.Matrix([1,0,0,1])/sp.sqrt(2)
    energy=sp.zeros(4)
    assert (before.T*energy*before)[0] == (after.T*energy*after)[0] == 0
