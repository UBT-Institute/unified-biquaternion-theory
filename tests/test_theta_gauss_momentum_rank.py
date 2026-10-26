from pathlib import Path
import subprocess
import sys

def test_linearized_gauss_rank():
    script=Path(__file__).resolve().parents[1]/"tools"/"verify_theta_gauss_momentum_rank.py"
    run=subprocess.run([sys.executable,str(script)],check=True,text=True,capture_output=True)
    assert "rank=3 of 6" in run.stdout
