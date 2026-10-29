<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: g1-invariant-causal-bridge -->
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

# G1: composite scalar observables and a causal-cone ambiguity

**2026-10-28 · PR #809 · C_working · OPEN.** First-jet mathematical construction on the restricted Mat(2,C) carrier; not full UBT, a unique quantum local algebra, a fundamental information selector or a selected action. Builds on G1_FINITE_DIAMOND_INFORMATION and the master theta_potential_invariants result.

## Reuse the two proven scalar invariants [PROVED, restricted]

The existing connected SL(2,C) congruence and constant/global U(1) phase action support a normalized quadratic invariant H and a quartic invariant K. Their basis completeness through degree four is an already documented restricted result; it does not classify all derivative or quantum observables:

\[
\Theta=\sum_{a=0}^{3}(u_a+iv_a)\sigma_a,\quad
H(\Theta)=\operatorname{Tr}(\Theta^\sharp\Theta^\dagger)
=2(u_0^2+v_0^2-\sum_{i=1}^3(u_i^2+v_i^2)),
\quad K(\Theta)=|\det\Theta|^2.
\]

On a **finite set of labelled events** S, define the classical commutative cylinder algebra of functions of these composites on the space of field configurations. Constants are included and complex conjugation makes it a *-algebra:

\[
\mathcal A_{\rm inv}(S)=
\operatorname{alg}\{\,f(H(\Theta_p),K(\Theta_p)):p\in S\,\},
\qquad \mathcal A_{\rm inv}(S)\subseteq\mathcal A_{\rm inv}(T)\quad(S\subseteq T).
\]

Local inclusions obey isotony, and disjoint algebras commute trivially because the model is classical. Internal Lorentz congruence and phase invariance hold pointwise. This is an invariant **kinematical subalgebra**, not the uniquely inferred physical observable net of UBT. The assignment of measurement outcome labels and their probabilities is additional operational input. Haag–Kastler nets require more, including causal locality/covariance and quantum state/measurement construction.

## Two-invariant information rank [PROVED, restricted]

Use two independently normalized trial binary channels with arbitrary beta scales, not physical Born-rule predictions. The candidate relative-entropy loss is:

\[
\mathcal I(q)=D_{\rm Bern}(r_H\Vert p_H(H(q)))
+D_{\rm Bern}(r_K\Vert p_K(K(q))),
\qquad p_j(I_j)=\frac{1}{1+\exp(-\beta_j I_j)}.
\]

At equality of the observed and reference probabilities, the Hessian is a sum of two positive rank-one matrices:

\[
\left.\partial_A\partial_B\mathcal I\right|_{r_j=p_j}
=\sum_{j\in\{H,K\}}\beta_j^2p_j(1-p_j)
\,\partial_A I_j\,\partial_B I_j.
\]

The Jacobian has exact rank two at a regular nonscalar example:

\[
q_*=(u_0,u_1,v_1)=(2,1,1)
\quad\text{with other real components zero},\quad
(H,K)=(4,20),\quad
\operatorname{rank}\frac{\partial(H,K)}{\partial q^A}=2,\quad
\operatorname{rank}\mathcal F=2.
\]

Thus this restricted two-channel information probe has six null tangent directions in the eight-real carrier; at a pure scalar field point its Jacobian rank collapses to one. Null directions are not automatically ghost modes, gauge modes or degrees of freedom of UBT. A different carrier or jet-dependent observables require new calculation.

## Exact pointwise-invariants / causal-cones mismatch [COUNTEREXAMPLE]

Consider two smooth, distinct matrices in the fixed Omega=0 Lorentz chart:

\[
\Theta=tI+x\sigma_1+y\sigma_2+z\sigma_3,\qquad
\widetilde\Theta=e^{i\alpha t}\Theta,\quad
\alpha\in\mathbb R.
\]

Their invariant *functions* agree throughout spacetime, not merely at one event:

