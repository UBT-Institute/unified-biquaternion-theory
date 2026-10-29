<!-- BILINGUAL-UNIT: linearized_flat_theta_pure_gauge_no_go -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# Linearized flat Theta geometry: conditional pure-gauge no-go

**Status: conditional kinematic theorem, C-tier working note, 2026-10-25. NOT a no-go for full UBT and NOT a dynamical action/constraint derivation.**

## Canonical starting point

Use locked Axiom C: `E_mu=N0^(-1/2) D_mu Theta`, and the Lorentz slice `E_mu=i e_mu^0 1+e_mu^k e_k` with central sharp metric. For the paired covariant derivative use the canonical sign convention

```
D_mu Theta=partial_mu Theta + A_mu Theta - Theta B_mu.
```

Note that the plus-right-B notation in the research note `two_sided_metric_covariance.en.md` defines its B with the opposite sign. Never identify those B components without this sign conversion.

Take a constant nondegenerate flat tetrad `bar E_mu`, flat connection in inertial gauge `bar A=bar B=0`, and an affine background `bar Theta=Theta_0+sqrt(N0) bar E_mu x^mu`. The affine solution is a **kinematic representer**, not claimed to solve the as-yet unselected field equations.

Set `Theta=bar Theta+epsilon phi`, `A=epsilon a`, `B=epsilon b`. At first order,
```
delta E_mu = N0^(-1/2) [partial_mu phi + a_mu bar Theta - bar Theta b_mu].
```
The field-dependence of a,b, when composite, must be included in later linearized operator calculations.

## Restricted theorem: fixed flat connection and Lorentz-slice perturbations

Impose **both** `a=b=0` and `phi/sqrt(N0)=v^a u_a` with real smooth `v^a` and constant Lorentz-slice basis `u_a` corresponding to `bar E_mu`. Identify `v_mu=eta_mu a v^a` in this inertial frame. Then

```
delta e_mu^a = partial_mu v^a,
h_mu nu = delta g_mu nu = partial_mu v_nu + partial_nu v_mu.
```

The standard linearized Riemann tensor around eta is
```
R^(1)_mu nu rho sigma =
  1/2 (partial_rho partial_nu h_mu sigma
      +partial_sigma partial_mu h_nu rho
      -partial_rho partial_mu h_nu sigma
      -partial_sigma partial_nu h_mu rho).
```
Commutativity of smooth partial derivatives yields exactly `R^(1)=0`. Thus these restricted perturbations are infinitesimal diffeomorphisms and do not describe gauge-invariant linearized gravitational radiation.

Equivalently, `e_mu^a=bar e_mu^a+epsilon partial_mu v^a` is the Jacobian tetrad of the infinitesimal coordinate map `y^a=x^a+epsilon v^a`. This is a *kinematic* conclusion; boundary conditions may affect whether the corresponding diffeomorphism is deemed gauge at a boundary.

## Scope and immediate open gate

This result **does not** extend automatically to arbitrary 8-real biquaternion perturbations, nonzero composite connection perturbations, nontrivial Lorentz/spinor carrier maps, curved backgrounds, psi dynamics, or solutions of the full equations of motion. In particular nonzero `a_mu bar Theta - bar Theta b_mu` can produce curvature in the linearized metric. Those terms may also have nonlocal/implicit dependence on phi through the chosen reconstruction; they cannot be regarded as independent propagating modes without a composite map.

Next calculate `a_mu[phi],b_mu[phi]` by linearizing the **actual** Theta-dependent connection reconstruction at the affine background; test gauge covariance, integrability, nonzero gauge-invariant curvature and the principal symbol. Only after a candidate dynamical principle is fixed can one compute a physical kinetic Hessian, propagating DOF, constraint brackets, positive energy or graviton dispersion. No unique Hamiltonian or Einstein limit is claimed.

## Repo grounding

- `canonical/CANONICAL_DEFINITIONS.md`, sections 2-3: sharp metric, affine flat representer, torsionful local reconstruction and canonical minus-right-B convention.
- `research_tracks/action_selection/two_sided_metric_covariance.en.md`: exact covariance in plus-right-B notation.
- `research_tracks/action_selection/hamiltonian_first_foundations.en.md`: Hamiltonian nonuniqueness.
