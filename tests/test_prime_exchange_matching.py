# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from verify_prime_exchange_matching import verify


def test_matching_and_vertex_cover_certificates():
    r = verify(limit=1000)
    assert r['sweep_excess_cutoffs'] == []
    row = r['samples'][-1]
    assert row['N'] == 1000
    assert row['toggle']['unmatched'] == 164
    assert row['exchange']['unmatched'] == 2
