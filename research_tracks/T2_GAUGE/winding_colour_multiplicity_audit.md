<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Winding-space audit for an internal colour triplet

Date: 2026-10-09  
Status: exact representation-theory audit

## Result 1 — no SO(3)-equivariant scalar projection

Let the imaginary quaternion directions transform as the standard vector
representation of SO(3):
\[
V_{\rm Im}=\operatorname{Im}\mathbb H\simeq\mathbb R^3.
\]
Let the target imaginary-time scalar be the trivial one-dimensional
representation. A linear map
\[
\Pi:V_{\rm Im}\to\mathbb R
\]
is SO(3)-equivariant iff
\[
\Pi(Rv)=\Pi(v)
\]
for every \(R\in SO(3)\).

The standard three-dimensional vector representation has no nonzero invariant
covector. Equivalently,
\[
\operatorname{Hom}_{SO(3)}(\mathbb R^3,\mathbb R)=0.
\]
Therefore the only SO(3)-equivariant linear scalar projection is
\[
\boxed{\Pi=0.}
\]

The historical equal-sum map
\[
(a,b,c)\mapsto a+b+c
\]
is invariant under permutations of the chosen coordinate axes, but not under
generic SO(3) rotations. It cannot be called isotropic or SO(3)-equivariant.

Exact infinitesimal check is in
verification/chronofactor_projection_and_winding_check.py.

## Result 2 — the S1 winding spectrum has no intrinsic colour triplet

The chronofactor Hilbert space is
\[
\mathcal H_{\rm wind}=L^2(S^1_\psi)
=\overline{\bigoplus_{n\in\mathbb Z}\mathbb C|n\rangle},
\]
with
\[
\hat N|n\rangle=n|n\rangle.
\]

For each \(n\), the eigenspace is one-dimensional over \(\mathbb C\):
\[
\dim_\mathbb C\ker(\hat N-n)=1.
\]

Hence the winding circle by itself supplies no canonical threefold degenerate
multiplicity space on which an internal SU(3) could act while commuting with
\(\hat N\).

Choosing three different windings \(n_1,n_2,n_3\) creates a vector space
isomorphic to \(\mathbb C^3\), but a generic SU(3) rotation mixes states with
different \(\hat N\) eigenvalues and therefore does not commute with the
winding U(1). Such a choice is not an internal colour degeneracy.

## Consequence

The exact factors currently available in the minimal field are:

- the Lorentz-transforming biquaternion index, which cannot host an independent
  internal SU(3) by the same-carrier Lorentz-commutant no-go;
- the single S1 winding index, whose eigenvalues have multiplicity one.

Therefore the present canonical ingredients do not yet derive the required
Lorentz-scalar threefold multiplicity for Standard-Model colour.

A successful bridge must derive an additional threefold degeneracy from the
existing field/mode structure without merely relabelling the Lorentz spatial
triplet or selecting three unequal winding numbers by hand.

This result narrows GAP-SU3-DYN; it does not rule out a derived multiplicity
from a more complete constrained fluctuation spectrum.
