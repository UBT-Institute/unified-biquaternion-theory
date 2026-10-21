"""Independent symbolic regression for the all-C2-potential minimal-action closure."""
from tools.verify_minimal_all_C2_potentials import verify

def test_minimal_action_all_C2_potential_dichotomy():
    checks=verify()
    assert len(checks)==14, checks
    assert all(checks.values()), {name:ok for name,ok in checks.items() if not ok}
