<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: mm-psi-winding-dynamical-decoupling -->
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


# Gravity-only MM cannot dynamically protect full-Theta winding: exact interpolation and psi-principal gate

**2026-11-01 · C_working · restricted off-shell dynamical nonselection theorem.** This uses the full-complex-Theta sharp-norm witness in PR #826 and the EXISTING split-jet MM action, spectator-sector rank and exact shift-gauge results. No new action, no altered tetrad, no string worldsheet and no unconditional physical gauge claim. It specifically tests the claim that nonzero determinant winding MUST be a physically stable excitation.

## Existing facts, not new results

`single_theta_macdowell_mansouri_candidate.en.md` explicitly defines the chosen curvature-square gravity comparator using a 4D exterior derivative and a FIFTH CLIFFORD MATRIX Gamma_psi. This fifth generator is not automatically a derivative d_psi along the compact circle; the displayed action has no independent psi-principal part. `mm_shift_gauge_dirac.en.md` already proves exact vertical shifts in the freely varied split-jet Q chart. `mm_complex_spectator_rank.en.md` already identifies four missing imaginary-field kinetic directions. `mm_projector_kinetic_shift.en.md` and `mm_shift_potential_obstruction.en.md` already show that adding field-dependent matter terms can break the old shift redundancy. We do NOT rederive their general conclusions.

## One full complex Theta, arbitrarily many windings [PROVED, conditional]

Reuse the SAME periodic full-complex field from PR #826, now parameterized by the integer n. All components of H and X remain inside the original Mat2(C) biquaternion:

\[
\Theta_n(x,\psi)=\sigma_3+
i\left(B_n(\psi)+tI_2+x\sigma_1+y\sigma_2+z\sigma_3\right),
\quad
B_n=\begin{pmatrix}0&c_n\\c_n&b_n\end{pmatrix},
\]

For each n its smooth compact-circle coefficients are:

\[
c_n=\sqrt{1+\rho\cos(n\psi/R_\psi)},\quad
b_n=\rho\sin(n\psi/R_\psi),\quad
0<\rho<1,\quad n\in\mathbb Z.
\]

The complex central quaternion-sharp norm at the spacetime origin has exactly winding n; each endpoint is invertible on the entire compact circle:

\[
\det\Theta_n\big|_{x^\mu=0}
=\rho e^{in\psi/R_\psi},\qquad
\nu_n=\frac{1}{2\pi i}\oint_{S^1_\psi}
\frac{d\det\Theta_n}{\det\Theta_n}=n.
\]

Yet for ALL n the FOUR ORIGINAL spacetime derivatives give exactly the same regular Lorentzian tetrad and canonical sharp metric; do not project or replace them:

\[
D_\mu=\partial_\mu,\quad \mathcal N_0=1,\qquad
E_\mu[\Theta_n]=(iI_2,i\sigma_1,i\sigma_2,i\sigma_3),\quad
\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)
=\eta_{\mu\nu}I_2.
\]

## Exact interpolation: determinant singular but tetrad regular [PROVED]

Interpolate linearly between n=0 and n=1 by changing ONLY the psi-dependent original-field coefficients at fixed spacetime jet:

\[
\Theta_s=(1-s)\Theta_0+s\Theta_1,\quad 0\le s\le1,
\quad
\partial_\mu\Theta_s=\partial_\mu\Theta_0
=\partial_\mu\Theta_1,\qquad \det e_s=-1.
\]

At psi=pi Rpsi the two endpoint off-diagonal entries lie on opposite sides of 1; at the explicit intermediate s-star the determinant passes through zero:

\[
\psi=\pi R_\psi,\quad
c_0=\sqrt{1+\rho}>1,\quad
c_1=\sqrt{1-\rho}<1,\quad
s_*=\frac{c_0-1}{c_0-c_1}\in(0,1).
\]

The **same tetrad remains nonsingular** at that zero of det Theta. This shows that the LOCKED canonical tetrad and metric DO NOT THEMSELVES require det Theta nonzero. If a future microscopic action or physical configuration space prohibits det Theta=0, then the integer may label separate topological components. Without such a prohibition the two winding labels are continuously connected through perfectly regular tetrad geometry:

\[
\det\Theta_{s_*}\big|_{x^\mu=0,\,\psi=\pi R_\psi}
=-1+\bigl[(1-s_*)c_0+s_*c_1\bigr]^2=0,\qquad
\det e_{s_*}=-1.
\]

## Gravity-only MM action is blind to this interpolation [PROVED, restricted]

Use the old SELECTED-but-not-fundamental 4D MM comparator, not a new psi-extended action. Its Γpsi is an algebraic fifth Clifford generator inside the spacetime exterior-curvature connection:

\[
S_{\rm MM}[E(\Theta),\omega]
=-\frac{i\varepsilon_\psi}{g_G^2}
\int_{M_4}\mathrm{Tr}
\left(\Gamma_*\mathcal F[E,\omega]\wedge
\mathcal F[E,\omega]\right),
\quad
\mathcal A=
\tfrac14\omega^{ab}\Gamma_a\Gamma_b+
\tfrac1{2\ell}E^a\Gamma_a\Gamma_\psi.
\]

On the explicit flat defining-connection chart, with auxiliary jet K=0 and wH=0, every interpolated field has the SAME E. Keep the physical omega fixed as well. Then every geometry-only functional, including this MM candidate, has exactly the same OFF-SHELL action for all s:

\[
E[\Theta_s]=E[\Theta_0],\quad
\omega_s=\omega_0\quad\Longrightarrow\quad
S_{\rm MM}[\Theta_s,\omega_0]
=S_{\rm MM}[\Theta_0,\omega_0]
\quad\forall s\in[0,1].
\]

The entire family gives the same ψ-independent geometric response. In this specified comparison the MM integrand does NOT contain a ψ derivative, hence its *direct* ψ-principal Hessian is zero. This is true whether one evaluates the 4D action at one ψ or formally integrates copies over ψ with a fixed ψ measure. It does not establish the FULL reduced Hamiltonian after extra constraints and omitted fields:

\[
\delta_\psi\Theta=iF(\psi),\quad
\delta_\psi E_\mu=\partial_\mu(iF(\psi))=0,\quad
\delta_\psi S_{\rm MM}=0,\quad
\frac{\partial^2\mathcal L_{\rm MM}}
{\partial(\partial_\psi\Theta)^A\,
\partial(\partial_\psi\Theta)^B}=0
\quad\text{in this declared comparison}.
\]

There is an important distinction between *local vertical action degeneracy* and a global topological charge: on the invertible-Theta subset, continuous admissible paths preserve integer winding. But the original regular-tetrad configuration space allows the interpolating det Theta=0 unless extra restrictions are imposed. Moreover det Theta changes already under small vertical shifts, so its local value is not an observable of the strict geometry-only shift quotient:

\[
\delta\det\Theta=
\det\Theta\,\operatorname{tr}(\Theta^{-1}\delta\Theta),
\quad
\delta_\lambda\Theta=i\lambda\sigma_1
\Longrightarrow
\left.\partial_\lambda\det\Theta\right|_{\lambda=0}
=2c_1(\psi)\ne0
\quad(x^\mu=0).
\]

**On-shell caveat:** the explicit regular example produces a FLAT Minkowski metric. For finite ℓ, the selected MM candidate requires nonzero cosmological constant Lambda and therefore this example is NOT a stationary vacuum solution. Off-shell indistinguishability does not provide a physical excitation or existence theorem for on-shell winding branches:

\[
R_{\mu\nu}(\eta)=0,\qquad
\Lambda=3\varepsilon_\psi/\ell^2\ne0,\qquad
R_{\mu\nu}=\Lambda g_{\mu\nu}
\quad\text{is NOT satisfied by }\eta_{\mu\nu}.
\]

## What a real ψ action would have to supply [OPEN]

As a TEST ONLY, a positive quadratic psi-derivative functional could distinguish the windings, while the original MM functional cannot. Such a term is not part of the locked action and can break the prior split-jet shift symmetry; its physical Hessian, Cartan constraints and energy sign would have to be derived and checked:

\[
\mathcal E_{\psi,\mathrm{test}}
=\frac{c_\psi}{2}\int d^4x\,d\psi\,
\sqrt{-g}\;\mathcal G\!\left(
\partial_\psi\Theta,\partial_\psi\Theta
\right),
\qquad
c_\psi\ \text{NOT selected by }S_{\rm MM}.
\]

For the specific winding family, the test term sees a nonzero ψ derivative proportional to n whereas geometry-only MM sees none:

\[
\operatorname{tr}\!\left[
(\partial_\psi\Theta_n)^\dagger
\partial_\psi\Theta_n\right]_{\psi=0,\,x^\mu=0}
=\frac{\rho^2n^2}{R_\psi^2}.
\]

Do not confuse a nonzero ψ-gradient norm at a fixed background with a stable physical soliton, a positive *reduced* Hamiltonian, physical string tension or full T-duality. The prior Gaussian momentum/winding lattice in UBT was an assumed spectral model; this audit does not supply its missing worldsheet, coupling or modular invariance.

## Verification and decision [OPEN]

**16 exact SymPy tests** in `tests/test_mm_full_theta_psi_winding_decoupling.py`, added alongside the existing 71 regressions in Physics Laws CI: periodic profiles n, winding from det Theta, fixed canonical sharp tetrad, ψ-shift variation, singular interpolation with regular e, direct zero ψ-principal Hessian, nonzero MM Lambda incompatibility, conditional ψ-gradient diagnostic and full complex-Theta carrier non-nullness. **Decision:** the current gravity-only comparator cannot select or protect the topological label without additional input. Test next whether any pre-existing fundamental invariant of UBT (information principle, shared-reality constraint, or full-Theta kinetic/connection sector) yields a ψ-principal term and a precise det-Theta admissibility boundary **without arbitrarily appending a new action**. Existing sources: `research_tracks/action_selection/full_theta_sharp_norm_winding_2026_10.en.md:15-143`, `research_tracks/action_selection/single_theta_macdowell_mansouri_candidate.en.md:30-160`, `research_tracks/action_selection/mm_shift_gauge_dirac.en.md:23-47`, `research_tracks/action_selection/mm_complex_spectator_rank.en.md:23-39`, `research_tracks/action_selection/mm_shift_potential_obstruction.en.md:23-36`, `canonical/CANONICAL_DEFINITIONS.md:160-190`, `canonical/THEORY/t_duality_ubt.tex:31-90`. No physical T-duality, string, on-shell winding solution or unique action is asserted.
