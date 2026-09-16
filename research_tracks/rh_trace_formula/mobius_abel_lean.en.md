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

# Möbius and Abel: exact formalization boundary

**Status:** `LEAN-PASS`; classical arithmetic, no RH claim.
**Date:** 2026-09-16

<!-- BILINGUAL-UNIT: mobius-abel-results -->
## Results

`formal/lean/UBT/RH/MobiusAbel.lean` formalizes the two-sided Dirichlet convolution inverse over complex arithmetic functions, its uniqueness, the identity \(\Lambda=\mu*\log\), and the exact prime-power support and values of \(\Lambda\). The arithmetic identities reuse the existing mathlib theorems, explicitly attributed in the source. They hold at every index; no finite cutoff is a premise. Arithmetic functions have value zero at index zero, and their unit is the delta at one. The symbol `ζ` in this module denotes the arithmetic function with value one at positive indices, not an analytic zeta function.

The additional induction proves the finite Abel identity for every natural cutoff, every ring, and arbitrary weights, preserving multiplication order:

\[
A(N)=\sum_{n=1}^{N}a(n),\qquad
\sum_{n=1}^{N}a(n)w(n)
=A(N)w(N+1)+\sum_{n=1}^{N}A(n)\bigl(w(n)-w(n+1)\bigr).
\]

The zero cutoff is included. The final summand combines with the endpoint to give the familiar endpoint \(A(N)w(N)\) when \(N\geq1\). This is an exact discrete identity, not a formalization of the integral version or of an infinite limit. Specializing to \(a(n)=\mu(n)\) gives the complex-weight Möbius statement.

<!-- BILINGUAL-UNIT: mobius-abel-open -->
## Remaining analytic and UBT obligations

The next analytic step requires a bound on the partial sums and a justified infinite limit. This work proves neither \(M(x)=O_\varepsilon(x^{1/2+\varepsilon})\) nor a zero-free half-plane. A formal convolution inverse is not automatically a bounded inverse of a Hilbert-space operator. Positivity of the von Mangoldt coefficients alone gives no Möbius cancellation estimate.

`GAP-THETA-PROP`, `GAP-THETA-PRIME-1`, and `GAP-RH-MOEBIUS-UBT` remain open. The canonical biquaternionic field and covariant tetrad are retained. The arithmetic formalization supplies a checked downstream identity; it does not derive an arithmetic operator or its coefficients from the UBT action. The action/Hessian and chirality selection obligations are unchanged.

<!-- BILINGUAL-UNIT: mobius-abel-checks -->
## Verification

The unchanged Lean workflow runs `lake build --wfail`, `leanchecker UBT`, and an axiom audit. Independent exact checks in `tools/verify_mobius_abel.py` cover coefficients through 500, 28 rational-weight cases and 5 symbolic matrix cases. These finite checks complement the Lean proof and do not replace it. `tests/test_mobius_abel.py` runs the verifier.

Evidence: `reports/lean_mobius_abel_2026_09_16.json` records successful CI run 35114672898, an audit of 167 declarations and byte identity for 18 source/configuration files. No unexpected axioms were found.

English is the translation source. Human semantic-equivalence review of the Czech pair is required before merge.
