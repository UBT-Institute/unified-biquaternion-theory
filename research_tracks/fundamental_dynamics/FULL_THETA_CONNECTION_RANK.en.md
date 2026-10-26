<!-- BILINGUAL-UNIT: FULL_THETA_CONNECTION_RANK -->
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


# Full complex biquaternion: fixed-Theta Lorentz-connection response rank

**2026-10-26 | integrated Fundamental Dynamics, local linear algebra; NOT full two-sided composite closure or an action.** Compare restricted vector-carrier #776.

For the SL(2,C) metric-compatible congruence branch (the trace-free, no-Weyl-dilation part of the Lorentz-real two-sided classification #762), consider a *general complex* invertible Theta in M2(C), NOT restricted to W_L. At each spacetime index the real-linear map
\[
L_\Theta:\mathfrak{sl}(2,\mathbb C)\longrightarrow M_2(\mathbb C),\quad
a\mapsto a\Theta+\Theta a^\dagger
\]
has a 6-real-dimensional domain. Compute its 8x6 real matrix using the three Pauli matrices sigma_j/2 and i sigma_j/2.

**Exact witness calculations using rational complex entries:** rank(L_{iI})=3, rank(L_I)=3, rank(L_{diag(1,i)})=5, rank(L_{[[1,2+i],[3-i,2i]]})=5. Hence the kernel has dimensions 3,3,1,1 respectively. This is not a proof of a universal generic-rank theorem; the examples establish that the restricted 12-function kernel from real vector-lift cannot be carried over indiscriminately to fully general Theta. For a fixed Theta, the four independent spacetime-index copies of this algebraic kernel in these witnesses have 12 or 4 real dimensions respectively before any composite/torsion/gauge constraints.

**Exact invariants:** A finite congruence Theta'=S Theta S†, S∈SL2(C), preserves det Theta. For invertible Theta, Q=Theta^{-1}Theta† transforms by Q'=(S†)^{-1} Q S†, hence tr Q is another invariant. These invariant restrictions help explain the rank deficiency. They do NOT uniquely reconstruct A[Theta] or determine dynamics, torsion or physical DOF.

**Critical reality/covariance caution.** The locked tetrad demands D_mu Theta∈W_L, so a generic variation a Theta+Theta a† need not itself lie in W_L when Theta is outside W_L. The map above is the ambient connection response, not the full rank of the constrained implicit system F=0. Imposing reality, composite reconstruction and holomorphic/psi constraints may change allowed directions. The trace central part and right representation require separate treatment if included; no claim that the SL2 congruence branch exhausts canonical UBT.

Next calculation: intersect image L_Theta with allowed anti-Hermitian tetrad response, then include derivative response of Theta and enforce all four tetrad reality equations. Only a selected torsion law and microscopic action permit a propagating graviton/physical Hamiltonian test.
