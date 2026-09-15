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
  norm_num at hh
  linarith

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
    change u * (starRingEnd ℂ) u = 1
    rw [Complex.mul_conj]
    simp [Complex.normSq_eq_norm_sq, hu]
  rw [H_eq_real_invariant, hInvariantPhaseInvariant u X hunit]
  exact (H_eq_real_invariant X).symm

theorem hermitian_of_entries (Y : Mat)
    (ha : (Y 0 0).im = 0) (hd : (Y 1 1).im = 0)
    (hb : (Y 0 1).re = (Y 1 0).re) (hc : (Y 0 1).im = -(Y 1 0).im) :
    Yᴴ = Y := by
  ext i j : 2
  fin_cases i <;> fin_cases j <;> apply Complex.ext <;>
    simp [Matrix.conjTranspose_apply, ha, hd, hb, hc]

theorem matrix_of_entries (Y : Mat)
    (ha : (Y 0 0).im = 0) (hd : (Y 1 1).im = 0)
    (hb : (Y 0 1).re = (Y 1 0).re) (hc : (Y 0 1).im = -(Y 1 0).im) :
    Y = !![((Y 0 0).re : ℂ), Y 0 1; star (Y 0 1), ((Y 1 1).re : ℂ)] := by
  ext i j : 2
  fin_cases i <;> fin_cases j <;> apply Complex.ext <;> simp [ha, hd, hb, hc]

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
    simp [u, norm_ne_zero_iff.mpr ht]
  have htr : Matrix.trace (u • X) = (‖Matrix.trace X‖ : ℂ) := by
    rw [Matrix.trace_smul]
    exact div_mul_cancel₀ _ ht
  have hnorm : ‖(u • X).det‖ = ‖X.det‖ := by
    simp [hu]
  have hsat : H (u • X) = 2 * ‖(u • X).det‖ := by
    rw [phase_preserves_H u X hu, hnorm, hs]
  have hti : (Matrix.trace (u • X)).im = 0 := by rw [htr]; rfl
  obtain ⟨ha, hd, hb, hc⟩ := real_trace_saturation (u • X) hti hsat
  refine ⟨u, hu, hti, ?_, ?_⟩
  · rw [htr]
    exact norm_pos_iff.mpr ht
  · exact hermitian_of_entries (u • X) ha hd hb hc

