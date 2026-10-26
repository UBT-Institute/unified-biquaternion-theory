<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional algebraic theorem; full UBT dynamics remains open.
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


# Composite Lorentz-slice kinetic volume collapse and flat-gradient boundary theorem

**Status: DERIVED_WITH_ASSUMPTIONS.** Independent clarification of the much narrower timelike-gauge Proposition 9 in merged PR #679. This **does not** replace the canonical UBT field or introduce a new action. The objective is to determine what the *existing* invariant quadratic kinetic family can and cannot generate.

## I. Definition and exact algebraic theorem (any nondegenerate Lorentz tetrad)

Use the current canonical single biquaternion \(\Theta\in\mathbb B\simeq M_2(\mathbb C)\). On the real Lorentz tetrad slice, write the **covariant derivative**, not necessarily the field itself, as
\[
D_\mu\Theta=i\sqrt{\mathcal N_0}\,[e_\mu{}^0 I+e_\mu{}^j\sigma_j],
\qquad e_\mu{}^a\in\mathbb R,\quad\mathcal N_0>0 .
\]
A fixed sign change of the three \(\sigma_j\) is an equivalent quaternion convention. The canonical central quaternion-antilinear metric identity gives
\[
g_{\mu\nu}=\eta_{ab}e_\mu{}^ae_\nu{}^b,\qquad
\eta=\operatorname{diag}(-1,+1,+1,+1).
\]
Let the real polarization of the uniquely specified constant quadratic invariant of the **declared** \(U(1)\times SL(2,\mathbb C)\) representation be
\[
B(X,Y)=\tfrac12\operatorname{Tr}
[\operatorname{adj}(X)Y^\dagger+\operatorname{adj}(Y)X^\dagger],
\quad B(X,X)=\operatorname{Tr}[\operatorname{adj}(X)X^\dagger].
\]
For arbitrary real \(a^a,b^a\), the Pauli identities yield exactly
\[
B\!\left(i\sqrt{\mathcal N_0}(a^0 I+a^j\sigma_j),
i\sqrt{\mathcal N_0}(b^0 I+b^j\sigma_j)\right)
=2\mathcal N_0(a^0b^0-\mathbf a\cdot\mathbf b).
\]
Consequently
\[
\boxed{B(D_\mu\Theta,D_\nu\Theta)=-2\mathcal N_0 g_{\mu\nu}.}
\]
For **any nondegenerate** \(g\), the Lorentz-invariant minimal kinetic density
\[
\mathcal L_{\rm kin}:=-\tfrac c2\sqrt{-g}\,
g^{\mu\nu}B(D_\mu\Theta,D_\nu\Theta)
\]
therefore collapses **identically**
\[
\boxed{\mathcal L_{\rm kin}=4c\mathcal N_0\sqrt{-g}.}
\]
The result holds at the level of the constrained Lorentz slice regardless of the explicit tetrad profile and without imposing \(X=i\rho I\), any special potential, a specific connection ansatz, or field equations. The coefficient depends on the action normalization and spacetime dimension; in four dimensions with the stated sign conventions it is exactly \(+4c\mathcal N_0\).

**Interpretation:** The assumed 'quadratic' kinetic operator contributes a volume term once the *same* field defines the metric. It cannot be double-counted as four healthy independent scalar oscillators. However \(\sqrt{-g}\) still depends on \(D\Theta\); its variation is NOT zero for a generic independent connection or for variations leaving the declared slice. This is *not* a full UBT no-go and not a complete Dirac/Hamiltonian analysis.

## II. Stronger restricted theorem: pure-gradient tetrad is flat

Make these **additional, restrictive** assumptions:
1. The two-sided connection is gauge-trivial on a simply connected local patch, so \(D_\mu\Theta=\partial_\mu\Theta\).
2. The field takes values in a fixed affine Lorentz-real subspace:
\[
\Theta(x)=\Theta_*+i\sqrt{\mathcal N_0}
[y^0(x)I+y^j(x)\sigma_j],\qquad y^a\in\mathbb R.
\]
3. The Jacobian \(J^a{}_\mu=\partial_\mu y^a\) is invertible and its determinant has fixed sign on the patch.
4. The only action terms are the collapsed minimal kinetic term and a derivative-free potential \(U(\Theta(y))\); no connection curvature, independent metric, additional matter kinetic term, torsion or curvature term.

