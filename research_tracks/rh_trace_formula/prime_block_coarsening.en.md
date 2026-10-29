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

# Prime-support block coarsening

**Status:** `LEAN-PASS`; RH `OPEN`. This is finite arithmetic for arbitrary natural cutoffs, not a convergence-rate theorem. Canonical UBT fields, tetrads and gap statuses are unchanged.

<!-- BILINGUAL-UNIT: block-definitions -->

## Definitions and scope

Let P be a finite selection of primes and let F(n) be the set of distinct prime factors of n. Partition the integers in the interval from zero to N by their remaining prime support:

\[
 c_P(n)=F(n)\setminus P,\qquad
 T_P(S,N)=\sum_{\substack{0\le n\le N\\c_P(n)=S}}\mu(n),
 \qquad W_P(N)=\sum_{S\in c_P(\{0,\ldots,N\})}|T_P(S,N)|.
\]

Zero has Möbius value zero. Nonsquarefree integers also have zero weight. For the remaining integers, the label uniquely identifies the product of prime factors outside P. Thus the blocks are precisely the disjoint arithmetic groups discussed in the subset construction. W counts the residual imbalance after unrestricted opposite-sign cancellation separately inside each block. It is not the maximum-matching remainder of the earlier restricted prime-exchange graph.

The Lean definition uses actual mathlib Möbius values and distinct prime-factor sets. Its coarsening result even allows arbitrary finite selections: inserting a nonprime simply cannot remove a prime factor. No square-root bound is an assumption.

<!-- BILINGUAL-UNIT: block-theorems -->

## General results

For every natural N and nested finite selections:

\[
 P\subseteq Q\quad\Longrightarrow\quad
 |M(N)|\le W_Q(N)\le W_P(N).
\]

Proof: the new label is obtained from the old label by deleting Q. Consequently every new block is a disjoint union of old blocks. Regrouping preserves the total signed sum. The triangle inequality bounds the absolute sum of a merged block by the sum of absolute old block sums. Summing gives the result. Lean proves the finite regrouping identity, the general contraction theorem, and its specialization to the actual arithmetic blocks.

If P contains every prime factor of every integer in the interval, all labels are empty and:

\[
 W_P(N)=|M(N)|.
\]

This is a terminal identity, not an asymptotic estimate. Inserting a new prime need not strictly decrease W. The previous subset module already proves the cutoff insertion identity for every cutoff. The new local gain theorem states:

\[
 ab\ge0\quad\Longrightarrow\quad
 |a|+|b|-|a-b|=2\min(|a|,|b|).
\]

Here a and b denote the two cutoff sums before the sign reversal from the added prime. The local gain theorem alone does not supply a frequency or magnitude estimate for such gains.

<!-- BILINGUAL-UNIT: block-bridge -->

## Product-cutoff representation and formal boundary

Writing q for the product of selected primes gives the equivalent paper representation:

\[
 B_q(x)=\sum_{\substack{d\mid q\\d\le x}}\mu(d),\qquad
 W_P(N)=\sum_{\substack{1\le a\le N\\(a,q)=1}}
 |\mu(a)|\,|B_q(N/a)|.
\]

Each squarefree integer has a unique decomposition into its selected and unselected prime factors. This proves the representation on paper; zero-weight nonsquarefree terms do not contribute. The explicit equality with this product-cutoff formula is independently checked on finite samples but is not a theorem in the new Lean module. The formal monotonicity theorem instead uses the direct block definition above and needs no assumed representation identity.

No estimate of the form required for RH is proved. In particular no logarithmic bound, statistical independence, uniform rate of decrease or universal saturation of the restricted exchange graph is asserted.

<!-- BILINGUAL-UNIT: block-verification -->

## Verification

Formal source: `formal/lean/UBT/RH/PrimeBlockCoarsening.lean`. Independent verifier: `tools/verify_prime_block_coarsening.py`. Evidence: `reports/lean_prime_block_coarsening_2026_09_22.json`.

The verifier compares direct prime-support grouping with independently enumerated subset products for 1206 cases at cutoffs from 0 through 200, checks 201 terminal cases and 3721 local gain cases. At cutoff 1000, adding primes in the order 2, 3, 5, 7, 11, 13, 17, 19 gives residual counts 200, 200, 200, 200, 192, 186, 178, 174; the signed total remains 2. These computations are finite checks, not an asymptotic proof.

Lean compilation with warnings treated as errors, kernel checking and the axiom audit passed: 323 declarations, only the standard allowlist, and 28 source/configuration files identical to the checked merge. The new module contains 11 named theorems. [Successful Lean run](https://github.com/UBT-Institute/unified-biquaternion-theory/actions/runs/35788351587). English is the translation source; human semantic-equivalence review is required before merge.
