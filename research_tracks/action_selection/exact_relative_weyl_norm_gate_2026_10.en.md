<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: exact-relative-weyl-norm-gate -->
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

# Exact relative dilation: Weyl recovery versus norm-only degeneracy

**2026-10-31 · C_working · conditional algebraic theorem and no-go for one ultralocal norm-only closure.** This continues merged PR #819 and explicitly REUSES the established closed relative-dilation model in `research_tracks/action_selection/flat_jet_torsion_action_2026_10.en.md`, plus the existing split-jet surjectivity and normal-Euler adjoint audit. Exact relative dilation itself and the Stueckelberg field change are NOT new UBT results. New here is the precise *no-extra-field Lorentz-invariant norm-only compensator* test and its unavoidable tetrad rank collapse. No physical action or new field content is selected.

## Lorentz-real comparison configuration [ASSUMED]

Work on a regular non-null Lorentz-real four-vector carrier X with the **canonical sharp metric** g=e eta e^T. A relative real exact one-form is present only in the *defining jet*, not automatically in the physical Lorentz spin connection. The scalar phi is initially treated as independently varied for a conditional comparison:

\[
s=\sqrt{\mathcal N_0}>0,\qquad
q=X^aX_a\ne0,\qquad
e_\mu{}^a=s^{-1}(D_\mu^\omega X^a+X^a\partial_\mu\varphi),\qquad
\omega_{\mu ab}=-\omega_{\mu ba}.
\]

The complete first variation of this composite tetrad is:

\[
\delta e_\mu{}^a=s^{-1}
\bigl[(D_\mu^\omega+\partial_\mu\varphi)\delta X^a+
X^a\partial_\mu\delta\varphi+
\delta\omega_\mu{}^a{}_bX^b\bigr].
\]

## Independent exact scalar restores a Weyl direction [PROVED, conditional]

Consider the *coupled*, compactly supported variation of X and phi. Terms proportional to d epsilon cancel identically, without demanding any field equation or choosing omega:

\[
\delta X^a=\varepsilon(x)X^a,\qquad
\delta\varphi=-\varepsilon(x),\qquad
\delta\omega=0
\quad\Longrightarrow\quad
\boxed{\delta e_\mu{}^a=\varepsilon e_\mu{}^a,\ \delta g_{\mu\nu}=2\varepsilon g_{\mu\nu}}.
\]

This is the familiar exact-dilation reparametrization (already used in the flat-jet track):

\[
Y^a=e^\varphi X^a,\qquad
e_\mu{}^a=s^{-1}e^{-\varphi}D_\mu^\omega Y^a.
\]

The pre-existing pure-Lorentz metric response has rank nine on a non-null regular tetrad; the displayed Weyl direction is transverse to its one-dimensional normal cokernel. Pointwise algebraic metric-response rank therefore becomes ten:

\[
\operatorname{rank}(\delta\omega\mapsto\delta g)=9,\qquad
\operatorname{rank}((\delta\omega,\varepsilon)\mapsto\delta g)=10
\quad(q\ne0,\ \det e\ne0).
\]

In particular the normal Euler test source from PR #819 cannot remain in the common formal adjoint kernel when BOTH field variations are allowed independently, since the coupled direction detects it:

\[
\mathcal E^\mu{}_a=hV^\mu X_a,\qquad
V^\mu=e^\mu{}_aX^a,\qquad
\mathcal E^\mu{}_a(\varepsilon e_\mu{}^a)
=\varepsilon hq\ne0
\quad(h\ne0).
\]

This removes a *source-map kernel*, NOT the physical Cartan equation. If a geometric action has an independent fixed-e connection Euler source, it must still be varied; the connection equation may mix it with the tetrad equation. Independent phi is NOT currently established as a fundamental or auxiliary degree of freedom of single-Theta UBT.

## Norm-only Theta composite cannot realize this compensation [PROVED, restricted]

Now forbid an independently varied scalar and try to obtain phi only as an **ultralocal Lorentz-invariant** function of the same real carrier X. On a connected fixed-sign non-null Lorentz orbit this has the form phi=f(q), q=X squared. Under a local rescaling of X:

\[
\varphi=f(q),\quad q=X^2,\qquad
\delta X^a=\varepsilon X^a
\ \Longrightarrow\
\delta\varphi=2q f'(q)\varepsilon.
\]

To reproduce the compensated pointwise Weyl variation of the previous section for EVERY smooth epsilon, the coefficient of its derivative must vanish. This forces the unique norm-dependent solution, up to an additive constant:

\[
1+2q f'(q)=0
\quad\Longrightarrow\quad
\boxed{\varphi=-\frac12\ln|q|+\mathrm{const.},\qquad
w_\mu=-\frac{\partial_\mu q}{2q}}.
\]

But metric compatibility of omega implies the following contraction of the ORIGINAL defining coframe, including arbitrary nonzero Lorentz curvature:

\[
X_aD_\mu^\omega X^a=\frac12\partial_\mu q,\qquad
X_a e_\mu{}^a
=\frac1s\left(\frac12\partial_\mu q+
q\,\partial_\mu\varphi\right)=0.
\]

Thus every row of the coframe lies in the three-dimensional internal subspace orthogonal to X. Since q is nonzero, the coframe and canonical sharp metric are necessarily degenerate:

\[
X_a e_\mu{}^a=0\ \forall\mu
\quad\Longrightarrow\quad
\operatorname{rank}e\le3,\qquad
\det e=0,\quad
\det g=(\det\eta)(\det e)^2=0.
\]

This is a pointwise algebraic obstruction for the *unique Lorentz-invariant norm-only ultra-local scalar compensator*, not for arbitrary complex biquaternion fields, derivative-dependent composite laws or nonminimal Clifford grade data. With phi=f(q) not obeying the compensation equation, the specific pointwise Weyl cancellation is absent; other dynamical ways of supplying a normal equation are not excluded.

## Implication for action selection [OPEN]

The tested alternatives separate sharply: **(i)** an independently admissible exact relative scalar removes the restricted normal adjoint kernel algebraically but requires a derivation of its variation, constraints and absence of extra physical modes; **(ii)** obtaining precisely that scalar from the sole Lorentz norm of X collapses the metric and cannot support the required regular classical branch. To progress, derive from the existing complete complex Theta and Clifford/two-sided structure a real relative channel with the required variation and a nondegenerate metric, or prove the normal Einstein equation through a different action/constraint mechanism. The previous flat-jet conformally-flat no-go and the one-action microscopic underdetermination remain unchanged.

**Verification:** `tests/test_exact_relative_weyl_norm_gate.py` — 11/11 exact local SymPy checks, including arbitrary time-dependent epsilon and phi, Lorentz Lie identity, Stueckelberg field change, norm-only differential equation, generic curved Lorentz algebraic connection, explicit singular determinant, normal Euler pairing and 9-to-10 metric-response rank. **Prior-work grounding:** `research_tracks/action_selection/flat_jet_torsion_action_2026_10.en.md:23-50`, `research_tracks/action_selection/composite_lorentz_variation_rank_2026_10.en.md:20-103`, `research_tracks/action_selection/theta_normal_adjoint_kernel_2026_10.en.md:20-66`, `canonical/geometry/connection.tex:16-80`. The full microscopic action, physical scalar admissibility, global solution and Lean proof remain unestablished.
