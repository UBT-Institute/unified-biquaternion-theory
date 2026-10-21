"""Exact exterior form and reduced composite Palatini/Holst Euler checks."""
from tools.verify_composite_palatin_holst_flrw import verify


def test_composite_palatin_holst_homogeneous_Euler_system():
    checks=verify()
    assert len(checks)==19, checks
    assert all(checks.values()),{key:value for key,value in checks.items() if not value}
