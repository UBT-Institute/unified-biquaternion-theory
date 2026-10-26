<!-- BILINGUAL-UNIT: vector_pair_spin_current_shear_benchmark -->
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


# Fixed-tetrad pure-pair Lorentz current: vector-source benchmark

**2026-10-25; conditional benchmark, not the complete canonical Theta spin-current derivation.**

## Assumptions and field carriers

On the *real Lorentz vector slice only*, write Theta=sqrt(N0) V^a u_a and D_mu Theta=sqrt(N0) e_mu^a u_a. Hold e and the volume measure fixed while varying a metric-compatible Lorentz connection omega_mu^{ab}=-omega_mu^{ba}. Choose the quadratic vector pairing
```
L_kin = c sqrt(-g) g^{mu nu} eta_ab (D_mu V^a)(D_nu V^b)
```
with an arbitrary overall constant c (including sign convention). Let D_mu V^a=partial_mu V^a+omega_mu^a{}_b V^b. This is a benchmark action, not shown to be the unique UBT action or the repository's exact biquaternionic pure-pair pairing. Varying at fixed e, V and g:
```
delta L_kin = 2c sqrt(-g) g^{mu nu} (D_nu V)_a V_b delta omega_mu^{ab}
            = c sqrt(-g) J^mu_ab delta omega_mu^{ab}
J^mu_ab = 2 (D^mu V)_[a V_b].
```
At the concurrent-vector reconstruction D_mu V^a=e_mu^a,
```
J^mu_ab = 2 e^{mu}_[a V_b].
```
In spacetime indices this is of pure **vector-trace type** (up to overall coefficient): J_{rho ab} proportional to g_{rho a} V_b - g_{rho b} V_a. A parity-even minimal Hilbert-Palatini Cartan map respects the Lorentz-irreducible trace / axial / tensor decomposition and is invertible, so this **benchmark source** produces pure-vector contortion, not mixed tracefree tensor contortion. Consequently its symmetric transverse projection (K_Cartan V)_{<mu nu>} vanishes.

If the demanded Gaussian reconstruction has Sigma_{mu nu}=W_{<mu nu>} != 0, then the minimal parity-even HP + vector-pair kinetic **benchmark** fails its shear compatibility gate. This is conditional on all stated assumptions. The scalar trace may also be mismatched; it has not been normalized or checked against the remaining image constraints.

## Why this is not yet a no-go for UBT

- The locked biquaternion Theta is eight-real-dimensional and its spinorial carrier, Hermitian/complex pairing, psi dependencies and any relative left/right connection components are not identified with the simple vector pairing above.
- The independent omega variation of HP is not automatically equivalent to varying a composite omega[Theta].
- Treating the metric as fixed during omega variation differs from its canonical definition g(DTheta,DTheta); the full composite variation includes induced delta g and induced delta e, which may add tensor structures.
- This current is not shown to coincide with the particular *existing fixed-background pure-pair spin current* cited in canonical/CANONICAL_DEFINITIONS.md; locate and compare its exact definition before promoting any UBT claim.
- Even if mixed source is nonzero, the full 12 transverse kernel, constraints and fundamental Hamiltonian remain to be determined.

## Next test

Work with the exact locked sharp-central metric, vary a fully specified Theta-only functional including delta E, delta g, delta omega[Theta], and derive the Lorentz spin-source irreducibles. Check shear projection and all reconstruction equations with fixed normalization, then test local constraint closure. Do not add new axioms or silently fix transverse kernel.
