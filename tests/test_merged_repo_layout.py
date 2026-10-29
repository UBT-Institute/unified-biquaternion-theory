"""Regression for the modern layout chosen when resolving the old reorganization."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_plain_python_can_import_the_compatibility_package():
    code = (
        "import forensic_fingerprint; "
        "from forensic_fingerprint.layer2.config_space import Layer2Config; "
        "assert forensic_fingerprint.get_target_root().is_dir(); "
        "assert 'tools/forensic_fingerprint' in str(forensic_fingerprint.get_target_root())"
    )
    subprocess.run([sys.executable, "-c", code], cwd=ROOT, check=True)


def test_legacy_helpers_resolve_preserved_archive_copies():
    import runpy
    helpers = runpy.run_path(str(ROOT / "tests/utils_repo_paths.py"))
    assert helpers["forensic_target_root"]() == ROOT / "tools/forensic_fingerprint"
    for name in ("ubt_with_chronofactor_root", "ubt_no_chronofactor_root"):
        path = helpers[name]()
        assert path.is_dir()
        assert "ARCHIVE" in path.parts
