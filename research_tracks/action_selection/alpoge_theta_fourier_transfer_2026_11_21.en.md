<!-- BILINGUAL-UNIT: alpoge-theta-transfer.scope -->
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

# Alpöge RH proof: finite Fourier/theta transfer gates for one UBT field

**Recorded 2026-11-21 · C_working · research only · LEAN-PENDING.**
This note tests a *finite Fourier analogue*, **not** Alpöge's arithmetic theta lift, and does not alter the canonical single-field tetrad, metric, or action. No UBT physics gap is closed.

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.sources -->
## Sources and separation of mechanisms

Alpöge's [original remark](https://alpo.ge/remark.pdf) proposes iterated theta lifts for an arithmetic multiplicity mechanism in a Stepanov-type GRH proof. The independent [proof architecture guide](https://nasqret.github.io/riemann-rev/guide/proof-guide.pdf) identifies CM fields, unitary groups, theta kernels, Hecke characters, cohomological and slope bounds. [Sutherland's audit](https://math.mit.edu/~drew/grh/) checks the Lean statements, including RH and Dirichlet GRH, but does not supply a transfer theorem for UBT.

An ordinary discrete Fourier transform, Jacobi theta summation, Gaussian heat smoothing, and the automorphic theta *lift* are different operations. The experiment below covers only the first and a nonunitary Gaussian control. Any connection to the actual iterated lift remains **OPEN**.

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.setup -->
## Exact toy space and invariants

Use the *existing* faithful matrix representation of one biquaternion:
[
Xinmathbb Bcongoperatorname{Mat}_2(mathbb C),qquad
B(X,Y)=operatorname{Re}operatorname{Tr}[operatorname{adj}(X)Y^dagger],
qquad JX=iX,qquad Omega(X,Y)=B(X,JY).
]
Here (operatorname{adj}) is the (2	imes2) adjugate, not the Hermitian adjoint. The real quadratic form (B) has inertia ((2+,6-)). (Omega) is alternating and nondegenerate; neither statement makes (B) a positive physical energy.

Take four *mode coefficients* (X_ninmathbb B), (n=0,1,2,3), without introducing a new fundamental field. Set
[
mathcal B(X,Y)=sum_{n=0}^3 B(X_n,Y_n),quad
mathcalOmega(X,Y)=sum_{n=0}^3 Omega(X_n,Y_n),
quad
(F_4X)_k=rac12sum_{n=0}^3e^{-2pi i kn/4}X_n.
]
This is a fixed-coefficient, finite-dimensional test; it does not assume that arbitrary mode mixing is a gauge transformation or that it preserves strict holomorphy in (	au=t+ipsi).

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.positive -->
## Algebraic result: exact preservation of the mode-space forms

**ALGEBRA-EXACT, conditional on this toy space.** Because (F_4^dagger F_4=I_4) and (F_4) acts complex-linearly on the mode index, it preserves both forms:
[
oxed{mathcal B(F_4X,F_4Y)=mathcal B(X,Y)},qquad
oxed{mathcalOmega(F_4X,F_4Y)=mathcalOmega(X,Y)},qquad
F_4^4=I.
]
The same proof applies to normalized (N)-mode DFTs with identical internal (B) on every mode. For four modes, the total real inertia is ((8+,24-)), unchanged by the transform. Thus exact symplectic covariance **does not cure an indefinite kinetic/Hamiltonian form**. It is not an on-shell positivity statement.

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.negative -->
## Two decisive negative controls

1. The positive Gaussian mode filter (G=operatorname{diag}(2^{-n^2})), acting on all four biquaternion coefficients, is **not** symplectic:
[
oxed{mathcalOmega(GX,GY)
eqmathcalOmega(X,Y)}
]
in general. A heat-kernel weight cannot be silently treated as a unitary/Weil symmetry.

2. The DFT is **not** a symmetry of the canonical UBT metric at fixed (psi), even though it preserves (mathcalOmega). In the simple trivial-connection, (mathcal N_0=1) flat witness, put all of the spacetime-dependent (Theta_{m SR}(x)) in mode (n=0):
[
Theta(x,psi)=Theta_{m SR}(x),quad
Theta'(x,0)=sum_{k=0}^3(F_4X)_k=2Theta_{m SR}(x),
quad E'_mu(x,0)=2E_mu(x,0),
]
[
oxed{g'_{mu
u}(x,0)=4g_{mu
u}(x,0)}
]
using the *unchanged* canonical (E_mu=mathcal N_0^{-1/2}D_muTheta) and central sharp anticommutator. This refutes the assertion that finite-mode Fourier covariance by itself implies a physical gauge symmetry. The flat witness is kinematical, not a solution of a selected UBT action.

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.gates -->
## Actual transfer gates — all OPEN

A proposed transfer of Alpöge's **arithmetic** theta-lift mechanism must first supply (i) a stated representation space and the actual lift kernel/intertwiner, with domains and convergence; (ii) covariance of the existing two-sided (D_muTheta=partial_muTheta+A_muTheta-Theta B_mu), including any mode mixing of (A_mu,B_mu); (iii) preservation or a derived transformation law of the *central sharp metric*, not merely of (mathcalOmega); (iv) a selected, constrained Hamiltonian and positivity test; and (v) a concrete UBT-specific consequence that fails a trivial Fourier/heat-kernel null model. An arithmetic divisibility/slope argument is not yet a physical propagator or gravitational dynamics.

The existing rank-one equivariant symplectic curvature no-go remains applicable to its specified scalar ansatz: a mode-space DFT does not create the rank-six bivector curvature coefficient required by Palatini. No new degree of freedom, action, physical symmetry, mass prediction or ghost-free claim is introduced.

<!-- BILINGUAL-UNIT: alpoge-theta-transfer.verification -->
## Verification and status

Independent analytic steps: DFT unitarity, complex-linearity, the inertia of (B), and direct evaluation of the sharp metric in a flat witness. The deterministic SymPy exact-arithmetic test is `research_tracks/action_selection/tests/test_alpoge_theta_fourier_transfer.py`; command:
```sh
python -m unittest research_tracks.action_selection.tests.test_alpoge_theta_fourier_transfer -v
```
Six tests passed locally with SymPy 1.14.0 on 2026-11-21: signature, order-four DFT, (B/Omega) covariance, non-symplectic Gaussian, surviving negative direction, and metric counterexample. This tests the encoded finite-dimensional identities only; no actual automorphic lift, UBT PDE, Einstein equations, constrained spectrum or Alpöge theorem is independently re-proved. **LEAN-PENDING**: no Lean file was compiled for this new note. No canon/status promotion and no semantic translation approval is claimed.
