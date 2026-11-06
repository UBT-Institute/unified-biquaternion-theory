#!/usr/bin/env python3
"""Reproduce the scoped U(1) erratum; no claim of UBT action selection.

Exact generator constraints and independent numerical congruence checks use
different representations. A positive scalar kinetic term is a comparator,
not an assertion that the unresolved UBT physical Hessian is positive.
"""
from __future__ import annotations

import argparse
import json
import platform
from pathlib import Path

import numpy as np
import sympy as sp


def lorentz_generators() -> list[sp.Matrix]:
    out = []
    for i in range(1, 4):
        boost = sp.zeros(4)
        boost[0, i] = boost[i, 0] = 1
        out.append(boost)
    for i, j in ((1, 2), (1, 3), (2, 3)):
        rotation = sp.zeros(4)
        rotation[i, j], rotation[j, i] = 1, -1
        out.append(rotation)
    return out


def exact_checks() -> dict:
    alpha, v, e, q, h, a = sp.symbols("alpha v e q h a", real=True)
    phase = sp.exp(sp.I * alpha)
    left = sp.diff(phase * v, alpha).subs(alpha, 0)
    conjugate = sp.simplify(phase * v / phase - v)
    # Constant complex scalar v (NOT v/sqrt(2)); Proca L = m^2 A^2/2.
    kinetic = sp.expand((sp.I * e * q * a * v) * (-sp.I * e * q * a * v))
    mass2 = sp.diff(kinetic, a, 2)
    generators = lorentz_generators()
    # Column-vectorization: vec(TL-LT)=(L^T tensor I-I tensor L)vec(T).
    constraints = sp.Matrix.vstack(*[
        sp.kronecker_product(sp.diag(g, g).T, sp.eye(8))
        - sp.kronecker_product(sp.eye(8), sp.diag(g, g))
        for g in generators
    ])
    rank = constraints.rank()
    block_basis = []
    for r in range(2):
        for c in range(2):
            m = sp.zeros(2)
            m[r, c] = 1
            block_basis.append(sp.kronecker_product(m, sp.eye(4)))
    commutes = all(t * sp.diag(g, g) == sp.diag(g, g) * t
                   for t in block_basis for g in generators)
    u = sp.Matrix(sp.symbols("u0:4", real=True))
    w = sp.Matrix(sp.symbols("w0:4", real=True))
    eta = sp.diag(1, -1, -1, -1)
    quadratic = lambda x: (x.T * eta * x)[0]
    uprime = sp.cos(alpha) * u - sp.sin(alpha) * w
    wprime = sp.sin(alpha) * u + sp.cos(alpha) * w
    invariant = sp.trigsimp(2 * (quadratic(uprime) + quadratic(wprime)
                               - quadratic(u) - quadratic(w)))
    # A general compact representation has an invariant positive inner product.
    # In an orthonormal multiplicity basis its generator is a real skew 2x2.
    b = sp.symbols("b", real=True)
    compact_generator = sp.Matrix([[0, -b], [b, 0]])
    results = {
        "left_phase_variation": str(left),
        "conjugation_variation": str(conjugate),
        "scalar_mass_squared": str(mass2),
        "lorentz_commutant_constraint_rank": rank,
        "lorentz_commutant_dimension": 64 - rank,
        "block_basis_commutes": commutes,
        "nontrivial_compact_generator_determinant": str(compact_generator.det()),
        "neutral_bilinear_variation": str(invariant),
        "neutral_bilinear_linearization_at_zero": [str(x.subs({z: 0 for z in (*u, *w)}))
                                                    for x in sp.derive_by_array(2 * (quadratic(u) + quadratic(w)), (*u, *w))],
    }
    assert left == sp.I * v and conjugate == 0
    assert sp.simplify(mass2 - 2 * e**2 * q**2 * v**2) == 0
    assert rank == 60 and commutes and invariant == 0
    assert all(x == "0" for x in results["neutral_bilinear_linearization_at_zero"])
    return results


