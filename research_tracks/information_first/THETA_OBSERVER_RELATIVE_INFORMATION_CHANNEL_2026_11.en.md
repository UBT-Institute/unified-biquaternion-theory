<!-- BILINGUAL-UNIT: theta-observer-channel.scope -->
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

# Full-complex-Theta observer-relative information channel and exact identifiability gate

**2026-11-05 · C_working · PROVED algebraically under stated observer-protocol assumptions; physical derivation OPEN.** English is the translation source. This closes a *finite local readout construction* proposed in the previous information-first notes. It is NOT a derivation of quantum states from fundamental UBT dynamics, an observer algebra on causal diamonds, a microscopic action, or a Hamiltonian. Do not replace the locked central-sharp tetrad.

<!-- BILINGUAL-UNIT: theta-observer-channel.primitive -->
## Observer clock, full Theta, and positive local readout [PROVED]

Use the original FULL complex matrix Theta in its Lorentz-congruence representation. The observer's future unit-timelike clock direction n is transported through the **existing** UBT composite tetrad, not added as a propagating field. In the Pauli-map convention it defines positive Hermitian N with unit determinant. For nonzero Theta construct the following *candidate* normalized local two-level readout and a protocol-specified positive measurement effect E:
\[
\Theta\in\mathbb C\otimes\mathbb H\simeq\operatorname{Mat}_2(\mathbb C),\quad
N=n^0I_2+n^j\sigma_j=N^\dagger>0,\quad
\det N=1,\quad g_{\mu\nu}n^\mu n^\nu=-1,
\]
\[
T_N=N^{-1/2}\Theta N^{-1/2},\qquad
Q_N=T_NT_N^\dagger,\qquad
\boxed{\rho_N[\Theta]=\frac{Q_N}{\operatorname{tr}Q_N}},\quad
p_N(E\mid\Theta)=\operatorname{tr}(\rho_N E),\quad 0\le E\le I_2.
\]

The observer clock N is indispensable protocol data. Its dependence on the composite tetrad must be included by the chain rule if any future action uses the readout. This formula neither invents a second Theta nor establishes that physical detectors in UBT implement this POVM.

Since Q is a nonzero positive semidefinite matrix, the readout is a legitimate finite-dimensional density matrix algebraically; a rank-deficient nonzero Theta gives a pure state without a divergence:
\[
\operatorname{tr}\rho_N=1,\quad \rho_N\ge0,\qquad
\det\rho_N=\frac{|\det\Theta|^2}{(\det N)^2(\operatorname{tr}Q_N)^2}.
\]

<!-- BILINGUAL-UNIT: theta-observer-channel.covariance -->
## Lorentz-covariant comparison of observer records [PROVED]

Under the *same* proper Lorentz transformation applied to Theta and the observer clock N, the induced matrix U is unitary; therefore corresponding measurement probabilities agree:
\[
\Theta'=S\Theta S^\dagger,\quad N'=SNS^\dagger,\quad
U(S,N)=N'^{-1/2}SN^{1/2},\quad S\in SL(2,\mathbb C),
\]
\[
UU^\dagger=I_2,\quad T_{N'}'=UT_NU^\dagger,\quad
\rho_{N'}[\Theta']=U\rho_N[\Theta]U^\dagger,\quad
E'=UEU^\dagger,\quad p_{N'}(E'\mid\Theta')=p_N(E\mid\Theta).
\]

This is an exact local implementation of **weak operational shared reality** (equivariant records). A fixed N under a boost gives false apparent disagreement. It is NOT the stronger shared-state extension theorem for overlapping quantum algebras, nor a causal field-theory net.

<!-- BILINGUAL-UNIT: theta-observer-channel.rank -->
## Generic information rank and exact invisible directions [PROVED]

