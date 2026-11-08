import Lean

/-!
# Finite identities for the two-carrier sharp-reality comparison

The kernel relations start from the three pair-transport constraints on a
complex Lorentz variation. The transport lemma abstracts the flat affine
commutator. The two-by-two identities check the gauge adjustment and the
normal Euler symbol.
-/

namespace UBT.Hamiltonian

open Lean.Grind

theorem sharpRealityKernelRelations {M : Type} [IntModule M]
    (lambda : M → M)
    (mapAdd : ∀ x y, lambda (x + y) = lambda x + lambda y)
    (mapNeg : ∀ x, lambda (-x) = -lambda x)
    (invertible : ∀ x, x + lambda (lambda x) = 0 → x = 0)
    (rV rW sV sW : M)
    (first : rV + lambda sV = 0)
    (second : sW - lambda rW = 0)
    (mixed : rW + lambda sW + sV - lambda rV = 0) :
    rV = -lambda sV ∧ rW = -sV ∧ sW = -lambda sV := by
  have hrV : rV = -lambda sV := by grind
  have hsW : sW = lambda rW := by grind
  have sumInKernel : (rW + sV) + lambda (lambda (rW + sV)) = 0 := by
    rw [mapAdd, mapAdd]
    rw [hrV, hsW, mapNeg] at mixed
    grind
  have sumZero := invertible _ sumInKernel
  have hrW : rW = -sV := by grind
  exact ⟨hrV, hrW, by rw [hsW, hrW, mapNeg]⟩

theorem sharpRealityKernelOnCarriers {R M : Type} [CommRing R] [IntModule M]
    (pair : M → M → R) (lambda : M → M) (v w : M)
    (pairNeg : ∀ x y, pair x (-y) = -pair x y)
    (lambdaSkew : ∀ x y, pair (lambda x) y = -pair x (lambda y))
    (detect : ∀ x, pair v x = 0 → pair w x = 0 →
      pair (lambda v) x = 0 → pair (lambda w) x = 0 → x = 0)
    (u rV rW sW : M)
    (hrV : rV = -lambda u) (hrW : rW = -u) (hsW : sW = -lambda u)
    (uOrthogonal : pair v u = 0)
    (rVOrthogonal : pair v rV = 0) (rWOrthogonal : pair w rW = 0)
    (sWOrthogonal : pair w sW = 0) :
    u = 0 := by
  apply detect u uOrthogonal
  · rw [hrW, pairNeg] at rWOrthogonal
    grind
  · rw [lambdaSkew]
    rw [hrV, pairNeg] at rVOrthogonal
    exact rVOrthogonal
  · rw [lambdaSkew]
    rw [hsW, pairNeg] at sWOrthogonal
    exact sWOrthogonal

theorem parallelSharpRealityTransport {M : Type} [IntModule M]
    (V W : M → M) (mapSub : ∀ x y, W (x - y) = W x - W y)
    (commutator : ∀ x, W (V x) = V (W x) + W x)
    (mapZero : V 0 = 0) (c : M) (parallel : W c = 0) :
    W (V c - c) = 0 := by
  rw [mapSub, commutator, parallel, mapZero]
  grind

theorem parallelSharpRealityTidalTransport {M : Type} [IntModule M]
    (V W : M → M) (mapAdd : ∀ x y, W (x + y) = W x + W y)
    (commutator : ∀ x, W (V x) = V (W x) + W x)
    (mapZero : V 0 = 0) (h : M) (parallel : W h = 0) :
    W (V (V h) + V h) = 0 := by
  have first : W (V h) = 0 := by
    rw [commutator, parallel, mapZero]
    grind
  rw [mapAdd, commutator (V h), first, mapZero]
  grind

theorem sharpRealityGaugeNumerators {R : Type} [CommRing R] (a b r s : R) :
    let x := a * r + b * s
    let y := a * s - b * r
    a * x - b * y = (a^2 + b^2) * r ∧ a * y + b * x = (a^2 + b^2) * s := by
  dsimp
  constructor <;> grind

theorem sharpRealityNormalSymbolVanish {R : Type} [CommRing R] (a b A B : R)
    (nonZeroDivisor : ∀ z, (a^2 + b^2) * z = 0 → z = 0)
    (first : A * a + B * b = 0) (second : -A * b + B * a = 0) :
    A = 0 ∧ B = 0 := by
  constructor <;> apply nonZeroDivisor
  · calc
      (a^2 + b^2) * A = a * (A * a + B * b) - b * (-A * b + B * a) := by grind
      _ = 0 := by
        rw [first, second]
        grind
  · calc
      (a^2 + b^2) * B = b * (A * a + B * b) + a * (-A * b + B * a) := by grind
      _ = 0 := by
        rw [first, second]
        grind

#print axioms sharpRealityKernelRelations
#print axioms sharpRealityKernelOnCarriers
#print axioms parallelSharpRealityTransport
#print axioms parallelSharpRealityTidalTransport
#print axioms sharpRealityGaugeNumerators
#print axioms sharpRealityNormalSymbolVanish

end UBT.Hamiltonian
