<!-- BILINGUAL-UNIT: shared-negentropy-correlation -->
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

# Shared reality: negentropy composition with quantum correlations

**2026-10-26. Mathematical benchmark, not a derived fundamental UBT action.** Units k_B=1; finite-dimensional, disjoint tensor factors only. This extends `SHARED_REALITY_PRINCIPLE.md` and does not conflate independent observers with independent physical subsystems.

For Hilbert space dimension d_A, J(A)=log(d_A)-S(A), S(A)=-Tr rho_A log rho_A. For a joint state rho_AB, d_AB=d_A d_B:
  **J(AB)=J(A)+J(B)+I(A:B)**,
where I(A:B)=S(A)+S(B)-S(AB)=D(rho_AB || rho_A tensor rho_B)>=0 (relative entropy).
This is exact for *compatible reductions of one state*, not a new physical postulate. Mutually incompatible observer assignments need not have a common global state.

For three subsystems, recursively:
  **J(ABC)=J(A)+J(B)+J(C)+I(A:B)+I(AB:C).**
All two correction terms are nonnegative. However replacing I(AB:C) by I(A:C)+I(B:C) is generally WRONG: the difference is the tripartite interaction information, whose sign is not fixed. In general,
  J(A_1...A_n)=sum_i J(A_i)+sum_{k=2}^n I(A_1...A_{k-1}:A_k).
The chain depends on order in its individual mutual-information terms but the total does not. The chain decomposition is bookkeeping; it does not imply an extensive local gravitational action.

**Exact witnesses:**
- Bell singlet/pair on two qubits: S(A)=S(B)=ln2, S(AB)=0, so J(A)=J(B)=0 while J(AB)=2 ln2 and I(A:B)=2 ln2. Information may reside wholly in correlations.
- GHZ state (|000>+|111>)/sqrt2: each one-qubit entropy ln2, S(AB)=ln2, S(ABC)=0. The three single-qubit J vanish, while I(A:B)=ln2 and I(AB:C)=ln2, recovering J(ABC)=3 ln2. Pairwise I(A:B)=I(A:C)=I(B:C)=ln2; summing all pairs would give 3ln2, an overcount.
- Product maximally mixed state rho=I/d has J(global)=0 and zero correlations, yet is stationary under infinitely many distinct Hamiltonians H because [H,rho]=0. Thus even complete knowledge of this negentropy and correlations does not select a unique generator.

**Important gauge/gravity limitations:** Hilbert-space factorization for SU(3) Gauss-law and gravitational constraints is nontrivial, requiring subalgebras, centers/edge modes, and an entropy prescription. For overlapping algebras one cannot naively set d_AB=d_A d_B. Infinite-dimensional local QFT entropy needs a regulator; use relative entropy or suitable conditional mutual information where defined.

**Concrete UBT research gate:** (1) obtain a physical positive Theta state and compatible observer subalgebras; (2) compute relative-entropy/mutual-information terms for derived states, not assumed Bell/GHZ toys; (3) see if variations of the correlation functional constrain the same gravitational Noether charges as the chosen MM action; (4) demonstrate noncircular selection of couplings; (5) check Dirac/ghost stability separately. No entropy identity by itself gives Einstein equations, a unique action or levitation.

Regression: `tests/test_shared_negentropy_composition.py`.
