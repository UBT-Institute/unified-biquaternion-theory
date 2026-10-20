<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Lie-closure theorem: raw-carrier Lorentz boosts plus full colour SU(3) force SU(1,3)

**Status:** exact Lie-algebra closure theorem.

## 1. Setup

Work on the raw coefficient carrier
\[
\mathbb B\cong\mathbb C^4
\]
with Lorentz-Hermitian form
\[
G=\operatorname{diag}(1,-1,-1,-1).
\]

Embed the candidate colour algebra as the lower-right stabilizer
\[
\mathfrak{su}(3)
\subset
\mathfrak{su}(1,3)
\]
fixing the reference timelike direction \(e_0\).

From the minimal bimodule intersection, retain the three boost generators
\[
K_i=\frac{i}{2}(L_{e_i}+R_{e_i}),
\qquad e_i\in\{I,J,K\}.
\]

The colour algebra already contains the three spatial rotation generators
\[
J_i=\frac12(L_{e_i}-R_{e_i})
\]
as its \(so(3)\) subalgebra.

## 2. Initial dimension

The real span
\[
\mathfrak s_0
=
\operatorname{span}_{\mathbb R}
\left(
\mathfrak{su}(3),K_1,K_2,K_3
\right)
\]
has dimension
\[
\boxed{\dim_{\mathbb R}\mathfrak s_0=11.}
\]

Every generator satisfies
\[
X^\dagger G+GX=0,
\qquad
\operatorname{tr}X=0,
\]
so
\[
\mathfrak s_0\subset\mathfrak{su}(1,3).
\]

## 3. Exact Lie closure

Close \(\mathfrak s_0\) under commutators.

The first commutator layer increases the real rank to 14.  A second layer gives
\[
\boxed{15}
\]
independent generators.

Since
\[
\dim_{\mathbb R}\mathfrak{su}(1,3)=15
\]
and every generated direction remains in \(\mathfrak{su}(1,3)\),
\[
\boxed{
\operatorname{Lie}
\left\langle
\mathfrak{su}(3),K_1,K_2,K_3
\right\rangle
=
\mathfrak{su}(1,3).
}
\]

This is checked exactly by symbolic matrix commutators and real-rank tests.

## 4. Representation-theoretic meaning

Under the stabilizer \(SU(3)\),
\[
\mathfrak{su}(1,3)
=
\mathfrak{su}(3)
\oplus
\mathfrak m,
\]
where the seven-real-dimensional coset sector decomposes as
\[
\mathfrak m
\cong
\mathbf3_{\mathbb C}\oplus\mathbf1_{\mathbb R}.
\]

The three minimal boost directions are only one real half of the complex
triplet.  Acting on them with the five additional colour generators outside
the \(SO(3)\) subgroup necessarily generates the missing real half.  Further
commutators generate the remaining singlet coset direction.

Thus the enlargement to full \(SU(3)\) cannot remain confined to
\[
SO(3)+3\text{ boosts}.
\]
Lie closure forces the complete \(SU(1,3)\) structure.

## 5. Consequence for raw-carrier unification

This creates a sharp architecture theorem.

Suppose one demands on the same raw four-complex-dimensional carrier:

1. the existing Lorentz boost sector from the minimal biquaternion action;
2. full internal colour \(SU(3)\) acting as the stabilizer of a timelike
   direction;
3. closure under local infinitesimal transformations;
4. preservation of the same Lorentz-Hermitian form \(G\).

Then the smallest closed Lie algebra is not
\[
so(1,3)\oplus su(3).
\]

It is
\[
\boxed{su(1,3).}
\]

Therefore there is no simple direct-product realization of physical Lorentz
and colour on the same raw \(\mathbb C^4\) coefficient carrier with these
actions.

## 6. Conflict with the current UBT core

The separate core audit already establishes that full coefficient-space
\(SU(1,3)\):

- has only the indefinite constant Hermitian invariant \(G\);
- does not preserve the canonical biquaternion sharp/determinant structure;
- is not a symmetry of the current tetrad/GR construction.

Combining the two results gives
\[
\boxed{
\text{raw-carrier Lorentz}
+
\text{full raw-carrier colour }SU(3)
\Longrightarrow
SU(1,3)
\Longrightarrow
\text{conflict with current sharp-based UBT core}.
}
\]

Hence the physical colour group cannot be implemented as just more linear
generators on the same raw biquaternion carrier while keeping the present GR
architecture unchanged.

## 7. Required architectural separation

A viable colour sector must instead act on a distinct structure derived from
the same fundamental field, for example:

- the moving rank-three bundle \(E_\Theta=\Theta^{\perp_h}\);
- its independent/collective local frame bundle;
- a nonlocal or spectral multiplicity space;
- or an enlarged fundamental carrier, which would revise Axiom A.

In such a formulation Lorentz acts on spacetime/raw-field structure while
colour acts vertically on an internal rank-three fibre, rather than both being
linear transformations of the same raw \(\mathbb C^4\) value space.

This theorem therefore strengthens the motivation for a **bundle-separated**
rather than raw-carrier-unified Standard-Model bridge.

Verification:
\`verification/su3_raw_carrier_lie_closure_check.py\`.
