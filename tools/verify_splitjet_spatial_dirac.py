#!/usr/bin/env python3
"""Conditional gravity-only parent reduction; no microscopic UBT selection.

Exact tests cover graph Dirac blocks, temporal chains and a field-dependent
Lorentz-adapted cotangent chart. An independent NumPy/SciPy implementation
checks the graph bracket on an actual three-dimensional periodic grid.
"""
from functools import lru_cache
from itertools import combinations
import json

import numpy as np
import scipy
from scipy import sparse
import sympy as s

ETA = (-1, 1, 1, 1)
PAIRS = tuple(combinations(range(4), 2))


def generators():
    matrices = []
    for a, b in PAIRS:
        matrix = s.zeros(4)
        matrix[a, b], matrix[b, a] = ETA[b], -ETA[a]
        matrices.append(matrix)
    return matrices


def adapted_map(x, u):
    """(Q^a,z^I) -> (w,K01,K02,K03,K12,K13,K23), future timelike X."""
    eta = s.diag(*ETA)
    r = s.sqrt(x[0]**2-sum(t**2 for t in x[1:]))
    boost = s.eye(4)
    boost[0, 0] = x[0]/r
    for i in range(1, 4):
        boost[0, i] = boost[i, 0] = x[i]/r
        for j in range(1, 4):
            boost[i, j] += x[i]*x[j]/(r*(x[0]+r))
    inverse = eta*boost.T*eta
    q_rest = inverse*s.Matrix(u[:4])
    rest = s.zeros(4)
    for i in range(1, 4):
        rest[0, i] = rest[i, 0] = q_rest[i]/r
    for (i, j), z in zip([(1, 2), (1, 3), (2, 3)], u[4:]):
        rest[i, j], rest[j, i] = z, -z
    K = boost*rest*inverse
    return s.Matrix([q_rest[0]/r]+[K[i, j] for i, j in PAIRS]), boost, K


