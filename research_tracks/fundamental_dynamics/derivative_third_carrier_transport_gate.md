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

# Derivative third carrier: construction does not supply transport law

**Conditional exact geometric distinction (2026-10-26).** Let v be nonnull timelike, w linearly independent, and e a nondegenerate Lorentz tetrad. Their plane has a nondegenerate Gram matrix G_IJ=eta(a_I,a_J) (a_0=v,a_1=w), and the orthogonal projector is P=1-a_I (G^{-1})^{IJ} a_J_flat. For a metric scalar I(g), define q^a=e^{a mu} partial_mu I and u=Pq. This is a covariant local composite constructed without an independent fundamental field, assuming g and its Levi-Civita curvature are already defined. If u!=0, the three vectors v,w,u are independent, so specifying consistent connection images for all three gives a unique Lorentz connection by the rank-six theorem.

However **the construction alone does NOT select the image omega_mu u**. For any solution omega of the two existing transport relations and any stabilizer one-form C_mu=alpha_mu J_perp with C_mu v=C_mu w=0, omega'=omega+C still obeys Dv and Dw, and e/g/I(g)/u are unchanged as kinematic data, while D'_mu u=D_mu u+alpha_mu J_perp u. If u!=0, J_perp u generally !=0. Thus merely computing u from the metric does not eliminate four arbitrary alpha_mu. Imposing Du=0, or Du=D_LC u, would be an additional transport law requiring an action/derivation, not a consequence of its definition.

Even u!=0 is background-dependent: for constant curvature scalar I, u vanishes. Using invariant I=Riemann² can help in some curved configurations but does not provide an everywhere-guaranteed nonzero third direction. Curvature built from the unknown torsionful omega would cause further implicit dependence; using Levi-Civita scalar of the metric avoids that circularity for the *candidate vector* but cannot by itself determine omega.

**Result:** a derivative composite can break the pointwise SO(2) stabilizer if provided a consistent independent transport image, but the current locked UBT kinematic axioms have not supplied that image. Therefore residual connection selection remains a dynamical rather than purely algebraic problem. No new canonical action, physical field, or Hamiltonian has been established.
