<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Pre-registration style experimental protocol; no positive UBT claim is made.
UBT-AI-PROVENANCE-END
-->

# CMB full-covariance falsification protocol

**Date:** 2026-10-09  
**Status:** protocol draft — freeze before evaluation

## Objective

Test whether a UBT theta/prime-gated cosmological signature contains information beyond
ordinary compact topology and beyond a generic oscillatory primordial spectrum.

## Null hierarchy

\[
\begin{aligned}
H_0&=\Lambda{\rm CDM}\text{, trivial topology},\\
H_1&=\text{compact topology with standard primordial spectrum},\\
H_2&=\text{compact topology with generic oscillatory primordial spectrum},\\
H_3&=\text{UBT theta/prime-gated model}.
\end{aligned}
\]

A result is UBT-specific only if \(H_3\) outperforms the properly tuned \(H_2\) on
independent evaluation data or simulations.

## Primary data object

Do not reduce the topology test to diagonal power spectra alone. The primary object is
the harmonic covariance
\[
C_{\ell m,\ell' m'}^{XY}
=
\langle a_{\ell m}^{X}a_{\ell' m'}^{Y*}\rangle,
\qquad X,Y\in\{T,E,B\}.
\]

Priority order:
1. TT + TE + EE full covariance;
2. off-diagonal topology statistics;
3. BB as a secondary channel unless a UBT derivation predicts an enhanced B-mode
   signature.

## Frozen analysis requirements

Before looking at the final evaluation set, freeze:

- multipole range;
- masks and foreground treatment;
- topology parameter range;
- oscillatory-null parameterization;
- UBT theta/prime filter and all tunable constants;
- covariance regularization;
- likelihood/test statistic;
- multiple-testing correction;
- failure threshold.

Use separate tuning and evaluation realizations. Report every frozen variant, including
negative results.

## Recommended statistics

At minimum compare:

- Gaussian harmonic-space log likelihood;
- likelihood ratio or \(\Delta\chi^2\);
- KL divergence between model covariances where numerically stable;
- calibration on null simulations;
- sensitivity to covariance regularization and sky cut.

## External benchmark

R. Himeno, A. J. Nishizawa, K. Ichiki,
Limited Impact of CMB B-mode Polarization on Constraints on Cosmic Topology,
arXiv:2610.05960.

That work is a methodological benchmark: in an idealized cubic three-torus analysis,
primordial B modes add only marginal topology information, while topology is encoded in
off-diagonal harmonic covariance. It does not validate any UBT model.

## Exit criteria

**Positive:** \(H_3\) beats \(H_2\) on an independent evaluation set with a pre-frozen
statistic and survives look-elsewhere correction.

**Negative:** \(H_3\) does not beat \(H_2\), or the effect disappears under
off-diagonal covariance/null-model controls. Record the falsification rather than
retuning the model.
