import subprocess
import sys
from pathlib import Path

def test_positive_slice_and_boost_escape():
    f=Path(__file__).resolve().parents[1]/"tools"/"verify_theta_positive_slice.py"
    p=subprocess.run([sys.executable,str(f)],capture_output=True,text=True,check=True)
    assert "maximal positive linear dimension=2" in p.stdout
    assert "infinitesimal boost exits" in p.stdout
