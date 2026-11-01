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

## Reference amplitude is not dynamically selected [PROVED]

The same winding n and the same original Theta produce continuously different QFI whenever the independently chosen reference amplitude changes. This exact modulation is bounded by unity and tends to zero for a vanishing or dominating reference:

\[
x=\frac a\rho>0,\qquad
F_Q[d_n;a]=\frac{n^2}{R_\psi^2}
\frac{4x^2}{(1+x^2)^2},\quad
0<\frac{4x^2}{(1+x^2)^2}\le1,
\quad
1-\frac{4x^2}{(1+x^2)^2}
=\frac{(x^2-1)^2}{(1+x^2)^2},
\quad
\lim_{x\to0,\infty}\frac{4x^2}{(1+x^2)^2}=0.
\]


The equality at x=1 is the optimally balanced *chosen readout*, not a unique Theta prediction. Thus neither the winding integer nor the canonical sharp geometry fixes the numerical QFI of an unspecified observer channel.

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

## Exact full-Theta radial unwinding and second-variation test [PROVED, CONDITIONAL]

A stronger test examines whether **postulating** the phase-sensitive QFI integral as a positive psi-gradient energy could make winding dynamically stable. Use the same original FULL complex biquaternion and flat defining 4D connection as in PR #827, with no new tetrad or auxiliary worldsheet:

\[
0<\rho<1,\quad n\in\mathbb Z\setminus\{0\},\quad
r_s=(1-s)\rho,\ 0\le s\le1,\quad
c_s=\sqrt{1+r_s\cos(n\psi/R_\psi)},\quad
b_s=r_s\sin(n\psi/R_\psi),
\]
\[
\Theta_{n,s}=\sigma_3+
i\left[\begin{pmatrix}0&c_s\\c_s&b_s\end{pmatrix}
+t I+x\sigma_1+y\sigma_2+z\sigma_3\right],\qquad
\det\Theta_{n,s}|_{x^\mu=0}=r_s e^{in\psi/R_\psi}.
\]
\[
E_\mu=\partial_\mu\Theta_{n,s}
=(iI,i\sigma_1,i\sigma_2,i\sigma_3),\quad
g_{\mu\nu}=\eta_{\mu\nu},\quad
X_{n,s}^2=c_s^2>0 .
\]


For every s<1, det Theta is nonzero along the entire internal circle, its integer winding remains n, and the same full original sharp tetrad and flat Lorentz metric survive. At s=1 the determinant vanishes, yet the original carrier X remains spacelike non-null and the tetrad is regular. The fields are smooth because 1+r_s cos(...) remains positive for rho<1.

The QFI functional for the **chosen** hypothetical reference readout has an exact radial value:

\[
\mathcal J_Q[r]=\int_0^{2\pi R_\psi}
\frac{4a^2|\partial_\psi d|^2}{(a^2+|d|^2)^2}\,d\psi
=\frac{2\pi n^2}{R_\psi}\frac{4a^2r^2}{(a^2+r^2)^2},
\]
\[
a=\rho,\qquad
\frac{\mathcal J_Q[r_s]}{\mathcal J_Q[\rho]}
=\frac{4(1-s)^2}{(1+(1-s)^2)^2}
=1-s^2+O(s^3),\qquad
\lim_{s\to1^-}\mathcal J_Q[r_s]=0,
\]
\[
\left.\frac{d^2\mathcal J_Q}{dr^2}\right|_{r=a}
=-\frac{4\pi n^2}{R_\psi a^2}<0 .
\]


For any fixed n!=0 and fixed a>0 the infimum of J_Q on the **nonzero-determinant winding-n subset** is already zero (take r>0 toward zero). Hence even imposing det Theta != 0 does not supply a positive winding-dependent lower bound from this functional. With the balanced reference a=rho, the nominal r=a winding is a stationary *maximum in the uniform radial direction*, not a stable energy minimum. The displayed negative second derivative is an explicit instability direction for this **hypothetical** energy, not a physical UBT instability theorem.

A direct variation treating z and its conjugate as independent real variations gives the projective sigma-model Euler equation:

\[
\mathcal L_Q=\frac{4a^2z'\bar z'}{(a^2+z\bar z)^2},\qquad
z''-\frac{2\bar z(z')^2}{a^2+|z|^2}=0 ,
\]
\[
z(\psi)=r e^{in\psi/R_\psi}
\quad\Longrightarrow\quad
z''-\frac{2\bar z(z')^2}{a^2+|z|^2}
=\frac{n^2}{R_\psi^2}z\,
\frac{r^2-a^2}{r^2+a^2}.
\]


The constant-radius winding is stationary for nonzero n only at r=a, and that point has the negative radial second variation. It therefore cannot be promoted to a protected physical solution by merely calling the reference-sensitive QFI an action. Neither a lower-dimensional sigma-model kinetic functional nor a new Hamiltonian has been derived from the locked single-Theta action.

**Scope:** this is a no-positive-winding-floor and negative-mode theorem for the explicitly chosen 1D QFI test functional on the exhibited full-Theta family. It does not exclude other independently derived invariants, full constraints, nonlocal terms or physical phase-sensitive sectors.

## Physical selection and shared-reality verdict [OPEN]

The old amplitude-only classical Fisher functional gives zero at both winding endpoints; this phase-sensitive *reference-dependent* QFI instead scales with n². Neither one derives a microscopic field action, imposes det Theta nonzero, supplies Cartan/Dirac constraints, or proves stable excitations. The full-Theta gravity-only MM comparator remains blind to the winding interpolation. Even postulating J_Q as a cost leaves the singular crossing finite and adds an unselected readout and coefficient.

The physical gate is to **derive rather than assume** a Theta-native observer algebra and measurement channel, the physical meaning/measure of psi, a phase reference (if any), and the composite covariant psi principal sector. Require its own constrained Hamiltonian and variational equations before asserting a winding particle or a new physical effect. Independent physical verification remains open.

## Verification and prior sources

Exact SymPy checks: `tests/test_mm_phase_qfi_reference_gate.py` (eight local tests; expanded radial tests pending). Reuses `research_tracks/action_selection/mm_winding_fisher_nonselection_2026_11.en.md`, `research_tracks/action_selection/mm_full_theta_psi_winding_decoupling_2026_11.en.md` and `research_tracks/fundamental_dynamics/SHARED_REALITY_INFORMATION_SELECTOR.en.md`. General pure-state QFI/Fubini–Study relation: https://www.nature.com/articles/ncomms8282. All physical claims remain C_working; no change to canonical architecture.
