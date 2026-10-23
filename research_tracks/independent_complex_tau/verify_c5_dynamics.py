#!/usr/bin/env python3
"""Exact checks for the explicitly conditional C5 dynamics study.

These are mathematical checks, not a validation of a complete UBT action.
The general flatness and variational proofs are given in the companion note.
Requires SymPy. Run with Python; results are written beside this script.
"""
import json
import platform
from pathlib import Path
import sympy as s

checks = []
details = {}


def zero(name, expr):
    values = list(expr) if isinstance(expr, (list, tuple, s.MatrixBase)) else [expr]
    residuals = [s.simplify(s.expand(v)) for v in values]
    passed = all(v == 0 for v in residuals)
    checks.append({"name": name, "passed": passed, "components": len(values)})
    if not passed:
        raise AssertionError((name, [v for v in residuals if v != 0][:3]))


def geometry(metric, coords):
    """Christoffel, full Riemann and Ricci calculated from the metric."""
    n = len(coords)
    inverse = metric.inv().applyfunc(s.simplify)
    conn = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                val = s.simplify(sum(inverse[a, d] * (
                    s.diff(metric[d, c], coords[b])
                    + s.diff(metric[d, b], coords[c])
                    - s.diff(metric[b, c], coords[d])) for d in range(n)) / 2)
                if val != 0:
                    conn[a, b, c] = val

    def C(a, b, c):
        return conn.get((a, b, c), s.S.Zero)

    riem = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    val = s.simplify(s.diff(C(a, d, b), coords[c])
                                     - s.diff(C(a, c, b), coords[d])
                                     + sum(C(a, c, e)*C(e, d, b)
                                           - C(a, d, e)*C(e, c, b) for e in range(n)))
                    if val != 0:
                        riem[a, b, c, d] = val
    ric = s.Matrix(n, n, lambda b, d: s.simplify(sum(
        riem.get((a, b, a, d), s.S.Zero) for a in range(n))))
    scalar = s.simplify(sum(inverse[b, d]*ric[b, d] for b in range(n) for d in range(n)))
    einstein = (ric - scalar*metric/2).applyfunc(s.simplify)
    return inverse, conn, riem, einstein


# A genuinely nonlinear, tau-dependent coordinate map with exact coframe.
t, x, y, z, tau = s.symbols('t x y z tau', real=True)
coords5 = [t, x, y, z, tau]
Y = s.Matrix([t, s.exp(t)*x + tau**2, y, z, tau])
J = Y.jacobian(coords5)
eta5 = s.diag(-1, 1, 1, 1, 1)
eta4 = s.diag(-1, 1, 1, 1)
g5 = (J.T*eta5*J).applyfunc(s.simplify)
g0 = J[:4, :].T*eta4*J[:4, :]
inverse5, conn5, riem5, _ = geometry(g5, coords5)
zero('nonlinear_map_jacobian', J.det() - s.exp(t))
zero('nonlinear_completed_metric_determinant', g5.det() + s.exp(2*t))
zero('nonlinear_completed_metric_full_Riemann_zero',
     [riem5.get((a, b, c, d), 0) for a in range(5) for b in range(5)
      for c in range(5) for d in range(5)])
zero('partial_kinetic_trace_is_four', s.trace(inverse5*g0) - 4)
u = s.Matrix([0, 0, 0, 0, 1])
zero('added_one_form_unit_norm', (u.T*inverse5*u)[0] - 1)
details['nonlinear_example'] = {'Y': [str(v) for v in Y],
                                'nonzero_connection_components': len(conn5),
                                'nonzero_Riemann_components': len(riem5)}

# General four functions of five variables: a Piola identity and null action.
# tau is fixed as fifth coordinate. Potential is nonconstant; the note proves
# the statement for every smooth F(Theta,tau), without explicit x dependence.
theta = [s.Function('theta'+str(i))(*coords5) for i in range(4)]
M = s.Matrix(theta).jacobian(coords5[:4])
detM = M.det(method='domain-ge')
cof = M.cofactor_matrix()
for a in range(4):
    zero('Piola_identity_'+str(a), sum(s.diff(cof[a, mu], coords5[mu]) for mu in range(4)))
zero('cofactor_chain_rule_identity', M*cof.T - detM*s.eye(4))
q = s.symbols('q0:4')
Fq = 2 - q[0]**2 - q[1]*q[2] - s.exp(q[3])
replace_q = dict(zip(q, theta))
F = Fq.subs(replace_q)
for a in range(4):
    euler = s.diff(Fq, q[a]).subs(replace_q)*detM - sum(
        s.diff(F*cof[a, mu], coords5[mu]) for mu in range(4))
    zero('composite_metric_action_Euler_Lagrange_'+str(a), euler)

# FLRW embedding: first and second fundamental forms, then Gauss identity.
coords4 = [t, x, y, z]
a = s.Function('a')(t)
Femb = s.Function('Femb')(t)
ad = s.diff(a, t)
add = s.diff(a, t, 2)
r2 = x*x + y*y + z*z
Yemb = s.Matrix([a, a*r2 + Femb, a*x, a*y, a*z])
ambient = s.zeros(5)
ambient[0, 1] = ambient[1, 0] = -s.Rational(1, 2)
for i in range(2, 5):
    ambient[i, i] = 1
