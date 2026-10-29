#!/usr/bin/env python3
"""A local nonlinear Cartan chart on the written eight-real Theta model.

This does not change the canonical sharp metric or select a UBT action.
It extends the declared Lorentz action locally, retains both real vectors,
and explicitly FAILS compatibility with the independent standard field phase.
"""
from functools import lru_cache
from itertools import combinations
import json

import numpy as np
import scipy
from scipy.linalg import expm
import sympy as s

ETA = (-1, 1, 1, 1)
PAIRS = tuple(combinations(range(4), 2))


def lorentz_generator(a, b):
    out = s.zeros(4)
    out[a, b] = ETA[b]
    out[b, a] = -ETA[a]
    return out


@lru_cache(maxsize=1)
def symbolic_checks():
    eta = s.diag(*ETA)
    x = s.Matrix(s.symbols("x:4", real=True))
    y = s.Matrix(s.symbols("y:4", real=True))
    ell = s.Symbol("ell", positive=True)
    phi = s.sqrt(ell**2 - (x.T * eta * x)[0])
    h = (x.T * eta * y)[0]
    n, v = x.col_join(s.Matrix([phi])), y.col_join(s.Matrix([-h / phi]))
    metric5 = s.diag(-1, 1, 1, 1, 1)
    coords = list(x) + list(y)
    joint = n.col_join(v)
    minor = joint.jacobian(coords)[[0, 1, 2, 3, 5, 6, 7, 8], :]
    checks = {
        "derived_compensator_fixed_norm": s.simplify((n.T * metric5 * n)[0] - ell**2) == 0,
        "derived_fiber_is_tangent": s.simplify((n.T * metric5 * v)[0]) == 0,
        "joint_lift_has_rank_eight_minor_one": minor.det() == 1,
        "all_real_coordinates_recovered": n[:4, :] == x,
        "all_imaginary_coordinates_recovered": v[:4, :] == y,
    }
    sigma = [s.eye(2), s.Matrix([[0, 1], [1, 0]]),
             s.Matrix([[0, -s.I], [s.I, 0]]), s.diag(1, -1)]
    pauli = lambda z: sum((z[i] * sigma[i] for i in range(4)), s.zeros(2))
    theta = pauli(x) + s.I * pauli(y)
    checks["complex_Theta_coordinates_are_not_discarded"] = (
        s.simplify((theta + theta.conjugate().T)/2 - pauli(x)) == s.zeros(2)
        and s.simplify((theta - theta.conjugate().T)/(2*s.I) - pauli(y)) == s.zeros(2))
    spin_boost = s.diag(2, s.Rational(1, 2))
    boost = s.eye(4)
    boost[0, 0] = boost[3, 3] = s.Rational(17, 8)
    boost[0, 3] = boost[3, 0] = s.Rational(15, 8)
    checks["declared_Lorentz_action_matches_matrix_congruence"] = (
        s.simplify(spin_boost * theta * spin_boost.conjugate().T
                   - pauli(boost*x) - s.I*pauli(boost*y)) == s.zeros(2))
    checks["declared_boost_preserves_internal_Lorentz_metric"] = boost.T*eta*boost == eta

    # A constant linear extension would require a Lorentz-vector family of
    # endomorphisms in EACH 4x4 block of End(V direct_sum V).
    unknowns = s.symbols("u:64")
    operators = [s.Matrix(4, 4, unknowns[16*a:16*(a+1)]) for a in range(4)]
    equations = []
    for a, b in PAIRS:
        J = lorentz_generator(a, b)
        for c in range(4):
            equations.extend(J * operators[c] - operators[c] * J
                             - eta[b, c] * operators[a] + eta[a, c] * operators[b])
    matrix, rhs = s.linear_eq_to_matrix(equations, unknowns)
    checks["constant_linear_extension_covariance_rank_64"] = (
        matrix.shape == (384, 64) and matrix.rank() == 64 and rhs == s.zeros(384, 1))

    # Negative fundamental vector fields make M -> F_M a Lie homomorphism.
    def bracket(A, B):
        return (B.jacobian(coords) * A - A.jacobian(coords) * B).applyfunc(s.simplify)

    broken = []
    for a in range(4):
        field = s.zeros(8, 1)
        field[a], field[4+a] = -phi, h / phi
        broken.append(field)
    phase = s.Matrix(list(-y) + list(x))
    for a, b in PAIRS:
        lorentz = -s.diag(lorentz_generator(a, b), lorentz_generator(a, b)) * s.Matrix(coords)
        checks[f"broken_bracket_{a}_{b}"] = (
            (bracket(broken[a], broken[b]) + lorentz).applyfunc(s.simplify) == s.zeros(8, 1))
        checks[f"ordinary_phase_commutes_with_Lorentz_{a}_{b}"] = (
            bracket(phase, lorentz) == s.zeros(8, 1))
        for c in range(4):
            predicted = eta[b, c] * broken[a] - eta[a, c] * broken[b]
            checks[f"mixed_bracket_{a}_{b}_{c}"] = (
                (bracket(lorentz, broken[c]) - predicted).applyfunc(s.simplify) == s.zeros(8, 1))
    nonzero = s.Symbol("r", positive=True)
    point = {**{z: 0 for z in coords}, x[0]: nonzero}
    for a in range(4):
        obstruction = bracket(phase, broken[a]).subs(point).applyfunc(s.simplify)
        target = s.zeros(8, 1)
        target[4+a] = ell**2 / s.sqrt(ell**2 + nonzero**2)
        checks[f"phase_obstruction_at_invertible_Theta_{a}"] = (
            (obstruction - target).applyfunc(s.simplify) == s.zeros(8, 1))
    return checks


