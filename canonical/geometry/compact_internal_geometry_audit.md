<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Compact internal geometry audit: S1 versus historical T3

Date: 2026-10-09  
Status: canonical-scope audit

## Canonical minimal geometry

The active minimal complex-time formulation keeps

\[
\tau_{\rm UBT}=t+i\psi
\]

with a single compact internal phase coordinate

\[
\psi\in S^1_\psi.
\]

Accordingly the canonical winding Hilbert space is

\[
\mathcal H_{\rm wind}=L^2(S^1_\psi),
\]

and the exact compact-fibre heat trace is

\[
K_{S^1}(s)
=\sum_{n\in\mathbb Z}e^{-s n^2/R_\psi^2}
=\vartheta_3\!\left(0\mid\frac{i s}{\pi R_\psi^2}\right).
\]

## Historical extended geometry

Some older files use additional imaginary coordinates chi and xi and therefore
a three-torus

\[
T^3=S^1_\psi\times S^1_\chi\times S^1_\xi.
\]

In the current canonical choice those extra directions belong to the
deprecated/historical full-biquaternion-time extension.  Therefore formulas
such as

\[
K_{T^3}(s)=\vartheta_3^3
\]

and cubic Epstein-zeta constructions are mathematically valid for that
extended model but are not consequences of the minimal canonical
S1_psi theory.

## Consequences

1. The exponent d/2=3/2 obtained from a three-dimensional compact heat kernel
   cannot be cited as a zero-assumption result of the minimal S1_psi theory.
2. A threefold internal colour multiplicity cannot be obtained merely by
   reinterpreting the three historical compact directions.
3. A genuine complex-structure/shape modulus of a two- or three-torus requires
   at least two compact cycles.  The single circle S1_psi has only an overall
   radius, not a Jacobi upper-half-plane shape modulus.
4. Cosmic spatial topology tests (for example an observable spatial T3) are a
   separate physical question and must not be conflated with the internal
   imaginary-time fibre.

## Status

- GAP-COMPACT-MINIMAL: CLOSED — current minimal canonical compact fibre is S1_psi.
- GAP-INTERNAL-T3: CONDITIONAL/HISTORICAL — a compact T3 requires reinstating or
  independently deriving the chi,xi directions from the finalized action.
- GAP-TORUS-SHAPE-POTENTIAL remains OPEN in the minimal theory because no
  multi-cycle internal shape modulus has yet been derived.
