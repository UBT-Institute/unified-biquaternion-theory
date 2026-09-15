import UBT.Action.PotentialVacuum

/-!
# Phase normalization of every nonzero potential minimum

The phase is a symmetry of the existing biquaternionic potential. This
classification does not identify a physical gauge quotient or a spacetime
vacuum, and does not change the covariant tetrad.
-/

noncomputable section

namespace UBT.Action.PotentialMinimumOrbit

open scoped Matrix
open UBT.Action.PotentialVacuum

theorem H_trace_identity (X : Mat) :
    H X = ‖Matrix.trace X‖ ^ 2 -
      (‖X 0 0‖ ^ 2 + ‖X 0 1‖ ^ 2 + ‖X 1 0‖ ^ 2 + ‖X 1 1‖ ^ 2) := by
  simp [H, Matrix.trace, Fin.sum_univ_succ,
    Complex.sq_norm, Complex.normSq_apply, Complex.mul_re]
  ring

theorem trace_ne_zero (X : Mat) (hh : 0 < H X) : Matrix.trace X ≠ 0 := by
  intro hz
  rw [H_trace_identity, hz] at hh
  have hn : 0 ≤ ‖X 0 0‖ ^ 2 + ‖X 0 1‖ ^ 2 + ‖X 1 0‖ ^ 2 + ‖X 1 1‖ ^ 2 := by
    positivity
  simpa using (not_lt_of_ge hn) (by simpa using hh)

theorem real_trace_saturation (X : Mat)
    (ht : (Matrix.trace X).im = 0) (hs : H X = 2 * ‖X.det‖) :
    (X 0 0).im = 0 ∧ (X 1 1).im = 0 ∧
      (X 0 1).re = (X 1 0).re ∧ (X 0 1).im = -(X 1 0).im := by
  have hi : (X 0 0).im + (X 1 1).im = 0 := by
    simpa [Matrix.trace, Fin.sum_univ_succ] using ht
  have hid :
      2 * X.det.re - H X =
      ((X 0 0).im - (X 1 1).im) ^ 2 +
      ((X 0 1).re - (X 1 0).re) ^ 2 +
      ((X 0 1).im + (X 1 0).im) ^ 2 -
      ((X 0 0).im + (X 1 1).im) ^ 2 := by
    simp [H, Matrix.det_fin_two, Complex.sq_norm,
      Complex.normSq_apply, Complex.mul_re]
    ring
  have hn := Complex.re_le_norm X.det
  have h₁ := sq_nonneg ((X 0 0).im - (X 1 1).im)
  have h₂ := sq_nonneg ((X 0 1).re - (X 1 0).re)
  have h₃ := sq_nonneg ((X 0 1).im + (X 1 0).im)
  rw [hi] at hid
  have hz₁ : ((X 0 0).im - (X 1 1).im) ^ 2 = 0 := by nlinarith
  have hz₂ : ((X 0 1).re - (X 1 0).re) ^ 2 = 0 := by nlinarith
  have hz₃ : ((X 0 1).im + (X 1 0).im) ^ 2 = 0 := by nlinarith
  have he₁ := sq_eq_zero_iff.mp hz₁
  have he₂ := sq_eq_zero_iff.mp hz₂
  have he₃ := sq_eq_zero_iff.mp hz₃
  exact ⟨by linarith, by linarith, by linarith, by linarith⟩

theorem phase_preserves_H (u : ℂ) (X : Mat) (hu : ‖u‖ = 1) :
    H (u • X) = H X := by
  have hunit : u * star u = 1 := by
    rw [Complex.mul_conj]
    simp [Complex.normSq_eq_norm_sq, hu]
  rw [H_eq_real_invariant, hInvariantPhaseInvariant u X hunit]
  exact (H_eq_real_invariant X).symm

/-- Every positive saturated matrix admits a unit phase with positive real
trace and Hermitian entries. No Hermitian restriction is assumed on X. -/
theorem phase_normalization (X : Mat)
    (hh : 0 < H X) (hs : H X = 2 * ‖X.det‖) :
    ∃ u : ℂ, ‖u‖ = 1 ∧
      (Matrix.trace (u • X)).im = 0 ∧
      0 < (Matrix.trace (u • X)).re ∧
      (u • X)ᴴ = u • X := by
  have ht := trace_ne_zero X hh
  let u : ℂ := (‖Matrix.trace X‖ : ℂ) / Matrix.trace X
  have hu : ‖u‖ = 1 := by
    simp [u, norm_div, norm_ne_zero_iff.mpr ht]
  have htr : Matrix.trace (u • X) = (‖Matrix.trace X‖ : ℂ) := by
    rw [Matrix.trace_smul]
    exact div_mul_cancel₀ _ ht
  have hnorm : ‖(u • X).det‖ = ‖X.det‖ := by
    simp [Matrix.det_smul, norm_mul, hu]
  have hsat : H (u • X) = 2 * ‖(u • X).det‖ := by
    rw [phase_preserves_H u X hu, hnorm, hs]
  have hti : (Matrix.trace (u • X)).im = 0 := by rw [htr]; rfl
  obtain ⟨ha, hd, hb, hc⟩ := real_trace_saturation (u • X) hti hsat
  refine ⟨u, hu, hti, ?_, ?_⟩
  · rw [htr]
    exact norm_pos_iff.mpr ht
  · ext i j : 2
    fin_cases i <;> fin_cases j <;> apply Complex.ext <;>
      simp [Matrix.conjTranspose_apply, ha, hd, hb, hc]

end UBT.Action.PotentialMinimumOrbit
