"""Exact examples supporting the geometric first-jet orbit theorem."""
from tools.verify_firstjet_natural_invariants import verify

def test_firstjet_algebraic_invariants_reduce_to_field_norm():
    checks=verify()
    assert len(checks)==23,checks
    assert all(checks.values()),{k:v for k,v in checks.items() if not v}
