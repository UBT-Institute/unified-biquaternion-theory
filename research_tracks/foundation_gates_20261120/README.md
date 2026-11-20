<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: pending
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Research tests, not canonical physics claims.
UBT-AI-PROVENANCE-END -->

# Three foundation gates — 2026-11-20

These are **bounded reproducible algebraic checks**, not closure of GR, the Standard Model, or quantum foundations.

## Gate S: metric signature (no-go for kinematic selection)

Canonical real Lorentz tetrad e defines g=e^T eta e, eta=diag(1,-1,-1,-1). If det(e) != 0, Sylvester's law of inertia implies inertia(g)=(1,3) for every e. Thus **sampling tetrads already restricted to the Lorentz slice can never discover why the Lorentz signature is preferred**. It merely reasserts the input. To test emergent signature statistically, first define a signature-unrestricted real extraction map g[Theta], its allowed domain, a measure on Theta, and an action/weight. No UBT probability such as 85% is justified before these are fixed. The Regge toy-model percentage cannot be transplanted.

Reference: Djordjevic, Prlina, Vojinovic, arXiv:2610.31776 (2026), https://arxiv.org/abs/2610.31776 .

## Gate H: Hermitian complex-quaternion orientation

Let n in C^3, n.n=1 (complex bilinear). Write n=u+i v: u.u-v.v=1 and u.v=0. The Hermitian sigma kinetic metric induced from the ambient Euclidean metric on (u,v) is positive on every nonzero tangent vector. In a regular patch it has four real scalar modes before further constraints. This does NOT show coupled UBT ghost freedom or a correct gauge representation.

Important obstruction: the positive Hermitian form is not invariant under full active SO(3,C). Example n(t)=(cosh t,i sinh t,0) has n.n=1 but bar(n).n=cosh(2t). A complex orthogonal boost changes the Hermitian norm. Hence a positive definite SO(3,C)-invariant fiber metric cannot be assumed without additional reality structure / compensator.

Reference: Ito, Nago, Tanigawa, arXiv:2604.19415v3 (2026), https://arxiv.org/abs/2604.19415 . Their classical graded-SYM stability does not imply UBT stability.

## Gate Q: exact qubit identity

For rho=(I+s.sigma)/2, real |s|<=1, and A=a.sigma, B=b.sigma, a,b real, define c=a cross b. Then
Var(A)=|a|²-(a.s)²,
Var(B)=|b|²-(b.s)²,
Cov(A,B)=a.b-(a.s)(b.s),
|<[A,B]>/(2)=|c.s|.
An exact algebraic identity is

Var(A) Var(B) - Cov(A,B)^2 = (c.s)^2 + (1-|s|²)|c|².

Thus the usual Robertson–Schrodinger bound leaves a nonnegative mixed-state remainder. The equality is a **standard qubit algebra identity**; comparison to the exact formula and normalization of Kimura et al. is a separate literature check. The map rho_Theta=Theta Theta^dagger/Tr(Theta Theta^dagger) is a standard positive qubit state whenever Theta!=0; reproducing the identity is not a prediction or independent confirmation of UBT.

Reference: Kimura et al., npj Quantum Information (2026), https://doi.org/10.1038/s41534-026-01374-0 .

## Unclosed dependencies and falsification

1. S: construct signature-unrestricted g[Theta] with nondegenerate configurations of multiple signatures; if impossible within canonical UBT, document this as a structural no-go, not a probabilistic result.
2. H: calculate full coupled UBT Dirac constraints and physical kinetic Hessian, with left/right connections, reality constraints, and residual SO(2,C) mode. The simple sigma positivity does not close this.
3. Q: verify exact published stronger uncertainty relation and formalize qubit identity in Lean; numerical checks are not formal proofs.
4. Check canonical compatibility: metric-rank ten, tetrad integrability, covariance of J(Theta) under two-sided gauge transformations. Do not silently replace canonical geometry with the diagonal subgroup.

Execute: `python3 research_tracks/foundation_gates_20261120/check_gates.py`.
