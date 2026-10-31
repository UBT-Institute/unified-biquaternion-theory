<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: theta-normal-euler-adjoint-20261031 -->
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

# Theta field variation: nonzero normal Euler formal-adjoint kernel

**2026-10-31 · C_working.** A restricted exact counter-control extending merged PR #817. All prior Palatini, split-jet, dilation and Clifford work is inherited; the exact-gradient no-go is not new. The Lorentz-real carrier X is a restricted chart, NOT the full complex Theta and not a selected fundamental component count.

## Restricted joint field/connection variation [ASSUMED]

On a regular non-null Lorentz-real patch with antisymmetric physical Lorentz connection, vary BOTH X and omega, but no independent relative dilation. The canonical metric remains the original central sharp metric on the classical slice:

\[
s=\sqrt{\mathcal N_0}>0,\quad X^2\ne0,\quad
e_\mu{}^a=s^{-1}(\partial_\mu X^a+\omega_\mu{}^a{}_bX^b),\quad
\delta e_\mu{}^a=s^{-1}(D_\mu^\omega\delta X^a+
\delta\omega_\mu{}^a{}_bX^b).
\]

For any supplied differentiable comparator S0[e,omega] write its independent densitized Euler sources E and C after integration by parts. The exact chain rule then reads:

\[
\delta S_0=\int d^4x(\mathcal E^\mu{}_a\delta e_\mu{}^a+
\mathcal C^\mu{}_{ab}\delta\omega_\mu{}^{ab}),\qquad
\mathcal E_{X,a}=-s^{-1}D_\mu^\omega\mathcal E^\mu{}_a,
\]

The omega equation also contains the composite tetrad response, not just C:

\[
\delta_\omega S_0[e(X,\omega),\omega]
=\int d^4x\,\Bigl(
\mathcal C^\mu{}_{ab}\delta\omega_\mu{}^{ab}
+s^{-1}\mathcal E^\mu{}_a
\delta\omega_\mu{}^a{}_bX^b\Bigr).
\]

## Exact formal-adjoint normal kernel [PROVED, restricted]

For a smooth density h and V the spacetime image of X, the following nonzero normal Euler test source is invisible to every antisymmetric Lorentz variation:

\[
V^\mu=e^\mu{}_aX^a,\quad
\mathcal E^\mu{}_a=hV^\mu X_a,\quad
\mathcal E^\mu{}_a\delta\omega_\mu{}^a{}_bX^b=0.
\]

The composite defining relation gives D_mu X_a=s e_mu a and V^mu e_mu a=X_a. Therefore its field variation vanishes whenever h solves the local transport equation:

\[
D_\mu^\omega(hV^\mu X_a)
=\bigl(\partial_\mu(hV^\mu)+sh\bigr)X_a,
\qquad
V^\mu\partial_\mu h+(\partial_\mu V^\mu+s)h=0.
\]

A regular non-null X gives nonzero V. Nonzero smooth initial density h on a local transverse three-dimensional hypersurface yields nonzero local solutions. Consequently BOTH adjoint variation channels can vanish while E is nonzero. This is an obstruction in the unrestricted *Euler-source test space*, not an on-shell theorem for the still-unselected UBT action.

## Exact timelike witness from a sourced functional [PROVED, restricted]

On the future timelike flat patch choose the following regular original-field composite background and nonzero homogeneous density:

\[
\eta=\operatorname{diag}(-1,1,1,1),\quad
s=1,\quad \omega=0,\quad X^a=x^a,\quad
e_\mu{}^a=\delta_\mu{}^a,\quad
\rho=t^2-x^2-y^2-z^2>0,\quad t>0,
\]

The full vector-valued divergence cancels exactly, with no use of field equations:

\[
h=\rho^{-5/2},\quad
\mathcal E^\mu{}_a=h x^\mu x_a,\quad
x^\mu\partial_\mu h=-5h,\quad
\partial_\mu\mathcal E^\mu{}_a=0,\quad
\mathcal E^\mu{}_a\ne0.
\]

To show that E really is a symmetric metric Euler covector, take the explicitly prescribed external source H and fiducial flat metric, held FIXED when varying e:

\[
H^{\mu\nu}=\tfrac12h x^\mu x^\nu,\quad
S_H[e]=\int_{\mathcal U}d^4x\,H^{\mu\nu}(x)
\bigl(e_\mu{}^ae_\nu{}^b\eta_{ab}-\eta_{\mu\nu}\bigr).
\]

At the stated background, independent tetrad variation gives nonzero E; both compactly supported composite variations vanish:

\[
\left.\frac{\delta S_H}{\delta e_\mu{}^a}\right|_{e=I}
=2H^{\mu\nu}\eta_{\nu a}=\mathcal E^\mu{}_a\ne0,\quad
\delta_X S_H[e(X,\omega)]=0,\quad
\delta_\omega S_H[e(X,\omega)]=0.
\]

**Critical limitation:** H and the background are EXTERNAL, fixed data. S_H is not a diffeomorphism/gauge-selected microscopic UBT action, nor does this example exhibit a physical solution or Einstein failure. Its role is to certify a genuine nonzero cokernel of the differential variation map.

## Noether identity and the remaining full-theory gate [OPEN]

For an independently diffeomorphism-invariant pure-metric action on a torsion-free compatible branch, the familiar Bianchi/Noether identity gives an even stronger redundancy of X variation (with densitized metric Euler H):

\[
\mathcal E^\mu{}_a=2\sqrt{|g|}\,H^{\mu\nu}e_{\nu a}
\quad\Longrightarrow\quad
D_\mu^\omega\mathcal E^\mu{}_a
=2\sqrt{|g|}\,(\nabla_\mu^{\mathrm{LC}}H^{\mu\nu})e_{\nu a}
\quad(T=0).
\]

Here the metric Noether identity makes the X Euler equation a differential identity rather than an independent normal equation. The torsion-free generated-tetrad branch is itself subject to the earlier concurrent-vector obstruction; the identity is standard geometry, not new UBT physics. Source currents and torsionful density conventions require separate work.

**Next decisive calculation:** identify the actual admissible Euler sources and full variation bundle of ONE selected complex-Theta action, including the independent fixed-tetrad Cartan derivative, relative two-sided jet, all Clifford grades, boundary data and constraint quotient. Test whether that admissible source set intersects this nonzero normal transport kernel. Do not assume any arbitrary E comes from UBT.

**Exact verifier:** `tests/test_theta_normal_euler_adjoint_kernel.py` (11/11 local SymPy tests). **Prior-work baseline:** `research_tracks/action_selection/composite_lorentz_variation_rank_2026_10.en.md`; `research_tracks/action_selection/physics_closure_action_family_2026_10.en.md`; `research_tracks/action_selection/splitjet_spatial_dirac_2026_10.en.md`; `canonical/ACTION.en.md`. No Lean or independent bilingual semantic approval is claimed.
