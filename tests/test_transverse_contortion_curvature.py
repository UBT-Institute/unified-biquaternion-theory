import subprocess,sys
from pathlib import Path
def test_transverse_contortion_curvature():
    f=Path(__file__).resolve().parents[1]/"tools"/"verify_transverse_contortion_curvature.py"
    p=subprocess.run([sys.executable,str(f)],check=True,capture_output=True,text=True)
    assert "changed curvature" in p.stdout
