from pathlib import Path
import subprocess
import sys
def test_four_real_composite_velocity_hessian():
    f=Path(__file__).resolve().parents[1]/"tools"/"verify_composite_vector4_hessian.py"
    p=subprocess.run([sys.executable,str(f)],check=True,capture_output=True,text=True)
    assert "4x4 Hessian exactly zero" in p.stdout
