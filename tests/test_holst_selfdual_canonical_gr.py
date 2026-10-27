"""Independent reconstruction of the proposed match, including its reality gap.

This is not a supplied Claude test file: the formulas were rederived here.
"""
import pytest

from tools.verify_physics_closure import selfdual_checks


@pytest.mark.parametrize("name", sorted(selfdual_checks()))
def test_holst_selfdual_match_and_admissibility(name):
    assert selfdual_checks()[name], name
