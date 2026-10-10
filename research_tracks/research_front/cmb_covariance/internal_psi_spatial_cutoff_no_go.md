<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Internal-psi compactification does not create a spatial IR cutoff

Date: 2026-10-09  
Status: kinematic no-go for the historical low-l CMB mechanism

## Statement

Compactifying the internal coordinate
\[
\psi\sim\psi+2\pi R_\psi
\]
quantizes momentum in the psi direction,
\[
p_\psi=\frac{n}{R_\psi},\qquad n\in\mathbb Z.
\]

For a free mode on noncompact physical space, separation of variables gives
the standard KK dispersion relation
\[
\boxed{
\omega_n^2(\mathbf k)
=|\mathbf k|^2+m_0^2+\frac{n^2}{R_\psi^2}.
}
\]

The compactification therefore produces a tower of effective masses
\[
m_n^2=m_0^2+\frac{n^2}{R_\psi^2},
\]
not a lower bound on the ordinary three-dimensional spatial wavenumber.

In particular the zero-winding sector obeys
\[
\omega_0^2=|\mathbf k|^2+m_0^2
\]
and permits arbitrarily small positive spatial wavenumber whenever physical space is noncompact.

Hence
\[
\boxed{S^1_\psi\text{ compactification alone does not imply }k_{\min}=1/R_\psi.}
\]

## Consequence for the historical CMB model

The phenomenological factor in experiments/simulations/prediction_models/ubt_primordial_spectrum.py contains an imposed infrared suppression factor and spatial resonances at k=n/R_psi. Neither follows from the KK dispersion relation above.

They can be retained as an exploratory signal family, but not as a derived UBT primordial spectrum.

The historical choice R_psi=c/H_0 is likewise phenomenological unless independently derived from the UBT action.

## What could generate a real spatial cutoff?

A genuine cutoff or discrete spatial spectrum would require additional physics, for example:
- compact or otherwise finite physical spatial topology;
- a boundary condition on physical spatial slices;
- a derived nonlocal transfer kernel coupling internal winding to comoving spatial momentum;
- inflationary initial-state dynamics that suppresses long wavelengths.

None of these follows from the single internal circle by itself.

## Status

- GAP-CMB-PSI-IR-CUTOFF: CLOSED AS NO-GO [L1]. Internal S1_psi compactification alone does not imply a spatial k_min=1/R_psi.
- The numerical low-l calculations based on the imposed cutoff remain reproducible toy-model calculations, but are not UBT predictions.
- The previous comb result remains an exploratory null test, not a core falsification.
- P3 should therefore focus on explicitly derived spatial topology or another pre-specified UBT covariance structure and compare it against ordinary topology plus generic oscillatory null models.
