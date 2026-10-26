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

# Covariant time-qubit algebra in canonical UBT: conditional constructions and obstructions

2026-10-26. **RESEARCH / CONDITIONAL MATHEMATICAL RESULTS.** No canonical action is postulated or modified. An algebraic qubit is not evidence of a physical qubit travelling backward through time.

## Canonical input and the reality constraint

Canonical source: `canonical/CANONICAL_DEFINITIONS.md`, sections 2 and 3. Let `B=H ⊗ C`, `J(X)=-conj(X^sharp)` and decompose `Theta=V+iW`, `JV=V`, `JW=W`. The central complex unit `i` is not a quaternion unit. Assume the **specific Lorentz-paired**, J-compatible connection `D` so `D(JX)=J(DX)`.

On the classical Lorentz slice, `E_mu=D_mu Theta/sqrt(N0)` is J-real, giving the **exact** equivalence

```
J(E_mu)=E_mu    <=>    D_mu W=0.
```

Thus `[D_mu,D_nu]W=F_mu_nu·W=0`. For a connection with no nonzero invariant vector under its full holonomy, `W=0`; exceptional holonomy may allow a nonzero parallel W. A **weaker** condition only requiring a real metric is not sufficient to reach this conclusion. This is a restricted classical branch, not a no-go for complex off-slice UBT.

## Lorentz-covariant algebraic projectors, if two vectors are available

Suppose a nonzero future-directed timelike V and a second real Lorentz vector W exist. Set `S=W-(V·W/V²)V` and assume S is nonzero. Then S is spacelike. Represent Lorentz vectors by Hermitian 2×2 matrices `N=H(V)`, `B=H(S)`. Use the convention `det H(X)=-eta(X,X)`; N is positive definite, `det N>0`, `det B<0`, `tr(N^-1 B)=0`.

Define

```
c = sqrt(-det N / det B);
Q = c N^-1 B;
P_plus=(I+Q)/2; P_minus=(I-Q)/2.
```

The trace-free Cayley–Hamilton identity gives `Q²=I`, hence `P_±²=P_±`, `P_+P_-=0`, and `P_++P_-=I`. They obey `Q^dagger N=NQ`: the rank-one splitting is orthogonal in the N-weighted positive inner product.

Under `N'=L N L^dagger`, `B'=L B L^dagger`, `L in SL(2,C)`, the projectors transform by `P'=(L^dagger)^-1 P L^dagger`, not by remaining constant along a preferred Pauli axis. These algebraic facts do **not** supply a physical Hamiltonian or establish a distinguished time direction.

## Parallel splitting is stronger than projector covariance

For the canonical pure pair `D_mu X=partial_mu X+Omega_mu X+X Omega_mu^dagger`:

```
D_mu(Theta P)-(D_mu Theta)P = Theta D^R_mu P,
D^R_mu P = partial_mu P-[Omega_mu^dagger,P].
```

The right ideals are separately transported if `D^R_mu Q=0`. This implies the curvature compatibility `[F^R_mu nu,Q]=0`. Generic full SL(2,C) holonomy cannot stabilize a nontrivial rank-one projector because its commutant on C² consists only of scalars; existence of such a parallel projector therefore imposes a **holonomy reduction**. A nonparallel projector is still algebraically valid, but its two sectors mix.

## Spatially flat FLRW: restricted obstruction

For the specific Lorentz-vector composite representer `V^a=(rho,0,0,0)`, `rho=t+t0 !=0`, `e^0=dt`, `e^i=a(t)dx^i`, `D V=e` fixes the isotropic boost connection `omega^i_0=omega^0_i=(1/rho)e^i` with zero spatial rotations. Its spatial curvature is `F^i_j=(1/rho²)e^i∧e^j`. Thus `D W=0` implies `F W=0`, forcing all three spatial components W^i=0; then spatial parallel transport forces W^0=0. Hence **W=0 for this chosen connection and representer**, for any smooth scale factor. An inertial flat-space representer may have a different connection and a nonzero constant W; this is not a metric-only theorem.

## Holomorphy, physical section and compact imaginary time

For holomorphic `Theta(t+i psi)=V+iW`, Cauchy–Riemann yields `partial_psi V=-partial_t W`, `partial_psi W=partial_t V`. In particular `W|psi=0=0` does not imply `W` vanishes off that section. If a holomorphic tetrad is J-real on an **open complex-time domain**, it must be independent of tau (componentwise holomorphic and real-valued); a nonstationary holomorphic classical tetrad must instead use reality on a physical section or give up one of those assumptions.

An additional precise selection gate concerns **globally holomorphic, exactly periodic** imaginary time: if `Theta(t+i(psi+L))=Theta(t+i psi)` and Theta is holomorphic for all complex tau and bounded uniformly on a full period strip `t in R, psi in [0,L]`, then by periodicity Theta is a bounded entire function and is constant by Liouville. Nontrivial modes must violate at least one assumption (e.g., nonuniform growth in real time, singularities/limited domain, or different analyticity/boundary conditions). Example: `exp(2 pi tau/L)` is imaginary-periodic but grows exponentially as t→+infinity. This is **not** an unconditional compact-psi no-go.

## Relation to optical time qubits

Bloch: https://arxiv.org/abs/2511.07220; Yoon: https://arxiv.org/abs/2610.27639. The standard controlled Hamiltonian `H=I⊗H0+sigma3⊗V_int` already predicts two reversed *interaction* branches. This note supplies only a conditional algebraic representation of a control qubit from UBT fields. It does not derive an action, a unitary reverse-time operator, a GR graviton, an observable deviation from quantum optics, or a physical preferred time.

**Next falsification gates:** (i) derive an actual nonzero covariant W or an intrinsic off-slice Q from UBT equations; (ii) determine its holonomy and physical transport; (iii) derive the dynamics and a dimensionless observable with a fixed coefficient; (iv) verify against standard QM null predictions without re-fitting. The fundamental UBT action and reduced Hamiltonian remain open.

**Reproducible algebra:** `tests/test_time_qubit_covariance.py` checks idempotence, Lorentz congruence covariance, projector mixing, Cauchy–Riemann and periodic imaginary-time examples.
