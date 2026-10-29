import UBT.RH.MobiusAbel

/-! Finite signed energy identities. Correlation bounds are explicit hypotheses,
not consequences of prime pairing or a proof of RH. -/
namespace UBT.RH.SignedEnergy
open UBT.RH.MobiusAbel
open scoped ArithmeticFunction.Moebius

variable {R : Type*} [CommRing R]

def diagonal (a : ℕ → R) (N : ℕ) : R :=
  ∑ k ∈ Finset.range N, a (k + 1) ^ 2

def cross (a : ℕ → R) (N : ℕ) : R :=
  ∑ k ∈ Finset.range N, partialSum a k * a (k + 1)

/-- Exact diagonal plus all unordered cross terms, in prefix form. -/
theorem energy_identity (a : ℕ → R) (N : ℕ) :
    partialSum a N ^ 2 = diagonal a N + 2 * cross a N := by
  induction N with
  | zero => simp [partialSum, diagonal, cross]
  | succ N ih =>
    rw [partialSum_succ]
    simp only [diagonal, cross, Finset.sum_range_succ] at ih ⊢
    rw [add_sq, ih]
    ring

/-- This equivalence relocates the bound; it does not prove it. -/
theorem energy_bound_iff (a : ℕ → ℝ) (N : ℕ) (B : ℝ) :
    partialSum a N ^ 2 ≤ B ↔ cross a N ≤ (B - diagonal a N) / 2 := by
  rw [energy_identity]
  constructor <;> intro h <;> linarith

theorem energy_bound_of_cross (a : ℕ → ℝ) (N : ℕ) (D C : ℝ)
    (hd : diagonal a N ≤ D) (hc : cross a N ≤ C) :
    partialSum a N ^ 2 ≤ D + 2 * C := by
  rw [energy_identity]
  linarith

theorem mobius_energy_identity (N : ℕ) :
    partialSum (fun n => (μ n : ℝ)) N ^ 2 =
      diagonal (fun n => (μ n : ℝ)) N +
        2 * cross (fun n => (μ n : ℝ)) N :=
  energy_identity _ _

end UBT.RH.SignedEnergy
