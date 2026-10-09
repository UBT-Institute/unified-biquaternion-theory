# P3 CMB covariance pre-registration gate

Status: template — **not yet frozen for real-data evaluation**

The statistical engine is ready, but a real evaluation is forbidden until all
fields below are filled and the resulting JSON configuration is committed and
its SHA-256 recorded before the evaluation data are opened.

## Hypotheses

- H0: baseline LambdaCDM covariance under the selected mask/noise treatment.
- H1: ordinary compact-spatial-topology covariance with no UBT-specific
  modulation.
- H2: H1 plus a generic oscillatory primordial-spectrum family broad enough to
  absorb non-specific oscillatory structure.
- H3: one UBT covariance family derived before evaluation, with every theta,
  prime, topology and amplitude/phase parameter fixed or trained only on a
  disjoint training set.

The scientific comparison of interest is H3 versus H2.  Beating H0 alone is
not sufficient.

## Data representation

Use a **real-packed harmonic vector** so that the likelihood engine works with
an ordinary real symmetric covariance.  The packing convention, sky mask,
beam, noise model and any E/B purification must be frozen in the config.

Primary data: T and E, hence TT/TE/EE covariance blocks.
B is secondary unless a distinct pre-evaluation UBT derivation predicts it.

## Required frozen fields

- dataset/release and map/component-separation product;
- mask and sky fraction;
- harmonic packing convention;
- ell_min and ell_max;
- treatment of monopole/dipole;
- beam/noise covariance;
- topology and orientation priors for H1/H2;
- generic oscillatory family and parameter bounds for H2;
- exact H3 functional form and all parameter bounds;
- training/evaluation split rule and random seed;
- decision statistic;
- look-elsewhere correction;
- success/failure threshold.

## Default decision rule

Until replaced by a stronger frozen rule:

1. H3 parameters may be selected only on training simulations/data.
2. Freeze the full configuration and record its SHA-256.
3. On evaluation data compute log L(H0..H3).
4. Primary contrast is
   Delta log L = log L(H3) - log L(H2).
5. Calibrate its null distribution under H2 simulations using the complete
   frozen selection procedure.
6. Claim evidence for H3 only if the pre-registered tail threshold survives
   the look-elsewhere correction.  Otherwise report a null result or limit.

No post-hoc change of prime set, theta kernel, multipole range, topology,
orientation, phase or filtering is allowed on the evaluation set.
