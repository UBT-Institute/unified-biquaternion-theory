"""Exact invariant bivector/tensor potential identities, not a UBT action proof."""
from tools.verify_bivector_potential_invariants import verify_bivector_potential


def test_bivector_potential_invariants_and_background_variations():
    checks=verify_bivector_potential()
    assert len(checks)==10, checks
    assert all(checks.values()), {key: value for key,value in checks.items() if not value}
