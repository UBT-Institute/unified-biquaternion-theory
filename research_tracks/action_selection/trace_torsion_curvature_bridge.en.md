<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: trace-torsion-action-bridge.provenance -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact scalar-tensor comparison under independent metric/connection assumptions; NOT finalized fundamental UBT action.
UBT-AI-PROVENANCE-END
-->
# Trace torsion from a nonminimal scalar-curvature term: a conditional action test

**Status: DERIVED_WITH_ASSUMPTIONS / UBT FIRST-PRINCIPLES GAP OPEN.** This is a sharp test against the existing `GAP-10T-DYN` and merged FLRW canonical-contortion calculations, NOT a selection of the one final UBT action. Standard scalar-tensor/Einstein–Cartan mathematics is not original to UBT.

## Restricted candidate and conventions

Introduce one positive function F of the radial field already in Theta, while **treating the metric and metric-compatible torsion as independent for this comparison** and setting direct spin matter currents to zero. The candidate is

\[
S_{\mathrm{test}}[g,\Gamma,\rho]
=\frac12\int d^4x\sqrt{-g}\,F(\rho)\mathcal R(g,\Gamma),
\qquad F(\rho)>0.
\]

Assume the **pure trace** torsion branch in four dimensions, with the same affine-index ordering used in the canonical contortion track. Then

\[
T^\lambda{}_{\mu\nu}=\Gamma^\lambda{}_{\mu\nu}
-\Gamma^\lambda{}_{\nu\mu},
\quad t_\mu=T^\nu{}_{\mu\nu},
\quad K^\lambda{}_{\mu\nu}
=\frac13(g_{\mu\nu}t^\lambda-\delta^\lambda_\mu t_\nu).
\]

By direct substitution into the affine Ricci tensor with the indicated curvature convention,

\[
\boxed{\mathcal R(g,\Gamma)=R(g)+2\nabla^{\mathrm{LC}}_\mu t^\mu
-\frac23t_\mu t^\mu.}
\]

The contribution of the gradient term is a divergence when F is constant. After integrating by parts,

\[
S_{\mathrm{test}}=
\frac12\int\sqrt{-g}\left[
FR(g)-2(\partial_\mu F)t^\mu-\frac23Ft_\mu t^\mu
\right]d^4x+\text{boundary}.
\]

Varying the trace torsion before any FLRW substitution yields the algebraic Cartan equation

\[
0=\frac{\delta S}{\delta t_\mu}
\quad\Longrightarrow\quad
\boxed{t_\mu=-\frac32\partial_\mu\ln F(\rho).}
\]

Thus a nonconstant nonminimal scalar coupling can generate trace torsion **without a fermion axial spin current**, but only in the specified independent-variable scalar–Cartan comparator. There is no added torsion propagator.

## Eliminate torsion and identify the hidden dynamical degeneracy

Substituting the algebraic solution back into that same restricted functional gives

\[
\boxed{
S_{\mathrm{eff}}=
\frac12\int d^4x\sqrt{-g}
\left[FR(g)+\frac{3}{2F}(\partial F)^2\right]
+\text{boundary}.}
\]

Under the conformal metric redefinition in four spacetime dimensions this is, up to a boundary term,

\[
\tilde g_{\mu\nu}=F g_{\mu\nu},\quad
\sqrt{-g}\left[FR(g)+\frac{3}{2F}(\partial F)^2\right]
=\sqrt{-\tilde g}\,\tilde R+\text{divergence}.
\]

Therefore this curvature term by itself is conformally equivalent to ordinary Einstein–Hilbert gravity, with **no independent scalar kinetic term in the conformal metric**. It belongs to the familiar degenerate Brans–Dicke sector with omega equal to minus three halves. A scalar potential term U adds a conformal potential U/F squared, but for **independent** rho and metric without other kinetic sources the remaining scalar equation is algebraic:

\[
\frac{d}{d\rho}\!\left[\frac{U(\rho)}{F(\rho)^2}\right]=0.
\]

