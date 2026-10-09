<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Zeta-regularized two-torus shape audit

**Status:** corrected massless one-loop determinant theorem.  This supersedes
the older termwise-differentiated claim that the square torus is a local
minimum of the positive one-loop log-determinant.

## 1. Scope

This note concerns a genuine Euclidean two-torus
\[
T^2=\mathbb C/(\mathbb Z+\tau_{\rm mod}\mathbb Z),
\qquad
\tau_{\rm mod}=x+i y,\quad y>0,
\]
with fixed area.

It does **not** identify the physical UBT complex-time coordinate
\[
\tau_{\rm UBT}=t+i\psi
\]
with \(\tau_{\rm mod}\).  The torus exists only in a branch where a second
compact Euclidean/thermal cycle has independently been introduced.

## 2. Zeta-regularized determinant

For the scalar Laplace--Beltrami operator with the zero mode omitted, the
Kronecker-limit formula gives, up to a normalization depending only on the
fixed area,
\[
\boxed{
\det{}'\Delta_\tau
=
C_A\,
y\,|\eta(\tau)|^4.
}
\]

Thus the pure shape functional is
\[
\boxed{
F_{\det}(\tau)
=
\log y+4\log|\eta(\tau)|
}
\]
up to an additive constant.

This is the quantity that must replace the formal divergent expression
\[
\sum_{(m,n)\ne(0,0)}\log\lambda_{m,n}
\]
after zeta regularization.

## 3. Why the earlier termwise Hessian proof is invalid

The older self-dual-torus derivation differentiated the infinite formal sum
term by term and obtained a positive contribution from every mode.

But the sum of those second derivatives is ultraviolet divergent.  Zeta
regularization is not equivalent to summing the unregularized positive
termwise Hessians.

Indeed, the correctly regularized result has the opposite curvature in the
rectangular aspect-ratio direction at the square point.

Therefore the sign of the old termwise second variation is not a valid
regularized stability proof.

## 4. Rectangular tori

Restrict to
\[
\tau=i y,
\qquad y>0.
\]

For unit area,
\[
\det{}'\Delta_{iy}
=
y|\eta(iy)|^4.
\]

A rigorous theorem of Faulhuber shows
\[
\boxed{
y|\eta(iy)|^4
\le
|\eta(i)|^4,
}
\]
with equality only at
\[
\boxed{y=1.}
\]

Thus the square torus is the unique **maximum** of the determinant among
rectangular unit-area tori.

Consequently, for the standard bosonic one-loop effective action
\[
\Gamma_1
=
+\frac12\log\det{}'\Delta,
\]
the square point is a local **maximum** in the rectangular shape direction,
not a minimum.

If one instead defines an opposite-sign phenomenological functional
\[
-\frac12\log\det{}'\Delta,
\]
the square becomes a rectangular minimum.  That sign choice must be derived
from the physical path integral and cannot be changed merely to obtain
stability.

## 5. Full two-dimensional modulus

Among all flat tori of fixed area, the determinant is uniquely maximized, up to
modular equivalence, by the hexagonal/equilateral lattice
\[
\boxed{
\tau_{\hex}
=
e^{i\pi/3}
=
\frac12+i\frac{\sqrt3}{2}
}
\]
(or the equivalent point \(-\tfrac12+i\tfrac{\sqrt3}{2}\)).

The square point
\[
\tau=i
\]
is therefore not the global determinant extremum in full moduli space.

A direct high-precision evaluation of
\[
F_{\det}(x,y)=\log y+4\log|\eta(x+i y)|
\]
gives the local Hessian at the square point
\[
\boxed{
\operatorname{spec}
\operatorname{Hess}F_{\det}(i)
\approx
\{+0.2982113,\,-1.2982113\}.
}
\]

Hence the square point is a **saddle** in the full \((x,y)\) modulus plane:
- negative curvature in the rectangular/aspect-ratio direction;
- positive curvature in a shear direction.

At the hexagonal point,
\[
\operatorname{spec}
\operatorname{Hess}F_{\det}(\tau_{\hex})
\approx
\{-0.6666667,-0.6666667\},
\]
consistent with its local maximum of the determinant.

The numerical Hessians are verification/diagnostic values; the global
maximization theorem is external classical mathematics.

## 6. Consequence for the bosonic effective action

For a Gaussian real bosonic mode,
\[
Z\propto(\det{}'\Delta)^{-1/2},
\qquad
\Gamma_1=-\log Z
=
+\frac12\log\det{}'\Delta.
\]

Since
\[
y|\eta(\tau)|^4\to0
\]
toward the cusp \(y\to\infty\),
\[
\Gamma_1\to-\infty
\]
for the isolated massless determinant.

Therefore the pure massless bosonic determinant has **no finite global
minimum in torus shape moduli**.

It does not dynamically select the square torus or the hexagonal torus as a
stable vacuum by itself.

Additional terms are required to obtain a bounded finite minimum.

## 7. Massive/interacting caveat

For
\[
P=-\Delta+M^2+\mathcal E
\]
the determinant is no longer given solely by the massless eta formula.

The old termwise positivity argument is still insufficient, because the
regularized determinant must be computed before differentiating the physical
effective action.

Therefore the massive/interacting shape potential remains open and must be
derived with a regulator consistent with the finalized UBT Hessian.

## 8. Revised P4 status

The following are now closed:

- **overall one-loop scale selection:** no-go in the isolated scale-rescaled
  determinant;
- **square-torus minimum from the massless determinant:** no-go;
- **termwise positive-Hessian proof:** invalid after proper regularization;
- **physical complex time = torus modulus:** no-go without an independent
  compact Euclidean cycle and action-derived map.

What remains open is narrower:
\[
\boxed{
\text{derive a genuine, bounded }
V_{\rm eff}(\tau_{\rm mod},\bar\tau_{\rm mod})
\text{ from the finalized UBT Hessian/interactions.}
}
\]

Only then is it meaningful to ask which square, hexagonal, or other modular
point is dynamically selected.

## References

- B. Osgood, R. Phillips, P. Sarnak,
  *Extremals of determinants of Laplacians*,
  J. Functional Analysis 80 (1988), 148--211.
- M. Faulhuber,
  *Extremal determinants of Laplace--Beltrami operators for rectangular
  tori*, Math. Z. 297 (2021), 175--195, arXiv:1709.06006.
- Kronecker limit formula / Dedekind eta representation of the flat-torus
  zeta determinant.

Verification:
\`verification/theta_torus_regularized_shape_check.py\`.
