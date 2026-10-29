# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
"""Exact boundary layers; selected prime families are not full Mertens sums."""
from math import comb, isqrt
import json


def verify():
    cases = 0
    for n in range(40):
        for r in range(45):
            lhs = sum((-1)**j * comb(n+1,j) for j in range(r+1) if j <= n+1)
            rhs = (-1)**r * (comb(n,r) if r <= n else 0)
            assert lhs == rhs
            cases += 1
    primes = [n for n in range(1009,1200)
              if all(n % d for d in range(2,isqrt(n)+1))][:20]
    r, k = 10, len(primes)
    cutoff = primes[-1]**r
    assert cutoff < primes[0]**(r+1)
    even = odd = visited = 0
    # Direct product enumeration, independently of the binomial formulas.
    def visit(i, product, size):
        nonlocal even, odd, visited
        if i == k:
            visited += 1
            admitted = product <= cutoff
            assert admitted == (size <= r)
            if admitted:
                if size % 2:
                    odd += 1
                else:
                    even += 1
            return
        visit(i+1, product, size)
        visit(i+1, product*primes[i], size+1)
    visit(0,1,0)
    assert even+odd == sum(comb(k,j) for j in range(r+1)) == 616666
    assert even-odd == (-1)**r*comb(k-1,r) == 92378
    assert (even-odd)**2 > even+odd
    assert (even-odd)**2 < cutoff  # Not an RH counterexample even on this scale.
    return {'result':'PASS','pascal_cases':cases,'direct_subsets':visited,
            'primes':primes,'cutoff':cutoff,'even':even,'odd':odd,
            'admitted':even+odd,'signed':even-odd,
            'scope':'Selected-prime parity imbalance only; not M(cutoff), no RH counterexample or asymptotic prime estimate.'}


if __name__ == '__main__':
    print(json.dumps(verify(),indent=2))
