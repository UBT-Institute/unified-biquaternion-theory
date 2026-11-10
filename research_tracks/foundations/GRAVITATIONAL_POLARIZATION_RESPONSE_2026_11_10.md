# Observational gate: can existing interferometers miss a UBT mode?

**Status:** methodological research note, 2026-11-10. No third UBT polarization or detector anomaly is claimed.

The standard long-wavelength response of detector I to a metric strain wave is

\[
d_I(t)=\sum_A F_I^{A}(\hat n,\psi)\,h_A(t-\Delta t_I)+n_I(t).
\]

A generic metric-theory classification can allow up to six polarization patterns (two tensor, two vector, two scalar), though interferometric antenna responses can be degenerate for some scalar modes. Two nearly coaligned LIGO detectors do not suffice to distinguish arbitrary polarizations; a differently oriented network helps. This is not a proof that an arbitrary additional mode can hide: tests already constrain particular purely vector/scalar and mixed hypotheses, and observed waveforms are consistent with GR.

**Crucial UBT qualification:** “third canonical pair” in the restricted commutator-square Hamiltonian is neither automatically a third *metric gravitational-wave polarization* nor automatically a detectable strain. First derive the mode eigenvector, its gauge-invariant metric/torsion/connection curvature response, its dispersion and coupling to electromagnetism and interferometer mirrors. A mode coupled only to a new torsion observable may have zero leading interferometric response yet be constrained in other experiments. A frequency-dependent or massive mode needs a separate transfer function.

## Computation requirements

1. Diagonalize the gauge-reduced, full composite Hessian and count physical modes; identify which are tensor/vector/scalar **under the background little group** where valid.
2. Derive the on-shell coupling of each mode to clocks, photons and test masses from the *same* action.
3. Calculate detector response \(F_I^A(f,\hat n)\) (or full transfer function for nonmetric modes), not a freely assumed standard GR tensor antenna.
4. Evaluate identifiability: the network response matrix rank/singular values across frequency, sky directions, detector orientations and noise curves. Null directions mean weak constraints; they are not detections.
5. Compare reproducible simulations to GR-only injections and to established scalar/vector hypotheses; use injections to calibrate detection efficiency and upper limits.
6. State posterior limits and modeling assumptions. Never say “LIGO measured three” or “LIGO cannot see third” without a calculated response and data.

## Reference anchors

- LIGO Scientific Collaboration, GW170814: https://ligo.org/science-summaries/gw170814/
- LIGO–Virgo, Tests of GR and polarizations (O2): https://ligo.org/science-summaries/O2TGR/
- LIGO–Virgo paper (section VIII, six possible metric patterns, response rank): https://dcc.ligo.org/public/0156/P1800316/008/O2_testingGR_v2.pdf
- Analysis of detector-network polarization sensitivity: https://doi.org/10.1103/PhysRevD.110.084057
- Standard interferometer scalar degeneracies: https://doi.org/10.1103/PhysRevX.7.041058

This is a **measurement-model gate**, not a post hoc license to evade negative observations.
