#!/usr/bin/env python3
"""Palatini--Holst algebra and the EXISTING homogeneous composite comparator.

This does not select a microscopic UBT action, prove its PDE constraint algebra,
or predict measured departures from GR.  The independent-connection vacuum
comparison and the one-clock composite reduction are DIFFERENT variations.
"""
from __future__ import annotations

import json
import math
import itertools
from functools import lru_cache

import mpmath as mp
import numpy as np
import scipy
from scipy.integrate import solve_ivp
import sympy as s


def poisson(f, g, coordinates, momenta):
    return s.factor(sum(s.diff(f, q) * s.diff(g, p) -
                        s.diff(f, p) * s.diff(g, q)
                        for q, p in zip(coordinates, momenta)))


@lru_cache(maxsize=1)
def fourform_variation_checks():
    """Differentiate all tetrad components of the general polynomial 4-form.

    All 16 tetrad and 36 curvature coefficients are symbolic. Curvature is an
    independent 2-form here; integration by parts of D(delta omega), composite
    surjectivity, and analytic boundary conditions are not proved by this test.
    """
    def wedge(*forms):
        out = {(): s.Integer(1)}
        for form in forms:
            new = {}
            for I, x in out.items():
                for J, y in form.items():
                    if set(I) & set(J):
                        continue
                    key = tuple(sorted(I+J))
                    sign = (-1)**sum(i > j for i in I for j in J)
                    new[key] = new.get(key, 0)+sign*x*y
            out = new
        return out
    eta = (-1, 1, 1, 1)
    evars = s.symbols("e:16")
    e = [{(mu,): evars[4*a+mu] for mu in range(4)} for a in range(4)]
    curv = [[{} for _ in range(4)] for _ in range(4)]
    for a, b in itertools.combinations(range(4), 2):
        curv[a][b] = {pair: s.Symbol(f"R{a}{b}_{pair[0]}{pair[1]}") for pair in itertools.combinations(range(4), 2)}
        curv[b][a] = {pair: -value for pair, value in curv[a][b].items()}
    top = (0, 1, 2, 3)
    four = lambda *fs: wedge(*fs).get(top, 0)
    kappa, beta, lam = s.symbols("kappa beta lam", nonzero=True)
    permutations = list(itertools.permutations(range(4)))
    pal = sum(s.LeviCivita(a, b, c, d)*four(e[a], e[b], curv[c][d]) for a, b, c, d in permutations)
    hol = sum(eta[a]*eta[b]*four(e[a], e[b], curv[a][b]) for a in range(4) for b in range(4))
    action = pal/(4*kappa)+beta*hol/(2*kappa)-lam*four(*e)/kappa
    checks = {}
    for a in range(4):
        for mu in range(4):
            delta = {(mu,): s.Integer(1)}
            predicted = sum(s.LeviCivita(a, b, c, d)*four(delta, e[b], curv[c][d])
                            for b, c, d in itertools.permutations([i for i in range(4) if i != a]))/(2*kappa)
            predicted += beta*sum(eta[a]*eta[b]*four(delta, e[b], curv[a][b]) for b in range(4))/kappa
            predicted -= lam*sum(s.LeviCivita(a, b, c, d)*four(delta, e[b], e[c], e[d])
                                for b, c, d in itertools.permutations([i for i in range(4) if i != a]))/(6*kappa)
            checks[f"general_tetrad_Euler_fourform_{a}_{mu}"] = s.expand(s.diff(action, evars[4*a+mu])-predicted) == 0
    return checks


