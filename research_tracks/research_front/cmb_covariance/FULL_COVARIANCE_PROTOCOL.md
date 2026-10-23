# Full-covariance CMB protocol: derivation boundary and H0--H3 model interface

**Status:** preregistration/infrastructure theorem. The statistical machinery
is specified; the UBT H3 primordial covariance is not yet derived.

## 1. Existing negative results are retained

Two earlier CMB routes already have useful negative outcomes:

1. the periodic TT comb variant returned a Planck null result
   \(p=0.919\);
2. the simple \(\psi\)-compactification primordial cutoff produced only
   sub-percent low-\(\ell\) suppression in the documented approximation and
   did not explain the observed low-\(\ell\) anomaly.

These results remain constraints on those specific variants. They are not to
be recycled as evidence for a new topology hypothesis.

## 2. Correct full-covariance observable

For CMB field type \(X\in\{T,E,B\}\),
\[
a_{\ell m}^X
=
4\pi i^\ell
\int\frac{d^3k}{(2\pi)^3}\,
\mathcal R(\mathbf k)\,
\Delta_\ell^X(k)\,
Y_{\ell m}^*(\hat{\mathbf k})
\]
in the simply connected continuum notation.

The general covariance is
\[
\boxed{
C_{\ell m,\ell'm'}^{XY}
=
\left\langle
a_{\ell m}^X
(a_{\ell'm'}^Y)^*
\right\rangle.
}
\]

In a finite/discrete mode basis this can always be written
\[
\boxed{
C=A\,P\,A^\dagger+N,
}
\]
where:
- \(P\) is the primordial mode covariance;
- \(A\) contains transfer functions, spherical harmonics, topology mode
  selection and the chosen real/complex vectorization;
- \(N\) is noise/systematic covariance.

This equation is the required interface between UBT theory and the
statistical test.

## 3. Hypotheses

### H0 — LambdaCDM
Primordial covariance is statistically isotropic/diagonal in the standard
continuum basis.

### H1 — ordinary compact topology
Allowed wavevectors are discrete/topology-dependent but primordial statistics
are otherwise standard.

### H2 — compact topology plus generic oscillatory spectrum
Use the same topology as H1 but allow a preregistered nuisance family of
generic smooth/oscillatory primordial modifications.

### H3 — UBT
H3 must provide before evaluation data are inspected an explicit
\[
\boxed{P_{\rm UBT}}
\]
or equivalent fully specified mode covariance derived from UBT theta/prime
dynamics.

Applying a prime or theta filter after seeing \(C_\ell\) data is not a valid
H3 derivation.

## 4. UBT derivation gap

Current UBT materials do not yet derive
\[
P_{\rm UBT}(\mathbf k,\mathbf k')
\]
or its discrete compact-topology analogue.

Therefore the current full-covariance H3 test is
\[
\boxed{\text{BLOCKED BY THEORY TEMPLATE, not by statistics code}.}
\]

No additional Planck scan should be interpreted as an H3 test until this
object exists.

## 5. Real-vector implementation

For robust numerical work, complex harmonic coefficients may be converted to a
real stacked vector
\[
x=(\operatorname{Re}a,\operatorname{Im}a)
\]
after removing redundant reality-constrained modes.

The zero-mean multivariate Gaussian log likelihood is
\[
\log L(x|C)
=
-\frac12
\left[
x^TC^{-1}x+\log\det C+n\log(2\pi)
\right].
\]

For two zero-mean Gaussian models,
\[
\boxed{
D_{\rm KL}(C_1\|C_0)
=
\frac12
\left[
\operatorname{tr}(C_0^{-1}C_1)
-n
+\log\frac{\det C_0}{\det C_1}
\right].
}
\]

## 6. Preregistration requirements

Before using evaluation data:

- freeze the topology family;
- freeze \(\ell_{\max}\) and included TT/TE/EE/BB blocks;
- freeze mask/noise treatment;
- freeze all H3 theta/prime parameters;
- hash the H3 primordial covariance/template;
- fit H2 nuisance parameters on simulations or a disjoint training subset;
- define the held-out likelihood/KL/Bayes statistic;
- define look-elsewhere correction for any remaining model family.

Primary order:
\[
\boxed{TT+TE+EE\quad\text{before}\quad BB}
\]
unless UBT derives a BB-specific signal.

## 7. Decision rule

A positive UBT-specific result requires at minimum
\[
\text{H3 out-of-sample score}>\text{H2 out-of-sample score}
\]
by a preregistered significance/evidence criterion.

H3 beating only H0 is insufficient.

## 8. Code interface

research_tracks/research_front/cmb_covariance/covariance_model_selection.py
implements:
- covariance propagation \(C=APA^T+N\) in real representation;
- strict SPD validation;
- Gaussian log likelihood;
- Gaussian KL divergence;
- frozen-template comparison on held-out samples.

The module intentionally has no built-in UBT template. A call labelled H3 must
supply an externally derived frozen covariance and its hash.

## 9. Next physics target

Derive
\[
\boxed{
\langle\mathcal R_n\mathcal R_{n'}^*\rangle_{\rm UBT}.
}
\]

Only then should Planck/LiteBIRD/CMB-S4 data be used for the new H3 test.
