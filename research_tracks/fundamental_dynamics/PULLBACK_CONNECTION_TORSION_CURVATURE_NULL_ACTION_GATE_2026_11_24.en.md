<!-- BILINGUAL-UNIT: pullback-connection-torsion-curvature-null-action-2026-11-24 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Restricted target-pullback four-real theorem, not a selected UBT connection/action or global no-go.
UBT-AI-PROVENANCE-END
-->
# Stronger connection-selection no-dynamics gate: nonzero curvature and torsion can still be a null pullback action

**24 November 2026 — C_working / exact restricted L0. The microscopic UBT action and unique torsion selector remain OPEN.**

\[
Y^2:=\eta_{ab}Y^aY^b>0,\quad J^a{}_\mu=\partial_\mu Y^a,\quad
\widehat\Omega_d{}^a{}_b(Y)
=\frac{\lambda\,\eta^{aa}}{Y^2}\varepsilon_{abcd}Y^c,\quad
C_\mu{}^a{}_b=\widehat\Omega_d{}^a{}_b(Y)J^d{}_\mu .\tag{1}
\]
\[
\boxed{C_\mu{}^a{}_bY^b=0,\quad
E^a=dY^a+C^a{}_bY^b=dY^a,\quad
g_{\mu\nu}=\eta_{ab}J^a{}_\mu J^b{}_\nu.}\tag{2}
\]
\[
\boxed{T_{abc}=\frac{2\lambda}{Y^2}\varepsilon_{abcd}Y^d,\qquad
T_{abc}T^{abc}=-\frac{24\lambda^2}{Y^2}.}\tag{3}
\]
\[
\left.F_{12}{}^1{}_2(C)\right|_{Y=(r,0,0,0),\,J=I}
=-\frac{\lambda^2}{r^2}\ne0,\qquad r>0,\ \lambda\ne0.\tag{4}
\]
\[
\boxed{\mathcal L_T=\sqrt{-g}\,T_{abc}T^{abc}
=-24\lambda^2\frac{\det J}{Y^2}\qquad(\det J>0).}\tag{5}
\]
\[
S[Y]=\int_M Y^*\widehat{\mathcal L}_4,\qquad
\widehat{\mathcal L}_4=f(Y)\,dY^0\wedge dY^1\wedge dY^2\wedge dY^3,\qquad
d\widehat{\mathcal L}_4=0.\tag{6}
\]
\[
\boxed{\widehat{\mathcal L}_4=d\widehat B_3\ \text{locally},\qquad
\frac{\delta S}{\delta Y^a}=0,\qquad
\frac{\partial^2\mathcal L}{\partial\dot Y^a\partial\dot Y^b}=0.}\tag{7}
\]
\[
\omega=Y^*\widehat\omega,\qquad E=Y^*\widehat E,\qquad
T=Y^*\widehat T,\qquad F=Y^*\widehat F,\qquad
\mathcal L_4=Y^*\widehat{\mathcal L}_4 .\tag{8}
\]

## Exact axial stabilizer-connection witness

Stay within the nondegenerate timelike **four-real pure-vector Lorentz slice** of one locked \(\Theta\), using a local oriented frame and \(\mathcal N_0=1\). Let \(e^a=dY^a\) in the reference zero-connection gauge. The target-space Lorentz-algebra-valued connection one-form (1), with \(\eta=\operatorname{diag}(1,-1,-1,-1)\) and \(\varepsilon_{0123}=+1\), is an **example**, not a derived physical selector. Its lowered internal indices are antisymmetric. Algebraic antisymmetry of \(\varepsilon_{abcd}\) proves that it stabilizes \(Y\), hence (2) is an **exact identity for all smooth \(Y(x)\)**, not merely a linearization. The canonical tetrad and locked metric are unchanged even though \(C\ne0\).

