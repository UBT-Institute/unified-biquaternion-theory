from tools.verify_theta_kinetic_signature import verify


def test_exact_invariant_kinetic_signature_and_vacuum_normal():
    result = verify()
    assert result["invariant_pairing_signature"] == {"positive": 2, "negative": 6}
    assert result["normal_kinetic_signature"] == {"positive": 1, "negative": 3}
    assert result["orbit_dimension"] == result["normal_dimension"] == 4


def test_auxiliary_gauge_elimination_preserves_indefinite_normal():
    result = verify()
    assert result["auxiliary_temporal_gauge_elimination"].startswith("PASS")
