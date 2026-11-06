import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Finite algebra for the timelike radial scalar of the derived-H comparator.
The continuum Euler equations, local covariant quotient and principal-order
reduction are inputs to the analytic argument, outside this formalization.
-/

namespace UBT.Action.DerivedHRadialVacuum

/-- Algebraic identity from the radial reconstruction and logarithmic coordinate. -/
theorem carrier_norm_identity (r k h q s f Z : ℝ) (hr : r ≠ 0)
    (hk : k * f ^ 2 = -8 * r ^ 2 * Z)
    (hh : h ^ 2 * k = 4 * s ^ 2 * r) (hq : q = h ^ 2 * r) :
    2 * Z * (-q) = s ^ 2 * f ^ 2 := by
  have heq : (4 * r) * (2 * Z * (-q) - s ^ 2 * f ^ 2) = 0 := by
    rw [hq]
    calc
      _ = (h ^ 2 * k - 4 * s ^ 2 * r) * f ^ 2 -
            h ^ 2 * (k * f ^ 2 + 8 * r ^ 2 * Z) := by ring
      _ = 0 := by rw [hh, hk]; ring
  exact sub_eq_zero.mp ((mul_eq_zero.mp heq).resolve_left (mul_ne_zero (by norm_num) hr))

/-- The spatially isotropic pressure drops out of a rest-frame null contraction. -/
theorem rest_null_stress (pressure slope Z : ℝ) :
    (2 * Z * slope - pressure) + pressure = 2 * Z * slope := by
  ring

/-- Diagonal scalar principal tensor acting on rest-frame covectors. -/
def principal (slope inertia : ℝ) (covector : Fin 4 → ℝ) : Fin 4 → ℝ :=
  fun i => (if i = 0 then -inertia else slope) * covector i

/-- On an Einstein vacuum the principal tensor annihilates the entire spatial
covector subspace, even if the time coefficient is nonzero. -/
theorem einstein_vacuum_degeneracy (Z slope inertia : ℝ) (hZ : 0 < Z)
    (hNull : 2 * Z * slope = 0) :
    slope = 0 ∧ ∀ covector : Fin 4 → ℝ, covector 0 = 0 →
      principal slope inertia covector = 0 := by
  have hZ2 : 0 < 2 * Z := mul_pos (by norm_num) hZ
  have hSlope := (mul_eq_zero.mp hNull).resolve_left (ne_of_gt hZ2)
  refine ⟨hSlope, ?_⟩
  intro covector hTime
  funext i
  by_cases hi : i = 0
  · subst i
    simp [principal, hTime]
  · simp [principal, hi, hSlope]

/-- A positive uniform spatial stiffness and bounded carrier give a curvature floor. -/
theorem null_focusing_floor (s f M carrier bound Z slope b curvature : ℝ)
    (hM : 0 < M) (hBound : 0 < bound) (hZ : 0 < Z)
    (hb : 0 < b) (hSlope : b ≤ slope) (hCarrier : carrier ≤ bound)
    (hNorm : 2 * Z * carrier = s ^ 2 * f ^ 2)
    (hEinstein : M ^ 2 * curvature = 2 * Z * slope) :
    s ^ 2 * f ^ 2 * b / (M ^ 2 * bound) ≤ curvature := by
  have hM2 : 0 < M ^ 2 := pow_pos hM 2
  have hStress : 0 < 2 * Z * slope :=
    mul_pos (mul_pos (by norm_num) hZ) (hb.trans_le hSlope)
  have hProduct : 0 < M ^ 2 * curvature := hEinstein.symm ▸ hStress
  have hCurvature : 0 < curvature := pos_of_mul_pos_right hProduct hM2.le
  apply (div_le_iff₀ (mul_pos hM2 hBound)).2
  calc
    s ^ 2 * f ^ 2 * b ≤ s ^ 2 * f ^ 2 * slope :=
      mul_le_mul_of_nonneg_left hSlope (mul_nonneg (sq_nonneg s) (sq_nonneg f))
    _ = (M ^ 2 * curvature) * carrier := by rw [hEinstein, ← hNorm]; ring
    _ ≤ (M ^ 2 * curvature) * bound :=
      mul_le_mul_of_nonneg_left hCarrier (mul_nonneg hM2.le hCurvature.le)
    _ = curvature * (M ^ 2 * bound) := by ring

end UBT.Action.DerivedHRadialVacuum