Then \(g_{\mu\nu}=\eta_{ab}J^a{}_\mu J^b{}_\nu\).
The map \(x\mapsto y(x)\) is a local diffeomorphism by the inverse-function theorem, and \(g=y^*\eta\). Hence
\[
\boxed{R_{\mu\nu\rho\sigma}[g]=0.}
\]
For the chosen positive-orientation branch \(\sqrt{-g}=\det J\), so the full reduced density is
\[
\mathcal L_{\rm red}=\det J\, F(y),\qquad
F(y)=4c\mathcal N_0-U(\Theta(y)).
\]
The target 4-form \(\Omega=F(y)\,dy^0\wedge dy^1\wedge dy^2\wedge dy^3\) is locally exact. Explicitly, take
\[
G(y)=\int_{0}^{y^0}F(s,y^1,y^2,y^3)\,ds,\quad
\beta=G(y)\,dy^1\wedge dy^2\wedge dy^3,\quad
d\beta=\Omega .
\]
Therefore \(\mathcal L_{\rm red}d^4x=d(y^*\beta)\), with explicit current
\[
J^\mu_{\rm bdy}=G(y)\,\epsilon^{\mu\nu\rho\sigma}
(\partial_\nu y^1)(\partial_\rho y^2)(\partial_\sigma y^3),
\quad
\boxed{\partial_\mu J^\mu_{\rm bdy}=F(y)\det(\partial_\mu y^a).}
\]
The local Euler--Lagrange equations of this **restricted** action therefore vanish identically for compactly supported \(y\)-variations. No new local propagating gravitational modes arise inside this truncation. For \(\det J<0\), an overall fixed orientation sign modifies the boundary current. Globally nontrivial target cohomology/boundaries can carry topological data, without changing the local E-L conclusion.

**Essential warning:** Variation of the *full unconstrained* \(\Theta,A,B,\ldots\) action followed by restriction is NOT generally equivalent to varying this restricted action. Therefore the theorem does not establish that these \(y\) configurations satisfy the full UBT field equations.

## III. Implications for action selection and CMB

1. The fixed-background oscillator Hamiltonian in the merged dodecahedral track is a **conditional test-field truncation**, not automatically the Hamiltonian of the composite-metric family.
2. The fixed-background ghost analysis and auxiliary-connection obstructions in merged PR #679 address different constraints. The algebraic volume identity here holds on *any* nondegenerate Lorentz-real tetrad, but makes no assertion about stability of the full constrained theory.
3. In the gauge-trivial pure-gradient branch, every nondegenerate metric is locally Minkowski, so that branch cannot support GR curvature, FLRW perturbations, primordial gauge-invariant \(\zeta\), or a genuine derived CMB spectrum. Coordinate wiggles \(y^a(x)\) do not generate Riemann curvature.
4. A successful candidate single UBT action must specify **which term** generates its nontrivial gravitational equations (curvature, holonomy, torsion, derivative connections or genuinely new constrained invariant), demonstrate a nondegenerate on-shell background, compute constraints/healthy physical energy, then derive \(\zeta[\Theta]\) and its power spectrum before using the \(S^3/2I\) CMB kernel.
5. A generic local curvature term such as \(\int\sqrt{-g}\,R[g(\Theta,A,B)]\) is **not** derived from the kinetic family and changes the variational order; it is only a test ansatz unless its coefficient and origin are fixed by UBT. When \(g=y^*\eta\) pure-gradient, this scalar curvature is still exactly zero.

**Independent verification:** \`tools/verify_lorentz_jet_boundary.py\` and \`tests/test_lorentz_jet_boundary.py\` include exact polynomial metric-determinant / boundary-current checks and finite-matrix checks with both coordinate-nonlinear and affine maps. SymPy checks are computational certificates for examples; the proofs above establish the unrestricted identities analytically.

**Related:** \`canonical/fields/theta_field.tex\` (single field and central tetrad); \`research_tracks/action_selection/theta_potential_invariants.en.md\` (unique invariant); \`research_tracks/action_selection/canonical_family_hamiltonian_bridge.en.md\` in **merged PR #679** (conditional ghost and narrower composite timelike branch); \`research_tracks/dodecahedral_action_cmb/DERIVATION.md\` (toy CMB, not a data fit).
