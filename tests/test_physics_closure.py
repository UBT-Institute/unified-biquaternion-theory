"""Independent algebra, constrained Hamiltonian and numerical closure gates."""
import pytest
from pathlib import Path
import yaml

from tools.verify_physics_closure import fourform_variation_checks, numerical_checks, symbolic_checks


@pytest.mark.parametrize("name", sorted(symbolic_checks()))
def test_exact_physics_closure_identity(name):
    assert symbolic_checks()[name], name


def test_numerical_physics_closure_checks():
    report = numerical_checks()
    assert all(report["checks"].values()), report


def test_all_general_tetrad_Euler_fourform_components():
    checks = fourform_variation_checks()
    assert all(checks.values()), checks


def test_gr_recovery_keeps_its_dynamical_postulate_explicit():
    root = Path(__file__).resolve().parents[1]
    ledger = yaml.safe_load((root / "canonical/gr_closure/gr_recovery_status.yaml").read_text())
    assert ledger["overall_status"] == "CONDITIONAL"
    assert ledger["action_derivation_status"] == "AXIOMATIC_CANDIDATE"
    assert ledger["fundamental_action_selection_status"] == "OPEN_GAP"
    assert ledger["postulate"]["physical_consequence_status"] == "CONDITIONAL"
    assert ledger["audit_2026_10_28"]["holst_coefficient_selection"] == "OPEN_GAP"


def test_phenomenological_alpha_input_cannot_be_promoted():
    root = Path(__file__).resolve().parents[1]
    claims = yaml.safe_load((root / "CLAIMS.yaml").read_text())["claims"]
    assert claims["alpha_full"]["status"] == "OPEN_GAP"
    assert "phenomenological" in " ".join(claims["alpha_full"]["assumptions"])
    assert claims["three_generations"]["status"] == "OPEN_GAP"


def test_both_claim_matrices_scope_physical_recovery_conditionally():
    root = Path(__file__).resolve().parents[1]
    for lang in ("en", "cs"):
        matrix = (root / f"CLAIMS_MATRIX.{lang}.md").read_text()
        physical_rows = [line for line in matrix.splitlines() if line.startswith("| ") and
                         "gravity_dynamical_postulate." in line and "| Primary" not in line]
        assert len(physical_rows) >= 4
        assert all("| CONDITIONAL |" in row for row in physical_rows), physical_rows
