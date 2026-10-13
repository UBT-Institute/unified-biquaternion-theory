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

# Connection stabilizer and integrability audit

Date: 2026-10-12. Research note, AI-assisted, not canonical. Continue PR #661.

## Lorentz-real sector and pointwise nonuniqueness

Assume non-null Lorentz-vector field V (V² != 0), a nondegenerate coframe e, a metric-compatible Lorentz connection omega with D_mu V^a=s e_mu^a and fixed s>0. If omega is one solution, omega'=omega+C generates exactly the same D_mu V if and only if

 C_mu{}^a{}_b V^b=0,  C_mu ab=-C_mu ba.

At any point, for each mu the kernel of so(1,3)->V, A|->A V is the little algebra of V, dimension 3 (so(3) for timelike V, so(1,2) for spacelike V). Hence an affine 12-dimensional pointwise family of compatible omega_mu components survives, provided one solution exists. The little algebra is **not** an additional independent internal Yang-Mills SU(3): it is a stabilizer of V under Lorentz transformations; no independent gluons follow.

A right inverse for perpendicular target W_mu^a=s e_mu^a-partial_mu V^a satisfying V·W_mu=0 is

 omega_mu ab = (W_mu a V_b - V_a W_mu b)/V² + C_mu ab,

with C_mu ab V^b=0, up to index/sign conventions for the connection action. Solvability requires V_a(s e_mu^a-partial_mu V^a)=0, equivalently ∂_mu(V²)=2s V_a e_mu^a. The torsionful Gaussian representer constructs V to meet this necessary condition.

## Integrability does not automatically select C

Commutation gives the identity

 [D_mu,D_nu]V^a=R_mu nu{}^a{}_b(omega)V^b.

Using D_mu V^a=s e_mu^a,

 R_mu nu{}^a{}_b V^b=s(D_mu e_nu^a-D_nu e_mu^a)

when D acts on the internal index only and partial antisymmetrization is used on coordinate indices. The RHS is the tetrad torsion 2-form in components, s T_mu nu^a, with T^a=de^a+omega^a{}_b wedge e^b. Thus

 R_mu nu{}^a{}_b V^b=s T_mu nu^a.

This is a **compatibility identity** for any smooth omega satisfying DV=s e, rather than a new dynamical equation selecting one connection. Under C in the stabilizer, the curvature and torsion generally both change, maintaining the identity. Imposing independent torsion constraints or an equation for curvature could remove degeneracy, but must be separately motivated and may invoke the known torsion-free concurrent-vector obstruction.

## Nuances

- The affine family is nonuniqueness at fixed V and e; local Lorentz gauge also acts on V and e, and is not identical to an arbitrary stabilizer deformation holding both fixed.
- Requiring omega to be the unique Levi–Civita spin connection of e removes C by an **additional** torsion-free equation, and the corresponding generated-tetrad sector has previously established restrictions.
- Topological/holonomy conditions may narrow global solutions but do not follow from this local commutator identity alone.
- For null V the little algebra changes; non-null dimension claims should not be extended without case analysis.
- The prescribed metric may itself be composite g[e]; no Euler–Lagrange dynamics has been derived.

## Research priorities

P0: Preserve exact stabilizer kernel and integrability identity as a connection-selection obstruction.
P1: Classify minimal *independently justified* conditions on torsion/curvature or spectral transport that could break the stabilizer degeneracy without hardcoding GR.
P2: Test whether candidate conditions yield a differentiable operator with suitable physical spectrum and no hidden extra fields.
P3: Only then consider a variational or spectral action and its unavoidable residual normalization freedom.

No GR recovery or unique fundamental action is claimed.
