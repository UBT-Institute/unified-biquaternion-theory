<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# SU(1,3)-enhanced potential branch and the exact role of lambda_2

**Status:** exact pointwise-potential theorem.  It identifies the coefficient
that obstructs the seven-dimensional SU(1,3)/SU(3) vacuum manifold.

## 1. The classified quadratic invariant is the Lorentz-Hermitian norm

Write
\[
\Theta=z_0+z_1 I+z_2 J+z_3 K
\]
and use the standard matrix realization
\[
X=
\begin{pmatrix}
z_0+i z_1 & z_2+i z_3\\
-z_2+i z_3 & z_0-i z_1
\end{pmatrix}.
\]

The classified quadratic invariant
\[
H(X)
=
\operatorname{Tr}(X^\sharp X^\dagger)
\]
obeys the exact identity
\[
\boxed{
H(X)
=
2\left(
|z_0|^2-|z_1|^2-|z_2|^2-|z_3|^2
\right)
=
2h_B(\Theta,\Theta).
}
\]

Thus \(H>0\) is precisely the timelike stratum used by the moving-colour
carrier construction.

## 2. Existing nonzero minimum is timelike

For
\[
\lambda_1\ge0,\qquad
\lambda_2>0,\qquad
\mu<0,
\]
the existing vacuum theorem defines
\[
r^2=\frac{-\mu}{4\lambda_1+\lambda_2}
\]
and has representative
\[
X_0=i r I_2.
\]

At this point
\[
H(X_0)=2r^2,
\qquad
h_B(\Theta_0,\Theta_0)=r^2>0.
\]

Therefore the pointwise minimum lies on the timelike branch on which
\[
E_{\Theta_0}=\Theta_0^{\perp_h}
\]
has complex rank three and the conditional moving-carrier SU(3) construction
is well defined.

This does not prove an admissible spacetime vacuum; the existing tetrad-rank
warning remains.

## 3. The determinant invariant is not SU(1,3)-invariant

The full classified potential is
\[
V=V_0+\mu H+\lambda_1H^2+\lambda_2|\det X|^2.
\]

The first three terms are functions only of the \(SU(1,3)\)-invariant
Hermitian norm \(H\).  The determinant term contains additional
biquaternionic structure.

A direct witness is
\[
q=(1,0,0,0),
\qquad
q'=(\sqrt2,1,0,0).
\]
Both have
\[
h_B(q,q)=h_B(q',q')=1,
\]
so they lie on the same unit timelike \(SU(1,3)\) orbit.  But
\[
|\det X(q)|^2=1,
\qquad
|\det X(q')|^2=9.
\]

Therefore
\[
\boxed{
|\det X|^2
\text{ is not an }SU(1,3)\text{ invariant.}
}
\]

Consequently \(\lambda_2\neq0\) explicitly breaks the enlarged
\(SU(1,3)\) symmetry of the pointwise potential.

## 4. Symmetry-enhanced branch lambda_2=0

Set
\[
\boxed{\lambda_2=0},
\qquad
\lambda_1>0,
\qquad
\mu<0.
\]

Then
\[
V(H)=V_0+\mu H+\lambda_1H^2
\]
depends only on the \(SU(1,3)\)-invariant norm.

Completing the square gives
\[
V
=
V_0-\frac{\mu^2}{4\lambda_1}
+
\lambda_1(H-H_*)^2,
\qquad
H_*=-\frac{\mu}{2\lambda_1}>0.
\]

Hence the complete pointwise minimum is
\[
\boxed{
H(\Theta)=H_*.
}
\]

After normalizing the radius, this vacuum manifold is
\[
\boxed{
SU(1,3)/SU(3).
}
\]

No determinant constraint remains.

## 5. Exact Hessian rank

At a minimum, \(dV/dH=0\).  Therefore
\[
\delta^2 V
=
2\lambda_1\,dH\otimes dH.
\]

On the nonzero timelike level set \(dH\neq0\), so in the eight-real-dimensional
field space
\[
\boxed{
\operatorname{rank}\operatorname{Hess}V=1,
\qquad
\dim\ker\operatorname{Hess}V=7.
}
\]

The seven flat directions are exactly tangent to the unit-timelike orbit:
one real singlet phase direction plus six real directions forming a complex
three-dimensional tangent carrier.

This matches
\[
\mathfrak{su}(1,3)/\mathfrak{su}(3)
\cong
\mathbf3_{\mathbb C}\oplus\mathbf1_{\mathbb R}
\]
as a real \(SU(3)\)-module.

By contrast, the existing \(\lambda_2>0\) vacuum theorem has Hessian rank four
and only four zero directions.  The determinant term lifts three of the seven
coset directions.

## 6. Why this branch matters for colour

The \(\lambda_2=0\) branch is the first pointwise-potential branch in which the
exact \(SU(1,3)/SU(3)\) collective geometry is also the actual vacuum
degeneracy of the potential rather than merely a redundant parametrization of
the timelike stratum.

This gives a much cleaner candidate origin for the charged coset triplet.

However it is **not yet a derived action choice**.

Selecting \(\lambda_2=0\) merely because it produces SU(3) would be circular.
The theory must independently explain why the allowed invariant
\(|\det X|^2\) is absent.

## 7. Radiative-stability question

Because \(|\det X|^2\) is allowed by the smaller declared
\(U(1)\times SL(2,\mathbb C)\) symmetry, loops will generically regenerate a
nonzero \(\lambda_2\) unless the **full microscopic action** possesses an
exact enlarged symmetry that forbids it.

Therefore the viable enhanced branch requires:

1. the kinetic/measure/constraint sector to respect the same \(SU(1,3)\)
   enhancement or another exact selection rule;
2. the renormalized effective action to preserve \(\lambda_2=0\);
3. a healthy kinetic metric for the seven coset directions;
4. compatibility with the nondegenerate tetrad and GR branch.

Without such protection, \(\lambda_2=0\) is a tuning rather than an
explanation.

## 8. Next theorem target

The next decisive action-selection test is:

\[
\boxed{
\text{Can the finalized kinetic and measure sector be made exactly
}SU(1,3)\text{-invariant while retaining a healthy physical Hessian?}
}
\]

If yes, \(\lambda_2=0\) becomes symmetry-protected and the coset colour route
is substantially strengthened.

If no, the current renormalizable potential generically breaks the enlarged
coset symmetry and the SU(3) colour interpretation remains only geometric.

Verification:
\`verification/su3_su13_potential_branch_check.py\`.
