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

# Binomial boundary layers in selected prime families

**Date:** 2026-09-22. **Status:** algebraic formalization `LEAN-PASS`; RH `OPEN`.

<!-- BILINGUAL-UNIT: parity-layers -->

## Exact layer imbalance

The full subset family has zero signed sum, but a cutoff may retain complete cardinality layers. With binomial coefficients outside their natural range interpreted as zero, Pascal cancellation gives:

\[
A_{k,r}=\sum_{j=0}^r(-1)^j\binom{k}{j}
=(-1)^r\binom{k-1}{r}\qquad(k\ge1).
\]

Proof: the r=0 case is one. Adding the next term and applying the Pascal identity cancels the previous boundary coefficient and leaves the next one with the reversed sign. This proves the formula for every nonnegative r, including cutoffs beyond the last layer. The result is classical combinatorics.

<!-- BILINGUAL-UNIT: parity-products -->

## A product cutoff that selects these layers

Let P consist of k distinct primes in the interval [a,b]. If the displayed separation holds, any subset of at most r factors has product at most b^r; every larger subset has product at least a^(r+1). Hence:

\[
a\le p\le b\quad(p\in P),\qquad b^r<a^{r+1},\qquad N=b^r
\quad\Longrightarrow\quad
\prod_{p\in S}p\le N\ \Longleftrightarrow\ |S|\le r.
\]
\[
B_P(N)=(-1)^r\binom{k-1}{r},\qquad
T_P(N)=\sum_{j=0}^r\binom{k}{j},\quad k=|P|.
\]

This is an exact finite argument using ordered products and unique factorization. It demonstrates how a nonzero boundary layer survives despite perfect cancellation in the complete family. T counts admissible squarefree products supported on P; B is their signed Möbius sum.

<!-- BILINGUAL-UNIT: parity-example -->

## Exact prime example

Take the 20 primes from 1009 through 1123. Trial division verifies their primality, and integer exponentiation verifies the separation:

\[
k=20,\quad r=10,\quad a=1009,\quad b=1123,\quad
N=1123^{10}<1009^{11},
\]
\[
T_P(N)=616666,\quad E=354522,\quad O=262144,\quad
B_P(N)=92378,\quad B_P(N)^2>T_P(N),\quad B_P(N)^2<N.
\]

All 1048576 subsets were also enumerated directly, with actual integer products. Thus the imbalance can greatly exceed the square root of the number of admitted terms, even for genuine prime products. This single example does not prove a universal asymptotic impossibility result.

It is not a counterexample to RH: P omits the other primes below N, so B_P(N) is not M(N). Moreover its squared signed sum is smaller than N. The square root of the number of selected terms must not be confused with the square root of the numerical cutoff. The unresolved problem remains the parity discrepancy for the full prime set up to N.

<!-- BILINGUAL-UNIT: parity-verification -->

## Formal scope and verification

`formal/lean/UBT/RH/ParityLayers.lean` formalizes the alternating-layer formula and the following elementary threshold criterion for natural numbers:

\[
0\le u\le B<A\quad\Longrightarrow\quad
cA+u\le rA+B\ \Longleftrightarrow\ c\le r.
\]

The criterion explains why perturbations smaller than a layer spacing preserve a cardinality cutoff. The ordered-product application to the prime interval and its concrete example are prose proofs and exact independent checks, not further Lean theorems.

`tools/verify_parity_layers.py` checks 1800 binomial cases and the full 1048576-subset prime example. `tests/test_parity_layers.py` runs it. No statistical independence, asymptotic Möbius estimate or UBT arithmetic bridge is established. The biquaternionic field and covariant tetrad remain unchanged.

English is the translation source; human semantic-equivalence review is required before merge.

Evidence: `reports/lean_parity_layers_2026_09_22.json`; [Lean CI](https://github.com/UBT-Institute/unified-biquaternion-theory/actions/runs/35706768221); 212 audited declarations; 24 matching source/configuration files.
