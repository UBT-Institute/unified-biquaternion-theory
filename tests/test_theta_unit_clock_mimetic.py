"""Regression tests for the conditional unit-clock projected variation."""
from tools.verify_theta_unit_clock_mimetic import verify


def test_unit_clock_mimetic_counterexample():
    result = verify()
    for key in (
        "unit_clock_identity",
        "projected_metric_equations",
        "nondegenerate_example",
        "FLRW_curvature_and_Einstein_tensor",
        "dust_current_conservation",
        "Einstein_vacuum_counterexample",
        "ADM_lapse_constraint_not_imposed",
    ):
        assert result[key] == "PASS"
