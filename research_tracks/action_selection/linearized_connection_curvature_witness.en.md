<!-- BILINGUAL-UNIT: linearized_connection_curvature_witness -->
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


# Curved linearized tetrad witness versus composite-connection dynamics

**Exact conditional kinematic witness (2026-10-25), not a propagating graviton or Hamiltonian.** Complements draft #739 and merged #740. Uses canonical D_mu Theta=partial_mu Theta+A_mu Theta-Theta B_mu (research plus-right notation has reversed B sign).

On a flat Lorentz background Ebar_mu=u_mu and affine Thetabar=Theta_*+sqrt(N0) x^mu u_mu, choose Theta_* invertible (e.g. a nonzero real scalar matrix cI) and restrict to an open neighborhood where det(Thetabar)≠0. Linearizing Theta=Thetabar+epsilon phi, A=epsilon a, B=epsilon b gives
\[
\delta E_\mu=N_0^{-1/2}(\partial_\mu\phi+a_\mu\bar\Theta-\bar\Theta b_\mu).
\]
Thus for ANY prescribed smooth Lorentz-slice δE_mu on this patch, an **algebraic auxiliary representer** is
\[
\boxed{b_\mu=0,\qquad a_\mu=(\sqrt{N_0}\delta E_\mu-\partial_\mu\phi)\bar\Theta^{-1}.}
\]
This is only surjectivity of an *unconstrained algebraic* connection perturbation: no claim that it follows from the locked composite metric-compatible reconstruction, no independent propagating connection, and no dynamical solution. In particular, choosing a_mu freely cannot be counted as a derived graviton.

Explicit witness: work at N0=1 and background u_0=iI, u_j=e_j with quaternion e_j²=-I, e_j sharp=-e_j. Choose phi=0 and
\[
\delta E_1=\tfrac12 f(t)e_1,\quad \delta E_2=-\tfrac12 f(t)e_2,\quad \delta E_0=\delta E_3=0;
\quad a_\mu=\delta E_\mu\bar\Theta^{-1},\ b_\mu=0.
\]
From the canonical central tetrad metric, to first order \(h_{11}=f(t), h_{22}=-f(t)\), all other h vanish. Its linearized curvature obeys
\[
R^{(1)}_{0101}=-\tfrac12 f''(t),\qquad R^{(1)}_{0202}=+\tfrac12 f''(t).
\]
For f=t² these components are nonzero. Hence allowing arbitrary perturbations of the connection can evade the frozen-connection pure-gauge statement in #739 **at the algebraic level**. This does NOT establish admissibility in full UBT: generic constructed a_mu may fail metric-compatible composite-connection relation and field equations. Also f=t² is not a vacuum traveling gravitational wave: linearized vacuum Einstein equations must be separately tested; the example only proves nonzero Riemann curvature.

**Required decisive gate:** derive the linearized actual composite map δA[phi,δE,T], δB[phi,δE,T] from the canonical connection reconstruction (including torsion equation), insert it into the tetrad equation, solve its linearized constraints, compute gauge-invariant R^(1) and the kinetic Hessian/characteristics. Until then no Hamiltonian selection or graviton mode count is justified.
