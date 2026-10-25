import subprocess
import sys
from pathlib import Path

def test_exact_sl2c_orbit_inertia():
    script = Path(__file__).resolve().parents[1] / "tools" / "verify_sl2c_orbit_inertia.py"
    result = subprocess.run([sys.executable, str(script)], capture_output=True, text=True, check=True)
    assert "orbit rank=3" in result.stdout
    assert "signature=(2,3)" in result.stdout
