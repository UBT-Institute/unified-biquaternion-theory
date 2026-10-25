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

# Algebraic torsion potential cannot source torsion by itself

**Conditional auxiliary-field variational theorem (2026-10-25). NOT a Theta-only UBT action or Hamiltonian.** Builds on torsion decomposition #744 and canonical composite metric with torsionful curved branch.

At a fixed regular Lorentz tetrad decompose metric-compatible torsion irreducibly T=V(t)+A(a)+Q, dimensions 4+4+16. Treat these 24 components **for this diagnostic only** as independent auxiliary variations. Consider a parity-even diagonal algebraic torsion density
\[
{\cal L}_{\mathrm{aux}}=e\left(\frac{\alpha}{2}t_\mu t^\mu+
\frac{\beta}{2}a_\mu a^\mu+
\frac{\gamma}{2}Q_{\lambda\mu\nu}Q^{\lambda\mu\nu}\right),
\]
with nonzero real \(\alpha,\beta,\gamma\), no linear source, no torsion derivatives, no mixed curvature terms, and e fixed in the torsion variation. Variations within the independent irreducible subspaces give exactly
\[
\alpha t^\mu=0,\quad\beta a^\mu=0,\quad\gamma Q^{\lambda\mu\nu}=0.
\]
Nondegeneracy of the Lorentz metric implies T=0 at stationary points. This is a local algebraic critical-point statement, **not** positivity or stability: the Lorentz signature makes the quadratic form indefinite generally.

With linear derived currents \({\cal L}_{source}=e(J_t^\mu t_\mu+J_a^\mu a_\mu+J_Q^{\lambda\mu\nu}Q_{\lambda\mu\nu})\), formal auxiliary extremization instead gives t=-J_t/alpha, a=-J_a/beta, Q=-J_Q/gamma. This is a *formula conditional on such derived sources*, NOT their derivation from Theta. Degenerate coefficients leave flat directions; torsion-derivative/curvature coupling can give differential torsion equations; a constrained implicit composite map means these variations are **not** independent and this theorem cannot be applied unchanged.

**UBT implication.** If the curved composite representation needs nonzero torsion, the simplest source-free nondegenerate quadratic algebraic torsion density is not enough to produce it. A legitimate fundamental single-Theta action would need to provide a nonzero induced torsion source/coupling or an entirely different variational structure; adding an auxiliary torsion potential does not count as deriving S_UBT[Theta]. Constraint closure, physical symplectic form, energy and GR limit remain unproved.

This test specifically targets a restricted ansatz. It does not prove all torsion-only invariants are forbidden or select coefficients. Nor does it independently establish physical torsion necessity in all curved branches (the canonical no-go is for its specific torsion-free connection pair).

Reproducer: research_tracks/action_selection/tests/test_quadratic_torsion_selector.py.
