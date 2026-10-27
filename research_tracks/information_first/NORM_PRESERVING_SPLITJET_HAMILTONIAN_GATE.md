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

# Norm-preserving split-jet transformations: exact finite lift and Hamiltonian gate

**2026-10-26. Exact non-null real Lorentz-carrier result; no full-complex Dirac closure claimed.**

Use E_mu=(D_omega X+Q_mu)/sqrt(N0), X²=X^T eta X>0, with eta=diag(1,-1,-1,-1). The infinitesimal restriction delta h=2X^T eta epsilon=0 picks the three-dimensional tangent plane to a constant-norm hyperboloid. It does NOT require h=0. At finite amplitude take any smooth local proper orthochronous Lorentz field L(x), X'=L X, Q'_mu=Q_mu+D_omega(X-X'). Then E'=E and h'=h identically. These transformations close by composition on (X,Q); the finite lift is a **subgroup of the already established split-jet carrier redundancy**. The transformed Q' can be decomposed into K'_J X'+w'X' on the non-null chart by the existing split-jet right inverse, so the auxiliary parametrization is preserved locally, not necessarily globally or with imposed auxiliary boundary conditions.

At a reference X=r e0, tangent variations epsilon=(0,epsilon_1,epsilon_2,epsilon_3). They change the colour projector P(X)=XX^T eta/X² in three independent directions: delta P_{0i}=-epsilon_i/r, delta P_{i0}=epsilon_i/r. For a boost X'=r(cosh chi,sinh chi,0,0), h'=r² while P' != P. Thus the condition delta h=0 preserves the **norm**, not the moving-colour orientation. If all these norm-preserving transformations remain gauge, the three real projector directions remain gauge artefacts, not physical colour excitations.

One must distinguish three different operations:
(A) restrict gauge transformations to norm-preserving ones: leaves the norm h(X) invariant and potentially changes the physical field content if the original larger gauge group was genuinely present;
(B) impose h(X)=h0>0 as a gauge condition of the ORIGINAL unrestricted split-jet redundancy: fixes a local radial carrier coordinate, leaving three residual gauge directions; it is not a dynamical equation of motion;
(C) impose h(X)=h0 as a new physical constraint after changing the action: requires a genuine Dirac consistency analysis and may remove physics.

If h(X) enters the original physical action nontrivially, (A) cannot be asserted a gauge symmetry of that action without checking the variations. In the pure gravity MM pullback depending only on E,omega, the larger shift remains exact locally; declaring only norm-preserving shifts gauge does not magically add kinetic energy for h. A meaningful dynamical selection of Hamiltonian must introduce an explicitly derived gauge-invariant term or a proved coupling to physical observables, not merely set delta h=0.

**Result:** norm-preserving split-jet subgroup closes and removes three real orientation coordinates on the non-null real carrier patch. It does not establish a physical triplet, unique Hamiltonian, or the corresponding first-class Dirac algebra for the full complex system.

Verification: tests/test_information_norm_preserving_splitjet.py.
