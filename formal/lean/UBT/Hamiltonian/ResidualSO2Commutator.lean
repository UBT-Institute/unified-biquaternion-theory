import Lean

/-!
# Finite principal-symbol checks for the two-carrier commutator square

The continuum calculation supplies the screen gauge action and the physical
quadratic symbol. These identities check their finite polynomial core.
-/

namespace UBT.Hamiltonian

open Lean.Grind

theorem residualSO2ScreenGradientGaugeKernel {R : Type} [CommRing R]
    (k q₂ q₃ ξ₂ ξ₃ : R) :
    (k * (2 * q₂ * ξ₂) - 2 * q₂ * (k * ξ₂),
     k * (q₃ * ξ₂ + q₂ * ξ₃) - q₃ * (k * ξ₂) - q₂ * (k * ξ₃),
     k * (2 * q₃ * ξ₃) - 2 * q₃ * (k * ξ₃)) = (0, 0, 0) := by
  simp only [Prod.mk.injEq]
  exact ⟨by grind, by grind, by grind⟩

/-- The characteristic determinant with the longitudinal shift removed and
the remaining matrix multiplied by two. The polynomial variable is
twice the squared frequency minus twice the squared longitudinal momentum. -/
theorem residualSO2ScreenCharacteristicPolynomial {R : Type} [CommRing R]
    (w x y : R) :
    (w - 2 * x^2) * ((w - x^2 - y^2) * (w - 2 * y^2) - 2 * x^2 * y^2)
        - 2 * x^2 * y^2 * (w - 2 * y^2) =
    w * (w - (x^2 + y^2)) * (w - 2 * (x^2 + y^2)) := by
  grind

#print axioms residualSO2ScreenGradientGaugeKernel
#print axioms residualSO2ScreenCharacteristicPolynomial

end UBT.Hamiltonian
