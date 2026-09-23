#!/usr/bin/env python3
"""Independent finite checks of the global obstruction; no RH estimate."""
from itertools import combinations
import json
from verify_prime_pairing import trial_moebius


def complete_condition(source, target, budget):
    for k in range(len(source) + 1):
        for subset in combinations(source, k):
            neighbors = set().union(*(target for _ in subset))
            if len(subset) > len(neighbors) + budget:
                return False
    return True


def verify():
    cases = 0
    for positive in range(7):
        for negative in range(7):
            for d in range(7):
                p, n = set(range(positive)), set(range(negative))
                both = complete_condition(p, n, d) and complete_condition(n, p, d)
                assert both == (abs(positive - negative) <= d)
                cases += 1
    m = p = n = 0
    for cutoff in range(1001):
        value = 0 if cutoff == 0 else trial_moebius(cutoff)
        m += value
        p += value == 1
        n += value == -1
        assert m == p - n
        for d in [0, abs(m), max(0, abs(m) - 1), abs(m) + 1]:
            assert ((p <= n + d) and (n <= p + d)) == (abs(m) <= d)
    return dict(result='PASS', exhaustive_complete_graph_cases=cases,
                actual_mobius_count_cutoffs=1001,
                limitations=['Finite independent checks; no uniform bound on M(N).',
                             'The full RH analytic bridge is not formalized by this audit.'])


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
