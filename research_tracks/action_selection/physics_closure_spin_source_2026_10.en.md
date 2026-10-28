<!-- BILINGUAL-UNIT: physics-closure.spin-source.scope -->
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

# Spin-source response and bulk coefficient identifiability

**29 October 2026; C_working; CONDITIONAL.** English is the translation source. This [audit](physics_closure_2026_10.en.md) extension studies an imported effective comparator. It selects no microscopic action, component count, or new fundamental field. The covariant tetrad and central metric are retained. The tetrad is held fixed during connection variation; the full composite-Theta chain rule remains open.

<!-- BILINGUAL-UNIT: physics-closure.spin-source.assumptions -->
## Action and source assumptions

Use a smooth oriented Lorentzian patch with invertible tetrad, a metric-compatible physical connection, constant real coefficients and compact-support variations or fixed boundary data. Physical contortion is distinct from the auxiliary jet connection. An omitted cosmological term does not affect this fixed-tetrad connection variation. Conventions and axial/trace coordinates are
\[
\eta=\operatorname{diag}(-1,1,1,1),\quad\epsilon_{0123}=+1,\quad
\omega=\mathring\omega+K,\quad T^a=de^a+\omega^a{}_b\wedge e^b,
\quad\kappa>0,\quad b,\zeta\in\mathbb R,
\]
\[
A^r=-\frac16\epsilon^{rabd}K_{abd},\qquad
V^a=\frac13\sum_b K^{ab}{}_b,\qquad X\cdot Y=\eta_{ab}X^aY^b.
\]
Declare an external axial source with fixed normalization. It is not a derived UBT current or another fundamental field. In natural units the contortion coordinates have inverse-length dimension, the source has inverse-length-cubed dimension, and kappa has length-squared dimension. The comparator is
\[
S=\frac1{4\kappa}\int\epsilon_{abcd}e^a\wedge e^b\wedge R^{cd}
+\frac1{2\kappa}\int(bH+\zeta Q_T)+\int\nu_e J\cdot A,
\quad H=e_a\wedge e_b\wedge R^{ab},\quad Q_T=T_a\wedge T^a.
\]
The extra coefficient multiplies an already allowed torsion invariant in the [restricted operator inventory](physics_closure_action_family_2026_10.en.md); all other torsion coefficients are fixed to zero in this comparator. Leaving it free tests identifiability and does not adopt another canonical action.

<!-- BILINGUAL-UNIT: physics-closure.spin-source.boundary -->
## Bulk equivalence with fixed boundary data

The Nieh–Yan identity and a constant coefficient shift give
\[
d(e_a\wedge T^a)=Q_T-H,\qquad
bH+\zeta Q_T=(b+\zeta)Q_T-b\,d(e_a\wedge T^a),
\]
\[
\beta=b+\zeta,\quad(b,\zeta)\mapsto(b+\delta,\zeta-\delta),\qquad
\Delta S=-\frac{\delta}{2\kappa}\int d(e_a\wedge T^a).
\]
Thus the bulk equations, including sourced equations, depend only on the effective coefficient. Quantum equivalence and boundary-charge equivalence are not established. Spacetime-dependent coefficients invalidate this reduction.

<!-- BILINGUAL-UNIT: physics-closure.spin-source.variation -->
## Full connection variation

Expand curvature around the Levi-Civita connection and remove only the stated total derivative. In the verifier's coordinate order, with antisymmetric Lorentz pairs ordered lexicographically and the coframe index varying fastest, the exact pointwise Hessian is
\[
K^{ab}=K^{ab}{}_c e^c,\quad a<b,\qquad
\det\!\left(\frac{\partial^2\mathcal L}{\partial K\,\partial K}\right)
=\frac{256}{\kappa^{24}}(1+\beta^2)^{12}>0.
\]
Every independent contortion entry is varied. Invertibility concerns an algebraic auxiliary equation, not a physical Hamiltonian's positivity or a propagating-mode count. The following connection satisfies every component of the full Euler equation; its uniqueness follows from that determinant:
\[
K^{ab}=\epsilon^{ab}{}_{cd}A^ce^d+V^ae^b-V^be^a,\qquad
\mathcal L_{A,V}=\frac3\kappa(A^2-V^2-2\beta A\cdot V)+J\cdot A,
\]
\[
A_*=-\frac{\kappa J}{6(1+\beta^2)},\qquad
V_*=\frac{\kappa\beta J}{6(1+\beta^2)},\qquad
\mathcal L_{\rm contact}=-\frac{\kappa}{12(1+\beta^2)}J^2.
\]
The tensor part is therefore eliminated by the full equation rather than discarded before variation. A nonzero known source allows the axial/trace ratio to distinguish the effective coefficient's sign; the contact coefficient alone is even. A physical fermion interaction still requires the normalized source and complete composite variation to follow from the same action.

<!-- BILINGUAL-UNIT: physics-closure.spin-source.information -->
## Information and shared records

For a differentiable regular statistical model whose bulk-record likelihood depends only on the effective coefficient,
\[
p(D\mid b,\zeta)=p(D\mid\beta),\quad
\partial_b\log p=\partial_\zeta\log p,\quad
I=I_\beta\begin{pmatrix}1&1\\1&1\end{pmatrix},\quad
I\begin{pmatrix}1\\-1\end{pmatrix}=0.
\]
Additional shared bulk records can improve the effective combination's precision, but cannot distinguish equal likelihoods. A boundary-sensitive protocol or an independently justified coefficient constraint could change this conclusion. Causality, information capacity and consistent shared records alone do not select the separate Holst coefficient here. No new shared-reality axiom is introduced.

<!-- BILINGUAL-UNIT: physics-closure.spin-source.verification -->
## Verification and remaining microscopic task

`tools/verify_holst_spin_source.py` passes **67** symbolic checks. A separate NumPy tensor contraction assembles and solves the full connection system in **12** seeded samples. The new pytest suite passes **68** cases. Numerical acceptance uses
\[
\varepsilon_{\rm numeric}=10^{-11}.
\]
`formal/lean/UBT/Hamiltonian/HolstSpinSource.lean` encodes the coefficient shift, normalized stationary response, on-shell contact and sign identities. **LEAN-PENDING:** no local Lean runtime is installed; compilation and the existing axiom audit in fresh CI are required before a formal verification claim. The full exterior-form variation, functional/boundary argument and statistical interpretation are outside those finite lemmas. Evidence is in `reports/holst_spin_source_2026_10_29.json`.

The sourced Holst mechanism has established antecedents, including [Freidel–Minic–Takeuchi](https://arxiv.org/abs/hep-th/0507253); the source normalization here is declared, not identified with theirs. The repository contribution is a full-component executable diagnostic and an explicit identifiability boundary in the already allowed action class. Deriving the source, torsion coefficients and physical constraint reduction from the same single-Theta action remains open. No UBT recovery gap or provenance tier is promoted. Independent bilingual semantic review remains required before merge.
