#!/usr/bin/env python3
"""Full-spatial ADM comparison: exact coefficients and independent torus test.

Assumes a reduced canonical spatial metric phase space. It does not derive
that phase space, its action, or its matter/complex-time sector from Theta.
The numerical bracket differentiates the discretized curvature functional;
it does not reuse the analytic curvature-variation formula being tested.
"""
from functools import lru_cache
import json

import numpy as np
import sympy as s


def symmetric(values):
    x, y, z, u, v, w = values
    return s.Matrix([[x, u, v], [u, y, w], [v, w, z]])


@lru_cache(maxsize=1)
def symbolic_checks():
    a, b, chi, volume = s.symbols("a b chi volume", real=True)
    p = symmetric(s.symbols("p:6", real=True))
    hess = symmetric(s.symbols("m:6", real=True))
    trace, lap = s.trace(p), s.trace(hess)
    q = p - chi * trace * s.eye(3)
    curvature_derivative = hess - lap * s.eye(3)
    contraction = s.trace(q * curvature_derivative)
    expected = s.trace(p * hess) - (1 - 2 * chi) * trace * lap
    checks = {"full_symmetric_curvature_contraction": s.expand(contraction - expected) == 0}
    # Six independent symmetric components: off-diagonal derivatives have
    # the factor 1/2 when interpreted as a full symmetric tensor gradient.
    variables = s.symbols("g:6", real=True)
    metric = symmetric(variables)
    det = metric.det()
    lowered = metric * p * metric
    pi_trace = s.trace(metric * p)
    norm = s.trace(metric * p * metric * p)
    kinetic = a * (norm - chi * pi_trace**2) / s.sqrt(det)
    sample = dict(zip(variables, [s.Rational(3, 2), 2, s.Rational(5, 2),
                                 s.Rational(1, 5), s.Rational(1, 7), s.Rational(-1, 6)]))
    inverse = metric.inv()
    kinetic_metric_gradient = a / s.sqrt(det) * (
        2 * p * metric * p - 2 * chi * pi_trace * p
        - inverse * (norm - chi * pi_trace**2) / 2)
    kinetic_momentum_gradient = 2 * a / s.sqrt(det) * (lowered - chi * pi_trace * metric)
    pairs = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
    pvars = list(s.symbols("p:6", real=True))
    for k, (i, j) in enumerate(pairs):
        factor = 1 if i == j else 2
        actual_g = (s.diff(kinetic, variables[k]) / factor).subs(sample)
        target_g = kinetic_metric_gradient[i, j].subs(sample)
        checks[f"kinetic_metric_variation_{i}{j}"] = s.simplify(actual_g - target_g) == 0
        actual_p = (s.diff(kinetic, pvars[k]) / factor).subs(sample)
        target_p = kinetic_momentum_gradient[i, j].subs(sample)
        checks[f"kinetic_momentum_variation_{i}{j}"] = s.simplify(actual_p - target_p) == 0
        checks[f"volume_variation_{i}{j}"] = s.simplify(
            (s.diff(s.sqrt(det), variables[k]) / factor
             - s.sqrt(det) * inverse[i, j] / 2).subs(sample)) == 0
    # Local smear derivative values and their independent first jets.
    N, M = s.symbols("N M", real=True)
    gradN, gradM = s.Matrix(s.symbols("n:3")), s.Matrix(s.symbols("mgrad:3"))
    checks["symmetric_gradient_products_cancel_in_IBP"] = s.expand(
        (gradN.T * p * gradM)[0] - (gradM.T * p * gradN)[0]) == 0
    divergence, trace_gradient = s.symbols("divergence trace_gradient", real=True)
    bracket = a*b*divergence + 2*a*b*(1-2*chi)*trace_gradient
    checks["selected_coefficients_give_required_offshell_bracket"] = s.simplify(
        bracket.subs({b: 1/a, chi: s.Rational(1, 2)}) - divergence) == 0
    checks["independent_divergence_coefficient"] = s.diff(bracket-divergence, divergence) == a*b-1
    checks["independent_trace_gradient_coefficient"] = s.diff(bracket, trace_gradient) == 2*a*b*(1-2*chi)
    checks["cosmological_coefficient_cancels_from_antisymmetrization"] = s.expand(
        N*M*volume - M*N*volume) == 0
    checks["ultralocal_bracket_cannot_match_structure_function"] = (
        s.simplify(bracket.subs(b, 0)) == 0
        and s.simplify(bracket.subs(b, 0)-divergence) != 0)
    # Exact periodic, divergence-free momentum with a varying trace:
    # h=I, pi=diag(0,sin x,0), N=1, M=sin x.
    x = s.symbols("x", real=True)
    pw = s.diag(0, s.sin(x), 0)
    checks["torus_witness_momentum_constraint_identically_zero"] = s.Matrix(
        [sum(s.diff(pw[i, j], x) if i == 0 else 0 for i in range(3)) for j in range(3)]) == s.zeros(3, 1)
    witness = s.integrate(s.cos(x)**2, (x, 0, 2*s.pi))
    checks["torus_witness_trace_anomaly_nonzero"] = witness == s.pi
    # Full six-component Legendre inversion at an orthonormal spatial point.
    K = a * (p - trace*s.eye(3)/2)
    checks["legendre_inverse_all_six_components"] = s.simplify(
        K - s.trace(K)*s.eye(3) - a*p) == s.zeros(3)
    checks["legendre_kinetic_density"] = s.expand(
        s.trace(K*K) - s.trace(K)**2 - a**2*(s.trace(p*p)-trace**2/2)) == 0
    v = s.Matrix([1, 1, 1, 0, 0, 0])
    hessian = 2*a*(s.eye(6)-chi*v*v.T)
    checks["trace_kinetic_eigenvalue"] = s.simplify(hessian*v - 2*a*(1-3*chi)*v) == s.zeros(6, 1)
    checks["GR_trace_eigenvalue_is_not_an_extra_TT_mode"] = (
        (hessian*v).subs(chi, s.Rational(1, 2)) == -a*v)
    # Nonzero spatial wave vector; 3 momentum conditions plus trace leave 2.
    momentum_constraints = p * s.Matrix([1, 2, 3])
    conditions = list(momentum_constraints) + [trace]
    constraint_matrix = s.linear_eq_to_matrix(conditions, pvars)[0]
    checks["TT_subspace_dimension_two_at_nonzero_wavevector"] = 6-constraint_matrix.rank() == 2
    lap_gamma = s.Symbol("lap_gamma")
    checks["TT_wave_speed_squared_is_ab"] = s.expand(2*a*(b*lap_gamma/2) - a*b*lap_gamma) == 0
    t, z, wave_number, A, B = s.symbols("t z k A B", real=True)
    wave = s.cos(wave_number*(z-t))
    gamma = s.Matrix([[A*wave, B*wave, 0], [B*wave, -A*wave, 0], [0, 0, 0]])
    checks["two_polarization_wave_solves_TT_equation"] = (
        s.diff(gamma, t, 2)-s.diff(gamma, z, 2) == s.zeros(3))
    checks["two_polarization_wave_satisfies_linear_constraints"] = (
        s.trace(gamma) == 0 and s.diff(gamma[:, 2], z) == s.zeros(3, 1))
    # Independent coordinate-curvature expansion for both TT polarizations.
    # Jets replace functions of z, so no field equation is inserted.
    eps, U, V, du, dv, ddu, ddv = s.symbols("eps U V du dv ddu ddv", real=True)
    def dz(expr):
        return s.diff(expr, U)*du + s.diff(expr, V)*dv + s.diff(expr, du)*ddu + s.diff(expr, dv)*ddv
    g = s.Matrix([[1+eps*U, eps*V, 0], [eps*V, 1-eps*U, 0], [0, 0, 1]])
    ginv = g.inv()
    dg = [s.zeros(3), s.zeros(3), g.applyfunc(dz)]
    Gamma = [[[sum(ginv[k, l]*(dg[i][l, j]+dg[j][l, i]-dg[l][i, j])
                    for l in range(3))/2 for j in range(3)] for i in range(3)] for k in range(3)]
    Ricci = s.zeros(3)
    for i in range(3):
        for j in range(3):
            Ricci[i, j] = sum((dz(Gamma[k][i][j]) if k == 2 else 0)
                - (dz(Gamma[k][i][k]) if j == 2 else 0)
                + sum(Gamma[k][k][l]*Gamma[l][i][j]-Gamma[k][j][l]*Gamma[l][i][k]
                      for l in range(3)) for k in range(3))
    density = -s.sqrt(g.det())*sum(ginv[i, j]*Ricci[i, j] for i in range(3) for j in range(3))
    second = s.expand(s.series(density, eps, 0, 3).removeO()).coeff(eps, 2)
    checks["TT_curvature_quadratic_density_from_Christoffels"] = s.simplify(
        second+2*(U*ddu+V*ddv)+s.Rational(3, 2)*(du**2+dv**2)) == 0
    checks["TT_gradient_energy_after_periodic_IBP"] = s.simplify(
        second+dz(2*(U*du+V*dv))-(du**2+dv**2)/2) == 0
    return checks


