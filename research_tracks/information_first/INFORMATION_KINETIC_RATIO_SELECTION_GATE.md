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

# Information and complex-time selector test for a/b

**2026-10-26. Exact nonuniqueness counterexample, NOT the full UBT quantum Hamiltonian.** Extends BIQUATERNION_KINETIC_SELECTOR_METRIC_LOCK.md.

Take two independent canonical real oscillators (representatives of singlet and one colour-direction) with q=(q_s,q_t), p=(p_s,p_t), mass-matrix/kinetic coefficients a,b>0:
 H_{a,b}=p_s²/(2a)+p_t²/(2b)+(a omega_s² q_s²+b omega_t² q_t²)/2.
This is bounded below and invariant under independent phase-space rotations in each normalized oscillator plane; a full SU(3) triplet is obtained by repeating the same b coefficient for three complex directions. Fix omega_s=omega_t=omega>0. For every positive a,b the uncoupled ground state is a product pure state, with entanglement entropies S(s)=S(t)=0 and mutual information I(s:t)=0. The same equal-time entropy and negentropy values cannot distinguish a/b. Distinct a/b do change dimensionful field quadrature correlators, e.g. ground-state <q_s²>=hbar/(2a omega) and <q_t²>=hbar/(2b omega), so a calibrated observable algebra plus state and preparation can infer a/b; it is NOT predicted by the shared-negentropy identity alone.

More sharply, a local canonical squeezing q_s->lambda_s q_s, p_s->p_s/lambda_s transforms a into a' =a lambda_s² in kinetic form while preserving the canonical symplectic structure. Similarly for b. Thus a/b by itself can depend on field normalization absent a fixed geometric Theta norm and observable identification. UBT's h(Theta) and metric lock may make relative normalization meaningful, but this must be proved in physical reduced variables before asking information to select a number.

For any constant real a,b>0, a free linear equation with analytic coefficients permits a holomorphic extension to complex time tau=t+i psi on appropriate local patches. Cauchy–Riemann analyticity alone imposes no a=b relationship. If psi is compact there are further spectral/boundary compatibility conditions; they do not follow from holomorphy alone. The Jacobi period-two transformation acts on the modular lattice variable tau_J, not canonically on physical tau_UBT.

**Consequence:** neither global SU(3) + involutions + analyticity nor the mere multipartite negentropy identity selects a/b. A nontrivial information selection rule would need a derived specific correlation functional with known physical normalization and calibrated observer dynamics; extremizing it is a NEW postulate unless it follows from a separate theorem. Existing composite-metric collapse leaves this issue even if a/b were somehow selected.

Regression: tests/test_information_kinetic_ratio_no_selection.py.
