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

# Exact Minkowski proxy comparison: metric quotient versus covariant Theta wave equation

Date: 2026-10-12. Working research note, AI-assisted; NOT a canonical UBT master equation.

## Setup and explicit background

Take Lorentz signature (-,+,+,+), s>0, and Minkowski Cartesian coordinates. On a sufficiently small neighborhood of x=0 let

 V^a(x)=v delta^a_0+s x^a, with v!=0, omega_mu{}^a{}_b=0.

Then e_mu{}^a=s^{-1}partial_mu V^a=delta_mu{}^a, g=eta and the metric Levi-Civita curvature vanishes. Work in a patch where V remains timelike.

Let H(x) be a smooth little-algebra generator with H(x)V(x)=0 and H(0)^1{}_2=h, H(0)^2{}_1=-h, all others zero at 0; a smooth local Lorentz-moving frame constructs such H(x). Define a one-form

 C_mu(x)=delta_mu^1 H(x),

and omega'=omega+C. Since C_mu V=0 everywhere, D'_mu V=D_mu V=s e_mu, and e',g' equal e,g.

## Proxy A: metric-only equation

Take E_g[g]=Ric(g), or Einstein tensor G(g), as a **probe** of metric-only differential observables (not a proposed fundamental action). Because g'=g exactly,

 E_g[g']-E_g[g]=0.

Both backgrounds satisfy Ric(g)=0. This proves metric-quotient invariance for any tensor constructed naturally from g and its Levi-Civita derivatives. It does not establish an equation of motion for Theta.

## Proxy B: connection-covariant wave equation

Define P_omega(V)^a := g^{mu nu} (D_mu D_nu V)^a on the internal Lorentz bundle, with the coordinate-index connection of the second derivative held fixed; it is zero in these Cartesian coordinates. The same calculation works with full affine covariantization if its affine connection is kept fixed.

For C_mu V=0,

 (P_{omega+C}-P_omega)(V)^a = s g^{mu nu} C_mu{}^a{}_b e_nu{}^b.

At origin choose C_1=H, e_1=delta_1 and metric g^{11}=1. Therefore

 Delta_C P(V)^2 = s H^2{}_1 = -s h !=0

for h !=0. In the original flat connection, P_omega(V)=0 everywhere since V is affine. The transformed connection thus fails P_{omega'}(V)=0 already at x=0. The two equations do not descend to the same metric quotient.

**Important distinction:** The full connection curvature of omega'=C can be zero or nonzero depending on H(x) and C; this second-jet result does not require a nonzero curvature. A different explicit deformation C=x^1 H(x)dx^2 shows curvature nonuniqueness (see earlier sibling note).

## Explicit algebraic interpretation

At x=0, the nontrivial term is the spatial rotation H acting on the spatial coframe e_1, despite H annihilating the timelike V. Thus first-jet equality does not imply second-jet equality. No added action or fitted coupling was used.

## Implications and limitations

- This is a **counterexample to stabilizer invariance of the proxy wave operator** P_omega V=0, and therefore to treating arbitrary stabilizer C as gauge for all second-order Theta equations.
- It does **not** refute the unknown full UBT master equation: the canonical GR notes distinguish the working kinetic Hessian from a D-composite self-consistency symbol, and GAP-B-MASTER remains open.
- An operator of the form g^{mu nu} nabla^g_mu nabla^g_nu applied to a metric-derived vector is insensitive to C by construction, but may lack independently propagating Theta degrees and uses g already supplied by the coframe.
- This comparison alone does not select a unique connection or spectral functional.

## Next gate

Identify a *source-exact* field equation and its status before using the invariance test to promote or reject canonical dynamics. If no independently selected equation exists, frame the result as underdetermination and seek an additional principle that differentiates connection observables without hardcoding Einstein equations.

Status: exact local proxy test completed, fundamental-action/master-equation selection open.
