<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: B_machine_verified
ai_assistance: disclosed
human_review: machine-verification
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact finite-dimensional identities are machine verified; physical action-level identification remains open.
UBT-AI-PROVENANCE-END
-->

# SU(3) dynamics bridge: quaternion spin, quadrupoles, and exact no-go boundaries

**Date:** 2026-10-09
**Track:** T2_GAUGE
**Verification:** verification/su3_spin_quadrupole_check.py

## Status summary

| Statement | Status |
|---|---|
| \(V=\mathbb C\text{-span}\{I,J,K\}\cong\mathbb C^3\) | inherited canonical result |
| Quaternion adjoints generate the spin-1 \(\mathfrak{su}(2)\) triple | PROVED / exact symbolic check |
| Symmetric traceless quadrupoles provide the other five Gell-Mann directions | PROVED / exact symbolic check |
| Combined \(3+5\) operators span \(\mathfrak{su}(3)\) | PROVED / exact symbolic check |
| Minimal \(A\Theta-\Theta B\) derivative contains full \(\mathfrak{su}(3)\) | NO-GO |
| \(U^{-1}dU\) alone gives generic gluon curvature | NO-GO: locally flat |
| Endomorphism-valued colour connection exists kinematically | PROVED as representation statement |
| Such a connection is derived from canonical \(S[\Theta]\) | OPEN: GAP-SU3-DYN |
| \(g_s\) fixed from first principles | OPEN |

## 1. Quaternion-adjoint spin-1 triple

On
\[
V=\mathbb C\text{-span}\{I,J,K\},
\]
define
\[
S_1=\frac{i}{2}\operatorname{ad}_I,\qquad
S_2=\frac{i}{2}\operatorname{ad}_J,\qquad
S_3=\frac{i}{2}\operatorname{ad}_K,
\qquad
\operatorname{ad}_I(v)=[I,v].
\]

Using
\[
[I,J]=2K,\quad [J,K]=2I,\quad [K,I]=2J,
\]
one obtains, in the ordered basis \((I,J,K)\),
\[
S_1=\lambda_7,\qquad
S_2=-\lambda_5,\qquad
S_3=\lambda_2.
\]
Therefore
\[
[S_i,S_j]=i\epsilon_{ijk}S_k.
\]

This is the ordinary spin-1 representation of \(\mathfrak{su}(2)\) carried
canonically by the imaginary quaternion sector. It accounts for three of the eight
Hermitian traceless directions of \(\mathfrak{su}(3)\).

## 2. The missing five directions are quadrupoles

Define
\[
Q_{ij}
=
\frac12\{S_i,S_j\}
-\frac23\delta_{ij}\mathbf 1_3.
\]

The \(Q_{ij}\) are symmetric and satisfy
\[
Q_{11}+Q_{22}+Q_{33}=0,
\]
leaving five independent components. Exact identities are
\[
\begin{aligned}
\lambda_1&=-2Q_{12},\\
\lambda_3&=Q_{22}-Q_{11},\\
\lambda_4&=-2Q_{13},\\
\lambda_6&=-2Q_{23},\\
\lambda_8&=\sqrt3\,Q_{33}.
\end{aligned}
\]
Together with
\[
\lambda_7=S_1,\qquad
\lambda_5=-S_2,\qquad
\lambda_2=S_3,
\]
this gives all eight Gell-Mann directions.

Hence the UBT colour carrier admits the exact operator decomposition
\[
\boxed{\mathfrak{su}(3)=\mathbf3_{\rm spin}\oplus\mathbf5_{\rm quadrupole}}
\]
as a decomposition under the embedded spin-1 \(\mathfrak{su}(2)\).

This is an operator decomposition; it is not the exterior/Fock decomposition
\[
\mathbf1\oplus\mathbf3\oplus\bar{\mathbf3}\oplus\mathbf1.
\]
The two appearances of dimension eight must not be conflated.

## 3. No-go for the minimal two-sided biquaternion derivative

Consider
\[
\rho(A,B)X=AX-XB,
\qquad
A,B\in M_2(\mathbb C)\simeq\mathbb C\otimes_{\mathbb R}\mathbb H.
\]

