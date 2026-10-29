#!/usr/bin/env python3
"""Restricted timelike free-jet quadratic torsion principal tensor audit.

This is a necessary high-frequency test on a declared isotropic branch.
It neither selects a microscopic action nor counts the complete constraints.
"""
from functools import lru_cache
from itertools import product
import json

import numpy as np
import sympy as s

ETA = (-1, 1, 1, 1)
PAIRS = ((1, 2), (1, 3), (2, 3))


@lru_cache(maxsize=1)
def exact_model():
    ut, vt, uz, vz = q = s.symbols("ut vt uz vz", real=True)
    c1, c2, c3 = c = s.symbols("c1 c2 c3", real=True)
    z = s.symbols("z0:12", real=True)
    gt = s.Matrix([[ut, vt, 0], [vt, -ut, 0], [0, 0, 0]]) / 2
    gz = s.Matrix([[uz, vz, 0], [vz, -uz, 0], [0, 0, 0]]) / 2
    Z = [s.zeros(4) for _ in range(4)]
    for mu in range(4):
        for k, (i, j) in enumerate(PAIRS):
            Z[mu][i, j] = z[3 * mu + k]
            Z[mu][j, i] = -z[3 * mu + k]

    def de(i, mu, nu):
        if i == 0 or nu == 0:
            return s.S.Zero
        return gt[i-1, nu-1] if mu == 0 else gz[i-1, nu-1] if mu == 3 else s.S.Zero

    T = {(i, mu, nu): de(i, mu, nu) - de(i, nu, mu)
         + Z[mu][i, nu] - Z[nu][i, mu]
         for i, mu, nu in product(range(4), repeat=3)}
    I1 = s.expand(sum(ETA[i]*ETA[mu]*ETA[nu]*v**2 for (i, mu, nu), v in T.items()))
    I2 = s.expand(sum(ETA[mu]*v*T[nu, mu, i] for (i, mu, nu), v in T.items()))
    trace = [sum(T[nu, mu, nu] for nu in range(4)) for mu in range(4)]
    I3 = s.expand(sum(ETA[mu]*trace[mu]**2 for mu in range(4)))
    invariants = (I1, I2, I3)
    L = s.expand(sum(a*b for a, b in zip(c, invariants)))
    star = dict.fromkeys(z, s.S.Zero)
    star.update({z[4]: uz/2, z[5]: vz/2, z[7]: vz/2, z[8]: -uz/2})
    return q, c, z, T, invariants, L, star


