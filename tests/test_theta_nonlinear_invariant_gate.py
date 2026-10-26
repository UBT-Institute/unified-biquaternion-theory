from pathlib import Path
import subprocess
import sys

def test_invariant_probe():
    script=Path(__file__).resolve().parents[1]/"tools"/"verify_theta_nonlinear_invariant_gate.py"
    result=subprocess.run([sys.executable,str(script)],capture_output=True,text=True,check=True)
    assert "second derivatives are nonzero" in result.stdout