@lru_cache(maxsize=1)
def selfdual_checks():
    """Independently check the proposed canonical match AND its domain.

    k is an analytically continued squared coefficient. A correct complex
    polynomial continuation need not preserve the original Hermitian pair.
    """
    C, a, V, N, k = s.symbols("C a V N k", nonzero=True, real=True)
    p, pi, pV, PV, av, lam = s.symbols("p pi pV PV av Lambda", real=True)
    F = a+a**3/(3*V**2)-lam*a**3/3
    h = p**2/(4*C*k*a)+a*p/V-C*F
    f = -s.Rational(2, 3)*C*k*a**3/V
    oldp = pi+s.diff(f, a)
    oldpV = PV+s.diff(f, V)
    K = s.factor(h.subs(p, oldp)+s.diff(f, V))
    target = pi**2/(4*C*k*a)-C*a+C*lam*a**3/3-C*(1+k)*a**3/(3*V**2)
    Hgr = -pi**2/(4*C*a)-C*a+C*lam*a**3/3
    simple = lambda x: s.factor(x) == 0
    checks = {
        "time_dependent_generating_function": simple(K-target),
        "extended_constraint_momentum_shift": simple((pV+h).subs({p: oldp, pV: oldpV})-(PV+K)),
        "clock_independence_requires_k_minus_one": simple(s.diff(K, V)-2*C*(1+k)*a**3/(3*V**3)),
        "selfdual_GR_FLRW_canonical_match": simple(K.subs(k, -1)-Hgr),
        "transformed_clock_momentum_conserved": simple(s.diff(K.subs(k, -1), V)),
        "original_clock_momentum_not_generically_conserved": s.diff(h.subs(k, -1), V) != 0,
    }
    Lcontinued = C*N*(F-a*(a/V-av/N)**2)
    Lgr = C*(-a*av**2/N+N*a-lam*N*a**3/3)
    boundary = s.Rational(2, 3)*C*a**3/V
    checks["continued_Lagrangian_GR_clock_plus_boundary"] = simple(
        Lcontinued-Lgr-s.diff(boundary, a)*av-s.diff(boundary, V)*N)
    r, mass, volume, kap = s.symbols("r mass volume kappa", nonzero=True, real=True)
    checks["homogeneous_dust_integration_constant"] = simple(
        (mass+Hgr).subs(pi, -2*C*a*r).subs(C, 3*volume/kap) -
        (mass-3*volume*a**3/kap*(r**2/a**2+1/a**2-lam/3)))

    # Matrix/Hermitian check does NOT use the continued reduced action.
    B, defect, rotation = s.symbols("B defect rotation", real=True)
    pauli = [s.Matrix([[0, 1], [1, 0]]), s.Matrix([[0, -s.I], [s.I, 0]]), s.diag(1, -1)]
    e1, e2, e3 = [-s.I*m for m in pauli]
    checks["quaternion_unit_has_square_minus_one"] = e1*e1 == -s.eye(2)
    checks["quaternion_unit_is_not_commuting_scalar"] = (e1*e2-e2*e1 == 2*e3 and 2*e3 != s.zeros(2))
    for i, sigma in enumerate(pauli):
        omega = (B+s.I*rotation)*sigma/2
        checks[f"original_real_rotation_cancels_{i}"] = s.simplify(omega+omega.conjugate().T-B*sigma) == s.zeros(2)
        continued = omega.subs(rotation, -1+s.I*defect)
        pair = s.simplify(continued+continued.conjugate().T)
        checks[f"continued_pair_changes_boost_{i}"] = s.simplify(pair-(B-defect)*sigma) == s.zeros(2)
        generated = s.simplify(V*pair.subs({B: a/V, defect: a/V-r}))
        checks[f"continued_tetrad_readout_is_Vr_{i}"] = s.simplify(generated-V*r*sigma) == s.zeros(2)
    checks["selfdual_readout_counterexample"] = (V*r-a).subs({V: 2, a: 1, r: 0}) == -1
    epsilon = s.symbols("epsilon", nonzero=True, real=True)
    perturbation = epsilon*V**2
    checks["linearized_readout_counterexample"] = simple(
        V*s.diff(perturbation, V)-perturbation-epsilon*V**2)
    # At b=i the general six-dimensional connection operator is singular.
    J = s.BlockMatrix([[s.zeros(3), s.eye(3)], [-s.eye(3), s.zeros(3)]]).as_explicit()
    checks["selfdual_connection_operator_rank_three"] = (J+s.I*s.eye(6)).rank() == 3
    # Test the proposed invariant real subset, rather than rejecting complex
    # notation. With the ORIGINAL readout a=V*a', the ratio a/V is constant.
    A = s.Function("a")(V)
    checks["readout_implies_constant_scale_clock_ratio"] = simple(
        s.diff(A/V, V)-(V*s.diff(A, V)-A)/V**2)
    Lclock = C*(-A*s.diff(A, V)**2+A-lam*A**3/3)
    Eclock = s.diff(Lclock, A)-s.diff(s.diff(Lclock, s.diff(A, V)), V)
    checks["selfdual_clock_scale_Euler_equation"] = simple(
        Eclock/C-(s.diff(A, V)**2+2*A*s.diff(A, V, 2)+1-lam*A**2))
    slope = s.symbols("slope", real=True)
    residual = s.expand((Eclock/C).subs(A, slope*V).doit())
    checks["closed_real_readout_Euler_residual"] = simple(
        residual-(1+slope**2-lam*slope**2*V**2))
    checks["closed_real_readout_constant_coefficient"] = (
        s.Poly(residual, V).coeff_monomial(1) == 1+slope**2)
    # Reuse the REAL-coefficient trajectory already integrated independently
    # below. Its existence is different from self-dual GR matching.
    real_h = h.subs(k, 1)
    real_point = {C: 1, a: 1, V: 2, p: -1, lam: 0}
    checks["real_comparator_initial_scale_velocity"] = s.diff(real_h, p).subs(real_point) == 0
    checks["real_comparator_initial_clock_momentum"] = -real_h.subs(real_point) == s.Rational(4, 3)
    checks["real_comparator_initial_rotation"] = (-p/(2*C*a)).subs(real_point) == s.Rational(1, 2)
    return checks