@lru_cache(maxsize=1)
def symbolic_checks():
    q, c, z, T, invariants, L, star = exact_model()
    ut, vt, uz, vz = q
    c1, c2, c3 = c
    time = ut**2 + vt**2
    space = uz**2 + vz**2
    zero_z = dict.fromkeys(z, 0)
    checks = {}
    reduced = -(c1+c2/2)*time
    checks["full_contractions_give_frozen_TT_wave_form"] = s.expand(L.subs(zero_z)+(c1+c2/2)*(time-space)) == 0
    for n, (inv, value) in enumerate(zip(invariants, (-time, -time/2, 0)), 1):
        checks[f"stationary_invariant_{n}_has_no_spatial_gradient"] = s.expand(inv.subs(star)-value) == 0
    for n, variable in enumerate(z):
        checks[f"all_auxiliary_Euler_equations_at_solution_{n}"] = s.expand(s.diff(L, variable).subs(star)) == 0
    checks["all_spatial_torsion_components_are_cancelled"] = all(
        s.expand(T[i, mu, nu].subs(star)) == 0
        for i, mu, nu in product(range(1, 4), repeat=3))
    spatial = [T[i, mu, nu] for i in range(1, 4) for mu in range(1, 4) for nu in range(mu+1, 4)]
    cartan = s.Matrix(spatial).jacobian(z[3:])
    checks["spatial_Cartan_map_is_square_and_invertible"] = cartan.shape == (9, 9) and cartan.det() != 0
    checks["entire_constant_coefficient_family_has_same_gradient_obstruction"] = s.expand(L.subs(star)-reduced) == 0
    r = s.symbols("r0:12", real=True)
    shifted = {a: r[n]+star[a] for n, a in enumerate(z)}
    spatial_q = L.subs(dict.fromkeys(q, 0)).subs({a: r[n] for n, a in enumerate(z)})
    checks["exact_auxiliary_translation_removes_all_spatial_sources"] = s.expand(L.subs(shifted)-reduced-spatial_q) == 0
    checks["temporal_auxiliaries_do_not_mix_with_TT_velocity"] = all(s.diff(L, a, b) == 0 for a in z[:3] for b in q[:2])
    checks["temporal_auxiliary_block_has_declared_coefficient"] = s.expand(
        L.subs(dict.fromkeys(z[3:], 0)).subs({uz: 0, vz: 0})-reduced
        -2*(c2-2*c1)*sum(a*a for a in z[:3])) == 0
    eh = {c1: -s.Rational(1, 4), c2: -s.Rational(1, 2), c3: 1}
    Leh = L.subs(eh)
    checks["Einstein_sign_full_auxiliary_Hessian_has_rank_nine"] = s.hessian(Leh, z).rank() == 9
    checks["Einstein_sign_spatial_auxiliary_Hessian_is_invertible"] = s.hessian(Leh, z[3:]).det() != 0
    checks["Einstein_sign_temporal_auxiliaries_are_undetermined_in_this_block"] = all(s.diff(Leh, a) == 0 for a in z[:3])
    checks["Einstein_sign_tensor_time_coefficient_is_positive"] = s.expand(reduced.subs(eh)-time/2) == 0
    a, b, cc, d, e, f, g, h, ii = r[3:]
    Q = 2*(h*d-ii*a+b*f-cc*e+cc*g-e*g)
    checks["explicit_nine_variable_Einstein_auxiliary_polynomial"] = s.expand(spatial_q.subs(eh)-Q) == 0
    equations = (-2*ii, 2*f, 2*(-e+g), 2*h, 2*(-cc-g), 2*b, 2*(cc-e), 2*d, -2*a)
    checks["nine_Euler_equations_match_finite_formal_core"] = all(
        s.expand(s.diff(Q, x)-value) == 0 for x, value in zip(r[3:], equations))
    eigen = s.symbols("y0:12", real=True)
    H = s.hessian(L, z)
    checks["translated_auxiliary_action_is_homogeneous_quadratic"] = s.expand(spatial_q-(s.Matrix(r).T*H*s.Matrix(r))[0]/2) == 0
    # H y=0 is precisely the stationary condition, including singular cases.
    checks["singular_stationarity_cannot_restore_gradient_energy"] = s.expand(
        (s.Matrix(eigen).T*H*s.Matrix(eigen))[0]
        -sum(eigen[i]*sum(H[i, j]*eigen[j] for j in range(12)) for i in range(12))) == 0
    kappa = s.Symbol("kappa", positive=True)
    A = -(2*c1+c2)/(4*kappa)
    p, velocity = s.symbols("p velocity", real=True)
    checks["tensor_canonical_momentum"] = s.diff(A*velocity**2, velocity) == 2*A*velocity
    checks["tensor_reduced_Hamiltonian_has_no_gradient_term"] = s.cancel(
        (p*velocity-A*velocity**2).subs(velocity, p/(2*A))-p*p/(4*A)) == 0
    omega, wave_number = s.symbols("omega wave_number", real=True)
    principal = s.diff(reduced/(2*kappa), ut, ut)*omega**2 + s.diff(reduced/(2*kappa), uz, uz)*wave_number**2
    checks["tensor_principal_polynomial_has_no_wave_number"] = s.diff(principal, wave_number) == 0
    # A regular exact original-field stationary background, not merely an
    # off-shell point. This expanding FLRW example is not Einstein for any Lambda.
    t, scale = s.symbols("t scale", positive=True)
    expansion = s.exp(t*t/2)
    E = s.diag(1, expansion, expansion, expansion)
    X = s.Matrix([scale/t, 0, 0, 0])
    w = s.Matrix([t+1/t, 0, 0, 0])
    connection = [s.zeros(4) for _ in range(4)]
    for mu, i in product(range(4), range(1, 4)):
        connection[mu][i, 0] = connection[mu][0, i] = t*E[i, mu]
    def partial(value, mu):
        return s.diff(value, t) if mu == 0 else s.S.Zero
    generated = s.Matrix(4, 4, lambda i, mu:
        (partial(X[i], mu)+(connection[mu]*X)[i]+w[mu]*X[i])/scale)
    checks["exact_FLRW_original_composite_tetrad"] = all(s.simplify(x) == 0 for x in generated-E)
    background_T = [partial(E[i, nu], mu)-partial(E[i, mu], nu)
                    +sum(connection[mu][i, j]*E[j, nu]-connection[nu][i, j]*E[j, mu] for j in range(4))
                    for i, mu, nu in product(range(4), repeat=3)]
    checks["all_64_exact_FLRW_jet_torsion_components_vanish"] = all(s.simplify(x) == 0 for x in background_T)
    checks["exact_FLRW_original_carrier_is_timelike_nonnull"] = (-X[0]**2).is_negative is True
    curvature12 = connection[1]*connection[2]-connection[2]*connection[1]
    checks["exact_FLRW_jet_is_curved"] = s.simplify(curvature12[1, 2]-t*t*expansion**2) == 0
    metric = E.T*s.diag(*ETA)*E
    inverse = metric.inv()
    Gamma = [[[s.simplify(sum(inverse[a, d]*(partial(metric[d, nu], mu)+partial(metric[d, mu], nu)
                      -partial(metric[mu, nu], d))/2 for d in range(4)))
               for nu in range(4)] for mu in range(4)] for a in range(4)]
    Ricci = s.Matrix(4, 4, lambda mu, nu: s.simplify(sum(
        partial(Gamma[a][nu][mu], a)-partial(Gamma[a][a][mu], nu)
        +sum(Gamma[a][a][b]*Gamma[b][nu][mu]-Gamma[a][nu][b]*Gamma[b][a][mu] for b in range(4))
        for a in range(4))))
    checks["exact_FLRW_coordinate_Ricci_time"] = s.simplify(Ricci[0, 0]+3*(1+t*t)) == 0
    checks["exact_FLRW_coordinate_Ricci_space"] = all(
        s.simplify(Ricci[i, j]-(1+3*t*t)*metric[i, j]) == 0 for i, j in product(range(1, 4), repeat=2))
    checks["exact_FLRW_fails_Einstein_equation_for_every_Lambda"] = s.simplify(Ricci[0, 0]+Ricci[1, 1]/metric[1, 1]+2) == 0
    epsilon = s.Symbol("epsilon", real=True)
    dT = s.symbols("dT0:3", real=True)
    matrix = s.symbols("M0:9", real=True)
    dmatrix = s.symbols("dM0:9", real=True)
    volume, dvolume = s.symbols("volume dvolume", real=True)
    first_variation = s.diff((volume+epsilon*dvolume)*sum(
        (matrix[3*i+j]+epsilon*dmatrix[3*i+j])*(epsilon*dT[i])*(epsilon*dT[j])
        for i, j in product(range(3), repeat=2)), epsilon).subs(epsilon, 0)
    checks["zero_torsion_full_quadratic_first_variation_core"] = first_variation == 0
    return {name: bool(value) for name, value in checks.items()}


