"""The axial-source diagnostic must vary every contortion component."""
import pytest

from tools.verify_holst_spin_source import symbolic_checks, numerical_checks


@pytest.mark.parametrize("name", sorted(symbolic_checks()))
def test_full_sourced_holst_identity(name):
    assert symbolic_checks()[name], name


def test_independent_full_connection_solution():
    report = numerical_checks()
    assert all(report["checks"].values()), report