@lru_cache(maxsize=1)
def symbolic_checks():
    C, b, a, V, N = s.symbols("C b a V N", nonzero=True, real=True)
    lam, av, w, pa, pV, pw = s.symbols("lam av w pa pV pw", real=True)
    F = a + a**3 / (3*V**2) - lam*a**3/3
    L = C*N*(F + b**2*a*(a/V-av/N)**2)
    p_a, p_V = s.diff(L, av), s.diff(L, N)
    H = a*pa/V + pa**2/(4*C*b**2*a) - C*F
    simple = lambda x: s.factor(x) == 0
    checks = {
        "momentum_a_from_differentiation": simple(p_a-2*C*b**2*a*(av/N-a/V)),
        "momentum_V_from_differentiation": simple(p_V-C*(F+b**2*a*((a/V)**2-(av/N)**2))),
        "canonical_energy_zero": simple(p_a*av+p_V*N-L),
        "primary_constraint_from_Legendre_map": simple(p_V+H.subs(pa, p_a)),
        "velocity_reconstruction": simple((a/V+pa/(2*C*b**2*a)).subs(pa, p_a)-av/N),
        "gauge_fixed_Legendre_transform": simple((pa*av-L.subs(N, 1)).subs(av, a/V+pa/(2*C*b**2*a))-H),
    }
    Hess = s.hessian(L, (av, N))
    expected_Hess = (2*C*b**2*a/N)*s.Matrix([[1, -av/N], [-av/N, (av/N)**2]])
    checks["rank_one_velocity_Hessian"] = (Hess-expected_Hess).applyfunc(s.factor) == s.zeros(2)
    checks["Hessian_clock_null_vector"] = (Hess*s.Matrix([av, N])).applyfunc(s.factor) == s.zeros(2, 1)

    # Start again with the first-order action BEFORE eliminating the rotation.
    Lfirst = C*(N*(F-a*w**2+2*b*a**2*w/V)-2*b*a*av*w)
    Bboundary = C*(a**3/(3*V)+b*a**2*w)
    wd = s.symbols("wd", real=True)
    original = C*(a*(N*((a/V)**2-(w-1)**2-2*(w-1))+
                         a*(av/V-a*N/V**2)) +
                  b*a*(2*N*(a/V)*w+a*wd)-lam*N*a**3/3)
    dBoundary = s.diff(Bboundary, a)*av+s.diff(Bboundary, V)*N+s.diff(Bboundary, w)*wd
    checks["original_curvature_action_boundary_identity"] = simple(original-Lfirst-dBoundary)
    wsol = b*(a/V-av/N)
    checks["algebraic_rotation_Euler_equation"] = simple(s.diff(Lfirst, w)+2*C*N*a*(w-wsol))
    checks["rotation_elimination_before_Legendre"] = simple(Lfirst.subs(w, wsol)-L)
    chi = s.Matrix([pa+2*C*b*a*w, pV-C*(F-a*w**2+2*b*a**2*w/V), pw])
    qs, ps = (a, V, w), (pa, pV, pw)
    bracket = s.Matrix(3, 3, lambda i, j: poisson(chi[i], chi[j], qs, ps))
    x = C*(s.diff(F, a)-w**2+4*b*a*w/V)
    y = 2*C*b*a
    z = 2*C*a*(w-b*a/V)
    expected = s.Matrix([[0, x, y], [-x, 0, z], [-y, -z, 0]])
    checks["all_primary_Poisson_brackets"] = (bracket-expected).applyfunc(s.factor) == s.zeros(3)
    checks["rank_two_primary_bracket_minor"] = simple(bracket.extract([0, 2], [0, 2]).det()-y**2)
    checks["primary_matrix_null_direction"] = (bracket*s.Matrix([z, -y, x])).applyfunc(s.factor) == s.zeros(3, 1)
    checks["first_order_constraint_reduces_to_phi"] = simple(chi[1].subs(w, -pa/(2*C*b*a))-(pV+H))

    # Dirac bracket for chi_a and chi_w, without assuming a canonical result.
    second = (chi[0], chi[2])
    second_inv = s.Matrix([[poisson(f, g, qs, ps) for g in second] for f in second]).inv()
    def dirac(f, g):
        left = s.Matrix([[poisson(f, c, qs, ps) for c in second]])
        right = s.Matrix([poisson(c, g, qs, ps) for c in second])
        return s.factor(poisson(f, g, qs, ps)-(left*second_inv*right)[0])
    retained = (a, V, pa, pV)
    Db = s.Matrix(4, 4, lambda i, j: dirac(retained[i], retained[j]))
    canonical = s.Matrix([[0, 0, 1, 0], [0, 0, 0, 1], [-1, 0, 0, 0], [0, -1, 0, 0]])
    checks["all_reduced_Dirac_brackets_canonical"] = Db == canonical
    checks["no_secondary_constraint_for_nonzero_b"] = dirac(pV+H, pV+H) == 0
    checks["Hamilton_equation_a"] = simple(s.diff(H, pa)-(a/V+pa/(2*C*b**2*a)))
    checks["Hamilton_equation_p"] = simple(-s.diff(H, a)-(-pa/V+pa**2/(4*C*b**2*a**2)+C*s.diff(F, a)))
    checks["energy_completed_square"] = simple(H-((pa+2*C*b**2*a**2/V)**2/(4*C*b**2*a)-C*(F+b**2*a**3/V**2)))
    checks["energy_minimum_over_momentum"] = simple(H.subs(pa, -2*C*b**2*a**2/V)-C*(-a+(lam-(1+3*b**2)/V**2)*a**3/3))

    # b=0 must be derived separately, never obtained by dividing its constraint.
    Fa = s.diff(F, a)
    checks["zero_b_has_zero_velocity_Hessian"] = s.hessian(C*N*F, (av, N)) == s.zeros(2)
    checks["zero_b_nonzero_secondary_minor"] = simple(s.diff(Fa, a).subs(lam, 1/a**2+1/V**2)+2/a)
    branch = V/s.sqrt(lam*V**2-1)
    checks["zero_b_stationary_branch"] = simple(Fa.subs(a, branch))
    lapse_residual = s.diff(branch, V)**2+1-lam*branch**2/3
    checks["zero_b_Einstein_normal_counterexample"] = s.simplify(lapse_residual.subs({lam: 1, V: 2})) == s.Rational(16, 27)

    # Lorentz bivector Hodge operator, all real b, independent of FLRW.
    I = s.eye(3)
    J = s.BlockMatrix([[s.zeros(3), I], [-I, s.zeros(3)]]).as_explicit()
    P = J+b*s.eye(6)
    checks["Lorentz_Hodge_square_minus_identity"] = J*J == -s.eye(6)
    checks["real_Holst_inverse"] = (P*(b*s.eye(6)-J)-(1+b**2)*s.eye(6)) == s.zeros(6)
    checks["real_Holst_determinant"] = s.factor(P.det()) == (1+b**2)**3
    checks["distinct_off_shell_operators"] = (J*s.ones(6, 1)) != ((J+s.eye(6))*s.ones(6, 1))
    return checks