Its induced tetrad torsion is exactly the totally antisymmetric axial tensor in (3), and its squared invariant is nonzero on the timelike patch for \(\lambda\ne0\). The full curvature also need not vanish: (4) is an explicit fixed-frame local witness at \(Y=(r,0,0,0)\) and \(J=I\). In that component the two exterior-derivative terms vanish identically, while the non-Abelian commutator gives the displayed nonzero answer. This is a **pointwise off-shell geometry construction**, not a statement that the connection solves UBT's dynamics, the Palatini equation or a globally prescribed Lorentz gauge. In another local Lorentz trivialization the connection *difference* must transform tensorially relative to the reference connection.

## Why its quadratic torsion action still has no bulk dynamics

For the selected example (1), (3) reduces the manifestly torsionful local invariant to the pullback-weighted volume (5). Applying the previously proven Piola/cofactor identity to \(f(Y)=-24\lambda^2/Y^2\) gives all four Euler–Lagrange derivatives equal to zero and a zero velocity Hessian for compactly supported variations. Thus even adding this nonzero \(T^2\) density fails to generate propagating dynamics on the declared slice. The sign convention in (3) is for signature \((+---)\) and the displayed internal index ordering.

## General pullback-only theorem, including curvature actions

The obstruction is broader than this axial example. Assume that the entire chosen tetrad and Lorentz connection on a domain are **target pullbacks** of *fixed smooth geometric data* defined over a four-dimensional target, as in (8), that \(Y\) is locally invertible and there are no independent fields, background base tensors, explicit base-coordinate coefficients or other jet dependence beyond the pullback. Then torsion, curvature, their local tensor contractions, and any natural scalar four-form built algebraically from them also pull back from the target (the target metric/Hodge operations transform naturally under a local diffeomorphism). Any such target four-form is automatically closed by dimension, so it is **locally exact** by the Poincaré lemma: (6)-(7). In coordinates this is exactly a possibly very complicated \(f(Y)\det(\partial Y)\) action. Its Euler derivative and velocity Hessian vanish on the fixed-orientation invertible branch. **Even a curvature-squared Lagrangian cannot help inside this precisely declared pullback-only class.**

The conclusion does NOT rule out globally nontrivial topology/boundary effects, different metric or torsion geometry outside the pullback class, an eight-real \(\Theta\), extra \(\psi\)-mode dependence, curvature/connection responses not expressible as \(Y^*\widehat\omega\), nonlocal quantum effective actions, or a truly independent dynamical connection selected by a single-field principle. The target data in the theorem are *fixed coefficients*, not an additional freely varied physical spacetime field. A chosen target connection may have nonzero curvature and torsion while its pullback action carries no local physical fluctuations of the coordinate map \(Y\). This does not prove absence of all full-UBT modes.

## Actual decision for the action-selection program

Do not equate a torsionful or curved reconstructed connection with a new fundamental kinetic term. **Reject pullback-only geometry actions as a source of bulk Theta dynamics in the four-real invertible branch.** To obtain physical evolution, one must demonstrate a genuinely non-pullback functional dependence of the selected two-sided connection on the real eight-component field/its independent jets or a derived quantum nonlocal sector, and then calculate the reduced Hessian, constraints and positive-energy spectrum. Merely choosing the free stabilizer coefficient \(\lambda\) is an arbitrary branch selection; it cannot replace a torsion law.

Links: research_tracks/action_selection/exact_stabilizer_torsion_ambiguity.en.md, research_tracks/action_selection/composite_contortion_kernel.en.md, research_tracks/fundamental_dynamics/WEIGHTED_GRADIENT_VOLUME_NULL_DYNAMICS_GATE_2026_11_24.en.md, draft PR #909.

**Verifier:** tools/verify_theta_pullback_connection_nodynamics_2026_11_24.py and research_tracks/fundamental_dynamics/tests/test_theta_pullback_connection_nodynamics_2026_11_24.py: exact symbolic checks for stabilizer/metric compatibility, fully axial torsion invariant, nonzero curvature witness, nonaffine Piola Euler identities and zero Hessian. The broad target-pullback theorem is proved analytically by exterior-form naturality, not asserted by a finite number of symbolic tests. **LEAN-PENDING, review and full physical Hamiltonian OPEN; do not merge as derived dynamical gravity.**
