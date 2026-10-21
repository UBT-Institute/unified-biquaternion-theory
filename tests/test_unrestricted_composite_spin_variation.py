"""First-jet and functional variation of unrestricted composite Lorentz spin field."""
from tools.verify_unrestricted_composite_spin_variation import verify_unrestricted_composite_spin


def test_unrestricted_spin_variational_chain_and_pointwise_rank():
    checks=verify_unrestricted_composite_spin()
    assert len(checks)==12, checks
    assert all(checks.values()), {name:ok for name,ok in checks.items() if not ok}
