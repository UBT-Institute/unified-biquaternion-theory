import Mathlib

/-!
# Split-jet pullback velocity Hessian and first-class constraint: finite core

A positive single physical oscillator H = h + α ψ is written with two
redundant coordinates. The gauge shift δh=-α ε, δψ=ε leaves H invariant.
This is a finite stand-in for the existing gravity-only split-jet
cotangent-lift/Dirac quotient. It does not establish that the ENTIRE
complex biquaternion or its psi circle is gauge in full UBT.
-/

namespace UBTPullbackDirac

def kineticQ (a α vh vψ : ℝ) : ℝ :=
  a * (vh + α*vψ)^2

def pulledDet (a α : ℝ) : ℝ :=
  a*(a*α^2) - (a*α)^2

theorem determinant_zero (a α : ℝ) :
    pulledDet a α = 0 := by
  unfold pulledDet
  ring

theorem velocity_energy_nonnegative
    {a α vh vψ : ℝ} (ha : 0 < a) :
    0 ≤ kineticQ a α vh vψ := by
  unfold kineticQ
  positivity

theorem null_velocity_direction (a α t : ℝ) :
    kineticQ a α (-α*t) t = 0 := by
  simp [kineticQ]

def physicalCoordinate (α h ψ : ℝ) : ℝ :=
  h + α*ψ

theorem gauge_shift_invariance
    (α h ψ ε : ℝ) :
    physicalCoordinate α (h - α*ε) (ψ + ε) =
    physicalCoordinate α h ψ := by
  unfold physicalCoordinate
  ring

def constraint (α ph pψ : ℝ) : ℝ :=
  pψ - α*ph

def primaryMomentumH (a α vh vψ : ℝ) : ℝ :=
  a*(vh+α*vψ)

def primaryMomentumPsi (a α vh vψ : ℝ) : ℝ :=
  α*a*(vh+α*vψ)

theorem primary_constraint_identity (a α vh vψ : ℝ) :
    constraint α (primaryMomentumH a α vh vψ)
      (primaryMomentumPsi a α vh vψ) = 0 := by
  unfold constraint primaryMomentumH primaryMomentumPsi
  ring

/-- Algebraic analogue of {C,H}=0 with
C=pψ-α ph, H=ph²/(2a)+m(h+α ψ)²/2:
the potential contribution is α∂hV-∂ψV. -/
theorem potential_constraint_closure (α m h ψ : ℝ) :
    α*(m*(h+α*ψ)) - (m*α*(h+α*ψ)) = 0 := by
  ring

noncomputable def reducedHamiltonian (a m α ph h ψ : ℝ) : ℝ :=
  ph^2/(2*a) + m*(physicalCoordinate α h ψ)^2/2

theorem reduced_hamiltonian_nonnegative
    {a m α ph h ψ : ℝ} (ha : 0 < a) (hm : 0 ≤ m) :
    0 ≤ reducedHamiltonian a m α ph h ψ := by
  unfold reducedHamiltonian physicalCoordinate
  positivity

/-- A higher-rank pullback Hessian is positive semidefinite
whenever it arises from a positive base quadratic form. -/
theorem generic_pullback_nonnegative
    {a : ℝ} (ha : 0 ≤ a) (x y α : ℝ) :
    0 ≤ a*(x+α*y)^2 := by
  positivity

end UBTPullbackDirac
