import importlib.util
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("action_gate", Path(__file__).resolve().parents[1] / "tools" / "check_single_ubt_action.py")
gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gate)

def test_prose_reference_is_allowed():
    assert gate.declarations(Path("elsewhere.md"), "We refer to S_UBT here.\n") == []

def test_structured_definition_detected():
    assert gate.declarations(Path("elsewhere.tex"), "\\newcommand{\\S_UBT}{X}\n") == [1]

def test_off_canonical_definition_rejected(tmp_path):
    (tmp_path / "research_tracks").mkdir()
    (tmp_path / "research_tracks" / "bad.md").write_text("DEFINE_S_UBT = S_UBT\n")
    assert len(gate.scan(tmp_path)) == 1

def test_canonical_declaration_permitted(tmp_path):
    p = tmp_path / "canonical" / "THEORY" / "canonical"
    p.mkdir(parents=True)
    (p / "canonical_action.tex").write_text("\\newcommand{\\S_UBT}{X}\n")
    assert gate.scan(tmp_path) == []

def test_family_name_not_banned():
    assert gate.declarations(Path("candidate.tex"), "S_Theta = ...\n") == []
