<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: full-clifford-torsion-square -->
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

# Full Clifford torsion and squared Dirac operator: exact scoped audit

**2026-10-31 · C_working · restricted mathematical comparator.** Build on the existing `canonical/geometry/biquaternion_dirac_lift.tex` and the established full-geometric-algebra research track. Trace/axial/tensor decomposition is *known Einstein–Cartan algebra*, not a new physical law or newly selected UBT action. No second tetrad or new fundamental field.

## Established Clifford module [ASSUMED]

Freeze the tetrad at an orthonormal regular frame and retain an arbitrary metric-compatible Lorentz spin connection with 24 independent coefficients:

\[
\{\gamma^a,\gamma^b\}=2\eta^{ab}I_4,\quad
\eta=\operatorname{diag}(-1,1,1,1),\quad
\Omega_\mu=\frac14\omega_{\mu ab}\gamma^a\gamma^b,\quad
\omega_{\mu ab}=-\omega_{\mu ba}.
\]

## Grade contraction and kernel [PROVED, restricted]

The product of a Clifford vector and a bivector contains exactly vector and trivector grades:

\[
\mathcal D=\gamma^\mu(\partial_\mu+\Omega_\mu),\quad
V=\gamma^\mu\Omega_\mu
=\frac12\eta^{\mu a}\omega_{\mu ab}\gamma^b
+\frac14\omega_{\mu ab}\gamma^{[\mu}\gamma^a\gamma^{b]}.
\]

The exact matrix rank of the 24-to-16-entry spin-connection contraction is 8, with 16-dimensional kernel. The image is precisely 4 vector plus 4 trivector grades:

\[
\operatorname{rank}_{\mathbb C}(\omega\mapsto V)=8,\quad
\dim_{\mathbb C}\ker=16,\quad
\operatorname{im}=\operatorname{span}_{\mathbb C}\{\gamma^a,\gamma^{abc}\}.
\]

The kernel is the standard tensor-torsion sector of this **minimal Dirac contraction**. It does not mean tensor torsion is absent from curvature, gravitational dynamics, transport or nonminimal couplings.

## Compatible square with torsion [PROVED, restricted]

The same frozen tetrad and Lorentz coefficients reconstruct the affine connection and torsion; compatibility is verified, not assumed by the test:

\[
\Gamma^\rho{}_{\mu\nu}=\eta^{\rho a}\omega_{\mu a\nu},\quad
T^\rho{}_{\mu\nu}=\Gamma^\rho{}_{\mu\nu}-\Gamma^\rho{}_{\nu\mu},\quad
[\Omega_\mu,\gamma^\nu]+\Gamma^\nu{}_{\mu\rho}\gamma^\rho=0.
\]

Define the spin curvature and bivector generators:

\[
\nabla_\mu=\partial_\mu+\Omega_\mu,\quad
F_{\mu\nu}=[\nabla_\mu,\nabla_\nu],\quad
\gamma^{\mu\nu}=\frac12[\gamma^\mu,\gamma^\nu],
\]

The **complete squared differential operator** includes a torsion-first-derivative term. Omitting it while keeping F gives an incorrect interpretation of the Clifford spin-curvature contribution:

\[
\boxed{\mathcal D^2
=\eta^{\mu\nu}(\nabla_\mu\nabla_\nu-\Gamma^\rho{}_{\mu\nu}\nabla_\rho)
+\frac12\gamma^{\mu\nu}(F_{\mu\nu}-T^\rho{}_{\mu\nu}\nabla_\rho).}
\]

For constant coefficients, the independent direct multiplication is:

\[
\mathcal D^2
=\eta^{\mu\nu}\partial_\mu\partial_\nu
+\{\gamma^\mu,V\}\partial_\mu+V^2
\quad(\gamma,\Omega\ \text{constant}).
\]

The regression suite verifies all 4 first-derivative coefficients and the complete zero-order 4-by-4 matrix for trace, axial, tensor-kernel and rational generic connections. The metric-compatible Clifford identity is tested on every frame index.

## Nonzero curvature invisible to contracted Dirac operator [COUNTEREXAMPLE]

The following nonzero tensor-kernel Lorentz connection has vanishing contracted V:

\[
\omega_{0\,12}=1,\quad\omega_{1\,02}=1,\quad
\Omega_0=\frac12\gamma^1\gamma^2,\quad
\Omega_1=\frac12\gamma^0\gamma^2,\quad
V=\gamma^0\Omega_0+\gamma^1\Omega_1=0.
\]

Yet it has noncommuting spin matrices and nonzero curvature, while the minimal first-order operator and its square are exactly flat in this **restricted frozen frame**:

\[
[\Omega_0,\Omega_1]\ne0,\quad
\mathcal D=\gamma^\mu\partial_\mu,\quad
\mathcal D^2=\eta^{\mu\nu}\partial_\mu\partial_\nu.
\]

This does not exclude additional torsion observables or matter couplings; it demonstrates that spin curvature alone cannot be read off from the contracted Dirac operator. All curvature and torsion terms must be retained before drawing a dynamical conclusion.

## Vector, axial and causal control [PROVED, restricted]

Two sparse witnesses isolate the vector and trivector channel:

\[
\omega_{0\,01}=2\Longrightarrow V=-\gamma^1,\quad
(\omega_{0\,12},\omega_{1\,02},\omega_{2\,01})=(1,-1,1)
\Longrightarrow V=\frac32\gamma^0\gamma^1\gamma^2.
\]

The first-order principal symbol stays on the previously established Clifford null cone:

\[
P(k)=\gamma^\mu k_\mu,\quad
P(k)^2=(\eta^{\mu\nu}k_\mu k_\nu)I_4,\quad
\det P(k)=(\eta^{\mu\nu}k_\mu k_\nu)^2.
\]

## Unresolved UBT dynamics [OPEN]

**Next real gate:** derive the metric-compatible spin and left/right connections *from the single Theta action*, not from freely assigned omega. Then decide which tensor-torsion directions are constrained or propagating, prove Dirac-factor selection despite the known second-order action-order obstruction, and calculate the reduced Hamiltonian and stability. The exact 24-to-8 result is a standard-algebra verification, not a solution of this dynamical problem.

**Verifier:** `tests/test_clifford_compatible_torsion_square.py`, 8/8 exact local SymPy cases. **Repo grounding:** `canonical/geometry/biquaternion_dirac_lift.tex:1-110`; `canonical/geometry/connection.tex:19-83`; `research_tracks/observer_information_hamiltonian_2026_10_full_clifford_operator.en.md:15-52`; `research_tracks/action_selection/clifford_axial_pseudoscalar.en.md:20-80`; `research_tracks/canonical_relation_generalized_dirac/action_origin_obstruction.tex:50-155`. Full UBT action, Lean proof and semantic translation review remain OPEN.
