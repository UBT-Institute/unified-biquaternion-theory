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

# Composite-volume velocity Hessian: an exact conditional no-constraint gate

**26 Oct 2026. Exact restricted first-jet comparison; NOT a complete composite UBT Dirac analysis.**

Let X^A(t,x), A=0,...,7, be eight real components, and at one spacetime point fix the lapse, spatial background data, and nondynamical connection. Let the quadratic time-kinetic Lagrangian be (1/2) dot X^A G_AB dot X^B for a constant nondegenerate real symmetric pairing G of signature (2,6), as in the known generic invariant kinetic sector (up to positive overall normalization). To test adding a geometrically natural composite-volume piece, take a four-vector carrier v^a=X^a for a=0,...,3 and a tetrad E_mu^a built from its first covariant derivative. Assume all spatial rows E_i^a are independent of dot X, and the time row is affine in velocities E_0^a=M^a_A dot X^A+c^a for velocity-independent M and c. Then the determinant is affine in its time row:

det E = sum_a C_a(E_1,E_2,E_3) (M^a_A dot X^A+c^a).

Thus d²(det E)/d dot X^A d dot X^B=0 identically. For the restricted trial

L = 1/2 dot X^A G_AB dot X^B + lambda det E - V(X,spatial jets),

the complete velocity Hessian remains G_AB, has rank eight and signature (2,6). No primary constraints can be induced by this added volume term. Canonical momenta P_A=G_AB dot X^B + lambda C_a M^a_A merely shift by functions of fields/spatial derivatives; the momentum quadratic form in the Legendre Hamiltonian still has six negative directions, so at fixed fields the unrestricted Hamiltonian is unbounded below. An additional action-generated constraint is necessary to remove negative modes. This is an exact **no-rescue** result for this restricted ansatz, not for all UBT models.

Caveats: in a truly composite metric g[Theta], the lapse, inverse metric and determinant can depend on velocities, and a reconstructed omega[Theta] may involve higher derivatives or constraints. Hence holding them fixed could omit terms central to the full theory. Some admissible nondegenerate tetrads cannot be chosen with zero connection, and the location/meaning of ghost modes can change after genuine gauge reduction. No claim of full no-go is made.

This gate narrows P0 to a genuinely derived connection or higher-jet dependence or action-generated constraints rather than adding volume terms to a nondegenerate indefinite quadratic kinetic family.

Check: tests/test_information_volume_hessian_gate.py.
