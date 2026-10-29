<!-- BILINGUAL-UNIT: vector_trace_shear_contortion_gate -->
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


# Irreducible-contortion screening: vector trace versus transverse shear

**2026-10-25 — conditional pointwise algebraic result, C-tier.** Uses the non-null Gaussian UBT reconstruction with symmetric W and W_(mu nu) V^nu=0. No fundamental UBT spin-current, action or Hamiltonian is selected.

## Pure vector trace

Define the metric-compatible pure-vector contortion representative (normalization absorbed into t)
```
K^(v)_(a m b) = g_(a m) t_b - g_(b m) t_a.
```
It is antisymmetric under a<->b. Its contraction is
```
Q_(m a) = K^(v)_(a m b) V^b
        = g_(a m) (t.V) - V_m t_a.
```
Symmetry Q_(m a)=Q_(a m) forces V_m t_a - V_a t_m=0, hence t_a=c V_a at any point with nonzero V. Then
```
Q_(m a) = c [ V^2 g_(m a) - V_m V_a ].
```
This is automatically V-transverse and is an isotropic multiple of the induced metric perpendicular to V. Consequently a pure-vector trace contortion cannot reconstruct nonzero transverse tracefree shear of W.

## Pure axial

A totally antisymmetric K gives Q_(m a) antisymmetric, so its symmetric contraction vanishes. To equal symmetric W, it must have Q=0 and W=0. Including axial and vector *only* does not change the symmetric piece: the vector piece still gives just isotropic W; cancellation of antisymmetric parts cannot create tracefree shear.

## Transverse symmetric decomposition

At non-null V, let P_(m n)=g_(m n)-V_m V_n/V^2. Since W is symmetric and W_(m n)V^n=0, it is a symmetric bilinear form on the three-dimensional V-perpendicular space, hence 6 independent algebraic components. Decompose uniquely
```
w=(1/3) P^(m n) W_(m n),
W_(m n) = w P_(m n) + Sigma_(m n),
P^(m n) Sigma_(m n)=0, Sigma_(m n) V^n=0.
```
The isotropic piece has dimension 1; transverse symmetric tracefree Sigma has dimension 5. Pure vector contortion can produce only w P, with c=w/V^2. Nonzero Sigma necessarily requires non-vector, non-axial (mixed tensor) contortion when decomposed into the standard three torsion irreducible sectors (4 trace +4 axial +16 tensor), assuming ordinary metric-compatible torsion and these conventions.

This is a *necessary condition*, not a proof that a particular Theta-derived mixed spin current supplies every Sigma or that a Cartan source obeys the full reconstruction. The antisymmetric components of Q must also vanish. The 12-dimensional kernel of K -> KV remains: counting 6 target symmetric transverse components does not remove the 12 kernel directions.

## Required next test

Compute the actual Theta pure-pair fixed-background spin-current tensor with its index conventions. Project the associated **conditional** Cartan solution K_Cartan on
(1) Q_[m a]=0,
(2) P-trace of Q = w,
(3) symmetric tracefree transverse component equals Sigma.
Then verify the 12 transverse-kernel variables are determined by the same legitimate variational equations rather than set to zero by hand. Do not infer a unique fundamental Hamiltonian from this algebraic filter.

Sources: canonical/CANONICAL_DEFINITIONS.md, section 3; research_tracks/action_selection/{palatini_cartan_compatibility_gate,axial_cartan_symmetric_W_no_go,composite_contortion_kernel}.en.md.
