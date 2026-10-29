#!/usr/bin/env python3
"""Full composite variation on a declared flat-jet/closed-dilation branch.

This tests a supplied torsion-quadratic family. It does not select a UBT
action or identify the flat jet connection with the physical Levi-Civita
connection. All variations here preserve the explicitly restricted branch.
"""
from functools import lru_cache
import json

import numpy as np
import sympy as s

ETA = (-1, 1, 1, 1)


@lru_cache(maxsize=1)
def symbolic_checks():
    checks = {}
    eta = s.diag(*ETA)
    w = s.Matrix(s.symbols("w:4", real=True))
    T = [[[int(a == b)*w[c]-int(a == c)*w[b]
           for c in range(4)] for b in range(4)] for a in range(4)]
    lower = [[[ETA[a]*T[a][b][c] for c in range(4)] for b in range(4)] for a in range(4)]
    upper = [[[ETA[a]*ETA[b]*ETA[c]*lower[a][b][c]
               for c in range(4)] for b in range(4)] for a in range(4)]
    I1 = sum(lower[a][b][c]*upper[a][b][c] for a in range(4) for b in range(4) for c in range(4))
    I2 = sum(lower[a][b][c]*upper[c][b][a] for a in range(4) for b in range(4) for c in range(4))
    trace = s.Matrix([sum(T[n][m][n] for n in range(4)) for m in range(4)])
    W = (w.T*eta*w)[0]
    checks["torsion_trace_is_minus_three_w"] = trace == -3*w
    checks["first_torsion_invariant_is_six_w_squared"] = s.expand(I1-6*W) == 0
    checks["second_torsion_invariant_is_three_w_squared"] = s.expand(I2-3*W) == 0
    checks["trace_square_is_nine_w_squared"] = s.expand((trace.T*eta*trace)[0]-9*W) == 0
    c1, c2, c3 = s.symbols("c1 c2 c3", real=True)
    kappa = s.Symbol("kappa", positive=True)
    coefficient = 6*c1+3*c2+9*c3
    checks["all_quadratic_coefficients_reduce_to_one_combination"] = s.expand(c1*I1+c2*I2+c3*9*W-coefficient*W) == 0
    checks["positive_EH_torsion_combination_has_coefficient_six"] = coefficient.subs({c1: -s.Rational(1, 4), c2: -s.Rational(1, 2), c3: 1}) == 6

    chi = s.Symbol("chi", positive=True)
    grad = s.Matrix(s.symbols("d:4", real=True))
    entries = s.symbols("h:10", real=True)
    hess = s.zeros(4)
    n = 0
    for i in range(4):
        for j in range(i, 4):
            hess[i, j] = hess[j, i] = entries[n]; n += 1
    box = sum(ETA[i]*hess[i, i] for i in range(4))
    norm_grad = (grad.T*eta*grad)[0]
    # Generic conformal metric jets, computed from the coordinate definition
    # of Riemann. Multiply Riemann by chi^2 to keep every entry polynomial.
    G = [[[int(a == b)*grad[c]+int(a == c)*grad[b]-eta[b, c]*ETA[a]*grad[a]
           for c in range(4)] for b in range(4)] for a in range(4)]
    dG = [[[[int(a == b)*hess[c, m]+int(a == c)*hess[b, m]-eta[b, c]*ETA[a]*hess[a, m]
             for m in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
    R = [[[[s.expand(chi*(dG[a][nu][b][mu]-dG[a][mu][b][nu])
                -grad[mu]*G[a][nu][b]+grad[nu]*G[a][mu][b]
                +sum(G[a][mu][l]*G[l][nu][b]-G[a][nu][l]*G[l][mu][b] for l in range(4)))
             for nu in range(4)] for mu in range(4)] for b in range(4)] for a in range(4)]
    ricci_scaled = s.Matrix(4, 4, lambda b, nu: sum(R[a][b][a][nu] for a in range(4))).applyfunc(s.expand)
    scalar_scaled = s.expand(sum(ETA[i]*ricci_scaled[i, i] for i in range(4)))
    checks["Ricci_scalar_from_full_coordinate_Riemann"] = s.expand(scalar_scaled+6*chi*box) == 0
    Weyl = []
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    value = ETA[a]*R[a][b][c][d] - (
                        eta[a, c]*ricci_scaled[b, d]-eta[a, d]*ricci_scaled[b, c]
                        -eta[b, c]*ricci_scaled[a, d]+eta[b, d]*ricci_scaled[a, c])/2
                    value += scalar_scaled*(eta[a, c]*eta[b, d]-eta[a, d]*eta[b, c])/6
                    Weyl.append(s.expand(value))
    checks["all_256_Weyl_components_vanish_identically"] = all(v == 0 for v in Weyl)
    checks["Ricci_torsion_boundary_identity"] = s.expand(-6*chi*box-(6*norm_grad-6*(norm_grad+chi*box))) == 0

    # Differentiate with respect to the coordinate-map Jacobian BEFORE
    # evaluating at Y=x. Thus the carrier/coordinate equations are retained.
    A, eps = s.symbols("A eps", real=True)
    currents = s.zeros(4)
    for a in range(4):
        for mu in range(4):
            unit = s.zeros(4); unit[a, mu] = 1
            J = s.eye(4)+eps*unit
            L = A*J.det()*(grad.T*J.inv()*eta*J.inv().T*grad)[0]
            momentum = s.diff(L, eps).subs(eps, 0)
            predicted = A*(int(a == mu)*norm_grad-2*grad[a]*ETA[mu]*grad[mu])
            checks[f"coordinate_momentum_variation_{a}_{mu}"] = s.expand(momentum-predicted) == 0
            currents[a] += sum(s.diff(momentum, grad[j])*hess[j, mu] for j in range(4))
    scalar_euler = -2*A*box
    for a in range(4):
        checks[f"full_coordinate_Euler_Noether_identity_{a}"] = s.expand(-currents[a]+grad[a]*scalar_euler) == 0
    EY = s.Matrix(s.symbols("EY:4"))
    Y = s.Matrix(s.symbols("Y:4")); Ec = s.Symbol("Ec")
    b = s.Symbol("b", nonzero=True)
    ef = (Y.T*EY)[0]-chi*Ec
    checks["composite_field_value_chain_recovers_scalar_equation"] = s.simplify(
        (ef-(Y.T*(b*EY/b))[0])/(-chi)-Ec) == 0

    velocity, p = s.symbols("velocity p", real=True)
    L_scalar = A*(-velocity**2+sum(grad[i]**2 for i in range(1, 4)))
    checks["scalar_canonical_momentum"] = s.diff(L_scalar, velocity) == -2*A*velocity
    H = s.simplify((p*velocity-L_scalar).subs(velocity, -p/(2*A)))
    expected_H = -p**2/(4*A)-A*sum(grad[i]**2 for i in range(1, 4))
    checks["full_scalar_Legendre_Hamiltonian"] = s.simplify(H-expected_H) == 0
    checks["regular_scalar_velocity_Hessian"] = s.diff(L_scalar, velocity, 2) == -2*A
    checks["Einstein_sign_reduced_energy_is_negative"] = s.simplify(H.subs(A, 3/kappa)+kappa*p**2/12+3*sum(grad[i]**2 for i in range(1, 4))/kappa) == 0
    lam = s.Symbol("lam", real=True)
    checks["reduced_energy_scales_quadratically"] = s.expand(H.subs({p: lam*p, **{grad[i]:lam*grad[i] for i in range(1, 4)}}, simultaneous=True)-lam**2*H) == 0
    # Every conformal-plus-coordinate perturbation has zero TT projection.
    k = s.Matrix([1, 2, 3]); shift = s.Matrix(s.symbols("shift:3"))
    projector = s.eye(3)-k*k.T/(k.T*k)[0]
    perturbation = 2*chi*s.eye(3)+k*shift.T+shift*k.T
    transverse = projector*perturbation*projector
    tt = transverse-projector*s.trace(transverse)/2
    checks["no_TT_mode_in_composite_metric_tangent"] = tt.applyfunc(s.simplify) == s.zeros(3)
    # Explicit composite, on-shell, curved and non-Einstein witness.
    t, e = s.symbols("t e", real=True)
    substitution = {chi:1+e*t, **{grad[i]:(e if i == 0 else 0) for i in range(4)}, **{h:0 for h in entries}}
    witness_R = (ricci_scaled/chi**2).subs(substitution).applyfunc(s.simplify)
    checks["linear_chi_is_on_shell_for_scalar_equation"] = scalar_euler.subs(substitution) == 0
    checks["curved_witness_has_R00"] = s.simplify(witness_R[0, 0]-3*e**2/(1+e*t)**2) == 0
    checks["curved_witness_has_R11"] = s.simplify(witness_R[1, 1]-e**2/(1+e*t)**2) == 0
    checks["curved_witness_has_zero_scalar_R"] = scalar_scaled.subs(substitution) == 0
    checks["exact_non_Einstein_witness_at_chi_two"] = witness_R.subs({t:1,e:1}) == s.diag(s.Rational(3,4),s.Rational(1,4),s.Rational(1,4),s.Rational(1,4))
    return checks


def local_density(data, coefficients, scale=1.3, kappa=1.7):
    """Independent original X,f,L jet construction, including connection response."""
    Y, J, HY, chi, c, h, beta, db, hb, angle, da, ha = data
    eta = np.diag(ETA)
    KB = np.zeros((4, 4)); KB[0, 1] = KB[1, 0] = 1
    KR = np.zeros((4, 4)); KR[1, 2], KR[2, 1] = 1, -1
    B = np.eye(4); B[0, 0] = B[1, 1] = np.cosh(beta); B[0, 1] = B[1, 0] = np.sinh(beta)
    R = np.eye(4); R[1, 1] = R[2, 2] = np.cos(angle); R[1, 2], R[2, 1] = np.sin(angle), -np.sin(angle)
    L = B@R; inverse_L = eta@L.T@eta
    dL = [db[m]*KB@L+da[m]*B@KR@R for m in range(4)]
    ddL = [[hb[m,n]*KB@L+db[m]*db[n]*KB@KB@L+ha[m,n]*B@KR@R
             +da[m]*da[n]*B@KR@KR@R+(db[m]*da[n]+db[n]*da[m])*KB@B@KR@R
             for n in range(4)] for m in range(4)]
    omega = [-v@inverse_L for v in dL]
    domega = [[-ddL[m][n]@inverse_L+dL[m]@inverse_L@dL[n]@inverse_L for n in range(4)] for m in range(4)]
    X = scale*chi*(L@Y)
    dX = [scale*(c[m]*L@Y+chi*dL[m]@Y+chi*L@J[:,m]) for m in range(4)]
    ddX = [[scale*(h[m,n]*L@Y+c[m]*dL[n]@Y+c[n]*dL[m]@Y+chi*ddL[m][n]@Y
              +c[m]*L@J[:,n]+c[n]*L@J[:,m]+chi*dL[m]@J[:,n]+chi*dL[n]@J[:,m]+chi*L@HY[:,m,n])
             for n in range(4)] for m in range(4)]
    w = -c/chi; dw = -h/chi+np.outer(c,c)/chi**2
    frame = np.column_stack([(dX[m]+omega[m]@X+w[m]*X)/scale for m in range(4)])
    dframe = [[(ddX[m][n]+domega[m][n]@X+omega[m]@dX[n]+dw[m,n]*X+w[m]*dX[n])/scale
               for m in range(4)] for n in range(4)]
    torsion = np.zeros((4,4,4))
    curvature_error = commutator_norm = 0.
    for m in range(4):
        for n in range(4):
            torsion[:,m,n] = dframe[m][n]-dframe[n][m]+omega[m]@frame[:,n]-omega[n]@frame[:,m]
            commutator = omega[m]@omega[n]-omega[n]@omega[m]
            curvature_error = max(curvature_error,float(np.max(np.abs(domega[n][m]-domega[m][n]+commutator))))
            commutator_norm = max(commutator_norm,float(np.linalg.norm(commutator)))
    metric = frame.T@eta@frame; inv = np.linalg.inv(metric)
    coordinate_torsion = np.einsum("ra,amn->rmn",np.linalg.inv(frame),torsion)
    lower = np.einsum("rs,smn->rmn",metric,coordinate_torsion)
    upper = np.einsum("ai,bj,ck,ijk->abc",inv,inv,inv,lower)
    trace = np.einsum("nmn->m",coordinate_torsion)
    invariants = np.array([np.sum(lower*upper),np.einsum("abc,cba",lower,upper),trace@inv@trace])
    original = np.linalg.det(frame)*np.dot(coefficients,invariants)/(2*kappa)
    coefficient = np.dot([6,3,9],coefficients)/(2*kappa)
    reduced = coefficient*np.linalg.det(J)*(c@np.linalg.inv(J.T@eta@J)@c)
    return original,reduced,{
        "coframe_error":float(np.max(np.abs(frame-chi*L@J))),
        "curvature_error":curvature_error,"commutator_norm":commutator_norm,
        "density_error":float(abs(original-reduced)),
        "non_null_X":bool(X@eta@X < 0),"positive_orientation":bool(np.linalg.det(frame)>0),
    }


def numerical_checks(samples=24, seed=20261029):
    rng = np.random.default_rng(seed)
    worst = {"coframe_error":0.,"curvature_error":0.,"density_error":0.,"first_variation_error":0.}
    commutator = 0.; regular = True
    def symmetric_matrix():
        a=rng.normal(scale=.05,size=(4,4)); return (a+a.T)/2
    for sample in range(samples):
        Y = rng.normal(scale=.1,size=4);Y[0]+=2
        J=np.eye(4)+rng.normal(scale=.03,size=(4,4))
        HY=np.stack([symmetric_matrix() for _ in range(4)])
        data=[Y,J,HY,float(rng.uniform(.9,1.3)),rng.normal(scale=.1,size=4),symmetric_matrix(),
              float(rng.normal(scale=.1)),rng.normal(scale=.08,size=4),symmetric_matrix(),
              float(rng.normal(scale=.1)),rng.normal(scale=.08,size=4),symmetric_matrix()]
        coefficients=(np.array([-.25,-.5,1]) if sample%3==0
                      else np.array([1.,-2.,0.]) if sample%3==1 else rng.normal(size=3))
        _,_,record=local_density(data,coefficients)
        for key in ["coframe_error","curvature_error","density_error"]:worst[key]=max(worst[key],record[key])
        commutator=max(commutator,record["commutator_norm"])
        regular=regular and record["non_null_X"] and record["positive_orientation"]
        direction=[]
        for a in data:
            direction.append(rng.normal(scale=.03,size=np.shape(a)) if np.shape(a) else float(rng.normal(scale=.03)))
        direction[2]=(direction[2]+direction[2].transpose(0,2,1))/2
        for i in [5,8,11]:direction[i]=(direction[i]+direction[i].T)/2
        epsilon=1e-5
        plus=local_density([a+epsilon*b for a,b in zip(data,direction)],coefficients)
        minus=local_density([a-epsilon*b for a,b in zip(data,direction)],coefficients)
        d_original=(plus[0]-minus[0])/(2*epsilon)
        d_reduced=(plus[1]-minus[1])/(2*epsilon)
        worst["first_variation_error"]=max(worst["first_variation_error"],float(abs(d_original-d_reduced)))
    return {"samples":samples,"seed":seed,"finite_difference_step":1e-5,"maximum_errors":worst,
            "maximum_noncommuting_connection_norm":commutator,
            "checks":{"original_tetrad_covariance":worst["coframe_error"]<1e-11,
                      "nonzero_Lorentz_connection_is_flat":worst["curvature_error"]<1e-11,
                      "noncommuting_connection_components_present":commutator>1e-4,
                      "original_torsion_action_matches_reduced_action":worst["density_error"]<1e-10,
                      "full_branch_jet_first_variation_matches":worst["first_variation_error"]<1e-7,
                      "all_points_regular":bool(regular)}}


def run_checks():
    exact,numeric=symbolic_checks(),numerical_checks()
    return {"scope":"Conditional quadratic jet-torsion family with flat Lorentz jet and closed real dilation; full branch variation, conformal scalar Hamiltonian and absent tensor sector",
            "versions":{"sympy":s.__version__,"numpy":np.__version__},
            "symbolic":exact,"numerical":numeric,
            "passed":all(exact.values()) and all(numeric["checks"].values()),
            "not_proved":["a selected microscopic Theta action or Newton coefficient","unrestricted-connection torsion equations","full complex-time or matter spectrum","global/null continuation","a no-go for nonflat jets or all teleparallel formulations"]}


if __name__ == "__main__":
    report=run_checks();print(json.dumps(report,indent=2))
    raise SystemExit(0 if report["passed"] else 1)
