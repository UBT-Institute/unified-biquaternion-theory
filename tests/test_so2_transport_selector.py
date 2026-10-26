import subprocess,sys
from pathlib import Path
def test_so2_transport_selector():
    script=Path(__file__).resolve().parents[1]/"tools"/"verify_so2_transport_selector.py"
    p=subprocess.run([sys.executable,str(script)],capture_output=True,text=True,check=True)
    assert "compatibility requires" in p.stdout
