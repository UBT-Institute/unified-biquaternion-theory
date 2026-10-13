<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Stabilizer deformation is not generically gauge: explicit curvature counterexample

Date: 2026-10-12. Research-only, AI-assisted; no claim promotion.

## Setup
Work on a local Lorentz-vector branch with metric-compatible spin connection omega, non-null V, and invertible tetrad e=s^{-1}DV. Define stabilizer-valued one-form C with C_mu V=0. Then omega'=omega+C preserves DV, e, and the induced metric g for fixed V.

Curvature two-form F(omega)=d omega+omega wedge omega obeys

  F(omega+C) = F(omega) + D_omega C + C wedge C,

where D_omega C=dC+omega wedge C + C wedge omega in matrix-valued exterior-form notation (graded commutator convention).

Torsion T(e,omega)=de+omega wedge e changes by

  T(e,omega+C)-T(e,omega)= C wedge e.

Thus the induced metric remains unchanged but connection curvature and torsion are generically changed.

## Exact local counterexample at a point

Use Minkowski coordinates x^mu on a small patch and omega=0. Choose an affine V^a(x)=v^a+s x^a with v^a non-null, shrink patch so V remains non-null. Then e_mu^a=delta_mu^a (up to normalization convention s) is nondegenerate and g is Minkowski.

Choose a smooth nonzero Lorentz-generator field H(x) in the little algebra of V(x), H(x)V(x)=0, available locally by a smooth Lorentz moving frame. Set

  C = h(x) H(x) dx^2,  h(x)=x^1

in coordinates centered at p=x=0. Then C_mu V=0 identically and C(p)=0, so e remains flat exactly. But

  F'(p)=dC(p)=H(p) dx^1 wedge dx^2,

hence F'_{12}(p)=H(p) !=0 whereas F(omega)=0. Choose H(p) a nonzero spatial rotation in the little algebra for a timelike v; tr(H(p)^2) !=0, so tr(F'_{mu nu}F'^{mu nu}) at p is nonzero (for the specified spacelike 1,2 indices) while the original connection invariant vanishes.

The Levi-Civita Riemann tensor of g is still zero for both configurations. The changed curvature is the curvature of the *torsionful Lorentz connection*, not the Riemann curvature of g. Do not conflate these observables.

## Holonomy consequence
For a small 1-2 loop of oriented area A about p, the parallel-transport holonomy is I + A F'_{12}(p)+O(A^{3/2}) under smoothness conventions (sign depends on transport convention). It is generically nontrivial for omega+C and trivial for omega=0. Gauge-equivalent connections at identical base point have conjugate holonomy; identity cannot be conjugate to a nonidentity. Thus the deformation is not in general an ordinary Lorentz gauge transformation.

## Meaning and limitations

- Connection stabilizer freedom is *not* generically a gauge redundancy of the full spin-connection geometry. Two configurations yield the same e and g but different F, T and parallel transport.
- Whether UBT matter actually couples to F, T or the full connection must be specified before calling these distinctions **experimentally observable**. If every physical observable depends only on metric and its Levi-Civita derivative, the excess connection may become an auxiliary equivalence by an additional physical postulate; this does not follow algebraically.
- Some special flat stabilizer shifts might be pure gauge; the example disproves an **all-shifts-are-gauge** claim.
- We cannot use the stabilizer as emergent SU(3) gluons: little group is dimension-three Lorentz stabilizer.
- This does not select a unique omega or a fundamental action.

## Next tasks

(1) Fix UBT physical observable algebra / allowed parallel transport (metric only vs spin/Theta transport).
(2) Determine whether one can canonically quotient by stabilizer deformations while retaining UBT covariant-Theta dynamics; examine D acting on other fields, and commutator.
(3) If curvature and torsion are physical, identify an independently justified selection law for the 12 stabilizer components.
(4) Keep connection selection before spectral action/physical Hessian.
