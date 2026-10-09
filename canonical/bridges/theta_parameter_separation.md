<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: B_machine_verified
ai_assistance: disclosed
human_review: machine-verification
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Parameter-separation statements are exact; physical extensions remain open.
UBT-AI-PROVENANCE-END
-->

# UBT complex time versus the Jacobi modular parameter

Date: 2026-10-09  
Status: **canonical notation audit + exact heat-kernel theta bridge**

## 1. Two different variables

Canonical UBT uses
\[
\tau_{\rm UBT}=t+i\psi,
\]
where the active canonical interpretation treats \(\psi\) as a compact internal
phase coordinate on \(S^1_\psi\).

A classical Jacobi theta function uses a modular parameter
\[
\tau_J\in\mathbb H
=\{\tau\in\mathbb C:\operatorname{Im}\tau>0\},
\]
for example
\[
\vartheta_3(z|\tau_J)
=\sum_{n\in\mathbb Z}
e^{\pi i\tau_J n^2+2\pi i n z}.
\]

These symbols must not be identified by notation alone.

## 2. Naive identification no-go

The assignment
\[
\tau_J\stackrel{?}{=}\tau_{\rm UBT}=t+i\psi
\]
is not a canonical UBT statement.

The roles and domains are different:

- \(\psi\) is a periodic coordinate modulo the compact fibre period;
- \(\operatorname{Im}\tau_J\) is a positive modulus in the upper half-plane;
- modular transformations act on \(\tau_J\), whereas no such action on physical
  UBT complex time has been derived;
- a Jacobi modulus must be dimensionless after normalization, while \(t,\psi\)
  may carry physical dimensions before scaling.

Therefore the earlier reduced-model replacement
\(\phi\leftrightarrow\psi\) is only a toy-model notation choice, not a
canonical map.

**Status:** GAP-THETA-TAU-NAIVE is CLOSED AS A NOTATION/DOMAIN NO-GO:
the identity map is not justified and is incompatible with the compact-fibre
interpretation unless an additional dimensionless map and domain prescription
are explicitly derived.

## 3. Exact Jacobi parameter already present in UBT

The conditional induced-gravity branch contains the compact-\(\psi\) KK heat
trace
\[
K_\psi(s;R_\psi)
=\sum_{n\in\mathbb Z}e^{-s n^2/R_\psi^2}
=\vartheta_3(0,e^{-s/R_\psi^2}).
\]

Using the convention
\[
\vartheta_3(0|\tau_J)
=\sum_{n\in\mathbb Z}e^{\pi i\tau_J n^2},
\]
the exact modular parameter is
\[
\boxed{
\tau_J(s)=\frac{i\,s}{\pi R_\psi^2}.
}
\]

This is a genuine mathematical identification:
the Jacobi modulus is built from Euclidean proper time \(s\) and the compact
radius \(R_\psi\).  It is **not** the canonical complex time
\(\tau_{\rm UBT}\).

## 4. Modular inversion equals Poisson resummation

The Jacobi S transformation gives
\[
\vartheta_3(0|\tau)
=(-i\tau)^{-1/2}
\vartheta_3(0|-1/\tau).
\]
For
\[
\tau=\frac{i s}{\pi R_\psi^2}
\]
this becomes
\[
\boxed{
\sum_{n\in\mathbb Z}e^{-s n^2/R_\psi^2}
=
\sqrt{\frac{\pi R_\psi^2}{s}}
\sum_{k\in\mathbb Z}
e^{-\pi^2R_\psi^2k^2/s}.
}
\]

Thus modular inversion is exactly the Poisson-resummed KK heat trace, exchanging
the large-\(s\)/small-\(s\) descriptions of the same spectral quantity.

This bridge is directly reusable in:
- induced-gravity coefficient calculations;
- the conditional induced Yang--Mills coefficient;
- UV/IR asymptotics of the compact-\(\psi\) spectrum;
- rigorous estimates of the proper-time integrals.

## 5. Consequence for resurgence / boundary analysis

Any mock-modular or resurgent analysis formulated in terms of the Jacobi
modulus must first specify which UBT object supplies that modulus.

For the established heat-kernel bridge,
\[
\operatorname{Im}\tau_J\to0^+
\quad\Longleftrightarrow\quad
s\to0^+,
\]
so the boundary is the ultraviolet proper-time limit.  It is **not**
automatically the physical limit \(\psi\to0\) of UBT complex time.

Therefore Stokes phenomena or analytic continuation across a modular boundary
cannot be interpreted as propagation into negative imaginary UBT time without
an additional derivation.

## 6. Status of the reduced complex-time theta model

The reduced expression
\[
\sum_n a_n e^{-\pi\psi n^2}e^{\pi i t n^2}
\]
is mathematically a theta-type kernel after suitable dimensionless scaling and
when the damping variable is positive.  It remains a useful bridge/toy model.

It is not currently the canonical full UBT propagator and does not establish
that \(\tau_{\rm UBT}\) itself is a modular parameter.

## 7. Next theorem target

The remaining P1 question is now narrower:

1. identify any additional UBT spectral/lattice kernels;
2. assign each its own modular variable \(\tau_J\);
3. derive its transformation law from the corresponding lattice/quadratic form;
4. test whether any such derived modulus couples nontrivially to
   \(\tau_{\rm UBT}\) through the finalized action.

Only step 4 could establish a physical complex-time/modular bridge.
