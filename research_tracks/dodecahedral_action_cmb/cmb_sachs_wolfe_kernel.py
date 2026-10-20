#!/usr/bin/env python3
"""Exact S^3/(binary icosahedral) scalar projector kernel; SW-only CMB toy.

No Planck data or cosmological transfer functions. Modal weights are arbitrary
user-supplied P_n: never interpret output as a confirmed UBT CMB prediction.
"""
from __future__ import annotations

from itertools import permutations, product
from math import cos, pi, sin, sqrt, fsum
from typing import Sequence


OBSERVATIONAL_FIT_STATUS = "NO OBSERVATIONAL FIT"
EXACT_PROJECTION_STATUS = "BLOCKED: exact xi_{nj,lm} projection is not implemented"

Quaternion = tuple[float, float, float, float]


def observational_fit_status() -> dict[str, str]:
    """Return the explicit gate status for this research track.

    This is a synthetic, SW-only toy model. It is not a Planck likelihood or
    cosmological fit and does not claim observational support.
    """
    return {
        "scalar_spectrum": "exact (2I quotient spectrum confirmed independently)",
        "full_sky_projection": EXACT_PROJECTION_STATUS,
        "planck_fit": OBSERVATIONAL_FIT_STATUS,
        "proof_gate": "BLOCKED: the missing theta-to-zeta and transfer-function bridge is not derived here",
    }


def require_exact_projection_gate() -> None:
    """Fail fast when the exact spherical-harmonic projection is required.

    The quotient spectrum is implemented exactly, but the full-sky 
    xi_{nj,lm}(x_o, O, chi_*) projection is not available in this research track.
    This avoids silently substituting the heat-trace or SW kernel proxy.
    """
    raise NotImplementedError(
        "Exact xi_{nj,lm} projection and a real Planck likelihood are blocked for "
        "this research track. Synthetic SW covariance is not a real CMB fit; "
        "use the low-l toy kernel only for null/diagnostic checks."
    )


def _even_perm(index_tuple: Sequence[int]) -> bool:
    return sum(index_tuple[i] > index_tuple[j] for i in range(4)
               for j in range(i + 1, 4)) % 2 == 0


def binary_icosahedral_vertices() -> tuple[Quaternion, ...]:
    """The 120 unit quaternions (vertices of the 600-cell)."""
    golden = (1 + sqrt(5)) / 2
    points: list[Quaternion] = []
    for k in range(4):
        for sign in (-1, 1):
            coords = [0.0] * 4
            coords[k] = float(sign)
            points.append(tuple(coords))
    for signs in product((-1, 1), repeat=4):
        points.append(tuple(sign * 0.5 for sign in signs))
    base = (0.0, 0.5, golden / 2, 1 / (2 * golden))
    for perm in permutations(range(4)):
        if not _even_perm(perm):
            continue
        vals = [base[i] for i in perm]
        nz = [i for i, val in enumerate(vals) if val != 0]
        for signs in product((-1, 1), repeat=3):
            coords = vals.copy()
            for k, sign in zip(nz, signs):
                coords[k] *= sign
            points.append(tuple(coords))
    assert len(points) == 120
    assert len({tuple(round(x, 12) for x in q) for q in points}) == 120
    return tuple(points)


GROUP = binary_icosahedral_vertices()


def left_multiply(g: Quaternion, x: Quaternion) -> Quaternion:
    """Hamilton quaternion product g*x; acts on S^3 by left translation."""
    a, b, c, d = g
    e, f, h, i = x
    return (
        a*e - b*f - c*h - d*i,
        a*f + b*e + c*i - d*h,
        a*h - b*i + c*e + d*f,
        a*i + b*h - c*f + d*e,
    )


def dot(x: Sequence[float], y: Sequence[float]) -> float:
    return sum(a * b for a, b in zip(x, y))


def chebyshev_u(n: int, t: float) -> float:
    """Chebyshev U_n: Gegenbauer C_n^1(t), stable on [-1,1] at low n."""
    if n < 0:
        raise ValueError("degree must be nonnegative")
    if not -1.0 - 1e-10 <= t <= 1.0 + 1e-10:
        raise ValueError("S^3 dot product outside [-1,1]")
    t = max(-1.0, min(1.0, t))
    if n == 0:
        return 1.0
    x, y = 1.0, 2*t
    for _ in range(2, n + 1):
        x, y = y, 2*t*y - x
    return y


def quotient_mode_kernel(n: int, x: Quaternion, y: Quaternion) -> float:
    """Sum_j Y^Q_nj(x)Y^Q_nj(y) with Y^Q orthonormal on quotient.

    K_n^Q(x,y) = (n+1)/(2*pi^2) * sum_{g in 2I} U_n(<g*x,y>).
    This is real, symmetric, positive semidefinite as a kernel.
    x,y are unit quaternions and n a NONNEGATIVE integer.
    """
    for v in (x, y):
        if abs(dot(v, v) - 1.0) > 1e-8:
            raise ValueError("x,y must lie on unit S^3")
    return (n + 1)/(2*pi*pi) * fsum(
        chebyshev_u(n, dot(left_multiply(g, x), y)) for g in GROUP
    )


def point_on_last_scattering_sphere(direction: Sequence[float],
                                    chi: float) -> Quaternion:
    """Observer at identity of S^3, angular comoving radius chi in [0,pi]."""
    if len(direction) != 3 or not (0 <= chi <= pi):
        raise ValueError("Expected 3-direction and 0 <= chi <= pi")
    norm = sqrt(dot(direction, direction))
    if norm <= 0:
        raise ValueError("Nonzero sky direction required")
    return (cos(chi), *(sin(chi)*v/norm for v in direction))


def sw_sky_covariance(direction_a: Sequence[float], direction_b: Sequence[float],
                      chi: float, modal_weights: dict[int, float]) -> float:
    """Conditional ordinary-Sachs-Wolfe-only covariance in a toy model.

    E[deltaT/T(a) deltaT/T(b)] = 1/25 * sum_n P_n K_n^Q(x_a,x_b).
    P_n are specified scalar-mode variances and MUST be nonnegative.
    n=0 omitted: homogeneous monopole is not a CMB anisotropy.

    This is an explicit null/diagnostic model. It is not a real CMB fit and does
    not implement the exact full-sky projected covariance matrix. See the gate in
    observational_fit_status() and require_exact_projection_gate().
    """
    x = point_on_last_scattering_sphere(direction_a, chi)
    y = point_on_last_scattering_sphere(direction_b, chi)
    if any(n <= 0 or weight < 0 for n, weight in modal_weights.items()):
        raise ValueError("Use positive n and nonnegative P_n (no CMB monopole)")
    return fsum(weight*quotient_mode_kernel(n,x,y)/25
                for n,weight in modal_weights.items())
