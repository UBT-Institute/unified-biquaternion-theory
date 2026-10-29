<!-- BILINGUAL-UNIT: mm-composite-presymplectic-variation -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact conditional first-variation identity, not a completed full-Theta Dirac analysis.
UBT-AI-PROVENANCE-END -->
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

# Exact first variation of split-jet MM/Palatini and its presymplectic boundary term

**26 October 2026.** Builds on the existing `single_theta_macdowell_mansouri_candidate.en.md` and `splitjet_presymplectic_gate.en.md`. Work locally at non-null X, constant N0>0, and express the auxiliary carrier map as Q^a=K_J{}^a{}_b X^b+w X^a. Because the split-jet map is pointwise onto, use (X,Q,omega) as local redundant variables, E^a=N0^(-1/2)(D_omega X^a+Q^a). The map back to K_J,w and its kernel must be separately accounted for.

For the **chosen** MM candidate, Euler topology aside, write its first-order Palatini Lagrangian four-form L_HP(E,omega), and define Euler–Lagrange 3-forms F_a and C_ab by the convention
  δL_HP = δE^a ∧ F_a + δω^{ab} ∧ C_ab + d θ_HP,
  θ_HP = (1/(4κ)) ε_abcd E^a∧E^b∧δω^{cd}
(with the normalization of the repository's MM note). The Euler-density variation also adds an exact boundary potential θ_Euler, which must be retained for horizon charges.

Since
 δE^a=N0^(-1/2)(D_omega δX^a + δω^a{}_b X^b+δQ^a),
the Leibniz identity for a 0-form δX and a 3-form F gives
 DδX^a∧F_a=d(δX^a F_a)-δX^a D F_a.
Consequently the composed action has the exact bulk-plus-boundary split
 δL_comp = δQ^a∧(F_a/√N0)
 + δω^{ab}∧[C_ab + (X-dependent algebraic contraction of F)/√N0]
 - δX^a (D F_a)/√N0
 + d[θ_HP + θ_Euler + δX^a F_a/√N0].
The contraction of δω X with F depends on antisymmetric index conventions and is intentionally not promoted here to a component formula. This expression is an identity modulo the Euler-density boundary convention; no use of field equations was made.

Thus a valid presymplectic potential is
  θ_comp = θ_HP + θ_Euler + δX^a F_a/√N0.
**On the full Palatini equation F_a=0**, its additional Theta term vanishes in the bulk, while its variation must be evaluated carefully on tangent vectors that solve the linearized field equations, and boundary terms from the Euler density retained. The on-shell presymplectic current is therefore a pullback of the Palatini-plus-Euler current, modulo the standard potential ambiguities and admissible boundary conditions. This identifies a necessary part of, but not yet a global proof of, reduced phase-space equivalence.

For δX=ε, δQ=−D_omega ε, δω=0, one has δE=0 **off shell** and hence δL_comp=0 for the pure Palatini/MM pullback. This is an honest local gauge redundancy of that candidate's **(X,Q)** parametrization, provided the auxiliary lift exists and the transformation respects boundaries. Its presymplectic charge vanishes for compactly supported ε on the stationary surface. Nothing here proves the full complex eight-real Theta or ψ sector is pure gauge. Generic finite boundary transformations can carry edge charges and cannot be discarded.

This exact identity is the next bridge towards a Dirac count, not proof of Hamiltonian positivity: one must compute the complete rank of the auxiliary lift and all remaining first-class constraints, then compare reduced phase spaces on a nondegenerate background, including horizons.

Test: `tests/test_mm_composite_variation_identity.py`.
