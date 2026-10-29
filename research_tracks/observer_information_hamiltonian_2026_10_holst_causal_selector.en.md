<!-- BILINGUAL-UNIT: holst-causal-selector -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Exact obstruction: causal Clifford cones cannot by themselves select the Holst coefficient

<!-- BILINGUAL-UNIT: inputs -->
## Canonical inputs and status
The already existing `research_tracks/action_selection/clifford_palatini_trace_selector.en.md` identifies two independent Lorentz-invariant curvature-linear contractions of the canonical Clifford tetrad: graded Palatini and ungraded Holst. `canonical/geometry/biquaternion_dirac_lift.tex` proves the Clifford anticommutator. The following deduction is an exact **restricted torsion-free comparison**, not a unique microscopic UBT action.

<!-- BILINGUAL-UNIT: proof -->
## Torsion-free identity and causal underdetermination
$$S_{\beta}[e,\omega]=S_{\mathrm P}[e,\omega]+\beta\int e^a\wedge e^b\wedge R_{ab}[\omega],$$
$$T^a=0\ \Longrightarrow\ e^a\wedge e^b\wedge R_{ab}=0,$$
$$d(e_a\wedge T^a)=T_a\wedge T^a-e_a\wedge e_b\wedge R^{ab}.$$
For the torsion-free Levi--Civita connection, $T^a=0$ and the first Bianchi identity (equivalently the Nieh--Yan identity) gives $e^a\wedge e^b\wedge R_{ab}=0$ pointwise. Therefore the full restricted functional $S_\beta[e,\omega_{\mathrm{LC}}(e)]$ is independent of $\beta$ for any smooth invertible tetrad. Its **restricted variations and linearized equations** are likewise independent of $\beta$, hence cannot be distinguished by their gravitational principal symbols, causal characteristics, operational observer capacity, or shared-record consistency as long as those tests are confined to this branch. Independently the Clifford Dirac-type principal symbol $P(k)=\Gamma^\mu k_\mu$ is connection-independent when the connection occurs at differential order zero. Its determinant $\det P(k)=(g^{\mu\nu}k_\mu k_\nu)^2$ does not select $\beta$ either.

<!-- BILINGUAL-UNIT: nuance -->
## Off-shell torsion caveat
This statement is **not** the assertion that the full Palatini--Holst theory is identical for all $\beta$ when the connection is varied freely or torsion exists: the Holst term can alter connection/torsion equations, matter couplings and boundary terms. Under the canonical pure-pair torsionful branch or split-jet completion, those terms must be computed before drawing physical conclusions. The first-order torsionless comparison is a counterexample to the claim that symmetry and causal-cone constraints automatically yield a unique action.

<!-- BILINGUAL-UNIT: next -->
## Concrete next proof gate
Compute the exact canonical paired-connection curvature representation in the Clifford carrier; calculate its torsionful graded/ungraded trace actions and full composite variations; constrain the $\psi$ grading by an independently derived phase/chirality rule; test whether any physically measurable torsion observable or shared-record consistency genuinely distinguishes the two invariant channels. **STATUS: conditional exact no-selection theorem; full-$\Theta$ Hamiltonian OPEN; LEAN-PENDING; bilingual semantic review PENDING.**

<!-- BILINGUAL-UNIT: selfdual-domain -->
## Standard identity and the separate complex matching question

The torsion-free Holst/Nieh–Yan identity is a standard result, not new UBT physics. The restricted causal no-selection deduction concerns protocols on the same torsion-free metric branch. The [closure audit](action_selection/physics_closure_2026_10.en.md) separately verifies a GR FLRW canonical match at $b=\pm i$ after complex continuation and an added GR-matching requirement. This does not refute the restricted deduction: it changes both the hypotheses and the coefficient domain. Moreover the original Hermitian paired derivative no longer generates the assumed tetrad under the naive continued rotation. The complex branch requires its own action-derived reality conditions and full variation. No claim that all possible stronger principles can never select a coefficient is made here.
