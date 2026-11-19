<!-- BILINGUAL-UNIT: phase-measurement-real-branch-2026-11-19 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional algebraic audit; not a microscopic quantum collapse model or new metric definition.
UBT-AI-PROVENANCE-END
-->
# Phase is not collapse: a conditional real-geometry selection gate

<!-- UNIT: scope -->
## Motivation and status

The UBT research programme has long considered imaginary-time phase, quantum/observer relative phases, and branch selection. This note uses the original full biquaternion Θ and the fixed canonical central-sharp tetrad; it does not modify the field, Axiom B complex-time coordinate, Axiom C metric or fundamental-action registry. The goal is to distinguish an algebraic phase, a physical measurement update and a real-Lorentz geometric branch **without assuming FLRW, an observer-independent global clock, or a final collapse mechanism**. Existing work on phase-texture, G1 strict reality and mimetic clocks supplies independent warning gates.

<!-- UNIT: phase -->
## Exact single-central-phase rank gate

Start with a generic biquaternion first jet in its faithful \(2\times2\) complex representation,
\[
E_\mu=A_\mu+iB_\mu,\qquad
A_\mu=A_\mu^\dagger,\quad B_\mu=B_\mu^\dagger.
\]
The **canonical** real Lorentz tetrad slice corresponds to \(E_\mu^\dagger=-E_\mu\), i.e. \(A_\mu=0\) for every \(\mu\), with the nondegenerate central sharp metric fixed by Axiom C.

