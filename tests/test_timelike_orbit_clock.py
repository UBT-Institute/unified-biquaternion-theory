"""Exact invariant timelike-orbit clock and radialization checks (conditional)."""
from tools.verify_timelike_orbit_clock import verify_timelike_orbit_clock


def test_full_positive_hermitian_orbit_keeps_unit_clock():
    checks=verify_timelike_orbit_clock()
    assert len(checks)==8,checks
    assert all(checks.values()), {k: v for k,v in checks.items() if not v}
