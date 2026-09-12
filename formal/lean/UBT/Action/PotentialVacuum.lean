import UBT.Action.PotentialInvariants

/-!
# A nonzero minimum of the existing biquaternionic quartic potential

This is a constructive result about the declared potential, on all eight real
coordinates of Mat(2,C). The negative quadratic coefficient is parametrized by
r. No new term or field is introduced. Potential stability does not establish
a kinetic operator, physical masses, a quantum measure or an Einstein term.
-/

namespace UBT.Action.PotentialVacuum

open scoped Matrix

abbrev Mat := Matrix (Fin 2) (Fin 2) ℂ
abbrev Direction := Fin 8 → ℝ

def H (X : Mat) : ℝ :=
  2 * (X 0 0 * star (X 1 1)).re - ‖X 0 1‖ ^ 2 - ‖X 1 0‖ ^ 2

def potential (mu l₁ l₂ V₀ : ℝ) (X : Mat) : ℝ :=
  V₀ + mu * H X + l₁ * H X ^ 2 + l₂ * ‖X.det‖ ^ 2

def massCoefficient (r l₁ l₂ : ℝ) : ℝ := -(4 * l₁ + l₂) * r ^ 2

/-- i*r*I is in the original Lorentz-real biquaternionic slice. -/
def vacuum (r : ℝ) : Mat := !![Complex.I * (r : ℂ), 0; 0, Complex.I * (r : ℂ)]

theorem negative_mass_parameterization (mu l₁ l₂ : ℝ)
    (hmu : mu < 0) (hl₁ : 0 ≤ l₁) (hl₂ : 0 < l₂) :
    0 < Real.sqrt (-mu / (4 * l₁ + l₂)) ∧
      massCoefficient (Real.sqrt (-mu / (4 * l₁ + l₂))) l₁ l₂ = mu := by
  have hc : 0 < 4 * l₁ + l₂ := by linarith
  have hp : 0 < -mu / (4 * l₁ + l₂) := div_pos (neg_pos.mpr hmu) hc
  constructor
  · exact Real.sqrt_pos.mpr hp
  · unfold massCoefficient
    rw [Real.sq_sqrt hp.le]
    have hd := div_mul_cancel₀ (-mu) (ne_of_gt hc)
    nlinarith

theorem H_eq_real_invariant (X : Mat) : H X = (hInvariant X).re := by
  simp [H, hInvariant, Matrix.adjugate_fin_two, Matrix.trace, Matrix.mul_apply,
    Fin.sum_univ_succ, Complex.sq_norm, Complex.normSq_apply, Complex.mul_re]
  ring

/-- The universal norm inequality is proved for the actual complex entries. -/
theorem H_le_twice_norm_det (X : Mat) : H X ≤ 2 * ‖X.det‖ := by
  have h₁ := Complex.re_le_norm (X 0 0 * star (X 1 1))
  have h₂ := sq_nonneg (‖X 0 1‖ - ‖X 1 0‖)
  have h₃ := norm_sub_norm_le (X 0 0 * X 1 1) (X 0 1 * X 1 0)
  simp only [norm_mul, norm_star] at h₁ h₃
  rw [Matrix.det_fin_two]
  unfold H
  nlinarith

theorem potential_gap_identity (r l₁ l₂ V₀ : ℝ) (X : Mat) :
    potential (massCoefficient r l₁ l₂) l₁ l₂ V₀ X -
        (V₀ - (4 * l₁ + l₂) * r ^ 4) =
      l₁ * (H X - 2 * r ^ 2) ^ 2 +
      l₂ * (‖X.det‖ - r ^ 2) ^ 2 +
      l₂ * r ^ 2 * (2 * ‖X.det‖ - H X) := by
  unfold potential massCoefficient
  ring

