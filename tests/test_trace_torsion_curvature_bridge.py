"""Regression: exact torsion-curvature scalar and FLRW nonminimal coupling match.

Only verifies independent metric/connection scalar--Cartan comparison,
not the complete composite UBT equations or a Planck CMB likelihood.
"""
from tools.verify_trace_torsion_curvature_bridge import verify_trace_torsion_bridge


def test_trace_torsion_curvature_bridge_exact():
    checks=verify_trace_torsion_bridge()
    assert len(checks)==14, checks
    assert all(checks.values()), {k:v for k,v in checks.items() if not v}
