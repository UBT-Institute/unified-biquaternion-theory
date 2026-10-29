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

# Signed energy and the precise correlation obligation

**Date:** 2026-09-22. **Status:** finite identities `LEAN-PASS`; correlation growth and RH `OPEN`.

<!-- BILINGUAL-UNIT: energy-identity -->

## Exact decomposition

For real coefficients, define the prefix sum, diagonal energy and unordered cross terms. The algebraic identity also holds in every commutative ring.

\[
S_N=\sum_{n=1}^N a_n,\quad D_N=\sum_{n=1}^N a_n^2,\quad
K_N=\sum_{1\le i<j\le N}a_i a_j=\sum_{j=1}^N S_{j-1}a_j,
\qquad S_N^2=D_N+2K_N.
\]

Expand each square of the next prefix: the increment is the square of the new coefficient plus twice its product with the previous prefix. Summing these increments proves the identity. `formal/lean/UBT/RH/SignedEnergy.lean` uses induction, with no sign or independence assumption. Its Möbius specialization keeps the actual coefficients.

<!-- BILINGUAL-UNIT: energy-bound -->

## Sufficient bound and its logical status

\[
S_N^2\le B\quad\Longleftrightarrow\quad K_N\le(B-D_N)/2.
\]
\[
|a_n|\le1,\quad K_N\le C_\varepsilon N^{1+2\varepsilon},\quad
C_\varepsilon\ge0,\quad\varepsilon>0,\quad N\ge1
\quad\Longrightarrow\quad
|S_N|\le\sqrt{1+2C_\varepsilon}\,N^{1/2+\varepsilon}.
\]

The first equivalence is formalized as `energy_bound_iff`; `energy_bound_of_cross` combines explicit diagonal and cross-term upper bounds. For the second implication, the diagonal is at most N, and N is at most the displayed larger power. Taking the nonnegative square root proves the conclusion. The power implication is a prose derivation, not an additional Lean theorem.

The needed correlation estimate is not proved. For Möbius coefficients it repackages the partial-sum difficulty: the exact equivalence must not be treated as independent evidence for RH. A random-sign interpretation is not a bound for this deterministic sequence. This module does not formalize a new implication to the zeta zero set.

<!-- BILINGUAL-UNIT: energy-counterexample -->

## A concrete sign obstruction

The single-prime identity permits the following surviving odd band:

\[
N=13,\quad (m)=(7,9,11,13),\quad (\mu(m))=(-1,0,-1,-1),
\quad M(13)=-3,\quad D=3,\quad K=3,\quad 9=3+2\cdot3.
\]

Thus its cross term can be positive. Dropping it or declaring all surviving pairs anticorrelated would be false. The example is checked by independent factorization and exact pair enumeration; it is not a new Lean theorem. This refutes that shortcut, not the possibility of a weaker uniform growth bound.

<!-- BILINGUAL-UNIT: energy-verification -->

## Verification and scope

`tools/verify_signed_energy.py` checks the polynomial identity symbolically at 8 lengths and the odd-band specialization at 301 cutoffs, including the counterexample. `tests/test_signed_energy.py` runs these checks. Neither finite computation nor the algebraic identity proves an asymptotic correlation estimate. Formal CI evidence is recorded separately after completion.

The biquaternionic field and covariant tetrad are unchanged. No UBT dynamics-to-arithmetic bridge is assumed. English is the translation source; human semantic-equivalence review is required before merge.

Evidence: `reports/lean_signed_energy_2026_09_22.json`; [Lean CI](https://github.com/UBT-Institute/unified-biquaternion-theory/actions/runs/35703409640); 200 audited declarations; 22 matching source/configuration files.