At invertible T, the differential of the normalized positive matrix is zero precisely when the infinitesimal variation is a real rescaling plus a right anti-Hermitian rotation. Hence the local channel maps the real components of full Theta onto the interior of the Bloch ball with the following rank and kernel:
\[
\delta\rho_N=0\iff\delta Q_N=\lambda Q_N
\iff \delta T_N=T_N(cI_2+A),\quad
c\in\mathbb R,\quad A^\dagger=-A
\qquad(\det\Theta\ne0),
\]
\[
\dim_{\mathbb R}\ker(d\rho_N)=1+4=5,\qquad
\operatorname{rank}_{\mathbb R}(d\rho_N)=8-5=3.
\]

This kernel belongs to the *chosen observer readout*, not automatically to a gauge symmetry of the locked UBT action. Independent physical observables might distinguish these directions; discarding them from the UBT field would be unjustified.

<!-- BILINGUAL-UNIT: theta-observer-channel.winding -->
## Phase and determinant-winding blindness [PROVED for the readout]

Right multiplication by an observer-metric-adjusted unitary preserves this density matrix, but may rotate the complex determinant by an arbitrary winding:
\[
V^\dagger V=I_2,\qquad
\Theta_V=\Theta N^{-1/2}VN^{1/2},\qquad
\rho_N[\Theta_V]=\rho_N[\Theta],\quad
\det\Theta_V=\det\Theta\det V,
\]
\[
N=I_2,\quad
V_m(\psi)=\operatorname{diag}(e^{im\psi/R_\psi},1),\quad m\in\mathbb Z,\qquad
\nu(\det\Theta_V)=\nu(\det\Theta)+m.
\]

The displayed winding family is a witness about this LOCAL readout's information loss on unconstrained nonzero full matrices. It does **not** prove that the transformed full-Theta fields preserve the original Lorentz-real canonical tetrad, satisfy the microscopic field equations, or belong to one physical gauge orbit. A phase-sensitive independent reference channel would be additional operational input; compare the separate Fisher gates in PR #828.

<!-- BILINGUAL-UNIT: theta-observer-channel.reference -->
## Different clocks yield different information [PROVED]

Even for fixed Theta, changing the admissible observer clock changes the density spectrum. This is a change of the protocol, not a contradiction with simultaneous Lorentz covariance:
\[
\Theta=\operatorname{diag}(2,1),\quad N_1=I_2,\quad
N_2=\operatorname{diag}(\sqrt2,1/\sqrt2),\qquad
\rho_{N_1}=\operatorname{diag}(4/5,1/5),\quad
\rho_{N_2}=I_2/2.
\]

There is no unique observer-independent normalization selected by this construction. The hypothetical physical observer must supply its time direction, admissible effects, and preparation protocol from already derived UBT geometry and matter couplings.

<!-- BILINGUAL-UNIT: theta-observer-channel.multiclock -->
## Ideal three-clock shared-reality tomography [PROVED for this local channel]

The single-clock rank deficit is **not** an absolute information-loss theorem if calibrated observers can compare complete density matrices. On the same matrix fiber use the following positive unit-determinant clock directions with noncommuting relative boosts:
\[
N_0=I_2,\qquad N_1=\operatorname{diag}(2,1/2),\qquad
N_2=\begin{pmatrix}2&1\\1&1\end{pmatrix},\quad
N_j=N_j^\dagger>0,\ \det N_j=1,
\]
\[
\left(\forall j\in\{0,1,2\},\
\rho_{N_j}[\Theta]=\rho_{N_j}[\Phi]\right)
\ \wedge\ \det\Theta\det\Phi\ne0
\quad\Longrightarrow\quad
\boxed{\Theta=c\Phi,\quad c\in\mathbb C^\times},
\]
\[
\dim_{\mathbb R}\ker d(\rho_{N_0},\rho_{N_1},\rho_{N_2})=2,\qquad
\operatorname{rank}_{\mathbb R}d(\rho_{N_0},\rho_{N_1},\rho_{N_2})=6.
\]
\[
\rho_{N_0}[I_2]=\rho_{N_0}[\sigma_z],\quad
\rho_{N_1}[I_2]=\rho_{N_1}[\sigma_z],\quad
\rho_{N_2}[I_2]\ne\rho_{N_2}[\sigma_z].
\]

