import Mathlib

/-! Exact centered fractional-part identities. These finite statements do not
prove a bound for the arithmetic Mobius vector or the Riemann hypothesis. -/
namespace UBT.RH.CenteredKernel
open Finset

noncomputable def kernel (N a b : ℝ) : ℝ :=
  N / (a * b) - (⌊N / (a * b)⌋ : ℝ) - 1 / 2

/-- The product interval fixes the floor exactly. -/
theorem floor_one (N a b : ℝ) (ha : 0 < a) (hb : 0 < b)
    (hlo : a * b ≤ N) (hhi : N < 2 * (a * b)) :
    ⌊N / (a * b)⌋ = (1 : ℤ) := by
  have hab : 0 < a * b := mul_pos ha hb
  apply Int.floor_eq_iff.mpr
  constructor
  · norm_num
    exact (le_div_iff₀ hab).mpr (by simpa using hlo)
  · norm_num
    exact (div_lt_iff₀ hab).mpr (by nlinarith)

/-- No statistical or arithmetic assumptions on the weights. -/
theorem rank_two_sum (I : Finset ℕ) (w d : ℕ → ℝ) (N c : ℝ) :
    (∑ a ∈ I, ∑ b ∈ I, w a * w b * (N / (d a * d b) - c)) =
      N * (∑ a ∈ I, w a / d a) ^ 2 - c * (∑ a ∈ I, w a) ^ 2 := by
  calc
    _ = ∑ a ∈ I, ∑ b ∈ I,
        (N * (w a / d a) * (w b / d b) - c * w a * w b) := by
      apply sum_congr rfl
      intro a ha
      apply sum_congr rfl
      intro b hb
      simp only [div_eq_mul_inv, mul_inv_rev]
      ring
    _ = _ := by
      simp_rw [sum_sub_distrib]
      simp only [← mul_sum, ← sum_mul]
      ring

/-- Exact weighted block identity for the actual floor-defined kernel. -/
theorem corner_identity (I : Finset ℕ) (w d : ℕ → ℝ) (N : ℝ)
    (hpos : ∀ a ∈ I, 0 < d a)
    (hlo : ∀ a ∈ I, ∀ b ∈ I, d a * d b ≤ N)
    (hhi : ∀ a ∈ I, ∀ b ∈ I, N < 2 * (d a * d b)) :
    (∑ a ∈ I, ∑ b ∈ I, w a * w b * kernel N (d a) (d b)) =
      N * (∑ a ∈ I, w a / d a) ^ 2 -
        (3 / 2 : ℝ) * (∑ a ∈ I, w a) ^ 2 := by
  calc
    _ = ∑ a ∈ I, ∑ b ∈ I, w a * w b *
        (N / (d a * d b) - (3 / 2 : ℝ)) := by
      apply sum_congr rfl
      intro a ha
      apply sum_congr rfl
      intro b hb
      rw [kernel, floor_one N (d a) (d b) (hpos a ha) (hpos b hb)
        (hlo a ha b hb) (hhi a ha b hb)]
      push_cast
      ring
    _ = _ := rank_two_sum I w d N (3 / 2)

/-- Recentring retains the square of the sum of weights exactly. -/
theorem recenter (I : Finset ℕ) (w d : ℕ → ℝ) (N : ℝ) :
    (∑ a ∈ I, ∑ b ∈ I, w a * w b *
      (N / (d a * d b) - (⌊N / (d a * d b)⌋ : ℝ))) =
      (1 / 2 : ℝ) * (∑ a ∈ I, w a) ^ 2 +
      ∑ a ∈ I, ∑ b ∈ I, w a * w b * kernel N (d a) (d b) := by
  have hc : (1 / 2 : ℝ) * (∑ a ∈ I, w a) ^ 2 =
      ∑ a ∈ I, ∑ b ∈ I, w a * w b * (1 / 2 : ℝ) := by
    simp only [pow_two, mul_sum, sum_mul]
    apply sum_congr rfl
    intro a ha
    apply sum_congr rfl
    intro b hb
    ring
  rw [hc, ← sum_add_distrib]
  apply sum_congr rfl
  intro a ha
  rw [← sum_add_distrib]
  apply sum_congr rfl
  intro b hb
  unfold kernel
  ring

/-- Every point of the upper tenth block has the same negative sign. -/
theorem upper_corner_negative (u a b : ℝ) (hu : 0 < u)
    (ha : 9 / 10 * u < a) (hau : a ≤ u)
    (hb : 9 / 10 * u < b) (hbu : b ≤ u) :
    kernel (u ^ 2) a b < -(43 / 162 : ℝ) := by
  have ha0 : 0 < a := by linarith
  have hb0 : 0 < b := by linarith
  have hp : 81 / 100 * u ^ 2 < a * b := by
    have h := mul_lt_mul ha hb (by positivity : 0 < (9 / 10 : ℝ) * u)
      (le_of_lt ha0)
    nlinarith
  have hq : a * b ≤ u ^ 2 := by
    have h := mul_le_mul hau hbu (le_of_lt hb0) (le_of_lt hu)
    nlinarith
  have hu2 : 0 < u ^ 2 := sq_pos_of_pos hu
  have hf := floor_one (u ^ 2) a b ha0 hb0 hq (by nlinarith)
  have hd : u ^ 2 / (a * b) < (100 / 81 : ℝ) :=
    (div_lt_iff₀ (mul_pos ha0 hb0)).mpr (by nlinarith)
  rw [kernel, hf]
  push_cast
  linarith

/-- A finite block witness; this is not a norm bound specialized to Mobius. -/
theorem negative_block_sum (I : Finset ℕ) (K : ℕ → ℕ → ℝ) (c : ℝ)
    (h : ∀ a ∈ I, ∀ b ∈ I, K a b ≤ -c) :
    (∑ a ∈ I, ∑ b ∈ I, K a b) ≤ -c * (I.card : ℝ) ^ 2 := by
  calc
    _ ≤ ∑ a ∈ I, ∑ b ∈ I, -c := by
      apply sum_le_sum
      intro a ha
      exact sum_le_sum (fun b hb => h a ha b hb)
    _ = _ := by simp; ring

end UBT.RH.CenteredKernel
