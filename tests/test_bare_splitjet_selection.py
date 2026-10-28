"""The stated bare/free-jet family must not be called a derivation of GR."""
import pytest
from tools.verify_bare_splitjet_selection import symbolic_checks, numerical_checks


@pytest.mark.parametrize("name", sorted(symbolic_checks()))
def test_bare_splitjet_exact_selection_obstruction(name):
    assert symbolic_checks()[name], name


def test_critical_weight_variation_independent_numeric():
    report = numerical_checks()
    assert all(report["checks"].values()), report
