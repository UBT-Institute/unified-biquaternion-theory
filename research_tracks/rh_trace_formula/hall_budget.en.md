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

# Global matching with an explicit Hall deficit budget

**Status:** `LEAN-PASS`; arithmetic expansion estimate and RH `OPEN`.

<!-- BILINGUAL-UNIT: hall-condition -->

## Global condition

Let I be a finite collection of negative Möbius vertices and let t(i) be the finite set of allowed positive partners. For every subcollection A, write Γ(A) for the union of its partner sets. The relevant condition is:

\[
\forall A\subseteq I:\quad |A|\le |\Gamma(A)|+d.
\]

Checking individual vertex degrees or only the total number of available partners is insufficient. Shared partners can create a deficit for a subcollection. Here d is a natural number bounding unmatched negative vertices, not necessarily the total number of unmatched vertices on both sides.

<!-- BILINGUAL-UNIT: hall-proof -->

## Finite proof and arithmetic specialization

Add d distinct auxiliary targets to every partner set. A nonempty subcollection then has exactly its real neighbors plus these auxiliary targets, so the displayed condition is Hall's condition for the augmented family. The empty subcollection is automatic. Mathlib's finite Hall theorem supplies an injective choice. At most d choices can land in the auxiliary targets; the remaining choices are distinct real partners. Conversely, any such augmented injection implies the displayed cardinality condition for every subcollection.

`formal/lean/UBT/RH/HallBudget.lean` proves these two directions and specializes the sufficient direction to the actual mathlib Möbius sign classes in the interval from zero to N. Every selected real partner is at most N, satisfies the explicitly supplied relation E, and has a Möbius value cancelling its negative source. The finite Hall theorem is imported from `Mathlib.Combinatorics.Hall.Finite`, authored by Alena Gusakov, Bhavik Mehta and Kyle Miller; it is not claimed as a new theorem.

Crucially, the arithmetic subset condition remains an explicit hypothesis. The module does not prove it for the prime-exchange relation. Auxiliary targets are bookkeeping for unmatched vertices, not extra arithmetic cancellation terms or new physical objects.

<!-- BILINGUAL-UNIT: hall-reservation -->

## Reserving partners for large primes

The independent experiment reserves distinct positive semiprimes for negative primes in the upper half of the interval. It chooses the positive targets in increasing order from:

\[
S_N=\{2q\le N:q\text{ prime},q\ge3\}
\cup\{3q\le N:q\text{ prime},q\ge5\}.
\]

It then removes both endpoints of each reserved pair and computes a certified maximum matching in the remaining exchange graph. For every cutoff from 14 through 600, and additionally at 1000, this produces the unavoidable total remainder |M(N)|. At 1000, 73 reserved pairs plus 230 remaining pairs leave 2 vertices. An augmenting-path round is needed after the residual greedy matching. This does not prove that the reservation works for every cutoff; the general extension question is governed by Hall's condition on the residual graph after the reserved targets are removed.

<!-- BILINGUAL-UNIT: hall-verification -->

## Verification and remaining work

Independent script: `tools/verify_hall_budget.py`. Evidence: `reports/lean_hall_budget_2026_09_23.json`. Exhaustive checks cover all 689 bipartite graphs with each side of size at most 3, comparing brute-force maximum matching with the maximum subset deficit. There are 2629 augmented-budget checks. The arithmetic reservation sweep contains 587 cutoffs; the larger explicit sample is 1000. These finite cases are Python-checked, not separately formalized Lean instances.

Compilation with warnings treated as errors, kernel checking and the axiom audit passed: 329 declarations and only the standard allowed axioms. All 29 source/configuration files match the checked merge. The new module contains 3 named theorems. [Successful Lean run](https://github.com/UBT-Institute/unified-biquaternion-theory/actions/runs/35891705417). The missing RH step is a uniform arithmetic estimate on subset deficits and the resulting total unmatched count. No square-root estimate or logarithmic estimate is asserted. Canonical UBT architecture and gap statuses are unchanged. English is the translation source; human semantic-equivalence review is required before merge.
