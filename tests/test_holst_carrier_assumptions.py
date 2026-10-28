"""Catch unsupported carrier/symmetry/phase changes before Hamiltonian reduction."""
import pytest

from tools.verify_physics_closure import carrier_checks, dilation_comparator_checks


@pytest.mark.parametrize("name", sorted(carrier_checks()))
def test_carrier_and_reality_assumptions(name):
    assert carrier_checks()[name], name


@pytest.mark.parametrize("name", sorted(dilation_comparator_checks()))
def test_conditional_dilation_variation(name):
    assert dilation_comparator_checks()[name], name
