import UBT.RH.MobiusAbel

/-! Exact prime pairing for the Mertens sum. No asymptotic cancellation
estimate or probabilistic independence is assumed. -/
namespace UBT.RH.PrimePairing
open Finset
open scoped ArithmeticFunction.Moebius

noncomputable def primeFree (p n : ℕ) : ℤ := if p ∣ n then 0 else μ n
noncomputable def mertens (N : ℕ) : ℤ := ∑ n ∈ range (N + 1), μ n
noncomputable def freeSum (p N : ℕ) : ℤ := ∑ n ∈ range (N + 1), primeFree p n

theorem moebius_prime_mul (p m : ℕ) (hp : p.Prime) :
    μ (p * m) = -primeFree p m := by
  by_cases hm : p ∣ m
  · have hn : ¬Squarefree (p * m) := by
      intro hs
      exact (Nat.squarefree_iff_prime_squarefree.mp hs p hp)
        (mul_dvd_mul (dvd_refl p) hm)
    simp [primeFree, hm, ArithmeticFunction.moebius_eq_zero_of_not_squarefree hn]
  · have hc : p.Coprime m := hp.coprime_iff_not_dvd.mpr hm
    rw [ArithmeticFunction.IsMultiplicative.map_mul_of_coprime
      ArithmeticFunction.isMultiplicative_moebius hc,
      ArithmeticFunction.moebius_apply_prime hp]
    simp [primeFree, hm]

theorem coefficient_split (p n : ℕ) (hp : p.Prime) :
    μ n = primeFree p n - (if p ∣ n then primeFree p (n / p) else 0) := by
  by_cases hn : p ∣ n
  · have he : p * (n / p) = n := Nat.mul_div_cancel' hn
    have h := moebius_prime_mul p (n / p) hp
    rw [he] at h
    simpa [primeFree, hn] using h
  · simp [primeFree, hn]

/-- Reindex all multiples of p in a finite interval, including zero. -/
theorem sum_quotient_multiples (f : ℕ → ℤ) (p N : ℕ) (hp : 0 < p) :
    (∑ n ∈ range (N + 1), if p ∣ n then f (n / p) else 0) =
      ∑ m ∈ range (N / p + 1), f m := by
  rw [← sum_filter]
  apply sum_bij (fun n _ => n / p)
  · intro n hn
    simp only [mem_filter, mem_range] at hn ⊢
    exact Nat.lt_succ_of_le (Nat.div_le_div_right (Nat.le_of_lt_succ hn.1))
  · intro n hn m hm hnm
    have hn' := (mem_filter.mp hn).2
    have hm' := (mem_filter.mp hm).2
    calc
      n = p * (n / p) := (Nat.mul_div_cancel' hn').symm
      _ = p * (m / p) := by rw [hnm]
      _ = m := Nat.mul_div_cancel' hm'
  · intro m hm
    refine ⟨p * m, ?_, ?_⟩
    · simp only [mem_filter, mem_range]
      refine ⟨?_, dvd_mul_right p m⟩
      have hle : m * p ≤ N := (Nat.le_div_iff_mul_le hp).mp (Nat.le_of_lt_succ (mem_range.mp hm))
      exact Nat.lt_succ_of_le (by simpa [mul_comm] using hle)
    · simp [hp.ne']
  · intro n hn
    rfl

theorem mertens_prime_difference (p N : ℕ) (hp : p.Prime) :
    mertens N = freeSum p N - freeSum p (N / p) := by
  unfold mertens freeSum
  simp_rw [coefficient_split p _ hp]
  rw [sum_sub_distrib, sum_quotient_multiples _ p N hp.pos]

/-- Only the p-free upper band survives exact pairing. -/
theorem mertens_prime_band (p N : ℕ) (hp : p.Prime) :
    mertens N = ∑ n ∈ (range (N + 1)).filter (fun n => N / p < n), primeFree p n := by
  have hf : (range (N + 1)).filter (fun n => n ≤ N / p) = range (N / p + 1) := by
    ext n
    simp only [mem_filter, mem_range]
    have hd := Nat.div_le_self N p
    omega
  have h := sum_filter_add_sum_filter_not (range (N + 1))
    (fun n => n ≤ N / p) (primeFree p)
  rw [hf] at h
  simp only [not_le] at h
  rw [mertens_prime_difference p N hp]
  unfold freeSum
  linarith

/-- An unconditional bound by the number of surviving p-free indices.
This is a linear-scale counting bound, not an RH-strength estimate. -/
theorem mertens_band_bound (p N : ℕ) (hp : p.Prime) :
    |mertens N| ≤ (((range (N + 1)).filter (fun n => N / p < n)).filter
      (fun n => ¬p ∣ n)).card := by
  rw [mertens_prime_band p N hp]
  calc
    _ ≤ ∑ n ∈ (range (N + 1)).filter (fun n => N / p < n), |primeFree p n| :=
      abs_sum_le_sum_abs _ _
    _ ≤ ∑ n ∈ (range (N + 1)).filter (fun n => N / p < n),
        if ¬p ∣ n then (1 : ℤ) else 0 := by
      apply sum_le_sum
      intro n hn
      by_cases hd : p ∣ n
      · simp [primeFree, hd]
      · simpa [primeFree, hd] using (ArithmeticFunction.abs_moebius_le_one (n := n))
    _ = _ := by rw [← sum_filter]; simp

end UBT.RH.PrimePairing
