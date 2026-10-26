<!-- BILINGUAL-UNIT: right_only_su2_lorentz_slice_stabilizer -->
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


# Right-only SU(2) stabilizer of the canonical Lorentz slice

**Exact kinematic theorem (2026-10-25), not a full gauge-group determination or Hamiltonian.** Refines the scope of #747.

In the standard 2x2 matrix representation, the locked Lorentz slice is W_L=i Herm_2. Consider constant **right-only** multiplication E→ER with R∈SU(2), demanding ER∈W_L for **every** E∈W_L.

For E=iI this condition implies (iR)†=−iR, thus R†=R. For arbitrary E=iH, H†=H, condition (iHR)†=−iHR implies R†H=HR; with R†=R this gives [R,H]=0 for every Hermitian H. Therefore R=cI with real c, and R∈SU(2) forces c=±1:
\[
\boxed{\operatorname{Stab}_{SU(2)}^{\mathrm{right-only}}(W_L)=\{+I,-I\}.}
\]
Conversely ±I clearly preserve W_L. More generally for arbitrary invertible right-only complex matrices the stabilizer is the nonzero real scalars; SU2 restricts it to ±I.

**Important interpretation:** the arbitrary right-SU2 mixing used as a diagnostic in #747 does *not* preserve the entire canonical Lorentz slice when acting only on E. This removes the premise that all of SU2 can be assumed a gauge freedom of admissible tetrads. However the theorem is not a proof that right-column choice in the F(Theta) Weyl-dual map is canonical: the physically allowed transformation of Theta need not equal pure right multiplication of E; two-sided Lorentz congruence E→SES† does preserve W_L and the sharp metric (#735), while the spinor carrier map and composite derivative still require compatibility. Nor is SU2 ruled out as a symmetry acting jointly on other composite structures.

**For Hamiltonian/action:** no extra right-SU2 first-class constraints may be imposed merely from arbitrary column recombinations. Determine the actual symmetry action on full (Theta,DTheta,A[Theta],B[Theta],T[Theta]) and physical presymplectic structure before defining chiral charges and torsion sources.

This proof imposes preservation of W_L for *all* admissible tetrad elements. Stabilizers of particular field configurations can be larger; they do not establish a universal gauge symmetry.