theorem global_lower_bound (r l₁ l₂ V₀ : ℝ)
    (hl₁ : 0 ≤ l₁) (hl₂ : 0 ≤ l₂) (X : Mat) :
    V₀ - (4 * l₁ + l₂) * r ^ 4 ≤
      potential (massCoefficient r l₁ l₂) l₁ l₂ V₀ X := by
  rw [← sub_nonneg, potential_gap_identity]
  exact add_nonneg
    (add_nonneg (mul_nonneg hl₁ (sq_nonneg _)) (mul_nonneg hl₂ (sq_nonneg _)))
    (mul_nonneg (mul_nonneg hl₂ (sq_nonneg r))
      (sub_nonneg.mpr (H_le_twice_norm_det X)))

theorem potential_at_vacuum (r l₁ l₂ V₀ : ℝ) :
    potential (massCoefficient r l₁ l₂) l₁ l₂ V₀ (vacuum r) =
      V₀ - (4 * l₁ + l₂) * r ^ 4 := by
  simp [potential, massCoefficient, H, vacuum, Matrix.det_fin_two,
    Complex.sq_norm, Complex.normSq_apply, Complex.mul_re, Complex.mul_im]
  ring

/-- A global minimum is actually attained on the Lorentz-real slice. -/
theorem vacuum_is_global_minimum (r l₁ l₂ V₀ : ℝ)
    (hl₁ : 0 ≤ l₁) (hl₂ : 0 ≤ l₂) (X : Mat) :
    potential (massCoefficient r l₁ l₂) l₁ l₂ V₀ (vacuum r) ≤
      potential (massCoefficient r l₁ l₂) l₁ l₂ V₀ X := by
  rw [potential_at_vacuum]
  exact global_lower_bound r l₁ l₂ V₀ hl₁ hl₂ X

theorem vacuum_ne_zero (r : ℝ) (hr : 0 < r) : vacuum r ≠ 0 := by
  intro hz
  have he := congrArg (fun X : Mat => (X 0 0).im) hz
  simp [vacuum] at he
  exact (ne_of_gt hr) he

/-- In this sign region the known noncompact H=D=0 ray is strictly above
the minimum; flatness of that ray is not instability of this vacuum. -/
theorem null_ray_above_vacuum (r l₁ l₂ V₀ t : ℝ)
    (hr : 0 < r) (hl₁ : 0 ≤ l₁) (hl₂ : 0 < l₂) :
    potential (massCoefficient r l₁ l₂) l₁ l₂ V₀ (vacuum r) <
      potential (massCoefficient r l₁ l₂) l₁ l₂ V₀
        !![(t : ℂ), 0; 0, 0] := by
  rw [potential_at_vacuum]
  have hp : 0 < (4 * l₁ + l₂) * r ^ 4 := mul_pos (by linarith) (pow_pos hr 4)
  simpa [potential, H, Matrix.det_fin_two] using sub_lt_self V₀ hp

