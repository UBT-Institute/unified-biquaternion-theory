# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from verify_subset_cancellation import verify


def test_subset_parity_cutoff_and_mobius_bridge():
    r = verify()
    assert r['result'] == 'PASS'
    assert r['samples'][-1]['full_subsets'] == 1024
    assert r['samples'][-1]['admissible_subsets'] == 19
