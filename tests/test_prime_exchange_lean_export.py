# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from export_prime_exchange_lean import generate


def test_generated_certificates_match_checked_sources():
    for n, name in [(100, 'ConcreteExchange'), (1000, 'ConcreteExchange1000')]:
        assert generate(n) == (ROOT / 'formal/lean/UBT/RH' / (name+'.lean')).read_text()
