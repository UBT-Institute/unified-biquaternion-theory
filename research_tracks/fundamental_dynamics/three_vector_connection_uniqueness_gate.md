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

# Three independent Lorentz vectors: conditional removal of the connection stabilizer

**Research-only theorem, 2026-10-26.** Extends the merged conditional two-vector results #780 and #781. Does not alter the single-field carrier or declare an extra physical field or selected canonical action.

At a point in real Minkowski 4-space, take three linearly independent carrier vectors v,w,u, where v is nonnull timelike and w,u have linearly independent projections into v's spacelike orthogonal complement. Suppose a metric-compatible Lorentz connection omega_mu must satisfy three prescribed transport equations omega_mu v=a_mu, omega_mu w=b_mu, omega_mu u=c_mu, and suppose these prescriptions are **jointly consistent** with one skew endomorphism for each mu.

If omega and omega' both solve all three equations, their difference C_mu belongs to so(1,3), annihilates v,w,u. Since C_mu is eta-skew, and three independent vectors have a nondegenerate 3-plane containing a timelike direction, C_mu acts only on a one-dimensional orthogonal complement. An antisymmetric endomorphism of a one-dimensional metric vector space vanishes; hence C_mu=0. Therefore the connection is unique if it exists.

For one world index the map so(1,3) -> (Cv,Cw,Cu) has rank 6 and zero kernel. With one timelike v alone it has rank 3 and kernel dimension 3; with two independent v,w it has rank 5 and kernel dimension 1 (four leftover functions over four mu); with three independent v,w,u it is rank 6 and kernel zero.

**Critical physical gate:** Neither a third independent vector component nor its prescribed transport follows from canonical UBT. The single biquaternion Theta contains two Lorentz-real 4-vector parts, not three independent freely available 4-vectors without another derived composite construction. Prescribing a third parallel vector or covariant derivative is an additional strong condition and generally reduces holonomy/allowed curvature. A third vector is not a proposal to introduce a new fundamental field. Also the consistency equations for the prescribed images become more restrictive as vectors are added; full rank does not guarantee existence.

Thus this provides a sharp *conditional kinematic uniqueness threshold*, not a proof that the physical UBT connection is unique or that its reduced Hamiltonian exists. Action selection, eight-real Hessian, psi evolution and Dirac closure remain open.

Exact test: tests/test_three_vector_stabilizer_rank.py.
