"""Full variation on a declared branch; preserve all scope restrictions."""
import pytest

from tools.verify_flat_jet_torsion_action import numerical_checks, symbolic_checks


@pytest.mark.parametrize("name",sorted(symbolic_checks()))
def test_exact_flat_jet_torsion_result(name):
    assert symbolic_checks()[name],name


def test_independent_nonzero_connection_composite_first_variation():
    report=numerical_checks()
    assert all(report["checks"].values()),report
