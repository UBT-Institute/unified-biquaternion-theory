<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: mm-winding-fisher-nonselection-20261101 -->
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

# Determinant winding is not protected by amplitude Fisher information

**2026-11-01 · C_working · restricted mathematical nonselection result.** Continuation of merged PR #826 and #827, using the ORIGINAL single full complex biquaternion field and unchanged 4D sharp tetrad. No extra string, physical probe or kinetic action is postulated.

## Exact field family and regular geometry [REUSED, PROVED]

Use the already verified n=0 to n=1 interpolation on a compact smooth internal circle. The defining 4D connection is flat in this witness. All members have the SAME regular tetrad and sharp metric; the determinant vanishes at one intermediate point:

\[
\Theta_s=\sigma_3+i\left(
\begin{pmatrix}0&c_s\\c_s&b_s\end{pmatrix}
+t I+x\sigma_1+y\sigma_2+z\sigma_3\right),\quad
c_s=(1-s)\sqrt{1+\rho}+s\sqrt{1+\rho\cos(\psi/R_\psi)},\quad
b_s=s\rho\sin(\psi/R_\psi),\quad 0<\rho<1,\ 0\le s\le1 .
\]
\[
d_s(\psi)=\det\Theta_s|_{x^\mu=0}=c_s^2-1+i b_s,\qquad
s_*={\sqrt{1+\rho}-1\over\sqrt{1+\rho}-\sqrt{1-\rho}},\qquad
d_{s_*}(\pi R_\psi)=0,\quad \det e_{s_*}=-1 .
\]


## Invariant amplitude and explicit Fisher counterexample [NEW, PROVED]

The complex determinant is the original central quaternion-sharp norm. Its absolute square is invariant under the existing SL(2,C) congruence with determinant one. As a MATHEMATICAL TEST, normalize that nonnegative amplitude on the circle and compute its classical one-coordinate Fisher functional:

\[
q_s(\psi)=|d_s(\psi)|^2,\quad
Z_s=\int_0^{2\pi R_\psi}q_s(\psi)\,d\psi>0,\quad
p_s(\psi)=q_s(\psi)/Z_s,\quad
\mathcal I_s=\int_0^{2\pi R_\psi}{(\partial_\psi p_s)^2\over p_s}\,d\psi .
\]
\[
{(\partial_\psi q_s)^2\over q_s}
={4[\operatorname{Re}(\overline{d_s}\,\partial_\psi d_s)]^2\over|d_s|^2}
\le 4|\partial_\psi d_s|^2,\qquad
\boxed{\mathcal I_s\le{4\over Z_s}\int_0^{2\pi R_\psi}|\partial_\psi d_s|^2\,d\psi<\infty}.
\]
\[
\partial_\psi d_{s_*}(\pi R_\psi)=-{i s_*\rho\over R_\psi},\qquad
\lim_{\psi\to\pi R_\psi}{(\partial_\psi q_{s_*})^2\over q_{s_*}}
={4s_*^2\rho^2\over R_\psi^2},\qquad
\mathcal I_0=\mathcal I_1=0 .
\]


The displayed bound is pointwise Cauchy–Schwarz at nonzero q. The only zero in the n=0 to n=1 interpolation occurs at the displayed intermediate configuration and is isolated. At that zero the Fisher integrand has the stated finite limit. The continuous Z_s is strictly positive on the compact interpolation, so even a uniform finite bound follows. Both endpoints have q=rho², hence identical uniform p and zero amplitude Fisher information **despite different winding**. Consequently this Lorentz-congruence-invariant amplitude/Fisher construction does not force det Theta nonzero and does not detect its phase winding.

This p is a declared illustrative probability density on internal psi, **not an independently derived physical record distribution or unique UBT information law**. Invariance under SL(2,C) alone does not settle arbitrary psi reparametrizations or the physical choice of integration measure. The counterexample applies to claims of automatic Fisher-based protection, not to every possible information principle.

## Ordinary smooth gradient versus inverse-determinant singularity [NEW, PROVED]

The same interpolation has a finite ordinary psi-gradient norm, also across det Theta=0. This Frobenius diagnostic is NOT asserted to be a Lorentz-invariant physical action:

\[
\operatorname{Tr}[(\partial_\psi\Theta_s)^\dagger\partial_\psi\Theta_s]
=2(\partial_\psi c_s)^2+(\partial_\psi b_s)^2
\le{\rho^2\over R_\psi^2}\left(1+{1\over2(1-\rho)}\right).
\]
\[
A_\Theta=\tfrac12 d\log(\det\Theta),\qquad
F_\Theta=dA_\Theta=0\quad (\det\Theta\ne0),\qquad
\exp\oint A_\Theta=(-1)^{\nu_\Theta}.
\]


On the invertible subset the previously studied determinant connection A_Theta is locally exact and its curvature vanishes. Therefore a local curvature-only Maxwell-like term in F_Theta cannot provide a bulk propagation or protect winding. By contrast an action using Theta^{-1} or |A_Theta|² may become singular at det Theta=0. Such singular protection would *presuppose* a selected inverse-field operator or restricted domain; neither is derived by the current MM or shared-reality framework. The square-root holonomy only distinguishes winding parity and is not automatically a physical charge.

## Operational shared reality and gravity-only functional [REUSED, CONSEQUENCE]

Any information/observer functional that depends ONLY on the shared composite 4D geometry g[Theta_s], its derivatives, and protocols/states independently fixed by that same geometry has identical value along the displayed interpolation. It therefore cannot rule out the determinant crossing. This statement does NOT cover observer channels or quantum states with independently established sensitivity to the full Theta determinant or its phase.

The existing MM comparator has no independent psi-principal term. The already documented SR0/SR1 observer-consistency benchmarks fail to select a unique Hamiltonian. Thus the above finite Fisher counterexample cannot be promoted into an action or a universal impossibility theorem.

## Decision and falsifiable physical gate [OPEN]

**PROVED in the declared witness:** regular 4D tetrad, different winding endpoints, isolated det Theta zero, finite invariant-amplitude Fisher functional and finite smooth psi-gradient. **NOT PROVED:** any physical winding excitation, stable sector, positive reduced Hamiltonian, spin structure, or microscopic action.

The next physical gate requires an INDEPENDENT source for both (i) admissible det Theta != 0 configurations or a dynamically divergent barrier and (ii) a well-posed psi-principal and Dirac-reduced sector. Derive observer probability channels/measure and a full-Theta covariant derivative from existing UBT premises first; test whether their action excludes the displayed smooth crossing. Do not simply declare A_Theta a physical gauge field or append a chosen singular potential.

## Reproduction and scope

Exact SymPy regression: `tests/test_mm_winding_fisher_nonselection.py`; eight local tests pass. Background and prior bounds: `research_tracks/action_selection/mm_full_theta_psi_winding_decoupling_2026_11.en.md`, `research_tracks/fundamental_dynamics/SHARED_REALITY_INFORMATION_SELECTOR.en.md`, `research_tracks/information_first/SHARED_REALITY_PRINCIPLE.md`. Numeric estimates are unnecessary for the bound. This note does not modify the canonical action, tetrad, translations, or claim tier.
