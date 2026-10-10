<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Tree-level degree-of-freedom no-go for eight perturbative gluons from one biquaternion

**Status:** exact linearized/local second-order no-go.  It does not exclude
genuinely nonperturbative composite poles.

## 1. Microscopic field count

A single biquaternion field has
\[
\dim_{\mathbb C}\mathbb B=4,
\qquad
\dim_{\mathbb R}\mathbb B=8.
\]

Let its real linearized fluctuation vector be
\[
\varphi^A,\qquad A=1,\dots,8.
\]

For a healthy local second-order quadratic action,
\[
S^{(2)}
=
\frac12
\int\frac{d^4p}{(2\pi)^4}\,
\varphi^A(-p)\,
K_{AB}(p)\,
\varphi^B(p),
\]
where \(K(p)\) is an \(8\times8\) inverse-propagator matrix.

At any simple mass-shell pole, the propagator residue is an \(8\times8\)
matrix.  Therefore
\[
\boxed{
\operatorname{rank}(\operatorname{Res}\,K^{-1})
\le8.
}
\]

Constraints or gauge redundancies can only reduce the physical rank.

## 2. Physical gluon rank

A massless spin-one field in four spacetime dimensions has two physical
helicities.

For \(SU(3)\) colour there are eight adjoint directions, so a perturbative
gluon sector has
\[
\boxed{
N_{\rm gluon}^{\rm phys}
=
8\times2
=
16
}
\]
independent physical one-particle polarizations at a fixed null momentum.

Equivalently, the physical transverse residue is
\[
P_{\rm T}\otimes I_8
\]
with
\[
\operatorname{rank}P_{\rm T}=2,
\]
hence
\[
\boxed{
\operatorname{rank}
(P_{\rm T}\otimes I_8)
=
16.
}
\]

## 3. No local invertible rewrite can double the pole rank

An invertible local linear field redefinition
\[
\varphi=R(p)\chi
\]
transforms the propagator by multiplication with nonsingular matrices.  It
does not increase the rank of a residue at a given pole.

Likewise, introducing purely algebraic auxiliary variables and subsequently
eliminating them exactly cannot create additional physical poles or increase
the physical residue rank.

Therefore
\[
\boxed{
8\text{-real-component single-Theta quadratic theory}
\not\cong
8\text{ massless gluons}
}
\]
at tree level through any local invertible/auxiliary rewriting that introduces
no new propagating poles.

## 4. Scope

This theorem applies to:
- a regular perturbative vacuum;
- a local quadratic second-order microscopic action;
- finite-component linearized fields;
- invertible local field redefinitions;
- truly auxiliary variables carrying no independent initial data.

It does **not** exclude:

1. nonperturbative bound states / composite poles in exact correlation
   functions;
2. a nonlocal collective-field effective action with additional low-energy
   poles;
3. higher-derivative dynamics producing extra poles, though these must pass
   ghost/unitarity tests;
4. an enlarged fundamental carrier;
5. emergent gauge fields in a many-body/strongly coupled phase whose
   one-particle spectrum is not visible in the microscopic quadratic Hessian.

## 5. Consequence for UBT colour

The tree-level search for eight independent gluons inside the ordinary
single-Theta Hessian is now closed.

The correct Axiom-A-compatible target is instead:

\[
\boxed{
\text{show that exact/quantum Theta correlators develop an adjoint set of
eight massless spin-one composite poles with two transverse residues each.}
}
\]

This is a much stronger requirement than:
- finding eight algebraic generators;
- deriving a local SU(3) frame redundancy;
- inducing an \(F^2\) invariant in a background effective action.

All three may hold without producing sixteen physical gluon polarizations.

## 6. Required composite-pole benchmark

A successful nonperturbative colour derivation must eventually exhibit a
gauge-invariant/current correlator with an adjoint transverse pole structure
schematically
\[
\langle J_\mu^a(p)J_\nu^b(-p)\rangle
\sim
\delta^{ab}
\left(
\eta_{\mu\nu}
-\frac{p_\mu p_\nu}{p^2}
\right)
\frac{Z}{p^2+i0}
+\cdots
\]
for
\[
a,b=1,\dots,8,
\]
with:
- positive residue \(Z\);
- the correct Ward identities;
- no additional ghost poles;
- universal non-Abelian self-couplings;
- the correct matter coupling and beta function.

Without such new poles, the exact one-field theory cannot contain the
perturbative QCD gluon spectrum.

Verification:
\`verification/su3_tree_level_dof_no_go.py\`.
