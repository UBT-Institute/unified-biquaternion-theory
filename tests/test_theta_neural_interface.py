"""Time-domain, passivity, and boundary checks for a speculative comparator."""

import importlib.util
from pathlib import Path
import sys

import numpy as np
import pytest


ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "speculative_extensions/consciousness/theta_neural_interface/model.py"
spec = importlib.util.spec_from_file_location("theta_neural_test_model", MODEL)
model = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = model
spec.loader.exec_module(model)


def test_zero_coupling_recovers_neural_baseline():
    p = model.Parameters(coupling=0)
    for omega in np.linspace(0, 3, 31):
        response = p.susceptibility(omega)
        expected = 1/(p.omega_n**2-omega**2-1j*p.gamma_n*omega)
        np.testing.assert_allclose(response, [expected, 0], rtol=2e-14, atol=1e-14)


def test_coupling_sign_is_unidentifiable_from_neural_autoresponse():
    positive, negative = model.Parameters(coupling=.4), model.Parameters(coupling=-.4)
    for omega in (.2, .9, 1.3, 2.0):
        plus, minus = positive.susceptibility(omega), negative.susceptibility(omega)
        np.testing.assert_allclose(plus[0], minus[0])
        np.testing.assert_allclose(plus[1], -minus[1])


@pytest.mark.parametrize("coupling", [1.3, -1.3, 1.31, -1.31])
def test_marginal_and_unstable_energy_are_rejected(coupling):
    with pytest.raises(ValueError, match="strict stability"):
        model.Parameters(omega_n=1, omega_z=1.3, coupling=coupling)


@pytest.mark.parametrize("changes", [{"omega_n":0}, {"gamma_z":-1},
                                         {"coupling":float("nan")}, {"omega_z":float("inf")}])
def test_nonphysical_parameter_inputs_are_rejected(changes):
    with pytest.raises(ValueError):
        model.Parameters(**changes)


def test_retarded_response_has_passive_sign_and_reality_symmetry():
    p = model.Parameters(coupling=.6)
    for omega in np.geomspace(.001, 30, 100):
        plus, minus = p.susceptibility(omega), p.susceptibility(-omega)
        assert plus[0].imag > 0
        np.testing.assert_allclose(minus, plus.conjugate(), rtol=1e-13)


def test_time_domain_response_matches_complex_susceptibility():
    p = model.Parameters(coupling=.4)
    omega = .95
    times = np.linspace(0, 500, 2501)
    states = model.simulate(p, times, drive_frequency=omega, drive_amplitude=1)
    late = times >= 300
    basis = np.column_stack((np.cos(omega*times[late]), np.sin(omega*times[late])))
    fitted, *_ = np.linalg.lstsq(basis, states[late, :2], rcond=None)
    measured = fitted[0] + 1j*fitted[1]
    np.testing.assert_allclose(measured, p.susceptibility(omega), rtol=2e-8, atol=2e-9)


def test_unforced_energy_obeys_damping_balance():
    p = model.Parameters(coupling=.8)
    times = np.linspace(0, 100, 10001)
    states = model.simulate(p, times, initial=[1, -.4, .3, -.2])
    energy = p.energy(states)
    dissipated_power = p.gamma_n*states[:, 2]**2 + p.gamma_z*states[:, 3]**2
    dissipated = np.trapezoid(dissipated_power, times)
    assert np.max(np.diff(energy)) < 2e-10
    assert energy[-1] < 1e-5*energy[0]
    np.testing.assert_allclose(energy[0]-energy[-1], dissipated, rtol=2e-5)


def test_near_boundary_remains_stable_without_claiming_coherence():
    p = model.Parameters(coupling=1.3*(1-1e-6))
    assert np.linalg.eigvalsh(p.stiffness()).min() > 0
    assert np.linalg.eigvals(p.drift()).real.max() < 0
