import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Module.LinearMap.Basic
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Linarith

/-!
# Bare volume action with freely varied algebraic jet auxiliaries

V is an arbitrary real variation space. No Theta component count is fixed.
The premises are a matched kinetic Gram pairing, a derivative-free potential,
and freely available algebraic jet variations. This is not a theorem about
every UBT action, connection closure, quantum measure or physical PDE.
-/

namespace UBT.GR.BareSplitJet

theorem relative_jet_right_inverse {R : Type*} [Ring R]
    (x xinv base target : R) (hx : xinv * x = 1) :
    base + ((target - base) * xinv) * x = target := by
  rw [mul_assoc, hx, mul_one]
  abel

theorem auxiliary_multiplier_vanishes {R : Type*} [Ring R]
    (x xinv : R) (hx : xinv * x = 1) (dual : R → ℝ)
    (h : ∀ p, dual (p * x) = 0) : ∀ target, dual target = 0 := by
  intro target
  have hc : (target * xinv) * x = target := by rw [mul_assoc, hx, mul_one]
  simpa only [hc] using h (target * xinv)

/-- Local stationarity of volume*F with independent volume/field variations.
The smooth functional/right-inverse interpretation is a separate premise. -/
theorem stationarity_iff_zero_weight_and_critical
    {V : Type*} [AddCommGroup V] [Module ℝ V]
    (volume f : ℝ) (hv : volume ≠ 0) (df : V →ₗ[ℝ] ℝ) :
    (∀ dv v, dv * f + volume * df v = 0) ↔
      f = 0 ∧ ∀ v, df v = 0 := by
  constructor
  · intro h
    have hf : f = 0 := by simpa using h 1 0
    refine ⟨hf, ?_⟩
    intro v
    have hd : volume * df v = 0 := by simpa using h 0 v
    exact (mul_eq_zero.mp hd).resolve_left hv
  · rintro ⟨hf, hd⟩ dv v
    simp [hf, hd v]

theorem critical_weight_kills_first_variation
    (volume f : ℝ → ℝ) (dv : ℝ)
    (hv : HasDerivAt volume dv 0) (hf : HasDerivAt f 0 0)
    (hz : f 0 = 0) : HasDerivAt (fun t => volume t * f t) 0 0 := by
  convert hv.mul hf using 1
  · rfl
  · rfl
  · rfl
  · simp [hz]

/-- Algebraic product-rule core, after the differential data are supplied. -/
theorem critical_second_variation {V : Type*}
    (f volume dv dw ddv : ℝ) (df : V → ℝ) (hessian : V → V → ℝ)
    (hf : f = 0) (hdf : ∀ v, df v = 0) (v w : V) :
    ddv * f + dv * df w + dw * df v + volume * hessian v w =
      volume * hessian v w := by
  simp [hf, hdf]

/-- The Ricci components are computed independently from Christoffels in CAS.
This theorem checks their finite incompatibility with Ricci=Lambda*g. -/
theorem non_Einstein_closed_metric_witness (lam : ℝ)
    (h00 : (-6 : ℝ) = -lam) (h11 : (4 : ℝ) = lam) : False := by
  linarith

end UBT.GR.BareSplitJet
