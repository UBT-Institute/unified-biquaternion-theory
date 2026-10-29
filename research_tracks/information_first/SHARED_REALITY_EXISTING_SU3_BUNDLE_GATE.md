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

# Shared reality and the existing UBT SU(3) colour bundle: gluing does not select curvature

**2026-10-26 — integrative exact geometric theorem and action-selection gate.** This is a cross-reference to, NOT a replacement for, the canonical results.

## Existing results are the premises

- `canonical/su3_derivation/su3_stabilizer_exterior_fock.tex`: on V=C-span{I,J,K}, Stab(h,Omega)=SU(3), and Lambda^bullet V=1+3+3bar+1.
- `research_tracks/T2_GAUGE/su3_dynamics_endgame_2026_10.md`: timelike Theta gives Lorentz-equivariant moving rank-three colour bundle E_n; local SU(3) is frame redundancy, not yet QCD dynamics.
- `research_tracks/T2_GAUGE/su3_hidden_local_catch22.md`: minimal hidden-local SU(3) two-derivative route does not automatically generate massless gluons; possible quantum critical routes remain conditional.
- `research_tracks/T2_GAUGE/su3_tree_level_dof_no_go.md`: eight real microscopic local second-order modes cannot become sixteen gluon helicities by invertible tree-level rewrite.
- `research_tracks/T2_GAUGE/su3_positive_kinetic_metric_lock_audit.md`: putative positive colour-triplet kinetic metric collapses under the full Theta-induced metric lock.

## Shared reality = local frame gluing, an exact kinematic requirement

On overlapping patches Ui and Uj in the timelike Theta colour bundle, let an oriented h-orthonormal frame change be hij:Ui∩Uj -> SU(3). Consistency on triple overlaps requires hij hjk hki = I (in a consistent convention); observers calculate identical scalar gauge-invariant predictions. Local connection one-forms Ai must obey

Aj = hij^-1 Ai hij + hij^-1 d hij,

and curvature Fj = hij^-1 Fi hij, Fi=dAi+Ai wedge Ai. Thus local observers can share one covariant reality without sharing numerical components of Ai. For any real g>0, the comparator functional integral Tr(F wedge *F)/g² is compatible with these transformations; its coefficient is not determined by overlap consistency.

**Exact no-selection witness on one trivial patch:** both A=0 (F=0) and A=T x dy for nonzero T∈su3 (F=T dx∧dy) are legitimate globally consistent smooth connections on a trivial colour bundle. They produce different curvature but obey every transition-function consistency law (with hij=I). Therefore observer independence plus local SU(3) frame compatibility alone DOES NOT pick a connection, its curvature or a unique Yang–Mills coupling. This witness concerns geometric compatibility only; no claim is made that both are solutions of the same field equations or arise from a specific Theta.

On a curved moving colour bundle, the induced projection connection P_n d can acquire nonzero curvature due to movement of n; see existing SU3 coset results. Such an induced curvature remains kinematically specified by the bundle embedding only once n and an ambient derivative are specified. No independent physical gluon poles follow.

## Hamiltonian bridge: what would need derivation

Assuming an *independent* SU(3) YM effective action is eventually obtained from the single Theta theory, its canonical structure in flat spacetime (A0 multiplier) would have 8 primary constraints pi0^a=0 and 8 secondary Gauss constraints (D_i E^i)^a=0, both first class under the usual regularity assumptions. Physical local polarizations: 2*8=16. Standard Hamiltonian H_eff = integral[(g²/2) E_i^a E_i^a +(1/4g²)F_ij^a F_ij^a - A_0^a(D_i E^i)^a] up to the declared A0/Poisson conventions. **This is a benchmark conditional effective theory, not a Theta-derived Hamiltonian.** A derived quantum/collective 1PI gluon sector must reproduce Gauss/BRST identities, 2/3/4 point vertices, positive transverse residues, and no gauge-breaking mass; the microscopic Theta constraints and any GR constraints must be checked separately.

## New information-first target
Operational overlap consistency should be tested at the level of parallel transport and Wilson loops, rather than just observer marginal entropies. Wilson-loop trace is invariant under local frame changes and distinguishes the trivial and curved witnesses for suitable finite loops; it is therefore a *shared observable* that requires dynamics to predict its value. Require that Theta's actual quantum dynamics predicts curvature correlators and an effective action for this shared observable, instead of asserting consistency fixes it.

**Status:** compatibility theorem and exact non-selection counterexample. It narrows the missing bridge but leaves S_UBT and H_UBT unresolved. Do not repeat already established algebraic SU(3) constructions as new UBT achievements.

Test: `tests/test_information_su3_observer_gluing.py`.
