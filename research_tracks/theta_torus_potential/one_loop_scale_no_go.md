<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# One-loop torus scale-modulus audit

Date: 2026-10-09  
Status: exact scaling audit; previous self-dual stabilisation claim superseded

## Setup

For an isotropic flat three-torus with common radius R, omit the zero mode and
write the spectral zeta function of the scalar Laplacian as

\[
 Z_R(s)=\sum_{n\in\mathbb Z^3\setminus\{0\}}
 \left(\frac{|n|^2}{R^2}\right)^{-s}
 =R^{2s}E_3(s),
\]

where E_3 is the standard cubic Epstein zeta function.

The analytically continued Epstein zeta satisfies

\[
 \boxed{E_3(0)=-1}.
\]

Hence

\[
 Z_R'(0)=2\log R\,E_3(0)+E_3'(0)
 =-2\log R+E_3'(0),
\]

and

\[
 \boxed{
 \log\det{}'(-\Delta_R)
 =-Z_R'(0)
 =2\log R-E_3'(0).
 }
\]

Overall 2 pi conventions can shift the additive constant but do not change the
R dependence.

## Consequence 1 — no one-loop scale minimum

Any one-loop quantity proportional to the logarithm of this determinant has
only logarithmic R dependence.  In particular the historical choice

\[
 V_{1\rm loop}(R)=-\frac12\log\det{}'(-\Delta_R)
\]

gives

\[
 V_{1\rm loop}(R)=-\log R+\text{constant},
\]

which is monotone and has no isolated stationary point.

Thus a massless determinant of the scale-rescaled Laplacian alone cannot
dynamically select a finite value of R.

## Consequence 2 — inversion symmetrisation gives a flat direction

Assume, as an additional symmetry hypothesis, an inversion

\[
R\mapsto \frac{R_0^2}{R}.
\]

Symmetrising the logarithmic potential gives

\[
\frac12\left[
V(R)+V\!\left(\frac{R_0^2}{R}\right)
\right]
=\text{constant}.
\]

Therefore

\[
\boxed{\partial_R V_{\rm sym}=0\quad\text{for every }R,}
\]

not only at R=R_0.

The self-dual value R=R_0 is the unique fixed point of the inversion map, but
a fixed point of a symmetry is not by itself a dynamically selected minimum.

## Consequence 3 — separate three different modular variables

The historical file mixed three distinct objects:

1. canonical UBT complex time tau_UBT=t+i psi;
2. a candidate geometric torus-shape modulus tau_mod=i R_psi/R_t, which exists
   only if an additional compact Euclidean-time cycle R_t is actually part of
   the derived geometry;
3. the exact heat-kernel Jacobi modulus

\[
\boxed{
\tau_J(s)=\frac{i s}{\pi R_\psi^2},
}
\]

which follows directly from the KK heat trace.

These variables must remain distinct until an action-level relation is proved.

## Updated P4 target

The one-loop overall scale determinant is therefore a no-go for stabilising
R_psi by itself.

A viable theta-energy selection mechanism must instead introduce a genuinely
nontrivial dimensionless modulus, for example:

- a shape modulus at fixed volume;
- anisotropic radii or a complex structure modulus;
- masses/interactions/backreaction that break pure scale covariance;
- higher-loop or nonperturbative terms derived from the UBT action.

Only after such a modulus and its effective potential are derived is it
meaningful to test square, hexagonal or other modular fixed points for actual
minima.

## Status ledger

- GAP-RPSI-ONELOOP-SCALE: CLOSED AS NO-GO — the isolated determinant has no
  finite scale minimum.
- GAP-RPSI-INVERSION-SELECTION: CLOSED AS NO-GO — inversion symmetrisation of
  the logarithmic scale potential is flat and does not select the self-dual
  point dynamically.
- GAP-TORUS-SHAPE-POTENTIAL: OPEN — derive a genuine action-level shape/modulus
  potential and certify its minima.
