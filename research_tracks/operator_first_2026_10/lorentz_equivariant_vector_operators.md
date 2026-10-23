# Lorentz-equivariant first-order operators on the UBT Lorentz-vector slice

Date: 2026-10-11. Status: RESEARCH / conditional representation-theoretic lemma. AI-assisted, awaiting independent review.

## Scope

The Lorentz-real slice of B = C tensor H ≅ Mat(2,C) is a real Lorentz four-vector. With the standard spin-cover congruence action on Hermitian (or equivalent anti-Hermitian) matrices, its complexification is the irreducible (1/2,1/2) representation of SL(2,C) viewed as a real group (complexified Lie algebra sl2(C)⊕sl2(C)). The classification below presupposes this representation and a *linear* differential endomorphism with coefficient tensor independent of the field and no extra distinguished background vector.

## Theorem: no invariant linear first-order vector-to-vector principal symbol

A first-order equivariant operator L: sections(V) -> sections(V) has principal symbol a Lorentz intertwiner

  sigma(L) in Hom_Lor(T* tensor V, V).

Since T* ≅ V = (1/2,1/2),

  T* tensor V ≅ (0,0) ⊕ (1,0) ⊕ (0,1) ⊕ (1,1).

The target V=(1/2,1/2) does not occur. Consequently

  Hom_Lor(T* tensor V,V) = 0,

and any such first-order equivariant operator has vanishing first-order principal symbol. A Lorentz-invariant zeroth-order endomorphism is a scalar multiple of the identity (over the complexified irreducible representation); it does not supply wave propagation.

**Caveat:** This is not a no-go for first-order operators on spinors, inhomogeneous differential forms, doubled modules, coupled multiplets, or *nonlinear* / background-dependent operators. Neither is it a classification for the full unconstrained complex biquaternion under an arbitrary chosen action; specify the carrier first.

## Allowed alternative target representations

There are nonzero first-order equivariant maps from a vector field V:
- divergence: ∂_μ V^μ -> scalar (0,0);
- exterior derivative: ∂_[μ V_{ν]} -> antisymmetric 2-tensor (1,0)⊕(0,1);
- symmetric traceless derivative: ∂_(μ V_{ν)} - (1/4)η_{μν}∂·V -> (1,1).

This is why a **complex of operators between representations**, rather than a vector-to-vector Dirac operator, is the natural first-order candidate.

## Two inequivalent vector second-order symbols remain

With no additional invariants and flat background, generic Poincare-invariant parity-even second-order vector principal symbol is

  P_μ{}^ν(k) = a k² δ_μ{}^ν + b k_μ k^ν

for free coefficients a,b (not uniquely fixed by algebra). Projectors transverse/longitudinal for k²≠0 have eigenvalues a k² (multiplicity 3) and (a+b) k² (multiplicity 1). Degenerate limits demand constraint analysis, not naive inversion. Maxwell-type symbol corresponds to b=-a (with a gauge kernel); the pure wave operator corresponds to b=0. Both pass Lorentz invariance and algebraic naturalness, hence those principles alone do not select an action.

In particular, a first-order operator complex V --d--> Λ² --δ--> V gives δd V = □V - d(div V) up to convention, whereas V --div--> scalar --grad--> V gives dδ V = grad(div V). Their sum can provide □V, but the relative coefficient is not fixed without an additional principle (adjointness, gauge symmetry, complex structure, etc.).

## Proposed next selection criterion

1. Establish exact Theta carrier and invariant nondegenerate inner product, including star/sharp and anti-Hermitian slice.
2. Study the de Rham / Dirac–Kähler-type operator d+δ on the *graded exterior bundle*, whose square is a Laplace-type operator in flat space, while showing exactly what additional bundle degrees are bookkeeping versus physical.
3. Compare the Maxwell-type gauge branch to the wave branch using constraint closure, stability and physical spectrum.
4. Reintroduce the composite tetrad E = DTheta/sqrt(N0) and demand that all first-order maps are equivariant for its **actual** connection. Account for curvature/torsion correction terms.
5. Recheck the linear TT inclusion: rank of a projection onto TT is not equivalent to availability of an exact pure TT metric perturbation.
6. Do not define a spectral action before selecting the operator domain, measure, regulator and function.

## Verification scope and status

The representation decomposition and the transverse/longitudinal eigenvalues are standard algebraic consequences. No symbolic executable verifier added in this note; human/machine cross-check welcome. No derived fundamental action, new physical graviton pole or GR prediction is claimed. Keep this research-only.
