<!-- BILINGUAL-UNIT: spin-source-accessible-rank-2026-11-16 -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Restricted rank and preexisting comparator, not full Theta dynamics.
UBT-AI-PROVENANCE-END -->
# Restricted spin-current rank and identifiable torsion response

<!-- UNIT: scope -->
## Scope and existing evidence
[EXACT RESTRICTED / FULL UBT OPEN] This note compares existing results in research_tracks/action_selection/vector_kinetic_spin_current_cartan_gate.en.md, vector_pair_spin_current_shear_benchmark.en.md, fixed_theta_torsion_response_rank.en.md, physics_closure_spin_source_2026_10.en.md, and tools/verify_canonical_spin_current.py. It does not rename existing work as new.

<!-- UNIT: rank -->
## Distinct ranks and exact calculation
J_(mu ab)[X] = e_(mu a) X_b - e_(mu b) X_a
C:R^4 -> R^24; rank(C)=4; ker(C)=0; codimension(image C)=20
J^a_(a b)=3 X_b
H: symmetric invertible 24x24 algebraic contortion Hessian
L_eff(X)=-1/2 X^T (C^T H^(-1) C) X
Q=C^T H^(-1) C is 4x4 symmetric (at most 10 entries)
Holst torsion-square comparator: beta=b+zeta
(b,zeta)->(b+delta,zeta-delta) changes bulk action by an exact Nieh-Yan density

For the fixed-tetrad Lorentz-vector kinetic comparator, the 24 source components depend linearly on just four independent real X components. An exact 24-by-4 integer calculation gives rank four, zero kernel and 20 independent source-space restrictions. The source is pure vector trace in the stated basis. By contrast, the map of all 24 Lorentz-connection components acting on a fixed non-null X in four jet directions has rank 12 and a 12-dimensional stabilizer kernel: that is a DIFFERENT map. Neither rank is a physical propagation count. The pre-existing canonical pure-pair fixed-background verifier independently showed that the source depends only on four anti-Hermitian real components of generic eight-real-component Theta, and that their joint map is injective. These are fixed-background statements, not full composite equations.

<!-- UNIT: observables -->
## Restricted-source identifiability
If contortion is auxiliary with invertible symmetric H and accessible current J=CX, the observable contact form from varying X is determined by Q=C^T H^(-1) C, not the entire 24x24 matrix H. Q has at most ten symmetric entries whereas H has 300, but these are formal matrix dimensions, not counts of UBT parameters. Changes in H invisible to Q need not be gauge: independent torsion observables, additional sources, interactions or constraints can distinguish them. The true on-shell source manifold must be derived, not assumed.

<!-- UNIT: existing -->
## An already-established bulk coefficient redundancy
The existing sourced Holst-plus-torsion-square effective comparator in research_tracks/action_selection/physics_closure_spin_source_2026_10.en.md proves that beta=b+zeta is the only bulk combination for fixed boundary data, since changing b and zeta with opposite shifts adds an exact Nieh-Yan density. This is a genuine restricted bulk action equivalence, stronger than source insensitivity. It does not imply a local gauge transformation or quantum/boundary equivalence of full UBT.

<!-- UNIT: next -->
## Actual remaining research gate
Calculate the finalized paired biquaternionic source with full metric and connection chain rule, determine the physical on-shell accessible sources, and use the actual 24x24 contortion Hessian to compute Q and its coupling Jacobian. Only then determine the number of UBT observable constants. The full constrained Hamiltonian/spin-2 sector, CI, Lean and independent bilingual semantic verification remain pending. Do not merge or promote to canonical.
