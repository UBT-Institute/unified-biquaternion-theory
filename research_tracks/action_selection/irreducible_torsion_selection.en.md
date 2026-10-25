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

# Irreducible torsion decomposition and Hamiltonian selection gates

**Exact 4D Lorentz-tensor algebra, 2026-10-25; not a derived torsion equation or Hamiltonian.** Continues #742/#743 and relates to current flux #728/#729.

Use \(T_{abc}=-T_{acb}\), real Lorentz metric \(\eta_{ab}=(-,+,+,+)\). Define its trace \(t_b=T^a{}_{ab}\), totally antisymmetric component \(A_{abc}=T_{[abc]}\), and vector piece
\[
V_{abc}=\frac13(\eta_{ab}t_c-\eta_{ac}t_b).
\]
Then define \(Q_{abc}=T_{abc}-V_{abc}-A_{abc}\). Direct contractions give
\[
Q^a{}_{ab}=0,\qquad Q_{[abc]}=0,\qquad
T=V+A+Q.
\]
The independent real component dimensions are respectively **4+4+16=24**; A can be Hodge-dualized to an axial 4-vector in oriented Lorentz geometry. These are irreducible under the proper Lorentz group (the tensor piece is 16 real dimensions); their vanishing is NOT a theorem of UBT dynamics.

For any current satisfying the torsionful covariance conventions of #728, the density-flux mismatch depends on t via
\[
\nabla_\mu j^\mu=e^{-1}\partial_\mu(ej^\mu)+t_\mu j^\mu.
\]
So pure axial torsion (t=0,Q=0) is *sufficient* to remove this specific flux obstruction; it is not selected by the locked Theta axioms. The exact integrating-factor gate of #729 depends only on the one-form t. Nor do either condition constrain the remaining 16 tensor components.

**Hamiltonian selection implication:** metric compatibility reconstructs the connection from a *given* T but does not choose t, axial A or Q. One should derive from the single-Theta equations what each of the 4+4+16 components does, check composite A_mu,B_mu admissibility, and compute constraints and propagating characteristics. Declaring Q=0, t=0, or an axial torsion equation would add an independent restriction absent a proof; a special sector may be studied clearly labeled conditional.

Exact algebra regression: tests/test_irreducible_torsion_projection.py. No locked axiom changes.
