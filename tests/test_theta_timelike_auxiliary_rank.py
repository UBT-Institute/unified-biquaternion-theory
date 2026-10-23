"""Timelike Lorentz-real auxiliary gauge: healthy scalar but degenerate tetrad."""
from tools.verify_theta_timelike_auxiliary_rank import verify


def test_exact_auxiliary_boost_elimination():
    result = verify()
    assert result["timelike_lorentz_real_potential_reduction"] == "PASS"
    assert result["auxiliary_boost_connection_equations"] == 12
    assert result["reduced_radial_kinetic_energy_for_c_positive"] == "positive"


def test_rank_one_tetrad_blocks_naive_gr_recovery():
    result = verify()
    assert result["on_shell_composite_tetrad_rank"] == 1
    assert result["on_shell_composite_metric_determinant"] == 0
    assert "cannot simultaneously generate a nondegenerate" in result["conclusion"]
