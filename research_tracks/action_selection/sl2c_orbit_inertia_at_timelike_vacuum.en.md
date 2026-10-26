<!-- BILINGUAL-UNIT: sl2c_orbit_inertia_at_timelike_vacuum -->
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


# SL(2,C) vacuum stabilizer: rank three, not six

**2026-10-25 — exact finite-dimensional tangent-orbit computation, C-tier, independently reproducible in SymPy. Not a full Dirac constraint analysis.**

Let X0=i r I, r real nonzero, and local SL(2,C) act on the vector/Hermitian-congruence carrier as X -> S X S^dagger. A basis of the real Lie algebra is J_j=i sigma_j/2 and B_j=sigma_j/2. Its infinitesimal action is delta_T X=T X+X T^dagger. For J_j, delta X0=0. For B_j, delta X0=i r sigma_j. Hence the orbit at X0 has rank 3, not 6, while the stabilizer is SU(2), dimension 3.

For X=z0 I+sum_j z_j i sigma_j, the real Lorentz/phase invariant H=2(|z0|^2-sum|zj|^2) has inertia (2,6) on the eight real coordinates. The three boost-orbit tangent directions lie in the negative subspace, and their induced Gram form is negative definite. The orthogonal complement therefore has inertia (2,3). Exactly three negative directions survive tangent-orbit removal.

This does NOT establish three physical ghosts: additional primary/secondary constraints, time diffeomorphisms, other gauge transformations, and matter/gravity mixing may alter physical mode counting. Conversely, the numerical coincidence dim SL(2,C)=6 and negative inertia=6 supplies no proof of ghost removal. In a noncompact YM extension its gauge-field kinetic signature is an independent obstruction and must be included before claiming stability.

**Verifier:** tools/verify_sl2c_orbit_inertia.py; pytest tests/test_sl2c_orbit_inertia.py.

**ADR scope:** proposed independent metric and psi-circle changes are not accepted. Existing canonical action remains unfinalized. This result is for the already studied congruence action at X0 and does not assume that every UBT connection transforms in this representation.
