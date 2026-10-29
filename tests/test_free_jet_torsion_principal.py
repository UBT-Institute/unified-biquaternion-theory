"""Principal tensor audit; success confirms the scoped obstruction."""
import pytest

from tools.verify_free_jet_torsion_principal import numerical_checks, symbolic_checks


@pytest.mark.parametrize("name", sorted(symbolic_checks()))
def test_exact_free_jet_tensor_result(name):
    assert symbolic_checks()[name], name


def test_original_nonflat_jet_and_independent_auxiliary_elimination():
    report = numerical_checks()
    assert all(report["checks"].values()), report
