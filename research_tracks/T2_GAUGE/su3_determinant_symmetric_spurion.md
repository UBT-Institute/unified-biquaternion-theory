<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Symmetric-spurion form of the determinant anisotropy

**Status:** exact representation-theory form of the \(SU(3)\to SO(3)\)
physical anisotropy.

## 1. Complex triplet

Write a physical tangent triplet as
\[
z=x+iy,
\qquad
x,y\in\mathbb R^3.
\]

Then
\[
z^\dagger z=x^2+y^2
\]
and
\[
\operatorname{Re}(z^Tz)=x^2-y^2.
\]

Hence
\[
\boxed{
\|{\rm Im}\,z\|^2
=
\frac12
\left[
z^\dagger z-\operatorname{Re}(z^Tz)
\right].
}
\]

Introduce a symmetric tensor
\[
\Sigma=\Sigma^T
\]
and write
\[
Q_\Sigma(z)
=
\frac12
\left[
z^\dagger z-\operatorname{Re}(z^T\Sigma z)
\right].
\]

The determinant-sensitive vacuum corresponds to
\[
\boxed{\Sigma=I_3.}
\]

## 2. Representation

Under
\[
z\to Uz,
\qquad
U\in SU(3),
\]
covariance of
\[
z^T\Sigma z
\]
requires
\[
\Sigma\to U^{-T}\Sigma U^{-1}
\]
(or the equivalent active convention).

Thus \(\Sigma\) is a complex symmetric rank-two tensor, the
\[
\boxed{\mathbf6}
\]
of \(SU(3)\).

Its vacuum value is a physical spurion/background, not a failure of the local
frame redundancy.

## 3. Stabilizer

For
\[
\Sigma=I_3,
\]
the invariance condition is
\[
U^TI_3U=I_3.
\]

Together with
\[
U^\dagger U=I_3,
\qquad
\det U=1,
\]
this implies that \(U\) is real orthogonal with determinant one.

Therefore
\[
\boxed{
\operatorname{Stab}_{SU(3)}(\Sigma=I_3)=SO(3).
}
\]

## 4. Dynamical gauge-field consequence

If an autonomous hidden-local connection
\[
B_\mu\in su(3)
\]
exists and the symmetric tensor has a covariant kinetic term, then
\[
D_\mu\Sigma
=
\partial_\mu\Sigma
+
B_\mu\Sigma
+
\Sigma B_\mu^T
\]
in the anti-Hermitian convention.

At the constant background
\[
\Sigma=I_3,
\]
\[
\boxed{
D_\mu\Sigma=B_\mu+B_\mu^T.
}
\]

A term
\[
\kappa_\Sigma
\operatorname{tr}
(D_\mu\Sigma)^\dagger(D^\mu\Sigma)
\]
therefore produces the vector mass quadratic form
\[
\kappa_\Sigma
\operatorname{tr}
(B_\mu+B_\mu^T)^\dagger
(B^\mu+B^{T\mu}).
\]

## 5. Exact Gell--Mann spectrum

Use
\[
B_\mu=iA_\mu^aT_a,
\qquad
T_a=\lambda_a/2.
\]

The matrices
\[
T_2,T_5,T_7
\]
are antisymmetric under transpose, so
\[
B+B^T=0
\]
in those directions.

The matrices
\[
T_1,T_3,T_4,T_6,T_8
\]
are symmetric, so
\[
B+B^T=2B.
\]

With
\[
\operatorname{tr}(T_aT_b)=\frac12\delta_{ab},
\]
all five broken directions have equal norm in this isotropic spurion model.

Therefore the gauge-boson mass matrix has
\[
\boxed{
\operatorname{rank}=5
}
\]
with:
- three exactly zero \(SO(3)\) directions;
- five degenerate broken directions before further interactions split them.

## 6. Scope

The exact rank-five pattern is representation-theoretic.

The coefficient
\[
\kappa_\Sigma
\]
is **not** yet derived from the UBT determinant potential itself.

The pointwise \(\lambda_2\) term establishes the physical symmetric spurion/
anisotropy.  Deriving a kinetic coefficient for that spurion after the HLS
connection becomes dynamical is a separate action/1PI calculation.

Thus the safe statement is:
\[
\boxed{
\lambda_2\ne0
\text{ supplies the }{\bf6}\text{-type }SO(3)\text{ physical background;}
}
\]
if that background participates dynamically in the gauge EFT, its canonical
Higgs pattern is rank five.

Verification:
verification/su3_symmetric_spurion_rank5_check.py
