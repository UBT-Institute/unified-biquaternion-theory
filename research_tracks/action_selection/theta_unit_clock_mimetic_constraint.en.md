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

# Unit-clock constraint and dust integration constant in the UBT timelike branch

**Status: conditional variational theorem and explicit counterexample; NOT a derivation of fundamental UBT dynamics.**

This article extends the strictly stated timelike auxiliary connection branch of Proposition 9 in `canonical_family_hamiltonian_bridge.en.md`. The earlier exact collapse of the bare kinetic term to a volume term remains valid. Here we test what happens *if* a separate Einstein-Hilbert infrared functional is proposed as a diagnostic. That functional is not assumed to have been derived microscopically from Theta. The dust mechanism is related to the previously published mimetic-gravity literature (Chamseddine and Mukhanov, JHEP 2013 135, doi:10.1007/JHEP11(2013)135); we do NOT claim invention of mimetic gravity.

## 1. Exact kinematic unit-clock identity

Assume a positive-Hermitian Lorentz-real patch with gauge-fixed (X=iho I), (ho>0), independent boost one-forms (b^i), and constant (N_0>0). The composite coframe is:

\[
e^0_\mu=\frac{\partial_\mu\rho}{\sqrt{N_0}},\qquad
e^i_\mu=\frac{\rho}{\sqrt{N_0}}b^i_\mu,\qquad
g_{\mu\nu}=-e^0_\mu e^0_\nu+\sum_{i=1}^3e^i_\mu e^i_\nu.
\]

**Proposition A.** On every patch where the coframe is invertible, its metric automatically obeys the unit-gradient identity:

\[
n_\mu:=e^0_\mu,\qquad
g^{\mu\nu}\partial_\mu\rho\,\partial_\nu\rho=-N_0,\qquad
n^\mu n_\mu=-1.
\]

**Proof.** In the coframe basis, (n=e^0) has squared norm (-1). Thus the gradient of (ho) is a fixed-norm timelike covector. It is not a freely variable lapse. This is *kinematic*; its dynamical consistency as a full-Theta branch is still unestablished.

## 2. Exactly which metric field equation is lost

Let (S_g[g,ho]) be an arbitrary differentiable local metric-scalar functional evaluated on this composite coframe. The independent-metric first-variation convention is:

\[
\delta S_g=\int d^4x\,\sqrt{-g}\,
\left(\mathcal E^{\mu\nu}\delta g_{\mu\nu}
+\mathcal J\,\delta\rho\right),
\quad
\mathcal E^{\mu\nu}:=\frac{1}{\sqrt{-g}}
\left.\frac{\delta S_g}{\delta g_{\mu\nu}}\right|_\rho,\quad
\mathcal J:=\frac{1}{\sqrt{-g}}
\left.\frac{\delta S_g}{\delta\rho}\right|_g .
\]

**Proposition B (projection lemma).** Varying all independent (b^i_mu) while holding (ho) fixed yields

\[
\frac{\delta S_g}{\delta b^i_\mu}
=2\sqrt{-g}\,\frac{\rho}{\sqrt{N_0}}\,
\mathcal E^{\mu\nu}e^i_\nu=0
\quad\Longrightarrow\quad
\boxed{\mathcal E^{\mu\nu}=\lambda n^\mu n^\nu.}
\]

**Proof.** The variations are (delta_b e^0=0) and (delta_b e^i_mu=(ho/sqrt{N_0})delta b^i_mu). Since the three spatial coframe covectors (e^i) are linearly independent, the symmetric tensor (mathcal E^{mu
u}) can annihilate all three covectors only if both indices lie in their one-dimensional annihilator, spanned by (n^mu). Thus its remaining component is (lambda n^mu n^
u), not necessarily zero.

**Proposition C (clock equation).** Varying (ho) next, and imposing the (b) equations only *after* the variation, yields

\[
\delta_\rho e^0_\mu=\frac{\partial_\mu\delta\rho}{\sqrt{N_0}},
\qquad
\delta_\rho e^i_\mu=\frac{b^i_\mu}{\sqrt{N_0}}\delta\rho,
\qquad
\boxed{\mathcal J-\frac{2}{\sqrt{N_0}}
\nabla_\mu(\lambda n^\mu)=0.}
\]

**Proof.** The spatial-coframe contribution proportional to (b^i_mudeltaho) vanishes on the (b) equations. The temporal variation contributes (-2sqrt{-g}mathcal E^{mu
u}e^0_
u,partial_mudeltaho/sqrt{N_0}=2sqrt{-g}lambda n^mupartial_mudeltaho/sqrt{N_0}). Integrating by parts produces the displayed conservation/source equation (boundary variations vanish). No independent equation enforces (lambda=0).

## 3. Explicit EH diagnostic and vacuum counterexample

For a separately **assumed**, not derived, curvature functional with (M^2>0),

\[
S_{\rm EH}=\frac{M^2}{2}\int d^4x\,\sqrt{-g}\,R,
\qquad
\mathcal E^{\mu\nu}=-\frac{M^2}{2}G^{\mu\nu},
\qquad\mathcal J=0,
\]

Propositions B and C reduce to a pressureless-dust integration constant:

\[
\boxed{G^{\mu\nu}=\varepsilon n^\mu n^\nu,\qquad
\nabla_\mu(\varepsilon n^\mu)=0,\qquad
\varepsilon=-\frac{2\lambda}{M^2}.}
\]

**Concrete non-GR-vacuum stationary solution (local).** Choose

\[
N_0=1,\quad \rho=t>0,\quad a(t)=t^{2/3},\qquad
e^0=dt,\quad e^i=a(t)\,dx^i,\quad
b^i=\frac{a(t)}{t}\,dx^i.
\]

The composite metric and its Einstein tensor are exactly

\[
g=-dt^2+t^{4/3}(dx^2+dy^2+dz^2),\quad
G_{00}=\frac{4}{3t^2},\quad G_{ij}=0,\quad
\lambda=-\frac{2M^2}{3t^2},\quad
\partial_t(a^3\lambda)=0.
\]

The coframe determinant is nonzero for (t>0); the projected spatial metric equations vanish, and the clock current is conserved. Nevertheless (G_{00}
e0). This exhibits a genuine solution of the restricted Einstein-Hilbert variational system that is **not** an Einstein vacuum solution. It must not be marketed as a UBT dark-matter prediction. The known mimetic-gravity analogy is used as a warning about the missing lapse/Hamiltonian equation, not a new phenomenological fit.

## 4. Necessary closure test and honest limits

\[
\boxed{\text{GR vacuum requires }\lambda=0;
\quad \text{the restricted equations do not impose }\lambda=0.}
\]

To recover ordinary Einstein vacuum equations from such a reduced metric variation, the full fundamental dynamics must independently impose the residual normal projection or an equivalent initial-value condition (lambda=0). For (mathcal J=0), the clock conservation law propagates initial (lambda=0) along the noncaustic normal flow, but it does not select that condition. If the full UBT theory varies extra composite connections, reality constraints, torsion or other sectors, these can change the result; no full Dirac algebra is derived here.

**Specific priority:** derive the *normal Einstein constraint* from the complete unfixed Theta action before claiming that an imposed Einstein-Hilbert term is sufficient to reproduce GR. This is a new explicit diagnostic for the existing GR-closure track, not a second fundamental action.
