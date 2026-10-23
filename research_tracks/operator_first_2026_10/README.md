# UBT operator-first programme — Weyl factorization and the action-selection gap

**Date:** 2026-10-11  
**Status:** research / working; no canonical theorem promotion.  
**Provenance:** AI-assisted derivation for author review.  
**Scope:** four-dimensional complexified Lorentz slice; no identification of physical complex time with a Jacobi modulus.

## Motivation and priority change

The canonical metric is the central anticommutator of the covariant tetrad `E_mu = D_mu Theta/sqrt(N0)`. Existing GR recovery is conditional and the fundamental action is not selected. Stop adding Hilbert–Palatini, curvature-squared, torsion-squared, or spectral cutoffs simply because they reproduce desired physics.

Two complementary selection principles:

1. **Constraint / consistency first**: classify algebra-native operators, symmetry requirements, principal symbols, integrability and constrained physical mode spaces. Eliminate inadmissible constructions.
2. **Spectral reconstruction second**: only for an independently specified operator and domain, investigate a spectral functional; do not mistake its definition for a first-principles action.

## Result 1: two-component biquaternionic Weyl factorization (algebraic identity)

Over C, the biquaternion algebra is `B = C tensor H ≅ Mat_2(C)`. In a chosen complex Minkowski frame of signature (+---), define Pauli matrices `sigma^mu = (I, sigma_1, sigma_2, sigma_3)` and `bar_sigma^mu = (I,-sigma_1,-sigma_2,-sigma_3)`. Then

`sigma^mu bar_sigma^nu + sigma^nu bar_sigma^mu = 2 eta^{mu nu} I_2`.

With commuting partial derivatives and constant frame,

`(sigma^mu partial_mu)(bar_sigma^nu partial_nu) = Box I_2`,
where `Box = partial_0^2 - sum_i partial_i^2`.

The mixed map factors the wave operator without choosing a local action. **This is a standard Weyl/Pauli algebra identity, not an original derivation of Einstein dynamics.** Check performed symbolically using SymPy 2×2 matrices for all 16 ordered index pairs.

Important: The two factors act naturally between left- and right-chiral spinor spaces; calling the individual matrices a 2×2 representation of the full four-dimensional Clifford algebra is incorrect.

## Result 2: obstruction to a 2×2 full Dirac Clifford representation

For a nondegenerate four-dimensional complex quadratic form, `Cl_4(C) ≅ Mat_4(C)`; its irreducible module has complex dimension 4. Therefore a faithful unital 2×2 set `Gamma^mu` satisfying

`{Gamma^mu,Gamma^nu}=2 eta^{mu nu} I_2`

does not exist. A full Dirac operator may instead use the doubled module `C^2 ⊕ C^2` and block matrices

`gamma^mu = [[0,sigma^mu],[bar_sigma^mu,0]]`.

These satisfy the four-dimensional Clifford relation. This doubling must be derived or motivated by the chosen representation/physical requirements; it is not an extra elementary biquaternion field by itself. The regular vector space `Mat_2(C)` also has dimension four, but identifying it with this Dirac module is not canonical under all proposed Lorentz and internal actions.

**Selection test:** specify the actual UBT transformation of Theta (Lorentz-vector / congruence versus spinor-module action) before applying a Dirac operator to it.

## What this does NOT select

The factorization leaves undetermined:
- whether fields transform as Weyl spinors, Lorentz vectors, or matrix-valued bimodules;
- connection `D_mu`, its torsion, left/right representation and compatibility;
- zero-order terms / masses, normalizations and admissible boundary domains;
- inner product and adjointness in Lorentzian signature; Wick-rotation assumptions;
- a measure and function `f` for any `Tr f(D^2/Lambda^2)`, and the scale Lambda;
- a unique fundamental action.

Thus neither Weyl factorization nor a Clifford operator alone derives GR, quantum probabilities, SU(3) dynamics or coupling constants.

## New priorities (cross-cutting, superseding execution order only; preserve existing P1–P4 research findings)

- **P0 AXIOMS:** inventory minimal independent input data (B, star/sharp, Lorentz real slice, physical variables including tau=t+i psi, transformation laws). Mark any metric, tetrad, spinor module and action as derived vs independently adopted.
- **P1 OPERATOR:** classify first-order equivariant symbols on the **actual** Theta representation, distinguishing vector congruence, bimodule and chiral spinor representations. Prove uniqueness or explicit nonuniqueness within a stated class.
- **P2 CONSISTENCY:** enforce closure of constraints, gauge equivariance, self-consistent connection and full linearized TT/ghost/tachyon tests. The previous pointwise map rank 13 / TT projection rank 2 is only a kinematic statement and does not establish a graviton.
- **P3 SPECTRAL:** only after P1–P2, establish Hilbert-space/domain, elliptic Euclidean continuation, regularization, the spectral action functional and whether its coefficients are independently fixed. Treat `f` and Lambda as explicit open inputs.
- **P4 PHYSICS:** compare GR, quantum theory and SU(3) with no hidden insertion of the desired results. Complex-time holomorphy, modular objects and cosmology remain separate compatibility tracks.

## Immediate proof tasks

1. Write down the exact Lorentz group action `Theta -> S Theta S^dagger` (or the canonical alternative) and determine whether the Weyl pair is an endomorphism or an intertwiner on that carrier.
2. Classify all equivariant linear first-order principal symbols `A(k)` under the stated action; exhibit multiple inequivalent choices if uniqueness fails.
3. Check a curved covariant factorization: the product of chiral covariant operators acquires connection-curvature terms; do NOT replace it by a pure scalar Laplacian without calculation.
4. Quantify the rank of the **pure TT target inclusion**, not just surjectivity of the TT projection, once gauge constraints are incorporated.
5. Only then attempt action selection and the physical Hessian.

## Claims / caution

**Established here:** standard Pauli–Weyl factorization; 2×2 Clifford obstruction; underdetermination of action by factorization.

**Not established:** a canonical UBT operator, a unique action, propagation of spin-2 modes, induced Newton coupling, global UBT solutions.

**Repository impact:** this note is research-only. No changes to canonical status or claims matrix are justified by it.
