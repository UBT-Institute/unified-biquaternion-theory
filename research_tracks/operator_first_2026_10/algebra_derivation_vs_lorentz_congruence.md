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

# Algebra-derivation compatibility versus Lorentz congruence

Date: 2026-10-12. Working research, AI-assisted. No canonical promotion.

## Precise algebraic setting
B=C tensor H ≅ Mat_2(C) with associative matrix product. A complex-linear derivation d of B obeys d(XY)=d(X)Y+X d(Y), d(I)=0. Every derivation is inner (Skolem–Noether / derivations of full matrix algebras):

 d(X)=[A,X],

where A is unique modulo scalar multiples of I. Thus an algebra-product-compatible connection on the trivial B bundle is locally

 nabla_mu X=partial_mu X+[A_mu,X].

This is a structural classification, NOT a dynamical selection of the one-form A_mu. The center acts trivially; any A_mu may still vary in spacetime.

## Lorentz vector action and incompatibility with full matrix multiplication
On the Hermitian realization of Lorentz vectors, spin cover S in SL(2,C) acts as X -> S X S^dagger. This preserves the Lorentz determinant quadratic form, but is not generally an algebra automorphism:

 (S X S^dagger)(S Y S^dagger) = S X (S^dagger S) Y S^dagger,

which equals S(XY)S^dagger for all X,Y only if S^dagger S=I (up to special central factors; for SL2 complex, unitary branch).

Infinitesimally the congruence connection acts as

 D_mu X=partial_mu X+Omega_mu X+X Omega_mu^dagger.

Its multiplication defect for matrix-valued sections X,Y is

 D_mu(XY) - (D_mu X)Y - X(D_mu Y)
   = -X (Omega_mu+Omega_mu^dagger)Y,

with partial derivatives cancelling. (This follows directly on expansion.) For Lorentz boosts the Hermitian part Omega+Omega^dagger is nonzero, so the defect is generally nonzero. For anti-Hermitian Omega (rotation/compact subgroup), the connection reduces to a commutator and Leibniz is recovered.

Therefore one cannot simultaneously demand the *same ordinary matrix product* be preserved by the full noncompact Lorentz congruence action and retain the standard vector representation, without changing what multiplication/equivariance means.

## Options for an exact programme

(A) Vector/Clifford bundle: distinguish internal Clifford multiplication of tangent/cotangent vectors and its spinorial representation, with compatible spin connection; avoid identifying Lorentz-vector congruence with an algebra automorphism of raw Mat_2(C) multiplication.

(B) Adjoint algebra bundle: preserve ordinary Mat_2(C) multiplication and use commutator connection, but explain why the gravitational Lorentz-vector metric is represented and how boost transformations act.

(C) Enlarged or graded module: use left/right spinor spaces and a proper Clifford action. Extra modules must be justified (representation bookkeeping vs new physical particles).

## Decision
Algebra-derivation compatibility does not uniquely determine a physical connection; it exposes a representation choice that must be made at P0 (axioms) before pursuing operator or action selection.

Next: establish the exact canonical use of sharp/ddagger and whether its multiplication is intended as a Lorentz-covariant product of two vector carriers or only a Clifford pairing; test consistent mixed-sigma (left/right) products.

Status: exact algebraic obstruction under specified representations, not a proof of UBT inconsistency as a whole.
