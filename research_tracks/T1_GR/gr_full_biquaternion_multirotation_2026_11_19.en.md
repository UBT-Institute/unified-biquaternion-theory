<!-- BILINGUAL-UNIT: gr-full-biquaternion-multirotation-phase-2026-11-19 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact conditional finite algebra; no quantum-collapse selection or physical gauge extension proved.
UBT-AI-PROVENANCE-END
-->
# Full-biquaternion phase and multirotations: metric and observer selection gates

<!-- UNIT: scope -->
## Scope: reuse the entire quaternionic phase

Earlier UBT tracks already considered several noncommuting quaternion rotations, noncompact complex directions, two-sided field transformations, phase winding and observer-relative phase information. This note joins those existing results; the original full biquaternion Θ is never reduced to one physical phase angle. All claims are finite-dimensional conditional algebra, not a new chosen microscopic action or quantum-collapse mechanism.

<!-- UNIT: decomposition -->
## Full group decomposition and double-rotation structure

Use exactly the original biquaternion \(\Theta\in\mathbb B=\mathbb C\otimes\mathbb H\simeq\operatorname{Mat}_2(\mathbb C)\), with quaternion conjugation \(\sharp\), represented by the matrix adjugate. Let the quaternion generators satisfy \(\mathbf I^2=\mathbf J^2=\mathbf K^2=-1\) and \([\mathbf I,\mathbf J]=2\mathbf K\). The central complex unit \(i\) commutes with these generators. For a generic invertible matrix \(q=\rho(\Theta)\),
\[
q^\sharp q=(\det q)I_2,\qquad
\boxed{q=zS,\quad z^2=\det q,\quad S\in SL(2,\mathbb C).}\tag{A}
\]
This factorization is **local** on a region where \(\det q\ne0\) and a continuous square root is chosen. Its sign-paired ambiguity is \((z,S)\sim(-z,-S)\):
\[
GL(2,\mathbb C)\simeq
\big(\mathbb C^\times\times SL(2,\mathbb C)\big)/\mathbb Z_2.
\]
Further polar-factorize \(S=PU\), with \(P=(SS^\dagger)^{1/2}\) positive Hermitian and \(\det P=1\), and \(U=P^{-1}S\in SU(2)\). Locally there are **eight real parameters**: one logarithmic amplitude in \(z\), one central angle in \(z\), three positive-Hermitian boost directions in \(P\), and three compact quaternionic rotation directions in \(U\). These are algebraic coordinates, NOT eight automatically independent observable fields or gauge generators.

For a pure unit-sharp biquaternion, \(S^\sharp S=I_2\), the group is \(SL(2,\mathbb C)\) (real dimension six). For example,
\[
e^{\alpha\mathbf I}=\cos\alpha+\mathbf I\sin\alpha,\qquad
e^{i\beta\mathbf I}=\cosh\beta+i\mathbf I\sinh\beta .
\]
The first one is a compact quaternion rotation, the second a noncompact hyperbolic one. Different quaternion-axis rotations do not commute. Thus a "full phase" is not simply several independent commuting \(U(1)\) angles.

<!-- UNIT: metric -->
## Sharp-unit multirotations conserve the central metric

