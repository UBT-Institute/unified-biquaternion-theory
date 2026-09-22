# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
"""Finite exact diagnostics for prime-set pairing, not an RH proof."""
from fractions import Fraction
from itertools import combinations, accumulate
from math import gcd, prod
import json
from verify_prime_pairing import trial_moebius


def divisors_with_sign(primes):
    return [(prod(subset), (-1) ** k)
            for k in range(len(primes) + 1)
            for subset in combinations(primes, k)]


def envelope_coefficient(primes):
    divisors = divisors_with_sign(primes)
    points = sorted({Fraction(0), *(Fraction(1, d) for d, _ in divisors)})
    area = sum((b - a) * abs(sum(sign for d, sign in divisors
                                if (a + b) / 2 <= Fraction(1, d)))
               for a, b in zip(points, points[1:]))
    return prod(Fraction(p - 1, p) for p in primes) * area


def verify(limit=2000):
    mu = [trial_moebius(n) for n in range(limit + 1)]
    mertens = list(accumulate(mu))
    rows = []
    cases = 0
    for primes, expected in [((2,), Fraction(1, 4)),
                             ((2, 3), Fraction(2, 9)),
                             ((2, 3, 5), Fraction(16, 75)),
                             ((2, 3, 5, 7), Fraction(256, 1225))]:
        q = prod(primes)
        divisors = divisors_with_sign(primes)
        free_sum = list(accumulate(mu[n] if gcd(n, q) == 1 else 0
                                   for n in range(limit + 1)))
        coefficient = envelope_coefficient(primes)
        assert coefficient == expected
        assert coefficient >= Fraction(1, 2 * (len(primes) + 1))
        # Check convolution against independently factored Mobius values.
        for n in range(1, limit + 1):
            value = sum(sign * mu[n // d] for d, sign in divisors
                        if n % d == 0 and gcd(n // d, q) == 1)
            assert value == mu[n], ('coefficient', q, n)
        # Direct weighted sums also check the interval boundaries independently.
        for n in range(limit + 1):
            convolution = sum(sign * free_sum[n // d] for d, sign in divisors)
            weighted, envelope = 0, 0
            for m in range(1, n + 1):
                if gcd(m, q) != 1:
                    continue
                weight = sum(sign for d, sign in divisors if d * m <= n)
                weighted += mu[m] * weight
                envelope += abs(weight)
            assert mertens[n] == convolution == weighted, (q, n)
            assert abs(mertens[n]) <= envelope
            if q == 6:
                band = sum(mu[m] * (int(2 * m > n) - int(n < 6 * m and 3 * m <= n))
                           for m in range(1, n + 1) if gcd(m, 6) == 1)
                assert band == mertens[n], ('two bands', n)
            cases += 1
        rows.append({'Q': q, 'linear_coefficient': str(coefficient)})
    return {'result': 'PASS', 'limit': limit, 'interval_cases': cases,
            'coefficients': rows, 'lean_status': 'LEAN-PENDING',
            'scope': 'Exact finite checks; no uniform growing-Q estimate or RH proof.'}


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