/-- All global minimizers have these exact invariant values. -/
theorem equality_iff (r l₁ l₂ V₀ : ℝ)
    (hr : 0 < r) (hl₁ : 0 ≤ l₁) (hl₂ : 0 < l₂) (X : Mat) :
    potential (massCoefficient r l₁ l₂) l₁ l₂ V₀ X =
        V₀ - (4 * l₁ + l₂) * r ^ 4 ↔
      H X = 2 * r ^ 2 ∧ ‖X.det‖ = r ^ 2 := by
  have ha := mul_nonneg hl₁ (sq_nonneg (H X - 2 * r ^ 2))
  have hb := mul_nonneg hl₂.le (sq_nonneg (‖X.det‖ - r ^ 2))
  have hc := mul_nonneg (mul_nonneg hl₂.le (sq_nonneg r))
    (sub_nonneg.mpr (H_le_twice_norm_det X))
  have hp : 0 < l₂ * r ^ 2 := mul_pos hl₂ (sq_pos_of_pos hr)
  constructor
  · intro he
    have hg := potential_gap_identity r l₁ l₂ V₀ X
    rw [he, sub_self] at hg
    have hz : l₂ * (‖X.det‖ - r ^ 2) ^ 2 = 0 := by linarith
    have hsq : (‖X.det‖ - r ^ 2) ^ 2 = 0 :=
      (mul_eq_zero.mp hz).resolve_left (ne_of_gt hl₂)
    have hn : ‖X.det‖ = r ^ 2 := sub_eq_zero.mp (sq_eq_zero_iff.mp hsq)
    have hz' : l₂ * r ^ 2 * (2 * ‖X.det‖ - H X) = 0 := by linarith
    have hh := (mul_eq_zero.mp hz').resolve_left (ne_of_gt hp)
    exact ⟨by linarith, hn⟩
  · rintro ⟨hh, hn⟩
    have hg := potential_gap_identity r l₁ l₂ V₀ X
    rw [hh, hn] at hg
    nlinarith

/-- An arbitrary eight-real-component affine variation of the same matrix. -/
def variation (r t : ℝ) (v : Direction) : Mat :=
  !![((t * v 0 : ℝ) : ℂ) + Complex.I * ((r + t * v 1 : ℝ) : ℂ),
      ((t * v 4 : ℝ) : ℂ) + Complex.I * ((t * v 5 : ℝ) : ℂ);
     ((t * v 6 : ℝ) : ℂ) + Complex.I * ((t * v 7 : ℝ) : ℂ),
      ((t * v 2 : ℝ) : ℂ) + Complex.I * ((r + t * v 3 : ℝ) : ℂ)]

def hDirection (v : Direction) : ℝ :=
  2 * (v 0 * v 2 + v 1 * v 3) - v 4 ^ 2 - v 5 ^ 2 - v 6 ^ 2 - v 7 ^ 2
def detReDirection (v : Direction) : ℝ :=
  v 0 * v 2 - v 1 * v 3 - v 4 * v 6 + v 5 * v 7
def detImDirection (v : Direction) : ℝ :=
  v 0 * v 3 + v 1 * v 2 - v 4 * v 7 - v 5 * v 6
def quadratic (r l₁ l₂ : ℝ) (v : Direction) : ℝ :=
  r ^ 2 * ((4 * l₁ + l₂) * (v 1 + v 3) ^ 2 +
    l₂ * ((v 0 - v 2) ^ 2 + (v 4 + v 6) ^ 2 + (v 5 - v 7) ^ 2))
def cubic (r l₁ l₂ : ℝ) (v : Direction) : ℝ :=
  2 * r * (2 * l₁ * (v 1 + v 3) * hDirection v +
    l₂ * (-(v 1 + v 3) * detReDirection v + (v 0 + v 2) * detImDirection v))
def quartic (l₁ l₂ : ℝ) (v : Direction) : ℝ :=
  l₁ * hDirection v ^ 2 + l₂ * (detReDirection v ^ 2 + detImDirection v ^ 2)

set_option maxHeartbeats 4000000 in
theorem variation_polynomial (r l₁ l₂ V₀ t : ℝ) (v : Direction) :
    potential (massCoefficient r l₁ l₂) l₁ l₂ V₀ (variation r t v) =
      (V₀ - (4 * l₁ + l₂) * r ^ 4) +
      quadratic r l₁ l₂ v * t ^ 2 + cubic r l₁ l₂ v * t ^ 3 +
      quartic l₁ l₂ v * t ^ 4 := by
  simp [potential, massCoefficient, H, variation, Matrix.det_fin_two,
    Complex.sq_norm, Complex.normSq_apply, Complex.mul_re, Complex.mul_im,
    quadratic, cubic, quartic, hDirection, detReDirection, detImDirection]
  ring

theorem secondDeriv_quartic (a b c d : ℝ) :
    deriv (fun t : ℝ => deriv (fun s : ℝ =>
      a + b * s ^ 2 + c * s ^ 3 + d * s ^ 4) t) 0 = 2 * b := by
  have first : (fun t : ℝ => deriv (fun s : ℝ =>
      a + b * s ^ 2 + c * s ^ 3 + d * s ^ 4) t) =
      (fun t : ℝ => 2 * b * t + 3 * c * t ^ 2 + 4 * d * t ^ 3) := by
    funext t
    have hd := (((hasDerivAt_const t a).add
      (((hasDerivAt_id t).pow 2).const_mul b)).add
      (((hasDerivAt_id t).pow 3).const_mul c)).add
      (((hasDerivAt_id t).pow 4).const_mul d)
    convert hd.deriv using 1
    ring
  rw [first]
  have hd := (((hasDerivAt_id (0 : ℝ)).const_mul (2 * b)).add
    (((hasDerivAt_id (0 : ℝ)).pow 2).const_mul (3 * c))).add
    (((hasDerivAt_id (0 : ℝ)).pow 3).const_mul (4 * d))
  simpa using hd.deriv

/-- The actual second derivative in every real field direction. -/
theorem secondVariation_at_vacuum (r l₁ l₂ V₀ : ℝ) (v : Direction) :
    deriv (fun t : ℝ => deriv (fun s : ℝ =>
      potential (massCoefficient r l₁ l₂) l₁ l₂ V₀ (variation r s v)) t) 0 =
      2 * quadratic r l₁ l₂ v := by
  simp_rw [variation_polynomial]
  exact secondDeriv_quartic _ _ _ _

theorem quadratic_nonnegative (r l₁ l₂ : ℝ)
    (hl₁ : 0 ≤ l₁) (hl₂ : 0 ≤ l₂) (v : Direction) :
    0 ≤ quadratic r l₁ l₂ v := by
  unfold quadratic
  positivity

/-- Strict positivity transverse to the four displayed flat tangent directions. -/
theorem quadratic_positive (r l₁ l₂ : ℝ)
    (hr : 0 < r) (hl₁ : 0 ≤ l₁) (hl₂ : 0 < l₂) (v : Direction)
    (hv : 0 < (v 1 + v 3) ^ 2 + (v 0 - v 2) ^ 2 +
      (v 4 + v 6) ^ 2 + (v 5 - v 7) ^ 2) :
    0 < quadratic r l₁ l₂ v := by
  have hp := mul_pos hl₂ hv
  have ha := mul_nonneg hl₁ (sq_nonneg (v 1 + v 3))
  have hb : 0 < (4 * l₁ + l₂) * (v 1 + v 3) ^ 2 +
      l₂ * ((v 0 - v 2) ^ 2 + (v 4 + v 6) ^ 2 + (v 5 - v 7) ^ 2) := by
    nlinarith
  exact mul_pos (sq_pos_of_pos hr) hb

theorem quadratic_eq_zero_iff (r l₁ l₂ : ℝ)
    (hr : 0 < r) (hl₁ : 0 ≤ l₁) (hl₂ : 0 < l₂) (v : Direction) :
    quadratic r l₁ l₂ v = 0 ↔
      v 1 + v 3 = 0 ∧ v 0 - v 2 = 0 ∧ v 4 + v 6 = 0 ∧ v 5 - v 7 = 0 := by
  constructor
  · intro hz
    have ha := sq_nonneg (v 1 + v 3)
    have hb := sq_nonneg (v 0 - v 2)
    have hc := sq_nonneg (v 4 + v 6)
    have hd := sq_nonneg (v 5 - v 7)
    have hnot : ¬ 0 < (v 1 + v 3) ^ 2 + (v 0 - v 2) ^ 2 +
        (v 4 + v 6) ^ 2 + (v 5 - v 7) ^ 2 := by
      intro hs
      exact (ne_of_gt (quadratic_positive r l₁ l₂ hr hl₁ hl₂ v hs)) hz
    have hs := le_of_not_gt hnot
    have ha₀ : (v 1 + v 3) ^ 2 = 0 := by linarith
    have hb₀ : (v 0 - v 2) ^ 2 = 0 := by linarith
    have hc₀ : (v 4 + v 6) ^ 2 = 0 := by linarith
    have hd₀ : (v 5 - v 7) ^ 2 = 0 := by linarith
    exact ⟨sq_eq_zero_iff.mp ha₀, sq_eq_zero_iff.mp hb₀,
      sq_eq_zero_iff.mp hc₀, sq_eq_zero_iff.mp hd₀⟩
  · rintro ⟨ha, hb, hc, hd⟩
    simp [quadratic, ha, hb, hc, hd]

end UBT.Action.PotentialVacuum
