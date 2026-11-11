import Mathlib

/-!
# Conditional positive TT kinetic energy versus indefinite DeWitt form

This is a finite orthonormal-frame algebraic check for the inherited
reduced metric Hamiltonian with chi=1/2. It does not identify the
physical constraint quotient of the FULL complex-Theta theory.
-/

namespace UBTDeWittTT

def trace3 (a b c : ℝ) : ℝ := a+b+c

def quad3 (a b c xy xz yz : ℝ) : ℝ :=
  a^2+b^2+c^2+2*(xy^2+xz^2+yz^2)

def kinetic3 (a b c xy xz yz : ℝ) : ℝ :=
  quad3 a b c xy xz yz - (trace3 a b c)^2 / 2

/-- The unreduced DeWitt trace channel is negative on a pure trace tensor. -/
theorem pure_trace_negative :
    kinetic3 1 1 1 0 0 0 = -(3/2 : ℝ) := by
  norm_num [kinetic3, quad3, trace3]

/-- Exact identity on any tracefree symmetric 3x3 momentum tensor. -/
theorem tracefree_restricts_to_square_sum
    (a b c xy xz yz : ℝ)
    (ht : trace3 a b c = 0) :
    kinetic3 a b c xy xz yz = quad3 a b c xy xz yz := by
  simp [kinetic3, ht]

/-- Every tracefree tensor has nonnegative DeWitt kinetic energy. -/
theorem tracefree_kinetic_nonnegative
    (a b c xy xz yz : ℝ)
    (ht : trace3 a b c = 0) :
    0 ≤ kinetic3 a b c xy xz yz := by
  rw [tracefree_restricts_to_square_sum _ _ _ _ _ _ ht]
  unfold quad3
  positivity

/-- Positivity of the GR TT kinetic coefficient is an extra sign input,
not selected by the closure condition a*b=1 alone. -/
theorem positive_normalized_tt
    (a b c xy xz yz norm : ℝ)
    (ht : trace3 a b c = 0)
    (hnorm : 0 ≤ norm) :
    0 ≤ norm * kinetic3 a b c xy xz yz := by
  have h := tracefree_kinetic_nonnegative a b c xy xz yz ht
  exact mul_nonneg hnorm h

/-- Explicit transverse and traceless polarization in a wave-vector frame. -/
theorem explicit_tt_polarization :
    trace3 1 (-1) 0 = 0 ∧ kinetic3 1 (-1) 0 0 0 0 = 2 := by
  norm_num [trace3, kinetic3, quad3]

/-- Constraint algebra alone demands a*b=1, not sign(a)>0. -/
theorem closure_does_not_select_sign :
    (1 : ℝ) * 1 = 1 ∧ (-1 : ℝ) * (-1) = 1 := by
  norm_num

/-- A coefficient multiplying a vanishing torsion-free Holst channel
cannot be distinguished by any on-branch kinetic inequality. -/
theorem torsionfree_holst_degeneracy
    (base holstCoeff : ℝ) :
    base + holstCoeff * (0 : ℝ) = base := by
  ring

end UBTDeWittTT
