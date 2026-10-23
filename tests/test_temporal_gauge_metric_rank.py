"""Exact off-shell temporal first-jet rank, not a propagating-mode count."""
from tools.verify_temporal_gauge_metric_rank import verify_temporal_rank


def test_temporal_gauge_rank_and_adm_lapse():
    checks = verify_temporal_rank()
    assert len(checks) == 11, checks
    assert all(checks.values()), {name: ok for name, ok in checks.items() if not ok}