**Proof.** Equality at N_0 gives `A=Phi^{-1}Theta=sqrt(k) V`, where k is positive and V unitary. At the other clocks, equality of normalized readouts and their determinants forces `V N_j^{-1} V†=N_j^{-1}`, so V commutes with both. The commutant of diagonal N_1 is diagonal, while commuting with the off-diagonal N_2 forces its diagonal entries to coincide. Thus V is a global phase and Theta differs from Phi only by one nonzero complex scalar. The intersection of infinitesimal kernels gives the displayed real rank and kernel. The last line is an exact witness that the first two clocks cannot resolve the relative right-unitary phase.

This is a **conditional local identifiability theorem**, not a claim that physical UBT detectors implement complete tomography in causally overlapping regions. Protocols must calibrate all clocks on the same geometric fiber, and operational effects and comparison maps remain to be derived. The residual complex scalar is blindness of this readout, NOT automatically a microscopic gauge orbit. A rescaled full field need not preserve the locked tetrad.

<!-- BILINGUAL-UNIT: theta-observer-channel.no-selection -->
## Static information does not yet select the Hamiltonian [PROVED benchmark]

For fixed N, the following **finite-dimensional test histories** arise from full complex matrices and are distinguishable by an x-basis measurement. Both retain positivity and normalized quantum entropy, yet the frequency is arbitrary:
\[
\rho_0=\tfrac12(I_2+r\sigma_x),\quad 0<r<1,\quad
T_0=\sqrt{\rho_0},\quad
\Theta_\omega(t)=e^{-i\omega t\sigma_z}T_0,\quad N=I_2,
\]
\[
\rho_\omega(t)=e^{-i\omega t\sigma_z}\rho_0e^{i\omega t\sigma_z},\quad
p_+(t)=\tfrac12(1+r\cos(2\omega t)),\quad
F_\omega=\frac{4r^2t^2\sin^2(2\omega t)}{1-r^2\cos^2(2\omega t)}.
\]

The Fisher information is a positive parameter-estimation diagnostic (for nonvanishing outcome probabilities), not an equation determining omega. This reuses the earlier shared-reality Hamiltonian nonselection argument, now applied to the explicit Theta-native *readout*. It is NOT an on-shell UBT solution and does not implement local causal propagation.

<!-- BILINGUAL-UNIT: theta-observer-channel.next -->
## Next information-first physical gate [OPEN]

Promote this optional local construction only after deriving a PHYSICAL observer-relative positive state, an instrument/POVM, a causal-domain algebra, calibrated proper-time evolution and overlap/extension rules directly from the same single-Theta action. Test relative entropy under physically derived restrictions and its response to the composite geometry, then show whether modular-energy response eliminates the Hamiltonian deformation freedom. An admissible information selector must give new variational constraints, not merely label a positive Fisher metric.

For any hypothetical microscopic use of rho_N, vary BOTH Theta and the tetrad-dependent N; verify Lorentz/clock covariance, ghost-free reduced symplectic structure and GR/QED limit. Do not treat data processing, or the entanglement first law alone, as a unique action-selection theorem.

<!-- BILINGUAL-UNIT: theta-observer-channel.verification -->
## Verification and provenance

Exact symbolic regression: `tests/test_theta_observer_information_channel.py` (fifteen SymPy unit tests), including nontrivial Lorentz transport, observer choice, rank-three differential, five null directions, winding blindness and arbitrary-frequency benchmark. A test proves only the displayed finite matrix identities, not a physical measurement theory. No Lean formalization, independent semantic translation approval, on-shell state, selected Hamiltonian, or experimental prediction is claimed. Source premises: `canonical/CANONICAL_DEFINITIONS.md`, `research_tracks/information_first/SHARED_REALITY_PRINCIPLE.md`, `research_tracks/information_first/CAUSAL_ACCESS_SHARED_REALITY_HAMILTONIAN_GATE.md`, `research_tracks/information_first/MODULAR_HAMILTONIAN_RECONSTRUCTION_GATE.md`, and `research_tracks/action_selection/mm_phase_qfi_reference_gate_2026_11.en.md` (draft PR #828).