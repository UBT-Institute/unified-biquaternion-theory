"""Independent exterior-form variation of Palatini Holst parent action."""
from tools.verify_palatin_holst_parent_euler import run_checks


def test_full_parent_spin_and_tetrad_curvature_variation():
    checks=run_checks()
    assert len(checks)==9,checks
    assert all(checks.values()),{k:v for k,v in checks.items() if not v}
