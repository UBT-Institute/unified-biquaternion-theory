# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"tools"))
from verify_power_weight_limit import verify


def test_nonreal_power_weights_and_regularization_context():
    assert verify()["result"] == "PASS"
