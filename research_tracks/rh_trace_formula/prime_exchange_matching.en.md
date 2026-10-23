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

# Prime exchange matching: exact finite experiment

**Date:** 2026-09-22. **Status:** `FINITE-CERTIFICATES-PASS`; `LEAN-PASS` for the certificate principle and cutoffs 100, 1000; RH `OPEN`.

<!-- BILINGUAL-UNIT: exchange-graph -->

## Graph and allowed exchanges

Use the nonzero Möbius coefficients as vertices. Positive and negative signs form the two parts. For a candidate pair from opposite parts, remove the common prime factors:

\[
L_N=\{n\le N:\mu(n)=1\},\quad R_N=\{n\le N:\mu(n)=-1\},
\quad g=\gcd(x,y),\quad a=x/g,\quad b=y/g.
\]
\[
\{\Omega(a),\Omega(b)\}=\{0,1\}\quad\lor\quad
\{\Omega(a),\Omega(b)\}=\{1,2\}.
\]

Here Ω counts prime factors with multiplicity; all vertices are squarefree, so these are also distinct-factor counts. The first edge type toggles one prime. The second replaces one prime by two distinct primes, or reverses that exchange, preserving any common core. Both endpoints must be at most N. No exchange joins equal signs. The combined graph retains the first edge type as well as the second.

In the single-toggle graph, every prime in (N/2,N] has only the vertex 1 as a neighbour. If there are h such primes, at least h-1 are unmatched. Exchanges can remove this particular bottleneck.

<!-- BILINGUAL-UNIT: exchange-certificate -->

## Algorithm and exact certificates

The verifier begins with a deterministic greedy matching and then searches layered augmenting paths. Reversing a path matches one additional pair while keeping all endpoints distinct. The algorithm stops when no augmenting path is found.

The result is checked by a separate certificate: every matched edge exists, matched endpoints are distinct, and a vertex cover of the same size covers every graph edge. Any matching has at most as many edges as any vertex cover, since disjoint matched edges require distinct covering vertices. Equality therefore certifies maximum cardinality without trusting the search algorithm. Certificates are constructed and checked in memory; their deterministic hashes are recorded, and rerunning the verifier reconstructs them.

<!-- BILINGUAL-UNIT: exchange-results -->

## Results

The table uses U_1 for the minimum unmatched count with single toggles, U_g for the combined greedy result, and U_{1+2} for the combined result after augmentation. Every listed maximum matching has a checked equal-size vertex cover.

| N | M(N) | U_1 | U_g | U_{1+2} |
|---|---|---|---|---|
| 30 | -3 | 3 | 3 | 3 |
| 100 | 1 | 19 | 1 | 1 |
| 300 | -5 | 47 | 5 | 5 |
| 1000 | 2 | 164 | 4 | 2 |
| 3000 | -6 | 502 | 8 | 6 |
| 10000 | -23 | 1685 | 23 | 23 |

Every cutoff from 1 through 200 was tested, as well as the larger displayed cutoffs. In all tested cases the combined graph attains the unavoidable imbalance. At 1000 and 3000, augmentation improves the greedy result. The sample at 10000 has 4749839 combined edges. The implementation tests all opposite-sign vertex pairs, so graph construction is quadratic in the number of vertices and storing its edges limits scalability.

<!-- BILINGUAL-UNIT: exchange-limit -->

## What this establishes and what it does not

If ν_N is the maximum number of pairs, the count identity is:

\[
U_N=|L_N|+|R_N|-2\nu_N\ge\bigl||L_N|-|R_N|\bigr|=|M(N)|.
\]

The observed equality U_N=|M(N)| means the graph permits all cancellation allowed by the sign counts at the tested cutoffs. It is not a proof of equality at every cutoff. Even a general saturation theorem alone would not bound |M(N)|: it would still leave the original sign imbalance to estimate.

To prove RH by this mechanism, a separate uniform estimate on the unmatched count would be needed:

\[
U_N\le C_\varepsilon N^{1/2+\varepsilon}\qquad(\varepsilon>0).
\]

The present computation does not supply that estimate. It must be derived from the arithmetic structure or from a rigorously bounded construction, not assumed from the measured Mertens values. No asymptotic statistical inference is made from the sample. No UBT dynamics-to-arithmetic bridge is assumed; the biquaternionic field and covariant tetrad are unchanged.

<!-- BILINGUAL-UNIT: exchange-reproduction -->

## Reproduction and formal scope

Run `python tools/verify_prime_exchange_matching.py`. Evidence is in `reports/prime_exchange_matching_2026_09_22.json`; the regression test is `tests/test_prime_exchange_matching.py`. Möbius values use trial factorization; factor counts for the graph use an independent smallest-prime-factor sieve. At small cutoffs, edge classification is cross-checked using explicit prime supports. Full matching and cover checks use exact integers.

The companion `prime_exchange_lean.en.md` now records kernel-checked proofs of the certificate principle and actual matching instances at 100 and 1000. The complete Python search program and the remaining sampled cutoffs are not thereby formalized. In particular the 10000 case remains a Python-checked certificate. Evidence: `reports/lean_prime_exchange_2026_09_22.json`. English is the translation source; human semantic-equivalence review is required before merge.
