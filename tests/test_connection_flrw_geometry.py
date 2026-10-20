"""Focus: mathematical identities, never full UBT equations or Planck fit."""
from tools.verify_connection_flrw_geometry import check_connection_closed_flrw


def test_conditional_clifford_connection_closed_flrw_geometry():
    checks = check_connection_closed_flrw()
    assert len(checks) == 11, checks
    assert all(checks.values()), {key: value for key, value in checks.items() if not value}
