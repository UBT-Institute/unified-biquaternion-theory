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

# Hamiltonian audit: Theta orientation and an auxiliary diagonal connection

## Scope and warning

This note tests the candidate action `L=(kappa/2) eta^{mu nu} Sc[(D_mu Theta)^dagger D_nu Theta]`, `kappa>0`, `eta=diag(+---)`, `D_mu Theta=partial_mu Theta+[C_mu,Theta]`, on a fixed Minkowski background. Theta and C are independent complex-biquaternion fields, but the central part of C is redundant. This is **not** the canonical UBT action, nor a full Dirac analysis of the canonical tetrad. Full local SO(3,C) is NOT a symmetry of this Hermitian norm; a positive Hermitian metric picks a reality structure. Consequently one must not call the entire complex C a gauge connection with first-class constraints before checking the action's symmetry.

## Exact algebraic results

Write `Theta=z0+r J`, `J^2=-1`, `r!=0`, in a regular patch, and at a point take `J=e3`. For `C_mu=c1 e1+c2 e2+c3 e3`,
`[C_mu,J]=2(c2 e1-c1 e2)`.
The stabilizer component `c3 J` and the center commute with Theta. Thus **they drop out of the matter covariant derivative**, and no propagating residual photon can be deduced from the Theta kinetic term alone.

Let the 8 real coordinates of Theta be q^A. The Lagrangian time dependence is `L_time=(kappa/2) sum_A (dot(q^A)+K^A(C_0,q))^2`. In these Cartesian field coordinates, `W_AB=d²L/dot(q^A)dot(q^B)=kappa delta_AB>0`; all connection components have **zero velocity Hessian**, since no dot(C_mu) occurs. Hence there are primary vanishing canonical momenta for C_mu, and the connection is nonpropagating in this toy action. This is only a **primary-constraint** statement. Secondary constraints, their rank and first/second class nature require the full Dirac algorithm; no physical DOF count is claimed here.

The pointwise Hermitian scalar norm is positive, but after eliminating C_0, or coupling gravity, a positive reduced Hamiltonian has **not** been established.

## Local orientation compensation

For any smooth J with J²=-1, the derivative X_mu=partial_mu J anticommutes with J. The algebraic choice
`C_mu^perp = -(1/4)[J,partial_mu J]`
satisfies
`partial_mu J+[C_mu^perp,J]=0`
because `[[J,X],J]=4X` for `{J,X}=0`. Thus, absent a separate curvature term, the connection can locally compensate orientation gradients. This illustrates why treating the isolated sigma-model's four real orientation coordinates as automatically propagating physical DOF is unjustified once C is varied. Whether the compensation is a gauge symmetry depends on the full action and its reality conditions.

## Reality/gauge obstruction

Complex-orthogonal rotations preserve `n.n` but do not preserve `bar(n).n`. For example `n(t)=(cosh(t), i sinh(t),0)` obeys `n.n=1` but has Hermitian norm `cosh(2t)`. Thus the proposed Hermitian kinetic term is not invariant under general active SO(3,C). This rules out inferring first-class SO(3,C) Gauss constraints solely from formal covariance of D.

## What an F² term changes

If one adds `-1/(4g²) Re Tr(F_mu_nu^dagger F^{mu nu})` with a carefully chosen positive internal pairing, velocities of spatial C_i enter through F_0i. This changes the primary constraint structure and may introduce propagating connection modes. However, the Hermitian pairing is generally not invariant under noncompact SO(3,C) gauge transformations, so one must derive the physical real form / compensator first. A formally positive quadratic expression is not a proof of consistent gauge-invariant, ghost-free UBT.

## Required next closure

1. Start from the actual canonical two-sided `D_mu Theta` and metric `g_mu_nu=Sc(E_mu^sharp E_nu)` on its specified Lorentz slice.
2. Obtain the complete Lagrangian including connection curvature and multipliers, not a guessed kinetic term.
3. Perform a 3+1 split, calculate the full Hessian and primary/secondary constraints, classify first-/second-class constraints, and count physical modes.
4. Check preservation of the canonical rank-ten tetrad map and integrability; do not infer it from unconstrained pointwise first jets.
5. Derive a real, gauge-compatible internal metric or demonstrate a no-go for the proposed complex residual field.
