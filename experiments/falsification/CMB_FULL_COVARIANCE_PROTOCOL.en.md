<!-- BILINGUAL-UNIT: cmb-cov-2026.provenance -->
<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# CMB full-covariance falsification protocol — October 2026

**Status:** protocol draft — freeze before evaluation

<!-- BILINGUAL-UNIT: cmb-cov-2026.nulls -->
## 1. Null hierarchy

The test must compare
\[
\begin{aligned}
H_0&=\Lambda{\rm CDM}\text{, trivial topology},\\
H_1&=\text{compact topology with standard primordial spectrum},\\
H_2&=\text{compact topology with generic oscillatory primordial spectrum},\\
H_3&=\text{UBT theta/prime-gated model}.
\end{aligned}
\]

A result is UBT-specific only if \(H_3\) outperforms a properly tuned \(H_2\) on
independent evaluation data or simulations.

<!-- BILINGUAL-UNIT: cmb-cov-2026.data -->
## 2. Primary data object

The primary object is the full harmonic covariance
\[
C_{\ell m,\ell' m'}^{XY}
=
\langle a_{\ell m}^{X}a_{\ell' m'}^{Y*}\rangle,
\qquad X,Y\in\{T,E,B\}.
\]

Priority is TT + TE + EE full covariance and off-diagonal topology information.
BB is secondary unless an independent UBT derivation predicts an enhanced B-mode
signature.

<!-- BILINGUAL-UNIT: cmb-cov-2026.freeze -->
## 3. Frozen analysis requirements

Before final evaluation, freeze:

- multipole range and sky treatment;
- topology parameter range;
- the \(H_2\) oscillatory null parameterization;
- the \(H_3\) UBT filter and all tunable constants;
- covariance regularization;
- likelihood/test statistic;
- multiple-testing correction and failure threshold.

Tuning and evaluation data or simulations must be separate. Negative variants are
reported rather than retuned away.

<!-- BILINGUAL-UNIT: cmb-cov-2026.impl -->
## 4. Repository implementation

The fixed-model comparator is
experiments/falsification/cmb_full_covariance_compare.py.

It evaluates realified covariance models using:

- Gaussian harmonic-space log likelihood;
- likelihood differences between fixed models;
- Gaussian KL divergence;
- positive-definite covariance regularization.

Regression checks are in tests/test_cmb_full_covariance_protocol.py.

The comparator deliberately does not tune model parameters.

<!-- BILINGUAL-UNIT: cmb-cov-2026.exit -->
## 5. Exit criterion

**Positive:** \(H_3\) beats \(H_2\) on an independent evaluation set with the statistic
and parameter ranges frozen in advance and survives the look-elsewhere correction.

**Negative:** \(H_3\) does not beat \(H_2\), or the effect disappears under
full-covariance/null-model controls.

External benchmark: R. Himeno, A. J. Nishizawa, K. Ichiki,
*Limited Impact of CMB B-mode Polarization on Constraints on Cosmic Topology*,
arXiv:2610.05960.
