#!/usr/bin/env python3
"""Independent exact checks of the existing quartic potential's nonzero minimum.

This verifies the pointwise potential, not the full Theta action or its kinetic
operator. All eight real coordinates of the biquaternion are varied.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def verify() -> dict:
    x = sp.symbols("x0:8", real=True)
    v = sp.Matrix(sp.symbols("v0:8", real=True))
    r, l2 = sp.symbols("r l2", positive=True)
    l1 = sp.symbols("l1", nonnegative=True)
    v0, h, n = sp.symbols("V0 H n", real=True)
    mass = -(4*l1+l2)*r**2
    minimum = v0-(4*l1+l2)*r**4
    gap = v0+mass*h+l1*h**2+l2*n**2-minimum
    certificate = l1*(h-2*r**2)**2+l2*(n-r**2)**2+l2*r**2*(2*n-h)
    assert sp.expand(gap-certificate) == 0

    H = 2*(x[0]*x[2]+x[1]*x[3])-sum(x[j]**2 for j in (4, 5, 6, 7))
    dr = x[0]*x[2]-x[1]*x[3]-x[4]*x[6]+x[5]*x[7]
    di = x[0]*x[3]+x[1]*x[2]-x[4]*x[7]-x[5]*x[6]
    X = sp.Matrix([[x[0]+sp.I*x[1], x[4]+sp.I*x[5]],
                   [x[6]+sp.I*x[7], x[2]+sp.I*x[3]]])
    assert sp.expand(X.det()-dr-sp.I*di) == 0
    assert sp.expand(sp.trace(X.adjugate()*X.conjugate().T)-H) == 0
    potential = v0+mass*H+l1*H**2+l2*(dr**2+di**2)
    point = dict(zip(x, (0, r, 0, r, 0, 0, 0, 0)))
    assert sp.expand(potential.subs(point)-minimum) == 0
    assert all(sp.expand(sp.diff(potential, z).subs(point)) == 0 for z in x)
    hessian = sp.simplify(sp.hessian(potential, x).subs(point))
    q = 2*r**2*((4*l1+l2)*(v[1]+v[3])**2+
               l2*((v[0]-v[2])**2+(v[4]+v[6])**2+(v[5]-v[7])**2))
    assert sp.expand((v.T*hessian*v)[0]-q) == 0
    assert hessian.eigenvals() == {0: 4, 4*l2*r**2: 3, 4*r**2*(4*l1+l2): 1}
    kernel_map = sp.Matrix([
        [-r, 0, 0, 0], [0, 0, 0, r], [-r, 0, 0, 0], [0, 0, 0, -r],
        [0, 0, r, 0], [0, r, 0, 0], [0, 0, -r, 0], [0, r, 0, 0],
    ])
    assert hessian*kernel_map == sp.zeros(8, 4)
    assert kernel_map.rank() == 4
    assert hessian.rank() == 4
    t = sp.symbols("t", real=True)
    ray = dict(zip(x, (t, 0, 0, 0, 0, 0, 0, 0)))
    assert sp.expand(potential.subs(ray)-v0) == 0
    assert sp.factor(v0-minimum) == r**4*(4*l1+l2)
    # Independent global-orbit algebra: the trace defect forces Hermiticity
    # after the unit-phase normalization proved in Lean.
    trace_defect = (x[1]-x[3])**2+(x[4]-x[6])**2+(x[5]+x[7])**2-(x[1]+x[3])**2
    assert sp.expand(2*dr-H-trace_defect) == 0
    assert sp.expand((x[0]+x[2])**2+(x[1]+x[3])**2-sum(z*z for z in x)-H) == 0
    a = sp.symbols("a", positive=True)
    br, bi, pr, pi = sp.symbols("br bi pr pi", real=True)
    b = br+sp.I*bi
    d = (r**2+br**2+bi**2)/a
    Y = sp.Matrix([[a, b], [sp.conjugate(b), d]])
    T = sp.Matrix([[sp.sqrt(a), 0], [sp.conjugate(b)/sp.sqrt(a), r/sp.sqrt(a)]])
    assert sp.simplify(T.det()-r) == 0
    assert sp.simplify(T*T.conjugate().T-Y) == sp.zeros(2)
    S = T/sp.sqrt(r)
    assert sp.simplify(S.det()-1) == 0
    assert sp.simplify(r*S*S.conjugate().T-Y) == sp.zeros(2)
    phase = pr+sp.I*pi
    orbit_X = phase*Y
    assert sp.simplify(sp.trace(orbit_X.adjugate()*orbit_X.conjugate().T)
                       -2*r**2*(pr**2+pi**2)) == 0
    assert sp.simplify(orbit_X.det()-phase**2*r**2) == 0
    return {
        "global_gap_identity": "PASS",
        "matrix_invariant_identity": "PASS",
        "nonzero_minimizer_and_gradient": "PASS",
        "full_eight_real_hessian": "PASS",
        "hessian_rank": 4,
        "positive_eigenvalues": {"4*l2*r^2": 3, "4*r^2*(4*l1+l2)": 1},
        "kernel_dimension": 4,
        "kernel_equations": ["v1+v3=0", "v0-v2=0", "v4+v6=0", "v5-v7=0"],
        "null_ray_energy_above_minimum": "(4*l1+l2)*r^4",
        "phase_normalization_defect_identity": "PASS",
        "triangular_factor_and_determinant_one_normalization": "PASS",
        "orbit_invariant_identities": "PASS",
        "assumptions": ["r>0", "l1>=0", "l2>0", "mu=-(4*l1+l2)*r^2"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    checks = verify()
    paths = [
        "tools/verify_biquaternionic_potential_vacuum.py",
        "formal/lean/UBT/Action/PotentialVacuum.lean",
        "formal/lean/UBT/Action/PotentialMinimumOrbit.lean",
        "research_tracks/action_selection/biquaternionic_potential_vacuum.en.md",
        "research_tracks/action_selection/biquaternionic_potential_vacuum.cs.md",
        "tests/test_biquaternionic_potential_vacuum.py",
    ]
    record = {
        "schema": "ubt-verification/v1",
        "date": datetime.now(timezone.utc).date().isoformat(),
        "result": "PASS", "checks": checks,
        "tools": {"python": platform.python_version(), "sympy": sp.__version__},
        "lean": {"status": "NOT_RUN_BY_THIS_SCRIPT",
                 "evidence_record": "reports/lean_volume_hessian_2026_09_09.json"},
        "source_sha256": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        "limitations": [
            "The sign region is an explicit input, not derived coefficient selection.",
            "The norm inequality and universal minimizer proof are checked in Lean; CAS verifies independent identities and Hessian entries.",
            "Potential curvature is not a kinetic operator or a normalized particle mass.",
            "Symmetry tangent directions are not automatically physical gauge modes.",
            "No nondegenerate spacetime background, full-action vacuum, positive Einstein term, Newton constant or RH is proved.",
        ],
        "canonical_claim_status_changes": [],
    }
    if args.output:
        args.output.write_text(json.dumps(record, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps(checks, indent=2))


if __name__ == "__main__":
    main()