tangents = Yemb.jacobian(coords4)
subs_F = {s.diff(Femb, t, 2): -add/ad**2, s.diff(Femb, t): 1/ad}
g4 = s.diag(-1, a*a, a*a, a*a)
zero('FLRW_induced_metric', (tangents.T*ambient*tangents).subs(subs_F) - g4)
normal = s.Matrix([ad, ad*r2 - 1/ad, ad*x, ad*y, ad*z])
zero('FLRW_unit_spacelike_normal', (normal.T*ambient*normal)[0] - 1)
zero('FLRW_normal_orthogonality', (normal.T*ambient*tangents).subs(subs_F))
K = s.Matrix(4, 4, lambda mu, nu: s.simplify((normal.T*ambient*
    Yemb.diff(coords4[mu]).diff(coords4[nu]))[0].subs(subs_F)))
zero('FLRW_second_fundamental_form', K - s.diag(add/ad, -a*ad, -a*ad, -a*ad))
inv4, _, riem4, ein4 = geometry(g4, coords4)
gauss_residuals = []
for mu in range(4):
    for nu in range(4):
        for rho in range(4):
            for sig in range(4):
                lowered = sum(g4[mu, b]*riem4.get((b, nu, rho, sig), 0) for b in range(4))
                gauss_residuals.append(lowered - K[mu, rho]*K[nu, sig] + K[mu, sig]*K[nu, rho])
zero('FLRW_Gauss_equation_all_components', gauss_residuals)

# RT normal equation, residual continuity, and the conserved FLRW charge.
rho = s.Function('rho')(t)
p = s.Function('p')(t)
kappa = s.symbols('kappa', positive=True)
H = ad/a
drho = s.simplify(ein4[0, 0]/kappa - rho)
dp = s.simplify(ein4[1, 1]/(kappa*a*a) - p)
zero('residual_conservation_from_Bianchi', s.diff(drho, t) + 3*H*(drho + dp)
     + s.diff(rho, t) + 3*H*(rho + p))
Eup = inv4*(ein4 - kappa*s.diag(rho, p*a*a, p*a*a, p*a*a))*inv4
rt = s.simplify(sum(Eup[i, j]*K[i, j] for i in range(4) for j in range(4))/kappa)
zero('RT_normal_equation', rt - (drho*add/ad - 3*H*dp))
charge = a**3*ad*drho
matter_continuity = {s.diff(rho, t): -3*H*(rho+p)}
zero('RT_first_integral_equivalence', (s.diff(charge, t) - a**3*ad*rt).subs(matter_continuity))
details['FLRW_normal_form'] = {'K00':str(K[0, 0]), 'Kij_coefficient':str(K[1, 1])}
details['conditional_cosmology'] = {
    'assumptions': '4D Einstein-Hilbert plus covariant matter, varied through a 5D embedding; k=0; a>0; a_dot!=0; conserved matter',
    'charge': 'C = a^4 H rho_X',
    'Friedmann': '3 H^2 = kappa (rho + rho_X)',
    'unsquared_cubic': '3 H^3 - kappa rho H - kappa C/a^4 = 0',
    'squared_density_relation': 'rho_X^2 (rho + rho_X) = 3 C^2/(kappa a^8)',
    'branch_warning': 'The squared density equation must retain the sign of rho_X H = C/a^4.',
}

# Exact non-Einstein vacuum solution: not just counting of equations.
apow = t**s.Rational(3, 4)
subs_vac = {s.diff(a, t, 2):s.diff(apow, t, 2), s.diff(a, t):s.diff(apow, t), a:apow, rho:0, p:0}
zero('vacuum_power_law_solves_RT', rt.subs(subs_vac))
zero('vacuum_power_law_nonzero_Einstein_00', ein4[0, 0].subs(subs_vac) - s.Rational(27, 16)/t**2)
zero('vacuum_power_law_nonzero_charge', charge.subs(subs_vac) - s.Rational(81, 64)/kappa)
zero('vacuum_power_law_effective_equation_of_state', (dp/drho).subs(subs_vac) + s.Rational(1, 9))

# Linearized correction when a conserved constant-w fluid dominates GR.
w = s.symbols('w', real=True)
n = 4 - s.Rational(3, 2)*(1+w)
wX = s.simplify(-1+n/3)
for name, val, exponent, wx in [
    ('radiation', s.Rational(1,3), 2, -s.Rational(1,3)),
    ('dust', 0, s.Rational(5,2), -s.Rational(1,6)),
    ('vacuum_energy', -1, 4, s.Rational(1,3)),
]:
    zero('near_GR_scaling_'+name, n.subs(w, val) - exponent)
    zero('near_GR_effective_pressure_'+name, wX.subs(w, val) - wx)
details['near_GR'] = {'rho_X_power':str(n), 'w_X':str(wX),
                      'condition':'abs(rho_X) << rho; H_GR>0; constant matter w; first order in C'}

result = {'date':'2026-10-08', 'python':platform.python_version(), 'sympy':s.__version__,
          'scope':'Exact conditional identities, not a complete UBT dynamics or empirical test.',
          'lean_status':'LEAN-PENDING: lean and lake executables were unavailable in this runtime; generic claims have not been formalized.',
          'passed':all(c['passed'] for c in checks), 'checks_count':len(checks),
          'checks':checks, 'details':details}
output = Path(__file__).with_name('c5_dynamics_results.json')
output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'passed':result['passed'], 'checks_count':len(checks), 'details':details},
                 ensure_ascii=False, indent=2))
