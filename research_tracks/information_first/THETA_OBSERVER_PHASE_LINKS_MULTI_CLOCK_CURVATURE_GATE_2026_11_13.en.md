<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional local information-geometry results, not a physical QED photon or fundamental quantum action.
UBT-AI-PROVENANCE-END
-->

# Theta observer phase links: local density blindness, three-clock recovery, spin transport, and linear-photon gate

**2026-11-13. C_working; exact scoped algebra, microscopic physics OPEN.**
Continue the revised programme Theta -> quantum/observer -> QED+GR -> Maxwell/Standard Model. Earlier direct classical electromagnetic projections are controls, NOT proof of fundamental Maxwell dynamics.

## 1. Full Theta and observer readout

Use one original complex biquaternion represented faithfully as a 2x2 complex matrix. The earlier observer protocol (research_tracks/information_first/THETA_OBSERVER_RELATIVE_INFORMATION_CHANNEL_2026_11.en.md) chooses positive Hermitian unit-determinant clock N:
\[
T_N=N^{-1/2}\Theta N^{-1/2},\quad
t_N=T_N/\sqrt{\operatorname{tr}(T_N^\dagger T_N)},\quad
\rho_N=t_Nt_N^\dagger.
\]
These are readout candidates, NOT additional physical fields or a proof of Born dynamics. The canonical gravity metric remains the central-sharp anticommutator of E_mu=N0^-1/2 D_mu Theta on the real Lorentz tetrad slice. No change to that axiom is proposed.

One observer has only three generic real readout directions out of the full eight of Theta. In particular rho_N[e^{i alpha}Theta]=rho_N[Theta].

## 2. The local phase connection is not determined by ONE observer density

In a fixed single comparison frame (spin connection Gamma=0 as an explicitly limited toy), define for the normalized full amplitude
\[
a=-i\,\operatorname{tr}(t^\dagger dt),\quad
f=da=-i\,\operatorname{tr}(dt^\dagger\wedge dt).
\]
Normalization makes a real; under a local central scalar phase t'=exp(i alpha)t it becomes a'=a+d alpha, f'=f. These are standard Berry-geometry properties, not a claim of photon dynamics or UBT microscopic gauge invariance.