def _rotation_tensor(values):
    result = np.zeros((4, 4, 4))
    for mu in range(4):
        for k, (i, j) in enumerate(PAIRS):
            result[mu, i, j] = values[3*mu+k]
            result[mu, j, i] = -values[3*mu+k]
    return result


def _invariants(T):
    eta = np.asarray(ETA)
    lower = eta[:, None, None]*T
    upper = eta[:, None, None]*eta[None, :, None]*eta[None, None, :]*lower
    trace = np.einsum("nmn->m", T)
    return np.array([np.sum(lower*upper), np.sum(lower*upper.transpose(2, 1, 0)), np.sum(eta*trace*trace)])


def numerical_checks(samples=32, seed=20261029):
    rng = np.random.default_rng(seed)
    errors = dict(coframe=0., differentiated_coframe=0., metric_compatibility=0.,
                  stationary_density=0., frozen_density=0., independent_auxiliary_solution=0.,
                  auxiliary_stationarity=0.)
    minimum_curvature = float("inf")
    coefficients = [(-.25, -.5, 1.), (1., 2., 0.), (0., 0., 1.), (0., 0., 0.)]
    for sample in range(samples):
        rotation, _ = np.linalg.qr(rng.normal(size=(3, 3)))
        if np.linalg.det(rotation) < 0:
            rotation[:, 0] *= -1
        n = rotation[:, 2]
        plus = rotation@np.diag([1., -1., 0.])@rotation.T
        cross = rotation@np.array([[0., 1., 0.], [1., 0., 0.], [0., 0., 0.]])@rotation.T
        ut, vt, uz, vz = rng.normal(size=4)
        amplitude = rng.uniform(.15, .5)
        s0, radius, kappa = rng.uniform(.7, 1.7, size=3)
        m = s0/radius
        coframe = np.eye(4)
        carrier = np.array([radius, 0., 0., 0.])
        w = m*coframe[0]
        de = np.zeros((4, 4, 4))
        de[1:, 0, 1:] = amplitude*(ut*plus+vt*cross)/2
        for i in range(3):
            de[1:, i+1, 1:] = amplitude*n[i]*(uz*plus+vz*cross)/2
        Zstar = np.zeros((4, 4, 4))
        for mu, i, j in product(range(1, 4), repeat=3):
            Zstar[mu, i, j] = de[i, j, mu]-de[j, i, mu]
        zstar = np.array([Zstar[mu, i, j] for mu in range(4) for i, j in PAIRS])
        boost = np.zeros((4, 4, 4))
        dboost = np.zeros((4, 4, 4, 4))
        for mu, i in product(range(4), range(1, 4)):
            boost[mu, i, 0] = boost[mu, 0, i] = m*coframe[i, mu]
            for nu in range(4):
                dboost[nu, mu, i, 0] = dboost[nu, mu, 0, i] = m*de[i, nu, mu]
        conn = boost+_rotation_tensor(zstar)
        generated = ((conn@carrier).T+carrier[:, None]*w[None, :])/s0
        differentiated = np.einsum("nmab,b->anm", dboost, carrier)/s0
        errors["coframe"] = max(errors["coframe"], float(np.max(np.abs(generated-coframe))))
        errors["differentiated_coframe"] = max(errors["differentiated_coframe"], float(np.max(np.abs(differentiated-de))))
        eta = np.diag(ETA)
        errors["metric_compatibility"] = max(errors["metric_compatibility"], float(max(np.linalg.norm(eta@a+a.T@eta) for a in conn)))
        curvature = [dboost[mu, nu]-dboost[nu, mu]+conn[mu]@conn[nu]-conn[nu]@conn[mu]
                     for mu in range(4) for nu in range(mu+1, 4)]
        minimum_curvature = min(minimum_curvature, float(np.linalg.norm(curvature)))
        coeff = np.array(coefficients[sample] if sample < len(coefficients) else rng.normal(size=3))

        def density(values, derivatives=de):
            connection = boost+_rotation_tensor(values)
            T = derivatives-derivatives.transpose(0, 2, 1)
            for mu, nu in product(range(4), repeat=2):
                T[:, mu, nu] += connection[mu]@coframe[:, nu]-connection[nu]@coframe[:, mu]
            return float(coeff@_invariants(T)/(2*kappa))

        zero = np.zeros(12)
        base = density(zero, np.zeros_like(de))
        predicted = -(coeff[0]+coeff[1]/2)*(ut*ut+vt*vt)/(2*kappa)
        frozen = -(coeff[0]+coeff[1]/2)*(ut*ut+vt*vt-uz*uz-vz*vz)/(2*kappa)
        errors["stationary_density"] = max(errors["stationary_density"], abs((density(zstar)-base)/amplitude**2-predicted))
        errors["frozen_density"] = max(errors["frozen_density"], abs((density(zero)-base)/amplitude**2-frozen))
        # Independently solve the complete twelve-variable original quadratic
        # action, including singular Hessians, using unit evaluations only.
        origin = density(zero)
        basis = np.eye(12)
        positive = np.array([density(a) for a in basis])
        negative = np.array([density(-a) for a in basis])
        gradient = (positive-negative)/2
        H = np.diag(positive+negative-2*origin)
        for i in range(12):
            for j in range(i+1, 12):
                H[i, j] = H[j, i] = density(basis[i]+basis[j])-positive[i]-positive[j]+origin
        zsol = -np.linalg.pinv(H, rcond=1e-11)@gradient
        errors["auxiliary_stationarity"] = max(errors["auxiliary_stationarity"], float(np.linalg.norm(H@zsol+gradient)), float(np.linalg.norm(H@zstar+gradient)))
        errors["independent_auxiliary_solution"] = max(errors["independent_auxiliary_solution"], abs((density(zsol)-base)/amplitude**2-predicted))
    tolerance = 1e-9
    return {"samples": samples, "seed": seed, "maximum_errors": errors,
            "minimum_original_jet_curvature_norm": minimum_curvature, "tolerance": tolerance,
            "checks": {"all_original_jet_and_stationary_action_errors_below_tolerance": all(v < tolerance for v in errors.values()),
                       "every_original_jet_is_nonflat": minimum_curvature > 1e-6,
                       "random_wave_directions_and_both_polarizations": samples >= 16,
                       "degenerate_auxiliary_coefficients_included": samples >= 4}}


def run():
    exact = symbolic_checks()
    numerical = numerical_checks()
    return {"scope": "Principal TT block of a declared timelike isotropic free Lorentz-jet quadratic torsion family",
            "versions": {"sympy": s.__version__, "numpy": np.__version__},
            "symbolic": exact, "numerical": numerical,
            "passed": all(exact.values()) and all(numerical["checks"].values()),
            "not_proved": ["a full constrained mode count or stability theorem", "classification of all on-shell backgrounds", "a selected microscopic UBT action", "null, spacelike or anisotropic branches", "a no-go for flat-connection teleparallel gravity or other connection functionals"]}


if __name__ == "__main__":
    report = run()
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["passed"] else 1)
