# Composite timelike branch: exact zero velocity Hessian and primary momentum constraint

**2026-10-26, conditional exact Hamiltonian statement.** Applies exclusively to the timelike Lorentz-real minimal composite-metric auxiliary-boost branch in Proposition 9 of research_tracks/action_selection/canonical_family_hamiltonian_bridge.en.md; does NOT claim the full original Theta action is specified.

Write X=i rho I, rho>0 and E_mu^a=N0^-1/2 (partial_mu rho, rho b_mu^1,rho b_mu^2,rho b_mu^3), where b_mu^j is independent and auxiliary. On a nondegenerate fixed-orientation patch let epsilon be the fixed sign of det(E), so sqrt(-g)=epsilon det(E) with epsilon chosen to make the volume positive. Define F(rho)=4 c N0-U(rho), and Q_mu^a=(partial_mu rho,rho b_mu^j). The exact minimal Lagrangian is

L_min = epsilon F(rho) det(Q) / N0^2.

In a t+3 split the ONLY Theta velocity in Q is dot(rho) in Q_0^0. Spatial gradients and all b_mu^j are held fixed in the velocity Hessian. Cofactor expansion gives

det Q = dot(rho) rho^3 det(b_i^j) + R(rho,partial_i rho,b_0^j,b_i^j),

where R does not depend on dot(rho). Hence

pi_rho = dL/d dot(rho) = epsilon F(rho) rho^3 det(b_i^j)/N0^2,
d²L/d dot(rho)² = 0.

The exact scalar primary constraint is

phi_rho := pi_rho - epsilon F(rho) rho^3 det(b_i^j)/N0^2 ≈ 0.

Because no dot(b_mu^j) is present, all 12 auxiliary-boost momenta also vanish as primary constraints in this *particular* unconstrained-component formulation, before classifying primary/secondary, first/second class or checking boost gauge redundancies. The complete Dirac algorithm is required; counting these constraints as physical removed degrees is premature.

In fact Proposition 9 establishes that varying b_mu^j for nonconstant classified U prevents a nondegenerate stationary tetrad on a connected patch. Thus the conditional momentum-constraint result is a property of an action with no allowed nondegenerate stationary solution under those assumptions; it does NOT rescue the minimal composite branch or establish a viable physical Hamiltonian.

For the full eight-real Theta carrier, for a composite connection omega[Theta], or with curvature terms, the Hessian must be recomputed with ALL induced velocity and possibly higher-derivative dependence. Neither the zero Hessian rank nor the exact form of phi_rho generalizes without proof.

**Reproduction:** tools/verify_composite_timelike_primary_constraint.py and tests/test_composite_timelike_primary_constraint.py.
