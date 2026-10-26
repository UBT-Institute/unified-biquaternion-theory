<!-- BILINGUAL-UNIT: chirality_projector_naturality -->
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


# Chirality projectors: a naturality obstruction in Mat(2,C)

**2026-10-24. Conditional algebraic theorem, not fundamental Hamiltonian selection.** Follow-up to draft #722. Do not change locked UBT axioms.

Let A=M_2(C) and demand an *intrinsic right-multiplication chirality operator* Gamma=R_G, Gamma(X)=XG, for a fixed complex matrix G satisfying Gamma²=1. Under arbitrary right frame changes X↦XV, V∈SL(2,C), require chirality to be unchanged: Gamma(XV)=Gamma(X)V. Then VG=GV for all V, so G lies in the commutant of the fundamental SL(2,C) representation. That commutant is C·I₂ (Schur's lemma; alternatively the generators sigma1 and sigma3 suffice). Thus G=zI₂; G²=I₂ implies z=+1 or -1. Therefore P±=(I±G)/2 are only (I,0) or (0,I): **no nontrivial intrinsic pair of rank-one right projectors exists under unrestricted right SL(2,C) frame symmetry**.

The projector pair in #722, P_L=diag(1,0), P_R=diag(0,1), corresponds to a choice G=diag(-1,+1), which breaks the unrestricted right-frame change to the stabilizer of G (diagonal subgroup). That is a valid **candidate additional structure or gauge fixing**, but not an output of the bare algebra alone. The theorem is specifically about *fixed right multiplication* projectors and unrestricted right-frame naturality. If the right module is not a physical symmetry of UBT, this no-go does not apply as a physical requirement; the actual permitted right gauge group must be identified from locked covariant derivative data.

**Other possible route, not yet demonstrated:** chirality grading in the full even spacetime Clifford representation with a volume pseudoscalar, or a graded module induced from the actual covariant tetrad/Spin(1,3) connection. Such a grading must be defined on the correct carrier, preserve the real Lorentz metric slice and be compatible with the first-order Hamiltonian and invariant symplectic pairing. It is not enough to identify the commuting imaginary unit i with gamma5: multiplication by i obeys J²=-1 as a *real* operator, not a nontrivial complex-linear involution, while i·J=-I is trivial.

**Falsification/next gate:** derive the actual right gauge symmetry of Theta from the canonical two-sided D_mu and determine whether it permits a nontrivial chirality projector; only then classify equivariant linear first-order Hamiltonian symbols. Do not add a gamma5-like degree of freedom or double the field without derivation.

Reproduction: python -m unittest discover -s research_tracks/action_selection/tests -p 'test_chirality_projector_naturality.py' -v.
