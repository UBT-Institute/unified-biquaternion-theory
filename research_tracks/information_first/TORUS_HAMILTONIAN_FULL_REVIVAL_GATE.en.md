<!-- BILINGUAL-UNIT: torus-hamiltonian-full-revival-gate -->
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

# Toroidal Hamiltonian and exact recurrence criterion (route B)

**2026-10-26. Conditional spectral theorem, not a derivation of the fundamental UBT Hamiltonian.** Applies to a flat d-torus with positive definite metric G_ab in angular coordinates theta^a ∼ theta^a+2π. It extends `THETA_PERIOD_TWO_HAMILTONIAN_RECURRENCE.en.md` while respecting `canonical/bridges/theta_parameter_separation.md`.

Let physical Hilbert space for this isolated test sector be L²(T^d,sqrt(det G) d^d theta), and let
  H_tor = E0 + alpha (-Delta_G), alpha>0,
with -Delta_G = -G^{ab} partial_a partial_b. This operator on periodic H² functions is self-adjoint and bounded below by E0, with normalized Fourier eigenvectors e_n(theta)=exp(i n_a theta^a), n in Z^d, and
  E_n=E0+alpha n^T G^{-1} n.
The positive metric gives no negative kinetic modes in this **isolated torus sector**, not positivity of the full coupled gravity/Theta system.

**Full revival theorem.** U(T)=exp(-i E0 T/hbar) I on the complete Hilbert space if and only if
  (alpha T/(2π hbar)) n^T G^{-1} n ∈ Z for every n∈Z^d.
Set B=(alpha T/(2π hbar)) G^{-1}. Testing integer basis vectors and their pairwise sums proves equivalence to
  B_ii ∈ Z and 2 B_ij ∈ Z (i≠j).
Sufficiency follows n^T B n=∑ B_ii n_i²+∑_{i<j} 2B_ij n_i n_j ∈ Z. The criterion permits half-integral off-diagonal entries: requiring every B_ij integer would be unnecessarily strong.

For diagonal circular radii G=diag(R_1²,...,R_d²), revival exists iff there is T with alpha T/(2π hbar R_a²) integer for ALL a. Equivalent to all inverse-square radii ratios being rational (for finite d). Incommensurate radii prevent an EXACT common revival, although approximate quantum recurrences may occur on finite mode sets. Generic tilted torus likewise fails the exact rational quadratic-form condition.

**Nonuniqueness:** GL(d,Z) torus coordinate changes relabel the integer lattice and preserve the spectrum. The revival criterion constrains shape ratios only; it does not fix overall scale alpha, R, or select one lattice. The scalar theta heat-trace modular identities remain different from physical-time recurrence absent the declared generator above. Correlation-negentropy identities do not enforce exact revival; using revival as a new selection principle would be a further physical hypothesis that requires independent motivation and empirical support.

**UBT gate:** derive this -Delta_G with alpha and G from the true reduced Theta dynamics (not merely propose it); find gauge-invariant observer observables sensitive to relative Fourier phases; then compare their correlator revivals to candidate physical clocks and the MM/gravity constraints. No string winding sectors have been introduced.
