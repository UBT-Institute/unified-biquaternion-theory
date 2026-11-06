import Lean

/-!
# Independence of the residual SO(2) Euler polynomials

The continuum classification realizes the two traces and the transverse jet
as independent pointwise data. This file checks the remaining finite algebra:
the Euler map of the twelve proposed bulk monomials is injective.
-/

namespace UBT.Hamiltonian

open Lean.Grind

structure ResidualSO2Coefficients (R : Type) where
  sourceU : R
  sourceN : R
  uTraceU : R
  uTraceN : R
  nTraceU : R
  nTraceN : R
  transverseDot : R
  transverseRotated : R
  squareU : R
  crossUN : R
  squareN : R
  squareP : R

def ResidualSO2Coefficients.euler {R : Type} [CommRing R]
    (c : ResidualSO2Coefficients R) (a b p₂ p₃ kᵤ kₙ x₂ x₃ : R) : R × R × R × R :=
  (c.sourceU + c.uTraceU * kᵤ + c.uTraceN * kₙ + 2 * c.squareU * a + c.crossUN * b,
   c.sourceN + c.nTraceU * kᵤ + c.nTraceN * kₙ + c.crossUN * a + 2 * c.squareN * b,
   c.transverseDot * x₂ - c.transverseRotated * x₃ + 2 * c.squareP * p₂,
   c.transverseDot * x₃ + c.transverseRotated * x₂ + 2 * c.squareP * p₃)

theorem ResidualSO2Coefficients.eq_zero_of_euler_zero {R : Type} [Field R] [IsCharP R 0]
    (c : ResidualSO2Coefficients R)
    (h : ∀ a b p₂ p₃ kᵤ kₙ x₂ x₃, c.euler a b p₂ p₃ kᵤ kₙ x₂ x₃ = (0, 0, 0, 0)) :
    c = ⟨0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0⟩ := by
  have atZero := h 0 0 0 0 0 0 0 0
  have atU := h 1 0 0 0 0 0 0 0
  have atN := h 0 1 0 0 0 0 0 0
  have atP := h 0 0 1 0 0 0 0 0
  have atTraceU := h 0 0 0 0 1 0 0 0
  have atTraceN := h 0 0 0 0 0 1 0 0
  have atX := h 0 0 0 0 0 0 1 0
  letI : NoNatZeroDivisors R := Field.noNatZeroDivisors.ofIsCharPZero
  cases c
  grind [euler]

#print axioms ResidualSO2Coefficients.eq_zero_of_euler_zero

end UBT.Hamiltonian
