<!-- BILINGUAL-UNIT: gr-phase-reality-selection-retraction-2026-11-19 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Local off-shell counterexamples and conditional topology theorem; not a quantum-collapse dynamics derivation.
UBT-AI-PROVENANCE-END
-->
# Výběr reálné větve z úplného Theta: hodnost, topologie a informace pozorovatele

<!-- UNIT: scope -->
## Stav tvrzení a kanonická omezení

Keep original Axiom A and C: \(\Theta\) is one full biquaternion, and for a physically admitted classical branch \(E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta\in W_L=i\,\mathrm{Herm}_2\), with the central-sharp metric \(g_{\mu\nu}I_2=\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)\). The **generic complex jet** is not itself certified as physical. This note studies candidate maps from the wider nondegenerate complex-jet domain to the classical real slice without modifying the locked metric, assuming no FLRW ansatz and no universal time.

<!-- UNIT: projection -->
## Protipříklad: reálná Minkowského metrika, ale ztracené nohy tetrády

Represent every full-complex jet by complex coframe coefficients
\[
E_\mu=i\sum_{a=0}^3Z_\mu{}^a\sigma_a,\quad
Z\in GL(4,\mathbb C),\quad
\sigma_0=I_2,\quad
\eta=\operatorname{diag}(-1,1,1,1),\quad
g=Z\eta Z^{\mathsf T}.
\]
On \(Z\in GL(4,\mathbb R)\) all \(E_\mu\) are anti-Hermitian and yield an admissible real tetrad. Choose
\[
Z_\star=
\begin{pmatrix}
0&i&0&0\\
i&0&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix},
\quad
\boxed{Z_\star^{\mathsf T}\eta Z_\star=\eta,\quad \det Z_\star=1.}\tag{A}
\]
This complex but invertible field first jet gives the **real Minkowski** central metric \(g=\eta\). Explicitly
\[
E_0=-\sigma_1,\quad E_1=-I_2,\quad E_2=i\sigma_2,\quad E_3=i\sigma_3.
\]
The tempting "collapse to a real tetrad" by anti-Hermitian projection
\[
\mathcal P(E_\mu)=\frac{E_\mu-E_\mu^\dagger}{2}
\]
kills the first two legs:
\[
\mathcal P(E_0)=0,\quad\mathcal P(E_1)=0,\quad
g[\mathcal P(E)]=\operatorname{diag}(0,0,1,1),\qquad
\boxed{\det g[E]=-1,\quad \det g[\mathcal P(E)]=0.}\tag{B}
\]
Thus a pointwise linear reality projection can destroy the tetrad rank even when the initial full-complex jet yields a nonsingular **real** central metric. This does not refute every non-linear, non-local, dynamical, or outcome-conditioned reality selector; it disproves a universal use of this specific elementary projection. A selective quantum operation cannot be identified with this projection without a derived state-space and action.

<!-- UNIT: topology -->
## Neexistuje univerzální spojitá retrakce na obě reálné orientace

**Conditional topological no-retraction theorem.** Let \(\mathcal D=GL(4,\mathbb C)\), the space of all **nondegenerate complex coframe coefficient matrices**, and \(\mathcal R=GL(4,\mathbb R)\), the full real nondegenerate coframe locus with **both determinant orientations**. There is no globally continuous map
\[
r:\mathcal D\longrightarrow\mathcal R,\qquad r|_{\mathcal R}=\operatorname{id}_{\mathcal R}.\tag{C}
\]
Proof: the complex domain \(\mathcal D\) is path connected, whereas \(\mathcal R\) has two connected components distinguished by \(\operatorname{sign}\det Z\). An explicit complex nonsingular path joins opposite-orientation real coframes:
\[
Z(s)=\operatorname{diag}(e^{i\pi s},1,1,1),\quad
0\le s\le1,\quad \det Z(s)=e^{i\pi s}\ne0,
\]
\[
Z(0)=I_4,\qquad Z(1)=\operatorname{diag}(-1,1,1,1).
\]
A continuous \(r(Z(s))\) would connect determinant-positive and determinant-negative real invertible matrices, violating continuity of \(\det r(Z(s))\) without zeros. QED.

This theorem is about the unrestricted **off-shell complex domain** and an output preserving *all* real coframes of both orientations. It does NOT forbid selecting a fixed orientation from a restricted domain, a discontinuous selective outcome map, a patchwise selector with excluded points, or a microscopic dynamics in which the interpolating complex path is forbidden or dynamically inaccessible. The metric along the interior of the explicit path is complex (not an on-shell classical geometry). The result is a structural warning against imposing a universal, smooth, branch-preserving "collapse-as-retraction" on all possible complex jets, NOT proof that physical collapse is discontinuous.

<!-- UNIT: observer -->
## Jeden pozorovatel nerozliší různé metrické první jety

