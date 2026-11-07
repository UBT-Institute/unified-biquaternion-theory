import Lean

/-!
# Finite algebra for the trace-tuned two-carrier cone

These polynomial identities are used in the trace condition, the shift Schur
complement and the nonzero bracket norm of a characteristic amplitude.
-/

namespace UBT.Hamiltonian

open Lean.Grind

theorem residualSO2TraceConeSquare {R : Type} [CommRing R] (kLong lam odd : R) :
    kLong * (2 * kLong - lam^2 + (lam + 2 * odd)^2)
      - 2 * (2 * kLong - lam^2) * odd^2 =
    2 * (kLong + lam * odd)^2 := by
  grind

theorem residualSO2TunedShiftSchur {R : Type} [CommRing R]
    (shear electric odd k w qSquared : R) :
    (shear * qSquared + electric * k^2) * (electric * w^2 - shear * qSquared)
      - (electric * w * k)^2 - (odd * qSquared)^2 =
    qSquared * (shear * electric * (w^2 - k^2) - (shear^2 + odd^2) * qSquared) := by
  grind

theorem residualSO2TunedBracketNorm {R : Type} [CommRing R] (a b z₂ z₃ : R) :
    (a * z₂ - b * z₃)^2 + (a * z₃ + b * z₂)^2 =
    (a^2 + b^2) * (z₂^2 + z₃^2) := by
  grind

#print axioms residualSO2TraceConeSquare
#print axioms residualSO2TunedShiftSchur
#print axioms residualSO2TunedBracketNorm

end UBT.Hamiltonian
