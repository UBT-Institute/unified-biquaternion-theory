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

# SO(2) residual connection: curvature versus gauge, and dynamical underdetermination

**26 October 2026 — restricted sector, local example. Not a microscopic UBT action.**

Let the two timelike/spacelike carriers fix a transverse oriented Euclidean two-plane. In a local frame adapted to these carriers, two metric-compatible connections compatible with their assigned transports differ by alpha J, where J is the fixed infinitesimal SO(2) generator acting only on that plane. Their transverse frame-gauge connection one-form A transforms under a frame rotation chi as A -> A + d chi (sign depends on frame convention), and its curvature F=dA is unchanged. Thus a gauge choice can locally set A=0 on a simply connected patch **only if F=0**. If F!=0 there is no such gauge removal.

In an adapted patch with reference connection omega0=0 and constant J, choose alpha=x dy. The residual curvature is F=dalpha=dx wedge dy, nonzero; choosing alpha=0 yields F=0. Both retain the same prescribed images on the two fixed carrier vectors because J annihilates them. This explicit connection-space witness is algebraic and local: the constant-carrier patch itself need not realize a nondegenerate first-jet UBT tetrad. It disproves a blanket inference that the stabilizer freedom is *always* pure gauge, not a universal physical degree-of-freedom statement.

Where omega0 or J vary, the full Lorentz curvature difference is D_omega0(alpha J); do **not** identify its full expression with d alpha J. The transverse SO(2) curvature is the curvature of the induced oriented normal-plane connection, including reference/frame effects.

A dynamical selector requires more input: e.g. an independent curvature-squared trial functional \int F wedge *F gives a Maxwell-type equation d*F=0, but this equation alone does not force F=0 and does not determine all initial/boundary data. A condition F=0 would still permit local gauge ambiguity, while holonomy may survive globally. Neither trial principle follows from the locked single-Theta definitions. We therefore have an exact separation:
(i) two-carrier kinematics fixes connection up to SO(2),
(ii) a third independently transported vector fixes the pointwise connection if compatible,
(iii) curvature tests show SO(2) freedom is not universally gauge,
(iv) a selected action plus admissible boundary/constraint reduction is necessary to claim physical uniqueness and Hamiltonian stability.

Tests: tests/test_residual_so2_curvature_witness.py.
