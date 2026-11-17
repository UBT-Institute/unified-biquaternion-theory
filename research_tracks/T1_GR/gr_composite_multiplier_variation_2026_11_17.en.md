<!-- BILINGUAL-UNIT: composite-multiplier-2026-11-17 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact constrained variational identity; no full UBT action selection or on-shell GR.
UBT-AI-PROVENANCE-END
-->
# Exact constrained composite variation without assuming inverse A

<!-- UNIT: scope -->
## What is and is not derived

This is the exact constrained-variation formalism for a GIVEN parent functional S[Theta,E,K] with the locked canonical tetrad and metric-compatible omega. Lambda is an auxiliary multiplier, not an independent propagating physical field or a new canonical axiom. Introducing a parent independent K is a provisional auxiliary parametrization; a real single-Theta theory also needs its constitutive or algebraic torsion selector. The functional itself is not fixed by the kinematic axioms.

<!-- UNIT: variation -->
## Complete constrained Euler system

```text
E = J(Theta,E,K) = N0^(-1/2) D_{omega(E,K)} Theta
omega(E,K) = omega_LC(E)+K
S_tilde = S_parent[Theta,E,K] + <Lambda,E-J(Theta,E,K)>
A=I-J_E, Y=-Lambda
delta_Lambda: E-J=0
delta_E:      A^*Y=S_E
delta_Theta:  S_Theta + J_Theta^*Y=0
delta_K:      S_K+J_K^*Y=0
If A is invertible in the chosen gauge and functional setting:
  Y=(A^*)^(-1)S_E;
  reduced equations agree with ordinary implicit chain rule.
If A has kernel, existence of Y may require
  <z,S_E>=0 for z in ker(A) (necessary; sufficient only under closed-range
  or Fredholm-type assumptions); Y may be nonunique.
For a locked Lorentz-invariant quadratic kinetic term on the Lorentz-real slice:
  S_kin=2N0 integral det(E), S_E=2N0 det(E) E^(-1).
```

<!-- UNIT: proof -->
## Variation and invertibility-free formulation

Differentiate F=E-J in the respective independent variables: F_E=A, F_Theta=-J_Theta, F_K=-J_K. The Lagrange term contributes A^*Lambda, -J_Theta^*Lambda, -J_K^*Lambda to the three Euler derivatives. With Y=-Lambda obtain the boxed system. Integrations by parts are formal and require specified domains, gauge and boundary conditions; for Levi-Civita(E), J_E is a differential operator. If A is invertible on the reduced domain, eliminate Y and recover the existing implicit-chain formulas. If not, keep Y and all compatibility equations instead of asserting an inverse.

<!-- UNIT: gradient -->
## Sanity check: pure-gradient slice

In the restricted torsion-free gradient scheme E=dY with no implicit E dependence, A=I. The locked kinetic is the Jacobian null Lagrangian and its compact-supported variation with respect to Y vanishes by the Piola identity. The multiplier system is compatible with this fact; it does not produce an Einstein kinetic term. Explicit potential terms or imported curvature terms change the parent functional and invalidate the pure-volume-only inference.

<!-- UNIT: critical -->
## Remaining first-principles obstruction

The constrained system is NOT a unique UBT theory, a solution existence theorem, or a graviton proof. The canonical audit canonical/gr_closure/gap_10tdyn_10d_canonical_action_audit.tex still identifies the Hilbert-Palatini gravity term as imported. Neither rank-four direct current nor rank-fifteen arbitrary-force tangent space decides the source rank after solving A^*Y=S_E with full Theta reality constraints. A complete first-principles result requires (1) microscopic action selection, (2) consistent physical torsion K[Theta], (3) on-shell background and boundary/gauge function spaces, (4) constrained Hessian, positive massless helicity-two sector, (5) universal matter coupling and coefficient.

<!-- UNIT: verification -->
## Reproducible finite analogue and CI status

Exact SymPy source: tools/verify_gr_constrained_multiplier_2026_11_17.py verifies every Euler derivative and its equivalence to the directly reduced derivative in a nonlinear two-dimensional finite model, plus a singular adjoint compatibility counterexample. This finite test does not verify the full Fréchet/PDE adjoints. Prior PR #900 CI has failures in bilingual parity, provenance, documentation and repository-size gates; this new note is not merged. Formal Lean and full constrained on-shell UBT tests remain unresolved.
