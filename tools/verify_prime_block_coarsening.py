#!/usr/bin/env python3
"""Independent exact checks; finite evidence is not an asymptotic RH bound."""
from collections import defaultdict
from itertools import combinations
from math import gcd, prod
import json


def arithmetic(n):
    if n == 0:
        return 0, frozenset()
    primes = set()
    squarefree = True
    d = 2
    while d * d <= n:
        exponent = 0
        while n % d == 0:
            n //= d
            exponent += 1
        if exponent:
            primes.add(d)
            squarefree &= exponent == 1
        d += 1
    if n > 1:
        primes.add(n)
    return ((-1) ** len(primes) if squarefree else 0), frozenset(primes)


def block_mass(data, selected):
    blocks = defaultdict(int)
    for value, factors in data:
        blocks[factors - selected] += value
    return sum(abs(v) for v in blocks.values()), sum(blocks.values())


def cutoff_formula(data, selected):
    n = len(data) - 1
    divisors = [(prod(s), (-1) ** len(s))
                for k in range(len(selected) + 1)
                for s in combinations(sorted(selected), k)]
    q = prod(selected)
    terms = [value * sum(sign for d, sign in divisors if a * d <= n)
             for a, (value, _) in enumerate(data) if a and gcd(a, q) == 1]
    return sum(abs(t) for t in terms), sum(terms)


def verify():
    table = [arithmetic(n) for n in range(1001)]
    cases = 0
    for n in range(201):
        selected = set()
        previous = None
        data = table[:n + 1]
        for p in [None, 2, 3, 5, 7, 11]:
            if p is not None:
                selected.add(p)
            mass, total = block_mass(data, selected)
            assert (mass, total) == cutoff_formula(data, selected)
            assert total == sum(value for value, _ in data)
            assert abs(total) <= mass
            assert previous is None or mass <= previous
            previous = mass
            cases += 1
        all_factors = set().union(*(factors for _, factors in data))
        assert block_mass(data, all_factors)[0] == abs(total)
    rows = []
    selected = set()
    for p in [2, 3, 5, 7, 11, 13, 17, 19]:
        selected.add(p)
        mass, total = block_mass(table, selected)
        assert (mass, total) == cutoff_formula(table, selected)
        rows.append(dict(added_prime=p, remainder=mass, mertens=total))
    for a in range(-30, 31):
        for b in range(-30, 31):
            gain = abs(a) + abs(b) - abs(a - b)
            assert gain >= 0
            if a * b >= 0:
                assert gain == 2 * min(abs(a), abs(b))
    return dict(result='PASS', grouped_formula_cases=cases,
                cutoff_range=[0, 200], terminal_cases=201,
                local_gain_cases=61 ** 2, cutoff_1000=rows,
                limitations=['Finite independent checks only; no RH bound.',
                             'Product-cutoff identification checked numerically; Lean uses direct arithmetic blocks.'])


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