Take 0<p(x)<1:
\[
t_0=\operatorname{diag}(\sqrt{1-p},\sqrt{p}),\qquad
t_1=\operatorname{diag}(\sqrt{1-p},\sqrt p\,e^{iy/L}).
\]
Both have EXACTLY the same rho=diag(1-p,p) for the N=I observer, but
\[
a_0=0,\quad f_0=0,\quad
a_1=(p/L)dy,\quad f_1=(p'(x)/L)dx\wedge dy.
\]
Choosing p=1/2+B L x on a local domain yields constant nonzero f_1=B dx wedge dy while rho is unchanged. Hence no functional of ONE observer's pointwise rho alone fixes this particular phase curvature. The two Theta configurations are not claimed to satisfy the full canonical real-tetrad constraint or Euler-Lagrange equations.

A generic right-unitary t->tV(x) likewise preserves rho but can change f. Right U(2) is an information-kernel direction of ONE protocol, NOT automatically a physical gauge group: if it were a true redundancy, f would fail the physical gauge-invariance gate.

## 3. A positive conditional result from the old three-clock theorem

The existing multi-clock result states that for three specified complete, co-calibrated noncommuting observer-clock density readouts, identical records for two invertible smooth Theta fields imply Phi(x)=c(x)Theta(x), with c(x) a smooth nonzero complex scalar. For the same fixed N reference and smooth comparison frame,
\[
t_\Phi=e^{i\arg c}t_\Theta,\quad
a_\Phi=a_\Theta+d\arg c,\quad
\boxed{f_\Phi=f_\Theta}.
\]
Therefore the chosen f is a *conditional projectively identifiable functional of complete three-clock histories*, unlike one-clock rho. It still requires a selected across-point frame transport and physically admissible measurements. As an explicit witness, N=I cannot distinguish t0 from t1 of section 2, but the positive non-diagonal clock N=[[5/4,3/4],[3/4,5/4]] (det=1) gives distinguishable densities for p=1/4 and relative phase pi/2. This was verified exactly.

The result does not by itself mean multiple observers create electromagnetism. It means that relative quantum phases may be operationally accessible through joint calibrated data.

## 4. Exact four-point gauge-invariant loop

For normalized matrices t(p,phi)=diag(sqrt(1-p),sqrt(p) exp(i phi)), use four points (p0,phi0)=(1/4,0), (p1,phi0)=(3/4,0), (p1,phi1)=(3/4,pi/2), (p0,phi1)=(1/4,pi/2). Set overlap L_ij=tr(t_i^\dagger t_j), and Bargmann/Pancharatnam product W=L_01 L_12 L_23 L_30. Exact algebra gives
\[
\boxed{W=9/32+3i/8,\quad \arg W=\arctan(4/3)\ne0}.
\]
Each t_i -> exp(i alpha_i)t_i changes individual overlaps, but all local central phases cancel in W. Infinitesimally arg W approximates the flux integral of f, with fixed orientation. For a finite rectangle, arg W need not equal the continuous flux exactly. This assumes the *same* spin/frame comparison at all vertices, so local Lorentz covariance requires the next step.

## 5. Correct local Lorentz/spin comparison: no fake phase from rotating the basis

The prior clock-covariance identity makes the normalized matrix transform at each point as
t'=U t U^\dagger, with U in SU(2) induced by a proper Lorentz transformation and the observer clock. Let Gamma be a **chosen**, as yet not dynamically derived, su(2)-valued comparison connection:
\[
\mathscr D t=dt+[\Gamma,t],\qquad
\Gamma'=U\Gamma U^\dagger-dU U^\dagger.
\]
Then \(\mathscr D' t'=U(\mathscr Dt)U^\dagger\) and
\[
a_\Gamma=-i\,\operatorname{tr}(t^\dagger\mathscr Dt)
\]
is local spin-frame invariant and transforms as a_\Gamma -> a_\Gamma+d alpha under an additional central phase. Its curvature da_\Gamma is independent of these *specified* gauge changes. This does NOT fix Gamma from the microscopic Theta theory.

Explicit fake-phase diagnostic: choose constant rank-one t0=[[0,1],[0,0]], U(chi)=diag(exp(i chi),exp(-i chi)). The rotated t'=exp(2i chi)t0 has naïve a_raw=2 dchi. With the correct spin connection Gamma'=-dU U^\dagger, however \(\mathscr D' t'=0\), so the corrected a_Gamma'=0. A rotating local tetrad frame must not be confused with an electromagnetic phase.

## 6. Fundamental warning: the simple Berry curvature does not produce a linear photon around a constant background

If t(x)=t_*+epsilon u(x)+O(epsilon^2) with constant normalized t_*, then dt=O(epsilon), hence
\[
\boxed{f=-i\,\operatorname{tr}(dt^\dagger\wedge dt)=O(epsilon^2)}.
\]
It cannot be a linearly propagating free electromagnetic field strength around that background by itself (assuming fixed trivial spin transport).

Full-rank exact sample near t_*=I/sqrt(2):
\[
t_\epsilon=\operatorname{diag}(1+\epsilon x,1+i\epsilon y)/\sqrt{D},\quad
D=(1+\epsilon x)^2+1+\epsilon^2y^2,
\]
\[
a=\frac{\epsilon}{D}dy,\quad
f=-\frac{2\epsilon^2(1+\epsilon x)}{D^2}dx\wedge dy,\quad
\partial_\epsilon f|_{\epsilon=0}=0.
\]
A nonconstant physical background, dynamical composite connection with first-order curvature, or collective quantum gauge degrees might avoid this restriction, but must be derived.

## 7. Priority: the Theta -> quantum -> QED and gravity bridge

1. Reconstruct the physically selected *inter-point* quantum transport, compatible with the canonical Theta-derived Lorentz tetrad, without silently choosing a new field Gamma.
2. Derive the relevant gauge equivalence from the complete single-Theta constrained symplectic/quantum phase space; distinguish unmeasurable one-clock directions from actual gauge redundancy.
3. Analyze the linearized physical reduced Hessian and constraint algebra around an on-shell background; show two massless helicity-one modes, positive energy, conserved charge, gauge/Ward constraints and a legitimate QED effective action from a single Theta system.
4. Recover the familiar classical Maxwell limit on the same derived geometry, with the GR and Standard Model branches checked separately.
5. Integrate information, observer capacity and relative entropy quantitatively; do not claim they uniquely select H, since earlier counterexamples already refuted that proposition.

**Verification:** five exact SymPy checks passed locally in the active session: same rho vs different f, nonzero invariant four-point loop, a second clock resolving hidden relative phase, cancellation of fake local SU(2) phase, and vanishing first variation of f around a constant full-rank background. Focused regression: tests/test_theta_observer_phase_link_gate.py. No claim of CI, a physical photon, or solved UBT dynamics.
