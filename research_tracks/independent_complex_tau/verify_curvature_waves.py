#!/usr/bin/env python3
"""Bounded checks for curvature_waves.en.md / curvature_waves.cs.md.

Recomputes the curved symplectic normal map and ADM tensor coefficients.
The Fraction channel independently checks finite lifts and polarization
energies. This does not select an action or establish the full C5 spectrum.
"""
import itertools
import json
import platform
from fractions import Fraction as Q
from pathlib import Path

import sympy as s


def verify():
    checks = []

    def exact(name, expression, channel="SymPy"):
        values = list(expression) if isinstance(expression, (s.MatrixBase, list, tuple)) else [expression]
        passed = all(s.simplify(v) == 0 for v in values) if channel == "SymPy" else all(v == 0 for v in values)
        checks.append({"name": name, "channel": channel, "passed": passed})
        if not passed:
            raise AssertionError(name)

    t, x, y, z = coords = s.symbols("t x y z", real=True)
    T, beta = s.Function("T")(t), s.Function("beta")(t)
    xi = s.Matrix([s.Function("xi" + str(i))(*coords) for i in range(4)])
    eta = s.diag(-1, 1, 1, 1)
    pairing = -2*eta
    P = s.diag(s.diff(T, t), beta*T, beta*T, beta*T)  # internal, coordinate
    connection = [s.zeros(4) for _ in range(4)]
    for i in range(1, 4):
        connection[i][0, i] = connection[i][i, 0] = beta
    X = s.Matrix([T, 0, 0, 0])
    DX = s.Matrix.hstack(*[X.diff(c) + connection[mu]*X for mu, c in enumerate(coords)])
    exact("curved_background_generated_coframe", DX-P)
    exact("curved_background_nondegeneracy_factor", P.det()-s.diff(T,t)*(beta*T)**3)
    curvature = [[connection[nu].diff(coords[mu])-connection[mu].diff(coords[nu])
                  + connection[mu]*connection[nu]-connection[nu]*connection[mu]
                  for nu in range(4)] for mu in range(4)]
    exact("curvature_time_boost_component", curvature[0][1][1,0]-s.diff(beta,t))
    exact("curvature_spatial_rotation_component", curvature[1][2][1,2]-beta**2)
    Dxi = s.Matrix.hstack(*[xi.diff(c) + connection[mu]*xi for mu,c in enumerate(coords)])
    alpha = -P.T*pairing*xi

    def exterior(one_form):
        return s.Matrix(4,4,lambda mu,nu: s.diff(one_form[nu],coords[mu])-s.diff(one_form[mu],coords[nu]))

    delta_Q = -Dxi.T*pairing*P + P.T*pairing*Dxi
    exact("curved_normal_map_twisted_exact_form", delta_Q-beta*exterior(alpha/beta))
    curvature_pair = s.Matrix(4,4,lambda mu,nu: (-xi.T*pairing*curvature[mu][nu]*X)[0])
    exact("curved_normal_map_covariant_chain_rule", exterior(alpha)-delta_Q-curvature_pair)
    pfaffian = lambda A: A[0,1]*A[2,3]-A[0,2]*A[1,3]+A[0,3]*A[1,2]
    exact("curved_quadratic_weight_beta_squared", pfaffian(delta_Q)-beta**2*pfaffian(exterior(alpha/beta)))

    # Recompute the ADM coefficients from gamma=a^2 exp(epsilon h), without
    # starting from an assumed tensor wave action. A Fourier direction can be
    # rotated to z; both independent transverse tensor polarizations remain.
    eps = s.symbols("eps")
    plus, cross = s.Function("plus")(t,z), s.Function("cross")(t,z)
    h = s.Matrix([[plus,cross,0], [cross,-plus,0], [0,0,0]])
    identity = s.eye(3)
    spatial = identity+eps*h+eps**2*h*h/2
    inverse = identity-eps*h+eps**2*h*h/2

    def truncate(value):
        return s.expand(value).series(eps,0,3).removeO().expand()

    exact("TT_exponential_volume_through_second_order", truncate(spatial.det())-1)
    exact("TT_inverse_metric_through_second_order", (spatial*inverse-identity).applyfunc(truncate))
    expansion = s.symbols("H", real=True)
    K = (expansion*identity+inverse*spatial.diff(t)/2).applyfunc(truncate)
    kinetic = truncate(s.trace(K*K)-s.trace(K)**2)
    exact("ADM_background_extrinsic_term", kinetic.coeff(eps,0)+6*expansion**2)
    exact("ADM_linear_tensor_extrinsic_term", kinetic.coeff(eps,1))
    exact("ADM_quadratic_tensor_kinetic_coefficient", kinetic.coeff(eps,2)-s.trace(h.diff(t)*h.diff(t))/4)
    spatial_coords = [x,y,z]
    Gamma = [[[truncate(sum(inverse[i,l]*(
        s.diff(spatial[l,k],spatial_coords[j])+s.diff(spatial[l,j],spatial_coords[k])
        -s.diff(spatial[j,k],spatial_coords[l]))/2 for l in range(3)))
        for k in range(3)] for j in range(3)] for i in range(3)]
    Ricci = s.Matrix(3,3,lambda i,j: truncate(sum(
        s.diff(Gamma[k][i][j],spatial_coords[k])-s.diff(Gamma[k][i][k],spatial_coords[j])
        +sum(Gamma[k][k][l]*Gamma[l][i][j]-Gamma[k][j][l]*Gamma[l][i][k] for l in range(3))
        for k in range(3))))
    scalar = truncate(sum(inverse[i,j]*Ricci[i,j] for i,j in itertools.product(range(3),repeat=2)))
    exact("ADM_linear_tensor_spatial_curvature", scalar.coeff(eps,1))
    exact("ADM_quadratic_tensor_gradient_coefficient", scalar.coeff(eps,2)+s.trace(h.diff(z)*h.diff(z))/4)
    a, kappa = s.Function("a")(t), s.symbols("kappa", positive=True)
    adm_second = a**3*(kinetic.coeff(eps,2)+scalar.coeff(eps,2)/a**2)/(2*kappa)
    target = a**3*(s.diff(plus,t)**2+s.diff(cross,t)**2
                  -(s.diff(plus,z)**2+s.diff(cross,z)**2)/a**2)/(4*kappa)
    exact("ADM_two_polarization_action_normalization", adm_second-target)
    # The linear lapse/shift constraints vanish for TT data on the background.
    exact("TT_linear_momentum_constraint", s.Matrix([
        sum(s.diff(h.diff(t)[j,i],spatial_coords[j]) for j in range(3)) for i in range(3)]))
    exact("TT_linear_trace_constraint", s.trace(K).expand().coeff(eps,1))
    variables = s.symbols("hxx hxy hxz hyy hyz hzz")
    general_h = s.Matrix([[variables[0],variables[1],variables[2]],
                         [variables[1],variables[3],variables[4]],
                         [variables[2],variables[4],variables[5]]])
    constraints = s.Matrix([s.trace(general_h),general_h[2,0],general_h[2,1],general_h[2,2]])
    exact("nonzero_momentum_TT_constraint_rank", constraints.jacobian(variables).rank()-4)

    # Complete Euler equation and Hamiltonian from the computed density.
    q = s.Function("q")(*coords)
    density = a**3*(s.diff(q,t)**2-sum(s.diff(q,c)**2 for c in [x,y,z])/a**2)/(4*kappa)
    euler = sum(s.diff(s.diff(density,s.diff(q,c)),c) for c in coords)
    expected = s.diff(q,t,2)+3*s.diff(a,t)/a*s.diff(q,t)-sum(s.diff(q,c,2) for c in [x,y,z])/a**2
    exact("tensor_full_Euler_equation", 2*kappa*euler/a**3-expected)
    momentum = s.diff(density,s.diff(q,t))
    hamiltonian = momentum*s.diff(q,t)-density
    exact("tensor_Hamiltonian_positive_sum", hamiltonian-a**3*(s.diff(q,t)**2
          +sum(s.diff(q,c)**2 for c in [x,y,z])/a**2)/(4*kappa))
    frequency, k, scale = s.symbols("frequency k scale", positive=True)
    plane = s.exp(s.I*(k*z-frequency*t))
    exact("tensor_frozen_characteristic_polynomial", (s.diff(plane,t,2)-s.diff(plane,z,2)/scale**2)/plane
          -(-frequency**2+k**2/scale**2))

    # de Sitter has Lambda>0; finite ell does not have a flat vacuum.
    ell, coupling = s.symbols("ell g_G", positive=True)
    exact("candidate_de_Sitter_Friedmann_constraint", 3/ell**2-3*(1/ell)**2)
    exact("candidate_tensor_coefficient", 1/(8*(coupling**2*ell**2/2))-1/(4*coupling**2*ell**2))
    conformal_time = s.symbols("eta", negative=True)
    v = s.Function("v")(conformal_time)
    av = s.Function("a_c")(conformal_time)
    rescaled = v/av
    exact("canonical_rescaled_tensor_equation", av*(s.diff(rescaled,conformal_time,2)
        +2*s.diff(av,conformal_time)/av*s.diff(rescaled,conformal_time)+k**2*rescaled)
        -(s.diff(v,conformal_time,2)+(k**2-s.diff(av,conformal_time,2)/av)*v))
    de_sitter_a = -ell/conformal_time
    exact("de_Sitter_conformal_pump", s.diff(de_sitter_a,conformal_time,2)/de_sitter_a-2/conformal_time**2)
    mode = (conformal_time-s.I/k)*s.exp(-s.I*k*conformal_time)
    exact("de_Sitter_exact_tensor_mode", s.diff(mode,conformal_time,2)-2*s.diff(mode,conformal_time)/conformal_time+k**2*mode)
    exact("de_Sitter_finite_late_time_mode", s.limit(mode,conformal_time,0,dir="-")+s.I/k)

    # The explicit split-jet lift can carry tensor perturbations with delta X=0.
    norm, nu = s.symbols("normalization nu", nonzero=True)
    dE = s.zeros(4)
    dE[1:4,1:4] = a*h/2
    domega = [s.zeros(4) for _ in range(4)]
    dK = [s.zeros(4) for _ in range(4)]
    for mu in range(4):
        for i in range(1,4):
            boost = s.symbols("boost_"+str(mu)+"_"+str(i))
            domega[mu][i,0] = domega[mu][0,i] = boost
            dK[mu][i,0] = dK[mu][0,i] = norm*dE[i,mu]/nu-boost
    constant_X = s.Matrix([nu,0,0,0])
    lifted = s.Matrix.hstack(*[(domega[mu]+dK[mu])*constant_X/norm for mu in range(4)])
    exact("TT_split_jet_lift_at_constant_Theta", lifted-dE)
    exact("TT_split_jet_lift_Lorentz_antisymmetry", [(eta*A+(eta*A).T)[i,j]
          for A in dK for i,j in itertools.product(range(4),repeat=2)])

    # Separate rational implementations: no SymPy expressions in this channel.
    for index, (bb,db,tt,dt,xx,dx) in enumerate([
        (Q(2),Q(3),Q(5),Q(7),[Q(1),Q(2),Q(3),Q(4)],
         [[Q(i+2*j+1) for j in range(4)] for i in range(4)]),
        (Q(3,2),Q(-2,3),Q(4,5),Q(7,3),[Q(2),Q(-1),Q(4),Q(3)],
         [[Q(2*i-j,3) for j in range(4)] for i in range(4)])
    ]):
        pp = [dt,bb*tt,bb*tt,bb*tt]
        dpp = [Q(0),db*tt+bb*dt,db*tt+bb*dt,db*tt+bb*dt]
        hh = [Q(2),Q(-2),Q(-2),Q(-2)]
        cov = [row[:] for row in dx]
        for i in range(1,4):
            cov[0][i] += bb*xx[i]
            cov[i][i] += bb*xx[0]
        al = [-hh[i]*pp[i]*xx[i] for i in range(4)]
        dal = [[-hh[j]*(pp[j]*dx[j][i]+(dpp[j]*xx[j] if i==0 else 0))
                +hh[i]*(pp[i]*dx[i][j]+(dpp[i]*xx[i] if j==0 else 0))
                for j in range(4)] for i in range(4)]
        residual = []
        for i,j in itertools.product(range(4),repeat=2):
            direct = -hh[j]*cov[j][i]*pp[j]+hh[i]*cov[i][j]*pp[i]
            twisted = dal[i][j]-db/bb*((al[j] if i==0 else 0)-(al[i] if j==0 else 0))
            residual.append(direct-twisted)
        exact("fraction_curved_normal_identity_"+str(index),residual,"Python Fraction")

    for index,(pp,cc,dp,dc,nn,vv) in enumerate([
        (Q(2),Q(3),Q(5),Q(7),Q(11),Q(13)),
        (Q(-2,3),Q(4,5),Q(1,7),Q(-3,2),Q(5,2),Q(7,3))
    ]):
        tensor = [[pp,cc,Q(0)],[cc,-pp,Q(0)],[Q(0),Q(0),Q(0)]]
        velocity = [[dp,dc,Q(0)],[dc,-dp,Q(0)],[Q(0),Q(0),Q(0)]]
        residual = [sum(v*v for row in velocity for v in row)/Q(4)-(dp*dp+dc*dc)/Q(2)]
        for i,j in itertools.product(range(3),repeat=2):
            target_entry = tensor[i][j]/Q(2)
            omega_entry = Q(i+j+1,7)
            jet_entry = nn*target_entry/vv-omega_entry
            residual.append((jet_entry+omega_entry)*vv/nn-target_entry)
        exact("fraction_tensor_normalization_and_lift_"+str(index),residual,"Python Fraction")

    return {"date":"2026-10-10", "passed":all(c["passed"] for c in checks),
            "checks_count":len(checks), "checks":checks,
            "python":platform.python_version(), "sympy":s.__version__,
            "scope":"Fixed curved isotropic symplectic branch; conditional four-dimensional vacuum tensor dynamics of the existing split-jet curvature candidate.",
            "not_tested":"Microscopic action selection, full nonlinear constraint formalization, arbitrary composite connections, all complex/independent-tau modes, quantization or observations.",
            "lean_status":"LEAN-PENDING: no Lean/Lake executables or checked formalization of the geometric and variational arguments supplied."}


if __name__ == "__main__":
    result = verify()
    Path(__file__).with_name("curvature_waves_results.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({key:result[key] for key in ["passed","checks_count","python","sympy"]}))