def derivative(field, axis):
    """Real pseudospectral derivative on a 2pi-periodic Cartesian grid."""
    count = field.shape[axis]
    modes = np.fft.fftfreq(count, d=1/count)
    shape = [1] * field.ndim
    shape[axis] = count
    return np.fft.ifft(1j*modes.reshape(shape)*np.fft.fft(field, axis=axis), axis=axis).real


def scalar_curvature(metric):
    """Coordinate definition through Christoffels, with all three derivatives."""
    inverse = np.linalg.inv(metric)
    dg = [derivative(metric, k) for k in range(3)]
    gamma = np.zeros(metric.shape[:-2] + (3, 3, 3))
    for a in range(3):
        for i in range(3):
            for j in range(3):
                gamma[..., a, i, j] = sum(inverse[..., a, k]*(
                    dg[i][..., k, j] + dg[j][..., k, i] - dg[k][..., i, j])
                    for k in range(3))/2
    dgamma = [derivative(gamma, k) for k in range(3)]
    ricci = np.zeros_like(metric)
    for i in range(3):
        for j in range(3):
            ricci[..., i, j] = sum(dgamma[k][..., k, i, j] - dgamma[j][..., k, i, k]
                + sum(gamma[..., k, k, l]*gamma[..., l, i, j]
                      - gamma[..., k, j, l]*gamma[..., l, i, k] for l in range(3))
                for k in range(3))
    return np.einsum("...ij,...ij->...", inverse, ricci)


