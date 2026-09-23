# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from verify_multi_prime_pairing import verify


def test_prime_set_identity_and_boundaries():
    assert verify()['interval_cases'] == 8004
