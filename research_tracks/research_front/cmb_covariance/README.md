# UBT CMB full-covariance falsification track

Status: exploratory / preregistration design.

The primary topology statistic is the full harmonic covariance
\[
C^{XY}_{\ell m,\ell' m'}
=
\langle a^X_{\ell m}(a^Y_{\ell' m'})^*\rangle,
\qquad X,Y\in\{T,E,B\},
\]
not only the diagonal power spectra \(C_\ell\).

## Hypotheses

- H0: simply connected \(\Lambda\)CDM.
- H1: ordinary compact topology with standard primordial spectrum.
- H2: compact topology plus a generic oscillatory primordial spectrum.
- H3: pre-specified UBT theta/prime-gated signal family.

A UBT-specific claim requires H3 to outperform H2 out of sample, not merely H0.

## Priority observables

Use TT + TE + EE first.  BB is secondary unless a UBT derivation predicts a
BB-specific signature.

## Anti-overfitting rules

- Freeze topology, prime set, theta kernel, and filter parameters before
  evaluation.
- Tune only on simulations or a disjoint training subset.
- Include look-elsewhere correction for family searches.
- Publish null results.
- Compare likelihood, KL divergence, or Bayes factor across H0--H3.

## Exit criterion

A reproducible pipeline yielding either:
1. an out-of-sample H3 discriminator that survives comparison with H2; or
2. a quantitative upper bound excluding the tested UBT signal family.

An observed anomaly is not called an UBT prediction unless it was
pre-specified.
