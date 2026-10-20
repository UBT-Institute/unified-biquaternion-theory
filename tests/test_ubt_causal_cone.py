"""Causal-cone and holomorphy regression checks for the fixed-background family."""
from tools.verify_ubt_causal_cone import verify


def test_common_characteristic_cone_does_not_imply_positive_energy():
    result = verify()
    assert result["eight_real_principal_determinant"] == (
        "256*kappa**8*(k**2-omega**2/c_light**2)**8"
    )
    assert result["kinetic_inertia_kappa_positive"] == [2, 6]
    assert result["kinetic_sign_changes_characteristic_cone"] is False


def test_holomorphy_does_not_project_out_negative_kinetic_directions():
    result = verify()
    assert result["holomorphic_negative_kinetic_example"] == (
        "z1=a*(t+i*psi)"
    )
    assert result["holomorphy_alone_implies_ghost_freedom"] is False
    assert result["two_mode_toy_characteristic_speeds"] == [
        "c_light", "s*c_light"
    ]
