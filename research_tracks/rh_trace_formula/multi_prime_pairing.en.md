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

# Pairing across a finite set of primes

**Date:** 2026-09-22. **Status:** exact mathematical derivation and finite checks; `LEAN-PENDING`; RH `OPEN`.

<!-- BILINGUAL-UNIT: multi-prime-identity -->
## Exact identity

Let P be a finite nonempty set of distinct primes. Define the squarefree integer Q, the restricted partial sum, and the step weight below. The floor convention is implicit in sums over integers.

\[
Q=\prod_{p\in P}p,\quad
A_Q(x)=\sum_{1\le m\le x,\ (m,Q)=1}\mu(m),\quad
w_Q(t)=\sum_{d\mid Q}\mu(d)\mathbf 1_{dt\le1}.
\]
\[
M(N)=\sum_{d\mid Q}\mu(d)A_Q(N/d)
=\sum_{1\le m\le N,\ (m,Q)=1}\mu(m)w_Q(m/N),\qquad N\ge1.
\]

Proof: in the coefficient of a positive integer n, sum μ(d)μ(n/d) over divisors d of Q for which d divides n and n/d is coprime to Q. If a prime of Q divides n twice, no term survives and μ(n)=0. Otherwise exactly one term survives: d is the product of primes common to n and Q. Multiplicativity gives μ(d)μ(n/d)=μ(n), including zero when n has a square factor outside Q. Summing this coefficient identity to N and exchanging finite sums proves both equalities. No infinite-product limit or coefficient independence is used.

For Q=6 the step weight is zero below 1/6, minus one on (1/6,1/3], zero on (1/3,1/2], and one on (1/2,1]. Thus:

\[
M(N)=\sum_{N/2<m\le N,\ (m,6)=1}\mu(m)
-\sum_{N/6<m\le N/3,\ (m,6)=1}\mu(m).
\]

All endpoints follow from the weak inequality in the indicator. This is classical finite inclusion-exclusion, not an RH proof.

<!-- BILINGUAL-UNIT: multi-prime-bound -->
## Exact envelope and leading coefficient

The triangle inequality and |μ(m)|≤1 imply:

\[
|M(N)|\le E_Q(N):=\sum_{1\le m\le N,\ (m,Q)=1}|w_Q(m/N)|
=c_QN+O_Q(1),
\qquad c_Q=\frac{\varphi(Q)}Q\int_0^1|w_Q(t)|\,dt.
\]

For fixed Q, coprime integers in any real interval (a,b] have count φ(Q)(b-a)/Q plus an error bounded in magnitude by twice the number of divisors of Q. This follows by inclusion-exclusion and bounding each floor error. Partition (0,1] at the finitely many points 1/d, where d divides Q, and multiply each count by the constant absolute weight on that interval. This proves the displayed fixed-Q asymptotic formula. Rational integration of the step function gives:

| Q | c_Q |
|---|---|
| 2 | 1/4 |
| 6 | 2/9 |
| 30 | 16/75 |
| 210 | 256/1225 |

In particular two-prime pairing improves the earlier linear coefficient but does not change the power of N. The weights for larger Q must be counted with their absolute magnitudes; they cannot generally be replaced by a simple indicator of survival.

<!-- BILINGUAL-UNIT: multi-prime-obstruction -->
## Limit of a fixed finite pairing

Every divisor other than 1 is at least 2, so the upper half of the step function has weight one. Order the k primes increasingly; the i-th is at least i+1. The product of (1-1/p) is therefore at least the telescoping product of i/(i+1). Consequently:

\[
w_Q(t)=1\quad(1/2<t\le1),\qquad
c_Q\ge\frac{\varphi(Q)}{2Q}\ge\frac1{2(k+1)}>0,\quad k=|P|.
\]

Thus this particular counting envelope remains of linear order for every fixed finite prime set. This is a limitation of the envelope, not a lower bound on |M(N)| and not a no-go theorem for RH. Letting Q grow with N requires explicit uniform control of the interval-counting errors; the fixed-Q remainder cannot be treated as an absolute constant. The signed residual sum may be much smaller, but that cancellation is not established here. UBT's biquaternionic field and covariant tetrad are unchanged.

<!-- BILINGUAL-UNIT: multi-prime-verification -->
## Verification

`tools/verify_multi_prime_pairing.py` independently factors the integers and checks both the coefficient convolution and direct weighted sums. It checks 8004 interval cases through N=2000, including N=0 separately, and the exact two-band formula and four rational leading coefficients. `tests/test_multi_prime_pairing.py` runs these checks. These finite checks are not a proof for all N. These multi-prime statements have not been formalized; the later successful Lean check of single-prime cardinality and signed energy does not cover them. The earlier five single-prime theorems retain their separate successful check.

English is the translation source; human semantic-equivalence review is required before merge. This document and the verifier supply no RH-strength cancellation estimate or UBT derivation of one.
