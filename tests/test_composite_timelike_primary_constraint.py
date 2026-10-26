import subprocess
import sys
from pathlib import Path

def test_timelike_composite_velocity_hessian():
    script=Path(__file__).resolve().parents[1]/"tools"/"verify_composite_timelike_primary_constraint.py"
    result=subprocess.run([sys.executable,str(script)],capture_output=True,text=True,check=True)
    assert "velocity Hessian: zero" in result.stdout
