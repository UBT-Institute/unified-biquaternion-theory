# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from verify_signed_energy import verify


def test_energy_and_positive_correlation_counterexample():
    assert verify()['positive_cross_counterexample']['cross'] == 3