def numerical_checks():
    rng = np.random.default_rng(20261028)
    errors = []
    covariance = []
    for _ in range(64):
        C, a, V, N = rng.uniform(.5, 2, 4)
        b = rng.choice([-1, 1])*rng.uniform(.25, 2)
        av, lam = rng.uniform(-1, 1, 2)
        def lag(u, n):
            return C*n*(a+a**3/(3*V**2)-lam*a**3/3+b*b*a*(a/V-u/n)**2)
        exact = np.array([2*C*b*b*a*(av/N-a/V),
                          C*(a+a**3/(3*V**2)-lam*a**3/3+b*b*a*((a/V)**2-(av/N)**2))])
        row = []
        for h in (1e-3, 1e-4, 1e-5):
            fd = np.array([(lag(av+h, N)-lag(av-h, N))/(2*h),
                           (lag(av, N+h)-lag(av, N-h))/(2*h)])
            row.append(float(np.max(np.abs(fd-exact)/(1+np.abs(exact)))))
        errors.append(row)
        # Independent upper-index antisymmetric-tensor implementation of dual.
        rapidity = rng.uniform(-2, 2)
        ch, sh = math.cosh(rapidity), math.sinh(rapidity)
        boost = np.array([[ch, sh, 0, 0], [sh, ch, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        rotation = np.eye(4)
        angle = rng.uniform(-math.pi, math.pi)
        rotation[2:4, 2:4] = [[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]]
        lorentz = rotation @ boost
        def unpack(v):
            M = np.zeros((4, 4))
            for val, (i, j) in zip(v, ((0, 1), (0, 2), (0, 3), (2, 3), (3, 1), (1, 2))):
                M[i, j], M[j, i] = val, -val
            return M
        def pack(M):
            return np.array([M[0, 1], M[0, 2], M[0, 3], M[2, 3], M[3, 1], M[1, 2]])
        def dual(v):
            return np.concatenate((v[3:], -v[:3]))
        vec = rng.normal(size=6)
        transported = pack(lorentz @ unpack(vec) @ lorentz.T)
        covariance.append(float(np.max(np.abs(dual(transported)-pack(lorentz @ unpack(dual(vec)) @ lorentz.T)))))

    # Independent integrators, on a regular patch. This is a model trajectory,
    # not cosmological data and not a solution of the unrestricted UBT PDE.
    def rhs(V, y):
        a, p = y
        return np.array([a/V+p/(2*a), -p/V+p*p/(4*a*a)+1+a*a/(V*V)])
    start, stop = 2., 2.2
    reference = solve_ivp(rhs, (start, stop), [1., -1.], method="DOP853", rtol=1e-12, atol=1e-13)
    assert reference.success, reference.message
    integration_errors = []
    for steps in (10, 20, 40):
        h = (stop-start)/steps
        y = np.array([1., -1.])
        for i in range(steps):
            t = start+i*h
            k1 = rhs(t, y)
            k2 = rhs(t+h/2, y+h*k1/2)
            k3 = rhs(t+h/2, y+h*k2/2)
            k4 = rhs(t+h, y+h*k3)
            y += h*(k1+2*k2+2*k3+k4)/6
        integration_errors.append(float(np.max(np.abs(y-reference.y[:, -1]))))
    # Precision cross-check without SymPy or NumPy arithmetic.
    with mp.workdps(80):
        C, b, a, V, av, N, lam = [mp.mpf(n)/d for n, d in ((7, 5), (2, 3), (11, 7), (13, 9), (-5, 8), (17, 10), (3, 11))]
        F = a+a**3/(3*V**2)-lam*a**3/3
        L = C*N*(F+b*b*a*(a/V-av/N)**2)
        pa = 2*C*b*b*a*(av/N-a/V)
        pV = C*(F+b*b*a*((a/V)**2-(av/N)**2))
        constraint_residual = abs(pV+a*pa/V+pa*pa/(4*C*b*b*a)-C*F)
        energy_residual = abs(pa*av+pV*N-L)
        precision_residual = float(max(constraint_residual, energy_residual))
    max_fd = np.max(np.array(errors), axis=0).tolist()
    return {
        "seed": 20261028, "samples": 64,
        "finite_difference_steps": [1e-3, 1e-4, 1e-5],
        "max_scaled_momentum_errors": max_fd,
        "max_Lorentz_dual_covariance_error": max(covariance),
        "RK4_errors_against_DOP853": integration_errors,
        "arbitrary_precision_decimal_digits": 80,
        "arbitrary_precision_residual": precision_residual,
        "checks": {
            "finite_difference_variations": max_fd[-1] < 1e-8,
            "finite_difference_convergence": max_fd[-1] < max_fd[0]/100,
            "Lorentz_covariance": max(covariance) < 1e-12,
            "independent_integrator_convergence": integration_errors[0] > 8*integration_errors[1] > 64*integration_errors[2],
            "independent_integrator_accuracy": integration_errors[-1] < 1e-9,
            "precision_check": precision_residual < 1e-65,
        },
    }


def verify():
    exact = dict(symbolic_checks(), **fourform_variation_checks(), **selfdual_checks())
    numeric = numerical_checks()
    return {
        "scope": "real bivector algebra and specified one-clock homogeneous comparator only",
        "versions": {"sympy": s.__version__, "numpy": np.__version__, "scipy": scipy.__version__, "mpmath": mp.__version__},
        "symbolic": exact, "numerical": numeric,
        "passed": all(exact.values()) and all(numeric["checks"].values()),
        "not_proved": ["microscopic action selection", "unrestricted composite field equations", "full field-theoretic constraint algebra", "ghost freedom", "beyond-GR prediction"],
    }


if __name__ == "__main__":
    result = verify()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["passed"] else 1)
