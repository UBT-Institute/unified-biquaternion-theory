import subprocess
import sys
from pathlib import Path

def test_invariant_kinetic_inertia():
    f=Path(__file__).resolve().parents[1]/"tools"/"verify_sl2c_yang_mills_inertia.py"
    p=subprocess.run([sys.executable,str(f)],check=True,capture_output=True,text=True)
    assert "inertia (3,3)" in p.stdout
