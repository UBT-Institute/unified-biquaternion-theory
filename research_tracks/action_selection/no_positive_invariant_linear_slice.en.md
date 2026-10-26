<!-- BILINGUAL-UNIT: no_positive_invariant_linear_slice -->
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


# No nonzero positive SL(2,C)-invariant linear slice

**2026-10-26, exact conditional linear-algebra theorem.** This strengthens the positive-slice witness test, but it does not analyze nonlinear constraint manifolds or physical ADM phase space.

Let X=z0 I+ i sum_{j=1}^3 zj sigma_j for arbitrary complex z0,zj and H(X)=2(|z0|^2-sum_j |zj|^2). Consider the real 8-dimensional module with congruence X -> S X S^dagger for S in SL(2,C). Suppose W is a real linear subspace invariant under that representation and H restricted to W is positive definite.

SU(2) rotations preserve the scalar coefficient z0 and rotate the spatial vector coefficients (complex linearly in the three-vector). For any X in W, its Haar average over SU(2) is z0 I, which is still in W (finite-dimensional linear subspace and integral of elements of W). Hence Y=X-z0 I = i sum zj sigma_j belongs to W. If Y is nonzero, H(Y)=-2 sum |zj|²<0, contradicting positive definiteness. Thus all X in W are scalar z0 I.

For any nonzero X=z0 I in W, the boost S=exp(eta sigma3/2) yields S X S^dagger=z0[cosh(eta)I+sinh(eta)sigma3]. For real eta != 0 the second term is a nonzero traceless matrix, and hence the transformed X is outside the scalar line. This contradicts invariance. Consequently W={0}.

This proof applies regardless of which of the two allowed positive scalar real directions is selected. Note: the real-linear action used here is congruence (not the different left spinor action), H is the stated invariant form, and full SL(2,C) is required. The Lorentz-vector metric signature (2,6) and the group-action assumptions are mandatory. If a future ADR changes the representation, the conclusion must be retested.

**Interpretation:** A positive invariant *linear* configuration-space restriction of this kinetic quadratic form is impossible under the locked congruence action. This is a no-go for the specified class of variant (a), not a proof of physical ghosts in a fully constrained theory and not a theorem covering nonlinear or gauge-reduced phase-space constraints. Do not claim the entire UBT programme is falsified.

Proof is elementary and exact; the existing SymPy witness in tools/verify_theta_positive_slice.py verifies the maximal two-dimensional positive slice and its failure under a boost. This note upgrades the result using the SU(2) group-average argument without relying on sampling.
