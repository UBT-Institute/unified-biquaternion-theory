<!-- BILINGUAL-UNIT: dirac_square_spectral_bridge_gate -->
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


# Dirac-square spectral bridge: what the Clifford identity actually fixes

**Status: conditional mathematical audit (2026-10-25), C-tier. Not a derived fundamental UBT action or physical spinor carrier.**

## Conditional standard geometry

Given a Riemannian spin four-manifold, an honest Clifford module S with c(v)c(w)+c(w)c(v)=-2g(v,w), Clifford-compatible spin connection, and a compatible twisting connection, the standard Dirac operator (with sign conventions fixed accordingly) obeys the Lichnerowicz/Weitzenbock identity
```
Dslash^2 = nabla^* nabla + R/4 + (1/2) c(e^mu)c(e^nu) F_twist(mu,nu).
```
This fixes the relative R/4 algebraic coefficient **within those premises**; it does not fix the coefficient multiplying an action integral, the spectrum boundary conditions, or a regularization. Lorentzian continuation needs independent signature and self-adjointness/domain care; do not pass Euclidean heat-kernel or positivity results unmodified into a Lorentzian UBT Hamiltonian.

## Critical carrier obstruction

Locked UBT: E_mu=N0^-1/2 D_mu Theta and E_mu -> S E_mu S^dagger for S in SL(2,C). The central -I acts trivially on this Lorentz-vector tetrad carrier, while on a genuine spinor it acts as -1. Therefore a transformation-equivariant *complex-linear isomorphism* taking this tetrad/vector carrier directly into a single Dirac spinor carrier does not exist with these actions: applying -I would require the same image to be simultaneously unchanged and negated, hence zero. This does not rule out a separate real-linear Weyl-dual map, a different left-acting Theta representation, a spin structure, or a derived spinor bundle; their equivariance and covariant derivative dictionary remain separate theorem gates.

## What does not follow

Writing gamma^mu D_mu Theta is insufficient unless gamma act on an identified Clifford module and D_mu is Clifford compatible. The commutator [D_mu,D_nu]Theta alone need not produce the scalar R/4 term. Even if a Dirac square exists, the identity is an operator decomposition, not a variational selection principle. The geometric spectral action Tr f(Dslash^2/Lambda^2), if proposed, additionally chooses f, Lambda, spectral domain/compactness or regularization, and its heat-kernel coefficients; it is **not** implied by the Clifford identity. No a2 heat coefficient or physical Newton constant is calculated here.

## Suggested decisive tests

1. Specify the actual Theta Lorentz/spin representation separately from E and prove central -I covariance.
2. Build a metric Clifford module and the Omega[Theta] spin lift; verify [nabla_mu,c(e_nu)] compatibility and correct connection/torsion terms.
3. Derive Dslash^2 by direct commutator calculation with the chosen carrier, including torsion and the transverse 12-dimensional contortion kernel.
4. Examine possible kinetic operator principal symbol and compare independently with gauge-reduced metric/Theta modes.
5. Only then compare possible spectral functional candidates and show an axiom-grounded coefficient/regularization selector rather than postulating an action.

**Conclusion:** the R/4 coefficient is conditional standard Clifford geometry; it is not yet a UBT-generated term in a unique action. The first hard missing bridge is the spinor carrier and compatible connection, not an additional guessed R, R^2 or F^2 term.

Sources: canonical/CANONICAL_DEFINITIONS.md (sharp tetrad); research_tracks/action_selection/two_sided_metric_covariance.en.md (vector carrier distinction); canonical/ACTION.en.md (unfinalized action).