This is the key physical limitation: getting the required torsion trace is not yet getting independent scalar cosmological perturbations, a physical Hamiltonian, or GR via one composite UBT action. The metric in UBT is a *function* of Theta and the spin connection, so the independent-variable variations assumed above cannot be silently replaced by full UBT variations.

## Match the pre-existing closed-FLRW torsion representation

In merged PR #685 the canonical single-Theta contortion representative with cosmic time V=t-t0 and radial Theta gives a pure-trace torsion t0. Matching its value with the above Cartan equation imposes the exact first-order relation

\[
\boxed{t_0=3\left(H-\frac1V\right)
=-\frac32\frac{\dot F}{F}
\quad\Longleftrightarrow\quad
a(t)^2F(\rho(t))=C^2V(t)^2.}
\]

This integrates to a positive function F proportional to V squared divided by a squared; equivalently it restricts the scale factor once F(rho) is independently specified. Matching is NECESSARY for the representative to solve the scalar–Cartan connection equation, but is NOT SUFFICIENT for the metric and scalar equations, and must not be used as a free functional fit to data.

## Stronger test for the simplest quadratic coupling

For the lowest even positive quadratic model along the same radial representation choose

\[
F(\rho)=F_0+\xi\rho^2,\quad \rho=\sqrt{\mathcal N_0}V,
\quad a(V)=\frac{CV}{\sqrt{F_0+\xi\mathcal N_0V^2}}.
\]

If F0, xi, N0, C and V are positive, differentiation gives

\[
\boxed{
\frac{d^2a}{dV^2}
=-\frac{3CF_0\xi\mathcal N_0V}
{(F_0+\xi\mathcal N_0V^2)^{5/2}}.}
\]

This strictly negative acceleration means that this **minimal positive quadratic curvature coupling** cannot support late-time positive cosmic acceleration on this branch by itself, even before the remaining Einstein and scalar equations are imposed. With F0 equal to zero the scale factor is constant. Other signs or functions can evade the result on limited positive-F domains, but tuning F to any desired a would not count as a prediction.

## Additional decisive test: the existing radial quartic potential

We can go beyond comparing scale factors. In the independent-metric/connection comparator, let the **same existing UBT classified radial quartic** and simplest curvature coupling take the forms
\[
F(\rho)=F_0+\xi\rho^2,\quad
U(\rho)=U_c+\lambda(\rho^2-r^2)^2,
\qquad F_0>0,\ \lambda>0,\ \xi\ge0,\ \rho>0.
\]
The Einstein-frame scalar variation of the *full candidate* including a potential is algebraic, not a propagating scalar wave equation. Its numerator factors **exactly** as
\[
\boxed{
F U'-2UF'
=4\rho\left[\lambda(\rho^2-r^2)(F_0+\xi r^2)-\xi U_c\right].
}
\]
For the nontrivial radial branch, the equation is solved only at an isolated constant value
\[
\boxed{
\rho^2=r^2+\frac{\xi U_c}{\lambda(F_0+\xi r^2)}
}
\]
when the right side is positive; otherwise no real positive solution exists. On any connected smooth solution, rho therefore cannot vary with cosmic time under these hypotheses. But the earlier single-Theta FLRW coframe needs nonzero time derivative of rho to produce a nondegenerate temporal leg. **Consequently the naive independent-variable scalar–Cartan model with this canonical quartic cannot simply be transported unchanged to the nondegenerate radial-Theta FLRW solution.** This is an *additional conditional obstruction*, not a theorem excluding a fully composite UBT variation, other kinetic or matter terms, or modified scalar couplings. It is essential to vary the actual composite action rather than borrow the Einstein-frame equation after independent-field reduction.

## Chain-rule correction: the real composite-UBT connection equation

