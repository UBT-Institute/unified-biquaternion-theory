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

# Exponentially many prime subsets and the product cutoff

**Date:** 2026-09-22. **Status:** combinatorial formalization `LEAN-PASS`; asymptotic parity discrepancy `OPEN`.

<!-- BILINGUAL-UNIT: subset-count -->

## What grows exponentially

Let P be a finite set of distinct primes. Unique factorization identifies its subsets with distinct squarefree divisors of Q, including the empty product 1. The sign is positive for an even subset size and negative for an odd size.

\[
Q=\prod_{p\in P}p,\quad k=|P|,\quad
B_P(N)=\sum_{S\subseteq P}(-1)^{|S|}\mathbf1_{\prod_{p\in S}p\le N}
=\sum_{d\mid Q,\ d\le N}\mu(d).
\]
\[
\#\{S\subseteq P\}=2^k,\qquad
\sum_{S\subseteq P}(-1)^{|S|}=(1-1)^k=0\quad(k\ge1).
\]

Each prime is used at most once here. Allowing arbitrary repeated factors gives infinitely many products without a cutoff, but any repeated prime has Möbius value zero and makes no contribution to M. The exponential count is in the number k of available primes, not in the cutoff N.

For a nonempty full subset family, toggling any chosen prime pairs every positive term with a negative term. Cancellation is exact. For prime subsets all products are admitted once N is at least Q. The identity alone gives no estimate when only part of the family is admitted.

<!-- BILINGUAL-UNIT: subset-cutoff -->

## Exact effect of the cutoff

Split the subsets according to whether they contain the new prime p. Its inclusion reverses the sign and multiplies the product by p, so the second group has cutoff floor(N/p). Subtraction yields the exact recurrence and its boundary band:

\[
B_{P\cup\{p\}}(N)=B_P(N)-B_P(\lfloor N/p\rfloor)
=\sum_{S\subseteq P}(-1)^{|S|}\mathbf1_{N/p<\prod_{q\in S}q\le N},
\quad p\notin P.
\]
\[
\prod_{p\in S}p\le N\quad\Longleftrightarrow\quad
\sum_{p\in S}\log p\le\log N\qquad(N\ge1).
\]

The cutoff therefore selects a weighted subset-sum region in logarithmic coordinates. This is an exact change of variables, not an independence or equidistribution theorem. Inside the region a subset and its toggled partner may both occur and cancel; across the boundary only one occurs. The number of available subsets is relevant, but their parity imbalance at that boundary is what determines the residual sum.

<!-- BILINGUAL-UNIT: subset-mertens -->

## Relation to the actual Mertens sum

If P contains only some primes, B counts only squarefree numbers supported on those primes. It is generally not M. For the set of all primes at most N, unique factorization gives:

\[
P_N=\{p\le N:\operatorname{Prime}(p)\},\quad
E_N=\#\{S\subseteq P_N:\textstyle\prod_{p\in S}p\le N,\ |S|\equiv0\pmod2\},
\]
\[
O_N=\#\{S\subseteq P_N:\textstyle\prod_{p\in S}p\le N,\ |S|\equiv1\pmod2\},
\quad M(N)=E_N-O_N,\quad E_N+O_N=\sum_{n=1}^N|\mu(n)|\le N.
\]
\[
|E_N-O_N|\le C_\varepsilon N^{1/2+\varepsilon}\qquad
(\varepsilon>0,\ N\ge1).
\]

The last inequality is the still-open target, with a constant depending on epsilon and valid for every N; it is not a consequence of the preceding identities. There are at most N admissible subsets because their products are distinct positive integers at most N. Thus the full exponential count cannot be substituted for the number of summands below the cutoff.

Exact examples using all primes at most N:

| N | k | 2^k | E_N+O_N | E_N | O_N | M(N) |
|---|---|---|---|---|---|---|
| 5 | 3 | 8 | 4 | 1 | 3 | -2 |
| 6 | 3 | 8 | 5 | 2 | 3 | -1 |
| 30 | 10 | 1024 | 19 | 8 | 11 | -3 |

For the fixed set {2,3,5}, admitting all products up to 30 gives B=0. This must not be confused with M(30)=-3 in the table, where the prime set is larger. No claim of balanced parity after truncation follows from balanced parity in the full family.

<!-- BILINGUAL-UNIT: subset-verification -->

## Verification and limitations

`formal/lean/UBT/RH/SubsetCancellation.lean` contains the subset count, a weighted insertion identity, full-family cancellation and the exact cutoff recurrence. The formal statements apply to finite sets of natural numbers; the recurrence requires a positive newly inserted element. The interpretation as distinct prime products and as Möbius coefficients is proved above using unique factorization, but is not formalized in this module. The full-family sum with constant weight is formalized; the product-saturation threshold and logarithmic reformulation are prose consequences.

`tools/verify_subset_cancellation.py` independently checks prime-product uniqueness, parity counts, 964 recurrence cases, and the actual Möbius correspondence at 31 cutoffs using trial factorization. `tests/test_subset_cancellation.py` runs it. Finite checks do not prove an asymptotic parity bound. No RH or UBT dynamics-to-arithmetic bridge is proved; the biquaternionic field and covariant tetrad are unchanged. These are classical combinatorial identities, not a priority claim.

English is the translation source; human semantic-equivalence review is required before merge.

Evidence: `reports/lean_subset_cancellation_2026_09_22.json`; [Lean CI](https://github.com/UBT-Institute/unified-biquaternion-theory/actions/runs/35705820177); 206 audited declarations; 23 matching source/configuration files.
