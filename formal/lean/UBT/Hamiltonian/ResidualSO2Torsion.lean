import Lean

/-!
# Algebraic elimination for the residual SO(2) torsion comparison

The continuum calculation supplies the five Lorentz contractions. This file
checks the resulting coefficient map and the stationary quadratic reduction.
-/

namespace UBT.Hamiltonian

open Lean.Grind

theorem residualSO2EvenCoefficientMap {R : Type} [CommRing R]
    (c₁ c₂ c₃ a b p₂ p₃ : R) :
    c₁ * (4 * (b^2 - a^2) + 2 * (p₂^2 + p₃^2)) +
      c₂ * (-2 * (b^2 - a^2) + (p₂^2 + p₃^2)) + c₃ * (p₂^2 + p₃^2) =
    (4 * c₁ - 2 * c₂) * (b^2 - a^2) + (2 * c₁ + c₂ + c₃) * (p₂^2 + p₃^2) := by
  grind

theorem residualSO2EvenKernel {R : Type} [Field R] [IsCharP R 0]
    (c₁ c₂ c₃ : R) :
    (4 * c₁ - 2 * c₂ = 0 ∧ 2 * c₁ + c₂ + c₃ = 0) ↔
      (c₂ = 2 * c₁ ∧ c₃ = -4 * c₁) := by
  letI : NoNatZeroDivisors R := Field.noNatZeroDivisors.ofIsCharPZero
  grind

private def residualQuadratic {R : Type} [CommRing R]
    (longitudinal screen ja jb jp₂ jp₃ a b p₂ p₃ : R) : R :=
  longitudinal * (b^2 - a^2) + screen * (p₂^2 + p₃^2) +
    ja * a + jb * b + jp₂ * p₂ + jp₃ * p₃

theorem residualSO2StationaryTranslation {R : Type} [CommRing R]
    (longitudinal screen ja jb jp₂ jp₃ a b p₂ p₃ a₀ b₀ p₀₂ p₀₃ : R)
    (ha : ja = 2 * longitudinal * a₀) (hb : jb = -2 * longitudinal * b₀)
    (hp₂ : jp₂ = -2 * screen * p₀₂) (hp₃ : jp₃ = -2 * screen * p₀₃) :
    residualQuadratic longitudinal screen ja jb jp₂ jp₃ a b p₂ p₃ -
      residualQuadratic longitudinal screen ja jb jp₂ jp₃ a₀ b₀ p₀₂ p₀₃ =
    longitudinal * ((b - b₀)^2 - (a - a₀)^2) +
      screen * ((p₂ - p₀₂)^2 + (p₃ - p₀₃)^2) := by
  subst ja jb jp₂ jp₃
  unfold residualQuadratic
  grind

#print axioms residualSO2EvenKernel
#print axioms residualSO2StationaryTranslation

end UBT.Hamiltonian