On the classical Lorentz-real tetrad, the **locked** geometric law is
\[
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta,\quad
g_{\mu\nu}I_2=\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu).
\]
For arbitrary \(L,R\in SL(2,\mathbb C)\), suppose the composite two-sided jet transforms homogeneously as \(E_\mu'=L E_\mu R^{-1}\); this requires the proper corresponding connection transformation. From \((ABC)^\sharp=C^\sharp B^\sharp A^\sharp\) and \(L^\sharp=L^{-1}\), \(R^\sharp=R^{-1}\), we obtain
\[
\begin{split}
(E_\mu')^\sharp E_\nu'
&=R E_\mu^\sharp L^{-1} L E_\nu R^{-1}\\
&=R(E_\mu^\sharp E_\nu)R^{-1},
\end{split}
\qquad
\boxed{g_{\mu\nu}'=g_{\mu\nu}.}\tag{B}
\]
The metric coefficient may be complex for a generic full-complex first jet, but it is algebraically central. Thus any arbitrary sequence of **sharp-unit** two-sided rotations preserves every component of that central metric: it cannot turn an initially complex metric into a real metric.

Even allowing arbitrary invertible \(L,R\in GL(2,\mathbb C)\) instead, the only change is a **common** complex scale:
\[
\boxed{g_{\mu\nu}'=\frac{\det L}{\det R}\,g_{\mu\nu}.}\tag{C}
\]
All independent component ratios of a nonzero metric are invariant. If some such ratio is non-real, no single common complex rescaling can make the entire metric real. An explicit full-complex four-jet example is
\[
E_0=e^{i\pi/4}(iI_2),\quad E_j=i\sigma_j,\qquad
g_{\mu\nu}=\operatorname{diag}(-i,1,1,1).
\]
Here \(g_{00}/g_{11}=-i\notin\mathbb R\). Therefore neither sharp-unit left/right multirotations, nor their unrestricted invertible extension acting homogeneously on the same jets, can reach an everywhere-real metric in this example. The example is an algebraically admissible full-complex affine jet, NOT a physical on-shell classical Lorentz tetrad.

This **does not** preclude a nonunitary measurement-conditioned state update, changes of an entire solution including its derivative and connection, or a dynamically selected subset of solutions. It does rule out a universal "real collapse = just several internal rotations of the same fixed complex jet" claim under the stated group actions.

<!-- UNIT: stabilizer -->
## Which double rotations really preserve the Lorentz-real slice?

The full pointwise subgroup preserving the **entire** physical Lorentz-real slice \(W_L=i\,\mathrm{Herm}_2\) is much smaller than the independent two-sided group.

**Proposition (two-sided reality stabilizer).** Suppose \(L,Q\in SL(2,\mathbb C)\) and \(LHQ\) is Hermitian for **every** Hermitian \(2\times2\) matrix \(H\). Define \(M=Q(L^\dagger)^{-1}\). The requirement is equivalent to
\[
HM=M^\dagger H\qquad\text{for every }H=H^\dagger.
\]
Taking \(H=I_2\) gives \(M=M^\dagger\); commuting with all Hermitian matrices then forces \(M=cI_2\), \(c\in\mathbb R\). The determinant-one condition yields \(c^2=1\). Consequently
\[
\boxed{Q=\pm L^\dagger.}\tag{D}
\]
For \(E'=L E R^{-1}\), this is \(R^{-1}=\pm L^\dagger\). The positive-sign component is the usual Lorentz spin congruence \(E'=L E L^\dagger\); the negative sign reverses the full tetrad and can affect time orientation. Independent left/right sharp-unit matrices conserve the complex metric but **need not** preserve the Lorentz-real tetrad slice.

The theorem requires preservation for **all** Hermitian inputs, not just existence of a special correction for one chosen complex field configuration. It is a real-slice stabilizer classification under homogeneous complex-linear two-sided actions, NOT a classification of every possible non-linear or observer-conditional UBT branch-selection mechanism.

<!-- UNIT: winding -->
## Global sign ambiguity and determinant winding

The \(\mathbb Z_2\) pairing in (A) has a real global consequence. On a closed loop \(\gamma\) where \(\det\Theta\ne0\), a globally single-valued continuous scalar square root \(z\) with \(z^2=\det\Theta\) requires the determinant winding to be even:
\[
\operatorname{wind}_\gamma(\det\Theta)
=2\operatorname{wind}_\gamma z\in2\mathbb Z.\tag{E}
\]
For an illustrative loop parameter \(s\in[0,2\pi]\), the invertible matrix
\[
\Theta(s)=\operatorname{diag}(e^{is},1),\quad
\det\Theta(s)=e^{is}
\]
is single-valued on the loop, but a local square root \(z=e^{is/2}\) changes sign at \(2\pi\). Thus the **full biquaternion** can be global even when the separate central-phase and \(SL(2,\mathbb C)\) factors cannot both be chosen globally and continuously without transition signs.

This is an exact square-root/winding fact, not a proof of topological protection of a physical UBT excitation. The original canonical \(\psi\) coordinate is not asserted compact here: the example applies to ANY chosen closed parameter loop, with a compact \(\psi\)-fiber only as an extra optional model. The earlier full-Theta winding analysis already gives off-shell interpolations through \(\det\Theta=0\) while the canonical tetrad stays regular; those interpolations can invalidate winding conservation unless microscopic dynamics forbids them.

<!-- UNIT: observer -->
## Observer-relative polar phase and multi-clock information

The **existing candidate observer protocol** gives a particularly natural meaning to several relative phases, without changing the locked gravitational metric. For a selected positive Hermitian reference clock \(N\), define
\[
T_N=N^{-1/2}\Theta N^{-1/2},\qquad
T_N=P_N U_N,\quad
P_N=(T_NT_N^\dagger)^{1/2},\quad U_N\in U(2),\tag{F}
\]
on invertible \(T_N\), and
\[
\boxed{\rho_N=\frac{P_N^2}{\operatorname{tr}(P_N^2)}.}\tag{G}
\]
The **four real \(U(2)\) phase parameters** (one central phase plus three \(SU(2)\) rotation coordinates) are invisible in this one-clock \(\rho_N\). They are NOT necessarily fundamental gauge redundancies. As previously proved in the multi-clock research, different calibrated noncommuting reference clocks can recover relative right-unitary information up to a remaining complex scalar. This is a candidate operational meaning of "many phases".

Exact witness: choose \(\Theta=\operatorname{diag}(2,i)\), \(V=\sigma_1\), and the observer \(N_0=I_2\). Then
\[
\rho_{N_0}[\Theta]=\rho_{N_0}[\Theta V]
=\operatorname{diag}(4/5,1/5).
\]
For \(N_1=\operatorname{diag}(2,1/2)\), the same two full fields instead give
\[
\rho_{N_1}[\Theta]=\operatorname{diag}(1/5,4/5),\qquad
\rho_{N_1}[\Theta V]=\operatorname{diag}(4/5,1/5).
\]
These different readout values demonstrate **recoverable relative-phase information**, not a physical collapse or a reason why the corresponding full field jets must solve UBT dynamics. Under simultaneous Lorentz transformations of \(\Theta\) and \(N\), the normalized \(T_N\) transforms by unitary conjugation, and its polar factors do likewise. A physical measurement selection law and compatible canonical metric still need to be derived.

<!-- UNIT: decision -->
## Conclusions and next concrete gate

**Scientific decision.** We should test the user's phase-based reality-selection hypothesis with the full left/right biquaternion field and observer-relative phase data; reducing it to one \(e^{i\phi}\) is unjustified. But by the exact gates (B)--(D) multirotations *alone* leave too many complex geometries and can represent mere frame changes. Genuine selection of an observable Lorentz-real branch must add a derived physical condition, for example a measurement instrument acting on a quantum/operational state or a dynamically selected real invariant sector, **not** simply call a two-sided sharp-unit rotation a collapse.

Priority steps: identify the full on-shell symmetry/constraint group of \(D_\mu\Theta\); distinguish geometric Lorentz gauge from internal relative phases; derive a covariant observer measurement channel and its physical selection/outcome law; verify that the selected state has nondegenerate canonical sharp-derived real tetrad and preserves the Hamiltonian constraints; then test whether \(\psi\)-holomorphy or phase-winding supplies a real dynamical selection condition. Do not promote old real-part/trace projections to canonical metrics.

Existing related sources: canonical/AXIOMS.md; research_tracks/unified_physics_axioms/BIQUATERNION_MULTIPHASE_GROUP_GATE_2026_11_12.en.md; research_tracks/unified_physics_axioms/BIQUATERNION_TWO_SIDED_PHASE_LORENTZ_GATE_2026_11_12.en.md; research_tracks/information_first/THETA_OBSERVER_RELATIVE_INFORMATION_CHANNEL_2026_11.en.md; research_tracks/action_selection/mm_full_theta_psi_winding_decoupling_2026_11.en.md; research_tracks/T1_GR/gr_phase_collapse_selection_gate_2026_11_19.en.md. This note sharpens their connection; group identities are standard algebra, not a new experimentally confirmed UBT prediction.

Exact finite algebra regression: tools/verify_gr_biquaternion_multirotation_gate_2026_11_19.py. Its symbolic examples do not prove the full stabilizer theorem or global topological statement without the analytic arguments given here.
