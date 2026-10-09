<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Kinematic projector identities are exact/machine checked; physical identification and dynamics remain candidate-level.
UBT-AI-PROVENANCE-END
-->

# Composite rank-three projector route to a non-flat colour connection

Date: 2026-10-09  
Status: **kinematic candidate / exact local algebra; action-level selection OPEN**

## Motivation

The fixed colour carrier
\[
V_0=\mathbb C\operatorname{-span}\{I,J,K\}
\]
has canonical stabiliser \(SU(3)\), but a fixed carrier plus an ordinary
derivative gives only a global symmetry. A pure local frame \(U^{-1}dU\) is
flat. To obtain nonzero composite curvature without postulating an independent
fundamental gauge field, the carrier itself must vary.

## 1. Field-dependent rank-three carrier

Let
\[
W=\mathbb C\otimes_{\mathbb R}\mathbb H\simeq\mathbb C^4
\]
with the positive Hermitian algebraic form
\[
H_4(X,Y)=\operatorname{Sc}(X^\dagger Y).
\]
On a patch where a candidate internal biquaternionic field
\(\Phi(x)\neq0\), define
\[
n(x)=\frac{\Phi(x)}{\sqrt{H_4(\Phi,\Phi)}},
\qquad H_4(n,n)=1,
\]
and
\[
P(x)=\mathbf1_W-|n(x)\rangle\langle n(x)|.
\]
Then
\[
P^\dagger=P,\qquad P^2=P,\qquad \operatorname{rank}_{\mathbb C}P=3.
\]

The candidate colour bundle is
\[
E=\operatorname{im}P\subset M\times W.
\]

At the reference configuration \(n=\mathbf1\),
\[
E=\mathbf1^\perp
=\mathbb C\operatorname{-span}\{I,J,K\}=V_0,
\]
so the construction reduces exactly to the canonical algebraic colour carrier.

**Important:** \(\Phi\) is intentionally left distinct from the full physical
\(\Theta\) until the action proves that this normalized direction is the
correct internal variable. Setting \(\Phi=\Theta\) is a candidate
identification, not yet a theorem.

## 2. Projected connection

The canonical projected connection on sections \(s\in\Gamma(E)\) is
\[
\nabla^E s=P\,ds.
\]
In a local orthonormal frame \(e=(e_1,e_2,e_3)\) of \(E\), with
\(e^\dagger e=\mathbf1_3\) and \(ee^\dagger=P\), the connection matrix is
\[
\mathcal A=e^\dagger de\in u(3).
\]
Under a local frame change \(e\mapsto eU(x)\), \(U(x)\in U(3)\),
\[
\mathcal A\mapsto U^\dagger\mathcal A U+U^\dagger dU.
\]
Thus local frame covariance is a genuine bundle gauge redundancy.

Unlike the square pure-frame expression for a fixed carrier, the curvature is
\[
\boxed{
\mathcal F
=d\mathcal A+\mathcal A\wedge\mathcal A
=e^\dagger(dP\wedge dP)e
}
\]
equivalently \(P(dP\wedge dP)P\) on \(E\), and is generically nonzero because
the subspace itself varies.

## 3. Pointwise curvature span

At a reference point \(n=e_0\in\mathbb C^4\), identify
\(E\simeq\mathbb C^3\). A tangent variation of the projective direction is
\(u\in\mathbb C^3\). For two real tangent directions \(u,v\),
the induced curvature endomorphism is, up to the orientation convention,
\[
\boxed{
\mathcal F(u,v)=uv^\dagger-vu^\dagger\in u(3).
}
\]

As \(u,v\) range over the six real tangent directions of
\(\mathbb{CP}^3\), these matrices span all nine real dimensions of \(u(3)\).
Their traceless parts
\[
\mathcal F_0
=\mathcal F-\frac13\operatorname{tr}(\mathcal F)\mathbf1_3
\]
span all eight real dimensions of \(su(3)\).

Exact rank check: verification/su3_projector_connection_check.py.

This proves that the projector geometry is not restricted to the old
quaternion-adjoint \(so(3)\) triplet at the level of curvature.

## 4. Relation to the canonical h/Omega stabiliser

The projected Hermitian structure naturally gives a \(U(3)\) frame bundle.
Locally, the traceless connection/curvature defines an \(su(3)\) component.

A genuine global \(SU(3)\) reduction additionally requires control of the
determinant line / induced complex volume form. The universal quotient bundle
over \(\mathbb{CP}^3\) is not globally an \(SU(3)\) bundle in general; its
central \(U(1)\) part must not be silently discarded. On a spacetime pullback,
global reduction depends on the topology of the pulled-back determinant line.

This global issue is potentially relevant rather than merely inconvenient:
the natural kinematic structure is \(U(3)\), whose local algebra splits as
\[
u(3)=su(3)\oplus u(1).
\]
Any identification of the trace component with hypercharge or another U(1)
requires a separate representation/charge derivation.

## 5. Lorentz-covariance blocker

The simplest identification \(\Phi=\Theta\) on the same spacetime
biquaternion carrier is **not** currently admissible.  The UBT action audit
uses the Lorentz action
\[
X\mapsto SXS^\dagger,\qquad S\in SL(2,\mathbb C),
\]
and explicitly finds that the positive dagger/Hilbert--Schmidt norm is not
invariant under generic boosts.  Therefore the normalized projector built
with \(H_4\) is not automatically Lorentz equivariant when applied directly
to the Lorentz-transforming \(\Theta\) index.

Moreover, the exact same-carrier commutant theorem shows that no nontrivial
internal \(SU(3)\) can commute with the full Lorentz action on that same
\(M_2(\mathbb C)\) index.

Accordingly the projector route survives only in the sharper form:

- first derive a Lorentz-scalar internal/multiplicity variable
  \(\Phi[\Theta]\);
- then form its positive-Hermitian rank-three quotient bundle;
- only then test whether its traceless projected connection is physical colour.

See canonical/su3_derivation/su3_lorentz_commutant_no_go.tex.

## 6. What this does and does not close

### Exact kinematic result

A varying rank-three subbundle constructed from one normalized
biquaternionic direction has a canonical connection with generically nonzero
curvature, and its traceless curvature values can span \(su(3)\).

This bypasses the two earlier kinematic obstructions:
- it is not a single minimal \(AX-XB\) operator;
- it is not a pure Maurer--Cartan connection of a fixed colour space.

### Still open

1. Derive the internal direction \(\Phi[\Theta]\) from the finalized UBT action.
2. Show that physical colour matter lives in \(E=\operatorname{im}P\).
3. Determine whether the pullback determinant line admits the required global
   \(SU(3)\) reduction.
4. Derive the kinetic term and normalisation from the physical Theta Hessian.
5. Establish whether the restricted composite connection has enough physical
   degrees of freedom to reproduce generic QCD, rather than only a constrained
   sigma-model/topological sector.
6. Handle zeros of \(\Phi\), where the normalized projector chart breaks down.

## 6. Immediate falsification test

The route should be rejected as a full QCD mechanism if the action-selected
\(\Phi[\Theta]\) forces \(P\) to be constant, forces
\(P(dP\wedge dP)P=0\), or constrains the resulting curvature so strongly that
the local Yang--Mills solution space cannot be reproduced.

Accordingly this construction is a **candidate bridge**, not a promotion of
GAP-SU3-DYN to proved.
