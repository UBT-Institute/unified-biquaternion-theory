"""Regression for exact flat-gradient Dirac constraint certificates.

Scope: restricted composite pure-gradient branch only, not canonical UBT
gravity or a real CMB observation.
"""
from tools.verify_flat_gradient_dirac import verify_flat_gradient_dirac


def test_flat_gradient_dirac_exact_jets():
    checks=verify_flat_gradient_dirac()
    assert len(checks) == 10
    assert all(checks.values()), {name: ok for name, ok in checks.items() if not ok}