\[
H(\widetilde\Theta(x))=H(\Theta(x)),\qquad
K(\widetilde\Theta(x))=K(\Theta(x))
\quad\text{for all }x.
\]

Hence all finite derivatives or algebraic functions of H and K also agree. Nonetheless the restricted gradient-metric readout produces different null cones at a point:

\[
g_{\mu\nu}=B(\partial_\mu\Theta,\partial_\nu\Theta),\qquad
g|_{(1,0,0,0)}=\operatorname{diag}(1,-1,-1,-1),\qquad
\widetilde g|_{(1,0,0,0)}
=\operatorname{diag}(1+\alpha^2,-1,-1,-1).
\]

For nonzero alpha the zero sets of the two Lorentzian quadratic forms differ. If local phase were declared a gauge transformation, the Omega=0 derivative metric would not be an acceptable gauge-invariant physical readout until a transforming phase connection were included. If it is not gauged, the two distinct fields are indistinguishable by the entire H/K observable subalgebra yet have different causal geometry. Both branches expose missing structure, not a general no-go for UBT. The local phase is NOT a symmetry of the fixed-Omega=0 metric comparator.

## Conditional causal order from one and the same Theta field [PROVED in comparator]

Reuse the previous nonflat eight-real gradient embedding, adding a constant scalar to keep N and K positive at sampled points without affecting the metric:

\[
\Theta_c=(t+2)I+x\sigma_1+y\sigma_2+z\sigma_3
+i\kappa tx\,\sigma_1,\quad
g_c=\eta-\kappa^2(x\,dt+t\,dx)^2,\quad
A=1+\kappa^2(t^2-x^2)>0.
\]

For A>0 and Lorentz signature, the two local coordinate null directions in the (t,x) sector satisfy:

\[
v_\pm=\left.\frac{dx}{dt}\right|_{ds^2=0,\,dy=dz=0}
=\frac{-\kappa^2tx\pm\sqrt A}{1+\kappa^2t^2},\qquad
v_\pm\big|_{(\kappa,t,x)=(1/2,1,0)}
=\pm\frac{2}{\sqrt5}.
\]

This is a coordinate velocity, not a universal observer-independent bound; at the origin the coordinate speed is unity in the chosen units. Along the x=y=z=0 worldline the tangent is future timelike, so the sampled event chain is:

\[
a=(-1/2,0,0,0)\prec o=(0,0,0,0)\prec
b=(1/2,0,0,0),\qquad
g_c(\partial_t,\partial_t)\big|_{x=0}=1.
\]

This **replaces the previously imposed finite three-site causal ordering with one computed from the same trial Theta metric**. The sampled subintervals {a,o}, {o,b} are not full continuous causal diamonds. The example is nonflat, but it is NOT on-shell Einstein gravity, a selected physical causal cone or an actual quantum net.

## Falsifiable next gate [OPEN]

The new bridge supports scalar gauge-invariant kinematics and a causal sampling in the same **restricted** geometric comparator. Its key negative result is structural: even all jets of these two scalar invariants fail to reconstruct the phase-sensitive causal metric. A genuine physical shared-reality principle must use covariant derivative or holonomy observables, their gauge transformations, and a constrained solution/state space, not only pointwise H,K. Construct one such candidate and test a Lorentz-real, phase-covariant null cone and a nontrivial information restriction before declaring a dynamical selector.

**Status:** G1 PARTIAL, G2 NOT PROMOTED, G3/G4 PARKED. Do not change PR #807 or #808; do not merge or modify canonical claims. Exact SymPy test: `python -m unittest discover -s tests -p 'test_theta_invariant_causal_bridge.py' -v` (7 tests passed locally).

**Background:** existing repo `research_tracks/action_selection/theta_potential_invariants.en.md`; Haag–Kastler local algebra framework: https://doi.org/10.1063/1.1704187 ; measurement theory caveat: https://doi.org/10.1007/s10701-024-00756-8 .