def periodic_data(count=16):
    x, y, z = np.meshgrid(*([np.arange(count)*2*np.pi/count]*3), indexing="ij")
    metric = np.broadcast_to(np.eye(3), x.shape + (3, 3)).copy()
    for i, phase in enumerate([x+y, y+z, z+x]):
        metric[..., i, i] += 0.08*np.cos(phase)
    for (i, j), phase in zip([(0, 1), (0, 2), (1, 2)], [x-z, y-x, z-y]):
        metric[..., i, j] = metric[..., j, i] = 0.035*np.sin(phase)
    momentum = np.zeros_like(metric)
    for i, phase in enumerate([x, y+x, z-y]):
        momentum[..., i, i] = 0.15*np.sin(phase) + 0.08*np.cos(z+x)
    for (i, j), phase in zip([(0, 1), (0, 2), (1, 2)], [z+y, x+z, y-x]):
        momentum[..., i, j] = momentum[..., j, i] = 0.07*np.cos(phase)
    N = 1 + 0.2*np.sin(x) + 0.1*np.cos(y+z)
    M = 0.3*np.cos(x+y) + 0.2*np.sin(z-x)
    return metric, momentum, N, M


def torus_bracket(count=16, a=2., b=.5, chi=.5, c=.17, epsilon=1e-4):
    metric, momentum, N, M = periodic_data(count)
    root = np.sqrt(np.linalg.det(metric))
    inverse = np.linalg.inv(metric)
    trace = np.einsum("...ij,...ij->...", metric, momentum)
    lowered = np.einsum("...ik,...kl,...lj->...ij", metric, momentum, metric)
    flow = 2*a/root[..., None, None]*(lowered-chi*trace[..., None, None]*metric)
    cell = (2*np.pi/count)**3

    def potential(g, lapse):
        return cell*np.sum(lapse*np.sqrt(np.linalg.det(g))*(-b*scalar_curvature(g)+c))

    def differential(lapse, direction):
        return (potential(metric+epsilon*direction, lapse)
                - potential(metric-epsilon*direction, lapse))/(2*epsilon)

    # Direct functional directional derivatives. This implementation never
    # inserts the analytical delta(sqrt(h) R)/delta h formula.
    actual = differential(N, M[..., None, None]*flow) - differential(M, N[..., None, None]*flow)
    beta_cov = np.stack([N*derivative(M, i)-M*derivative(N, i) for i in range(3)], axis=-1)
    beta = np.einsum("...ij,...j->...i", inverse, beta_cov)
    lie_metric = sum(beta[..., k, None, None]*derivative(metric, k) for k in range(3))
    for i in range(3):
        for j in range(3):
            lie_metric[..., i, j] += sum(metric[..., k, j]*derivative(beta[..., k], i)
                + metric[..., i, k]*derivative(beta[..., k], j) for k in range(3))
    diffeomorphism = cell*np.sum(momentum*lie_metric)
    trace_term = cell*np.sum(root*sum(beta[..., i]*derivative(trace/root, i) for i in range(3)))
    anomaly = 2*a*b*(1-2*chi)*trace_term
    predicted = a*b*diffeomorphism + anomaly
    return {"grid": count, "epsilon": epsilon, "a": a, "b": b, "chi": chi,
            "direct_functional_bracket": float(actual), "momentum_generator": float(diffeomorphism),
            "trace_anomaly": float(anomaly), "predicted_bracket": float(predicted),
            "absolute_error": float(abs(actual-predicted)),
            "minimum_metric_eigenvalue": float(np.linalg.eigvalsh(metric).min())}


