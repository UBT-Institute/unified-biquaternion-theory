<!-- BILINGUAL-UNIT: pr750-rebase-gate-snapshot -->
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


# PR #750 merge/rebase gate — 2026-10-26

Do not merge this draft into `master` without conflict reconciliation and rerun of required workflows.

## GitHub snapshot
- Head f8dfc290710b9e94c76b2d13e280b53c3c4e1904; base `master` as seen at inspection.
- Head is **182 commits ahead and 42 behind** master from merge base b837cb7cab06d46841b0715c0fc48a3f3a77b1d5.
- GitHub PR mergeable=false; PR draft=true; 343 files changed according to PR metadata.
- GitHub compare returns only **300 entries** for the old branch file list, so the following overlap list is **incomplete**, not an exhaustive reconciliation.

## Currently detected potentially overlapping source paths
- axial_phase_mass_gate (.en/.cs)
- conditional_axial_torsion_from_dirac_carrier (.en/.cs)
- gradient_hamiltonian_closure_benchmark (.en/.cs)
- irreducible_torsion_selection.en.md
- linearized_connection_curvature_witness (.en/.cs)
- torsion_connection_rank (.en/.cs)
- ultralocal_constraint_closure (.en/.cs)
- matching research_tracks/action_selection/tests test files.

For the files above, preserve subsequent master results and scientific claim boundaries unless a per-hunk manual review justifies otherwise. Merely choosing the older integrated branch is not scientifically safe.

## CI snapshot for this exact head
Passing: Theory Invariants, Lean theorem verification, Physics Laws CI, Hamiltonian charge and torsion, and many additional focused gates. Failing: Verify Lorentz Invariance, Bilingual document parity, Repo Integrity Gate, Build all LaTeX PDFs, Build textbook PDF. These failures require inspecting job logs and must not be labeled fixed before a new completed run.

## Merge exit criteria
1. Resolve overlap of changed content against latest master, preserving canonical single-action registry `DEFINED_FAMILY_NOT_FINALIZED`.
2. Determine whether old PR branches are already integrated in content before merging independently; avoid duplicative changes.
3. Run focused research verifiers, Python pytest, Lean, bilingual parity, repository integrity/provenance, and textbook/PDF jobs.
4. Publish the residual-failure list if some unrelated baseline workflows fail and receive explicit documented approval before overriding them.
5. Only mark ready and merge when current GitHub mergeability and protection checks permit it.

This file documents a current block; it is not evidence that the branch was rebased or merged.
