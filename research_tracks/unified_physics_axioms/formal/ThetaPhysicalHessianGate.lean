import Mathlib

/-!
# Theta partition-function stability gate for the existing minimal action

The theorems below prove only sign consequences of the generalized
mass-squared eigenvalues calculated in the existing fixed-background
8-real-field quartic UBT comparator. They do not derive that Hessian,
the connection, a positive physical mode matrix or an action.
-/

namespace UBTThetaHessianGate

/-- Generalized radial mass squared, for nonzero kinetic coefficient c. -/
noncomputable def radialMassSq (lambda1 lambda2 r c : ℝ) : ℝ :=
  4 * (4 * lambda1 + lambda2) * r ^ 2 / c

/-- Threefold generalized transverse mass squared. -/
noncomputable def transverseMassSq (lambda2 r c : ℝ) : ℝ :=
  -(4 * lambda2 * r ^ 2) / c

/-- With positive kinetic normalization, the radial and transverse
    generalized eigenvalues have opposite signs. -/
theorem positive_c_opposite_signs
    {lambda1 lambda2 r c : ℝ}
    (h1 : 0 ≤ lambda1) (h2 : 0 < lambda2)
    (hr : 0 < r) (hc : 0 < c) :
    0 < radialMassSq lambda1 lambda2 r c ∧
      transverseMassSq lambda2 r c < 0 := by
  constructor
  · unfold radialMassSq
    positivity
  · unfold transverseMassSq
    apply div_neg_of_neg_of_pos
    · have hnum : 0 < 4 * lambda2 * r ^ 2 := by positivity
      linarith
    · exact hc

/-- Flipping the kinetic normalization does not remove the negative
    generalized eigenvalue: the radial mode then becomes negative. -/
theorem negative_c_opposite_signs
    {lambda1 lambda2 r c : ℝ}
    (h1 : 0 ≤ lambda1) (h2 : 0 < lambda2)
    (hr : 0 < r) (hc : c < 0) :
    radialMassSq lambda1 lambda2 r c < 0 ∧
      0 < transverseMassSq lambda2 r c := by
  constructor
  · unfold radialMassSq
    apply div_neg_of_pos_of_neg
    · positivity
    · exact hc
  · unfold transverseMassSq
    apply div_pos_of_neg_of_neg
    · have hnum : 0 < 4 * lambda2 * r ^ 2 := by positivity
      linarith
    · exact hc

/-- With c nonzero, there always exists a negative generalized eigenvalue.
    This is a sign diagnostic, not a full constraint-reduced physical spectrum. -/
theorem negative_mass_direction
    {lambda1 lambda2 r c : ℝ}
    (h1 : 0 ≤ lambda1) (h2 : 0 < lambda2)
    (hr : 0 < r) (hc : c ≠ 0) :
    radialMassSq lambda1 lambda2 r c < 0 ∨
      transverseMassSq lambda2 r c < 0 := by
  rcases lt_or_gt_of_ne hc with hneg | hpos
  · exact Or.inl (negative_c_opposite_signs h1 h2 hr hneg).1
  · exact Or.inr (positive_c_opposite_signs h1 h2 hr hpos).2

end UBTThetaHessianGate
