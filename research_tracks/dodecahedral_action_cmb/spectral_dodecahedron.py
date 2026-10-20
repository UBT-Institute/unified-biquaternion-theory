#!/usr/bin/env python3
"""Exact Poincare-sphere scalar spectrum and NON-CMB heat-trace diagnostics.

Research only. No Planck data, Boltzmann transfer or physical CMB C_ell.
Uses only Python standard library. See DERIVATION.md.
"""
from __future__ import annotations

import argparse
import math


def _partition_count(n: int) -> int:
    """Number of triples of nonnegative integers with 12a+20b+30c=n."""
    if n < 0:
        return 0
    return sum(
        1
        for a in range(n // 12 + 1)
        for b in range((n - 12 * a) // 20 + 1)
        if (n - 12 * a - 20 * b) % 30 == 0
    )


def invariant_dimension(n: int) -> int:
    """[t^n] (1-t^60)/((1-t^12)(1-t^20)(1-t^30))."""
    if n < 0:
        return 0
    return _partition_count(n) - _partition_count(n - 60)


def character_dimension(n: int) -> int:
    """Independent character-averaging verification for binary icosahedral group.

    Group of 120 elements: central +/-1 (one each), 30 of angle pi/2,
    20 each of angles pi/3, 2pi/3, and 12 each of the four angles j*pi/5.
    """
    if n < 0:
        return 0

    def chi(theta: float) -> float:
        return math.sin((n + 1) * theta) / math.sin(theta)

    dimension = (
        (n + 1) * (1 + (-1) ** n)
        + 30 * chi(math.pi / 2)
        + 20 * (chi(math.pi / 3) + chi(2 * math.pi / 3))
        + 12 * sum(chi(j * math.pi / 5) for j in range(1, 5))
    ) / 120
    result = round(dimension)
    if abs(dimension - result) > 1e-8:
        raise ArithmeticError(f"Character/Molien precision failure at n={n}")
    return result


def scalar_multiplicity(n: int, quotient: bool = True) -> int:
    """Scalar Laplacian eigenvalue multiplicity at lambda_n=n(n+2)."""
    if n < 0:
        return 0
    return (n + 1) * invariant_dimension(n) if quotient else (n + 1) ** 2


def eigenvalue(n: int) -> int:
    if n < 0:
        raise ValueError("n must be nonnegative")
    return n * (n + 2)


def heat_trace(s: float, cutoff: int, quotient: bool = True) -> float:
    if s <= 0 or cutoff < 0:
        raise ValueError("Require s>0 and cutoff>=0")
    return math.fsum(
        scalar_multiplicity(n, quotient) * math.exp(-s * eigenvalue(n))
        for n in range(cutoff + 1)
    )


def nonconstant_spectral_proxy(s: float, cutoff: int = 250) -> float:
    """Compare nonconstant spectral traces at the same curvature radius and
    per-unit-volume normalization. This is NOT the CMB C_ell or likelihood.
    """
    numerator = heat_trace(s, cutoff, True) - 1.0
    denominator = (heat_trace(s, cutoff, False) - 1.0) / 120
    if denominator <= 0:
        raise ValueError("Spectral proxy denominator underflow; reduce s")
    return numerator / denominator


def hamiltonian(mode_u: float, mode_p: float, a: float, rc: float,
                mass: float, n: int) -> float:
    """Test-field Hamiltonian for one real normalized scalar eigenmode."""
    if a <= 0 or rc <= 0 or mass < 0:
        raise ValueError("Require a>0, rc>0, mass>=0")
    omega_sq = eigenvalue(n) / (a * rc) ** 2 + mass * mass
    return 0.5 * (mode_p * mode_p / a ** 3 + a ** 3 * omega_sq * mode_u * mode_u)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-degree", type=int, default=60)
    parser.add_argument("--heat-s", type=float, default=0.05)
    parser.add_argument("--cutoff", type=int, default=250)
    args = parser.parse_args()
    if args.max_degree < 0:
        parser.error("--max-degree must be nonnegative")

    print("n  lambda_n  multiplicity")
    for n in range(args.max_degree + 1):
        dim = invariant_dimension(n)
        if dim != character_dimension(n):
            raise ArithmeticError(f"Independent invariant calculation disagrees at {n}")
        if dim:
            print(f"{n:2d} {eigenvalue(n):8d} {scalar_multiplicity(n):12d}")
    print("Nonconstant heat-trace proxy (not CMB C_ell):",
          f"{nonconstant_spectral_proxy(args.heat_s, args.cutoff):.8g}")


if __name__ == "__main__":
    main()
