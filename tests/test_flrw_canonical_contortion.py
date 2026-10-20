"""Restricted canonical contortion-closed-FLRW exact algebra checks."""
from tools.verify_flrw_canonical_contortion import verify


def test_canonical_contortion_rotor_completion():
    results = verify()
    assert len(results) == 13, results
    assert all(results.values()), {k: v for k, v in results.items() if not v}
