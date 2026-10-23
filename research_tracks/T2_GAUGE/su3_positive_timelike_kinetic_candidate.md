<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Positive timelike-cone kinetic candidate for the SU(1,3)/SU(3) branch

**Status:** exact positivity/covariance theorem for a new action-selection
candidate.  This is not yet the canonical UBT kinetic term.

## 1. Problem

The only constant Hermitian form preserved by the fundamental
\(SU(1,3)\) action is
\[
G=\operatorname{diag}(1,-1,-1,-1),
\]
which is indefinite.

Therefore the naive constant-pairing kinetic term is unsuitable if all
components of Theta are ordinary independent propagating scalar modes.

On the timelike branch, however, the field itself supplies a preferred
positive direction and can be used to define a field-dependent positive
metric.

## 2. Canonical sign-flip metric selected by a timelike Theta

Let
\[
h(\Theta):=\Theta^\dagger G\Theta>0,
\qquad
n:=\frac{\Theta}{\sqrt{h(\Theta)}}.
\]

For any tangent/fluctuation vector \(u\in\mathbb C^4\), define
\[
\boxed{
K_\Theta^+(u,u)
=
-u^\dagger G u
+
2\frac{|\Theta^\dagger G u|^2}{\Theta^\dagger G\Theta}.
}
\]

Equivalently,
\[
K_\Theta^+(u,v)
=
-u^\dagger G v
+
2\frac{(u^\dagger G\Theta)(\Theta^\dagger Gv)}
        {\Theta^\dagger G\Theta}.
\]

The associated Hermitian matrix is
\[
\boxed{
K^+(\Theta)
=
-G
+
2\frac{G\Theta\Theta^\dagger G}
       {\Theta^\dagger G\Theta}.
}
\]

## 3. Exact positivity

Decompose uniquely
\[
u=\alpha n+v,
\qquad
n^\dagger Gv=0.
\]

Then
\[
u^\dagger Gu
=
|\alpha|^2+v^\dagger Gv,
\]
and
\[
n^\dagger Gu=\alpha.
\]

Because the orthogonal complement of a timelike \(n\) is negative definite,
\[
v^\dagger Gv\le0
\]
with equality only for \(v=0\).

Therefore
\[
\boxed{
K_\Theta^+(u,u)
=
|\alpha|^2-v^\dagger Gv>0
}
\]
for every nonzero \(u\).

Thus \(K^+(\Theta)\) is positive definite throughout the timelike stratum.

At the reference point
\[
\Theta=r e_0,
\]
one obtains
\[
\boxed{
K^+(\Theta)=I_4.
}
\]

## 4. SU(1,3) covariance

For
\[
L^\dagger GL=G,
\]
one has
\[
h(L\Theta)=h(\Theta)
\]
and direct substitution gives
\[
\boxed{
K_{L\Theta}^+(Lu,Lv)=K_\Theta^+(u,v).
}
\]

Thus the field-dependent kinetic metric is exactly covariant under the
coefficient-space \(SU(1,3)\) action on the timelike branch.

This evades the constant-pairing no-go because the metric is nonlinear in the
field rather than a fixed invariant matrix.

## 5. Candidate kinetic density

A dimension-four local two-derivative candidate is
\[
\boxed{
\mathcal L_{\rm kin}^{(+)}
=
g^{\mu\nu}
K_\Theta^+(D_\mu\Theta,D_\nu\Theta).
}
\]

Explicitly,
\[
\mathcal L_{\rm kin}^{(+)}
=
-g^{\mu\nu}
(D_\mu\Theta)^\dagger G(D_\nu\Theta)
+
2g^{\mu\nu}
\frac{
[(D_\mu\Theta)^\dagger G\Theta]
[\Theta^\dagger G(D_\nu\Theta)]
}{
\Theta^\dagger G\Theta
}.
\]

No new fundamental field or external mass scale is required.

The price is that the action is nonlinear/rational in Theta and is defined
only on the timelike patch unless a separate null/spacelike continuation is
constructed.

## 6. Quadratic spectrum with the enhanced potential

Combine this kinetic candidate with
\[
V=V_0+\mu H+\lambda_1H^2,
\qquad
\lambda_1>0,\quad\mu<0,\quad\lambda_2=0.
\]

At a constant timelike vacuum, the kinetic metric is positive identity while
the potential Hessian has
\[
\operatorname{rank}=1,
\qquad
\dim\ker=7.
\]

Thus the fixed-background quadratic spectrum contains:
- one positive-kinetic radial massive mode;
- seven positive-kinetic tangent zero modes.

Under the isotropy \(SU(3)\), the seven tangent modes decompose as
\[
\boxed{
\mathbf3_{\mathbb C}\oplus\mathbf1_{\mathbb R}.
}
\]

This is the first simple local action candidate found in the current audit
that simultaneously realizes:
- the timelike \(SU(1,3)/SU(3)\) vacuum geometry;
- a healthy fixed-background kinetic sign;
- the complex triplet plus singlet tangent content.

## 7. Why this is still only a candidate

The construction does not yet satisfy the single-action closure requirements.

Open issues:

1. the canonical tetrad/GR sector still uses sharp/multiplication structures
   that are not fully \(SU(1,3)\)-invariant;
2. the denominator \(h(\Theta)\) is singular at the null stratum;
3. the complete composite Hessian and constraint algebra are unknown;
4. nonlinear sigma interactions in four dimensions require an EFT/UV
   interpretation or a stronger completion;
5. the local \(SU(3)\) frame redundancy still does not by itself generate
   independent massless gluons;
6. the relative normalization of possible singlet/triplet invariant metrics
   is not fixed by \(SU(1,3)\) alone unless the specific sign-flip metric above
   is selected by an additional principle.

Therefore this file proposes a sharply testable action candidate, not a status
upgrade.

## 8. Next test

Insert this kinetic metric into the already classified timelike potential
branch and compute:

1. the exact Euler--Lagrange equations;
2. the full fixed-background Hessian;
3. the compatibility of the Theta-derived tetrad map with the nonlinear
   kinetic metric;
4. whether the one-loop background-frame calculation induces a transverse
   \(SU(3)\) two-point kernel without the hidden-local mass problem.

Verification:
\`verification/su3_positive_timelike_kinetic_check.py\`.
