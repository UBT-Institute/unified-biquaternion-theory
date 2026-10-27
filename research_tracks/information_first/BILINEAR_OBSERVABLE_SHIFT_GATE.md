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

# Bilinear observables under split-jet reduction: a no-selection theorem

**2026-10-26. Restricted non-null Lorentz-real split-jet result, not a full-complex Theta no-go.**

Take the gravitational parametrization E=(D_omega X+Q)/sqrt(N0), with the finite local carrier transformation X->X+epsilon, Q->Q-D_omega epsilon, at fixed omega. On any non-null chart small arbitrary epsilon(x) preserve admissibility and keep E exactly unchanged. Thus a derivative-free scalar F(X) that is invariant under all these shifts must satisfy dF_X(epsilon)=0 for all epsilon, hence is locally constant on each connected chart. This applies to Lorentz norm h(X)=X^T eta X: delta h=2X^T eta epsilon, and to every nonconstant polynomial invariant derived from it. For the moving complex projector P(Theta), restricting epsilon to the real carrier changes it in three independent directions at timelike reference Theta=r e0. Therefore neither h(X) nor P(Theta) is an observable of this **gravity-only quotient**, even if it is invariant under other groups such as Lorentz or SU(3).

Consequently equal-time or time-dependent correlators of h(X) or P(Theta) cannot legitimately fix the physical kinetic ratio a/b in the gravity-only MM model: they depend on arbitrary representative X. Choosing a gauge and declaring these correlators physical would be a new observable prescription, not a derivation. In particular a positive Hermitian coefficient pairing K_{a,b} does not by itself supply a gauge-invariant variance ratio.

What survives: local functions of E,omega and geometric curvature/torsion, their properly dressed/relational observables, and boundary data subject to gravity diffeomorphism constraints. These can encode gravitational responses but do not generally access the triplet carrier orientation. Ordinary point-local E itself is Lorentz-covariant, NOT automatically a gauge-invariant diffeomorphism observable; physical comparisons require relational identification.

This theorem cannot be extended to all complex Theta imaginary modes without a proved full-complex shift action, and it does not preclude a modified unified action with physical orientation and altered constraints. The actual remaining task is an explicit full-complex action and its Dirac reduction, or a derivation that observables built from geometry determine kinetic coefficients.

**Decision:** on the exact known gravitational quotient, the proposed Theta-bilinear information selector is obstructed. The correlation-negentropy principle alone cannot repair the lack of a physical state/observable map or choose a/b.

Test: tests/test_information_bilinear_shift_invariance.py.