def lift_point(x, y, ell):
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    if x.shape != (4,) or y.shape != (4,) or not np.all(np.isfinite(np.r_[x, y, ell])) or ell <= 0:
        raise ValueError("finite real chart data and positive ell required")
    radicand = ell**2 - np.dot(np.asarray(ETA) * x, x)
    if radicand <= 0:
        raise ValueError("point lies outside the positive-radical chart")
    phi = np.sqrt(radicand)
    h = np.dot(np.asarray(ETA) * x, y)
    return np.r_[x, phi], np.r_[y, -h / phi]


def chart_action(x, y, ell, group):
    group = np.asarray(group, dtype=float)
    metric = np.diag([-1, 1, 1, 1, 1])
    if (group.shape != (5, 5) or not np.all(np.isfinite(group))
            or not np.allclose(group.T @ metric @ group, metric, atol=1e-11, rtol=0)
            or not np.isclose(np.linalg.det(group), 1, atol=1e-11, rtol=0)):
        raise ValueError("declared SO(1,4) group element required")
    n, v = lift_point(x, y, ell)
    new_n, new_v = group @ n, group @ v
    if new_n[4] <= 0:
        raise ValueError("transformation leaves the positive-radical chart")
    lift_point(new_n[:4], new_v[:4], ell)
    return new_n[:4], new_v[:4]


def numerical_checks(samples=24, seed=20261029):
    rng = np.random.default_rng(seed)
    metric = np.diag([-1, 1, 1, 1, 1])
    worst_lift = worst_composition = worst_inverse = 0.0

    def group_element():
        raw = rng.normal(scale=0.025, size=(5, 5))
        generator = metric @ (raw - raw.T)
        return expm(generator)

    for _ in range(samples):
        ell = rng.uniform(1, 2)
        x, y = rng.normal(scale=0.1, size=(2, 4))
        first, second = group_element(), group_element()
        n, v = lift_point(x, y, ell)
        xx, yy = chart_action(x, y, ell, first)
        nn, vv = lift_point(xx, yy, ell)
        worst_lift = max(worst_lift, np.max(np.abs(nn - first @ n)), np.max(np.abs(vv - first @ v)))
        a, b = chart_action(xx, yy, ell, second)
        c, d = chart_action(x, y, ell, second @ first)
        worst_composition = max(worst_composition, np.max(np.abs(a - c)), np.max(np.abs(b - d)))
        back_x, back_y = chart_action(xx, yy, ell, np.linalg.inv(first))
        worst_inverse = max(worst_inverse, np.max(np.abs(back_x - x)), np.max(np.abs(back_y - y)))
    return {
        "samples": samples, "seed": seed,
        "max_lift_covariance_error": float(worst_lift),
        "max_local_composition_error": float(worst_composition),
        "max_inverse_error": float(worst_inverse),
        "checks": {"lift_covariance": bool(worst_lift < 1e-11),
                   "local_composition": bool(worst_composition < 1e-11),
                   "inverse_preserves_all_data": bool(worst_inverse < 1e-11)},
    }


def run_checks():
    symbolic, numerical = symbolic_checks(), numerical_checks()
    return {
        "scope": "Local nonlinear SO(1,4) chart on the written two-real-Lorentz-vector Theta carrier; standard independent field-phase compatibility fails",
        "versions": {"sympy": s.__version__, "numpy": np.__version__, "scipy": scipy.__version__},
        "symbolic": symbolic, "numerical": numerical,
        "passed": all(symbolic.values()) and all(numerical["checks"].values()),
        "not_proved": ["canonical sharp tetrad/metric equivalence", "selected local SO(1,4) gauge symmetry or connection", "compatible independent standard field phase", "normalization relating the field-coordinate scale to a gravity length", "microscopic action, physical Dirac reduction or stability", "global chart or fundamental Theta component count"],
    }


if __name__ == "__main__":
    report = run_checks()
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["passed"] else 1)
