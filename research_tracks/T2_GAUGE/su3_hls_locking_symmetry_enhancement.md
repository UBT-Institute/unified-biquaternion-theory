<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Symmetry enhancement at zero HLS locking coefficient

**Status:** exact effective-action symmetry theorem after a dynamical
\(F_B^2\) term exists.

## 1. Two separately invariant sectors

The positive Stiefel/coset action
\[
\mathcal L_A[Z]
\]
is invariant under a local frame transformation
\[
Z\to Zh_Z(x),
\qquad
h_Z(x)\in SU(3)_Z.
\]

This is true without introducing \(B_\mu\).  In particular
\[
P_+\partial_\mu Z
\to
(P_+\partial_\mu Z)h_Z
\]
because the inhomogeneous \(Z\partial_\mu h_Z\) term is annihilated by
\[
P_+Z=0.
\]

The trace/singlet one-form is also invariant under \(SU(3)\) because
\[
\operatorname{tr}(h_Z^{-1}dh_Z)
=
d\log\det h_Z
=
0.
\]

Separately, once quantum dynamics has generated
\[
\mathcal L_B
=
-\frac{Z_B}{4}
\operatorname{tr}F_{\mu\nu}(B)F^{\mu\nu}(B),
\qquad
Z_B>0,
\]
this sector is invariant under an independent local group
\[
SU(3)_B:
\qquad
B_\mu\to
h_B^{-1}B_\mu h_B-h_B^{-1}\partial_\mu h_B.
\]

## 2. The vertical term locks the two groups

The frame connection transforms as
\[
C_{\mu,0}
\to
h_Z^{-1}C_{\mu,0}h_Z+h_Z^{-1}\partial_\mu h_Z.
\]

The operator
\[
\mathcal O_V
=
-\operatorname{tr}(B_\mu-C_{\mu,0})^2
\]
is invariant only when the two transformations are identified,
\[
h_B=h_Z.
\]

Therefore for
\[
c_V\ne0
\]
the symmetry is the diagonal subgroup:
\[
\boxed{
SU(3)_Z^{\rm local}\times SU(3)_B^{\rm local}
\longrightarrow
SU(3)_{\rm diag}^{\rm local}.
}
\]

The HLS mass/locking term is thus a gauge-locking operator.

## 3. Enhanced symmetry at c_V=0

If
\[
\boxed{c_V=0}
\]
while
\[
Z_B>0,
\]
the two sectors decouple and the independent transformations are restored:
\[
\boxed{
SU(3)_Z^{\rm local}\times SU(3)_B^{\rm local}.
}
\]

Hence the zero-locking point has a larger exact local redundancy than the
generic locked theory.

This refines the earlier statement that the HLS mass operator is merely an
allowed relevant operator.

It is allowed by the diagonal HLS symmetry, but its exact zero is a
symmetry-enhanced point of the already-generated two-sector effective action.

## 4. Technical-naturalness consequence

At exactly
\[
c_V=0
\]
there is no field/operator in the minimal truncation coupling the \(Z\) and
\(B\) sectors.

Loops internal to \(\mathcal L_A\) respect \(SU(3)_Z\).

Loops internal to the pure-\(B\) Yang--Mills sector respect \(SU(3)_B\).

Therefore a locking operator cannot be generated additively from the
strictly decoupled theory without another interaction that already breaks the
product symmetry to the diagonal.

Schematically,
\[
\boxed{
\beta_{c_V}
=
c_V\,F(\text{dimensionless couplings})
+\text{terms from other locking operators}.
}
\]

Thus \(c_V=0\) is a technically natural invariant surface provided all other
cross-sector locking operators vanish as well.

## 5. What this does not prove

Canonical power counting still makes \(c_V\) a relevant dimension-two
coefficient.

Therefore generic trajectories starting with
\[
c_V\ne0
\]
do not automatically flow to zero in the infrared.

The symmetry theorem proves stability **on** the zero-locking surface, not
attraction **toward** it.

A QCD-like phase still requires:
- a critical trajectory reaching \(c_V=0\);
- finite \(Z_B>0\) accumulated/generated before or at that transition;
- no other relevant operator that re-locks \(SU(3)_Z\) and \(SU(3)_B\);
- gapped charged frame matter if the low-energy theory is to approach pure
  Yang--Mills.

## 6. Two-stage emergence becomes structurally consistent

The following Wilsonian sequence is now a concrete candidate:

1. **locked regime:** \(c_V/c_3\ne0\), allowing frame fluctuations to generate
   \(Z_B>0\);
2. **critical approach:** the renormalized locking coefficient tends to zero;
3. **enhanced point:** independent
   \[
   SU(3)_Z^{\rm local}\times SU(3)_B^{\rm local}
   \]
   emerges;
4. **frame decoupling:** charged frame/coset excitations become gapped;
5. **low-energy colour:** the \(B\) sector remains as an approximately pure
   \(SU(3)_B\) Yang--Mills theory.

The already-generated \(Z_B\) is a Wilsonian coupling and need not disappear
when the matter source that produced it subsequently decouples.

## 7. Relation to the massless gauge condition

On the enhanced surface
\[
c_V=0
\]
the explicit Stueckelberg/HLS mass operator vanishes.

If the generated Yang--Mills sector contains no other gauge-locking mass
operator, local \(SU(3)_B\) forbids an ordinary Proca mass
\[
\operatorname{tr}B_\mu B^\mu.
\]

Thus once the product-symmetry point is reached, gauge-boson masslessness is
technically protected in the ordinary Yang--Mills sense.

## 8. Revised finite-radius target

The main P2 question becomes:
\[
\boxed{
\text{Can the finite }4\times3\text{ theory flow from a locked regime that
generates }Z_B
\text{ to the symmetry-enhanced surface }c_V=0
\text{ at finite timelike radius?}
}
\]

This avoids the singular raw-field origin and gives a sharper FRG target than
the earlier radial-collapse scenario.

Verification:
verification/su3_hls_locking_symmetry_check.py
