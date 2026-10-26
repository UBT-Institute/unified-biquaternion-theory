<!-- BILINGUAL-UNIT: volume_primary_constraints_nonzero_connection -->
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


# Primary constraints from volume Lagrangian with nonzero velocity-independent composite connection

**Exact conditional Legendre analysis, 2026-10-26. Not a final UBT Hamiltonian/action or a zero-connection model.** Extends draft #767.

Restricted pure Lorentz-vector-lift branch: e_mu^a=(partial_mu v^a+omega_mu^a_b[v,partial_i v,...]v^b)/sqrt(N0), with omega generally NONZERO but **not dependent on dot(v)** or higher time derivatives in the chosen local reduction. Work in an oriented regular tetrad chart. Let c=2N0 and L=c det(e_mu^a).

Write u^a=dot(v^a), w^a=omega_0^a_b v^b. Spatial e_i^a are independent of u by hypothesis. By determinant multilinearity in its time row,
\[
L=\frac{c}{\sqrt{N_0}}(u^a+w^a)C_a,\quad C_a=(-1)^a\det(e_i{}^{b\ne a}).
\]
The cofactor uses the standard time-row Laplace signs.

Hence
\[
p_a=\partial L/\partial u^a=\frac{c}{\sqrt{N_0}}C_a,\quad W_{ab}=\partial^2 L/\partial u^a\partial u^b=0,\quad \phi_a=p_a-\frac{c}{\sqrt{N_0}}C_a\approx0.
\]
The canonical Hamiltonian density evaluated on this first-order branch is
\[
H_c=p_a u^a-L=-\frac{c}{\sqrt{N_0}}w^a C_a
\]
on the primary constraint surface, and the total Hamiltonian is H_T=H_c+lambda^a phi_a, with lambda undetermined until the full Dirac consistency algorithm. The 4 primary constraints need NOT be first-class. They do not imply four gauge transformations or zero propagating degrees of freedom without computing their mutual PB and secondary constraints.

If omega depends on u or spatial e_i depends on u through implicit reconstruction (as may happen in the actual UBT), the argument fails: the full chain-rule and reduced Hessian from merged #757 must be computed. A potential term can change constraints' preservation and H_c, but if velocity independent it does not alter the zero Hessian. This is a necessary *candidate rejection* test, not proof of the full single-Theta action.

An explicit symbolic 4x4 coframe with NONZERO omega_0^0_1=omega_0^1_0=k yields L=c(u0+k v1)/sqrtN0 times cofactor C0 plus terms from other velocity components; regression verifies Hessian=0, primary momenta and cancellation of velocities in H_c.

Open: derive torsion selection and actual omega[v,jets] including velocity response, compute all Θ components (eight real), complex-time psi data, induced higher derivative variation, actual PB/constraint closure and physical energy.