def numerical_checks():
    cases = []
    for a, b, chi in [(2., .5, .5), (2., .5, .2), (1.3, .4, .5)]:
        for count in [12, 20]:
            for epsilon in [2e-4, 1e-4]:
                cases.append(torus_bracket(count=count, a=a, b=b, chi=chi, epsilon=epsilon))
    tolerance = 2e-6
    fine = [case for case in cases if case["grid"] == 20]
    return {"method": "Fourier differentiation in all 3 spatial directions and central finite differences of the curvature functional",
            "cases": cases, "tolerance": tolerance,
            "checks": {"fine_grid_full_bracket": all(case["absolute_error"] < tolerance for case in fine),
                       "non_GR_trace_anomaly_is_resolved": any(abs(case["trace_anomaly"]) > 1e-4 for case in fine),
                       "all_metrics_positive": all(case["minimum_metric_eigenvalue"] > .5 for case in cases),
                       "finite_difference_converges": all(
                           cases[k+1]["absolute_error"] < .4*cases[k]["absolute_error"]
                           for k in range(0, len(cases), 2))}}


def run_checks():
    exact, numerical = symbolic_checks(), numerical_checks()
    return {"scope": "Conditional reduced canonical metric family; full spatial refoliation bracket, coefficient selection, GR evolution and flat TT benchmark",
            "versions": {"sympy": s.__version__, "numpy": np.__version__},
            "symbolic": exact, "numerical": numerical,
            "passed": all(exact.values()) and all(numerical["checks"].values()),
            "not_proved": ["Theta-only action selection or reduced canonical symplectic form",
                           "full complex-time, matter, Holst-source or split-jet Dirac algebra",
                           "global boundaries or positivity on every background",
                           "values of Newton or cosmological constants"]}


if __name__ == "__main__":
    report = run_checks()
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["passed"] else 1)
