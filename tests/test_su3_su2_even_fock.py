"""Regression for conditional SU(3)xSU(2)xU(1) even-Fock algebra."""
from tools.verify_su3_su2_even_fock import verify_even_fock_generation


def test_even_exterior_generation_and_anomalies():
    checks = verify_even_fock_generation()
    assert len(checks) == 25, checks
    assert all(checks.values()), {k: v for k, v in checks.items() if not v}
