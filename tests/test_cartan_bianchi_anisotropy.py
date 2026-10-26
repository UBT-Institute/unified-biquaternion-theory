import subprocess,sys
from pathlib import Path
def test_cartan_bianchi_anisotropy():
    p=Path(__file__).resolve().parents[1]/"tools"/"verify_cartan_bianchi_anisotropy.py"
    result=subprocess.run([sys.executable,str(p)],check=True,capture_output=True,text=True)
    assert "Not SO(3)-invariant" in result.stdout
