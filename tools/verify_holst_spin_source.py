#!/usr/bin/env python3
"""Full 24-component, fixed-tetrad sourced Holst comparator.

This is a diagnostic of an IMPORTED effective action, not the microscopic UBT
action or its composite-Theta variation.  An external, normalized axial source
is declared, not derived.  Constant-coefficient Nieh--Yan boundary terms are
discarded only under compact-support/fixed-boundary assumptions.
"""
from __future__ import annotations

from functools import lru_cache
from itertools import combinations, permutations
import json

import numpy as np
import sympy as s

ETA = (-1, 1, 1, 1)
PAIRS = tuple(combinations(range(4), 2))
PERMUTATIONS = tuple(permutations(range(4)))


def epsilon(*indices):
    """Lower epsilon_0123=+1 in the oriented orthonormal frame."""
    if len(set(indices)) != 4:
        return 0
    inversions = sum(indices[i] > indices[j]
                     for i in range(4) for j in range(i + 1, 4))
    return (-1) ** inversions


def connection(coordinates):
    """K^{ab}_mu, antisymmetric in its two raised Lorentz indices."""
    out = [[[s.Integer(0) for _ in range(4)] for _ in range(4)]
           for _ in range(4)]
    for i, (a, b) in enumerate(PAIRS):
        for mu in range(4):
            out[a][b][mu] = coordinates[4 * i + mu]
            out[b][a][mu] = -coordinates[4 * i + mu]
    return out


def gravity_quadratic(K, beta):
    """Coefficient of the Palatini + beta*Holst four-form, at kappa=1.

After omega=omega_LC+K, the D_LC K term is a boundary term.  No homogeneous
spacetime restriction is used: all 24 pointwise contortion entries are varied.
    """
    palatini = 0
    holst = 0
    for a, b, c, d in PERMUTATIONS:
        for mu, nu in permutations(i for i in range(4) if i not in (a, b)):
            for f in range(4):
                palatini += (epsilon(a, b, c, d) * epsilon(a, b, mu, nu)
                              * ETA[f] * K[c][f][mu] * K[f][d][nu])
    for a, b in permutations(range(4), 2):
        for mu, nu in permutations(i for i in range(4) if i not in (a, b)):
            for f in range(4):
                holst += (ETA[a] * ETA[b] * epsilon(a, b, mu, nu)
                          * ETA[f] * K[a][f][mu] * K[f][b][nu])
    return s.expand(palatini / 4 + beta * holst / 2)


def axial_components(K):
    """A^r=-epsilon^{rabd} K_abd/6; epsilon^0123=-1."""
    return s.Matrix([
        s.expand(sum(epsilon(r, a, b, d) * ETA[a] * ETA[b] * K[a][b][d]
                     for a, b, d in permutations(i for i in range(4) if i != r)) / 6)
        for r in range(4)])


def trace_components(K):
    return s.Matrix([sum(K[a][b][b] for b in range(4)) / 3
                     for a in range(4)])


def axial_trace_connection(A, V):
    return [[[sum(ETA[a] * ETA[b] * epsilon(a, b, c, d) * A[c]
                  for c in range(4))
              + V[a] * int(b == d) - V[b] * int(a == d)
              for d in range(4)] for b in range(4)] for a in range(4)]


def torsion_square(K):
    """Independent T_a wedge T^a coefficient from T^a=K^a_b wedge e^b."""
    torsion = [
        {(mu, nu): ETA[nu] * K[a][nu][mu] - ETA[mu] * K[a][mu][nu]
         for mu, nu in PAIRS} for a in range(4)]
    return s.expand(sum(ETA[a] * epsilon(mu, nu, rho, sigma)
                        * torsion[a][mu, nu] * torsion[a][rho, sigma]
                        for a in range(4)
                        for mu, nu in PAIRS for rho, sigma in PAIRS))


