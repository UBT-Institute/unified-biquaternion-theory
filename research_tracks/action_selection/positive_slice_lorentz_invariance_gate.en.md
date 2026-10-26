<!-- BILINGUAL-UNIT: positive_slice_lorentz_invariance_gate -->
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


# Positive real slice: exact inertia and Lorentz-congruence obstruction

**Status:** conditional finite-dimensional no-go for a *linear* positive-definite restriction of the already classified quadratic invariant H, under the established congruence carrier X->SXS^dagger. 2026-10-26. Not a proof that every constrained or nonlinear completion is impossible.

For the real eight-vector (Re z0,Re z1,Re z2,Re z3,Im z0,Im z1,Im z2,Im z3), the invariant H(X)=2(|z0|²-sum_j|zj|²) has exact inertia (2,6). Sylvester's law implies a positive-definite linear subspace has real dimension <=2. The complex scalar line P={X=zI} has dimension two and H|P=2|z|²>0 when z!=0, hence saturates this bound.

But for the SL(2,C) congruence action and real boost S=exp(eta sigma3/2),
S(z I) S^dagger=z[cosh(eta) I+sinh(eta) sigma3].
Its derivative at eta=0 is z sigma3 and lies outside P for z !=0. Thus P is not invariant under the full local Lorentz congruence action. SU(2) rotations do preserve P. Another frequently suggested choice, the Hermitian slice X=X^dagger, has H inertia (1,3) rather than positive definite: merely choosing a Hermitian restriction does not repair the original kinetic-signature problem.

Dynamical invariance is a SEPARATE gate: even if a truncated scalar ansatz is preserved by a simplified ungauged potential model, it is not a consistent reduction of the proposed locally SL(2,C)-gauged theory unless the gauge transformations, connection, time evolution, constraints and gauge fixing preserve the slice. An independent metric decouples the tetrad rank obstruction from X only if explicitly accepted in a new ADR; the canonical composite tetrad remains unchanged pending such decision.

**Verdict:** keeping the same Lorentz-invariant H and congruence symmetry, no positive-definite linear two-plus-real-dimensional Theta slice exists; the exhibited maximal positive two-real-dimensional slice fails local boost invariance. This alone is not an exhaustive classification of every nonlinear, constrained or gauge-fixed option (a), and is not a full ADM Dirac falsification.

Reproduction: tools/verify_theta_positive_slice.py and tests/test_theta_positive_slice.py. No fundamental action was changed.
