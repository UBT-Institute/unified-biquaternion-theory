import Mathlib

/-!
# Conditional stable radial Hamiltonian versus composite rank obstruction

This file proves finite algebraic statements in the already documented
auxiliary-connection, fixed-background Lorentz-real scalar branch.
It does not prove the consistency of that slice, energy conservation for
the full PDE, or stability of the full composite UBT system.
-/

namespace UBTRadialStability

/-- c>0 kinetic normalization and A>0 double-well potential.
p is canonical momentum; g2 is squared spatial gradient magnitude
and is assumed nonnegative. The vacuum energy has been subtracted. -/
noncomputable def reducedEnergy (c A r rho p g2 : ℝ) : ℝ :=
  p^2 / (4*c) + c*g2 + A*(rho^2-r^2)^2

/-- The full nonlinear radial energy density is nonnegative, assuming
a prescribed positive spatial metric and the already reduced scalar branch. -/
theorem reduced_energy_nonnegative
    {c A r rho p g2 : ℝ}
    (hc : 0 < c) (hA : 0 < A) (hg : 0 ≤ g2) :
    0 ≤ reducedEnergy c A r rho p g2 := by
  unfold reducedEnergy
  positivity

/-- Exactly at the positive radial vacuum, with no momentum or gradient,
the vacuum-relative energy vanishes. -/
theorem vacuum_zero_energy
    (c A r : ℝ) (hc : 0 < c) :
    reducedEnergy c A r r 0 0 = 0 := by
  simp [reducedEnergy]

/-- The squared frequency of any scalar linear Fourier mode is positive
for nonnegative spatial Laplacian eigenvalue k2. This is a *radial*
linear stability result on a prescribed time-independent background. -/
noncomputable def radialFrequencySq (c A r k2 : ℝ) : ℝ :=
  k2 + 4*A*r^2/c

theorem radial_mode_omega_sq_positive
    {c A r k2 : ℝ}
    (hc : 0 < c) (hA : 0 < A) (hr : 0 < r) (hk : 0 ≤ k2) :
    0 < radialFrequencySq c A r k2 := by
  unfold radialFrequencySq
  positivity

/-- Any pair of columns constructed from the same single scalar
has vanishing 2x2 minors. This is the rank-one tetrad obstruction. -/
theorem scalar_outer_product_minor_zero
    (a b u v : ℝ) :
    (a*u)*(b*v) - (a*v)*(b*u) = 0 := by
  ring

/-- A rank-one scalar readout cannot be an invertible two-direction
block; this elementary algebraic gate excludes full tetrad rank. -/
theorem no_nonzero_scalar_outer_minor
    (a b u v : ℝ) :
    ¬ ((a*u)*(b*v) - (a*v)*(b*u) ≠ 0) := by
  rw [scalar_outer_product_minor_zero]
  simp

end UBTRadialStability
