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

# Global imbalance inside the Hall hypothesis

**Status:** `LEAN-PASS`; RH and the required uniform arithmetic estimate remain `OPEN`.

<!-- BILINGUAL-UNIT: obstruction-statement -->

## Exact finite statement

Let P and R be the actual positive and negative Möbius sign classes up to N. The general count identity is:

\[
M(N)=|P|-|R|.
\]

Suppose a Hall budget d holds for every subset of R, with all neighbors in P. Applying the condition to the full source set already gives the first inequality below. Applying the reverse condition gives the second:

\[
|R|\le|P|+d,\qquad |P|\le|R|+d,
\qquad |M(N)|\le d.
\]

This argument requires neither the full matching theorem nor a construction of pairs. It applies to any allowed relation, including restricted prime exchanges.

<!-- BILINGUAL-UNIT: obstruction-equivalence -->

## Complete adjacency gives an equivalence

For unrestricted opposite-sign pairing, every nonempty subset has the entire opposite sign class as its neighbor set. Therefore the full-set cardinality condition is sufficient as well as necessary. The two directions together give:

\[
\bigl[\forall A\subseteq R:\ |A|\le|\Gamma(A)|+d\bigr]
\land
\bigl[\forall B\subseteq P:\ |B|\le|\Gamma(B)|+d\bigr]
\quad\Longleftrightarrow\quad |M(N)|\le d.
\]

The empty subsets cause no exception. The Lean proof covers every natural N and d, including empty sign classes and the zero cutoff. It uses the actual mathlib Möbius function. The existing general count identity is reused from `ConcreteExchange.mertens_counts`; despite that module's name, the identity itself quantifies over arbitrary N.

For a restricted relation only the implication to the Mertens bound is proved here. The converse can fail because subsets may have too few allowed neighbors.

<!-- BILINGUAL-UNIT: obstruction-meaning -->

## Consequence for the proof strategy

The Hall reformulation does not establish the missing arithmetic cancellation. Asking for a uniform two-sided Hall budget of the order required for RH already includes the corresponding uniform Mertens bound. With unrestricted adjacency it is an exact reformulation, not a weaker intermediate target. Restricted adjacency can make the hypothesis stronger.

This does not disprove RH or rule out a future arithmetic proof using matching. It identifies why another conditional matching theorem cannot by itself close the gap. No unconditional square-root estimate, statistical independence or successful RH proof is claimed. The analytic implication from the uniform Mertens estimate to RH is not formalized by this module. Canonical UBT and its physical gaps are unchanged.

<!-- BILINGUAL-UNIT: obstruction-verification -->

## Verification

Source: `formal/lean/UBT/RH/HallObstruction.lean`. Independent script: `tools/verify_hall_obstruction.py`. Evidence: `reports/lean_hall_obstruction_2026_09_23.json`.

The independent verifier enumerates 343 complete-graph size/budget cases by checking every subset, and checks actual Möbius counts at 1001 cutoffs. These are finite checks; the universal statements require Lean verification. Compilation with warnings treated as errors, kernel checking and axiom audit passed: 340 declarations and only the standard allowed axioms. All 30 source/configuration files match the checked merge. The new module contains 5 named theorems. [Successful Lean run](https://github.com/UBT-Institute/unified-biquaternion-theory/actions/runs/35898465289). English is the translation source; human semantic-equivalence review is required before merge.
