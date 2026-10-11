# Physical-observable algebra and second covariant jet: stabilizer test

Date: 2026-10-12. Research-only AI-assisted note. No canonical claim promotion.

## Setting

Let V be a non-null Lorentz vector and e_mu=(1/s)D_mu V an invertible tetrad on a smooth patch (s>0). Let omega be a metric-compatible Lorentz connection and omega'=omega+C with C_mu in so(1,3), satisfying C_mu V=0 pointwise. Here D_mu denotes the connection acting on the internal Lorentz index only when applied to V and on internal indices of further derivatives; the coordinate-index connection, if supplied, is kept fixed for the comparison. e and g are unchanged.

## Lemma 1: second internal covariant jets separate stabilizer shifts

As D'_nu V=D_nu V, we find

 D'_mu D'_nu V - D_mu D_nu V = C_mu D_nu V = s C_mu e_nu.

If this vanishes for every mu,nu and e is invertible, then for every mu C_mu annihilates a complete Lorentz basis and hence C_mu=0. Consequently the full second covariant jet separates all nonzero stabilizer shifts.

This statement is about a fixed configuration and an entire second jet; it does NOT say an arbitrary scalar contraction of the second jet is sensitive to every C. One may restrict observable data to metric and its Levi–Civita curvature, thereby deliberately forgetting the extra connection; this is an additional physical equivalence rule.

## Lemma 2: connection curvature and torsion generically distinguish shifts

F'=F + D_omega C + C wedge C; T'=T + C wedge e. Small-loop parallel transport varies with F. An explicit counterexample with unchanged Minkowski metric and nonzero stabilizer curvature is in stabilizer_curvature_holonomy_counterexample.md.

## Consequence for quotient proposals

The quotient (V,omega)~(V,omega+C) with C V=0 is consistent as a relation on the restricted kinematical observables (V,DV,g) at a given configuration. It is **not** automatically a symmetry of the covariant differential algebra that includes D²V or parallel transport. The equivalence may also fail to respect subsequent evolution unless a dynamics preserving the quotient is established.

The stabilizer Lie algebra for non-null V has dimension three at each point, giving twelve pointwise connection components; this count is not a count of propagating particles and should not be confused with SU(3).

## Decision framework

A. Metric-only option: formulate physical observables from e,g and the Levi–Civita connection of g, and **prove** that all Theta equations and matter couplings descend to this quotient; otherwise such restriction is a postulate.

B. Connection-physical option: include D²Theta, torsion/curvature, or holonomies; then stabilizer shifts are generally distinct and need independently selected equations or constraints.

C. Hybrid: the stabilizer sector might be auxiliary and eliminated by constraints. This cannot be assessed without those constraints and a physical action or equivalent dynamical law.

## Next tests

1. Inventory the exact canonical UBT master equations and their dependence on D²Theta and connection curvature; avoid interpreting notation alone as an observable postulate.
2. Ask whether the equations are invariant under omega->omega+C with C V=0 on the non-null patch.
3. Check closure under variations/evolution, not just equality of the single on-shell metric.
4. If invariance fails, formulate a minimal new axiom selecting connection dynamics; keep separate from already derived facts.

No proof of new dynamical action, GR or particle content is claimed.
