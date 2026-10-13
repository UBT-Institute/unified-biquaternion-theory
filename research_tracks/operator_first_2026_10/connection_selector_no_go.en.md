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

# Connection selector from Theta data: a residual-gauge obstruction

Status: Tier C working research. Analytic argument under explicit assumptions; symbolic example independently checked. LEAN-PENDING. This is not a fundamental UBT action or a GR theorem.

## Assumptions and question

Take a smooth non-null Lorentz-vector carrier V in an oriented four-dimensional patch, a metric-compatible Lorentz spin connection omega, and a nondegenerate coframe e subject to the canonical-branch relation

\[
D_\mu^\omega V^a=\partial_\mu V^a+\omega_\mu{}^a{}_b V^b=s e_\mu{}^a,\quad
g_{\mu\nu}=\eta_{ab}e_\mu{}^a e_\nu{}^b.
\]

Consider an attempted **pointwise, locally Lorentz-equivariant** connection selector using only V, any finite number of its ordinary derivatives, any finite number of ordinary derivatives of the invariant spacetime metric g, and the **value** of e at the point, but not derivatives of e or an independently chosen gauge frame. A prescribed gauge fixing is also outside this class.

## Theorem: residual local stabilizer prevents such a selector

Under these assumptions, no universally locally Lorentz-equivariant rule can recover the complete omega from that restricted list of data, even on a flat nondegenerate coframe background.

Proof. On a non-null patch there is a smooth local little group H(V) of Lorentz transformations preserving V, with Lie algebra dimension 3: SO(3) for timelike V, SO(1,2) for spacelike V. Choose a local Lorentz transformation h(x) satisfying h(x)V(x)=V(x), with h(p)=I and nonzero derivative dh(p) in the little algebra. Under this local frame transformation,

\[
V'=hV=V,\quad e'=he,\quad
\omega'=h\omega h^{-1}-(dh)h^{-1},\quad g'=g.
\]

Every ordinary derivative of V is identical before and after the transformation because V'=V **as a field**. Every ordinary derivative of g is also identical. At p the tetrad value is identical since h(p)=I, yet

\[
\omega'(p)=\omega(p)-dh(p)\ne\omega(p).
\]

A deterministic pointwise rule with identical input data must give identical outputs, contradicting the inhomogeneous transformation law. QED.

This is a **restricted-data no-go**, not an assertion that no spin connection can be derived from richer geometric data. In particular, derivatives of e transform inhomogeneously and can supply precisely the missing information.

## Explicit nondegenerate test configuration

In Cartesian Minkowski coordinates choose

\[
\eta=\operatorname{diag}(-1,1,1,1),\quad
V=(2+t,x,y,z)^T,\quad s=1,\quad \omega=0,\quad e_\mu{}^a=\delta_\mu{}^a.
\]

Restrict to a small timelike patch around p=0. Define

\[
q=V^T\eta V,\quad
P=I-\frac{V(V^T\eta)}{q},\quad
J^1{}_2=1,\quad J^2{}_1=-1,\quad H=PJP.
\]

The exact identities P^2=P, PV=0, H V=0, and H^T eta+eta H=0 hold. At p, H(p)=J. The smooth local Lorentz transformation h(x)=exp(x H(x)) has h V=V, h(p)=I, and (partial_x h)(p)=J. Consequently omega'_x(p)=-J while V, its derivatives, g and e(p) coincide with the original configuration.

For each spacetime index, the map from the 6-dimensional Lorentz Lie algebra to A V has rank 3 and kernel 3 at p; across 4 base directions the algebraic freedom is 12 components. It is not a count of physical particle modes.

## Implications and constructive alternatives

1. A pointwise formula that sets the little-algebra component of omega to zero in a chosen frame can solve the algebraic equation D V=s e, but **is not an equivariant connection selector** under arbitrary local stabilizer changes. Such a rule amounts to a gauge convention.
2. The torsion-free Levi-Civita spin connection omega[e] uses derivatives of the coframe and is gauge covariant. The previous UBT concurrent-vector obstruction shows that simultaneously enforcing e=s^{-1}D V and zero torsion restricts generic curved Einstein geometry in the minimal Lorentz-pair branch.
3. Given a tetrad and a **selected** torsion tensor, metric-compatible omega is unique. Selecting torsion from microscopic UBT data is a separate physical problem; assigning it by hand is not a first-principles derivation.
4. The metric-only quotient is algebraically consistent for metric observables but is not automatically a symmetry of arbitrary second-jet Theta field equations.

## Verification and decision

- Analytic argument: displayed above, relying only on the standard inhomogeneous gauge-connection law and a smooth non-null little group.
- SymPy 1.14.0: exact checks of projector, Lorentz skewness, H V=0, H(p)=J and little-algebra rank; PASS, using tools/verify_operator_first_local_selector_no_go.py.
- Lean: LEAN-PENDING; no formal compilation claimed.
- Physical claim: OPEN. No unique quantum dynamics, graviton, induced Newton constant or observed deviation is obtained.
- Next gate: check whether the physical UBT operator can be formulated purely on the metric quotient, or which independently justified torsion/connection dynamics must be specified before taking its Hessian.

## Repository grounding and attribution

The setup is taken from canonical/gr_closure/gap_10i_paired_connection_audit.tex and canonical/gr_closure/gap_10i_integrability_selection.tex; the status boundary follows research_tracks/operator_first_2026_10/operator_first_status.en.md and DERIVATION_INDEX.md. The local little-group and gauge-transformation principles are standard differential geometry. We claim no priority over those mathematical facts; their restricted-data implication is analyzed here for this UBT composite-tetrad framework.
