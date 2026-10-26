<!-- BILINGUAL-UNIT: horizon-microstate-nonuniqueness -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact finite-dimensional benchmark; not a derived Theta horizon Hilbert space.
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

# Horizon microstates: SU(3) and shared reality do not fix the area coefficient

**26 October 2026. Exact finite-dimensional counterexample; conditional on a hypothetical discretized boundary Hilbert space.** This does not postulate a new fundamental UBT field and must not be interpreted as a microstate count of the actual Theta theory.

Choose one SU(3) triplet V=C^3 and its dual V*=C^(3*) for each of N putative boundary cells, with area A=N a0. The canonical SU(3)-invariant pure singlet on V tensor V* is |Phi3> = (1/sqrt(3)) sum_i |i> tensor |i*>. Tracing the inaccessible second factor gives rho_in=I3/3 and entropy log(3). The N-fold tensor product is globally pure (S_global=0), is gauge-singlet under diagonal SU(3), and has observer-accessible entropy S_inside=N log(3)=A log(3)/a0. In contrast, the globally pure product singlet |Phi3> pairing *within* each observer-accessible region and a trivial exterior singlet, when two inside cells are available, has zero inside/outside entanglement. The SU(3)-invariant global state and consistency of reduced states therefore do not determine the outside entropy. More generally the triplet-singlet sector itself requires a specified factorization/edge-mode prescription in gauge theories.

Matching the maximal-entanglement toy coefficient to the independent conditional MM/Wald formula S=A/(4G)=4 pi A/(g_G² ell²) would require

 log(3)/a0 = 1/(4G) = 4 pi/(g_G² ell²),

or a0 = [g_G² ell² log(3)]/(4 pi).

This is a **matching condition, not a prediction**: a0 is not fixed by the canonical biquaternion algebra, the SU(3) stabilizer or observer consistency, and changing allowed states or regulator changes the entropy. In an actual local continuum QFT, raw entanglement entropy has ultraviolet divergences and the split into area/renormalized G plus bulk entropy depends on regulator and gravitational edge modes. SU(3) gauge constraints obstruct a naive physical Hilbert tensor product; this benchmark is deliberately only an extended-space counting witness.

**Action-selection decision:** the entropy route is useful as an independent consistency test ONLY after deriving from one admissible Theta action: (i) physical quantum state and positive Hilbert space; (ii) observer subalgebras and SU(3)/gravitational edge-mode prescription; (iii) regulator/renormalization of G; (iv) an independent area cell scale or continuum entanglement calculation; (v) the same presymplectic Noether horizon charges. Otherwise any asserted agreement with A/(4G) by adjusting a0 is circular. No entropy microscopic derivation, unique MM selector or physical Hamiltonian follows.

Verification: tests/test_mm_horizon_microstate_nonuniqueness.py.
