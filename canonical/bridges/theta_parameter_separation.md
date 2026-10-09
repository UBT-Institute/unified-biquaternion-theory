<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Theta parameter separation: physical complex time versus Jacobi modular parameter

**Status:** authoritative bridge/status note for the October 2026 theta audit.

This file separates three objects that older UBT material sometimes denoted by
the same symbol \(\tau\).

## 1. Canonical physical complex time

Canonical UBT uses
\[
\boxed{
\tau_{\rm UBT}=t+i\psi,
}
\]
with
\[
[t]=[\psi]=\text{length}
\]
in natural units.

The coordinate \(\psi\) is a physical/internal dynamical variable in the
canonical complex-time formulation.  In compact branches it is identified
modulo a circle period.

Therefore \(\tau_{\rm UBT}\) is a **dimensionful physical coordinate**.

## 2. Jacobi modular parameter

The classical Jacobi function uses a dimensionless lattice parameter
\[
\boxed{
\tau_J\in\mathbb H,
\qquad
\operatorname{Im}\tau_J>0.
}
\]

For the convention
\[
\vartheta_3(0|\tau_J)
=
\sum_{n\in\mathbb Z}
e^{\pi i n^2\tau_J},
\]
the parameter \(\tau_J\) is dimensionless.

Hence
\[
\boxed{
\tau_J\ne\tau_{\rm UBT}
}
\]
canonically.

An equality would require an explicit dimensionful scale and a map derived
from the action/spectral problem.

## 3. Exact heat-kernel identification

For a free compact circle of radius \(R_\psi\),
\[
Z_H(s)
=
\sum_{n\in\mathbb Z}
\exp\!\left(
-\frac{s n^2}{R_\psi^2}
\right),
\qquad s>0.
\]

This is exactly
\[
\boxed{
Z_H(s)
=
\vartheta_3(0|\tau_J),
\qquad
\tau_J=
\frac{i s}{\pi R_\psi^2}.
}
\]

This is the established UBT theta structure.

Here:
- \(s\) is heat/proper time;
- \(R_\psi\) is the compactification radius;
- \(\tau_J\) is the dimensionless Jacobi parameter;
- \(\psi\) is the coordinate on the compact circle.

The coordinate \(\psi\) itself is **not** the imaginary part of this
\(\tau_J\).

## 4. Global obstruction to identifying psi with Im tau_J

A compact coordinate obeys
\[
\psi\sim\psi+2\pi R_\psi.
\]

But a Jacobi modular parameter must remain in
\[
\operatorname{Im}\tau_J>0.
\]

A point moving around a physical circle therefore cannot globally be the
positive imaginary part of a Jacobi lattice parameter.

Moreover, physical complex time is dimensionful while \(\tau_J\) is
dimensionless.

Thus the identification
\[
\tau_J=t+i\psi
\]
can only be a reduced, rescaled, local model after explicitly declaring:
- the scale that makes the variable dimensionless;
- the patch with positive imaginary part;
- the loss or reinterpretation of the physical circle periodicity.

It is not a canonical identity.

## 5. Correct modular group for the convention used in the bridge

For
\[
\vartheta_3(\tau)
=
\sum_{n\in\mathbb Z}e^{\pi i n^2\tau},
\]
the standard transformations include
\[
\vartheta_3(\tau+1)=\vartheta_4(\tau),
\]
\[
\vartheta_3(\tau+2)=\vartheta_3(\tau),
\]
and
\[
\vartheta_3(-1/\tau)
=
(-i\tau)^{1/2}\vartheta_3(\tau)
\]
with the standard square-root multiplier convention.

Therefore \(\vartheta_3\) alone is not a scalar modular form for the full
\(SL(2,\mathbb Z)\).

Its natural scalar modular group is the theta subgroup
\[
\boxed{
\Gamma_\theta
=
\langle S,T^2\rangle.
}
\]

Reducing modulo 2,
\[
SL(2,\mathbb F_2)
\]
has order six, while the image of \(\Gamma_\theta\) is
\[
\{I,S\}
\]
of order two.  Hence
\[
\boxed{
[SL(2,\mathbb Z):\Gamma_\theta]=3.
}
\]

Older UBT wording calling this an index-2 subgroup is incorrect.

Under the full modular group the theta constants
\[
(\vartheta_2,\vartheta_3,\vartheta_4)
\]
are permuted/mixed with multiplier phases.  The natural full-group object is
therefore vector-valued rather than one scalar \(\vartheta_3\).

## 6. Gamma_0(4) convention warning

