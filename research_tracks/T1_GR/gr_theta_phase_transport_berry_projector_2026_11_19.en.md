<!-- BILINGUAL-UNIT: gr-theta-phase-transport-berry-projector-2026-11-19 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact conditional phase-transport algebra and parameter-space eigenbundle; NOT a UBT photon, Born collapse or selected gravity law.
UBT-AI-PROVENANCE-END
-->
# Theta phase transport: a pure-gauge no-go and a nontrivial observer eigenbundle

<!-- UNIT: scope -->
## Scope and novelty discipline

Full biquaternion Theta, locked central-sharp tetrad and observer-conditional rho_N remain unchanged. We test the proposed phase-transport mechanism before treating a nontrivial product of free quaternion rotations as a physically derived holonomy. The new result in this research note is a precise contrast between pure-gauge polar transport and a positive off-shell eigenbundle Berry example, plus a sharp degeneracy gate.

<!-- UNIT: pure -->
## Pure-gauge transport from one single-valued field is flat

Use the SAME original full biquaternion field, invertible on a declared patch, with its ordinary polar factor \(T_N=P_NU_N\) for a specified positive observer reference \(N\). If one defines link variables only by a single-valued local phase factor \(U_N(x)\),
\[
\ell_{ij}=U_N(x_i)^{-1}U_N(x_j),
\quad
\ell_{12}\ell_{23}\cdots\ell_{n1}=I_2.
\]
The continuous connection \(A_U=U_N^{-1}dU_N\) satisfies exactly
\[
\boxed{F_{A_U}=dA_U+A_U\wedge A_U=0.}\tag{A}
\]
When \(U_N\) is globally single-valued, parallel transport around a closed path is identity (even if the configuration space is not simply connected). A distinct multivalued lift or a nontrivial bundle connection must be specified explicitly before assigning nontrivial global holonomy.

The earlier computed \(W=UVU^{-1}V^{-1}\) can be nonidentity for independently chosen noncommuting \(U,V\in SU(2)\), but it is NOT the Wilson loop of the above single-valued pure-gauge links: the genuine links telescope. To realize \(W\ne I_2\) as a physical loop, one must derive or specify non-flat inter-point transport. Likewise the direct candidate \(A=-(d\Theta)\Theta^{-1}\) has zero curvature and makes \(D\Theta=d\Theta+A\Theta=0\), giving a degenerate **canonical** tetrad; it is not a free gravity mechanism.

This Maurer–Cartan no-go is standard gauge geometry, not an original quantum or gravity theorem. Related UBT work already found \(da_{\det}=0\) for the determinant-only central phase and a residual unselected SO(2) curvature in the physical Lorentz connection.

<!-- UNIT: eigen -->
## Exact positive eigenbundle phase geometry from ONE Theta

A separate, constructive option uses the spectral **eigenbundle** of the existing candidate observer matrix instead of the pure-gauge unitary factor. Select an auxiliary parameter two-sphere \(S^2\) with coordinates \((\theta,\varphi)\). This is a space of CONFIGURATION PARAMETERS, not assumed to be physical spacetime or the imaginary-time \(\psi\) circle. Let
\[
\mathbf n=(\sin\theta\cos\varphi,\sin\theta\sin\varphi,\cos\theta),
\qquad
\boxed{P=\tfrac12(I_2+\mathbf n\cdot\boldsymbol\sigma).}\tag{B}
\]
\(P\) is a globally smooth rank-one Hermitian projector with \(P^2=P\) and \(\operatorname{tr}P=1\). Construct the ONE original biquaternion field (as a smooth family of faithful complex matrix representatives)
\[
\boxed{\Theta(\mathbf n)=I_2+P(\mathbf n),\quad \Theta^\dagger=\Theta>0,\quad \det\Theta=2.}\tag{C}
\]
No additional fundamental field is introduced. For the already proposed conditional observer readout with fixed reference \(N=I_2\),
\[
\rho_I[\Theta]=\frac{\Theta\Theta^\dagger}
{\operatorname{tr}(\Theta\Theta^\dagger)}
=\boxed{\frac{I_2+3P}{5}},
\quad
\operatorname{spec}(\rho_I)=\{4/5,1/5\}.
\]
The projector is recoverable as \(P=(5\rho_I-I_2)/3\). Thus this particular observer protocol has a nondegenerate, smoothly varying spectral line.

Its standard Berry curvature, in this **fixed reference trivialization**, is the globally defined form
\[
\mathcal F_P=-i\,\operatorname{tr}(P\,dP\wedge dP)
=\boxed{\tfrac12\sin\theta\,d\theta\wedge d\varphi}.\tag{D}
\]
By direct integration,
\[
\boxed{c_1(P)=\frac1{2\pi}\int_{S^2}\mathcal F_P=1.}\tag{E}
\]
A local eigenvector \(|u\rangle=(\cos(\theta/2),e^{i\varphi}\sin(\theta/2))^\mathsf T\) defines \(a=-i\langle u|du\rangle=\sin^2(\theta/2)d\varphi\) in its gauge chart; it cannot furnish one globally smooth normalized eigenvector over this entire \(S^2\). The **projector P and full Theta are nevertheless globally smooth and invertible**. This is the usual Chern-1 eigenline (Hopf-bundle) topology.

Crucially here \(\Theta\) is POSITIVE Hermitian, so its right polar unitary \(U_N\) (for \(N=I_2\)) is simply \(I_2\). The nonzero \(\mathcal F_P\) therefore comes from projection onto an eigenline of the observer state, **not** from the globally pure-gauge polar-unitary \(U_N^{-1}dU_N\). It avoids the trivial-holonomy algebra of the first section without introducing an independent field. This is a real finite-dimensional mathematical construction, but it does NOT imply a Maxwell field, an on-shell spacetime geometry, or physical collapse from UBT.

