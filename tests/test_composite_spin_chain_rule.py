"""Functional chain rule for composite-Theta boost and radial Euler equations."""
from tools.verify_composite_spin_chain_rule import verify_composite_variation_chain


def test_composite_spin_chain_rule():
    checks=verify_composite_variation_chain()
    assert len(checks)==5, checks
    assert all(checks.values()), {k:v for k,v in checks.items() if not v}
