# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
"""Exact finite matching experiments; no RH or all-cutoff saturation claim."""
from collections import deque
from math import gcd
import hashlib
import json
from verify_prime_pairing import trial_moebius


def arithmetic(limit):
    spf = list(range(limit + 1))
    for p in range(2, limit + 1):
        if spf[p] == p:
            for n in range(p*p, limit+1, p):
                if spf[n] == n:
                    spf[n] = p
    omega = [0]*(limit+1)
    mu = [0]+[trial_moebius(n) for n in range(1, limit+1)]
    for n in range(2,limit+1):
        omega[n] = omega[n//spf[n]]+1
    return mu, omega, spf


def certify(adjacency, left, right, include_certificate=False):
    """Return a matching and equal-size vertex cover, checked edge by edge."""
    ml, mr = [-1]*len(left), [-1]*len(right)
    greedy = 0
    for u, row in enumerate(adjacency):
        for v in row:
            if mr[v] < 0:
                ml[u], mr[v] = v, u
                greedy += 1
                break
    rounds = 0
    while True:
        distance = [-1]*len(left)
        queue = deque()
        for u in range(len(left)):
            if ml[u] < 0:
                distance[u] = 0
                queue.append(u)
        while queue:
            u = queue.popleft()
            for v in adjacency[u]:
                w = mr[v]
                if w >= 0 and distance[w] < 0:
                    distance[w] = distance[u]+1
                    queue.append(w)
        def augment(u):
            for v in adjacency[u]:
                w = mr[v]
                if w < 0 or (distance[w] == distance[u]+1 and augment(w)):
                    ml[u], mr[v] = v, u
                    return True
            distance[u] = -1
            return False
        added = sum(augment(u) for u in range(len(left)) if ml[u] < 0)
        if not added:
            break
        rounds += 1
    pairs = [(u,v) for u,v in enumerate(ml) if v >= 0]
    assert len({v for _,v in pairs}) == len(pairs)
    for u,v in pairs:
        assert mr[v] == u and v in adjacency[u]
    # Alternating reachability constructs a candidate vertex cover.
    zl = {u for u in range(len(left)) if ml[u] < 0}
    zr = set()
    queue = deque(zl)
    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if ml[u] == v or v in zr:
                continue
            zr.add(v)
            w = mr[v]
            assert w >= 0, 'augmenting path remains'
            if w not in zl:
                zl.add(w)
                queue.append(w)
    cl = set(range(len(left))) - zl
    cr = zr
    assert all(u in cl or v in cr for u,row in enumerate(adjacency) for v in row)
    assert len(cl)+len(cr) == len(pairs)
    certificate = {'pairs':[(left[u],right[v]) for u,v in pairs],
                   'cover_positive':sorted(left[u] for u in cl),
                   'cover_negative':sorted(right[v] for v in cr)}
    digest = hashlib.sha256(json.dumps(certificate,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    result = {'edges':sum(map(len,adjacency)), 'matching_size':len(pairs),
            'cover_size':len(cl)+len(cr), 'unmatched':len(left)+len(right)-2*len(pairs),
            'greedy_unmatched':len(left)+len(right)-2*greedy,
            'augmenting_rounds':rounds, 'certificate_sha256':digest,
            'certificate_result':'PASS'}
    if include_certificate:
        result['certificate'] = certificate
    return result


def experiment(n, data, include_certificates=False):
    mu, omega, spf = data
    left = [m for m in range(1,n+1) if mu[m] == 1]
    right = [m for m in range(1,n+1) if mu[m] == -1]
    single = [[] for _ in left]
    combined = [[] for _ in left]
    for u,x in enumerate(left):
        for v,y in enumerate(right):
            g = gcd(x,y)
            a,b = omega[x//g],omega[y//g]
            edge = (a,b) in ((0,1),(1,0))
            exchange = (a,b) in ((1,2),(2,1))
            if n <= 100:
                def support(m):
                    result = set()
                    while m > 1:
                        result.add(spf[m]);m //= spf[m]
                    return result
                sx,sy = support(x),support(y)
                assert (a,b) == (len(sx-sy),len(sy-sx))
            if edge:
                single[u].append(v)
            if edge or exchange:
                combined[u].append(v)
    m = sum(mu[1:n+1])
    result = {'N':n,'M':m,'positive':len(left),'negative':len(right),
              'toggle':certify(single,left,right,include_certificates),
              'exchange':certify(combined,left,right,include_certificates)}
    for mode in ('toggle','exchange'):
        result[mode]['excess_over_absolute_M'] = result[mode]['unmatched']-abs(m)
        assert result[mode]['excess_over_absolute_M'] >= 0
    # Each prime in (N/2,N] only connects to 1 in the single-toggle graph.
    leaves = sum(spf[p] == p for p in range(max(2,n//2+1),n+1))
    assert result['toggle']['unmatched'] >= max(0,leaves-1)
    return result


def verify(limit=10000):
    assert limit >= 200
    data = arithmetic(limit)
    sweep = [experiment(n,data) for n in range(1,201)]
    samples = [experiment(n,data) for n in (30,100,300,1000,3000,10000) if n <= limit]
    excess = [r['N'] for r in sweep if r['exchange']['excess_over_absolute_M']]
    return {'result':'PASS','sweep_max':200,'sweep_excess_cutoffs':excess,
            'samples':samples,'lean_status':'EXPERIMENT_NOT_LEAN_FORMALIZED',
            'scope':'Exact finite maximum-matching certificates. No general saturation theorem, asymptotic unmatched bound, or RH proof.'}


if __name__ == '__main__':
    print(json.dumps(verify(),indent=2))