def numeric_checks(seed: int = 43127, samples: int = 80) -> dict:
    rng = np.random.default_rng(seed)
    one = np.eye(2, dtype=complex)
    pauli = [np.array([[0, 1], [1, 0]], dtype=complex),
             np.array([[0, -1j], [1j, 0]], dtype=complex),
             np.diag([1, -1]).astype(complex)]
    sharp = lambda x: np.trace(x) * one - x
    inv = lambda x: np.trace(sharp(x) @ x.conj().T)
    maximum = 0.0
    for _ in range(samples):
        x = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        direction = rng.normal(size=3)
        direction /= np.linalg.norm(direction)
        generator = sum(z * p for z, p in zip(direction, pauli))
        rapidity, alpha = rng.uniform(-0.8, 0.8, size=2)
        s = np.cosh(rapidity / 2) * one + np.sinh(rapidity / 2) * generator
        xp = np.exp(1j * alpha) * s @ x @ s.conj().T
        maximum = max(maximum, abs(inv(xp) - inv(x)))
        # A non-unitary basis change cannot create a neutral direction.
        basis = rng.normal(size=(2, 2))
        if abs(np.linalg.det(basis)) > 0.1:
            charge = np.linalg.solve(basis, np.array([[0., -1.], [1., 0.]]) @ basis)
            assert abs(np.linalg.det(charge) - 1) < 1e-11
        # Independently evaluate the kinetic energy, not the symbolic formula.
        v = rng.normal(size=3) + 1j * rng.normal(size=3)
        charge = np.diag([0., 1., -2.])
        avec, coupling = rng.uniform(.1, 2, size=2)
        derivative = 1j * coupling * avec * charge @ v
        actual = np.vdot(derivative, derivative).real
        mass = 2 * coupling**2 * np.vdot(charge @ v, charge @ v).real
        assert np.isclose(actual, .5 * mass * avec**2)
        # Two-body threshold: minimizing energies puts both constituents at
        # the same velocity; off-minimum samples must not lie below it.
        ma, mb = rng.uniform(.1, 3, size=2)
        k, p = rng.normal(size=(2, 3))
        minimum = np.sqrt(k @ k + (ma + mb)**2)
        total = np.sqrt(p @ p + ma**2) + np.sqrt((k-p) @ (k-p) + mb**2)
        pstar = ma * k / (ma + mb)
        attained = np.sqrt(pstar @ pstar + ma**2) + np.sqrt((k-pstar) @ (k-pstar) + mb**2)
        assert total >= minimum - 1e-12 and abs(attained - minimum) < 1e-12
    assert maximum < 1e-10
    return {"seed": seed, "samples": samples, "maximum_invariant_error": maximum,
            "tolerance": 1e-10, "passed": True}


def build_record() -> dict:
    return {
        "schema": "ubt-u1-neutrality/v1",
        "base_commit": "5cde1af91541cd33e3ae61b13a82f9639e9d2dfb",
        "claim_id": "GAP-U1-NEUTRALITY",
        "status": "FORMER_PROOF_REFUTED; PHYSICAL_BRIDGE_OPEN",
        "assumptions": [
            "The audited phase acts by left multiplication, not conjugation.",
            "The mass formula assumes positive canonical complex-scalar kinetic normalization.",
            "The commutant theorem concerns real-linear actions on Mat(2,C) commuting with S X S^dagger.",
            "The two-body threshold comparison assumes positive relativistic free modes, not a selected UBT spectrum.",
        ],
        "tools": {"python": platform.python_version(), "sympy": sp.__version__, "numpy": np.__version__},
        "exact": exact_checks(), "numerical": numeric_checks(),
        "lean_status": "LEAN-PENDING: no lean or lake executable available in the verification runtime",
        "limitations": ["No UBT physical Hessian, charge embedding, bound-state pole, EM matching coefficient or adjacent-universe channel is derived.",
                        "The noncompact Lorentz bilinear is not a positive norm.",
                        "Numerical checks do not prove analytic statements; no human attestation is made."],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    record = build_record()
    rendered = json.dumps(record, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
