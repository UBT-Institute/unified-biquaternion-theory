<!-- BILINGUAL-UNIT: lorentz_slice_two_sided_connection_classification -->
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


# Classification of two-sided connections preserving the locked Lorentz slice

**Exact algebraic connection theorem, 2026-10-25. NOT a torsion-selector theorem, fundamental action, or full implicit Theta solution.** Continuation of merged #761.

Let the canonical two-sided derivative on a matrix carrier be D_mu X=partial_mu X+A_mu X-X B_mu. For every anti-Hermitian X∈W_L=i Herm_2, require D_mu X to be anti-Hermitian when partial_mu X is. This is equivalent to
\[
(A_\mu+B_\mu^\dagger)X=X(A_\mu^\dagger+B_\mu),\quad \forall X\in i Herm_2.
\]
Setting X=iI forces A+B†=A†+B=:C Hermitian; commuting with every Hermitian X then forces C=r I with real r. Therefore the necessary and sufficient condition is
\[
\boxed{B_\mu=-A_\mu^\dagger+r_\mu I,\quad r_\mu\in\mathbb R.}
\]
Write A=Ahat+alpha I, tr Ahat=0. Then
\[
D_\mu X=\partial_\mu X+Ahat_\mu X+X Ahat_\mu^\dagger+\kappa_\mu X,\quad \kappa_\mu=2\,Re(alpha_\mu)-r_\mu.
\]
The sl2(C) term is the Lorentz vector connection; κ is a real Weyl-dilatation one-form. For the locked sharp central metric and fixed internal Minkowski tensor, metric compatibility of the induced frame connection requires κ=0: the infinitesimal determinant variation for Hermitian Y=-iX is δ det Y=2κ det Y when the sl2 term acts (its trace is zero). Thus modulo common central cancellation, the **metric-compatible induced Lorentz derivative** is exactly
\[
D_\mu X=\partial_\mu X+Ahat_\mu X+X Ahat_\mu^\dagger,
\]
with no restriction that Ahat or its torsion be zero.

This is a **classification of possible action on Lorentz-slice matrix values**. It does not say every fundamental Theta must transform as a Lorentz vector or that the composite two-sided B computed from omega has this form in all allowed gauges. If the Θ carrier representation and tetrad representation differ, the intertwiner/mismatch term from #761 remains to be checked. It also doesn't pick the 24 torsion components, choose a kinetic pairing, imply GR dynamics, or deliver H_UBT. The true remaining action gate is proving that an admissible composite torsion equation fixes Ahat[Theta] and that the resulting reduced variational Hessian and constraints are physically stable.

Symbolic verification uses a generic traceless Ahat and real κ on a general anti-Hermitian X and tests preservation of the Lorentz slice, and shows the determinant scaling of a Hermitian Y.
