<!-- BILINGUAL-UNIT: cartans_theta_integrability -->
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


# Exact Cartan integrability constraint for the pure Lorentz-lift Theta branch

**Exact conditional geometric identity, 2026-10-25; not a fundamental torsion dynamics or Hamiltonian.** Refines #758/#759.

Assume the real Lorentz-valued representative v^a of the single field Theta transforms in the Lorentz vector representation; the locked tetrad is identified with its **same** vector-covariant derivative:
\[
e^a=N_0^{-1/2}Dv^a=N_0^{-1/2}(dv^a+\omega^a{}_b v^b).
\]
This is a restricted *pure spin-lift* subbranch, not the most general two-sided biquaternionic DTheta with a relative left/right connection. N0 is constant and positive. Define the torsion and curvature two-forms using the **same** Lorentz connection,
\[
T^a=De^a=de^a+\omega^a{}_b\wedge e^b,\quad R^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b.
\]
Apply the curvature identity \(D^2v^a=R^a{}_bv^b\) to derive **without imposing zero connection**
\[
\boxed{\sqrt{N_0}\,T^a=R^a{}_b v^b.}
\]
This is a **first-jet integrability restriction** on any putative (v,e,omega) solution; it does NOT provide an evolution equation for omega or fix all its torsion components. If R=0, T=0 in this restricted exact-covariant-gradient branch, even though general metric-compatible R=0 connections can have T≠0. Hence the purely geometric witness in #758, which had flat spin curvature and nonzero torsion, cannot be promoted to a single-Theta solution of the restricted ansatz. This corrects the relevant scope, not the Bianchi identity counterexample itself.

Conversely the relation alone is not sufficient to find v globally from a prescribed tetrad and connection, nor to prove existence/nondegeneracy of a canonical curved solution. Its count is at most 24 scalar component conditions, but both sides depend on omega and e and their spacetime derivatives; do not count it as 24 new independent equations or an action selector. The first Bianchi identity DT=R∧e then follows from differentiating this relation together with DR=0 and Dv=√N0 e; thus it adds no independent dynamics.

In general two-sided UBT, \([D_\mu,D_\nu]\Theta=F^L_{\mu\nu}\Theta-\Theta F^R_{\mu\nu}\) in canonical minus-right-B convention. Unless this operator is shown equivalent to Lorentz curvature acting on the vector v, do **not** use the boxed formula unmodified. Any relative connection produces additional representation-dependent integrability contributions. The primary research task is to derive the actual two-sided representation and a dynamical torsion selector from the single Theta action, then perform the full Hamiltonian constraint analysis.

Regression: test_cartans_theta_integrability.py verifies D[Dv]=Rv for a noncommuting nonconstant connection and nonconstant v without setting omega=0.