@lru_cache(maxsize=1)
def symbolic_checks():
    beta, b, zeta, shift = s.symbols("beta b zeta shift", real=True)
    kappa = s.Symbol("kappa", positive=True)
    coordinates = s.symbols("K:24", real=True)
    source = s.Matrix(s.symbols("J:4", real=True))
    metric = s.diag(*ETA)
    K = connection(coordinates)
    quadratic = gravity_quadratic(K, beta)
    hessian = s.hessian(quadratic, coordinates)
    A = s.Matrix(s.symbols("A:4", real=True))
    V = s.Matrix(s.symbols("V:4", real=True))
    restricted = axial_trace_connection(A, V)
    dot = lambda x, y: (x.T * metric * y)[0]
    zero = lambda expression: s.factor(expression) == 0
    checks = {
        "axial_readout_matches_declared_normalization": axial_components(restricted) == A,
        "trace_readout_matches_declared_normalization": trace_components(restricted) == V,
        "full_quadratic_restricts_to_axial_trace_form": zero(
            gravity_quadratic(restricted, beta)
            - 3 * (dot(A, A) - dot(V, V) - 2 * beta * dot(A, V))),
        "full_24_hessian_determinant": zero(
            hessian.det(method="domain-ge") - 256 * (1 + beta**2)**12),
        "complex_selfdual_hessian_is_singular": hessian.subs(beta, s.I).rank() == 12,
        "torsion_square_matches_Holst_bulk_quadratic": zero(
            torsion_square(K) - 2 * s.diff(quadratic, beta)),
    }
    astar = -kappa * source / (6 * (1 + beta**2))
    vstar = -beta * astar
    stationary = axial_trace_connection(astar, vstar)
    candidate = {coordinates[4 * i + mu]: stationary[a][b_][mu]
                 for i, (a, b_) in enumerate(PAIRS) for mu in range(4)}
    action = quadratic / kappa + dot(source, axial_components(K))
    for i, variable in enumerate(coordinates):
        checks[f"full_connection_Euler_equation_{i:02d}"] = zero(
            s.diff(action, variable).subs(candidate))
    checks["on_shell_contact_in_full_24_model"] = zero(
        action.subs(candidate) + kappa * dot(source, source) / (12 * (1 + beta**2)))
    for i in range(4):
        checks[f"unique_solution_axial_component_{i}"] = zero(
            axial_components(stationary)[i] - astar[i])
        checks[f"unique_solution_trace_component_{i}"] = zero(
            trace_components(stationary)[i] - vstar[i])
    for i, value in enumerate(candidate.values()):
        composed = value.subs(beta, b + zeta)
        moved = composed.subs({b: b + shift, zeta: zeta - shift}, simultaneous=True)
        checks[f"coefficient_shift_preserves_connection_{i:02d}"] = zero(moved - composed)
    contact_weight = 1 / (1 + (b + zeta)**2)
    gradient = s.Matrix([s.diff(contact_weight, x) for x in (b, zeta)])
    information = gradient * gradient.T
    checks["contact_information_has_exact_null_direction"] = (
        (information * s.Matrix([1, -1])).applyfunc(s.factor) == s.zeros(2, 1))
    checks["contact_information_determinant_zero"] = zero(information.det())
    checks["contact_loses_sign_of_effective_coefficient"] = zero(
        contact_weight.subs({b: -b, zeta: -zeta}, simultaneous=True) - contact_weight)
    checks["trace_axial_ratio_retains_effective_sign"] = (
        (vstar + beta * astar).applyfunc(s.factor) == s.zeros(4, 1))
    return checks


