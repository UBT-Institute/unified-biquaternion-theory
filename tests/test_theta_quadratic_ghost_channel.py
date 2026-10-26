from pathlib import Path
import subprocess,sys
def test_reduced_ghost_channel():
    f=Path(__file__).resolve().parents[1]/"tools"/"verify_theta_quadratic_ghost_channel.py"
    p=subprocess.run([sys.executable,str(f)],capture_output=True,text=True,check=True)
    assert "p-Hessian=-1/a" in p.stdout
