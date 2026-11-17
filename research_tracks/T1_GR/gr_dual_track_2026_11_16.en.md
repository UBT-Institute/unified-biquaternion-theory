<!-- BILINGUAL-UNIT: gr-dual-track-2026-11-16 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional research, not a canonical theorem.
UBT-AI-PROVENANCE-END
-->
# Dual-track GR completion: architecture A versus B

<!-- UNIT: status -->
## Scope
[RESEARCH / CONDITIONAL] Canonical single-Theta covariant tetrad and central sharp metric are unchanged. The 4x4 biquaternion tensor remains an exploratory alternative, not a canonical replacement. Prior results are in canonical/gr_closure/gap_10t_minimal_one_connection_gr_no_go.tex, gap_10t_split_jet_auxiliary_completion.tex, gap_10t_palatini_torsion_dynamics.tex, and gap_10d_induced_gravity_endgame.tex.

<!-- UNIT: definitions -->
## Common equations
```text
E_mu = N0^(-1/2) D_mu Theta
A: omega_jet = omega_LC(E) + K_jet; omega_phys = omega_LC(E)
B: omega_jet = omega_phys = omega_LC(E) + K
S(K) = S0 + integral [ 1/2 K^A M_AB K^B + J_A K^A ]
M_AB K^B = -J_A
S_eff = S0 - 1/2 integral J_A (M^(-1))^AB J_B
```
The effective expression assumes a genuinely algebraic symmetric invertible torsion Hessian M and properly includes the dependence of M and J on remaining fields. It is not a proof of the complete composite-Theta equations.

<!-- UNIT: A -->
## A: Auxiliary jet versus physical Levi-Civita connection
The existing split-jet right inverse represents an arbitrary prescribed tetrad locally for a non-null Lorentz-real Theta projection. The existing auxiliary multiplier action gives nonpropagating jet auxiliaries, but the constraint is surjective and selects no tetrad. Thus A is an embedding/reformulation, not a fundamental derivation, unless an independent principle selects E from Theta without inserting a free gravitational action. Gates: exact composite variation; auxiliary selection; full constraint count; two GR tensor polarizations; either new prediction or explicit equivalence-only claim.

<!-- UNIT: B -->
## B: Single physical torsionful connection
The same omega appears in D Theta and in physical curvature. The 24 torsion components split into vector trace (4), axial trace (4), and tensor part (16). In a metric-compatible parity-even first-order action linear in curvature and quadratic in torsion, the connection equation is algebraic when its full coefficient matrix M is invertible. Singular couplings require separate constraint treatment. Eliminating torsion generates local spin-current contact terms, not propagating torsion by default. The canonical minimal one-connection no-go and the nonzero affine Theta spin source prevent declaring either generic torsion-free GR or a flat torsion-free vacuum without checking the complete field equations. Gates: compute the exact paired Theta spin source, find an on-shell background, determine M in an irreducible basis, eliminate K with all composite variations, check coupled physical Hessian and observational GR limit.

<!-- UNIT: choice -->
## Decision rule and information principle
Do not preferentially select A merely because it fits prescribed GR geometries. Choose between A and B using non-ad-hoc constraints derived from biquaternionic product, local covariance, relational information and a complete physical degree-of-freedom audit. None of these presently fixes the Einstein coefficient or uniquely selects the action. Preserve the GR-before-Jacobi-theta/QM ordering.

<!-- UNIT: verification -->
## Verification status
No new theorem is asserted. Lean, full CI, independent bilingual semantic checking, and coupled canonical Hamiltonian analysis are pending. Do not merge until required repository gates pass.
