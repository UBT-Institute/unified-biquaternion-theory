#!/usr/bin/env python3
"""Exact nearest matched-circle geometry for spherical Poincare dodecahedral space.

Pure standard library. This is a *conditional geometry test*, not detection of
matched circles and not a first-principles UBT topology selection.
Valid only for 0 < comoving LSS radius chi < pi/2 (unit round S^3).
"""
from __future__ import annotations

from math import acos, cos, pi, sin, sqrt, tan
from typing import Optional

from cmb_sachs_wolfe_kernel import (
    GROUP, dot, left_multiply, point_on_last_scattering_sphere,
)

Quaternion = tuple[float, float, float, float]
Vector3 = tuple[float, float, float]


def quaternion_conjugate(q: Quaternion) -> Quaternion:
    return (q[0], -q[1], -q[2], -q[3])


def deck_distance(g: Quaternion) -> float:
    """Clifford translation distance of the unit quaternion g on S^3."""
    return acos(max(-1.0, min(1.0, g[0])))


def nearest_deck_elements() -> tuple[Quaternion, ...]:
    """Exactly 12 minimum-displacement NONIDENTITY deck transformations."""
    nontrivial = [g for g in GROUP if deck_distance(g) > 1e-8]
    distance = min(deck_distance(g) for g in nontrivial)
    result = tuple(g for g in nontrivial if abs(deck_distance(g)-distance) < 1e-9)
    if len(result) != 12 or abs(distance-pi/5) > 1e-9:
        raise AssertionError("Unexpected 2I nearest-deck-element multiplicity")
    return result


def six_inverse_pairs() -> tuple[tuple[Quaternion, Quaternion], ...]:
    """The twelve shortest deck transformations give six inverse pairs."""
    nearest = nearest_deck_elements()
    seen: set[tuple[float, ...]] = set()
    pairs: list[tuple[Quaternion, Quaternion]] = []

    def key(x: Quaternion) -> tuple[float, ...]:
        return tuple(round(v, 12) for v in x)

    for g in nearest:
        if key(g) in seen:
            continue
        inv = quaternion_conjugate(g)
        if key(inv) not in {key(v) for v in nearest}:
            raise AssertionError("Nearest deck inverse not found")
        seen.add(key(g))
        seen.add(key(inv))
        pairs.append((g, inv))
    assert len(pairs) == 6
    return tuple(pairs)


def injectivity_radius() -> float:
    """Global injectivity radius of the round S^3/2I quotient."""
    return min(deck_distance(g) for g in GROUP if deck_distance(g) > 1e-8)/2


def matched_circle_radius(chi: float, displacement: float = pi/5) -> Optional[float]:
    """Return angular radius alpha, or None for no corresponding sphere overlap.

    cos(alpha)=tan(displacement/2)/tan(chi). All angles in radians.
    In this file chi is restricted to (0,pi/2).
    """
    if not (0.0 < chi < pi/2):
        raise ValueError("Require 0 < chi < pi/2 for this simple branch")
    if not (0.0 < displacement < pi):
        raise ValueError("Require 0 < displacement < pi")
    if chi <= displacement/2:
        return None
    ratio = tan(displacement/2) / tan(chi)
    if ratio >= 1.0:
        return None
    return acos(max(-1.0, min(1.0, ratio)))


def _cross(a: Vector3, b: Vector3) -> Vector3:
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def _unit(x: Vector3) -> Vector3:
    length = sqrt(dot(x, x))
    if length <= 1e-12:
        raise ValueError("Zero vector")
    return tuple(v / length for v in x)  # type: ignore[return-value]


def _tangent_basis(u: Vector3) -> tuple[Vector3, Vector3]:
    axes: tuple[Vector3, ...] = ((1.,0.,0.), (0.,1.,0.), (0.,0.,1.))
    ref = min(axes, key=lambda a: abs(dot(a,u)))
    e1 = _unit(tuple(ref[i]-dot(ref,u)*u[i] for i in range(3)))
    e2 = _cross(u, e1)
    return e1,e2


def matched_sky_directions(
    g: Quaternion, chi: float, phase: float
) -> tuple[Vector3, Vector3]:
    """Corresponding sky directions (n, n') of one identified 3D point.

    x=(cos chi, sin chi*n) is on our LSS, at the same radius chi from g.
    x'=g^-1*x is the identified representation on our own LSS.
    The centers are antipodal; the tangent-circle phase is shifted by -d,
    where d is the Clifford translation angle of g.
    """
    d=deck_distance(g)
    alpha=matched_circle_radius(chi,d)
    if alpha is None:
        raise ValueError("No matched circles for this chi and deck element")
    norm=sqrt(sum(v*v for v in g[1:]))
    if norm < 1e-12:
        raise ValueError("Central deck element has no circle axis")
    u=_unit(tuple(v/norm for v in g[1:]))
    e1,e2=_tangent_basis(u)
    axis=cos(alpha)
    side=sin(alpha)
    n=_unit(tuple(axis*u[i]+side*(cos(phase)*e1[i]+sin(phase)*e2[i])
                  for i in range(3)))
    x=point_on_last_scattering_sphere(n,chi)
    xp=left_multiply(quaternion_conjugate(g),x)
    if abs(xp[0]-cos(chi)) > 1e-9:
        raise ArithmeticError("Image point is not on observer's LSS")
    np=_unit(tuple(v/sin(chi) for v in xp[1:]))
    return n,np


if __name__=="__main__":
    from math import degrees
    print("Nontrivial deck translations at minimum distance:",len(nearest_deck_elements()))
    print("Inverse pairs:",len(six_inverse_pairs()))
    print("Injectivity radius:",injectivity_radius(),"radians")
    for chi in (0.30,0.35,0.40,0.50,0.60):
        alpha=matched_circle_radius(chi)
        print(f"chi={chi:.2f}, alpha={degrees(alpha):.4f} deg" if alpha else
              f"chi={chi:.2f}, no shortest matched circles")
