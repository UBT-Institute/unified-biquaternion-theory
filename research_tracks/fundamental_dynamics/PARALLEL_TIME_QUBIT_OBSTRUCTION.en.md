<!-- BILINGUAL-UNIT: parallel_time_qubit_obstruction -->
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

# No parallel field-derived time-qubit projectors on the nondegenerate classical vector branch

**Status:** exact conditional local obstruction, 2026-10-26; NOT a no-go for full complex UBT, unconstrained two-sided connections or a physical qubit experiment. English is the translation source; Czech is a matched working translation.

## Assumptions

Take the restricted pure Lorentz-vector realization of the canonical covariant tetrad. Let V and W be two real Lorentz vectors, with V future timelike and W independent of V. The classical-reality restriction is DW=0, while DV=sqrt(N0)e is an invertible tetrad. The Lorentz connection preserves the Hermitian spinor identification H of Minkowski vectors. No independent field is introduced.

## Pointwise construction

At an arbitrary point choose a Lorentz frame and a normal spin gauge where the connection one-form vanishes at that point. Write

\[
V=(r,0,0,0),\quad W=(w_0,s,0,0),\quad r>0,\ s>0,
\]
\[
S=W-\frac{V\cdot W}{V^2}V,\quad N=\mathcal H(V),\quad B=\mathcal H(S),
\]
\[
Q=\sqrt{-\frac{\det N}{\det B}}N^{-1}B,\quad
P_\pm=\frac{I\pm Q}{2}.
\]

Here N is positive Hermitian, S is nonzero spacelike, Q²=I, and the P projectors are complementary. Covariant nonvanishing is frame-independent.

## Theorem and proof

Invertibility of DV supplies a tangent X with image in the internal y direction. Using DW=0 in the normal gauge gives

\[
D_XV=(0,0,a,0),\quad a\ne0,\quad D_XW=0,
\]
\[
D_XN=a\sigma_2,\quad D_XB=-\frac{w_0}{r}a\sigma_2,
\]
\[
\boxed{D_XQ=\frac a r\left(i\sigma_3-\frac{w_0}{s}\sigma_2\right)\ne0.}
\]

Use sigma2 sigma1=-i sigma3 and observe that the determinant normalization has zero first variation along this transverse direction. The diagonal matrix entry (D_X Q)11=i a/r cannot vanish. Consequently DQ=0 contradicts full rank of DV whenever the stated conditions hold.

## Consequences and scope

The projectors remain valid algebraically and Lorentz covariantly at a point. Parallel transport of these particular projectors is impossible with DW=0 and nondegenerate DV. The result does not exclude transitions between sectors, a more general left/right connection, off-slice holomorphic dynamics, null V, degenerate e, or other projector definitions. This does not derive any optical probability or UBT action.

**Action/Hamiltonian gate:** a physical two-sector UBT dynamics must either use a different transport law or explain why the projectors need not be parallel. A trial H0±V_int is not a derived Hamiltonian without action-level selection.

## Verification

Exact SymPy regression in research_tracks/fundamental_dynamics/tests/test_parallel_time_qubit_obstruction.py checks Q²=I, transverse derivative, full-rank reachability and the Pauli multiplication. Four focused tests passed locally.
