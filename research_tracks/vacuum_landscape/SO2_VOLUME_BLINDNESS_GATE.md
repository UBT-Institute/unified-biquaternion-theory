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

# Exact residual-connection blindness of first-jet tetrad volume candidate

**Exact conditional no-selection lemma — 2026-10-26.** Within the already specified two-carrier real Lorentz lift, let v,w be prescribed and E_mu=N0^(-1/2)D_mu v be a nondegenerate tetrad, D_mu w=0. Suppose omega'_mu=omega_mu+alpha_mu J, with Jv=Jw=0. Then

D'_mu v=D_mu v, D'_mu w=D_mu w, E'_mu=E_mu, g[E']=g[E], det E'=det E

pointwise for arbitrary one-form alpha. Therefore every local trial density L(E,g,v,w) without separate omega, torsion, curvature, higher omega-dependent derivatives or explicit connection coupling is completely independent of alpha, including a constant-volume candidate \(S_{vol}=c\int |\det E|d^4x\). Its variational derivative with respect to alpha is identically zero, and no equation to select the residual connection arises from this restricted trial.

This does **not** mean alpha is a gauge field; its curvature can change (PR #787). It means these particular restricted densities are blind to alpha. It also does **not** establish the full eight-real single-Theta action: the two-sided representation, ψ dependence, matter couplings and reconstructed omega[Theta] might enter nontrivially.

Corollary for the main program: deriving a Hamiltonian for the pure-volume first-jet candidate alone cannot close residual torsion selection. A legitimate microscopic selector must contain further dependence or constraints, derived from the single selected action rather than postulated to close a gap. To identify it, compute the full off-slice Theta variation, trace any omega-dependence, and run Dirac reduction. No vacuum count or string duality follows.

Reproduction: tests/test_so2_volume_blindness.py.
