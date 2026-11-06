<!-- BILINGUAL-UNIT: mm-circle.scope -->
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

# The internal phase circle and the MM curvature scale

**2026-11-06 · C_working · [L1] in the stated gravity comparator.** English is the source edition. Work with smooth full complex biquaternion fields on a spacetime patch times an internal phase circle, with the original covariant tetrad and sharp metric. In the four-dimensional MacDowell–Mansouri (MM) candidate, \(\ell>0\) normalizes the transvections and \(R_\psi>0\) specifies the period. [MM candidate](single_theta_macdowell_mansouri_candidate.en.md)

\[
\psi\sim\psi+2\pi R_\psi,\qquad
\Gamma_\psi^2=\varepsilon_\psi I,\qquad
\varepsilon_\psi\in\{+1,-1\},\qquad
\Lambda=\frac{3\varepsilon_\psi}{\ell^2}.
\]

<!-- BILINGUAL-UNIT: mm-circle.centralizer -->
## The Lorentz centralizer

Let \(\eta=\operatorname{diag}(-1,1,1,1)\) and \(\eta_5=\operatorname{diag}(\eta,\varepsilon_\psi)\). Embed the Lorentz algebra in the first block of \(\mathfrak{so}(\eta_5)\). Its centralizer inside the MM algebra is zero for both signs and also after complexification. [Cartan decomposition](https://arxiv.org/abs/gr-qc/0611154)

For \(X^T\eta_5+\eta_5X=0\) all diagonal entries vanish. For each \(i\in\{1,2,3\}\), the boost \(B_i\) exchanges basis vectors \(0\) and \(i\) and annihilates the others. In \(B_iX=XB_i\), row \(i\) and column \(i\) give \(X_{0c}=X_{r0}=0\) by choosing \(i\) distinct from the corresponding nonzero index. Row \(0\) gives \(X_{ic}=0\) for \(c\notin\{0,i\}\). Row \(4\) and column \(0\) give \(X_{4i}=0\). This covers every entry.

A smooth internal \(U(1)\) homomorphism into MM commuting with the Lorentz subgroup would have its generator in this centralizer. Its derivative is zero, so its connected image is trivial. The Clifford matrix \(\Gamma_\psi\) commutes with the Lorentz bivectors in the ambient matrix algebra and lies outside the MM Lie algebra. The result allows discrete holonomies and applies only to the proposed commuting continuous action inside MM.

<!-- BILINGUAL-UNIT: mm-circle.radius -->
## Radius freedom in the four-dimensional action

Assume that the full field and the auxiliary variables enter the MM action through the four-dimensional tetrad and physical connection. Assume periodicity and admissibility conditions preserved by the circle identification below, no explicit radius-dependent coefficients and no derivatives along the circle. Keep the four-dimensional couplings, including \(\ell\), fixed.

\[
f\colon(x,\psi')\mapsto(x,R_\psi\psi'/R_\psi'),\qquad
d_4 f^*=f^*d_4,\qquad
\mathcal F[f^*\mathcal A]=f^*\mathcal F[\mathcal A].
\]

Pullback identifies the actions at corresponding phases. If the family is integrated with normalized uniform circle measure, the actions agree exactly. With unnormalized uniform measure they differ by the constant \(R_\psi'/R_\psi\) and give identical classical stationarity equations for the fields. The orientation-preserving identification also preserves determinant winding for invertible loops. Thus a fixed \(\ell\) admits every positive \(R_\psi'\). Constraints tying the time and circle derivatives, such as holomorphy in fixed units, lie outside these hypotheses. [MM winding comparator](mm_full_theta_psi_winding_decoupling_2026_11.en.md)

<!-- BILINGUAL-UNIT: mm-circle.normalization -->
## Normalization test for circle dynamics

Add to the normalized comparator a test term quadratic in the circle derivative, with a free constant coefficient \(\beta\) and a form \(\mathcal Q_\Theta\) independent of the radius. With \(\theta=\psi/R_\psi\),

\[
\beta\,\mathcal Q_\Theta(\partial_\psi\Theta,\partial_\psi\Theta)
=\frac{\beta}{R_\psi^2}\,
\mathcal Q_\Theta(\partial_\theta\Theta,\partial_\theta\Theta),\qquad
(R_\psi,\beta)\mapsto(\lambda R_\psi,\lambda^2\beta),\quad\lambda>0.
\]

This rescaling preserves the normalized test action. Even that derivative term requires an independent normalization to identify the radius. A physical relation between \(R_\psi\) and \(\ell\) requires additional input from the selected dynamics.

<!-- BILINGUAL-UNIT: mm-circle.verification -->
## Verification

Lean 4.33.1 checks the finite entry proof for the three boosts in `formal/lean/UBT/GR/MMInternalCircle.lean`. Six exact SymPy 1.14.0 tests in `tests/test_mm_internal_circle.py` check rank in the vector and Clifford representations for both signs, a noncommuting curvature pullback and a normalized Fourier gradient. The group-level inference and the continuum identities are analytic.
