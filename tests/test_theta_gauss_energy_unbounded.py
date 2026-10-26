from pathlib import Path
import subprocess
import sys
def test_negative_gauss_witness():
    path=Path(__file__).resolve().parents[1]/"tools"/"verify_theta_gauss_energy_unbounded.py"
    r=subprocess.run([sys.executable,str(path)],capture_output=True,text=True,check=True)
    assert "Unbounded below" in r.stdout
