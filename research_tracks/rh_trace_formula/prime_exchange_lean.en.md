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

# Lean certificates for prime-exchange matching

**Date:** 2026-09-22. **Status:** formalization `LEAN-PASS`; asymptotic unmatched-count estimate and RH `OPEN`.

<!-- BILINGUAL-UNIT: matching-lean-general -->

## General certificate theorem

A matching is a finite set of ordered pairs whose left and right coordinate maps are each injective. A cover consists of two finite vertex sets meeting every edge. Associate each matched edge with its left endpoint if that endpoint is in the cover, otherwise with its covered right endpoint. Tagging the side makes this map injective. Thus every competing matching K in the graph satisfies:

\[
|K|\le |C_L|+|C_R|,\qquad
|M|=|C_L|+|C_R|\quad\Longrightarrow\quad |K|\le|M|.
\]

The certificate comprises a valid matching M contained in the graph, a covering pair, and equality of their cardinalities. The upper-bound theorem is independent of the algorithm producing these data. `MatchingCertificate.lean` formalizes this injection and the resulting comparison with every competing matching.

<!-- BILINGUAL-UNIT: matching-lean-cancellation -->

## Cancellation and arithmetic

When each matched pair has opposite weights and its endpoints belong to L and R, injectivity ensures that no endpoint is counted twice. Splitting both vertex sums into matched and unmatched parts gives:

\[
\sum_{x\in L}f(x)+\sum_{y\in R}g(y)
=\sum_{x\in L\setminus\pi_1(M)}f(x)
+\sum_{y\in R\setminus\pi_2(M)}g(y).
\]

The file also proves the arithmetic exchange under the explicit coprimality assumptions:

\[
\mu(ap)+\mu(aqr)=0,\qquad
\operatorname{Prime}(p),\operatorname{Prime}(q),\operatorname{Prime}(r),
\quad(a,p)=(a,qr)=(q,r)=1.
\]

If the common core a has a square factor, both values can be zero; concrete certificate vertices separately require Möbius value +1 or -1. No squarefree or independence assumption is silently inferred.

<!-- BILINGUAL-UNIT: matching-lean-concrete -->

## Kernel-checked concrete data

The generated modules `ConcreteExchange.lean` and `ConcreteExchange1000.lean` check actual certificates at cutoffs 100 and 1000. The table gives positive and negative vertex counts, matched pairs, unmatched vertices and the actual Mertens sum:

| N | L_N | R_N | pairs | U_N | M(N) |
|---|---|---|---|---|---|
| 100 | 31 | 30 | 30 | 1 | 1 |
| 1000 | 305 | 303 | 303 | 2 | 2 |

The evaluator `muEval` uses zero handling, duplicate detection in the prime-factor list and its length parity. `muEval_eq` proves equality with the actual mathlib Möbius function for every natural input. The concrete modules also prove that the filtered vertex sets are the actual Möbius sign classes and establish:

\[
M(N)=|L_N|-|R_N|.
\]

Lean checks endpoint uniqueness, bounds, signs and allowed factor exchanges directly on every listed pair. The full negative vertex set is a cover; its size equals the matching size, so the general certificate theorem proves maximality against every competitor. Direct endpoint checks avoid constructing the entire edge graph during proof reduction.

<!-- BILINGUAL-UNIT: matching-lean-verification -->

## Trust boundary and verification

`tools/export_prime_exchange_lean.py` exports data from the Python search. Lean uses ordinary kernel-reduced `decide +kernel` proofs, not `native_decide`, to validate concrete computations. Python is not trusted for the mathematical validity of an accepted certificate. The exporter regression test checks deterministic reproduction of the committed Lean files.

This verifies the general certificate principle and these two concrete instances. It does not formalize every execution of the augmenting-path program, certify every previously sampled cutoff, prove saturation for all N, or establish a square-root bound on unmatched vertices. In particular the earlier experiment at 10000 remains a Python-checked finite certificate. No UBT dynamics-to-arithmetic bridge is assumed; the biquaternionic field and covariant tetrad are unchanged.

English is the translation source; human semantic-equivalence review is required before merge.

Evidence: `reports/lean_prime_exchange_2026_09_22.json`; [Lean CI](https://github.com/UBT-Institute/unified-biquaternion-theory/actions/runs/35752056147); 286 audited declarations; 27 matching source/configuration files.
