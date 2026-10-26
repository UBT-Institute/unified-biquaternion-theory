<!-- BILINGUAL-UNIT: bilinear_tetrad_conformal_rank -->
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


# Four bilinear Lorentz vectors produce only a conformal metric

**Exact algebraic limitation (2026-10-25), not the canonical tetrad, physical Hamiltonian or UBT action.** Extends #752.

Identify biquaternions with Mat2(C), choose Hermitian Pauli basis sigma_a=(I,sigma_x,sigma_y,sigma_z) and define four Lorentz-slice vectors
\[
\widetilde E_a=i\Theta\sigma_a\Theta^\dagger.
\]
Under Theta→STheta, S∈SL2(C), each transforms by Lorentz congruence \(\widetilde E_a→S\widetilde E_a S^\dagger\). If det Theta≠0, their four real components form an invertible basis for W_L=i Herm2.

By the 2×2 adjugate identity \(X^\sharp=\operatorname{adj}(X)\) and \(H(v)^\sharp H(v)=\det(H(v)) I\), equivalently polarization of the determinant, the canonical sharp anticommutator yields
\[
\boxed{\frac12(\widetilde E_a^\sharp\widetilde E_b+\widetilde E_b^\sharp\widetilde E_a)
=|\det\Theta|^2\eta_{ab}I,\quad \eta=\mathrm{diag}(-1,1,1,1).}
\]
Thus if the index a is directly identified with a **fixed coordinate coframe**, the resulting metric is only \(g_{ab}=|\det\Theta|^2\eta_{ab}\), a conformally flat metric. At a point its variations have rank **one in metric space** (away from singular det and possible zero gradient), compared with the generic 10 metric components. Additional left SL2C variations rotate the frame without changing the metric; the scalar conformal factor is |detTheta|.

This does NOT exclude general curved UBT configurations: the **locked** E_mu=N0^(-1/2)D_mu Theta is a derivative/connection-defined tetrad, not this bilinear frame. If one introduces a separate variable coordinate coframe, it carries more information but must be derived rather than assumed as a new fundamental field. Nor is nonzero Riemann curvature excluded: conformally flat metrics can have curvature, although the Weyl tensor vanishes for this ansatz.

Important: sigma_a index is originally an internal tetrad label; coordinate identification is an extra assumption. This is a rank obstruction to using the *naive algebraic bilinear frame* as the entire gravitational metric, not to all possible covariant soldering constructions.

Next gate: retain canonical DTheta and derive its composite two-sided connection + torsion such that the **first jet** attains full rank-10 metric variations after reduction; then test curvature, constraints and positive physical Hamiltonian. Do not replace canonical E by this tilde E.
