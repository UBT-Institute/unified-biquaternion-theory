"""Exact conditional auxiliary trace/axial torsion and clock integration tests."""
from tools.verify_auxiliary_axial_torsion_clock import verify_auxiliary_torsion_no_normal_constraint

def test_auxiliary_axial_torsion_elimination():
    checks=verify_auxiliary_torsion_no_normal_constraint()
    assert len(checks)==14,checks
    assert all(checks.values()), {k:v for k,v in checks.items() if not v}
