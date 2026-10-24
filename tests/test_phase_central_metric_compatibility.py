"""Exact quaternion-sharp central metric versus scalar U1 phase."""
from tools.verify_phase_central_metric_compatibility import verify

def test_phase_action_on_canonical_metric():
    checks=verify()
    assert len(checks)==12,checks
    assert all(bool(v) for v in checks.values()), {k:v for k,v in checks.items() if not bool(v)}
