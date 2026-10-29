# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from verify_parity_layers import verify


def test_layer_identity_and_actual_prime_products():
    r = verify()
    assert r['direct_subsets'] == 1048576
    assert r['signed'] == 92378
