/-
Power-weight proof adapted from Mathlib/NumberTheory/LSeries/SumCoeff.lean,
Copyright (c) 2025 Xavier Roblot, Apache 2.0.
The adaptation concludes ordered convergence directly, without the original
auxiliary theorem's LSeriesSummable hypothesis.
-/
import UBT.RH.MobiusAbel
import Mathlib.NumberTheory.LSeries.SumCoeff

namespace UBT.RH.PowerWeightLimit

open Finset Filter MeasureTheory Topology Complex Asymptotics

/-- A signed partial-sum bound, not a sum-of-norms bound. The conclusion is
natural-order convergence and an improper integral, not absolute convergence. -/
theorem ordered_power_limit (a : ℕ → ℂ) (ha : a 0 = 0)
    {r : ℝ} (hr : 0 ≤ r) {s : ℂ} (hs : r < s.re)
    (hO : (fun n ↦ ∑ k ∈ Icc 1 n, a k) =O[atTop] fun n ↦ (n : ℝ) ^ r) :
    Tendsto (fun n : ℕ ↦ ∑ k ∈ Icc 0 n, (k : ℂ) ^ (-s) * a k) atTop
      (𝓝 (s * ∫ t in Set.Ioi (1 : ℝ),
        (∑ k ∈ Icc 1 ⌊t⌋₊, a k) * (t : ℂ) ^ (-(s + 1)))) := by
  have h₁ : (-s - 1).re + r < -1 := by
    rwa [sub_re, one_re, neg_re, neg_sub_left, neg_add_lt_iff_lt_add, add_neg_cancel_comm]
  have h₂ : s ≠ 0 := ne_zero_of_re_pos (hr.trans_lt hs)
  have h₃ (t : ℝ) (ht : t ∈ Set.Ici 1) :
      DifferentiableAt ℝ (fun x : ℝ ↦ (x : ℂ) ^ (-s)) t :=
    differentiableAt_id.ofReal_cpow_const (zero_lt_one.trans_le ht).ne' (neg_ne_zero.mpr h₂)
  have h₄ : ∀ n, ∑ k ∈ Icc 0 n, a k = ∑ k ∈ Icc 1 n, a k := fun n ↦ by
    rw [← insert_Icc_add_one_left_eq_Icc n.zero_le, sum_insert (by aesop), ha,
      zero_add, zero_add]
  simp_rw [← h₄] at hO
  rw [← integral_const_mul]
  convert!
    tendsto_sum_mul_atTop_nhds_one_sub_integral₀ (f := fun x ↦ (x : ℂ) ^ (-s))
      (l := 0) ?_ ha h₃ ?_ ?_ ?_ (integrableAtFilter_rpow_atTop_iff.mpr h₁)
  · rw [zero_sub, ← integral_neg]
    refine setIntegral_congr_fun measurableSet_Ioi fun t ht ↦ ?_
    rw [deriv_ofReal_cpow_const (zero_lt_one.trans ht).ne', h₄]
    · ring_nf
    · exact neg_ne_zero.mpr h₂
  · refine (Iff.mpr integrableOn_Ici_iff_integrableOn_Ioi <|
      integrableOn_Ioi_deriv_ofReal_cpow zero_lt_one
        (by simpa using! hr.trans_lt hs)).locallyIntegrableOn
  · have hlim : Tendsto (fun n : ℕ ↦ (n : ℝ) ^ (-(s.re - r))) atTop (𝓝 0) :=
      (tendsto_rpow_neg_atTop (by rwa [sub_pos])).comp tendsto_natCast_atTop_atTop
    refine (IsBigO.mul_atTop_rpow_natCast_of_isBigO_rpow (-s.re) _ _ ?_ hO ?_).trans_tendsto hlim
    · exact isBigO_norm_left.mp <| (norm_ofReal_cpow_eventually_eq_atTop _).isBigO.natCast_atTop
    · linarith
  · refine .mul_atTop_rpow_of_isBigO_rpow (-(s + 1).re) r _ ?_ ?_ (by rw [← neg_re, neg_add'])
    · simpa [-neg_add_rev, neg_add'] using! isBigO_deriv_ofReal_cpow_const_atTop _
    · exact (hO.comp_tendsto tendsto_nat_floor_atTop).trans <|
        isEquivalent_nat_floor.isBigO.rpow hr (eventually_ge_atTop 0)

open scoped ArithmeticFunction.Moebius

/-- The cancellation bound hO is explicit and is not derived in this theorem. -/
theorem mobius_ordered_power_limit {r : ℝ} (hr : 0 ≤ r) {s : ℂ} (hs : r < s.re)
    (hO : (fun n ↦ ∑ k ∈ Icc 1 n, (μ k : ℂ)) =O[atTop]
      fun n ↦ (n : ℝ) ^ r) :
    Tendsto (fun n : ℕ ↦ ∑ k ∈ Icc 0 n, (k : ℂ) ^ (-s) * (μ k : ℂ)) atTop
      (𝓝 (s * ∫ t in Set.Ioi (1 : ℝ),
        (∑ k ∈ Icc 1 ⌊t⌋₊, (μ k : ℂ)) * (t : ℂ) ^ (-(s + 1)))) :=
  ordered_power_limit (fun k ↦ (μ k : ℂ)) (by simp) hr hs hO

end UBT.RH.PowerWeightLimit
