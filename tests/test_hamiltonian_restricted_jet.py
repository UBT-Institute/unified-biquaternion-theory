#!/usr/bin/env python3
"""Independent exact and numerical checks for a restricted determinant-jet model.

These tests verify a *chosen* first-jet model, not the complete UBT action.
The common-covector determinant is affine in s,t even with a constant
additive matrix shift.  We check polynomial coefficients exactly and
compare the identity at reproducible random integer samples.
"""
from __future__ import annotations

import random
import sympy as sp


def test_restricted_determinant_jet_symbolic():
    s, t = sp.symbols("s t")
    e = sp.Matrix(4, 4, lambda i, j: 2 if i == j else (i + j) % 3)
    shift = sp.Matrix(4, 4, lambda i, j: (i - j) % 2)
    k = sp.Matrix([1, 2, -1, 3])
    u = sp.Matrix([2, 0, 1, -2])
    v = sp.Matrix([-1, 1, 3, 0])
    density = sp.expand((e + shift + s * k * u.T + t * k * v.T).det())
    assert sp.diff(density, s, t) == 0
    assert sp.diff(density, s, 2) == 0
    assert sp.diff(density, t, 2) == 0


def test_restricted_determinant_jet_numeric_exact():
    rng = random.Random(20261027)
    for _ in range(25):
        e = sp.Matrix(4, 4, lambda _i, _j: rng.randint(-3, 3))
        k = sp.Matrix([rng.randint(-3, 3) for _ in range(4)])
        u = sp.Matrix([rng.randint(-3, 3) for _ in range(4)])
        v = sp.Matrix([rng.randint(-3, 3) for _ in range(4)])
        s, t = rng.randint(-3, 3), rng.randint(-3, 3)
        base = e.det()
        lhs = (e + s * k * u.T + t * k * v.T).det()
        rhs = (base + s * ((e + k * u.T).det() - base)
               + t * ((e + k * v.T).det() - base))
        assert lhs == rhs
