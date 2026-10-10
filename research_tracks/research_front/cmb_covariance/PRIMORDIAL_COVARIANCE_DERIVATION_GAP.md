# Primordial covariance derivation boundary for UBT CMB H3

**Status:** exact logical boundary and derivation specification.

The current UBT cosmology track derives/embeds FRW background dynamics but does
not yet derive a UBT-specific primordial covariance.

## 1. Background equations do not determine fluctuations

Let
\[
S[\Theta]
\]
be expanded around a cosmological background
\[
\Theta=\bar\Theta+\delta\Theta.
\]

The background solves
\[
\left.\frac{\delta S}{\delta\Theta}\right|_{\bar\Theta}=0.
\]

Primordial fluctuations are governed instead by the second variation
\[
\boxed{
S^{(2)}
=
\frac12
\int
\delta\Phi_A\,
\mathcal H^{AB}[\bar\Theta]\,
\delta\Phi_B,
}
\]
after all constraints and gauge redundancies are treated.

Knowledge of the first-variation/background equation does not determine the
Hessian \(\mathcal H\), and even a known Hessian does not determine a quantum
two-point function until an initial state/boundary condition is selected.

Therefore
\[
\boxed{
\text{FRW background recovery}
\not\Rightarrow
P_{\mathcal R}(k,k').
}
\]

This is a logical consequence of variational theory, not a numerical issue.

## 2. Missing gauge-invariant curvature variable

For CMB scalar perturbations the theory interface is the gauge-invariant
comoving curvature perturbation
\[
\mathcal R
\]
or an exactly equivalent canonical scalar variable.

Current UBT files contain background FRW ansätze and phenomenological
modification parameters, but no action-derived map
\[
\boxed{
\delta\Theta
\longrightarrow
\mathcal R
}
\]
after solving the lapse/shift, connection, split-jet and other constraint
sectors.

Without this map, a spectrum for a raw Theta component is not yet a CMB
primordial curvature spectrum.

## 3. Required second-order derivation

The minimum H3 derivation must:

1. choose an admissible FRW background that solves the same finalized action;
2. decompose \(\delta\Theta\), tetrad/metric and connection variables into
   scalar/vector/tensor sectors;
3. identify infinitesimal gauge redundancies;
4. integrate out or solve all nondynamical constraints;
5. construct the physical gauge-invariant scalar variable(s);
6. derive the reduced quadratic action.

Schematically, for physical scalar modes \(q_n\),
\[
\boxed{
S_{\rm scalar}^{(2)}
=
\frac12
\int d\eta\,
\left[
q'^\dagger K q'
-
q^\dagger \Omega^2 q
\right].
}
\]

For a compact/topological mode basis the matrices \(K_{nn'}\) and
\(\Omega^2_{nn'}\) need not be diagonal.

## 4. Quantum state is an independent datum unless derived

For a Gaussian initial state at \(\eta_0\),
\[
\Psi[q]
\propto
\exp\left(
-\frac12 q^\dagger W q
\right),
\qquad
\operatorname{Re}W>0.
\]

Its equal-time covariance is
\[
\boxed{
\langle q q^\dagger\rangle
=
\frac12(\operatorname{Re}W)^{-1}
}
\]
in the canonical normalized coordinates.

Different positive matrices \(W\) give different primordial covariances while
leaving the same classical FRW background unchanged.

Thus a UBT H3 prediction needs an action/regularity/ground-state principle that
selects \(W\), or an equivalent mode-function vacuum prescription.

## 5. Standard GR/inflation inheritance is H0-like, not a new UBT signal

If the UBT branch reduces exactly to GR plus a standard single-field
inflationary sector and the usual adiabatic vacuum is imposed, the reduced
equation has the familiar form
\[
v_k''+
\left(
k^2-\frac{z''}{z}
\right)v_k=0,
\qquad
v=z\mathcal R.
\]

Then the usual nearly scale-invariant diagonal spectrum is inherited.

That is a consistency result:
\[
\text{UBT contains standard primordial physics on that branch}.
\]

It is not a UBT-specific H3 signature.

A distinctive H3 requires a derived change in at least one of:
- the physical scalar Hessian;
- the topology/mode basis;
- the quantum initial state;
- the transfer from Theta to \(\mathcal R\);
- or a derived cross-mode covariance.

## 6. Compact psi does not by itself imply a spatial primordial cutoff

A compact internal coordinate
\[
\psi\sim\psi+2\pi R_\psi
\]
gives KK masses
\[
m_n^2\sim n^2/R_\psi^2
\]
for fields propagating in that internal direction.

It does **not** by itself imply that the ordinary three-dimensional comoving
spatial momentum satisfies
\[
k\ge1/R_\psi.
\]

A spatial infrared cutoff requires an independently derived spatial topology,
boundary condition or mode-mixing equation.

Therefore the historical ansatz
\[
P_{\rm UBT}(k)
=
P_{\rm std}(k)
[1-e^{-(kR_\psi)^2}]
\times(\text{winding resonances})
\]
is phenomenological until this spatial/internal map is derived.

## 7. Full-covariance output

Once the physical mode functions and state are derived, define the primordial
mode covariance
\[
\boxed{
P^{\rm UBT}_{nn'}
=
\langle
\mathcal R_n
\mathcal R_{n'}^*
\rangle.
}
\]

This is the frozen theory object consumed by the H0--H3 statistical pipeline:
\[
C_{\rm CMB}
=
A P^{\rm UBT} A^\dagger+N.
\]

No prime/theta filtering is permitted after observing the evaluation CMB data.

## 8. Status of existing phenomenological code

The file
\`experiments/simulations/prediction_models/ubt_primordial_spectrum.py\`
is retained as a historical phenomenological model.

Its own comments already identify:
- \(A_{\rm winding}\) as empirical;
- the correction \(F_\psi\) as a phenomenological parametrization;
- scenarios B/C as Hubble-scale/free-radius choices.

It must not be cited as an action-level derivation of
\(P_{\rm UBT}\).

## 9. P3 closure target

P3 is theory-complete only when the repository contains:

\[
\boxed{
S^{(2)}_{\rm physical\ scalar}
\quad+\quad
\text{state prescription}
\quad+\quad
\delta\Theta\to\mathcal R
\quad\Longrightarrow\quad
P^{\rm UBT}_{nn'}.
}
\]

Until then the full-covariance statistical pipeline is intentionally blocked
from an H3 real-data verdict.
