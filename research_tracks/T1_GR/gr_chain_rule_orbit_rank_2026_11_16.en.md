<!-- BILINGUAL-UNIT: gr-chain-rule-rank-2026-11-16 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional research; not a theorem for the full composite biquaternionic theory.
UBT-AI-PROVENANCE-END
-->
# Connection chain-rule rank and protected stabilizer equations

<!-- UNIT: scope -->
## Scope and hypothesis
[RESEARCH / CONDITIONAL] Analyze the canonical covariant-tetrad relation for an independently varied Lorentz connection, on the real Lorentz-vector slice Theta=X and X^2!=0. This is a tangent-space diagnostic, not the fully self-consistent connection-reconstructed Theta-only variation. Canonical metric and field axioms are unchanged.

<!-- UNIT: chain -->
## Composite variation
```text
E_mu = N0^(-1/2) D_mu^omega Theta
delta_omega S_composite = (delta S/delta omega)|_E + (delta S/delta E_mu) delta_omega E_mu
delta_omega E_mu = N0^(-1/2) (J_ab Theta) delta omega_mu^ab
For Theta=X in W_L: (J_ab X)^c = delta^c_a X_b - delta^c_b X_a
L_X: so(1,3) -> R^(1,3),  Lambda -> Lambda X
rank L_X=3 and dim ker L_X=3 for X^2!=0
for independent mu slots: rank=12, kernel=12
```
Here delta S/delta E is the full tetrad Euler derivative treating E and omega provisionally independent, including integrations by parts. The direct fixed-E connection current alone is not the composite current. In the exact two-sided biquaternion representation, J_ab must be replaced with the matched left/right generator and all reality conditions checked.

<!-- UNIT: lemma -->
## Conditional Lorentz-orbit rank lemma
For a non-null Lorentz four-vector X, the image of L_X consists of the 3-dimensional hyperplane X-perpendicular, and the kernel is the 3-dimensional stabilizer Lie algebra of X. For four independent spacetime slots the chain-rule map from 24 Lorentz connection variations to 16 tetrad variations has rank 12 and kernel 12. Thus connection Euler equations projected onto the stabilizer of X receive **no** chain correction: for each mu and any antisymmetric Lambda with Lambda X=0, the necessary condition is Lambda^{ab} C_{mu ab}=0, where C is the fixed-E connection Euler derivative. The other 12 components can receive a correction from the tetrad Euler derivative; no cancellation has been established. This rank count is not a physical DOF count and need not apply to all eight real components of generic complex biquaternionic Theta.

<!-- UNIT: interpretation -->
## Implications for A and B
B: compute the fixed-E current and its stabilizer projections on an actual on-shell background; if any protected projection is nonzero, an independent-omega composite stationary point there is impossible irrespective of chain terms. The canonical affine spin-source nonzero statement alone does not establish nonzero stabilizer projection. A: a compensating relative central/jet structure may change orbit rank, but must be derived, not inserted as a freely chosen selector. Neither branch is declared solved.

<!-- UNIT: implementation -->
## Verification and limit
Exact SymPy calculations on timelike X=(1,0,0,0), spacelike X=(0,1,0,0), and nontrivial timelike X=(2,1,0,0) give rank(L_X)=3, dim(kernel)=3 and X dot L_X=0. Reproducible checker: tools/verify_gr_chain_rule_orbit_rank_2026_11_16.py. General non-null result follows analytically because Lorentz generators span the orthogonal hyperplane. Full Theta Hessian, chained reconstruction, Lean, CI, and bilingual independent semantic checker remain pending.