@lru_cache(maxsize=1)
def symbolic_checks():
    checks = {}
    # General graph pair (P_Q, Q-F), allowing nonzero {F,F}.
    k0, k1, k2 = s.symbols("k0 k1 k2")
    K = s.Matrix([[0, k0, k1], [-k0, 0, k2], [-k1, -k2, 0]])
    zero, identity = s.zeros(3), s.eye(3)
    C = zero.row_join(-identity).col_join(identity.row_join(K))
    inverse = K.row_join(identity).col_join((-identity).row_join(zero))
    checks["graph_block_inverse_left"] = inverse*C == s.eye(6)
    checks["graph_block_inverse_right"] = C*inverse == s.eye(6)
    checks["graph_block_determinant_one_with_mixed_brackets"] = C.det() == 1
    left, right = s.Matrix(1, 3, s.symbols("u:3")), s.Matrix(3, 1, s.symbols("v:3"))
    # Observables independent of Q,P_Q have coupling (0,{A,Q-F}).
    checks["physical_Dirac_correction_zero_without_freezing_F"] = (
        s.zeros(1, 3).row_join(left)*inverse*s.zeros(3, 1).col_join(right))[0] == 0

    # Direct, unreordered 56-constraint matrix. This retains the mixed
    # temporal/spatial brackets instead of assuming a block diagonal matrix.
    # One linear graph fixture; spatial derivative operators are tested on
    # the separate genuinely three-dimensional grid below.
    nq = 52  # X[4], Q_mu[16], lambda_mu[16], base E_mu[16].
    rows = []
    def linear_constraint(entries):
        row = s.zeros(1, 2*nq)
        for column, value in entries.items():
            row[column] = value
        rows.append(row)
    for a in range(4):
        linear_constraint({nq+20+a: 1})
        linear_constraint({nq+a: 1, 20+a: 1})
    for mu in range(1, 4):
        for a in range(4):
            linear_constraint({nq+20+4*mu+a: 1})
            linear_constraint({20+4*mu+a: 1})
    for mu in range(1, 4):
        A = mu*s.eye(4)+generators()[mu-1]
        for a in range(4):
            linear_constraint({nq+4+4*mu+a: 1})
            entries = {4+4*mu+a: 1, 36+4*mu+a: -2}
            entries.update({b: A[a, b] for b in range(4)})
            linear_constraint(entries)
    jac = s.Matrix.vstack(*rows)
    canonical = s.zeros(nq).row_join(s.eye(nq)).col_join((-s.eye(nq)).row_join(s.zeros(nq)))
    full_C = jac*canonical*jac.T
    full_inverse = full_C.inv()
    checks["all_56_second_class_constraints_invertible"] = full_C*full_inverse == s.eye(56)
    checks["temporal_spatial_mixed_constraints_nonzero"] = full_C[:8, 32:] != s.zeros(8, 24)
    checks["full_second_class_determinant_one"] = full_C.det() == 1
    physical = list(range(4))+list(range(36, 52))
    retained = physical+[nq+j for j in physical]
    dirac = canonical-canonical*jac.T*full_inverse*jac*canonical
    checks["full_mixed_reduction_preserves_base_and_X_brackets"] = (
        dirac.extract(retained, retained) == canonical.extract(retained, retained))

    x, p = s.Matrix(s.symbols("X:4")), s.Matrix(s.symbols("p:4"))
    q, pq = s.Matrix(s.symbols("Q:4")), s.Matrix(s.symbols("P:4"))
    E0, eps, eps_dot = [s.Matrix(s.symbols(f"{name}:4")) for name in ["E", "eps", "epsdot"]]
    scale = s.Symbol("scale", positive=True)
    omega = sum((v*T for v, T in zip(s.symbols("omega:6"), generators())), s.zeros(4))
    H = (p.T*(scale*E0-omega*x-q))[0]
    coords, momenta = list(x)+list(q), list(p)+list(pq)

    def pb(A, B):
        return s.expand(sum(s.diff(A, c)*s.diff(B, m)-s.diff(A, m)*s.diff(B, c)
                            for c, m in zip(coords, momenta)))

    for a in range(4):
        checks[f"temporal_primary_preservation_{a}"] = pb(pq[a], H) == p[a]
        checks[f"temporal_secondary_closure_{a}"] = s.expand(pb(p[a], H)-(omega.T*p)[a]) == 0
    G = (eps.T*p-(eps_dot+omega*eps).T*pq)[0]
    for a in range(4):
        checks[f"vertical_generator_X_{a}"] = pb(x[a], G) == eps[a]
        checks[f"vertical_generator_Q0_{a}"] = s.expand(pb(q[a], G)+(eps_dot+omega*eps)[a]) == 0
    checks["parent_extra_phase_dimension_zero"] = 2*(4+16+16+12)-56-2*20 == 0

    # Complete smooth timelike adapted chart, evaluated at a rational point.
    # X=(5,3,0,0), invariant radius 4; transverse X derivatives are retained.
    u = s.Matrix(s.symbols("u:7"))
    old, boost, lorentz = adapted_map(list(x), list(u))
    point_x = dict(zip(x, [5, 3, 0, 0]))
    point_u = dict(zip(u, [2, 1, -1, 3, s.Rational(1, 2), -2, 1]))
    point = point_x | point_u
    eta = s.diag(*ETA)
    checks["adapted_boost_preserves_Lorentz_metric"] = s.simplify((boost.T*eta*boost-eta).subs(point_x)) == s.zeros(4)
    checks["adapted_K_is_Lorentz_antisymmetric"] = s.simplify((lorentz.T*eta+eta*lorentz).subs(point)) == s.zeros(4)
    checks["adapted_chart_recovers_all_Q_components"] = s.simplify(
        (lorentz*x+old[0]*x-s.Matrix(u[:4])).subs(point)) == s.zeros(4, 1)
    M = old.jacobian(u).subs(point_x).applyfunc(s.simplify)
    checks["seven_auxiliary_coordinates_invertible"] = M.det() != 0
    position_map = x.col_join(old)
    new_position = list(x)+list(u)
    jacobian = position_map.jacobian(new_position).subs(point).applyfunc(s.simplify)
    checks["all_X_dependent_position_derivatives_retained"] = jacobian[4:, :4] != s.zeros(7, 4)
    old_p = s.Matrix([s.Rational(i+1, 3) for i in range(11)])
    new_p = jacobian.T*old_p
    naive = old_p[:4, :].col_join(M.T*old_p[4:, :])
    checks["dropping_the_X_momentum_shift_fails"] = new_p != naive
    weighted = (old_p.T*position_map)[0]
    hessian = s.hessian(weighted, new_position).subs(point).applyfunc(s.simplify)
    inverse_t = jacobian.inv().T
    phase_map = jacobian.row_join(s.zeros(11)).col_join((-inverse_t*hessian).row_join(inverse_t))
    symplectic = s.zeros(11).row_join(s.eye(11)).col_join((-s.eye(11)).row_join(s.zeros(11)))
    checks["field_dependent_cotangent_map_is_symplectic"] = phase_map.T*symplectic*phase_map == symplectic
    checks["phase_space_Jacobian_one"] = phase_map.det() == 1
    # All four spacetime columns share X: their momentum corrections add.
    dM = [old.jacobian(u).diff(xx).subs(point_x).applyfunc(s.simplify) for xx in x]
    shared = s.diag(s.eye(4), M, M, M, M)
    old_covector = s.Matrix([s.Rational(i+1, 7) for i in range(32)])
    corrected_X = old_covector[:4, :].copy()
    for mu in range(4):
        data = s.Matrix([s.Rational(i+mu+1, 5) for i in range(7)])
        response = s.Matrix.hstack(*(matrix*data for matrix in dM))
        shared[4+7*mu:11+7*mu, :4] = response
        corrected_X += response.T*old_covector[4+7*mu:11+7*mu, :]
    checks["shared_X_momentum_sums_all_four_columns"] = (shared.T*old_covector)[:4, :] == corrected_X
    return checks


