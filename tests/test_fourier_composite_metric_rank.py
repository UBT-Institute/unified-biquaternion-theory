"""Exact frozen Fourier map, not the Euler/Dirac principal symbol."""
from tools.verify_fourier_composite_metric_rank import verify


def test_fourier_composite_metric_normal_rank():
    checks=verify()
    assert len(checks)==16, checks
    assert all(checks.values()),{k:v for k,v in checks.items() if not v}
