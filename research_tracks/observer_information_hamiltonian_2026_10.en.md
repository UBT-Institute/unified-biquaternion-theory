<!-- BILINGUAL-UNIT: observer-info-hamiltonian -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Observer information, causality and Hamiltonian: working derivations

<!-- BILINGUAL-UNIT: scope -->
## Scope and relation to canonical UBT

This research note records the observer-information, shared-reality and Hamiltonian discussion of 27 October 2026. It is **noncanonical**. The locked UBT architecture retains one fundamental field $\Theta(q,\tau)\in\mathbb C\otimes\mathbb H$, complex time $\tau=t+i\psi$, the tetrad $E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta$, and the central anticommutator metric. The auxiliary qubits, detector Hilbert spaces, real component fields and background Minkowski metric below are **effective test models**, not replacements or extra fundamental UBT fields.

**Status:** working derivations and explicit counterexamples; no unique fundamental UBT Hamiltonian or action derived.

<!-- BILINGUAL-UNIT: capacity -->
## Observer capacity and shared reality

For a physically allowed protocol $\pi\in\Pi_O$ define $\mathcal I_O(X)=\sup_\pi I(X;Y_\pi)$. The set $\Pi_O$ is constrained by state preparations, allowed measurements, memory, energy, time and causal access. If $\Pi_1\subseteq\Pi_2$, then $\mathcal I_1\le\mathcal I_2$; complexity alone, without measurement access, need not improve information. Operational equivalence of states is $\rho\sim_O\sigma$ iff $\mathrm{Tr}[(\rho-\sigma)A]=0$ for every accessible observable $A$. For two observers distinguish **individually shared** observables (intersection) from **collectively reconstructible** information (joint accessible measurements and communication). A shared-reality consistency requirement is proposed, **not derived** as a dynamics-selecting axiom.

<!-- BILINGUAL-UNIT: fisher -->
## Fisher geometry: an explicit example

For $\rho=(I+\mathbf r\cdot\boldsymbol\sigma)/2$, a $\sigma_z$ measurement with $z=r_z$ gives $p_\pm=(1\pm z)/2$ and $F(z)=1/(1-z^2)$. With symmetric sensitivity $\eta\in[0,1]$, $q_\pm=(1\pm\eta z)/2$ and $F_\eta(z)=\eta^2/(1-\eta^2z^2)$. This is an operational statistical metric, **not** the physical spacetime metric. Setting $z=\cos\vartheta$ gives $ds_F^2=d\vartheta^2$ in the ideal case. The functional $S_{\rm info}=\frac\kappa2\int\dot\vartheta^2dt$ is a **chosen** kinetic/geodesic action, not a consequence of Fisher geometry alone.

<!-- BILINGUAL-UNIT: identifiability -->
## Dynamic Hamiltonian identifiability

For $H=h_0I+\mathbf h\cdot\boldsymbol\sigma$ and $i\hbar\dot\rho=[H,\rho]$, $\dot{\mathbf r}=(2/\hbar)\mathbf h\times\mathbf r$. Define $H_1\sim_{\mathcal O}H_2$ when all allowed preparations, measurement expectations and observation times coincide. When **every** initial density matrix is preparable and measurements are ideal, equality at all times implies $[H_1-H_2,A]=0$ for each accessible $A$ (necessary, not sufficient in general). A scalar commutant $\mathcal O'=\mathbb CI$ is sufficient for identifying $H$ up to $\lambda I$. For sole observable $\sigma_z$, time derivatives identify transverse $h_x,h_y$, and generically $h_z$ when $(h_x,h_y)\ne(0,0)$; if both vanish, $h_z$ is invisible. With access to $\sigma_x$ and $\sigma_z$, their common commutant is scalar. **No observer principle yet selects the numerical couplings.**

<!-- BILINGUAL-UNIT: slits -->
## Double-slit detector: derived conditional results

