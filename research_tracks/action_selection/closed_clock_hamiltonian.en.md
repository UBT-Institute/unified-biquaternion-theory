<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: closed-clock-hamiltonian.provenance -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact restricted EH comparator, not a fundamental UBT action or a CMB prediction.
UBT-AI-PROVENANCE-END -->
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

# Canonical clock Hamiltonian: closed de Sitter composite-EH comparator

**Status: PROVED UNDER EXTERNAL-ACTION ASSUMPTION; UBT dynamics OPEN.** Complements the mimetic-clock result of merged PR #684 and the closed FLRW connection of PR #685. Unlike the previously excluded minimal kinetic action, this is an explicitly **assumed Einstein–Hilbert plus cosmological constant** functional, not a curvature term derived from the unique Theta action.

## Explicit restricted action and metric

The radial Lorentz-real single-Theta coframe on the chosen Poincaré quotient is

\[
q=\sqrt{\mathcal N_0},\quad \tau=\rho/q,\quad
e^0=d\tau,\quad e^i=a\upsilon^i,\quad
\Sigma=(2I)\backslash SU(2),\quad V_\Sigma=\pi^2/60.
\]

The *external* composite metric action with usual variational boundary treatment is

\[
S_{\mathrm{comp-EH}}[\Theta,\Omega]=\frac1{16\pi G}
\int d^4x\sqrt{-g[D\Theta]}\,[R(g[D\Theta])-2\Lambda]
+S_{\mathrm{boundary}}.
\]

Substituting the homogeneous coframe and only then performing the Legendre transform gives

\[
L=C\left[-\frac{a\dot a^2}{N}+Na-\frac{\Lambda Na^3}{3}\right],
\quad N=\dot\rho/q>0,\quad C=\frac{3V_\Sigma}{8\pi G}=\frac{\pi}{160G}.
\]

## Full homogeneous clock Legendre transform

The two canonical momenta are

\[
p_a=-\frac{2Ca\dot a}{N},\quad
p_\rho=\frac Cq\left[\frac{a\dot a^2}{N^2}+a-\frac{\Lambda a^3}{3}\right].
\]

The velocity Hessian has rank one. Homogeneity in the two velocities makes the canonical Hamiltonian vanish. The exact single primary first-class constraint is

\[
\boxed{\Phi=q p_\rho+\mathcal H_g\approx0,\quad
\mathcal H_g=-\frac{p_a^2}{4Ca}-Ca+\frac{C\Lambda a^3}{3}.}
\]

The homogeneous Dirac evolution is

\[
H_{\rm canonical}=0,\quad H_{\rm total}=N\Phi,\quad
\{\Phi,\Phi\}=0,\quad\dot p_\rho=0.
\]

This is the **minisuperspace** constraint algebra, not the local ADM or full Theta--spin Dirac algebra. It leaves one canonical pair after one first-class constraint removes two phase-space dimensions.

## Conserved dust-like integration constant

Clock rho is cyclic in this EH-only comparator. Its conserved momentum produces the exact first integral and clock-gauge acceleration equation

\[
D=\frac{q p_\rho}{C}=-\frac{\mathcal H_g}{C},\quad
\boxed{\frac{\dot a^2}{N^2}+1=\frac{\Lambda a^2}{3}+\frac D a},
\quad\frac{d^2a}{d\tau^2}=\frac{\Lambda a}{3}-\frac{D}{2a^2}.
\]

Nonzero D scales in the Friedmann equation exactly like ordinary dust; its value/sign are unrestricted by this composite-clock action. Full vacuum GR requires D=0. Deparameterizing the clock yields H_phys=H_g, with negative unbounded momentum square at fixed scale a; this is not by itself a claim of a physical full-UBT ghost.

## Constructive nondegenerate stationary solution

The zero-integration-constant branch has a closed de Sitter solution

\[
\boxed{D=0,\quad H=\sqrt{\Lambda/3},\quad
a(\tau)=H^{-1}\cosh[H(\tau-\tau_c)],\quad\Lambda>0.}
\]

It obeys the complete metric vacuum Einstein equation

\[
R_{\mu\nu}=\Lambda g_{\mu\nu},\quad
G_{\mu\nu}+\Lambda g_{\mu\nu}=0,\quad R=12H^2.
\]

The already existing compatible spin/contortion representation gives

\[
\Theta=iq\tau I,\qquad
\Omega=\frac12\left(\frac{a(\tau)}{\tau}-i\right)
\sigma_j\upsilon^j,\qquad A=\Omega,\quad B=-\Omega^\dagger,\quad\tau>0.
\]

and reproduces the desired composite metric on the compact quotient

\[
D\Theta=iq\left(I\,d\tau+a\sigma_j\upsilon^j\right),\quad
ds^2=-d\tau^2+a^2\sum_j(\upsilon^j)^2.
\]

Since the independent metric Euler tensor vanishes identically on this configuration, the **full composite variation** of the supplied EH functional also vanishes by the functional chain rule for all compactly supported field variations. Thus this is on shell for the **specified composite EH candidate**, not merely a kinematic coframe. The representation is only local in positive clock time; its spin torsion is not dynamically selected by an independent Cartan equation in an EH(g) action.

## Scientific boundary

The quotient topology is selected by hand and contributes only the constant volume to the homogeneous action; the cosmology does not predict a dodecahedral observable. The EH coefficient and Lambda are assumptions, and the original kinetic-potential family is not known to induce them. No full Theta--spin constraint analysis, healthy perturbation spectrum, primordial power or Planck CMB likelihood follows. The dust constant reflects the lost independent normal Einstein constraint and confirms, rather than repairs, the warning in merged PR #684.

**References and tests:** https://doi.org/10.1007/JHEP11(2013)135 ; `tools/verify_closed_clock_hamiltonian.py` and `tests/test_closed_clock_hamiltonian.py`.
