# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
"""Exact prime-subset diagnostics. No random-sign or RH assumption."""
import json
from itertools import combinations
from math import prod
from verify_prime_pairing import trial_moebius


def subsets(primes):
    return [(prod(s), (-1)**r) for r in range(len(primes)+1)
            for s in combinations(primes, r)]


def counts(primes, n):
    even = sum(d <= n and sign == 1 for d, sign in subsets(primes))
    odd = sum(d <= n and sign == -1 for d, sign in subsets(primes))
    return even, odd


def verify():
    cases = 0
    for primes in [(2,), (2, 3), (2, 3, 5), (2, 3, 5, 7)]:
        q = prod(primes)
        terms = subsets(primes)
        assert len(terms) == len({d for d, _ in terms}) == 2**len(primes)
        assert sum(sign for _, sign in terms) == 0
        assert counts(primes, q) == (2**(len(primes)-1),)*2
        for n in range(q + 2):
            e, o = counts(primes, n)
            expected = sum(trial_moebius(d) for d in range(1, n + 1) if q % d == 0)
            assert e - o == expected
            assert e + o <= n
            for p in primes:
                remaining = tuple(r for r in primes if r != p)
                rest = subsets(remaining)
                difference = sum(s for d, s in rest if d <= n) - sum(s for d, s in rest if d <= n // p)
                band = sum(s for d, s in rest if n // p < d <= n)
                assert expected == difference == band
                cases += 1
    samples = []
    for n in range(31):
        primes = tuple(p for p in range(2, n+1)
                       if all(p % d for d in range(2, int(p**0.5)+1)))
        e, o = counts(primes, n)
        assert e - o == sum(trial_moebius(d) for d in range(1, n+1))
        assert e + o == sum(abs(trial_moebius(d)) for d in range(1, n+1))
        if n in (5, 6, 30):
            samples.append({'N': n, 'prime_count': len(primes), 'full_subsets': 2**len(primes),
                            'admissible_subsets': e+o, 'even': e, 'odd': o, 'M': e-o})
    return {'result': 'PASS', 'recurrence_cases': cases, 'all_primes_cutoffs': 31,
            'samples': samples,
            'scope': 'Finite subset identities only; the prime-product/Mobius bridge is independently checked here, not Lean-formalized.'}


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
