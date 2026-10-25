"""Protect the combined bilingual build and explicit email opt-in during integration."""
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_email_delivery_requires_manual_opt_in():
    workflow = yaml.load((ROOT / ".github/workflows/textbook.yml").read_text(), Loader=yaml.BaseLoader)
    option = workflow["on"]["workflow_dispatch"]["inputs"]["send_email"]
    assert option["default"] == "false"
    steps = workflow["jobs"]["build-textbook"]["steps"]
    send = [step for step in steps if "SMTP" in step.get("run", "") or "email secrets" in step.get("name", "")]
    assert len(send) == 2
    for step in send:
        guard = step["if"]
        assert "github.event_name == 'workflow_dispatch'" in guard
        assert "inputs.send_email == true" in guard
        assert "github.ref == 'refs/heads/master'" in guard
        assert "||" not in guard


def test_only_one_workflow_owns_textbook_delivery():
    assert not (ROOT / ".github/workflows/textbook_build.yml").exists()
    text = (ROOT / "docs/textbook/Makefile").read_text()
    assert "pdfunite $(TEXTBOOK_CS_PDF) $(TEXTBOOK_EN_PDF) $@" in text
    assert "TEXTBOOK_PDF := $(PUBLIC_ROOT)/UBT_Textbook.pdf" in text
