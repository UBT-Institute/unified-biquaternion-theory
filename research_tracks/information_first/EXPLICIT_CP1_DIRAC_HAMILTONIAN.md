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

# Explicit Dirac Hamiltonian from a CP1 information state: worked endpoint and UBT obstruction

**26 Oct 2026 — complete finite-dimensional conditional derivation, NOT the fundamental Theta Hamiltonian.** Natural units hbar=1; work on local coordinate chart 0<theta<pi.

1. Information state z=(cos(theta/2),exp(i phi)sin(theta/2)) defines Berry 1-form A=-i<z|dz>=(1-cos(theta))/2 dphi and curvature dA=(sin theta/2)dtheta wedge dphi.
2. **Extra physical datum:** choose the calibrated two-level microscopic energy operator h sigma_z, h a fixed real energy constant. The state expectation gives H(theta,phi)=<z|h sigma_z|z>=h cos(theta). The information geometry and shared-reality axioms DO NOT select h or this operator. If reference rho_beta=e^{-beta h sigma_z}/Z is independently identified as Gibbs, K=-log rho_beta=beta h sigma_z+log Z I reconstructs the same operator at independently specified beta.
3. First-order action S=integral [ (1-cos theta)/2 dot phi - h cos theta ] dt. Momenta: p_theta=0, p_phi=(1-cos theta)/2. Primary constraints chi1=p_theta, chi2=p_phi-(1-cos theta)/2. Canonical Hamiltonian Hc=h cos theta. Constraint PB matrix C_12={chi1,chi2}=+sin theta/2, C_21=-sin theta/2. Inverse exists for 0<theta<pi, so both are second class. There are no further independent constraints: preservation fixes multipliers.
4. Reduced Dirac bracket {theta,phi}_D = -2/sin theta. Consequently dot theta=0 and dot phi={phi,H}_D=2/sin(theta)*dH/dtheta=-2h. This agrees with direct Euler–Lagrange equations. On the Bloch sphere, this is constant precession in the chosen phase convention. H is bounded: -|h|<=H<=|h|.
5. Because the Berry 1-form is only local on CP1, transition between charts alters action by a boundary/winding term; curvature is globally well-defined. There are zero local gauge/first-class constraints in this *already projectivized two-real-dimensional state-space model*, although the normalized-vector representation has a phase redundancy removed by projectivization.

**Important falsification:** replacing h by any h' changes dot phi but leaves information metric, Berry curvature, and consistency of all observer marginals intact. The complete conditional derivation is therefore an *existence demonstration* of a Hamiltonian, not the missing UBT selection theorem. CP1 has no local spacetime fields, gravitational constraints, composite spin connection, 4D tetrad, psi modes or graviton.

**UBT proof obligations before calling the project complete:** derive physical state/algebra from Theta (with positivity and correct Lorentz/phase symmetry), independently calibrate modular time/energy operator from Theta geometry, derive unique action rather than adding h, and execute full field-theoretic Dirac algorithm (including diffeomorphism/Lorentz constraints and SO2 residual connection). Registry remains DEFINED_FAMILY_NOT_FINALIZED.

Executable check: tests/test_information_dirac_hamiltonian.py.
