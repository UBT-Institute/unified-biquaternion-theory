# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
"""Exact finite checks; these do not prove asymptotic cancellation or RH."""
import json
from itertools import accumulate


def trial_moebius(n):
    if n == 0:
        return 0
    sign, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
        p += 1
    return -sign if n > 1 else sign


def verify(limit=200_000):
    assert limit >= 11
    mu = [1] * (limit + 1)
    mu[0] = 0
    composite = bytearray(limit + 1)
    for p in range(2, limit + 1):
        if composite[p]:
            continue
        for n in range(p, limit + 1, p):
            mu[n] = -mu[n]
            if n > p:
                composite[n] = 1
        for n in range(p * p, limit + 1, p * p):
            mu[n] = 0
    for n in range(min(limit, 2000) + 1):
        assert mu[n] == trial_moebius(n), ('independent factorization', n)
    mertens = list(accumulate(mu))
    primes = [2, 3, 5, 7, 11]
    for p in primes:
        free = [mu[n] if n % p else 0 for n in range(limit + 1)]
        sums = list(accumulate(free))
        for n in range(limit + 1):
            assert mu[n] == free[n] - (free[n // p] if n % p == 0 else 0)
            assert mertens[n] == sums[n] - sums[n // p], (p, n)
            lower = n // p
            count = (n - n // p) - (lower - lower // p)
            assert abs(mertens[n]) <= count, (p, n, count)
            if p == 2:
                assert count == (n + 1) // 2 - (n // 2 + 1) // 2
        for m in range(limit // p + 1):
            assert mu[p * m] == -free[m]
    return {'result': 'PASS', 'limit': limit, 'primes': primes,
            'band_cases': len(primes) * (limit + 1),
            'independent_factorizations': min(limit, 2000) + 1,
            'scope': 'Finite integer checks only; no asymptotic bound or RH proof.'}


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
