<!-- BILINGUAL-UNIT: bottom-up-theta-quadratic-action-selection -->
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

# Bottom-up quadratic Theta action and Hamiltonian: symmetry classification without importing a higher-dimensional action

**2026-10-26; restricted flat-background construction, NOT the fundamental S_UBT.** This is an independent inverse route; compare only afterward with canonical/ACTION.en.md and canonical/bridges/theta_quantum_structure.tex. Assumptions explicitly added here: complex coefficient field Phi=(s,z) in 1⊕3 of **global** SU(3), global U(1) common phase, ordinary 3+1 Lorentz covariance, flat torus T^d with constant positive metric G_ab, translation invariance, locality, Hermiticity, at most two derivatives, parity-even terms, and a standard second-order-in-time regular Lagrangian. SU(3) on this carrier need not be an independently realized local physical colour gauge group of UBT.

Under these assumptions the block-diagonal, constant-coefficient free action (modulo boundary terms and coordinate rescalings) is
 L= sum_{q=s,t} [ Z_q (|dot Phi_q|² - |grad_x Phi_q|²) - C_q^{ab} (partial_a Phi_q)†(partial_b Phi_q) - mu_q² Phi_q†Phi_q ],
with Z_q>0, real symmetric C_q>=0 (torus-translation invariance alone does NOT force C_q proportional to G^{-1}), mu_q²>=0 for a sufficient quadratic positivity condition. Here Phi_s=s and Phi_t=z in C³. Discrete involutions of the existing real-energy block do not generally equate Z_s and Z_t or fix mu_q or C_q. General geometric torus isometries beyond translations MAY restrict C further; requiring the principal symbol to be the metric Laplacian would impose C_q^{ab}=c_q G^{ab}, **an extra isotropy/metric-minimality condition** (automatic only under a sufficiently large relevant isometry group).

Canonical momenta pi_q=Z_q dot Phi_q†, and a formal positive fixed-background Hamiltonian is
 H_density= sum_q [ pi_q† pi_q/Z_q + Z_q |grad_x Phi_q|² + C_q^{ab}(partial_a Phi_q)†(partial_b Phi_q)+mu_q² Phi_q†Phi_q ].
Fourier frequencies obey omega_q²=|k|²+(mu_q²+n_a C_q^{ab}n_b)/Z_q, which is the relativistic wave-field dispersion; crucially this is NOT the earlier **first-quantized particle** operator H_tor=alpha(-Delta_G). The latter may arise only in a controlled nonrelativistic/one-particle limit after choosing a rest energy and reduction. Treating omega² eigenvalues as quantum energies would be erroneous.

Concrete nonuniqueness: choose fixed Z=1, mu²=1, C=G^{-1} versus C=2G^{-1}; both positive, local, SU(3), U(1), Lorentz covariant on the specified background and yet give different Kaluza–Klein spectra. The symmetry constraints alone cannot select the compact kinetic scale. More fundamentally C=0 respects the listed continuous symmetries but has no torus dispersion at all. Thus the desired torus derivative term cannot be proven from these symmetries alone.

Local SU(3) further changes the problem: replace ordinary derivatives by a covariant derivative with a connection transforming appropriately. Local symmetry does NOT by itself fix a gauge-field Yang–Mills F² term, its coupling, or its Dirac reduction. The moving-frame SU(3) of existing UBT is not yet such a full physical Yang–Mills sector. On the composite gravity branch the metric-lock and split-jet analysis invalidates a naive promotion of this healthy *fixed-background* Hamiltonian to H_UBT.

**Constructive next target:** Seek an independently justified geometric identity among the existing Theta kinetic invariants that fixes Z, C, mu and survives the exact split-jet quotient. If none exists, correlation-based information constraints must predict *additional numerical conditions* on cross-observer dynamical correlators, not merely state compatible marginals. This is the exact point where Route B would add content.

Test: tests/test_bottom_up_theta_quadratic_hamiltonian.py.
