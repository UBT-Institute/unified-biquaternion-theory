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

# Ordered Abel limits and the remaining cancellation estimate

**Status:** `LEAN-PASS` for the general transfer and remainder; power-weight application is `LEAN-PENDING` separately. No RH proof.
**Date:** 2026-09-16

<!-- BILINGUAL-UNIT: abel-limit-theorem -->
## General theorem

Let the coefficients and weights be complex sequences and define

\[
A(N)=\sum_{n=1}^{N}a(n),\quad
B_k=A(k+1)\bigl(w(k+1)-w(k+2)\bigr),\quad
S_N=\sum_{n=1}^{N}a(n)w(n).
\]

Assume the boundary term tends to zero and the transformed terms have a summable real majorant:

\[
A(N)w(N+1)\longrightarrow0,\qquad
|B_k|\leq g_k,\qquad \sum_{k=0}^{\infty}g_k<\infty.
\]
\[
S_N\longrightarrow L=\sum_{k=0}^{\infty}B_k.
\]

Proof: the finite Abel identity gives the sum of the boundary term and the finite sum of transformed terms. The latter converges by the comparison theorem; addition preserves limits. `ordered_limit` and `ordered_limit_of_majorant` in `formal/lean/UBT/RH/AbelLimit.lean` formalize precisely this argument. No claim of absolute convergence for the original series is made. Lean `Summable` is imposed on the transformed series; the original series uses `Tendsto` of sums in natural order.

<!-- BILINGUAL-UNIT: abel-limit-error -->
## Exact remainder and error bound

Splitting the summable transformed series at any natural cutoff gives

\[
S_N-L=A(N)w(N+1)-\sum_{k=0}^{\infty}B_{k+N},
\]
\[
|S_N-L|\leq |A(N)w(N+1)|+\sum_{k=0}^{\infty}g_{k+N}.
\]

The triangle inequality and comparison of the tail prove the bound. These identities require summability of the transformed terms, but do not require the boundary limit. Identifying the target with the limit of the original partial sums does require that additional condition. The Lean statements are `remainder_identity` and `remainder_bound`.

<!-- BILINGUAL-UNIT: abel-limit-application -->
## Application to power weights: explicit remaining premise

The following calculus application is an analytic derivation, not yet a Lean theorem in this patch. Suppose

\[
a(n)=\mu(n),\quad w(n)=n^{-s},\quad s=\sigma+it,\quad
|M(n)|\leq Cn^\theta,\quad C>0,\quad\theta\geq0,\quad\sigma>\theta.
\]
\[
|n^{-s}-(n+1)^{-s}|\leq |s|\int_n^{n+1}x^{-\sigma-1}\,dx,
\]
\[
|M(n)(n^{-s}-(n+1)^{-s})|
\leq C|s|\int_n^{n+1}x^{\theta-\sigma-1}\,dx.
\]
\[
|S_N-L|\leq C\left(1+\frac{|s|}{\sigma-\theta}\right)N^{\theta-\sigma},
\qquad N\geq1.
\]

The derivative of the weight and the fundamental theorem of calculus give the first inequality. Monotonicity of the nonnegative power bounds the transformed term by the displayed integral. Summing its intervals gives a convergent improper integral. The boundary term tends to zero because the exponent difference is negative. The error bound follows by integrating the tail and bounding the boundary term. The loose bound starts the integral at the cutoff rather than the next integer, and is valid as written.

This transfers a proved bound on the Mertens function into convergence; it does not supply that bound. The elementary coefficient estimate gives only the linear bound. To reach every point strictly to the right of the critical line by this route, a square-root-plus-epsilon cancellation estimate is still needed. Neither convolution inversion nor nonnegative von Mangoldt coefficients provide it in the current derivation. No zero-free conclusion is inferred from the conditional transfer alone.

<!-- BILINGUAL-UNIT: abel-limit-examples -->
## Independent checks and a necessary hypothesis

`tools/verify_abel_limit.py` checks a symbolic geometric-series remainder and 15 exact rational cases. It checks 6 alternating-harmonic truncations against the known logarithmic limit at 70 decimal digits. This illustrates why the original series need not be absolutely convergent. These are diagnostics, not proofs of the infinite theorem. The verifier also checks the power-weight derivative and the improper tail integral symbolically; the corresponding calculus application remains `LEAN-PENDING`.

The boundary hypothesis is essential: constant coefficients and constant unit weights give zero transformed terms, while the original partial sums grow as the cutoff. The checker includes this counterexample. It cannot be repaired by dropping the boundary term from the Abel identity.

<!-- BILINGUAL-UNIT: abel-limit-ubt -->
## UBT boundary and verification

`GAP-THETA-PROP`, `GAP-THETA-PRIME-1`, and `GAP-RH-MOEBIUS-UBT` remain open. The canonical action registry is `DEFINED_FAMILY_NOT_FINALIZED`; its current family does not select a demonstrated arithmetic cancellation law. No change to the biquaternionic field, covariant tetrad, or action is made here. A physical derivation needs that missing mechanism in addition to these analytic transfer results.

Lean verification uses the unchanged build, kernel check and axiom allowlist. `tests/test_abel_limit.py` runs the independent checker. The English edition is the translation source; human semantic-equivalence review is required before merge.

Evidence: `reports/lean_abel_limit_2026_09_16.json` pins successful CI run 35146584178, 174 audited declarations and 19 matching source/configuration files. All 4 new theorems passed. The record retains the initial failed compilation and its correction.
