"""Regression for a restricted KK doublet and exact Lorentz/translation commutants."""
from tools.verify_psi_mode_weak_obstruction import verify_psi_mode_weak_obstruction


def test_restricted_psi_pair_no_go():
    checks=verify_psi_mode_weak_obstruction()
    assert len(checks)==19, checks
    assert all(checks.values()), {name:value for name,value in checks.items() if not value}
