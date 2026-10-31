<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: dynamics-reuse-H-MM-adjoint -->
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


# Reuse audit and derived-H MM adjoint gate

**2026-10-31 · C_working.** Existing conditional Einstein dynamics are NOT microscopic action selection. This note connects the existing results and adds one scoped variation theorem.

## Existing proven work — no rederivation

Central sharp metric and full Clifford lift are fixed. Palatini–Holst, its independent split-jet variation, the MM curvature-square candidate and reduced ADM tensor waves exist as CONDITIONAL gravity. First-jet volume, matched bare kinetic, pure-gradient and pure common torsion-free connection models have scoped no-go results. MM presymplectic reduction is partial, and its gravity-only version has spectator complex-Theta sectors. The locked kinematic axioms do not fix the Einstein–Hilbert coefficient: one action-selection principle is still missing.

## Declared conditional comparison [ASSUMED]

Use H and X already inside the SAME original Theta, with determinant-derived w, not a new scalar:

\[
\Theta=H+X,\quad H^\ddagger=H,\quad X^\ddagger=-X,\quad
q=X^aX_a\ne0,\quad\det H>0,\quad
w_\mu=-\tfrac12\partial_\mu\ln\det H.
\]

**Keep TWO roles distinct:** the defining Lorentz jet connection varpi preserves normalized H, while the physical Lorentz connection omega entering S_geom is independently varied. An algebraic split-jet K_J acts separately on X. This is a real-linear comparator, NOT a derived unrestricted complex-linear two-sided Theta connection. Relative to the older freely variable split-jet coordinate K_old, the equivalent auxiliary coordinate is K_J=K_old+omega-varpi; its unrestricted algebraic variation is unchanged:

\[
e_\mu{}^a=s^{-1}(\partial_\mu X^a+
(\varpi_\mu{}^a{}_b+K_{J\mu}{}^a{}_b)X^b+w_\mu X^a),
\quad s=\sqrt{\mathcal N_0}>0,\quad\det e\ne0.
\]

Let a chosen geometric gravity-only functional depend on auxiliary K_J and Theta only through e. Keep the complete fixed-tetrad Cartan source C in the variation:

\[
S_{\rm pull}=S_{\rm geom}[e(X,H,K_J,\varpi),\omega],\qquad
\delta S_{\rm geom}=\int d^4x\,
(\mathcal P^\mu{}_a\delta e_\mu{}^a+
\mathcal C^\mu{}_{ab}\delta\omega_\mu{}^{ab}).
\]

## Conditional formal-adjoint injectivity [PROVED]

Variations of the independent antisymmetric K_J imply that the tetrad Euler covector is normal to X for each spacetime index:

\[
\mathcal P^\mu{}_a\delta K_{J\mu}{}^a{}_bX^b=0
\ \forall\delta K_J
\quad\Longrightarrow\quad
\mathcal P^\mu{}_a=f^\mu X_a.
\]

The independent field-X equation and an integration by parts force the remaining normal coefficient f into the direction V. This uses the invertible e and full X variations, not only an algebraic jet rank:

\[
0=\mathcal E_{X,a}=s^{-1}[
(-\partial_\mu f^\mu+2w_\mu f^\mu)X_a
-sf^\mu e_{\mu a}]
\quad\Longrightarrow\quad f^\mu=hV^\mu,\quad V^\mu=e^\mu{}_aX^a.
\]

Simultaneously rescale the EXISTING H and X by a compactly supported real epsilon. The determinant-derived w cancels all derivatives of epsilon while preserving the H reality constraint:

\[
\delta X=\varepsilon X,\quad\delta H=\varepsilon H,\quad
\delta w_\mu=-\partial_\mu\varepsilon
\quad\Longrightarrow\quad
\delta e_\mu{}^a=\varepsilon e_\mu{}^a.
\]

Stationarity of that same gravity functional eliminates the final normal Euler component because X is non-null. The induced physical omega contribution then vanishes and the usual fixed-e Cartan equation remains:

\[
0=\delta_\varepsilon S_{\rm pull}
=\int d^4x\,\varepsilon hX^2
\quad\Longrightarrow\quad h=0,\quad\mathcal P=0.
\]

