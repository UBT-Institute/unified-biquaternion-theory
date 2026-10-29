#!/usr/bin/env python3
"""Independent finite Hall-deficit checks and arithmetic reservation experiments."""
import json
from math import gcd
from verify_prime_exchange_matching import arithmetic, certify


def maximum_size(rows):
    def search(i, used):
        if i == len(rows):
            return 0
        return max([search(i + 1, used)] +
                   [1 + search(i + 1, used | {v}) for v in rows[i] if v not in used])
    return search(0, set())


def verify_graphs():
    graphs = 0
    budget_checks = 0
    for n in range(4):
        for m in range(4):
            for mask in range(1 << (n * m)):
                rows = [{j for j in range(m) if mask & (1 << (i * m + j))}
                        for i in range(n)]
                deficit = max(len(a) - len(set().union(*(rows[i] for i in a)))
                              for bits in range(1 << n)
                              for a in [{i for i in range(n) if bits & (1 << i)}])
                matched = maximum_size(rows)
                assert deficit == n - matched
                for d in range(n + 1):
                    padded = [row | set(range(m, m + d)) for row in rows]
                    assert (maximum_size(padded) == n) == (deficit <= d)
                    budget_checks += 1
                graphs += 1
    return dict(graphs=graphs, budget_checks=budget_checks,
                domain='All bipartite graphs with each side of size at most 3')


def reservation_case(n, data):
    mu, omega, spf = data
    large = [p for p in range(max(2, n // 2 + 1), n + 1) if spf[p] == p]
    candidates = sorted({2*q for q in range(3, n//2+1) if spf[q] == q} |
                        {3*q for q in range(5, n//3+1) if spf[q] == q})
    assert len(candidates) >= len(large)
    reserved = list(zip(large, candidates))
    used = {q for _, q in reserved}
    assert len(used) == len(reserved)
    for p, q in reserved:
        g = gcd(p, q)
        assert mu[p] == -1 and mu[q] == 1
        assert (omega[p//g], omega[q//g]) == (1, 2)
    left = [x for x in range(1, n+1) if mu[x] == 1 and x not in used]
    right = [x for x in range(1, n+1) if mu[x] == -1 and x not in large]
    rows = [[j for j, y in enumerate(right)
             if (omega[x//gcd(x, y)], omega[y//gcd(x, y)]) in
             [(0, 1), (1, 0), (1, 2), (2, 1)]] for x in left]
    cert = certify(rows, left, right)
    mertens = sum(mu[1:n+1])
    # This equality certifies global optimality after adjoining the reserved pairs.
    assert cert['unmatched'] == abs(mertens)
    return dict(N=n, reserved_pairs=len(reserved), candidates=len(candidates),
                M=mertens, remaining_certificate=cert)


def verify():
    data = arithmetic(1000)
    sweep = [reservation_case(n, data) for n in range(14, 601)]
    return dict(result='PASS', finite_graphs=verify_graphs(),
                reservation_sweep=dict(first=14, last=600, cases=len(sweep),
                                       excess_cases=[]),
                samples=[reservation_case(n, data) for n in [100, 1000]],
                limitations=['No all-cutoff reservation theorem.',
                             'No arithmetic Hall deficit bound for all subsets.',
                             'Python cases are independent finite checks, not Lean proofs of those cases.'])


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
