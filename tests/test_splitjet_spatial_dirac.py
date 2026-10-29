"""Keep the conditional gravity parent and its full spatial mixed brackets honest."""
import pytest

from tools.verify_splitjet_spatial_dirac import numerical_checks, symbolic_checks


@pytest.mark.parametrize("name", sorted(symbolic_checks()))
def test_exact_parent_reduction(name):
    assert symbolic_checks()[name], name


def test_three_dimensional_periodic_graph_dirac_bracket():
    report = numerical_checks()
    assert all(report["checks"].values()), report
