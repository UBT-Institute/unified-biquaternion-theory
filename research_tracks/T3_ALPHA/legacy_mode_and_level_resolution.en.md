<!-- BILINGUAL-UNIT: legacy_mode_and_level_resolution -->
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


# Historical mode-count and current-algebra proposals: integration status

PR #335 and PR #373 are merged as historical research proposals reconciled with the current claim ledger. Their original commits and full source files remain reachable through Git ancestry and the immutable references in `reports/open_pr_merge_resolution_2026_10_25.json`. The obsolete top-level consolidation tree and its old status replacements are not restored.

## Algebraic count versus physical loop count

The matrix algebra has the component dimension below. This does not count constrained propagating charged modes. The old calculation additionally assumes a phase representation, an unconstrained scalar kinetic operator and a colour multiplicity. In the current single-field programme these are separate dynamical and representation problems. Multiplying the component count by an assumed colour factor is conditional bookkeeping, not a derivation of a physical loop coefficient. A scalar loop, a Dirac loop and a gauge-boson count cannot be interchanged without specifying their operators, statistics, constraints and normalization.

\[
\mathbb C\otimes\mathbb H\simeq M_2(\mathbb C),\quad
\dim_{\mathbb C}=4,\quad\dim_{\mathbb R}=8,\quad
4\times3=12\quad(N_c=3).
\]

The old first-principles conclusion is therefore not adopted. In particular this integration does not promote the numerical alpha constant or a mode count to a proved microscopic prediction.

## Current algebra level remains unselected

PR #373 compared a trial WZW normalization, absence of a Chern--Simons term in a proposed parity sector and representation-index counting. Its trial normalization relation is shown below. Even when the relation is assumed, an independently undetermined vacuum amplitude leaves the level undetermined. A minimal level in a selected compact model does not select the level of the full complex biquaternion theory. The historical parity and multiplicity premises must be re-established for the finalized action before they can support a physical selection rule.

\[
k_{\rm trial}=8\pi r_{\rm vac}^2.
\]

The old tracking updates are retained as research history, not replacements for the newer canonical action status. The physical action, charged constrained spectrum, level selection and the alpha bridge remain open.

## Verification boundary

`verification/legacy_mode_level_bookkeeping.py` checks component dimension and conditional arithmetic only. Python 3.12 and SymPy 1.14.0 are used in this integration. No loop integral, quantum spectrum or level selector is derived by that script. LEAN-PENDING: these supporting bookkeeping statements have no new compiled Lean proof in this runtime; they are not used to promote a physics claim. The original unvalidated conclusions remain visible in their pinned source commits. English is the translation source; formal content and scope are identical in both editions.
