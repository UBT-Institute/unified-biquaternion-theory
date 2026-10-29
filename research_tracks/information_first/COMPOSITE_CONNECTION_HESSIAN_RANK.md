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

# Composite-connection velocity response: exact Hessian-rank dependence

**2026-10-26, controlled finite-dimensional jet model; not a full UBT closure.**

For eight real velocities u∈R^8 and a Lorentz-invariant internal pairing G of inertia (2,6), define a local linearized covariant velocity w=M u+b, where M=I+C is the Jacobian of the composite D_t Theta with respect to dot Theta; C encodes the velocity dependence of omega[Theta] acting on Theta. Let the quadratic kinetic trial L=(1/2)w^T G w, with M,b independent of u at the evaluation point. Then its exact Hessian is W=M^T G M.

If M is invertible, Sylvester's law guarantees inertia(W)=(2,6): **a regular velocity-dependent redefinition cannot cure ghosts**. If M is singular, rank W can drop, but singularity alone does NOT guarantee a positive-semidefinite reduced spectrum: W may retain negative eigendirections, and Dirac constraint propagation remains essential. For nonlinear w(u), the Hessian receives additional terms sum_A (G w)_A d²w_A/du_i du_j, so M^T G M alone cannot be substituted for a full nonlinear/composite calculation.

Concrete representatives:
- M=I: rank 8, inertia (2,6).
- M=diag(1,1,0,0,0,0,0,0): rank 2, positive semidefinite. This projects out six velocities by fiat; without an independently derived composite connection and propagated constraints it is *not* physical ghost removal.
- M=diag(1,0,1,0,0,0,0,0): rank 2, inertia (1,1); degeneracy coexists with a ghost.

Moreover, a composite tetrad g[Theta] depending on u adds metric, measure and inverse-metric chain-rule terms; its Hessian need not equal this fixed-background expression. If omega[Theta] depends on dot u or higher time jets, Ostrogradsky/degenerate higher derivative constraints must be analyzed explicitly.

**P0 decision:** recover M and the additional metric contributions from a uniquely specified covariant prescription for omega[Theta] and tetrad; otherwise the actual 8-field Hessian is mathematically underdetermined. No unique omega is supplied by the two-carrier transport constraints (residual SO(2), earlier PRs #780/#787). Selection of a projector by its favorable inertia is circular. Information consistency or entropy alone supplies no missing prescription.

Test: tests/test_information_connection_velocity_rank.py.
