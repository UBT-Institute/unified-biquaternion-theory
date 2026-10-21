"""Exact Clifford grade and parity/axial Cartan algebra checks."""
from tools.verify_clifford_pseudoscalar_axial_torsion import verify


def test_clifford_pseudoscalar_and_axial_torsion():
    checks=verify()
    assert len(checks)==16,checks
    assert all(checks.values()),{k:v for k,v in checks.items() if not v}
