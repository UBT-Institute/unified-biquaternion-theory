<!-- BILINGUAL-UNIT: gr-volume-chain-source-2026-11-17 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact direct volume variation on a restricted Lorentz slice; full implicit dynamics open.
UBT-AI-PROVENANCE-END
-->
# Volume-locked Theta spin source: direct chain rank collapses to the vector image

<!-- UNIT: scope -->
## Exact scope, not a complete GR proof

This note refines the earlier formal rank-15 chain-source counterexample by restricting the parent tetrad Euler force to the **actual locked kinetic volume functional**. We use only the Lorentz-vector subbranch Theta=X in W_L and a metric-compatible Lorentz connection with a direct connection variation at fixed Theta. No claim for generic eight-real Theta or the full implicit composite solution.

<!-- UNIT: equations -->
## Derivation and exact rank witness

E_mu^a=N0^(-1/2)(D_mu Theta)^a; g_mu_nu=eta_ab E_mu^a E_nu^b
S_kin[Theta]=2 N0 int d^4x det(E)  (admissible Lorentz-real branch)
p_a^mu := delta S_kin/delta E_mu^a = 2 N0 det(E) (E^-1)_a^mu
delta_omega E_mu^a=N0^(-1/2) delta omega_mu^a_b X^b (Theta=X in W_L)
delta_omega S_kin = 2 sqrt(N0) int det(E) (E^-1)_a^mu X_b delta omega_mu^(ab)
=> direct J^mu_ab proportional (E^-1)_[a^mu X_(b] (pure-vector frame type)
At E_mu^a=delta_mu^a: rank(C)=4, rank(L)=12,
rank([C,L^T])=15 for arbitrary tetrad force p, BUT L^T p_volume=C X.

For the implicit self-consistent composite:
E=J(Theta,E,K), A=I-J_E,
delta_K S_red = J_K^* (A^*)^(-1) p_volume + (S_other)_K terms
(with actual boundary, gauge and source assumptions).


<!-- UNIT: interpretation -->
## Why ranks 4 and 15 are compatible

The map from 16 possible tetrad-force slots to 24 connection-force slots has rank 12 for fixed nonnull X; the formal union with the four-dimensional pure-vector source image has rank 15 at the displayed flat point. But the volume action generates only one specific tetrad force p_a^mu proportional to the inverse coframe. Its direct chain contribution is pure vector, lying inside the rank-four image. The previous rank-15 result was a statement about arbitrary possible parent Euler forces, not a prediction that this action populates them. Neither rank is a physical propagating DOF count. Rewriting the constrained kinetic action as the volume must be done before restricting variations; adding a separately computed unconstrained fixed-E kinetic spin current to the volume-chain current would double-count incompatible variational descriptions.

<!-- UNIT: implicit -->
## Missing indirect Levi-Civita response

In the physical torsionful architecture, E is implicit in omega_LC(E)+K. Its linearization has a differential A=I-J_E and the true reduced variation contains J_K^*(A^*)^-1 p_volume, plus Euler derivatives of other action terms. In general (A^*)^-1 p_volume need not be pointwise proportional to p_volume, so the rank-four conclusion cannot be carried to the full constrained action. In a frozen translation-invariant approximation, A has derivative-only action and constant-coefficient p may simplify, but this is not a global PDE result: the affine Theta background and lambda(x) vary in space. A successful test must determine the adjoint inverse, solvability conditions, local Lorentz/diffeomorphism quotient and on-shell source manifold.

<!-- UNIT: selection -->
## Action-selection obstruction remains

On the classical central-metric constraint the quadratic Theta kinetic contraction equals 2 N0 sqrt(-g) and does not generate a standalone Einstein-Hilbert term. The existing canonical action audit identifies Hilbert-Palatini as imported. The direct rank-four result therefore does NOT deliver a graviton, a physical vacuum, an action selector or a Newton coefficient. To finish the theory without an ad hoc gravity term requires an independently derived microscopic or quantum effective principle with a positive, two-polarization graviton and consistent matter couplings.

<!-- UNIT: verification -->
## Verification and repo integration

Executable exact rational witness: tools/verify_gr_volume_chain_source_2026_11_17.py; verified locally with SymPy for rank 4, rank 12, formal rank 15, and exact equality of the direct volume-source and C X at timelike sample X. It is not a test of the real eight-component carrier, implicit A inverse, Lean, complete CI, or physical constrained Hessian. Preserve as research C_working and keep PR draft.
