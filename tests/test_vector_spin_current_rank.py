import subprocess,sys
from pathlib import Path
def test_vector_spin_current_rank():
    script=Path(__file__).resolve().parents[1]/"tools"/"verify_vector_spin_current_rank.py"
    p=subprocess.run([sys.executable,str(script)],capture_output=True,text=True,check=True)
    assert "rank=12" in p.stdout
