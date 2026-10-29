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

# Algebraic two-carrier obstruction to a third Lorentz vector

**2026-10-26. Exact conditional equivariance theorem.** Let v be timelike and w linearly independent in a real Lorentz four-vector representation. Consider a Lorentz-equivariant map F(v,w) yielding another Lorentz four-vector, using only v,w, eta, epsilon and scalar algebraic operations (including invariant scalar functions), and no derivatives, external frames, extra fields or spontaneous branch choices that break the stabilizer.

The common stabilizer of v,w in the proper orthochronous Lorentz group is SO(2). By equivariance, any h fixing v,w obeys hF(v,w)=F(hv,hw)=F(v,w). The fixed-vector subspace of this SO(2) is precisely span{v,w}. Hence F(v,w)=a(v²,w²,v·w)v+b(v²,w²,v·w)w. It cannot supply a third independent vector. Epsilon contractions with only v,w cannot provide an independent four-vector without extra independent directional input.

Thus the three-vector zero-kernel condition in PR #787 is algebraically sound but **not automatically attainable** from the two real four-vectors in one biquaternion. Derivative-dependent composites can in principle break the SO(2) stabilizer at some points, yet no nonvanishing, dynamically compatible third direction has been derived. In flat Lorentz-invariant or rotationally symmetric configurations a proposed construction may vanish or degenerate. Nor may an arbitrary local frame choice be mistaken for an invariant dynamic selector.

This is an obstruction only for algebraic equivariant F(v,w), NOT a no-go for the full eight-real differential carrier. It leaves the final action and Hamiltonian open.

Test: tests/test_two_carrier_third_vector_no_go.py verifies a nontrivial SO(2) generator's fixed kernel equals span{v,w} in an adapted frame.