Assume a nondemolition path readout and a two-level detector. The general path-preserving interaction is $H_{\rm int}=|L\rangle\langle L|\otimes V_L+|R\rangle\langle R|\otimes V_R=I\otimes V_++\sigma_z\otimes V_-$. **Choosing** $V_-=(\hbar g/2)\sigma_y$ (not uniquely deriving it) gives $H_{\rm int}=(\hbar g/2)\sigma_z^{(S)}\otimes\sigma_y^{(O)}$. For initial $(|L\rangle+|R\rangle)|0\rangle/\sqrt2$, the conditioned detector-state overlap is $\cos(gT)$, the particle visibility is $\mathcal V=|\cos(gT)|$, and optimal equal-prior path distinguishability is $\mathcal D=|\sin(gT)|$, hence $\mathcal V^2+\mathcal D^2=1$ in this ideal pure model. Detector-state distinguishability, not conscious reading, suppresses unconditioned interference. Greater post-processing capacity at fixed interaction does not change that visibility.

<!-- BILINGUAL-UNIT: causality -->
## Symmetry, geometry, and finite light speed

The Hermitian biquaternion representation $X=ct+i\sum_kx^k\mathbf e_k$ satisfies $X\bar X=c^2t^2-|\mathbf x|^2$ under quaternionic conjugation, giving a representation of flat Lorentz geometry but **not deriving** spacetime geometry or $c$ from UBT. A local relativistic scalar-multiplet effective model with eight real fields $q_A$ may be **chosen** as $\mathcal L=K\dot q_A\dot q_A/(2c^2)-K(\nabla q_A)^2/2-V(q)$, with $V=M^2q_Aq_A/2+\lambda(q_Aq_A)^2/4$. Then $\pi_A=K\dot q_A/c^2$ and $\mathcal H=c^2\pi_A\pi_A/(2K)+K(\nabla q_A)^2/2+V$. The equation is $c^{-2}\ddot q_A-\nabla^2q_A+K^{-1}\partial_AV=0$. This is a conditional **effective scalar multiplet** in fixed Minkowski space, not the canonical UBT action. Lorentz invariance constrains principal propagation; a full quantum causal proof requires locality and microcausality. A detector coupled locally along a worldline, e.g. $g_O\chi(\tau)m_O(\tau)\Phi(z_O(\tau))$, is preferable to instantaneous remote couplings. The detector coupling and $c$ remain external inputs here.

<!-- BILINGUAL-UNIT: algebra -->
## Biquaternion-specific interaction and unresolved selection

Using $\mathbf e_k\leftrightarrow-i\sigma_k$, the chosen two-qubit interaction can be represented as $\mathbb H_{\rm int}=-(\hbar g/2)\mathbf e_3^{(S)}\otimes\mathbf e_2^{(O)}$ in $\mathbb B\otimes_{\mathbb C}\mathbb B$. The isomorphism $\mathbb B\cong M_2(\mathbb C)$ **alone yields no distinct prediction**. For pure quaternion vectors $[\mathbf a,\mathbf b]=2\mathbf a\times\mathbf b$ and $\{\mathbf a,\mathbf b\}=-2\mathbf a\cdot\mathbf b$; a commutator-square term favors commuting (parallel) configurations rather than orthogonality, whereas an anticommutator-square term can favor orthogonality. Such additional couplings are exploratory, may break postulated internal $U(4)$ symmetry, and must not introduce another fundamental field without explicit architectural review. Their coefficients are undetermined.

<!-- BILINGUAL-UNIT: gaps -->
## Gaps, falsification and verification plan

1. **Canonical bridge:** derive an observer-accessible local observable and detector coupling from the locked $\Theta$, two-sided $D_\mu$, tetrad and anticommutator metric; do not replace them.
2. **Symmetry audit:** enumerate permitted terms using actual UBT transformation laws, not assumed $U(4)$.
3. **Causality:** derive characteristic cones from the canonical emergent metric and verify microcausality/no-signalling with smeared detector couplings.
4. **Information selection:** provide a noncircular extremal principle that excludes competing Hamiltonians or constrains a coupling; counterexample $H=0$ versus $H=\omega\sigma_z$ for path-only observations remains.
5. **Tests:** verify qubit commutators and visibility numerically/CAS; test action variation, positivity and parameter identifiability; compare with double-slit/quantum-eraser benchmarks.
6. **Proof/translation gates:** **LEAN-PENDING** (no Lean compilation), **CAS-PENDING**, **BILINGUAL-SEMANTICS-PENDING**. Do not merge or elevate claims before required checks; bilingual content identity and independent semantic review remain mandatory.
