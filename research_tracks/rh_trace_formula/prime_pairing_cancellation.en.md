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

# Exact prime pairing and the remaining cancellation estimate

**Date:** 2026-09-22. **Status:** identities `LEAN-PASS`; added cardinality bound `LEAN-PASS`; RH `OPEN`.

<!-- BILINGUAL-UNIT: prime-pair-statement -->
## Theorem and proof

For a prime p and nonnegative integer N, define the following sums, with the zero-index convention μ(0)=0 in Lean.

\[
M(N)=\sum_{n=1}^N\mu(n),\qquad
 a_p(n)=\begin{cases}\mu(n)&p\nmid n,\\0&p\mid n,\end{cases}
\qquad A_p(N)=\sum_{n=1}^N a_p(n).
\]
\[
\mu(pm)=-a_p(m),\qquad
M(N)=A_p(N)-A_p(\lfloor N/p\rfloor)
=\sum_{N/p<n\leq N,\ p\nmid n}\mu(n).
\]

If p divides m, the product pm has a square prime factor, so both sides of the first identity vanish. Otherwise multiplicativity and μ(p)=-1 give the identity. Split the finite sum into multiples of p and indices not divisible by p, then reindex the multiples. The lower part cancels exactly. These are elementary arithmetic identities, not a new RH theorem.

`formal/lean/UBT/RH/PrimePairing.lean` formalizes `moebius_prime_mul`, `coefficient_split`, `sum_quotient_multiples`, `mertens_prime_difference` and `mertens_prime_band`. No hypothesis of asymptotic cancellation appears in these five theorems.

<!-- BILINGUAL-UNIT: prime-pair-bound -->
## Counting the survivors

The triangle inequality and |μ(n)|≤1 bound the sum by the number of remaining indices. Counting nonmultiples of p in the two intervals gives:

\[
|M(N)|\leq C_p(N),\qquad
C_p(N)=N-2\lfloor N/p\rfloor+\lfloor N/p^2\rfloor
=(1-1/p)^2N+O(1).
\]
\[
C_2(N)=\left\lfloor\frac{N+1}{2}\right\rfloor
-\left\lfloor\frac{\lfloor N/2\rfloor+1}{2}\right\rfloor
=\frac N4+O(1).
\]

The proposed Lean theorem `mertens_band_bound` gives the cardinality bound. Its build, kernel check and axiom audit passed. The floor formulas and asymptotic evaluations are proved here by interval counting; they are not additional Lean-verified theorems. The finite verifier also checks the exact formulas. For p=2 the count has leading coefficient 1/4. For any fixed prime the scale remains linear.

<!-- BILINGUAL-UNIT: prime-pair-gap -->
## What remains to prove

The estimate needed by the existing power-weight route is:

\[
M(N)=O_\varepsilon(N^{1/2+\varepsilon})\qquad\forall\varepsilon>0.
\]

The epsilon statement above is an open target, not an assumption hidden in the prime-pairing identities. Repeatedly choosing another prime does not automatically multiply the savings: the surviving truncated intervals overlap and the next pairing need not remain inside them. A proof must control the signed residual sum, including the boundary terms. Counting alone supplies no such control. Neither a random-sign model nor independence of the coefficients has been established.

This arithmetic work does not change the single biquaternionic field or covariant tetrad. No UBT action-level derivation of the cancellation estimate has been supplied. RH and the physical bridge remain open.

<!-- BILINGUAL-UNIT: prime-pair-verification -->
## Verification and delivery

[Successful Lean workflow](https://github.com/UBT-Institute/unified-biquaternion-theory/actions/runs/35201941077) checked commit `354cc5489511f5dada54aadd517426267554b4d2` containing the five identity theorems. The workflow enables `lake build --wfail`, kernel checking and the axiom audit. The later cardinality theorem passed in [run 35703409640](https://github.com/UBT-Institute/unified-biquaternion-theory/actions/runs/35703409640) after GitHub access recovered.

`tools/verify_prime_pairing.py` uses integer arithmetic, a Möbius sieve, and independent trial factorization on 2001 inputs. It checks 1000005 interval cases for primes 2, 3, 5, 7, 11 through N=200000. All finite checks pass. They do not prove an asymptotic estimate. `tests/test_prime_pairing.py` runs the verifier.

English is the translation source; the Czech edition requires human semantic-equivalence review before merge. The verification record distinguishes the earlier five-theorem revision from the subsequently verified extension.
