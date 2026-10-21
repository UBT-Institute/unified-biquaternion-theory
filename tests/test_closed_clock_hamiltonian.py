"""Exact closed clock minisuperspace Dirac constraint and de Sitter check.

Does not test or assert a finalized fundamental UBT action.
"""
from tools.verify_closed_clock_hamiltonian import verify_closed_clock_hamiltonian


def test_closed_clock_hamiltonian_and_stationary_desitter():
    checks = verify_closed_clock_hamiltonian()
    assert len(checks)==15, checks
    assert all(checks.values()), {k: v for k,v in checks.items() if not v}
