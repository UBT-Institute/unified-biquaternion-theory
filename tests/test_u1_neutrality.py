"""Regression against a conjugation/left-action swap and neutral-mode overclaim."""
import importlib.util
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("u1_neutrality", ROOT / "tools/verify_u1_neutrality.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
OLD_SPEC = importlib.util.spec_from_file_location("qed_phi", ROOT / "tools/verify_qed_phi_const.py")
OLD = importlib.util.module_from_spec(OLD_SPEC)
OLD_SPEC.loader.exec_module(OLD)


def test_exact_erratum_and_real_lorentz_commutant():
    record = MODULE.exact_checks()
    assert record["lorentz_commutant_dimension"] == 4
    assert record["left_phase_variation"] != record["conjugation_variation"]


def test_independent_complex_matrix_and_two_body_checks():
    assert MODULE.numeric_checks()["passed"]


def test_old_mass_api_requires_charge_and_fixes_normalization():
    with pytest.raises(TypeError):
        OLD.photon_mass_squared()
    assert OLD.photon_mass_squared(q_phi=0, e=2, v=3) == 0
    assert OLD.photon_mass_squared(q_phi=1, e=2, v=3) == 72
    assert OLD.photon_mass_squared(q_phi=1, e=2, v=3j) == 72
    assert OLD.check_photon_massless()


def test_charge_is_not_assumed_by_beta_comparison():
    with pytest.raises(TypeError):
        OLD.compute_delta_B(phi=1)
    assert OLD.compute_delta_B(phi=1, q_phi=0) == 0
    with pytest.raises(ValueError):
        OLD.compute_delta_B(phi=1, q_phi=1)


def test_uniform_fiber_profile_has_no_nonzero_harmonic_overlap():
    n = 64
    psi = np.arange(n) * 2 * np.pi / n
    profile = np.ones(n)
    overlap = np.fft.fft(profile) / n
    np.testing.assert_allclose(overlap[1:], 0, atol=1e-15)
    # Nonuniform profiles have an overlap; this is not proof of a physical pole.
    localized = 1 + .2 * np.cos(3 * psi)
    assert abs(np.fft.fft(localized)[3] / n) == pytest.approx(.1)


def test_composite_fourier_normalization_and_reality_without_aliasing():
    rng = np.random.default_rng(289)
    length, count = 2 * np.pi * .8, 32
    psi = np.arange(count) * length / count
    modes = {n: rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2))
             for n in range(-2, 3)}
    sharp = lambda x: np.trace(x) * np.eye(2) - x
    field = np.array([sum(a * np.exp(2j*np.pi*n*p/length) / np.sqrt(length)
                          for n, a in modes.items()) for p in psi])
    # Independently evaluate the real quadratic expression in matrix entries.
    values = 2*(field[:, 1, 1]*field[:, 0, 0].conj()).real
    values -= abs(field[:, 0, 1])**2 + abs(field[:, 1, 0])**2
    for m in range(-4, 5):
        integrated = length/count * np.sum(
            np.exp(-2j*np.pi*m*psi/length) / np.sqrt(length) * values)
        convolved = sum(np.trace(sharp(modes[n+m]) @ modes[n].conj().T)
                        for n in modes if n+m in modes) / np.sqrt(length)
        assert integrated == pytest.approx(convolved, abs=2e-13)


def test_lorentz_neutral_invariant_is_not_a_positive_norm():
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    assert np.trace((np.trace(x)*np.eye(2)-x) @ x.conj().T).real == -2


def test_unmatched_scalar_loop_estimate_is_not_exposed_as_a_prediction():
    with pytest.raises(NotImplementedError):
        OLD.schwinger_phi_correction()
    with pytest.raises(TypeError):
        OLD.alpha_running_ubt_phi_const(mu=1, phi=1)