def periodic_operators(n=3):
    delta = 2*np.pi/n
    eye = sparse.eye(n, format="csr")
    one = sparse.csr_matrix((np.roll(np.eye(n), 1, axis=1)-np.roll(np.eye(n), -1, axis=1))/(2*delta))
    return [sparse.kron(sparse.kron(one if axis == 0 else eye, one if axis == 1 else eye),
                        one if axis == 2 else eye, format="csr") for axis in range(3)]


def numerical_checks(n=3, seed=20261029):
    """Full 3D periodic spatial graph: dynamic coframe and connection coordinates."""
    rng = np.random.default_rng(seed)
    cells = n**3
    D = periodic_operators(n)
    basis = np.array([np.array(T).astype(float) for T in generators()])
    e_count, omega_count, x_count = 12*cells, 18*cells, 4*cells
    base_count = e_count+omega_count+x_count
    graph_count = e_count
    E = rng.normal(scale=.08, size=(3, cells, 4))
    for i in range(3):
        E[i, :, i+1] += 1
    components = rng.normal(scale=.1, size=(3, cells, 6))
    X = rng.normal(scale=.1, size=(cells, 4)); X[:, 0] += 2
    omega = np.einsum("dnc,cab->dnab", components, basis)
    scale = 1.7
    J_E = scale*sparse.eye(graph_count, format="csr")
    J_X = sparse.vstack([-sparse.kron(D[i], sparse.eye(4), format="csr")
                        - sparse.block_diag(omega[i], format="csr") for i in range(3)], format="csr")
    J_omega = sparse.block_diag([
        sparse.block_diag([-np.stack([T@X[site] for T in basis], axis=1)
                           for site in range(cells)], format="csr") for _ in range(3)], format="csr")
    J_F = sparse.hstack([J_E, J_omega, J_X], format="csr")
    identity = sparse.eye(graph_count, format="csr")
    zero_base = sparse.csr_matrix((graph_count, base_count))
    zero_graph = sparse.csr_matrix((graph_count, graph_count))
    # Constraints are ordered (P_Q, Q-F); build their gradients independently.
    Cq = sparse.vstack([sparse.hstack([zero_base, zero_graph]), sparse.hstack([-J_F, identity])], format="csr")
    Cp = sparse.vstack([sparse.hstack([zero_base, identity]), sparse.hstack([zero_base, zero_graph])], format="csr")
    bracket_matrix = (Cq@Cp.T-Cp@Cq.T).toarray()
    inverse = np.linalg.inv(bracket_matrix)
    # Generic physical observables include coframe/connection/X momenta.
    Bq = rng.normal(size=(16, base_count))
    Bp = rng.normal(size=(16, base_count))
    mixed = Bp@J_F.T
    mixed = np.hstack([np.zeros((16, graph_count)), mixed])
    correction = mixed@inverse@mixed.T

    def graph(E, coeff, X):
        W = np.einsum("dnc,cab->dnab", coeff, basis)
        return scale*E-np.stack([D[i]@X for i in range(3)])-np.einsum("dnab,nb->dna", W, X)

    delta = rng.normal(size=base_count)
    de = delta[:e_count].reshape(E.shape)
    dw = delta[e_count:e_count+omega_count].reshape(components.shape)
    dx = delta[-x_count:].reshape(X.shape)
    epsilon = 1e-5
    fd = (graph(E+epsilon*de, components+epsilon*dw, X+epsilon*dx)
          - graph(E-epsilon*de, components-epsilon*dw, X-epsilon*dx))/(2*epsilon)
    gradient_error = np.max(np.abs(fd.ravel()-J_F@delta))
    inverse_error = np.max(np.abs(bracket_matrix@inverse-np.eye(2*graph_count)))
    correction_error = np.max(np.abs(correction))
    metric = np.einsum("ina,a,jna->nij", E, np.asarray(ETA), E)
    metric_minimum = np.linalg.eigvalsh(metric).min()
    carrier_norm = -X[:, 0]**2+np.sum(X[:, 1:]**2, axis=1)
    return {"grid_points_per_direction": n, "spatial_cells": cells, "internal_real_dimension": 4,
            "graph_constraints": 2*graph_count, "seed": seed, "finite_difference_step": epsilon,
            "maximum_gradient_error": float(gradient_error), "maximum_inverse_error": float(inverse_error),
            "maximum_physical_Dirac_correction": float(correction_error),
            "minimum_spatial_metric_eigenvalue": float(metric_minimum),
            "mixed_bracket_norm": float(np.linalg.norm(mixed)),
            "checks": {"three_nonzero_spatial_derivatives": all(np.linalg.norm(v.toarray()) > 0 for v in D),
                       "independent_graph_derivative": bool(gradient_error < 1e-8),
                       "full_constraint_matrix_invertible": bool(inverse_error < 1e-11),
                       "physical_bracket_unchanged": bool(correction_error < 1e-10),
                       "regular_spacelike_coframe": bool(metric_minimum > .4),
                       "future_timelike_carrier": bool(np.all(carrier_norm < 0) and np.all(X[:, 0] > 0)),
                       "mixed_brackets_are_not_frozen": bool(np.linalg.norm(mixed) > 1)}}


def run_checks():
    exact, numerical = symbolic_checks(), numerical_checks()
    return {"scope": "Local gravity-only split-jet parent of a supplied Palatini/GR base; extra constraints and physical bracket equivalence, not microscopic action selection",
            "versions": {"sympy": s.__version__, "numpy": np.__version__, "scipy": scipy.__version__},
            "symbolic": exact, "numerical": numerical,
            "passed": all(exact.values()) and all(numerical["checks"].values()),
            "not_proved": ["microscopic Theta action or its positive Newton coefficient", "full complex-time/matter/colour constraints", "null/global/horizon reduction", "formal continuum Dirac field theory", "microscopic quantum measure"]}


if __name__ == "__main__":
    report = run_checks()
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["passed"] else 1)
