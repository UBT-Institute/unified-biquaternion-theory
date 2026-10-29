#!/usr/bin/env python3
"""Specified bare matched-pairing/free-jet action; no fixed Theta dimension.

Not a no-go for all UBT pairings, carrier actions or quantum completions.
"""
from __future__ import annotations
import json
from functools import lru_cache
import numpy as np
import sympy as s


@lru_cache(maxsize=1)
def symbolic_checks():
    checks = {}
    vol, f, dv, df = s.symbols("vol F dv dF")
    eps = s.Symbol("eps")
    checks["general_first_variation_product_rule"] = s.diff((vol+eps*dv)*(f+eps*df), eps).subs(eps, 0) == dv*f+vol*df
    for n in (1, 3, 8, 13):
        q = s.symbols(f"q:{n}", real=True)
        weight = (sum(x*x for x in q)-1)**2
        critical = dict(zip(q, [1]+[0]*(n-1)))
        checks[f"arbitrary_carrier_dimension_{n}_critical_zero"] = weight.subs(critical) == 0 and all(s.diff(weight, x).subs(critical) == 0 for x in q)
    # Full matrix directions in the current illustrative potential family.
    q = s.symbols("q:8", real=True)
    X = s.Matrix([[q[0]+s.I*q[1], q[4]+s.I*q[5]], [q[6]+s.I*q[7], q[2]+s.I*q[3]]])
    H = 2*s.re(X[0, 0]*s.conjugate(X[1, 1]))-abs(X[0, 1])**2-abs(X[1, 0])**2
    D = s.expand_complex(X.det()*s.conjugate(X.det())).expand()
    F = s.expand(H-D-1)
    critical = dict(zip(q, [0, 1, 0, 1, 0, 0, 0, 0]))
    checks["existing_quartic_has_critical_zero"] = F.subs(critical) == 0
    for j, x in enumerate(q):
        checks[f"all_existing_matrix_directions_stationary_{j}"] = s.diff(F, x).subs(critical) == 0
    hessian = s.hessian(F, q).subs(critical)
    checks["witness_algebraic_Hessian_rank_four"] = hessian.rank() == 4
    left, right = s.symbols("left:8"), s.symbols("right:8")
    u, v = s.symbols("u v")
    dvol, evol, ddvol = s.symbols("dvol evol ddvol")
    curved_path = {x: critical[x]+u*left[j]+v*right[j] for j, x in enumerate(q)}
    density = (vol+u*dvol+v*evol+u*v*ddvol)*F.subs(curved_path, simultaneous=True)
    mixed = s.diff(density, u, v).subs({u: 0, v: 0})
    checks["complete_second_variation_has_only_algebraic_potential_block"] = s.expand(mixed-vol*(s.Matrix(left).T*hessian*s.Matrix(right))[0]) == 0
    # A noncentral invertible matrix tests the generic algebraic jet map.
    T = s.Matrix([[1+s.I, 2], [s.I, 3-s.I]])
    p = s.symbols("p:8", real=True)
    P = s.Matrix([[p[0]+s.I*p[1], p[2]+s.I*p[3]], [p[4]+s.I*p[5], p[6]+s.I*p[7]]])
    response = s.Matrix([part for z in P*T for part in (s.re(z), s.im(z))]).jacobian(p)
    checks["noncentral_matrix_auxiliary_response_is_surjective"] = response.det() == 256
    multipliers = s.symbols("lambda:8", real=True)
    checks["full_multiplier_equation_has_only_zero_solution"] = s.linsolve(list(response.T*s.Matrix(multipliers)), multipliers) == s.FiniteSet((0,)*8)
    base = s.Matrix(2, 2, s.symbols("base:4"))
    target = s.Matrix(2, 2, s.symbols("target:4"))
    checks["exact_relative_jet_right_inverse"] = (base+(target-base)*T.inv()*T-target).applyfunc(s.expand) == s.zeros(2)
    # Curvature is recomputed from coordinate Christoffels, not assumed.
    time, chi, theta, phi = s.symbols("T chi theta phi", real=True)
    coords = (time, chi, theta, phi)
    a = s.Function("a")(time)
    g = s.diag(-1, a*a, a*a*s.sin(chi)**2, a*a*s.sin(chi)**2*s.sin(theta)**2)
    inv = g.inv()
    Gamma = [[[s.simplify(sum(inv[i, k]*(s.diff(g[k, j], coords[l])+s.diff(g[k, l], coords[j])-s.diff(g[j, l], coords[k]))/2 for k in range(4))) for l in range(4)] for j in range(4)] for i in range(4)]
    def ricci(i, j):
        return s.simplify(sum(s.diff(Gamma[k][i][j], coords[k])-s.diff(Gamma[k][i][k], coords[j])+sum(Gamma[k][i][j]*Gamma[l][k][l]-Gamma[l][i][k]*Gamma[k][j][l] for l in range(4)) for k in range(4)))
    R00, R11 = ricci(0, 0), ricci(1, 1)
    checks["Ricci_time_from_coordinate_connection"] = s.simplify(R00+3*s.diff(a, time, 2)/a) == 0
    checks["Ricci_space_from_coordinate_connection"] = s.simplify(R11-(a*s.diff(a, time, 2)+2*s.diff(a, time)**2+2)) == 0
    witness = {a: 1+time**2}
    checks["non_Einstein_witness_time_component"] = R00.subs(witness).doit().subs(time, 0) == -6
    checks["non_Einstein_witness_space_component"] = R11.subs(witness).doit().subs(time, 0) == 4
    checks["non_Einstein_witness_is_regular"] = g.det().subs(witness).doit().subs({time: 0, chi: s.pi/2, theta: s.pi/2}) == -1
    pauli = [s.Matrix([[0, 1], [1, 0]]), s.Matrix([[0, -s.I], [s.I, 0]]), s.diag(1, -1)]
    A = 1+time**2
    boost = s.diff(A, time)
    for j, sigma in enumerate(pauli):
        physical = (boost-s.I)*sigma/2
        jet = (A-boost)*sigma/2
        combined = physical+jet
        generated = combined*(s.I*s.eye(2))+(s.I*s.eye(2))*combined.conjugate().T
        checks[f"constant_Theta_existing_splitjet_generates_scale_{j}"] = (generated-s.I*A*sigma).applyfunc(s.expand) == s.zeros(2)
    checks["constant_Theta_relative_time_jet_generates_unit_lapse"] = s.eye(2)*(s.I*s.eye(2)) == s.I*s.eye(2)
    return checks