The kernel is
\[
\ker\rho=\{(c\mathbf1_2,c\mathbf1_2):c\in\mathbb C\}.
\]
Thus
\[
\mathfrak g_{LR}
\cong
(\mathfrak{gl}_2(\mathbb C)\oplus\mathfrak{gl}_2(\mathbb C))/\mathbb C_{\rm diag}
\cong
\mathfrak{sl}_2(\mathbb C)\oplus
\mathfrak{sl}_2(\mathbb C)\oplus\mathbb C.
\]

A Lie-algebra homomorphism
\[
\mathfrak{sl}_3(\mathbb C)\to\mathfrak g_{LR}
\]
cannot be injective. Composition with either \(\mathfrak{sl}_2(\mathbb C)\)
projection has kernel an ideal in the simple algebra \(\mathfrak{sl}_3(\mathbb C)\),
hence is zero or injective; injectivity is impossible because \(8>3\) complex
dimensions. Projection to the abelian centre is zero. Therefore the full map is zero.

The same simplicity argument excludes a real \(\mathfrak{su}(3)\) embedding into the
underlying real minimal left/right algebra.

Therefore
\[
\boxed{\text{a full local colour connection cannot be encoded solely by one }A_\mu\Theta-\Theta B_\mu.}
\]

This is a no-go for that representation class, not for UBT as a whole.

## 4. No-go for a pure Maurer--Cartan gluon field

If a candidate connection is only
\[
\mathcal A=U^{-1}dU
\]
or \(U^\dagger dU\) for unitary \(U\), the Maurer--Cartan equation gives
\[
d\mathcal A+\mathcal A\wedge\mathcal A=0.
\]
Hence
\[
\boxed{\mathcal F=0.}
\]

Such a form can encode a local frame change, holonomy bookkeeping, or a pure-gauge
configuration. It cannot by itself represent a generic dynamical gluon field with
nonzero field strength.

## 5. Kinematically sufficient operator-valued connection

Let
\[
\mathbb C\otimes\mathbb H=\mathbb C\,1\oplus V
\]
with the scalar line a colour singlet. Let \(\Lambda_a\) act as zero on the scalar
line and as \(\lambda_a\) on \(V\). Then
\[
[\Lambda_a,\Lambda_b]=2if_{abc}\Lambda_c.
\]

A kinematically valid colour derivative can therefore be written
\[
\nabla_\mu^{(c)}
=
\partial_\mu-\frac{i g_s}{2}G_\mu^a\Lambda_a.
\]

This only proves that the existing UBT carrier supports the required endomorphism
representation. It does not derive the eight coefficient fields \(G_\mu^a\) from
\(S[\Theta]\).

That action-level derivation is the remaining core of
\[
\boxed{\text{GAP-SU3-DYN: OPEN}.}
\]

## 6. Conditional heat-kernel / Yang--Mills bridge

If the Euclideanized composite \(\Theta\)-Hessian is eventually proved to be a genuine
Laplace-type operator with the above colour connection,
\[
P=-(g^{\mu\nu}\nabla_\mu\nabla_\nu+\mathcal E),
\]
then the standard four-dimensional Seeley--DeWitt coefficient contains a curvature
term proportional to
\[
\operatorname{tr}\mathcal F_{\mu\nu}\mathcal F^{\mu\nu}.
\]

This gives a concrete route by which the same Hessian/heat-kernel programme used for
induced gravity could also generate a Yang--Mills kinetic term.

The implication is conditional until:
1. the colour connection is action-derived;
2. it is present in the full composite Hessian, including chain-rule and gauge-fixing
   terms;
3. normalization and sign are computed.

## 7. Next theorem target

The target is:

> Derive, from the canonical UBT action and no independent gauge-field postulate,
> a non-flat endomorphism-valued connection on \(V\) whose compatibility conditions
> preserve the canonical Hermitian form \(h\) and volume form \(\Omega\).

Success closes GAP-SU3-DYN. Failure should be stated as an action-level no-go.