For the actual radial single-Theta representation the metric/tetrad is **not independent** of the boost spin connection. Let the independent-tetrad first-order parent functional be (S[e,omega,ho]), and set the radial coframe only after its Euler derivatives are defined:
\[
e_\mu{}^0=\frac{\partial_\mu\rho}{\sqrt{\mathcal N_0}},\qquad
e_\mu{}^i=\frac{\rho\,b_\mu{}^i}{\sqrt{\mathcal N_0}}.
\]
Let the Euler densities at fixed other parent variables be
\[
\mathcal E^\mu{}_a:=\left.\frac{\delta S}{\delta e_\mu{}^a}\right|_{\omega,\rho},
\quad \mathcal C^\mu{}_i:=\left.\frac{\delta S}{\delta b_\mu{}^i}\right|_{e,\rho},
\quad \mathcal U_\rho:=\left.\frac{\delta S}{\delta\rho}\right|_{e,\omega}.
\]
Then exact functional chain differentiation, including variation of all metric/measure terms through e, gives the **true composite boost equation**:
\[
\boxed{
\frac{\delta S_{\mathrm{comp}}}{\delta b_\mu{}^i}
=\mathcal C^\mu{}_i+\frac{\rho}{\sqrt{\mathcal N_0}}\mathcal E^\mu{}_i=0.
}
\]
Likewise integrating by parts the derivative of rho in the temporal coframe gives the composite scalar equation:
\[
\boxed{
\frac{\delta S_{\mathrm{comp}}}{\delta\rho}
=\mathcal U_\rho+
\frac{b_\mu{}^i}{\sqrt{\mathcal N_0}}\mathcal E^\mu{}_i
-\frac1{\sqrt{\mathcal N_0}}\partial_\mu\mathcal E^\mu{}_0=0.
}
\]
Here (mathcal E^mu{}_a) already includes the contributions of the parent curvature, tetrad and metric variations; explicit (ho) dependence is in (mathcal U_ho). If the parent action contains derivative terms, these are **Euler functional derivatives** rather than partial derivatives, so the identities still hold under regular boundary assumptions.

**Critical correction to the preceding torison-matching argument:** The independent Cartan equation (mathcal C^mu{}_i=0), and hence its simple trace solution, is NOT generally the equation after substituting the composite tetrad. The exact boost equation includes the extra (homathcal E^mu{}_i/sqrt{mathcal N_0}) source. The earlier matching relation (a^2F=C^2V^2) is therefore a necessary condition **only in the independent-variable comparator (or in a branch where the relevant tetrad Euler terms independently vanish)**. It is *not* established as a necessary condition of any full single-Theta UBT action. A genuine dynamical rank/Hamiltonian claim must solve the coupled composite connection and Theta equations and their constraints, not borrow independent Palatini equations.

The exact toy functional identity is checked in `tools/verify_composite_spin_chain_rule.py` and `tests/test_composite_spin_chain_rule.py`. It is a structural calculus result, not a complete field-equation solution.

## Falsification gates and connection to existing UBT

The scalar-curvature comparison does NOT derive the function F from the biquaternion invariant action, the absolute gravitational coupling, the physical trace spin-current, or the UBT Dirac algebra. In the independent-variable Einstein frame with no scalar potential or matter, ordinary vacuum Einstein equations give no expanding closed spherical FLRW solution, so the curvature-only comparator is not a completed cosmology. A specified potential or matter sector is essential to attempt an on-shell solution. Re-impose e=DTheta/sqrt(N0) and **vary the complete composite action before selecting a gauge**. The rank-ten off-shell certificate of PR #686 does not supply the constrained Einstein lapse equation.

**No quantitative UBT CMB result is claimed.** Existing Planck topology and curvature limits still constrain any proposed closed-dodecahedral realization. The next gate is to derive a unique F and U (or prove their absence) from the declared Theta action, then compute the full composite spin/metric/Theta equations and the reduced quadratic Hamiltonian.

**References:** Shaposhnikov et al., *Matter matters in Einstein–Cartan gravity* (Phys. Rev. D 104, 064036), https://doi.org/10.1103/PhysRevD.104.064036; *Scale and Weyl invariance in Einstein-Cartan gravity* (Phys. Rev. D 104, 124014), https://doi.org/10.1103/PhysRevD.104.124014. Reproducibility: `tools/verify_trace_torsion_curvature_bridge.py`, `tests/test_trace_torsion_curvature_bridge.py`.