/-- An exact triangular factor with prescribed positive determinant. -/
theorem triangular_factor (a d r : ℝ) (b : ℂ) (ha : 0 < a)
    (he : a * d - ‖b‖ ^ 2 = r ^ 2) :
    ∃ T : Mat, T.det = (r : ℂ) ∧
      T * Tᴴ = !![(a : ℂ), b; star b, (d : ℂ)] := by
  let t : ℝ := Real.sqrt a
  have ht : t ≠ 0 := ne_of_gt (Real.sqrt_pos.mpr ha)
  have ht' : (t : ℂ) ≠ 0 := by exact_mod_cast ht
  have ht₂ : (t : ℂ) ^ 2 = (a : ℂ) := by
    exact_mod_cast (Real.sq_sqrt ha.le)
  have he' : (a : ℂ) * (d : ℂ) - b * star b = (r : ℂ) ^ 2 := by
    change (a : ℂ) * (d : ℂ) - b * (starRingEnd ℂ) b = (r : ℂ) ^ 2
    rw [Complex.mul_conj, Complex.normSq_eq_norm_sq]
    exact_mod_cast he
  let T : Mat := (1 / (t : ℂ)) • !![(a : ℂ), 0; star b, (r : ℂ)]
  refine ⟨T, ?_, ?_⟩
  · simp [T, Matrix.det_fin_two]
    field_simp
    rw [ht₂]
  · ext i j : 2
    fin_cases i <;> fin_cases j <;>
      simp [T, Matrix.vecMul, dotProduct, Fin.sum_univ_succ] <;>
      field_simp [ht'] <;> rw [ht₂]
    all_goals try ring
    change (starRingEnd ℂ) b * b + (r : ℂ) ^ 2 = (a : ℂ) * (d : ℂ)
    change (a : ℂ) * (d : ℂ) - b * (starRingEnd ℂ) b = (r : ℂ) ^ 2 at he'
    linear_combination -he'

/-- Every minimizer has a phase times an explicit positive Hermitian factor.
The input is the proved invariant equality condition, not a Hermitian ansatz. -/
theorem minimum_factorization (X : Mat) (r : ℝ) (hr : 0 < r)
    (hh : H X = 2 * r ^ 2) (hn : ‖X.det‖ = r ^ 2) :
    ∃ u : ℂ, ∃ T : Mat, ‖u‖ = 1 ∧ T.det = (r : ℂ) ∧ X = u • (T * Tᴴ) := by
  have hp : 0 < H X := by rw [hh]; positivity
  have hs : H X = 2 * ‖X.det‖ := by rw [hh, hn]
  obtain ⟨u, hu, hti, htr, _⟩ := phase_normalization X hp hs
  let Y : Mat := u • X
  have hY : H Y = 2 * r ^ 2 := by
    change H (u • X) = _
    rw [phase_preserves_H u X hu, hh]
  have hnY : ‖Y.det‖ = r ^ 2 := by
    simp [Y, hu, hn]
  have hsY : H Y = 2 * ‖Y.det‖ := by rw [hY, hnY]
  obtain ⟨ha, hd, hb, hc⟩ := real_trace_saturation Y hti hsY
  have hrepr := matrix_of_entries Y ha hd hb hc
  have he : (Y 0 0).re * (Y 1 1).re - ‖Y 0 1‖ ^ 2 = r ^ 2 := by
    conv_lhs at hY => rw [hrepr]
    simp [H, Complex.mul_re] at hY
    linarith
  have ht : 0 < (Y 0 0).re + (Y 1 1).re := by
    change 0 < (Matrix.trace Y).re at htr
    simpa [Matrix.trace, Fin.sum_univ_succ] using htr
  have hapos : 0 < (Y 0 0).re := by
    by_contra h
    have h₁ := le_of_not_gt h
    have h₂ : 0 < (Y 1 1).re := by linarith
    have h₃ := mul_nonpos_of_nonpos_of_nonneg h₁ h₂.le
    nlinarith [sq_pos_of_pos hr, sq_nonneg ‖Y 0 1‖]
  obtain ⟨T, hT, hTT⟩ := triangular_factor (Y 0 0).re (Y 1 1).re r (Y 0 1) hapos he
  have hu₀ : u ≠ 0 := by intro hz; simp [hz] at hu
  refine ⟨u⁻¹, T, by simp [norm_inv, hu], hT, ?_⟩
  rw [hTT, ← hrepr]
  change X = u⁻¹ • (u • X)
  simp [smul_smul, hu₀]

theorem normalize_factor (T : Mat) (r : ℝ) (hr : 0 < r)
    (hT : T.det = (r : ℂ)) :
    ∃ S : Mat, S.det = 1 ∧ T * Tᴴ = (r : ℂ) • (S * Sᴴ) := by
  let s : ℝ := Real.sqrt r
  have hs : s ≠ 0 := ne_of_gt (Real.sqrt_pos.mpr hr)
  have hs' : (s : ℂ) ≠ 0 := by exact_mod_cast hs
  have hs₂ : (s : ℂ) ^ 2 = (r : ℂ) := by exact_mod_cast Real.sq_sqrt hr.le
  have hc : (r : ℂ) * (1 / (s : ℂ)) * (1 / (s : ℂ)) = 1 := by
    field_simp
    exact hs₂.symm
  let S : Mat := (1 / (s : ℂ)) • T
  refine ⟨S, ?_, ?_⟩
  · simp [S, hT]
    field_simp
    exact hs₂.symm
  · symm
    calc
      (r : ℂ) • (S * Sᴴ) =
          ((r : ℂ) * (1 / (s : ℂ)) * (1 / (s : ℂ))) • (T * Tᴴ) := by
        simp [S, Matrix.conjTranspose_smul,
          smul_smul, mul_assoc]
      _ = T * Tᴴ := by rw [hc, one_smul]

/-- Every global minimizer belongs to the same declared unit-phase/SL(2,C)
congruence orbit of r*I. This is an orbit statement, not physical gauge fixing. -/
theorem every_minimum_in_one_orbit (X : Mat) (r l₁ l₂ V₀ : ℝ)
    (hr : 0 < r) (hl₁ : 0 ≤ l₁) (hl₂ : 0 < l₂)
    (hmin : potential (massCoefficient r l₁ l₂) l₁ l₂ V₀ X =
      V₀ - (4 * l₁ + l₂) * r ^ 4) :
    ∃ u : ℂ, ∃ S : Mat, ‖u‖ = 1 ∧ S.det = 1 ∧
      X = u • ((r : ℂ) • (S * Sᴴ)) := by
  obtain ⟨hh, hn⟩ := (equality_iff r l₁ l₂ V₀ hr hl₁ hl₂ X).mp hmin
  obtain ⟨u, T, hu, hT, hX⟩ := minimum_factorization X r hr hh hn
  obtain ⟨S, hS, hfactor⟩ := normalize_factor T r hr hT
  exact ⟨u, S, hu, hS, hX.trans (congrArg (fun Z : Mat => u • Z) hfactor)⟩

/-- Conversely every member of the stated orbit has the minimum energy. -/
theorem orbit_attains_minimum (u : ℂ) (S : Mat) (r l₁ l₂ V₀ : ℝ)
    (hu : ‖u‖ = 1) (hS : S.det = 1) :
    potential (massCoefficient r l₁ l₂) l₁ l₂ V₀
      (u • ((r : ℂ) • (S * Sᴴ))) = V₀ - (4 * l₁ + l₂) * r ^ 4 := by
  have hi : (r : ℂ) • (S * Sᴴ) = S * ((r : ℂ) • (1 : Mat)) * Sᴴ := by
    simp
  have hh : H ((r : ℂ) • (S * Sᴴ)) = H ((r : ℂ) • (1 : Mat)) := by
    rw [hi, H_eq_real_invariant, hInvariantSpinLiftInvariant S _ hS]
    exact (H_eq_real_invariant _).symm
  have hn : ‖(u • ((r : ℂ) • (S * Sᴴ))).det‖ =
      ‖((r : ℂ) • (1 : Mat)).det‖ := by
    rw [hi]
    simp [hu, determinantSpinLiftInvariant S _ hS]
  unfold potential
  rw [phase_preserves_H u _ hu, hh, hn]
  simp [H, massCoefficient, Matrix.det_fin_two]
  ring

/-- Exact classification: the global minimizing set is precisely this orbit. -/
theorem minimum_iff_orbit (X : Mat) (r l₁ l₂ V₀ : ℝ)
    (hr : 0 < r) (hl₁ : 0 ≤ l₁) (hl₂ : 0 < l₂) :
    potential (massCoefficient r l₁ l₂) l₁ l₂ V₀ X =
      V₀ - (4 * l₁ + l₂) * r ^ 4 ↔
      ∃ u : ℂ, ∃ S : Mat, ‖u‖ = 1 ∧ S.det = 1 ∧
        X = u • ((r : ℂ) • (S * Sᴴ)) := by
  constructor
  · exact every_minimum_in_one_orbit X r l₁ l₂ V₀ hr hl₁ hl₂
  · rintro ⟨u, S, hu, hS, rfl⟩
    exact orbit_attains_minimum u S r l₁ l₂ V₀ hu hS

end UBT.Action.PotentialMinimumOrbit
