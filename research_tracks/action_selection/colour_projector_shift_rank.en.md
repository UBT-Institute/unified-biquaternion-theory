<!-- BILINGUAL-UNIT: colour-projector-shift-rank -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact tangent-rank calculation; full complex split-jet gauge extension remains unproved.
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

# Route A: exact rank of the Theta colour projector and the split-jet carrier conflict

**2026-10-26.** Before this result read `T2_GAUGE/su3_positive_timelike_kinetic_candidate.md`, `su3_positive_kinetic_metric_lock_audit.md`, `su3_tree_level_dof_no_go.md`, and `action_selection/mm_geometry_colour_selection.en.md`. The positive internal timelike kinetic metric and its composite-metric collapse were already established; this note does not claim to rederive them.

Set G=diag(1,-1,-1,-1), h=Theta†GTheta>0, n=Theta/sqrt(h), P=n n†G. At reference Theta=r e0, r>0 real, for infinitesimal complex u, let u0=u0R+i u0I and u_j=u_jR+i u_jI. Taking the derivative of normalized n gives
 δP=(1/r)[ u_perp e0†G + e0 u_perp†G ],  u_perp=(0,u1,u2,u3).
Thus the pointwise real Jacobian dP/dTheta has **rank 6**, kernel span_R{e0,i e0} (radial and phase changes), on the full complex 8-real-dimensional timelike carrier. As a map from *Lorentz-real* carrier variations u in R^4 at e0, the Jacobian has **rank 3**, kernel radial span_R{e0}. The split-jet gravitational carrier shift δX=epsilon with auxiliary compensation can freely change these 3 Lorentz-real orientation directions while leaving (E,omega) invariant, as established on the non-null chart. A colour observable depending directly on P(Theta) therefore does not descend to the gravity-only split-jet quotient.

There is an important distinction: the additional imaginary components of full complex Theta yield three extra projector-tangent directions (total six), but **no** full-complex split-jet shift law has yet been proved that gauges those imaginary directions away. It would be incorrect to infer that all six colour-projector directions are gauge or ghosts.

The alternative projector-derivative density tr((∂P)(∂P)) has a positive spatial-tangent quadratic form on a fixed background: for u_j,
 tr(δP²)=-(2/r²) sum_j |u_j|², so -tr(δP²) is positive. Yet a kinetic action for P is not invariant under arbitrary X->X' compensated at Q, because P changes while E stays fixed. Further, because P is unaffected by the complex phase of Theta, it has no phase/singlet kinetic term. This is at most a geometric candidate for the six tangent fields on an **independently chosen spacetime metric**. It neither evades the previously proved metric-lock collapse nor produces the eight transverse physical gluons, and does not select the fundamental Hamiltonian.

**Exact decision:** route A leaves a genuine choice of model architecture. Keep the gravitational split-jet quotient and build matter from shift-invariant E,omega (losing this particular moving-colour orientation as a physical local field), OR retain the Theta orientation and derive a unified constraint system where its six projector modes have a healthy reduced Hamiltonian. The present algebra does not supply that dynamical completion.
