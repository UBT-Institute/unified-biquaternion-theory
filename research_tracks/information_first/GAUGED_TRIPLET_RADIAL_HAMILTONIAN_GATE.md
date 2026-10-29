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

# Minimal gauged SU(3) triplet: explicit Dirac-compatible radial Hamiltonian and colour no-go

**2026-10-26. Exact 0+1-dimensional benchmark, NOT the UBT action, a 3+1 Yang–Mills derivation, or the full Dirac algebra.** This deliberately tests what local colour-frame symmetry actually removes.

Take a single complex triplet z(t)∈C³ with r²=z†z>0 and a temporal su(3) connection A0(t), chosen anti-Hermitian. Let D_t z=dot z+A0 z, and S=∫dt [(D_t z)†(D_t z)−m²z†z], m²≥0. Under z→g z, A0→g A0 g⁻¹−dot g g⁻¹ it is invariant. The canonical momenta in a fixed temporal gauge A0=0 are p_z=dot z†, p_z†=dot z; gauge fields have primary momenta π_A≈0 and variation in A0 gives the eight Gauss constraints J_a≈0 (with rank/reducibility subtleties at fixed z; the stabilizer is SU(2), so orbit tangent dimension five). This gauge-covariant toy is **not** derived from biquaternionic Theta or split-jet gravity.

For z≠0, SU(3) acts transitively on the unit sphere S⁵ ⊂ C³: every z is gauge-equivalent to (r,0,0). On the Gauss/reduced branch, angular momenta are gauge and the surviving configuration variable is r only. In a gauge that cancels angular velocities via A0, the reduced Lagrangian is
   L_red=dot r²−m²r²,
   p_r=2 dot r,    **H_red=p_r²/4+m²r²≥0**.
The positive lower bound assumes m²≥0 and r≥0; r=0 is an orbit-singular stratum. The reduced phase space has one canonical pair (r,p_r), dimension 2. This exhibits a healthy but colourless radial toy degree of freedom, and explains why an SU(3) moving frame by itself does not produce eight gluons or six physical orientation excitations. Introducing spatial Yang–Mills curvature in 3+1 or additional gauge-invariant relational data is a separate dynamical task.

**Minimal physical observable algebra:** polynomial functions of r²=z†z and its conjugate radial momentum (or their quantum self-adjoint extensions with care at r=0). Individual z_i and their coherences are gauge dependent. Correlations between observers can use gauge-invariant operators at each accessible region; spatially separated charged operators require Wilson lines or appropriate edge dressing in a genuine Yang–Mills theory. The information identity J(AB)=J(A)+J(B)+I(A:B) applies only for a specified tensor decomposition of physical systems; a Gauss-law constraint can obstruct naive factorization.

**Hamiltonian selection verdict:** a whole family m²≥0 obeys the same gauge/rotation symmetries and yields bounded Hamiltonians. Shared entropic consistency alone does not select m. Time-dependent gauge-invariant correlators of r² can constrain it once a state and clock are supplied. The test gives an explicit action, constraints and reduced Hamiltonian, but not a microscopic UBT derivation or gravity coupling. The next bridge is a precisely specified Theta-to-(z,A0) map compatible with metric lock and MM presymplectic structure; absent that, this is a diagnostic lower-dimensional analogue only.

Regression: tests/test_information_gauged_triplet_radial_hamiltonian.py.
