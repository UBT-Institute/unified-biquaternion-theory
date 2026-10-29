<!-- BILINGUAL-UNIT: linearized-map -->
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

# Linearized Theta-to-metric map: exact flat-sector obstruction

<!-- BILINGUAL-UNIT: premise -->
## Premise and exact variation
In the locked one-field covariant-tetrad architecture, the full perturbation includes both the field and the two-sided connection; for the covariant derivative defined on the field, its linear variation is shown below. The bilinear pairing is the symmetric sharp/Minkowski pairing on the Lorentz slice.

$$E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta,\qquad g_{\mu\nu}=\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)/\mathbf1.$$
$$\delta E_\mu=\mathcal N_0^{-1/2}(D_\mu\delta\Theta+\delta A_\mu\Theta-\Theta\delta B_\mu),$$
$$\delta g_{\mu\nu}=\langle\delta E_\mu,E_\nu\rangle_\sharp+\langle E_\mu,\delta E_\nu\rangle_\sharp.$$
$$\text{For fixed flat }A=B=0:\quad\delta g_{\mu\nu}=\partial_\mu\xi_\nu+\partial_\nu\xi_\mu,\quad R^{(1)}_{\mu\nu\rho\sigma}=0.$$
$$L_k:\xi_\mu\mapsto k_\mu\xi_\nu+k_\nu\xi_\mu;\qquad\operatorname{rank}L_k=4\quad(k\ne0).$$

<!-- BILINGUAL-UNIT: rank -->
## Fixed-connection submodel and rank
For a flat affine background with fixed zero connection, the metric perturbation has pure-gauge form. In Fourier space its map from four components to ten symmetric metric components has rank four for every nonzero covector $k$. This was checked in SymPy for generic symbolic $k$ and concrete timelike, spacelike and null examples. The linearized Riemann tensor vanishes by commuting partial derivatives. This **does not** prove a rank-four restriction for varying connections.

<!-- BILINGUAL-UNIT: consequence -->
## Consequence and route
The fixed flat-gradient submodel cannot generate physical linearized gravitational waves: it produces only diffeomorphism-type metric perturbations. Allowing $\delta A_\mu,\delta B_\mu$ changes the linear map, but these variations cannot be counted as freely independent physical modes without the canonical connection equations, torsion constraints and a full composite action. Existing split-jet right inverses establish conditional representability, not dynamic propagation or mode count. The next decisive calculation is the linearized *constrained* paired-connection field equations plus their principal symbol and reduced phase-space Hessian. The infrared ADM sector remains conditional.

<!-- BILINGUAL-UNIT: status -->
## Verification
**Exact algebraic identity; SymPy rank check for fixed-connection submodel.** COMPOSITE-LINEARIZATION-OPEN; LEAN-PENDING; BILINGUAL-SEMANTICS-PENDING. No claim of fundamental Hamiltonian closure.
