# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"tools"))
from verify_abel_limit import verify


def test_exact_remainders_and_conditional_series():
    assert verify()["result"] == "PASS"
