<!-- BILINGUAL-UNIT: transverse_contortion_auxiliary_variation -->
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


# Transverse contortion: conditional quadratic auxiliary variational selector

**C-tier conditional result, 2026-10-25. NOT a derivation of the fundamental UBT action.** This note tests whether a separately postulated algebraic term can lift the 12-dimensional reconstruction kernel.

Let V be non-null, g Lorentzian and K=K0+C, with C_{a mu b}=-C_{b mu a} and C_{a mu b} V^b=0. Here K0 is the particular covariant local reconstruction in the canonical definitions and C is its transverse difference. Consider the auxiliary functional

S_C = (lambda/2) int d^4x sqrt(-g) C_{a mu b} C^{a mu b},

with nonzero real lambda, treating g,V and K0 as fixed for the *restricted* variation with respect to C. This functional is a **trial term**; lambda and the particular K0 are not selected by locked UBT axioms. The chosen non-null V makes the projector onto its orthogonal complement well-defined.

For each mu the antisymmetric pair (a,b) belongs to Lambda^2(V_perp); thus its induced metric is nondegenerate for non-null V. Since the metric on the mu index is nondegenerate too, the restricted quadratic Hessian on all 12 components is nondegenerate. The Euler-Lagrange equation for lambda != 0 and no other C-dependent pieces is uniquely C=0. For timelike V, the 12 components comprise four copies of three spatial two-form components. In an orthonormal rest frame the Hessian is a nonzero diagonal multiple of diag(-1,-1,-1,+1,+1,+1,+1,+1,+1,+1,+1,+1) (overall sign depends on signature conventions and ordering). In particular this quadratic form is indefinite in Lorentz signature: stationarity does not establish a positive energy minimum.

More generally, if other terms provide a transverse linear source J and no other C-dependent nonlinear terms, S_trial=S_C+int sqrt(-g) J^{a mu b} C_{a mu b} yields C=-lambda^{-1} P_transverse J (with appropriate raised/lowered positions). This is algebraic; do not infer physical spin-current identification without deriving the coupling.

The full Theta-only variation is not the restricted delta_C variation. C is not an established independent fundamental degree of freedom. If C=C[Theta] is already defined, one must apply chain rule for delta_Theta C and include implicit variation of g,V,K0. Alternatively, treating C as an auxiliary integration variable is a different candidate formulation, which must be justified as equivalent and constrained, not silently adopted. A generic curvature term R(omega0+C) and matter couplings introduce additional C dependence; their complete Euler-Lagrange equations may change the C=0 outcome. The effect on torsion, local Lorentz/diffeomorphism symmetry, kinetic principal symbol, Hamiltonian constraints, positivity and physical modes is not established here.

**Conclusion:** the algebraic 12-dimensional kernel is *liftable by an added quadratic auxiliary term*, but this is an existence construction, not an axiom-free selector of UBT dynamics or action. Next test: whether the same invertible transverse operator follows from a canonically justified existing Palatini/torsion sector or a Theta-only variational identity, with no new free postulate.

Grounding: canonical/CANONICAL_DEFINITIONS.md §3; research_tracks/action_selection/composite_contortion_kernel.en.md; transverse_contortion_dual.en.md; contortion_stabilizer_invisibility.en.md.
