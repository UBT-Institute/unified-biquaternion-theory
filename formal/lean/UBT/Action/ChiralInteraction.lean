import UBT.Action.PsiRestHamiltonian

/-!
# Exact chiral-current algebra and winding covariance with even interactions

These are algebraic statements for the declared Dirac-sector bridge. They do
not identify internal quaternionic left multiplication with Lorentz chirality,
nor select a gauge coupling from the complete biquaternionic action.
-/

namespace UBT.Action.ChiralInteraction

section RingIdentities
variable {R : Type*} [Ring R]

theorem conjugate_product (C A B : R) (hc : C * C = 1) :
    C * (A * B) * C = (C * A * C) * (C * B * C) := by
  symm
  calc
    (C * A * C) * (C * B * C) = C * A * (C * C) * B * C := by noncomm_ring
    _ = C * (A * B) * C := by rw [hc]; noncomm_ring

theorem conjugate_odd (C G : R) (hc : C * C = 1)
    (ha : C * G + G * C = 0) : C * G * C = -G := by
  have hz := congrArg (fun X : R => X * C) ha
  have hg : G * C * C = G := by rw [mul_assoc, hc, mul_one]
  rw [add_mul, hg, zero_mul] at hz
  calc
    C * G * C = (C * G * C + G) - G := by abel
    _ = -G := by rw [hz, zero_sub]

theorem conjugate_complement (C : R) (hc : C * C = 1) :
    C * (1 - C) * C = 1 - C := by
  calc
    C * (1 - C) * C = C * C - (C * C) * C := by noncomm_ring
    _ = 1 - C := by rw [hc, one_mul]

theorem chiral_sandwich_zero (C G : R) (hc : C * C = 1)
    (ha : C * G + G * C = 0) : (1 - C) * G * (1 - C) = 0 := by
  calc
    (1 - C) * G * (1 - C) = G - (C * G + G * C) + C * G * C := by
      noncomm_ring
    _ = 0 := by rw [ha, conjugate_odd C G hc ha]; simp

/-- The nonzero left vector-current kernel is even, not odd, under C. -/
theorem left_current_even (C G₀ G : R) (hc : C * C = 1)
    (h₀ : C * G₀ + G₀ * C = 0) (hG : C * G + G * C = 0) :
    C * (G₀ * G * (1 - C)) * C = G₀ * G * (1 - C) := by
  rw [conjugate_product C (G₀ * G) (1 - C) hc,
    conjugate_product C G₀ G hc, conjugate_odd C G₀ hc h₀,
    conjugate_odd C G hc hG, conjugate_complement C hc]
  simp

theorem conjugate_even (C V : R) (hc : C * C = 1)
    (hv : C * V = V * C) : C * V * C = V := by
  rw [hv, mul_assoc, hc, mul_one]

/-- Adding the same C-even interaction in both winding sectors preserves
the conjugacy. Left/right asymmetric couplings are allowed by this premise. -/
theorem interacting_conjugation (C Hplus Hminus V : R) (hc : C * C = 1)
    (hh : C * Hplus * C = Hminus) (hv : C * V = V * C) :
    C * (Hplus + V) * C = Hminus + V := by
  rw [mul_add, add_mul, hh, conjugate_even C V hc hv]

/-- Transport of a whole eigenmatrix, including degenerate eigenspaces. -/
theorem eigenmatrix_transport (C A B X D : R) (hc : C * C = 1)
    (hab : C * A * C = B) (hx : A * X = X * D) :
    B * (C * X) = (C * X) * D := by
  rw [← hab]
  calc
    C * A * C * (C * X) = C * A * (C * C) * X := by noncomm_ring
    _ = C * (A * X) := by rw [hc]; noncomm_ring
    _ = (C * X) * D := by rw [hx, mul_assoc]
end RingIdentities

noncomputable section
open scoped Matrix
variable {n : Type*} [Fintype n] [DecidableEq n]
abbrev Mat := Matrix n n ℂ

def leftProjector (C : Mat) : Mat := (1 / 2 : ℂ) • (1 - C)

theorem normalized_sandwich_zero (C G : Mat) (hc : C * C = 1)
    (ha : C * G + G * C = 0) : leftProjector C * G * leftProjector C = 0 := by
  simp only [leftProjector, Matrix.smul_mul, Matrix.mul_smul, smul_smul]
  rw [chiral_sandwich_zero C G hc ha, smul_zero]

theorem normalized_left_current_even (C G₀ G : Mat) (hc : C * C = 1)
    (h₀ : C * G₀ + G₀ * C = 0) (hG : C * G + G * C = 0) :
    C * (G₀ * G * leftProjector C) * C = G₀ * G * leftProjector C := by
  simp only [leftProjector, Matrix.smul_mul, Matrix.mul_smul]
  rw [left_current_even C G₀ G hc h₀ hG]

/-- Explicit left-only potential; it need not have an equal right coupling. -/
theorem left_only_commutes (C : Mat) : C * leftProjector C = leftProjector C * C := by
  simp only [leftProjector, Matrix.smul_mul, Matrix.mul_smul]
  congr 1
  noncomm_ring

end UBT.Action.ChiralInteraction
