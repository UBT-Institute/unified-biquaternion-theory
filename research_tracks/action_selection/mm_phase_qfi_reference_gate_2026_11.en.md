<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: mm-phase-qfi-reference-20261101 -->
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

# Full-Theta phase information: reference-sensitive QFI does not protect winding

**2026-11-01 · C_working.** Restricted, exact mathematical readout test continuing the previous determinant-amplitude Fisher gate. Do not interpret a constructed quantum channel as a physical UBT probe or a selected action. Original full-complex Theta and the locked sharp tetrad stay unchanged.

## Projective Fisher metric and necessary phase reference [PROVED]

Let the central sharp norm be d=det Theta. Construct a *hypothetical calibrated two-level readout* with real reference amplitude a and relative complex amplitude d. This is a projective state-space encoding, **not** a new fundamental field, UBT quantum state, or independently derived observer channel:

\[
d(\psi)=\det\Theta(\psi),\qquad
v(\psi)=\begin{pmatrix}a\\d(\psi)\end{pmatrix},\qquad
|\Phi(\psi)\rangle={v(\psi)\over\sqrt{a^2+|d(\psi)|^2}},\qquad a>0.
\]
\[
F_Q=4\bigl(\langle\partial_\psi\Phi|\partial_\psi\Phi\rangle
-|\langle\Phi|\partial_\psi\Phi\rangle|^2\bigr)
=\boxed{\frac{4a^2|\partial_\psi d|^2}{(a^2+|d|^2)^2}}.
\]


The formula follows algebraically from the standard pure-state quantum Fisher information (four times the Fubini–Study metric). Under det-one SL(2,C) congruence d is invariant, but physical accessibility of the reference and psi calibration remain unproved. A **single-component** normalized phase e^{in psi/Rpsi} is only an overall quantum-state phase and has projective QFI zero; treating its ordinary derivative norm as QFI would be an error.

## Phase-sensitive distinction and an explicit measurement [PROVED]

For the exact original full-Theta winding family at a spacetime point, the additional readout **does** detect the magnitude of the phase winding:

\[
d_n(\psi)=\rho e^{in\psi/R_\psi},\quad a=\rho,\quad
F_Q[d_n]=\frac{n^2}{R_\psi^2},\quad
\mathcal J_Q[d_n]:=\int_0^{2\pi R_\psi}F_Q\,d\psi
=\frac{2\pi n^2}{R_\psi}.
\]
\[
p_\pm(\psi;\chi)=\frac12\pm
\frac{a\,\operatorname{Re}(e^{-i\chi}d(\psi))}
{a^2+|d(\psi)|^2},\qquad p_++p_-=1.
\]


The two outcomes are an equatorial projective measurement with tunable reference phase chi. At a=rho and generic psi, choosing chi=0 yields classical Fisher information for estimating psi equal to n²/Rpsi² (zero-probability fringes require a limiting interpretation). Thus the phase information is operationally accessible **IF** such a coherent reference and protocol exist. The QFI depends on n² and by itself does not determine the sign of n. J_Q is a geometric information integral, **not** energy, tension, or a physical psi Hamiltonian; in particular its overall coefficient is unselected.

## The determinant-zero crossing remains regular [PROVED]

Reuse the existing n=0 to n=1 interpolation from the previous full-Theta MM note. At its determinant zero, the original spacetime tetrad remains regular. For every fixed a>0 the projective readout and its QFI also remain smooth:

\[
s_*=\frac{\sqrt{1+\rho}-1}{\sqrt{1+\rho}-\sqrt{1-\rho}},
\quad d_{s_*}(\pi R_\psi)=0,\quad
\partial_\psi d_{s_*}(\pi R_\psi)=-\frac{i s_*\rho}{R_\psi},
\]
\[
\left.F_Q\right|_{s_*,\pi R_\psi}
=\frac{4s_*^2\rho^2}{a^2R_\psi^2}<\infty,
\qquad
0\le F_Q(\psi,s)\le\frac{4|\partial_\psi d_s|^2}{a^2}<\infty .
\]
\[
p_\pm\big|_{d=0}=\frac12,\quad
\chi=-\frac{\pi}{2}
\ \Longrightarrow\
F_{\mathrm{cl}}\big|_{s_*,\pi R_\psi}=F_Q\big|_{s_*,\pi R_\psi}.
\]


The upper bound is uniform along the compact smooth interpolation because a stays strictly positive and d'_s is bounded. The displayed chi measurement locally saturates the QFI at the zero by measuring the imaginary derivative. This shows a phase-sensitive reference can detect winding in nonsingular endpoints **without imposing an infinite Fisher cost at the crossing**.

Geometrically the rays [a:d] belong to CP¹, a 2-sphere with trivial fundamental group. In the chart a>0 the coordinate d traverses the origin smoothly; the integer winding lives only in the extra *punctured* region d != 0. The explicit Theta interpolation supplies the actual original-field lift on the restricted flat defining-connection chart, not merely an abstract CP¹ homotopy.

## Physical selection and shared-reality verdict [OPEN]

The old amplitude-only classical Fisher functional gives zero at both winding endpoints; this phase-sensitive *reference-dependent* QFI instead scales with n². Neither one derives a microscopic field action, imposes det Theta nonzero, supplies Cartan/Dirac constraints, or proves stable excitations. The full-Theta gravity-only MM comparator remains blind to the winding interpolation. Even postulating J_Q as a cost leaves the singular crossing finite and adds an unselected readout and coefficient.

The physical gate is to **derive rather than assume** a Theta-native observer algebra and measurement channel, the physical meaning/measure of psi, a phase reference (if any), and the composite covariant psi principal sector. Require its own constrained Hamiltonian and variational equations before asserting a winding particle or a new physical effect. Independent physical verification remains open.

## Verification and prior sources

Exact SymPy checks: `tests/test_mm_phase_qfi_reference_gate.py` (eight local tests). Reuses `research_tracks/action_selection/mm_winding_fisher_nonselection_2026_11.en.md`, `research_tracks/action_selection/mm_full_theta_psi_winding_decoupling_2026_11.en.md` and `research_tracks/fundamental_dynamics/SHARED_REALITY_INFORMATION_SELECTOR.en.md`. General pure-state QFI/Fubini–Study relation: https://www.nature.com/articles/ncomms8282. All physical claims remain C_working; no change to canonical architecture.
