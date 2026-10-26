<!-- BILINGUAL-UNIT: composite_metric_kinetic_volume_identity -->
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


# Composite metric variation: vector kinetic contraction collapses to volume

**2026-10-25 — exact conditional Lorentz-vector-slice identity, C-tier. Not a derivation of the UBT action.**

## Locked geometry and explicitly chosen benchmark pairing

On the Lorentz-vector carrier of the canonical local construction take
```
E_mu^a = N0^(-1/2) D_mu V^a,
g_mu nu = eta_ab E_mu^a E_nu^b,
det(e) != 0.
```
Choose the trial scalar kinetic density (not assumed to be the full biquaternionic UBT action)
```
L_vec = c sqrt(-g) g^{mu nu} eta_ab (D_mu V^a)(D_nu V^b).
```
The inverse metric is the inverse of the SAME composite metric defined above, not independent background data. Then the contraction is identically
```
g^{mu nu} eta_ab D_mu V^a D_nu V^b
  = N0 g^{mu nu} g_mu nu
  = 4 N0
```
on a nondegenerate 4-dimensional Lorentz patch. Hence exactly
```
L_vec = 4 c N0 sqrt(-g).
```
This is an off-shell algebraic identity on the indicated carrier. It does not yield propagating Theta/graviton equations on its own; it behaves as a volume/cosmological contribution with coefficient fixed by the *chosen* c,N0, not a derived observed cosmological constant. Full Theta, psi, curvature/torsion terms, relative connections and non-identical pairings need not collapse.

## Correct variation including the composite metric

For a fixed V and fixed coordinate patch, under an independent trial Lorentz-connection variation,
```
delta E_mu^a = N0^(-1/2) delta omega_mu^a{}_b V^b,
delta g_mu nu = 2 eta_ab E_(mu^a delta E_nu)^b,
delta sqrt(-g) = (1/2) sqrt(-g) g^{mu nu} delta g_mu nu.
```
Varying the collapsed density gives
```
delta L_vec = 2 c N0 sqrt(-g) g^{mu nu} delta g_mu nu
            = 4 c sqrt(N0) sqrt(-g) g^{mu nu} E_mu a delta omega_nu^a{}_b V^b.
```
The explicit coefficient depends on normalization chosen in the definition of V; the formula as written follows E=N0^-1/2 D V. Thus the induced metric variation must NOT be dropped when deriving a current from L_vec. The fixed-background current from a noncomposite metric is not the same variational problem.

If a connection shift C obeys C^a_(mu b) V^b=0, delta E=delta g=delta L_vec=0. In fact along a finite transverse stabilizer shift preserving the contraction, E and g are exactly unchanged. Thus a functional solely of this metric and its ordinary derivatives cannot determine the 12 transverse kernel variables in the local reconstructed family. A curvature functional R(omega), torsion terms, spinor coupling and higher covariant derivatives can distinguish them.

## Consequences and limits

The volume identity holds only for the explicitly specified vector contraction, on a nondegenerate Lorentz slice, with the inverse metric built from the same D V. It does **not** establish equivalence of the full UBT candidate action to a cosmological term, or physical positivity/constraint closure. An independently varied Palatini omega does not automatically furnish the correct Theta-only Euler-Lagrange equations: composite delta omega[Theta] and delta e[Theta] must be respected. This observation strengthens the selection obstruction for the minimal vector benchmark instead of rescuing its missing transverse mixed source.

**Next gate:** retrieve the exact canonical Theta pure-pair kinetic action (including sharp vs ddagger and field carrier), distinguish its pairing from eta_ab E_mu^a E_nu^b, and compute its full Jacobian with respect to Theta and the *composite* connection. Only then test whether any uncancelled tensor-shear source is present.

Grounding: canonical/CANONICAL_DEFINITIONS.md section 3; research_tracks/action_selection/vector_pair_spin_current_shear_benchmark.en.md; contortion_stabilizer_invisibility.en.md; vector_trace_shear_contortion_gate.en.md.
