"""Checks actual projectors, interacting eigenspaces and the nonzero current."""
from tools.verify_chiral_current_interaction import verify


def test_chiral_currents_and_interacting_winding_transport():
    result=verify()
    assert result['numerical_eigenbasis_transport_cases']==12
    assert result['nonzero_left_current_even']=='PASS'
