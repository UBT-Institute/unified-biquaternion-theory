<!-- BILINGUAL-UNIT: gr-source-obstruction-2026-11-16 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional deduction; not a canonical UBT theorem.
UBT-AI-PROVENANCE-END
-->
# Spin-source obstruction under quadratic torsion deformations

<!-- UNIT: scope -->
## Scope [RESEARCH / CONDITIONAL]
This analysis compares the single-physical-connection torsion branch B against auxiliary split-jet branch A. Canonical UBT definitions remain frozen. It complements, without overriding, the canonical GAP-10T-FLAT-NOGO and GAP-10T-MINIMAL-ONE-CONNECTION-GR results. Full Theta composite variation has not been established.

<!-- UNIT: derivation -->
## Algebraic elimination
Consider 24 algebraic real contortion components K^A and remaining fields u. Assume a local action quadratic in K, with symmetric M, no independent derivatives of K after integration by parts, and J independent of K:
```text
S[K;u] = S0[u] + integral sqrt(-g) { J_A[u] K^A + (1/2) K^A M_AB[u] K^B }
delta S / delta K^A = sqrt(-g) (J_A + M_AB K^B)
K_* = - (M^(-1))^AB J_B   [only when M invertible]
S_eff = S0 - (1/2) integral sqrt(-g) J_A (M^(-1))^AB J_B
(delta S / delta K^A)|_{K=0} = sqrt(-g) J_A
```
The on-shell source-contact term is exact for this quadratic truncation. If M is singular, separate constraints/null vectors are required; inverse elimination is invalid. The complete coupled kinetic Hessian and its stability do not follow from invertibility alone.

<!-- UNIT: lemma -->
## Conditional source-obstruction lemma
At K=0, the torsion/connection variation depends on J and **not** on M. Hence, at a fixed background u0 with J[u0] nonzero, no modification solely of the quadratic torsion coefficients M[u0] can turn K=0 into a stationary solution. A zero-torsion solution requires J[u0]=0 or changes to the linear source / background / variables, or a different variational problem. Singular M does not cure a nonzero linear first variation at K=0. This is an elementary consequence of quadratic polynomial differentiation, not a new universal no-go theorem.

<!-- UNIT: canonical -->
## Relation to the canonical affine branch
The repository establishes a nonzero spin current for almost all points of a specified flat affine pure-pair representative under *fixed-background effective Palatini variation*. Under exactly those assumptions, tuning quadratic torsion-square coefficients cannot restore a torsion-free flat stationary solution. This does not rule out curved or nonzero-torsion backgrounds, a pure composite-Theta theory, or a different physical vacuum after backreaction. Recompute the chain-rule current before applying this lemma to the full theory.

<!-- UNIT: decision -->
## A/B decision
A: The split-jet construction supplies local representability but the known surjective auxiliary constraint does not select a metric, so its physical principle remains open.
B: Keeping one physical torsionful connection avoids the auxiliary split, but requires an explicitly on-shell curved or torsionful vacuum, a computed M and J, and the coupled Dirac/Hamiltonian constraint analysis. A nonzero J on the nominal vacuum is a selection condition, not an automatic disproof of B. Do not demand exactly vanishing physical torsion unless the resulting effective theory predicts it.

<!-- UNIT: verification -->
## Verification/status
An independent exact symbolic toy check of the polynomial identity is included in tools/verify_gr_torsion_source_obstruction_2026_11_16.py; this does not validate canonical Theta sources. Lean, repository CI, bilingual semantic verifier, and full coupled Hessian: PENDING. Do not merge prior to repository-mandated gates.

<!-- UNIT: composite-variation -->
## Chain-rule obstruction in the canonical composite tetrad
For an illustrative functional F[Theta,E,omega] evaluated at E_mu=N0^(-1/2)D_mu^omega Theta, the actual variation at fixed Theta satisfies
```text
delta_omega F_composite =
  (delta F / delta omega)|_(Theta,E) delta omega
 + (delta F / delta E_mu) delta_omega E_mu
delta_omega E_mu = N0^(-1/2) (delta omega_mu) acted on Theta
```
with indices, adjoints and the paired left/right generators restored for the exact UBT representation. Thus the *fixed-E* current is not automatically the complete source. Even if an effective Palatini source is nonzero, a chain-rule term could in principle modify the full stationarity equation. Conversely, claiming a cancellation without computing the full derivative is unjustified. The source-obstruction lemma must only be applied after this distinction is resolved.
