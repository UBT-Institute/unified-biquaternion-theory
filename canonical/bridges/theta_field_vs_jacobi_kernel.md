<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Fundamental Theta field versus Jacobi theta kernels

Date: 2026-10-09  
Status: canonical type/notation audit

## Core field

The active minimal UBT field is
\[
\Theta(q,\tau_{\rm UBT})\in\mathbb C\otimes\mathbb H,
\qquad \tau_{\rm UBT}=t+i\psi.
\]
It has four complex coefficients.  The capital Greek letter Theta is the
name of the field; it does not by itself assert that every field
configuration is a Jacobi theta function.

## Exact Jacobi object currently established

Compactification of the internal circle produces the free KK heat trace
\[
K_\psi(s)=\sum_{n\in\mathbb Z}e^{-s n^2/R_\psi^2}
=\vartheta_3\!\left(0\mid\frac{i s}{\pi R_\psi^2}\right).
\]
This is an ordinary Jacobi theta constant and has the standard
Poisson/modular transformation law.

That exact statement concerns a spectral trace derived from the compact
circle. It is not a proof that the full interacting field Theta is a modular
form, a Jacobi form, a mock theta function, or a Weil theta lift.

## Candidate full-field theta kernels

Research constructions such as vacuum correlators of the form
\[
\langle0|\Theta(0,t+i\psi)\Theta^\dagger(0,t)|0\rangle
\]
require a quantized UBT Hilbert/Fock space, vacuum, operator ordering and
dynamical calculation. Until those are supplied their identification with a
Jacobi or mock-modular object is speculative.

## Consequence

- Modular properties of the KK heat trace are exact spectral mathematics.
- Modularity of the full UBT field/action remains open.
- Mock-theta/resurgent methods should be applied only after an actual
  action-derived kernel with the relevant transformation defect is obtained.
- The notation Theta must never be used as evidence for a Jacobi-theta
  functional form.

## Status

- GAP-THETA-NAME-CONFLATION: CLOSED — the fundamental field and a Jacobi theta
  function are distinct mathematical types.
- GAP-THETA-HEAT-KERNEL-CLASS: CLOSED [L1 in the free compact-circle spectral
  sector] — the free S1_psi heat trace is an ordinary Jacobi theta constant.
- GAP-THETA-FULL-MODULAR-CLASS: OPEN — classify only after the full
  action-derived quantum/spectral kernel is specified.
