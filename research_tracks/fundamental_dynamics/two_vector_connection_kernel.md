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

# Two Lorentz vectors reduce the residual composite connection kernel 12 → 4

**26 October 2026 — exact pointwise algebraic theorem, conditional on the pure Lorentz-vector lift. Not an action, a torsion-selection law, or a physical mode-count claim.** Follows integrated PR #776 and the canonical time-qubit projector audit #778.

## The restricted two-vector problem

On an open patch with real Lorentzian internal metric eta, let v be nonnull timelike, and let w be a noncollinear real Lorentz vector. At each spacetime point and each world index mu, let u_mu and z_mu be prescribed real vectors. Seek an eta-skew Lorentz connection omega_mu satisfying

```
omega_mu v = u_mu,
omega_mu w = z_mu.
```

For a canonical Lorentz-vector lift one may use `u_mu=sqrt(N0)e_mu-partial_mu v`; for a parallel second component `D_mu w=0`, `z_mu=-partial_mu w`. Here `e_mu` is prescribed for the compatibility test; whether it is selected on shell by the single Theta dynamics is open.

## Necessary and sufficient compatibility

Because `omega^T eta+eta omega=0`, the following three scalar conditions are necessary, for each mu:

```
v·u_mu=0,
w·z_mu=0,
v·z_mu+w·u_mu=0.
```

They are also sufficient when `v²!=0` and `s=w-(v·w/v²)v` is nonzero. Since v is timelike, s is spacelike: `s²>0`.

Define the eta-skew rank-two endomorphism

```
M(a,b) = a tensor b_flat - b tensor a_flat
```

and first solve the v equation:

```
omega_v = M(u,v)/v²,  omega_v v = u.
```

Set `r=z-omega_v w`. The three scalar conditions entail `r·v=0` and `r·s=0`. Therefore

```
omega_0 = omega_v + M(r,s)/s²
```

is eta-skew and satisfies **both** `omega_0 v=u` and `omega_0 w=z`. The full solution is

```
omega_mu = omega_0,mu + C_mu,  C_mu v=0, C_mu w=0.
```

For timelike v, its stabilizer is SO(3). Fixing the independent spatial component s of w reduces it to SO(2). Consequently the homogeneous solution has exactly **one Lie algebra parameter per mu**, or **four arbitrary functions locally**, compared with 12 at fixed v alone in PR #776. The linear map `so(1,3)->(omega v,omega w)` has rank 5, kernel dimension 1.

This is a theorem about **kinematic underdetermination**, not four propagating connection degrees of freedom. It does NOT fix the remaining SO(2) curvature or torsion: a nonzero stabilizer-valued C can preserve v and w yet change connection curvature.

## Consequences of Dv=sqrt(N0)e and Dw=0

Metric compatibility gives the corresponding differential identities

```
partial_mu(v²) = 2 sqrt(N0) e_mu·v,
partial_mu(w²) = 0,
partial_mu(v·w) = sqrt(N0) e_mu·w.
```

These constrain admissible (v,w,e) triplets; they cannot be imposed on a prescribed arbitrary pair without checking integrability. Notice that if v·w vanishes *identically* on the patch and e is invertible, the third equation forces w=0. This does NOT exclude nonorthogonal w with a nonzero perpendicular projection s; e.g. the inertial Minkowski branch v=x, e=dx, w=constant works on timelike patches, with v·w varying in x.

Full holonomy remains a strong further obstruction. Parallel w is impossible if the chosen Lorentz connection has no nonzero invariant vector; for the specific FLRW torsionful representer, PR #778 derives w=0. A physical time-qubit sector cannot simply be deduced from the rank count.

## Why this matters for the UBT action and Hamiltonian

The second four-real slice component can **conditionally** reduce the residual Lorentz connection kernel from 12 to 4 functions without inserting any new independent field: w is already contained in the complex Theta. But classical Lorentz-reality forces Dw=0 and frequently removes w altogether. Even where w survives, neither these compatibility equations nor the Cartan/Bianchi identities fix the remaining stabilizer; a dynamical torsion selector or physical gauge quotient is still required before one may form the fully reduced action, its Legendre transform, or an invariant spin-2 Hamiltonian. The pure vector lift is not the general two-sided off-slice representation.

## Exact test

`tests/test_two_vector_connection_rank.py` checks constructive sufficiency and a nonzero SO(2) stabilizer using v=(2,0,0,0), w=(1,1,0,0), u=(0,1,2,0), z=(1/2,1/2,3,-1), with eta=(-,+,+,+). A symbolic linear map has rank 5; all four tests passed locally.
