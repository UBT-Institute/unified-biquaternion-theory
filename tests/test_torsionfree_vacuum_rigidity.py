"""Exact conditional timelike torsion-free Einstein vacuum rigidity regression."""
from tools.verify_torsionfree_vacuum_rigidity import verify

def test_ricci_flat_concurrent_vector_is_locally_flat():
    checks=verify()
    assert len(checks)==13, checks
    assert all(checks.values()), {name:ok for name,ok in checks.items() if not ok}
