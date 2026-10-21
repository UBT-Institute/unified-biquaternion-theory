"""Conditional anomaly consistency of the canonical UBT exterior carrier."""
from tools.verify_su3_fock_anomalies import verify_su3_fock_anomalies


def test_conditional_fock_anomaly_ledger():
    checks=verify_su3_fock_anomalies()
    assert len(checks)==22, checks
    assert all(checks.values()), {k:v for k,v in checks.items() if not v}