A separate obstruction comes from the **existing observer readout**, which loses quaternionic right-unitary phase data. Fix the illustrative reference \(N=I_2\) and its already defined candidate normalized density
\[
\rho_I[\Theta]=\frac{\Theta\Theta^\dagger}{\operatorname{tr}(\Theta\Theta^\dagger)}.
\]
On a local coordinate patch with trivial comparison derivative \(D=d\), define a single biquaternion field and a second phase-related field
\[
\Theta=I_2+i(tI_2+x\sigma_1+y\sigma_2+z\sigma_3),\qquad
U(t)=\operatorname{diag}(e^{iat},e^{-iat}),\qquad \Phi=\Theta U(t),
\]
with real \(a\). Because \(U U^\dagger=I_2\), their **entire same-reference readout history** agrees wherever the normalization is defined:
\[
\boxed{\rho_I[\Phi](t,x,y,z)=\rho_I[\Theta](t,x,y,z).}\tag{D}
\]
Yet at the coordinate origin, both first jets are anti-Hermitian, strictly nondegenerate real Lorentz tetrads, and
\[
g[\Theta](0)=\eta,\qquad
\boxed{
g[\Phi](0)=
\begin{pmatrix}
-1+a^2&0&0&a\\
0&1&0&0\\
0&0&1&0\\
a&0&0&1
\end{pmatrix},\quad \det g[\Phi](0)=-1.
}\tag{E}
\]
For \(a\ne0\) the same single-observer \(\rho_I\) history does not determine even the canonical local metric components of the admissible real first jet at that point. This comes from the extra \(dU\) term in \(d(\Theta U)\), not from a new fundamental tetrad. Both geometries could be related by a coordinate/frame change in a larger construction; **inequivalent gravity or different on-shell solutions are not claimed**. Also, the second field need not preserve the Lorentz-real jet condition throughout a surrounding open patch; the strict physical comparison is pointwise at the origin. A legitimate full observer-and-geometric protocol must dynamically control the allowed phase transport and may require several calibrated clocks or derivative observables.

<!-- UNIT: loop-holonomy -->
## Smyčky nekomutujících fází: konstruktivní kandidát invariantní vůči změně rámce

A useful constructive phase observable candidate, distinct from a geometric reality projection, arises from **noncommuting** normalized quaternion rotations. Let
\[
U_\alpha=e^{i\alpha\sigma_1},\quad
V_\beta=e^{i\beta\sigma_2},\quad
W=U_\alpha V_\beta U_\alpha^{-1}V_\beta^{-1}\in SU(2).
\]
Direct Pauli-matrix algebra gives the exact closed-loop character
\[
\boxed{\chi(\alpha,\beta)=\tfrac12\operatorname{tr}W
=1-2\sin^2\alpha\,\sin^2\beta.}\tag{F}
\]
In particular \(\chi(\pi/4,\pi/4)=1/2\ne1\): these two phase rotations do not commute. Under a **simultaneous** observer-frame change \(U_\alpha\mapsto G U_\alpha G^{-1}\), \(V_\beta\mapsto G V_\beta G^{-1}\), the loop transforms \(W\mapsto G W G^{-1}\), and its trace is invariant. More generally, if edge transports of a closed loop transform \(U_{ij}\mapsto G_iU_{ij}G_j^{-1}\), their ordered product conjugates by the group element at the base vertex, leaving its trace invariant. This is standard Wilson-loop/holonomy algebra.

This is a **positive conditional observable-design principle**: a calibrated network of observers sensitive to relative phase transport could use \(\chi\) rather than a raw angle or an imposed Hermitian reality projection. But a selected microscopic transport and loop are missing. If the relevant group is only the already-counted Lorentz spin frame, \(\chi\) would describe geometric spin holonomy rather than a new internal force or an objective collapse signal. It is NOT yet a physical measurement outcome, detector prescription, or UBT prediction.

<!-- UNIT: decision -->
## Důsledky a další dynamický test

The user's hypothesis of multiple noncommuting biquaternion phases and phase-sensitive selection remains a **research hypothesis**, not established collapse physics. The three exact gates combine as follows: (A)–(B) show that a simple valuewise reality projection may lose metric rank; (C) shows no continuous retraction preserving both real orientations on the entire complex nondegenerate jet space; (D)–(E) show that the prior single-clock density readout hides jet/geometry information in relative phases. None of them singles out a physical branch or derives Born probabilities.

Research priority: determine the dynamically admissible subspace and constraints of the original \(\Theta\); identify physical vs frame rotations among \(SL(2,\mathbb C)\), quaternionic \(SU(2)\) and right \(U(2)\) phases; construct a Lorentz-covariant multi-observer or operational phase-comparison law for the **first jet**, not just field values; and test a candidate selection law for (i) anti-Hermitian Lorentz slice, (ii) \(\det e\ne0\), (iii) constraint preservation, (iv) consistency with the complex-time \(\psi\) sector and (v) positive, normalized outcome probabilities. No modification of the Axiom C central-sharp metric, independent tetrad, or externally imposed FLRW clock is licensed.

Prior UBT sources: research_tracks/unified_physics_axioms/BIQUATERNION_MULTIPHASE_GROUP_GATE_2026_11_12.en.md; research_tracks/information_first/THETA_OBSERVER_RELATIVE_INFORMATION_CHANNEL_2026_11.en.md; research_tracks/information_first/THETA_OBSERVER_PHASE_LINKS_MULTI_CLOCK_CURVATURE_GATE_2026_11_13.en.md; research_tracks/T1_GR/gr_full_biquaternion_multirotation_2026_11_19.en.md; research_tracks/T1_GR/gr_phase_collapse_selection_gate_2026_11_19.en.md; research_tracks/action_selection/phase_central_metric_compatibility.en.md. Regression: tools/verify_gr_phase_selection_retraction_2026_11_19.py (exact SymPy), independently run locally PASS. The topology proof is analytic and not inferred from finite examples.
