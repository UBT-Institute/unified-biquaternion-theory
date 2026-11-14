<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact conditional representation and Wilson-loop information calculations, not a derived microscopic quantum action, electromagnetic charge or photon.
UBT-AI-PROVENANCE-END
-->

# Quantum observer holonomy → kinetic selector gate: why residual SO(2) is not automatically electromagnetic U(1)

**2026-11-14 — NEW COMPARISON GATE (L0 conditional algebra); QED/GR/SM OPEN.**

This continues the approved derivation order
\[
\Theta\ \longrightarrow\ \text{quantum state/observer + gravity geometry}
\ \longrightarrow\ \text{QED benchmark and GR}
\ \longrightarrow\ \text{classical Maxwell and broader SM}.
\]
The full \(\Theta\in\mathbb C\otimes\mathbb H\simeq M_2(\mathbb C)\), locked real Lorentz tetrad and sharp metric are unchanged. This note REUSES the established two-carrier \(\mathrm{SO}(2)\) stabilizer calculations rather than claiming to discover that group.

**Sources already in the repository:** research_tracks/fundamental_dynamics/field_built_so2_connection_family.en.md; residual_so2_curvature_decision_gate.md; residual_so2_invariant_basis.en.md; research_tracks/action_selection/central_phase_metric_gate.en.md; research_tracks/information_first/THETA_OBSERVER_SO2_HOLONOMY_IDENTIFIABILITY_GATE_2026_11_14.en.md (same PR); SHARED_REALITY_PRINCIPLE.md.

## 1. Distinguish the three candidate phase structures

(a) The local normalized observer readout \(\rho_N[\Theta]\) forgets a central scalar phase, but the scalar multiplication of the FULL Theta does not generally preserve the locked \(E_\mu\in i\mathrm{Herm}_2\) and central sharp metric (central_phase_metric_gate.en.md).

(b) The determinant phase \(\tfrac12\,d\arg\det\Theta\) is a locally exact 1-form on invertible patches: its smooth curvature is identically zero, so no local propagating photon follows from that prescription alone.

(c) In the existing two-carrier Lorentz-real branch, the transverse oriented-plane stabilizer \(\mathrm{SO}(2)\) has an Abelian connection \(\alpha\) (relative to a chosen reference), potentially with nonzero curvature. This is a **Lorentz frame/spin connection sector**, NOT automatically an *internal* electromagnetic charge connection. The existing first-jet action is blind to its free stabilizer shifts and does not determine \(\alpha\).

These are distinct mathematical objects; a relative observer phase, a determinant phase and a transverse spin holonomy must NOT be identified without an intertwiner and an actual physical action.

## 2. Exact conditional representation obstruction: spin holonomy is not universal electric charge

At an adapted tetrad point take the transverse SO(2) spin-half generator
\[
G_{\rm spin}=\frac i2\sigma_1,\quad
U_{\rm spin}(\varphi)=e^{\varphi G_{\rm spin}}
=\cos(\varphi/2)I+i\sin(\varphi/2)\sigma_1.
\]
Its eigenstates \(|\pm x\rangle\) acquire **opposite** phases \(e^{\pm i\varphi/2}\). By contrast, an ordinary electromagnetic U(1) transformation on *the two spin polarization states of one particle with a fixed electric charge* \(q\) acts as
\[
U_{\rm EM}(\chi)=e^{iq\chi}I_2.
\]
The Lie generators differ in their spectra and trace:
\[
\boxed{\operatorname{tr}G_{\rm spin}=0,\quad
\operatorname{spec}G_{\rm spin}=\{+i/2,-i/2\},\quad
\operatorname{tr}(iqI_2)=2iq\ne0\ (q\ne0)}.
\]
No similarity transformation can identify them for fixed nonzero \(q\). In fact \(G_{\rm spin}\) does not commute with all Lorentz-spin generators: with \(G_2=i\sigma_2/2\),
\[
[G_{\rm spin},G_2]=-\tfrac i2\sigma_3\ne0.
\]
An *internal* electromagnetic gauge charge acting on an irreducible left Weyl representation must commute with the Lorentz action and is scalar on its spin indices. The transverse SO(2) rotation is therefore **not the physical EM U(1) as-is** in this representation.

This is NOT a universal no-go: an additional internally represented U(1) on physical charged composite states, a different nontrivial representation on a larger quantum Hilbert space, or a derived coupling distinct from the Lorentz spin lift may work. In each case its charge assignments, separate gauge redundancy, and GR compatibility must be derived, not inferred from \(\mathrm{SO}(2)\simeq U(1)\).

## 3. Exact quantum-information bridge: Wilson interferometric contrast induces a curvature-square COMPARATOR

