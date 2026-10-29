"""Regression for the missing imaginary factor and its false spectral check."""
import numpy as np
import pytest
from tools.verify_psi_fock_chirality_selection import rest_hamiltonian, verify


def test_exact_and_independent_numerical_checks():
    assert verify()['numerical_mode_radius_cases'] == 21


@pytest.mark.parametrize('n',[-2,2])
def test_missing_factor_cannot_pass_as_real_energy(n):
    H=rest_hamiltonian(n,1.0)
    wrong=1j*H
    assert not np.allclose(wrong.conj().T,wrong)
    assert np.max(np.abs(np.linalg.eigvals(wrong).imag)) > 1
    assert np.allclose(np.linalg.eigvalsh(H),[-2,-2,2,2])


@pytest.mark.parametrize('radius',[0,-1,np.inf,np.nan])
def test_invalid_radius_is_rejected(radius):
    with pytest.raises(ValueError):
        rest_hamiltonian(1,radius)
