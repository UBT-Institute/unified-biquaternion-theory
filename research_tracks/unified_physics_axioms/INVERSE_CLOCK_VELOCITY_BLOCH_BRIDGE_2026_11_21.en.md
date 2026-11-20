<!-- BILINGUAL-UNIT: inverse-clock-velocity-bloch-bridge-2026-11-21 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Standard two-spinor/SR algebra verified in the locked tetrad convention. No novel physics, dynamics, operational identity, or Einstein recovery proved.
UBT-AI-PROVENANCE-END
-->
# Reverse-engineering bridge: canonical Theta tetrad, observer clocks and Bloch relative velocity

**21 November 2026. C_working. Exact conditional kinematics, no microscopic dynamics.**
Continue the 16 Nov inverse-principles cone-match result, the 5 Nov observer-relative quantum readout, and 21 Nov PR #908 metric-vs-Fisher no-go. **These are three distinct objects**: (1) canonical Lorentz-sharp tetrad, (2) positive *geometric tangent* matrix, and (3) separately chosen operational state \(\rho_N[\Theta]\). The identity below must not turn the geometric tangent into a physical qubit detector by assertion.

## 1. Canonical geometry and the clock-whitened tangent

On a Lorentz-real nondegenerate patch of the existing canonical UBT tetrad, set
\[
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta=iX_\mu,\quad
X_\mu=X_\mu^\dagger,\quad X(v)=v^\mu X_\mu,\quad
\det X(v)=-g(v,v).
\]
The determinant identity and cone matching are **already in** \`THETA_PROJECTIVE_LORENTZ_CONE_Z2_PRINCIPLES_GATE_2026_11_16.en.md\` §5b. No new tetrad is defined here.

Choose an observer future unit timelike tangent \(u\), \(g(u,u)=-1\), and \(N=X(u)>0\) with \(\det N=1\). For a future nonzero causal tangent \(v\), define a *geometric* normalized positive matrix
\[
\boxed{\pi_u(v)=
\frac{N^{-1/2}X(v)N^{-1/2}}
{\mathrm{tr}(N^{-1}X(v))}.}\tag{1}
\]
The clock-whitened numerator is Hermitian and positive semidefinite. The denominator is strictly positive; the matrix has unit trace. For \(S\in SL_2(\mathbb C)\) acting by **simultaneous** tetrad and clock congruence, \(X'=SXS^\dagger\), \(N'=SNS^\dagger\), and \(U=N'^{-1/2}SN^{1/2}\) is unitary. Hence
\[
\boxed{\pi'_u(v)=U\pi_u(v)U^\dagger.}\tag{2}
\]
This uses the **already derived** observer-clock covariance lemma from \`THETA_OBSERVER_RELATIVE_INFORMATION_CHANNEL_2026_11.en.md\`. It is a frame-covariance statement, not a new equation of motion.

## 2. Exact velocity-Bloch identification

The determinant/trace polarization of the canonical metric gives
\[
\mathrm{tr}(N^{-1}X(v))=-2g(u,v),\qquad
\det\pi_u(v)=\frac{-g(v,v)}{4[-g(u,v)]^2}.
\]
For two future unit timelike vectors put \(\gamma=-g(u,v)\ge1\), \(\beta=\sqrt{1-\gamma^{-2}}\) (units \(c=1\)). A trace-one \(2\times2\) Hermitian matrix \(\pi=\frac12(I+\mathbf r\cdot\boldsymbol\sigma)\) satisfies \(\det\pi=(1-|\mathbf r|^2)/4\). Therefore
\[
\boxed{|\mathbf r_u(v)|=\beta,\qquad
\mathrm{spec}\pi_u(v)=\{(1+\beta)/2,(1-\beta)/2\}.}\tag{3}
\]
At \(u=v\), \(\pi=I/2\). For future null \(v\), \(\det\pi=0\), so \(\pi\) is a rank-one projector (pure *as a mathematical state*). In the inertial clock \(N=I\), \(v=\gamma(1,\boldsymbol\beta)\) gives \(\pi=(I+\boldsymbol\beta\cdot\boldsymbol\sigma)/2\).

**Scope:** this identifies a Bloch *coordinate* with SR relative 3-velocity once \(u,v\) and the already-existing Lorentz tetrad are given. It does not derive a speed limit from a detector, explain time evolution, prove that laboratory qubit purity is particle velocity, or select the canonical metric from the operational \(\Theta\) density.

## 3. Hyperbolic velocity metric versus quantum Fisher metric

Use the Bloch/velocity coordinates \(\mathbf r=\boldsymbol\beta\), \(r^2<1\) on the future unit hyperboloid. The induced positive hyperbolic (Beltrami-Klein) metric and the standard SLD quantum Fisher information metric (QFI = \(4\) Bures) on this *same abstract open ball* are
\[
h_{ij}=\frac{\delta_{ij}}{1-r^2}+\frac{r_ir_j}{(1-r^2)^2},\qquad
(F_{\mathrm{SLD}})_{ij}=\delta_{ij}+\frac{r_ir_j}{1-r^2}.
\]
Thus
\[
\boxed{h_{ij}=\gamma^2(F_{\mathrm{SLD}})_{ij},\qquad
\gamma^2=(1-r^2)^{-1}.}\tag{4}
\]
The *radial* distances are \(\mathrm{arctanh}(r)\) for SR rapidity and \(\arcsin(r)\) for QFI; they are not the same metric. This exact conformal identity is **known, not a UBT discovery**. In particular see Bharath G. Srivats, *Fisher Information as the Squared Lorentz Factor: Conformal Equivalence of the Bures and Beltrami–Klein Metrics on the Qubit Bloch Ball*, Quantum Rep. 2026, 8(3), 68, DOI: https://doi.org/10.3390/quantum8030068 . That paper proves \(ds_{\rm BK}^2=4\gamma^2ds_{\rm Bures}^2=\gamma^2ds_{\rm QFI}^2\), and explores its operational measurement interpretation. The UBT-specific work here is only to anchor the geometric velocity construction to the **locked sharp tetrad** and to enforce the distinction from the optional \(\Theta\)-state readout.

## 4. The important physical nonidentification and falsification gate

The pre-existing positive *observer readout* is
\[
\rho_N[\Theta]=
\frac{(N^{-1/2}\Theta N^{-1/2})(N^{-1/2}\Theta N^{-1/2})^\dagger}
{\mathrm{tr}[(N^{-1/2}\Theta N^{-1/2})(N^{-1/2}\Theta N^{-1/2})^\dagger]}.
\]
It is **not** \(\pi_u(v)\). On the same valid flat *kinematic* jet as the earlier PR #908 note, \(\Theta(0)=I\), \(E_\mu=i\sigma_\mu\), \(u=(1,0,0,0)\), and \(v=(5/4,3/4,0,0)\),
\[
\boxed{\rho_N[\Theta](0)=I/2,\qquad
\pi_u(v)=(I+\tfrac35\sigma_1)/2\ne I/2.}\tag{5}
\]
So the naive identification of the universal \(\Theta\) Born readout with **every tangent velocity** is explicitly false. A valid operational bridge must supply an actual *tangent-/protocol-dependent* observable/conditioning mechanism that yields \(\pi_u(v)\), without redefining the canonical \(\rho_N[\Theta]\), adding an arbitrary field, or confusing a Lorentz frame change with physical state preparation.

## 5. Next decisive inverse gates

1. **Operational soldering:** Can covariant physical detector protocols tied to the existing \(\Theta\) and its fixed tetrad yield \(\pi_u(v)\) for a specified physical tangent/transport, rather than merely using it as mathematical encoding? Show how effects transform, and whether the result descends to the physical gauge quotient.
2. **Across-point transport:** Given specified \(\Theta\) and connection dynamics, derive the curvature of clock comparisons and distinguish Thomas-Wigner kinematic holonomy from actual spacetime Riemann curvature. The algebraic cone alone selects no \(\omega[\Theta]\).
3. **Microscopic dynamics:** Derive a gauge-fixed \(\Theta\)-composite action/Hessian with healthy massless spin-2 modes. Equations (1)–(4) depend only on a tetrad and do not determine Einstein-Hilbert coefficients or \(G\).
4. **Independent test:** Include a noncommuting boost, clock variation, on-shell background and a physically calibratable observable; a mathematical QFI/BK equality is not a new UBT prediction.

**Verification status:** exact SymPy finite-matrix and conformal-identity checker \`tools/verify_inverse_clock_velocity_bloch_gate_2026_11_21.py\`. Lean / bilingual semantic review / complete CI pending. Keep C_working on draft PR #908, do not merge as an unconditional derivation.
