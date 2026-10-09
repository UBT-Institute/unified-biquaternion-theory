# UBT CMB full-covariance falsification track

Status: exploratory / pre-registration design.

This track supersedes diagonal-only power-spectrum searches as the primary
topology discriminator. Existing 2D FFT and comb experiments remain archived
as exploratory precursors.

## Hypotheses

- H0: LambdaCDM, simply connected.
- H1: ordinary compact topology with standard primordial spectrum.
- H2: compact topology plus a generic oscillatory primordial spectrum.
- H3: the pre-specified UBT theta/prime-gated signal family.

A UBT claim requires H3 to beat H2 out of sample, not merely H0.

## Primary statistic

Use the full harmonic covariance
[
C^{XY}_{\ell m,\ell' m'}=
\langle a^X_{\ell m}(a^Y_{\ell'm'})^*\rangle,
\quad X,Y\in\{T,E,B\}.
]

Priority order: TT + TE + EE, then BB unless the theory predicts a BB-specific
effect.

## Anti-overfitting rules

- freeze topology, prime set, theta kernel and all filter parameters before
  evaluation;
- use simulation/training data for tuning and an independent evaluation set;
- include look-elsewhere correction for any family search;
- publish null results;
- compare likelihood, KL divergence or Bayes factor under all H0-H3 models.

## Exit criterion

A reproducible pipeline plus one of:
1. an out-of-sample H3 discriminator that survives H2;
2. a quantitative upper bound excluding the tested UBT signal family.

No observed anomaly is called an UBT prediction unless it was pre-specified.

## Spatial-topology gate

Canonical local flat-FRW recovery does not select a global spatial topology. The internal S1_psi fibre is not a cosmic spatial torus.  Therefore H1/H2 are external null/competitor models, while H3 must remain UNDEFINED until a UBT spatial-topology or other covariance-generating mechanism is independently derived. See spatial_topology_gate.md.