<!-- UNIT: gap -->
## Eigenvalue degeneracy prevents global unique branch selection

The spectral branch selector is sharply limited at degeneracy. For real \(0<\varepsilon<1\), put
\[
\Theta_\varepsilon=I_2+\varepsilon(2P-I_2),\qquad
\rho_\varepsilon=\frac12I_2+\frac{2\varepsilon}{1+\varepsilon^2}(P-\tfrac12I_2).
\]
For every \(\varepsilon>0\), the larger-eigenvalue projector is \(P\), independent of \(\varepsilon\). But
\[
\boxed{\lim_{\varepsilon\downarrow0}\rho_\varepsilon=\tfrac12 I_2}
\]
for **every** Bloch direction \(\mathbf n\). At the maximally mixed point there is no uniquely selected one-dimensional eigenprojector: approaching from the north gives \(P_N=\operatorname{diag}(1,0)\), from the south \(P_S=\operatorname{diag}(0,1)\). Therefore **no continuous assignment of the preferred eigenline extends through this degeneracy while agreeing with the nondegenerate spectral selector on all approaches**.

This is ordinary spectral geometry, not evidence that physical wavefunction collapse has occurred. If one tries to identify the preferred eigenline with the actual measured result, the probability rule and dynamical admissibility must still be obtained. Choosing only the larger eigenvalue by hand is NOT Born's rule.

<!-- UNIT: cov -->
## Covariance and the still-open physical Lorentz jet gate

An important *frame-covariance* qualification follows from the prior observer works. Under \(P\mapsto GPG^{-1}\) for a **position-dependent** spin-frame transformation \(G\in SU(2)\), computing \(-i\operatorname{tr}(P\,dP\wedge dP)\) with the ordinary \(d\) while silently resetting the frame connection to zero is not a valid local gauge-invariant measurement protocol. Given a COMPATIBLE and PHYSICALLY SELECTED comparison connection \(\Gamma\), define \(D_\Gamma P=dP+[\Gamma,P]\) and its ambient curvature \(F_\Gamma=d\Gamma+\Gamma\wedge\Gamma\). The induced eigenline connection has two-form
\[
\boxed{
\mathcal F_P^\Gamma=-i\operatorname{tr}\!\left(
P\,F_\Gamma+P\,D_\Gamma P\wedge D_\Gamma P
\right).
}\tag{F}
\]
With the usual anti-Hermitian matrix connection convention, this is invariant under simultaneous transformations of \(P,\Gamma\) by conjugation and the corresponding inhomogeneous connection law. Its integral on a closed \(S^2\) remains the first Chern number of the chosen eigenline bundle, though local curvature distributions can depend on the chosen connection. The fixed trivialization \(\Gamma=0\) gives (D). **The UBT microscopic law fixing \(\Gamma\) remains OPEN.**

Furthermore the explicit field family \(\Theta=I_2+P\) on the auxiliary parameter sphere is Hermitian and its ordinary derivatives are Hermitian. It is NOT a verified classical UBT tetrad family satisfying \(E_\mu^\dagger=-E_\mu\) on a physical four-dimensional Lorentz spacetime, nor a solution of any finalized fundamental UBT action. The same locked central-sharp metric remains unmodified. Any lift to the real Lorentz solution sector needs a separately derived physical first jet and torsion/connection dynamics.

<!-- UNIT: next -->
## Next derived transport requirements and provenance

**Decision for the ongoing UBT programme:** Two precise alternatives are now distinguished. Raw full-biquaternion polar phase transport from a single global \(U_N\) is flat and cannot by itself supply local physics. Projection onto an observer spectral eigenline can produce an integer Berry/Chern phase invariant without an independent field, but it requires a dynamically selected observer protocol, a phase comparison connection and, crucially, a CLASSICAL metric-compatible jet lift. The nondegenerate spectral selector also has an unavoidable degeneracy boundary. The existing central sharp phase-metric obstacle and the prior relative-Berry linear-photon no-go remain binding.

Priority next tests: (1) find a fully first-jet-compatible \(\Theta\) FAMILY plus physical observer references \(N\) on a parameter surface while maintaining the strict real Lorentz tetrad and nondegenerate metric; (2) derive rather than insert the observer/spin connection \(\Gamma\) from the full two-sided \(D_\mu\Theta\) or the constrained action; (3) determine whether the resulting eigenline curvature survives physical gauge reduction and is accessible to a legitimate finite-energy UBT probe; (4) perform Hamiltonian constraint and vacuum linearization checks; (5) only then ask if a measurement instrument/selective update can emerge and obey normalization/Born probabilities. No ad hoc global clock, FLRW metric, photon kinetic term or collapse rule is inserted.

References already in repo: research_tracks/information_first/THETA_OBSERVER_SO2_HOLONOMY_IDENTIFIABILITY_GATE_2026_11_14.en.md; research_tracks/information_first/THETA_OBSERVER_QED_BERRY_VACUUM_LINEARIZATION_GATE_2026_11_14.en.md; research_tracks/information_first/THETA_OBSERVER_RELATIVE_INFORMATION_CHANNEL_2026_11.en.md; research_tracks/T1_GR/gr_full_biquaternion_multirotation_2026_11_19.en.md. The mathematical identities are the standard Maurer–Cartan, rank-one Berry projector, Hopf-bundle and eigenvalue-crossing facts, not a novel UBT observational prediction.

Focused executable symbolic regression: tools/verify_gr_theta_phase_transport_berry_projector_2026_11_19.py. Analytic topology and physical scope claims are independently stated; exact matrix tests are not a proof of microscopic UBT dynamics.