def numerical_checks(samples=12, seed=20261029):
    """Independent NumPy tensor contraction and full 24x24 linear solve.

No symbolic Hessian, symbolic lambdification, or precomputed solution is used
to assemble the numerical equation.  The analytic answer is compared only
after the independent solve.
    """
    rng = np.random.default_rng(seed)
    metric = np.asarray(ETA, dtype=float)
    eps = np.zeros((4, 4, 4, 4))
    for indices in PERMUTATIONS:
        eps[indices] = epsilon(*indices)
    eye = np.eye(24)

    def tensor(vector):
        value = np.zeros((4, 4, 4))
        for i, (a, b) in enumerate(PAIRS):
            value[a, b, :] = vector[4 * i:4 * i + 4]
            value[b, a, :] = -value[a, b, :]
        return value

    def quadratic(vector, beta, kappa):
        value = tensor(vector)
        curvature = np.einsum("f,cfm,fdn->cdmn", metric, value, value)
        palatini = np.einsum("abcd,abmn,cdmn->", eps, eps, curvature)
        holst = np.einsum("a,b,abmn,abmn->", metric, metric, eps, curvature)
        return (palatini / 4 + beta * holst / 2) / kappa

    def axial(vector):
        return np.einsum("rabd,a,b,abd->r", eps, metric, metric, tensor(vector)) / 6

    max_solution_error = 0.0
    max_contact_error = 0.0
    max_stationarity_residual = 0.0
    max_shift_error = 0.0
    for _ in range(samples):
        b, zeta, shift = rng.uniform(-2, 2, 3)
        beta = b + zeta
        kappa = rng.uniform(0.2, 2)
        source = rng.normal(size=4)
        diagonals = np.array([quadratic(v, beta, kappa) for v in eye])
        hessian = np.diag(2 * diagonals)
        for i, j in combinations(range(24), 2):
            entry = quadratic(eye[i] + eye[j], beta, kappa) - diagonals[i] - diagonals[j]
            hessian[i, j] = hessian[j, i] = entry
        current = np.array([np.dot(metric * source, axial(v)) for v in eye])
        solution = np.linalg.solve(hessian, -current)
        a_expected = -kappa * source / (6 * (1 + beta**2))
        v_expected = -beta * a_expected
        predicted = np.einsum("a,b,abcd,c->abd", metric, metric, eps, a_expected)
        predicted += np.einsum("a,bd->abd", v_expected, np.eye(4))
        predicted -= np.einsum("b,ad->abd", v_expected, np.eye(4))
        max_solution_error = max(max_solution_error, float(np.max(np.abs(tensor(solution) - predicted))))
        evaluated = quadratic(solution, beta, kappa) + np.dot(metric * source, axial(solution))
        expected = -kappa * np.dot(metric * source, source) / (12 * (1 + beta**2))
        max_contact_error = max(max_contact_error, float(abs(evaluated - expected)))
        max_stationarity_residual = max(max_stationarity_residual, float(np.max(np.abs(hessian @ solution + current))))
        shifted = quadratic(solution, (b + shift) + (zeta - shift), kappa)
        max_shift_error = max(max_shift_error, float(abs(shifted - quadratic(solution, beta, kappa))))
    return {
        "seed": seed, "samples": samples,
        "max_connection_error": max_solution_error,
        "max_contact_error": max_contact_error,
        "max_full_Euler_residual": max_stationarity_residual,
        "max_coefficient_shift_error": max_shift_error,
        "checks": {
            "full_connection_solve": max_solution_error < 1e-11,
            "effective_contact": max_contact_error < 1e-11,
            "full_stationarity": max_stationarity_residual < 1e-11,
            "unidentifiable_shift": max_shift_error < 1e-11,
        },
    }


def run_checks():
    symbolic = symbolic_checks()
    numerical = numerical_checks()
    return {
        "scope": "Imported Palatini--Holst plus constant torsion-square comparator; fixed tetrad, full 24-component pointwise contortion, external normalized axial source, fixed boundary",
        "versions": {"sympy": s.__version__, "numpy": np.__version__},
        "symbolic": symbolic,
        "numerical": numerical,
        "passed": all(symbolic.values()) and all(numerical["checks"].values()),
        "not_proved": [
            "microscopic UBT action or spin-current normalization",
            "unrestricted composite-Theta field variation and physical Dirac reduction",
            "physical stability or a new propagating torsion mode",
            "quantum or boundary-sensitive equivalence",
            "selection of either independent parity-odd coefficient",
        ],
    }


if __name__ == "__main__":
    report = run_checks()
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["passed"] else 1)
