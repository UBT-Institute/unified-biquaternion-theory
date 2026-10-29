"""Preserve the full complex carrier and expose the unsolved phase gate."""
import numpy as np
import pytest

from tools.verify_nonlinear_cartan_chart import (
    chart_action, lift_point, numerical_checks, symbolic_checks,
)


@pytest.mark.parametrize("name", sorted(symbolic_checks()))
def test_exact_chart_identity_or_declared_obstruction(name):
    assert symbolic_checks()[name], name


def test_independent_finite_group_transport():
    report = numerical_checks()
    assert all(report["checks"].values()), report


def test_forbidden_chart_data_and_non_group_input_are_rejected():
    for x, ell in [([0, 2, 0, 0], 1), ([0]*4, 0), ([np.nan, 0, 0, 0], 1)]:
        with pytest.raises(ValueError):
            lift_point(x, [0]*4, ell)
    with pytest.raises(ValueError):
        chart_action([0]*4, [1]*4, 1, 2*np.eye(5))


def test_a_group_element_can_leave_this_local_chart():
    group = np.diag([1, -1, 1, 1, -1])
    with pytest.raises(ValueError, match="leaves"):
        chart_action([0]*4, [1]*4, 1, group)
