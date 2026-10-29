# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
"""Independent finite energy checks, with no statistical assumptions."""
import json
from itertools import combinations
import sympy as sp
from verify_prime_pairing import trial_moebius


def verify():
    for n in range(8):
        a = sp.symbols(f'a:{n}')
        pairs = sum(x * y for x, y in combinations(a, 2))
        assert sp.expand(sum(a)**2 - sum(x*x for x in a) - 2*pairs) == 0
    positive = None
    for n in range(301):
        a = [trial_moebius(m) for m in range(n // 2 + 1, n + 1) if m % 2]
        total = sum(trial_moebius(m) for m in range(1, n + 1))
        diag = sum(x*x for x in a)
        pairs = sum(x*y for x,y in combinations(a, 2))
        assert total == sum(a)
        assert total**2 == diag + 2*pairs
        if n == 13:
            assert (total, diag, pairs) == (-3, 3, 3)
            positive = {'N': n, 'M': total, 'diagonal': diag, 'cross': pairs}
    return {'result': 'PASS', 'symbolic_lengths': 8, 'band_cases': 301,
            'positive_cross_counterexample': positive,
            'scope': 'Exact energy identity and counterexample only; no correlation growth estimate.'}


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
