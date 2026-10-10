<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Critical-origin obstruction for the Stiefel colour frame

**Status:** exact geometry/measure theorem. It downgrades the naive
\(\rho\to0\) vector-manifestation path from an exact continuation to a singular
critical-limit candidate.

## 1. Cone structure of the timelike field space

On the timelike branch write
\[
\Theta=\rho n,
\qquad
\rho>0,
\qquad
n^\dagger Gn=1.
\]

For the positive timelike metric candidate,
\[
K_\Theta^+(d\Theta,d\Theta)
=
d\rho^2+\rho^2 ds_7^2,
\]
where \(ds_7^2\) is the positive metric on
\[
SU(1,3)/SU(3).
\]

Thus the timelike field space is a metric cone over the normalized orbit.

## 2. Exact Jacobian

For a cone metric with a seven-dimensional base,
\[
ds^2=d\rho^2+\rho^2 g_{ij}(y)dy^idy^j,
\]
one has
\[
\det g_{\rm cone}
=
\rho^{14}\det g_7.
\]

Therefore
\[
\boxed{
\sqrt{\det g_{\rm cone}}
=
\rho^7\sqrt{\det g_7}.
}
\]

The local field-space measure is
\[
\boxed{
d\mu_\Theta
\propto
\rho^7\,d\rho\,d\mu_{SU(1,3)/SU(3)}.
}
\]

At \(\rho=0\) the angular Jacobian vanishes and the polar/Stiefel change of
variables loses invertibility.

## 3. The normalized frame is undefined at the origin

The moving normal
\[
n=\Theta/\rho
\]
and the rank-three frame \(Z\subset n^{\perp_h}\) are defined only for
\(\rho>0\).

At \(\Theta=0\), every normalized direction corresponds to the same raw field
value.

Therefore the map
\[
\Theta
\longleftrightarrow
(\rho,Z/SU(3))
\]
is one-to-one only on the punctured timelike cone.

## 4. Homogeneous-frame attempt

Define
\[
W=\rho Z.
\]

Since
\[
Z^\dagger GZ=-I_3,
\]
one obtains
\[
\boxed{
W^\dagger GW=-\rho^2I_3.
}
\]

At \(\rho=0\),
\[
W^\dagger GW=0.
\]

Hence the columns of \(W\) must span a totally isotropic complex subspace of
the Hermitian space of signature \((1,3)\).

## 5. Witt-index obstruction

For a Hermitian form of signature \((1,3)\), the maximal dimension of a
totally isotropic complex subspace is
\[
\boxed{1.}
\]

An elementary proof takes a nonzero null vector to
\[
w=(1,1,0,0)^T.
\]

If
\[
v=(v_0,v_1,v_2,v_3)^T
\]
is both null and orthogonal to \(w\), then
\[
v_0-v_1=0.
\]

The null condition then reduces to
\[
-|v_2|^2-|v_3|^2=0,
\]
so
\[
v_2=v_3=0,
\qquad
v\propto w.
\]

Thus three mutually orthogonal null columns cannot remain independent:
\[
\boxed{
\rho=0
\Longrightarrow
\operatorname{rank}_{\mathbb C}W\le1.
}
\]

The rank-three colour frame collapses at the radial origin.

## 6. Consequence for radial vector manifestation

The scaling
\[
\rho_0\to0,
\qquad
c_3,c_V\propto\rho_0^2,
\qquad
m_B^2\to0
\]
remains an interesting approach to the origin from the timelike side.

But the endpoint is not contained in the same smooth rank-three Stiefel chart.

Therefore
\[
\boxed{
\text{radial massless scaling}
\neq
\text{proved exact HLS phase at }\rho=0.
}
\]

Keeping a full independent \(Z\) and \(B\) exactly at the origin would enlarge
the description unless the path integral derives a controlled collective
extension through the singular map.

## 7. Path-integral warning

The exact collective rewrite must include the Jacobian
\[
\rho^7.
\]

A treatment that drops this Jacobian, sets \(\rho=0\), and nevertheless keeps
a full independent rank-three Stiefel frame is not an exact rewrite of the
original one-biquaternion measure.

## 8. Better nonperturbative target

The safer primary target is a finite-radius quantum-disordered HLS regime in
which local configurations remain on the timelike branch and the rank-three
frame is well defined.

The phase must be classified by gauge-consistent or gauge-invariant
observables, not by a local gauge-variant frame expectation value.  In an
unfixed formulation Elitzur's theorem forbids using such a local VEV as a
physical order parameter.

The desired conditions remain
\[
m_{B,\rm ren}^2=0,
\qquad
Z_B>0,
\qquad
M_\beta^2>0,
\]
but they should first be sought without forcing the raw radial field through
\(\rho=0\).

The radial endpoint is retained as a secondary critical-limit candidate that
requires a separately proven collective extension.

## 9. Revised P2 implication

The preferred question is now
\[
\boxed{
\text{Does the finite-radius constrained Stiefel theory possess a
quantum-disordered local-SU(3) phase with a massless interacting gauge
kernel?}
}
\]

If not, a controlled extension through the singular origin would be required.

Verification:
verification/su3_stiefel_origin_obstruction_check.py
