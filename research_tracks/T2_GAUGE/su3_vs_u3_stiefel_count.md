<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Why the minimal moving-frame redundancy is SU(3), not U(3)

**Status:** exact degree-count and homogeneous-space theorem.

## 1. Minimal Stiefel size

Let a complex \(N\times3\) frame \(Z\) satisfy
\[
Z^\dagger H Z=-I_3
\]
for a nondegenerate ambient Hermitian form with at least three negative
directions.

The frame has
\[
6N
\]
real components.

The Hermitian orthonormality constraint supplies
\[
9
\]
real equations.

Quotienting by local \(SU(3)\) removes
\[
8
\]
gauge directions.

Therefore the physical real dimension is
\[
\boxed{
d_{SU(3)}=6N-17.
}
\]

A normalized non-null biquaternion has seven real angular variables.

Setting
\[
6N-17=7
\]
gives uniquely
\[
\boxed{N=4.}
\]

Thus a \(4\times3\) Stiefel frame is the unique minimal complex three-frame
construction with local \(SU(3)\) redundancy that reproduces exactly the seven
normalized degrees of freedom of one biquaternion.

Adding the radial mode restores
\[
7+1=8
\]
real physical variables.

## 2. What changes for U(3)

If the local frame redundancy were instead \(U(3)\), its dimension would be
nine.

For \(N=4\),
\[
\boxed{
24-9-9=6.
}
\]

One additional real degree of freedom would be gauged away.

That missing mode is precisely the phase of the normalized timelike vector.

## 3. Vector versus ray stabilizer

Let
\[
n^\dagger Gn=1.
\]

The stabilizer of the **specific normalized vector** \(n\) inside \(SU(1,3)\)
is
\[
\boxed{SU(3).}
\]

Therefore
\[
\boxed{
SU(1,3)/SU(3)
}
\]
is the seven-real-dimensional space of normalized timelike vectors, including
their complex phase.

If only the complex line/ray
\[
[n]=\{e^{i\alpha}n\}
\]
is retained, the stabilizer is the maximal compact subgroup
\[
S(U(1)\times U(3))
\simeq U(3),
\]
and the quotient has six real dimensions:
\[
\boxed{
SU(1,3)/U(3).
}
\]

Thus:
\[
\boxed{
\text{vector }n
\Rightarrow SU(3),
\qquad
\text{ray }[n]
\Rightarrow U(3).
}
\]

## 4. Determinant/volume interpretation

For an oriented frame
\[
g=(n,Z)\in SU(1,3),
\]
the condition
\[
\det g=1
\]
couples the phase of \(n\) to the determinant phase of the three-frame.

A right transformation
\[
Z\to Zh
\]
with
\[
h\in SU(3)
\]
preserves the determinant and leaves \(n\) unchanged.

If instead
\[
h\in U(3),
\]
then generally
\[
\det h\ne1.
\]

To keep the full \(4\times4\) frame in \(SU(1,3)\), the normal must transform
with the compensating phase
\[
n\to(\det h)^{-1}n.
\]

So the extra \(U(1)\subset U(3)\) acts precisely on the normal/vector phase.

This is the Stiefel version of the previously proved volume-form reduction
\[
U(3)\to SU(3).
\]

## 5. Relation to an abelian phase sector

The frame current naturally decomposes as
\[
C_\mu
=
C_{\mu,0}
+i a_\mu I_3,
\]
with
\[
C_{\mu,0}\in su(3)
\]
and
\[
a_\mu\in\mathbb R.
\]

The traceless part is the hidden-local colour connection candidate.

The trace is the phase/singlet direction.

If a future action derives an independent local \(U(1)\) gauge redundancy for
this phase, the combined local group can be written globally as
\[
\boxed{
U(3)\simeq
\frac{SU(3)\times U(1)}{\mathbb Z_3}.
}
\]

This is a geometric group-theory bridge only.

It does **not** identify the phase \(U(1)\) with electromagnetic \(U(1)\) or
Standard-Model hypercharge without a separate charge-normalization and matter
representation derivation.

## 6. UBT consequence

The present one-biquaternion field count naturally favors:
- a rank-three colour frame with local \(SU(3)\);
- one additional phase/singlet mode.

This matches the exact seven-dimensional normalized timelike coset without
introducing extra physical UV degrees of freedom.

The result independently supports keeping the colour and abelian phase
questions separate until the action fixes their coupling and global quotient.

Verification:
\`verification/su3_vs_u3_stiefel_count_check.py\`.
