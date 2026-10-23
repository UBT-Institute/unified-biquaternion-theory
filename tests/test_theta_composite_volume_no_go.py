"""Restricted composite-metric no-go for the minimal auxiliary-connection family."""
from tools.verify_theta_composite_volume_no_go import verify


def test_composite_metric_collapses_kinetic_to_volume():
    record = verify()
    assert record["central_metric_pairing_identity"] == "PASS"
    assert record["composite_kinetic_trace"] == "-8*N0 (four spacetime dimensions)"
    assert record["quartic_nonconstant"] is True


def test_nonconstant_potential_forces_degenerate_tetrad():
    record = verify()
    assert record["nondegenerate_stationarity_requires"] == "U(rho)=4*c*N0"
    assert record["resulting_rho_on_connected_patch"] == "constant"
    assert record["resulting_composite_tetrad_rank_at_most"] == 3
