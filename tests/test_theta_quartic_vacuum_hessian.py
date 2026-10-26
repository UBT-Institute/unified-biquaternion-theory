import subprocess
import sys
from pathlib import Path

def test_theta_quartic_vacuum_hessian():
    script=Path(__file__).resolve().parents[1]/"tools"/"verify_theta_quartic_vacuum_hessian.py"
    p=subprocess.run([sys.executable,str(script)],check=True,text=True,capture_output=True)
    assert "generalized mass²" in p.stdout