Another common convention is
\[
\theta(\tau)
=
\sum_{n\in\mathbb Z}
e^{2\pi i n^2\tau}
=
\vartheta_3(0|2\tau).
\]

This rescaled function is commonly described as a weight-\(1/2\) modular form
on \(\Gamma_0(4)\) with multiplier/character.

Therefore statements about \(\Gamma_0(4)\) and statements about
\(\Gamma_\theta\) are not contradictory when the argument convention is
changed consistently.

They must not be mixed while keeping the same symbol \(\tau\).

## 7. T^3 theta product

For a standard cubic three-dimensional lattice heat/spectral sum,
\[
Z_{T^3}(\tau_J)
=
\vartheta_3(0|\tau_J)^3.
\]

It has weight \(3/2\) under the same theta subgroup, with the corresponding
multiplier:
\[
Z_{T^3}(-1/\tau_J)
=
(-i\tau_J)^{3/2}Z_{T^3}(\tau_J).
\]

This is standard mathematics **if** \(\tau_J\) is a genuine spectral/lattice
parameter.

It does not prove that physical UBT complex time \(t+i\psi\) is that modulus.

## 8. The reduced finite weighted amplitude is not generically modular

The bridge also uses
\[
S_s(\tau_J)
=
\sum_{n=0}^{N-1}
a_n^{(s)}e^{\pi i n^2\tau_J}.
\]

For arbitrary finite \(N\) and arbitrary coefficients \(a_n^{(s)}\):

- the sum is an entire finite exponential polynomial in \(\tau_J\);
- it obeys \(T^2\) periodicity term by term;
- under \(T\), odd-\(n\) coefficients change sign;
- under \(S:\tau_J\mapsto-1/\tau_J\), it does not generically close into a
  scalar multiple of itself.

Near \(\tau_J=0\), terms
\[
e^{-\pi i n^2/\tau_J}
\]
produce essential exponential behaviour under \(S\), whereas a finite
weight factor times \(S_s(\tau_J)\) has only the original finite exponential
structure.

Therefore
\[
\boxed{
\text{generic finite weighted }S_s
\text{ is not a modular form.}
}
\]

It is best called a finite theta-like spectral projection unless its
coefficients are separately shown to furnish a finite Weil/vector-valued
representation.

## 9. It is not mock-modular by default

Mock modularity is not a synonym for failed ordinary modularity.

A mock modular form requires a precise modular completion/shadow structure.
No such structure has been derived for the generic UBT finite weighted
projection.

Therefore
\[
\boxed{
S_s\text{ is not to be called mock-modular without a derived completion.}
}
\]

The free heat trace is ordinary Jacobi theta mathematics, not mock theta.

## 10. Complex-time holomorphy remains a separate question

The companion result
\`research_tracks/theta_complex_time_classification/holomorphy_lorentz_no_go.md\`
shows that strict frame-independent microscopic Cauchy--Riemann holomorphy in
\(t+i\psi\) is incompatible with generic four-dimensional Lorentz-covariant
dynamics when \(\psi\) is an independent Lorentz scalar.

Thus two independent separations are now required:

1. physical \(\tau_{\rm UBT}\) versus Jacobi \(\tau_J\);
2. reduced theta-sector holomorphy versus microscopic UBT field dynamics.

## 11. Current classification

| Object | Exact classification |
|---|---|
| Free \(S^1_\psi\) heat trace | ordinary Jacobi theta constant |
| Free heat kernel | ordinary Jacobi theta function with elliptic argument |
| Cubic lattice product \(\vartheta_3^3\) | weight \(3/2\) on \(\Gamma_\theta\) in the \(\pi i n^2\tau\) convention |
| \((\vartheta_2,\vartheta_3,\vartheta_4)\) | vector-valued/permuted system under full modular group |
| Generic finite weighted \(S_s\) | finite theta-like exponential polynomial; not modular by default |
| Generic finite weighted \(S_s\) | not mock-modular without a derived completion |
| Fundamental UBT field \(\Theta(q,\tau_{\rm UBT})\) | no modular transformation law derived |
| Full interacting UBT action | no full modular covariance derived |

## 12. Consequence

The established modular content of present UBT is spectral/heat-kernel
mathematics.

The stronger statement
\[
\text{physical complex time is a modular parameter}
\]
remains false as a canonical identification and open only as a separately
derived effective map.

References:
- NIST DLMF, Chapter 20, especially §20.7(viii), theta transformations.
- \`research_tracks/theta_spectral/theta_kernel_foundations.tex\`
- \`research_tracks/alpha_spectral/modular_covariance_of_STheta.tex\`

Verification:
\`verification/theta_parameter_separation_check.py\`.