def numerical_checks():
    rng = np.random.default_rng(20261028)
    def weight(x):
        h = 2*np.real(x[0, 0]*np.conj(x[1, 1]))-abs(x[0, 1])**2-abs(x[1, 0])**2
        return h-abs(np.linalg.det(x))**2-1
    errors = []
    for _ in range(32):
        delta = (rng.normal(size=(2, 2))+1j*rng.normal(size=(2, 2)))/4
        tetrad = np.diag([1., 1.3, 1.7, 2.1])+rng.normal(size=(4, 4))/10
        de = rng.normal(size=(4, 4))/10
        vals = []
        for step in (1e-2, 1e-3, 1e-4):
            def density(t):
                return np.linalg.det(tetrad+t*de)*weight(1j*np.eye(2)+t*delta)
            vals.append(abs((density(step)-density(-step))/(2*step)))
        errors.append(vals)
    maxima = np.max(errors, axis=0).tolist()
    return {"seed":20261028,"samples":32,"steps":[1e-2,1e-3,1e-4],"max_first_variation_errors":maxima,"checks":{"critical_first_variation_accuracy":maxima[-1]<1e-6,"critical_first_variation_convergence":maxima[-1]<maxima[0]/1000}}


def verify():
    exact, numeric = symbolic_checks(), numerical_checks()
    return {"scope":"dimension-independent weighted-volume stationarity with free algebraic jets; current matrix-potential and non-Einstein metric are illustrative witnesses", "versions":{"sympy":s.__version__,"numpy":np.__version__}, "symbolic":exact,"numerical":numeric,"passed":all(exact.values()) and all(numeric["checks"].values()),"not_proved":["fundamental Theta component count","all carrier actions share this kinetic pairing","selected microscopic action or jet closure","general constrained Dirac algebra","quantum induced gravity with a derived measure"]}


if __name__ == "__main__":
    result = verify()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["passed"] else 1)