This is a LOCAL theorem for a SPECIFIED variation space. It does not select the microscopic action, include direct H-dependent matter terms, or prove physical stability. The differential X equation is essential: K_J plus one Weyl tangent is NOT pointwise surjective.

**Physical-versus-defining spin warning:** if varpi is identified with torsion-free physical Levi-Civita omega, the positive normalized H supplies a covariantly constant timelike internal vector. Its spacetime image n is Levi-Civita parallel and obeys Ric(n)=0; a nonzero-Lambda Einstein vacuum cannot then occur. Thus even when the adjoint theorem transmits the gravitational equations, imposing varpi=omega can exclude generic solutions. The conditional Einstein–Lambda branch needs the physical/jet separation, not a common spin identification.

\[
D^\varpi_\mu\widehat H=0,\quad
\varpi=\mathring\omega(e),\quad
\widehat H>0
\ \Longrightarrow\
\nabla^{\mathrm{LC}}_\mu n^\nu=0
\ \Longrightarrow\
R_{\mu\nu}n^\nu=0,\quad
R_{\mu\nu}=\Lambda g_{\mu\nu},\ \Lambda\ne0
\ \Longrightarrow\ n=0.
\]

## Same-connection obstruction [PROVED]

The K_J map cannot be casually identified with one SL-complex spin acting on both H and X. At H identity and X imaginary identity, the H reality constraint removes precisely the boost variations needed by K_J:

\[
H=I_2,\quad X=iI_2,\quad
\delta C_H=\delta K+\delta K^\ddagger,\quad
\delta E_X=i(\delta K+\delta K^\ddagger),\quad
\delta C_H=0\Longrightarrow\delta E_X=0.
\]

A K_J acting on only the anti-Hermitian sector employs a projector which is not complex linear on full Theta. The simultaneous K_J and Weyl pointwise rank is less than that of an unrestricted tetrad; full injectivity depends on the X differential equation:

\[
P_-(\Theta)=\tfrac12(\Theta-\Theta^\ddagger),\quad
P_-(i\Theta)\ne iP_-(\Theta),\quad
\operatorname{rank}(\delta K_J,\varepsilon\mapsto\delta e)=13<16.
\]

## Decision and verification [OPEN]

**15/15 local exact SymPy tests passed** in `tests/test_theta_hermitian_mm_adjoint_closure.py`. The sole next theorem gate is to derive or falsify an equivariant full-Theta two-sided/graded auxiliary connection supporting K_J without violating the H reality, canonical sharp metric, complex phase/time and action constraints. Without it this remains a conditional MM gravity proof, not a completed UBT. The competing induced-gravity route remains a distinct origin programme.

## Source ledger

- `canonical/CANONICAL_DEFINITIONS.md:130-201`
- `canonical/geometry/biquaternion_dirac_lift.tex:31-140`
- `research_tracks/action_selection/unconditional_gr_action_decision.en.md:19-53`
- `research_tracks/action_selection/theta_first_jet_gravity_no_go.en.md:19-126`
- `research_tracks/action_selection/physics_closure_bare_action_2026_10.en.md:21-85`
- `research_tracks/action_selection/split_jet_palatii_variational_lift.en.md:78-160`
- `research_tracks/action_selection/single_theta_macdowell_mansouri_candidate.en.md:30-253`
- `research_tracks/action_selection/full_spatial_dynamics_2026_10.en.md:25-160`
- `research_tracks/action_selection/mm_composite_presymplectic_variation.en.md:17-52`
- `research_tracks/action_selection/mm_complex_spectator_rank.en.md:17-39`
- `research_tracks/action_selection/lorentz_slice_two_sided_connection_classification.en.md:17-40`
- `research_tracks/action_selection/full_theta_hermitian_compensator_2026_10.en.md:19-159`
- `research_tracks/action_selection/theta_normal_adjoint_kernel_2026_10.en.md:19-165`
- `research_tracks/action_selection/biquaternionic_induced_gravity_boundary.en.md:19-455`
