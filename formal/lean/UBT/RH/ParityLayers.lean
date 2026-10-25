import UBT.RH.MobiusAbel
import Mathlib.Data.Nat.Choose.Basic

/-! Alternating cardinality layers and a cutoff classification lemma.
These do not identify artificial weights with logarithms of primes. -/
namespace UBT.RH.ParityLayers

def alternatingLayers (k r : ℕ) : ℤ :=
  ∑ j ∈ Finset.range (r + 1), (-1 : ℤ) ^ j * (k.choose j : ℤ)

/-- Pascal cancellation leaves an entire binomial boundary layer. -/
theorem alternating_layers (n r : ℕ) :
    alternatingLayers (n + 1) r = (-1 : ℤ) ^ r * (n.choose r : ℤ) := by
  induction r with
  | zero => simp [alternatingLayers]
  | succ r ih =>
    unfold alternatingLayers at ih ⊢
    rw [Finset.sum_range_succ, ih, Nat.choose_succ_succ]
    simp only [Nat.cast_add, pow_succ]
    ring

/-- Bounded perturbations below one layer spacing preserve the cutoff layers. -/
theorem threshold_layers (A B u c r : ℕ) (hBA : B < A) (hu : u ≤ B) :
    c * A + u ≤ r * A + B ↔ c ≤ r := by
  constructor
  · intro h
    by_contra hc
    have hcr : r + 1 ≤ c := by omega
    have hm := Nat.mul_le_mul_right A hcr
    nlinarith
  · intro hc
    have hm := Nat.mul_le_mul_right A hc
    omega

end UBT.RH.ParityLayers
