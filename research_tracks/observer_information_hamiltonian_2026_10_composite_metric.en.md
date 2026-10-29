<!-- BILINGUAL-UNIT: composite-metric-degeneracy -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Composite-metric contraction: Hamiltonian derivation obstruction

<!-- BILINGUAL-UNIT: premises -->
## Canonical premises

In the locked Lorentz sector $E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta\in W_L$ and $\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}\mathbf1$. Set $\langle X,Y\rangle_\sharp=\operatorname{Sc}\tfrac12(X^\sharp Y+Y^\sharp X)$ on $W_L$. Assume nondegenerate $g$ and the **same** pairing in the kinetic action. The two-sided derivative is $D_\mu\Theta=\partial_\mu\Theta+A_\mu\Theta-\Theta B_\mu$; the previously audited pure-pair representative is a special case. Do not vary the metric independently when evaluating the full composite theory.

<!-- BILINGUAL-UNIT: identity -->
## Exact contraction identity

$\langle D_\mu\Theta,D_\nu\Theta\rangle_\sharp=\mathcal N_0g_{\mu\nu}$, hence
$$g^{\mu\nu}\langle D_\mu\Theta,D_\nu\Theta\rangle_\sharp=4\mathcal N_0.$$
Thus for the assumed $\frac12\sqrt{-g}$ kinetic normalization,
$$S_{\rm kin}=2\mathcal N_0\int d^4x\sqrt{-g}.$$
This is a volume/cosmological-type term **after substitution of the composite metric**. It remains derivative-dependent through $\sqrt{-g(D\Theta)}$; it is neither constant as a functional nor proof that all physical modes vanish. It does show that a free eight-scalar Legendre transform does **not** follow from this canonical metric-identical kinetic pairing. The identity is a direct algebraic contraction; whether the full canonical action uses exactly this pairing and normalization in every branch must be checked before applying it globally.

<!-- BILINGUAL-UNIT: action -->
## Consequence for the Hamiltonian problem

For $S=S_{\rm HP}[e(D\Theta),\omega(D\Theta,\ldots)]+S_{\rm kin}+S_V$, a valid Hamiltonian requires a chosen time foliation, a declared independent-variable/connection scheme, all composite variations, boundary terms and a Dirac--Bergmann constraint analysis. $S_{\rm HP}$ can introduce higher derivatives through composite geometry; treating $e,\omega$ as independent gives a **different** phase-space problem unless equivalence is proved. Lorentz symmetry and no-superluminal propagation restrict allowed terms but do not determine unique coupling coefficients. Observer information has not yet selected a unique fundamental Hamiltonian.

<!-- BILINGUAL-UNIT: tests -->
## Verification and next steps

1. Audit the exact pairing and normalization against `canonical/THEORY/canonical/canonical_action.tex` and the existing action audit.
2. Check the contraction symbolically and then formally: **CAS-PENDING; LEAN-PENDING**.
3. Compute the principal symbol and constraint/Hessian rank of the composite action near an admissible background.
4. Couple a causally smeared detector to observables of the **single** canonical $\Theta$ rather than introduce new fundamental fields.
5. Derive or rule out an information-based selection of residual couplings and compare the double-slit visibility to standard quantum theory.
6. **BILINGUAL-SEMANTICS-PENDING:** independent equivalence review required before merging.

**Status:** exact conditional algebraic identity; physical interpretation and full Hamiltonian **OPEN**.