For a small loop \(\square_{\mu\nu}\) of oriented area \(A\) in an adapted transverse frame, let the integrated residual curvature be \(\varphi=A f_{\mu\nu}+O(A^{3/2})\) for sufficiently smooth connection and a small roughly square loop. Take the *assumed* spin-half parallel transporter
\[
U_\square=\exp(\varphi G_{\rm spin}).
\]
The gauge-conjugation invariant normalized spin-character is
\[
\boxed{w_\square=\tfrac12\operatorname{Re}\operatorname{tr} U_\square
=\cos(\varphi/2)}.
\]
Define a **trial** positive interferometric contrast-loss cost
\[
\boxed{I_\square=1-w_\square
=1-\cos(\varphi/2)
=\tfrac18 A^2 f_{\mu\nu}^2+o(A^2)}.
\]
This is an EXACT Taylor identity for the chosen unitary representation and chosen cost, not an exact UBT information principle. A concrete 4D Euclidean hypercubic discretization with square side \(\ell\), area \(A=\ell^2\) and a fixed per-plaquette coefficient gives
\[
\sum_{\square_{\mu\nu}}I_\square
\longrightarrow\frac18\int d^4x\sum_{\mu<\nu} f_{\mu\nu}^2
\]
in the smooth continuum limit (up to fixed site counting, cell orientation and overall normalization). It is a standard Wilson/holonomy mechanism providing a way for **quantum comparison data to motivate a derivative-sensitive action**, rather than merely postulating an arbitrary independent Maxwell term. The cost is nevertheless a chosen *hypothesis*, its coefficient and physically allowed probes are unselected, and \(\alpha\) is not yet a unique functional of Theta.

**Important Lorentzian obstruction:** the positive sum \(\sum_{\mu<\nu}f_{\mu\nu}^2=|\mathbf E|^2+|\mathbf B|^2\) is a Euclidean norm in a selected coordinate frame. The Lorentz-invariant kinetic scalar is
\[
\tfrac12 f_{\mu\nu}f^{\mu\nu}=|\mathbf B|^2-|\mathbf E|^2
\quad\text{for signature }(-,+,+,+).
\]
Hence **positive local interferometric information loss does not by itself derive the sign structure of the relativistic Maxwell action**, nor the canonical momentum, Gauss constraint or the positive physical Hamiltonian. A rigorous derivation must provide real-time causal/symplectic structure, an appropriate Wick continuation or an independently derived covariant action selection. The positive expression instead resembles Euclidean Yang–Mills density or the ordinary Maxwell *energy* density, which is not identical to the Lorentzian Lagrangian.

## 4. Why this is still not a single-Theta photon

The old stabilizer result states for the restricted first-jet family
\[
\omega\mapsto\omega+\alpha J,\quad JV=JW=0,\quad
D_\omega\Theta\text{ and }g\text{ unchanged}.
\]
Consequently local \(\Theta,D\Theta,g,\rho_N[\Theta]\) alone cannot choose \(\alpha\); no curvature kinetic Hessian follows from first-jet observer entropy. Our Wilson expression compares connection holonomies and can detect \(\alpha\), but requires a physically specified quantum transporter. Introducing an unconstrained \(\alpha\) with a manually chosen \(\int f^2\) would simply reproduce a Maxwell-like comparison theory, not derive a photon from the single Theta dynamics.

Further, the existing residual_so2_invariant_basis.en.md already classified derivative-weight ≤2 local invariant terms in the reduced two-carrier sector; it found that at that weight the residual \(\alpha\) is algebraic/auxiliary. A Maxwell-like curvature-square has higher weight in that counting, so the proposed plaquette comparator does not contradict the earlier basis theorem. The actual derivative order **after eliminating \(\omega[\Theta]\)** and any possible higher-derivative instabilities need explicit calculation.

Physical requirements still missing: an on-shell, constrained one-Theta Hamiltonian, local first-class U(1) commuting with Lorentz, massless spin-1 pole with two healthy helicities, coupling to a conserved electric current, Ward identities, positive energy, and a controlled classical Maxwell limit. The same microscopic dynamics must remain compatible with the sharp-metric gravity/GR branch.

## 5. Most decisive next mathematical task

The next non-circular gate is to **derive the representation and symplectic generator of the internal charge from the one-Theta quantum observable algebra**. Work in a trial real-linear 8D Theta phase space and explicitly calculate:
1. whether a nontrivial central charge generator \(Q\) commutes with the Lorentz action on physical matter states while leaving the *physical* tetrad and its sharp metric invariant after all composite variations;
2. whether \(Q\) is first class under the selected constraints and has a conserved local current;
3. whether any dynamically selected quantum holonomy for \(Q\) has a curvature term with the correct causal sign and two healthy photons;
4. how the observer readout/wilson data constrain rather than merely rename this dynamics.

Do not postulate \(Q=iI\) as a physical symmetry of the full homogeneous tetrad: that possibility has an exact sharp-metric counterexample. Do not transfer \(G_{\rm spin}\) into electric charge merely because both generate abstract circles.

## Verification

Five focused SymPy tests were executed locally in the current session (2026-11-14) and passed: spin-vs-internal generator obstruction, opposite spin holonomy phases, exact Wilson contrast expansion, Euclidean-vs-Lorentzian sign distinction, and residual stabilizer first-jet blindness. Regression: tests/test_theta_quantum_so2_charge_information_gate.py. These checks verify algebra only.
