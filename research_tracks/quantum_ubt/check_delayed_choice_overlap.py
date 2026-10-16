#!/usr/bin/env python3
"""Deterministic checks of a conditional two-path Hilbert-space overlap identity.

No UBT action, physical photon mapping, or nonstandard quantum effect is tested.
"""
import cmath
import math
import random


def overlap(a, b):
    return sum(x.conjugate() * y for x, y in zip(a, b))


def normalize(xs):
    norm = math.sqrt(sum(abs(x) ** 2 for x in xs))
    return [x / norm for x in xs]


def probability_by_paths(a, b, phi):
    phase = cmath.exp(1j * phi)
    p0 = sum(abs((x + phase * y) / 2) ** 2 for x, y in zip(a, b))
    p1 = sum(abs((x - phase * y) / 2) ** 2 for x, y in zip(a, b))
    return p0, p1


def main():
    rng = random.Random(20261016)
    for _ in range(500):
        a = normalize([complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(6)])
        b = normalize([complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(6)])
        phi = rng.uniform(-math.pi, math.pi)
        gamma = overlap(a, b)
        direct0, direct1 = probability_by_paths(a, b, phi)
        predicted0 = (1 + (cmath.exp(1j * phi) * gamma).real) / 2
        assert abs(direct0 - predicted0) < 1e-12
        assert abs(direct0 + direct1 - 1.0) < 1e-12
        assert -1e-12 <= direct0 <= 1 + 1e-12
        assert abs(gamma) <= 1 + 1e-12

    a = [math.sqrt(0.5), math.sqrt(0.5)]
    for k in range(401):
        theta = 2 * math.pi * k / 400
        b = [a[0], a[1] * cmath.exp(1j * theta)]
        gamma = overlap(a, b)
        assert abs(abs(gamma) - abs(math.cos(theta / 2))) < 1e-12

    print("PASS: 500 normalized random overlaps and 401 two-mode phase values")
    print("SCOPE: standard complex Hilbert-space identity only; no UBT dynamics or Born-rule derivation")


if __name__ == "__main__":
    main()
