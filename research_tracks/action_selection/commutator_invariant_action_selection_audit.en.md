<!-- BILINGUAL-UNIT: commutator_invariant_action_selection_audit -->
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


# Commutator-built invariant candidates do not select a unique Theta action

**2026-10-25 — structural selection audit, C-tier. Not a fundamental UBT action or a uniqueness theorem across all possible axioms.**

## Canonical algebra

With the canonical sign convention D_mu X = partial_mu X + A_mu X - X B_mu,
[D_mu,D_nu] X = F^A_mu nu X - X F^B_mu nu =: C_mu nu[X].
This commutator is covariant under properly transformed left/right connections. Its existence is a kinematic identity and does not impose an equation of motion.

If a real nondegenerate invariant bilinear pairing B on the relevant carrier is specified and the locked composite metric g(X) is nondegenerate, a *candidate* local functional is
I_C = int sqrt(-g) g^{mu rho} g^{nu sigma} B(C_mu nu,C_rho sigma) d4x.
Every part of this prescription beyond C itself — pairing, real slice, composite connection, measure and coefficient — must be justified. In particular the existing kinetic pairing has indefinite signature, so a positive Hamiltonian does not follow.

In branches where a metric-compatible connection and its scalar curvature R(Gamma) exist, another candidate is I_R=int sqrt(-g) R(Gamma) d4x, with required boundary terms and specified torsion dependence. Curvature-squared I_R2 and torsion-squared scalars are further alternatives unless eliminated by an independent derivative-order, symmetry or spectral principle. They are candidate tests, not simultaneously declared UBT actions.

An arbitrary linear combination a I_R + b I_C is not uniquely selected by the commutator identity: the identity fixes neither a nor b, nor even the choice of these sectors. Dimensional analysis requires dimensionful scales; it does not fix their values. For independent composite connections, curvature terms may contain derivatives of connection variables; for algebraically reconstructed connections they can introduce higher derivatives of Theta. Actual derivative order and degeneracy depend on the reconstruction, and cannot be claimed without explicit substitution.

## Important countercheck

The previous canonical Proposition 9 rules out the specified minimal timelike auxiliary-connection kinetic/potential subfamily with a nonconstant quartic and nondegenerate tetrad. It does NOT derive I_R or I_C as its replacement. Appending one to bypass the no-go would be a new theory choice unless derived from additional premises.

The kinematic relation between full curvature and contortion, F(omega0+C)-F(omega0)=D_omega0 C+C wedge C, establishes that the 12-dimensional tetrad-invisible stabilizer can affect curvature, and therefore an I_R/I_C candidate may distinguish it. It does NOT guarantee a nonsingular auxiliary Hessian, physical positive energy, or closed constraints.

## Selection gate

To claim a *fundamental* Hamiltonian one must supply:
(1) a single well-defined Theta-only action or independently derived presymplectic/Hamiltonian pair;
(2) canonical composite A[Theta], B[Theta], including transverse contortion;
(3) explicit principal symbol and constrained Hamiltonian Hessian;
(4) closed first-class diffeomorphism/Lorentz algebra, boundary conditions and psi evolution;
(5) stable physically reduced spectrum and correct GR + matter limits.
Nothing in the commutator identity by itself provides these.

**Verdict:** a curvature-based non-volume operator exists as a conditional invariant *candidate*, but no axiom-free coefficient or unique action is selected. Do not promote to canonical action.

References: canonical/ACTION.en.md (status DEFINED_FAMILY_NOT_FINALIZED); canonical/CANONICAL_DEFINITIONS.md (locked sharp metric/two-sided derivative); research_tracks/action_selection/{canonical_family_hamiltonian_bridge,hamiltonian_first_foundations,contortion_stabilizer_invisibility,proposition9_volume_overlap_audit}.en.md.
