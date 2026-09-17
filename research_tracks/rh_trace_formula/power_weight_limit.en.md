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

# Power-weight convergence and the meaning of zeta regularization

**Status:** `LEAN-PASS` for the ordered power-weight theorem; no RH claim.
**Date:** 2026-09-17

<!-- BILINGUAL-UNIT: power-limit-statement -->
## Exact theorem and assumptions

Let the coefficients be complex, with the zero-index convention specified in Lean, and suppose

\[
A(N)=\sum_{n=1}^{N}a(n),\quad A(N)=O(N^\theta),\quad
\theta\geq0,\quad s=\sigma+it,\quad\sigma>\theta.
\]
\[
\lim_{N\to\infty}\sum_{n=1}^{N}a(n)n^{-s}
=s\int_1^\infty A(\lfloor x\rfloor)x^{-s-1}\,dx.
\]

The conclusion is convergence of partial sums in natural order. It does not assume absolute convergence of the original series. Powers of positive real numbers use the real logarithm in the complex exponential. The integral is absolutely convergent. Big-O is a bound for the signed or complex partial sum, not the sum of norms.

`formal/lean/UBT/RH/PowerWeightLimit.lean` contains `ordered_power_limit` and its Möbius specialization `mobius_ordered_power_limit`. The latter retains the partial-sum bound as an explicit hypothesis. No such cancellation estimate is derived by specializing the coefficients.

<!-- BILINGUAL-UNIT: power-limit-proof -->
## Proof and source attribution

Apply Abel summation with the power weight. Its boundary and derivative satisfy

\[
|x^{-s}|=x^{-\sigma},\qquad
\frac{d}{dx}x^{-s}=-s x^{-s-1},\qquad
A(N)N^{-s}=O(N^{\theta-\sigma})\longrightarrow0.
\]
\[
|A(\lfloor x\rfloor)x^{-s-1}|=O(x^{\theta-\sigma-1}),\qquad
\theta-\sigma-1<-1.
\]

The boundary therefore vanishes. The step function of partial sums is locally integrable; the displayed power bound makes the derivative-weighted tail integrable. The infinite Abel theorem then gives the stated integral limit. This derives the boundary limit and integrability from the partial-sum hypothesis, rather than assuming them separately as in `AbelLimit.lean`.

The implementation adapts Xavier Roblot's proof in [mathlib SumCoeff.lean](https://github.com/leanprover-community/mathlib4/blob/v4.33.1/Mathlib/NumberTheory/LSeries/SumCoeff.lean), retaining its Apache 2.0 attribution. The original auxiliary integral-representation theorem assumes `LSeriesSummable` to identify an already summable L-series. Our conclusion instead uses the ordered limit directly and has no `LSeriesSummable` premise. This is classical analysis, not a new RH theorem.

The explicit numerical constant in the earlier quantitative power-weight error bound is still separately `LEAN-PENDING`; this module closes the convergence and integral-representation step only.

<!-- BILINGUAL-UNIT: power-limit-regularization -->
## Ordinary sums and regularized values

The harmonic series and the sum of positive integers both diverge. The negative fraction belongs to analytic continuation of zeta, not to either ordinary sum:

\[
\sum_{n=1}^{\infty}\frac1n=+\infty,\qquad
\sum_{n=1}^{\infty}n=+\infty,\qquad
\zeta(-1)=-\frac1{12}.
\]
\[
F(t)=\sum_{n=1}^{\infty}n e^{-nt}
=\frac{e^{-t}}{(1-e^{-t})^2}
=\frac1{t^2}-\frac1{12}+\frac{t^2}{240}+O(t^4),\qquad t\downarrow0.
\]
\[
\lim_{t\downarrow0}\left(F(t)-\frac1{t^2}\right)=-\frac1{12}.
\]

For positive cutoff parameter the damped series converges. Its rational expression follows by differentiating a geometric series; its Laurent expansion gives the displayed finite part after subtracting the divergent term. This explains the value without changing arithmetic at infinity. This contextual expansion and its inversion identity are checked with SymPy; they are not new Lean theorems in this patch. General Ramanujan summation and zeta regularization must not be identified without specifying conventions.

<!-- BILINGUAL-UNIT: power-limit-reflection -->
## What the reflection does and does not imply

The rational expression has an exact inversion symmetry:

\[
\frac{q}{(1-q)^2}=\frac{q^{-1}}{(1-q^{-1})^2},\qquad q\neq0,1.
\]
\[
\xi(s)=\xi(1-s),\qquad
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

With the exponential substitution, inversion reverses the cutoff parameter. This is a symmetry of the continued rational function; the defining damped series does not converge at negative real cutoff parameter. The completed zeta function has the separately established reflection shown above, with removable values understood by continuation. The functional equation is formalized in mathlib's [RiemannZeta.lean](https://github.com/leanprover-community/mathlib4/blob/v4.33.1/Mathlib/NumberTheory/LSeries/RiemannZeta.lean).

Reflection symmetry pairs zeros across the critical line; it does not on its own force each zero onto that line. Neither the finite part nor the functional equation supplies the missing Möbius cancellation estimate. The current UBT action has not been shown to supply that estimate either. `GAP-RH-MOEBIUS-UBT`, `GAP-THETA-PROP` and `GAP-THETA-PRIME-1` remain open, with the biquaternionic field and covariant tetrad unchanged.

<!-- BILINGUAL-UNIT: power-limit-checks -->
## Verification

The unchanged Lean workflow checks the build, kernel and axiom dependencies. `tools/verify_power_weight_limit.py` independently checks the derivative and tail integral symbolically and tests 20 nonreal power-weight cases at 80 decimal digits. It uses alternating coefficients with bounded partial sums and constant coefficients with linearly growing partial sums. The sampled error bounds are diagnostics; the general convergence theorem is the formal result. `tests/test_power_weight_limit.py` runs these checks.

English is the translation source; human semantic-equivalence review of the Czech pair is required before merge.

Evidence: `reports/lean_power_weight_limit_2026_09_17.json` records successful run 35150594731, attempt 2, with 176 audited declarations and 20 matching Lean source/configuration files. The first attempt failed to download Lean; the same source passed on retry.