**Conditional global or local scalar-phase action.** If a compatible two-sided derivative transforms homogeneously as \(E'_\mu=e^{i\phi}E_\mu\), then
\[
\frac{E'_\mu+E_\mu'{}^\dagger}{2}
=A_\mu\cos\phi-B_\mu\sin\phi.
\]
Therefore a *single* scalar phase can bring all four first jets into the Lorentz-real slice at one spacetime point if and only if a real unit vector \((\cos\phi,\sin\phi)\) annihilates the two columns \((A_\mu)_\mu\) and \(-(B_\mu)_\mu\) jointly. Except for the zero-jet case, equivalently this \(16\times2\) real matrix has rank at most one. Generic complex jets have rank two and cannot be repaired by ANY such central phase. A **single-jet** exact witness already suffices:
\[
E=\begin{pmatrix}1&0\\0&i\end{pmatrix},\quad
A=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
B=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
\]
Anti-Hermitian \(e^{i\phi}E\) would require \(\cos\phi=0=\sin\phi\), impossible. If a local \(\Theta\) phase does not induce homogeneous \(E'_\mu=e^{i\phi}E_\mu\) because a connection transformation is unspecified, this lemma does not apply until that transformation is derived.

The result does NOT exclude noncommutative quaternion phase rotations, selected relative left/right actions, observer-conditional geometry or genuine nonunitary measurement updates; their covariance and dynamics are separate gates. The earlier central phase/metric obstruction also remains: with the complex-linear canonical sharp, \(g[e^{i\phi}E]=e^{2i\phi}g[E]\), so the above phase is not automatically a physical metric gauge transformation.

<!-- UNIT: measurement -->
## Phase rotations, decoherence and selective collapse are different maps

In the previously established **candidate observer protocol**, with positive Hermitian observer clock \(N\), construct
\[
T_N=N^{-1/2}\Theta N^{-1/2},\qquad
\rho_N=\frac{T_NT_N^\dagger}{\operatorname{tr}(T_NT_N^\dagger)}.
\]
This gives a legitimate positive normalized finite-dimensional density matrix *algebraically*, not a derivation of the quantum measurement postulates from UBT. In particular \(\rho_N[e^{i\phi}\Theta]=\rho_N[\Theta]\) for a central phase: a one-observer density readout is blind to it.

For \(\Theta=I_2\), \(N=I_2\), one obtains \(\rho=I_2/2\). An invertible unitary phase or any unitary conjugation preserves its eigenvalues and purity \(\operatorname{tr}\rho^2=1/2\). A **selective** hypothetical outcome with projector \(P=\operatorname{diag}(1,0)\) instead obeys the ordinary Lüders measurement rule
\[
p=\operatorname{tr}(P\rho)=\frac12,\qquad
\rho_P=\frac{P\rho P}{p}=P,\qquad
\operatorname{tr}(\rho_P^2)=1.
\]
So a selective collapse is **not** the same mathematical transformation as a scalar phase rotation. This is a standard QM comparator, not a derived UBT collapse. Nonselective decoherence \(\rho\mapsto\sum_aP_a\rho P_a\) suppresses interference in an appropriate basis but by itself does not choose a unique single observed outcome; an outcome selection/instrument law and probability weights still require justification.

The user hypothesis "the observed real branch is selected by phase coherence/decoherence or collapse" becomes testable only after specifying (i) a Hilbert or operational state space induced by one full \(\Theta\), (ii) observer effects and dynamically selected phase comparisons, (iii) a completely positive or otherwise consistent state update with probabilities, (iv) how each selected outcome yields a nondegenerate, *canonical sharp-derived* real Lorentz tetrad and (v) the induced gravitational constraints. This is explicitly not the old superseded Hermitian/real-part metric readout.

<!-- UNIT: psi -->
## Complex time, quaternionic phases and physical branches

**Three distinct phase notions must be kept separate.**

- \(\psi\) is the **coordinate of imaginary complex time** in locked Axiom B, \(\tau=t+i\psi\); it is not automatically the same as a central state phase.
- A central \(e^{i\phi}\) is a one-parameter complex multiplication; on the canonical real tetrad its weight-two metric action is obstructed if treated as a continuous unchanged-metric gauge.
- Relative biquaternion/quaternion phases are generally noncommuting (unit-quaternion \(Sp(1)\cong SU(2)\)); they are neither the same as the scalar \(\psi\) coordinate nor three independent commuting phase circles.

The pre-existing complex-time calculation \(\Theta(\tau)=e^{i\tau}=e^{it-\psi}\) proves directly that shifting the imaginary-time coordinate \(\psi\) changes the **magnitude** in that holomorphic example, not its ordinary oscillatory phase. Therefore identifying \(\psi\) with a phase angle requires a separate dynamical or spectral prescription.

For multiple alternatives \(\Theta_1,\Theta_2\), the fact that some invariants coincide implies neither physical gauge equivalence nor a coherent quantum superposition: one needs a state space, an operator algebra, linearity/inner product and an on-shell dynamics. Distinct branches could share laws and invariants while still being physically distinct; ordinary quantum probabilities cannot be read off from algebraic invariant equality alone.

<!-- UNIT: next -->
## Required dynamical bridge and provenance

Next derivation task: formulate a covariant conditional phase-selection instrument on the EXISTING Θ phase space, prove preservation of the admitted real Lorentz central metric after outcome selection, and compute consistency of its Hamiltonian constraints and probability conservation. Any independent classical tetrad, modified trace/real-part metric or inserted state vector is inadmissible as a canonical replacement. This is a proposal, not a measured prediction. Prior research: docs/phase/ubt_phase_projection.tex (EXPLORATORY/NONCANONICAL old metric readout); research_tracks/complex_time_branch_selection/psi_branch_selection.en.md (holomorphy alone no-go); research_tracks/action_selection/physics_closure_phase_texture_2026_10.en.md (phase cancellation); research_tracks/conformal_causal_shared_reality/G1_PHASE_STRICT_REALITY.en.md (rank obstruction); research_tracks/information_first/THETA_OBSERVER_RELATIVE_INFORMATION_CHANNEL_2026_11.en.md (candidate positive observer readout); research_tracks/information_first/THETA_OBSERVER_PHASE_LINKS_MULTI_CLOCK_CURVATURE_GATE_2026_11_13.en.md (relative phases and multi-clock information). Finite exact SymPy verifier: tools/verify_gr_phase_collapse_selection_gate_2026_11_19.py. It does not derive quantum dynamics or show a physical measurement event.
