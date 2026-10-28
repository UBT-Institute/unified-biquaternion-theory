import Mathlib.Data.Real.Basic
import Mathlib.Data.Complex.Basic
import Mathlib.Algebra.Group.Pi.Basic
import Mathlib.Algebra.Group.Prod
import Mathlib.Tactic.Ext
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Abel

/-!
# Restricted Palatini--Holst closure

The first part proves the inverse of `star + b` on real Lorentz bivectors.
The second part proves identities for the already specified homogeneous
composite comparator, NOT for a selected microscopic single-Theta action.
No field-theoretic variation, constraint count, or physical stability theorem
is asserted by these finite-dimensional algebraic identities.
-/

noncomputable section

namespace UBT.Hamiltonian.PalatiniHolst

abbrev Triple := Fin 3 → ℝ
abbrev Bivector := Triple × Triple

/-- Electric/magnetic coordinates with the chosen Lorentz Hodge convention. -/
def star (z : Bivector) : Bivector := (z.2, fun i => -z.1 i)

def holst (b : ℝ) (z : Bivector) : Bivector :=
  (fun i => z.2 i + b * z.1 i, fun i => -z.1 i + b * z.2 i)

def inverseHolst (b : ℝ) (z : Bivector) : Bivector :=
  (fun i => (b * z.1 i - z.2 i) / (1 + b ^ 2),
   fun i => (b * z.2 i + z.1 i) / (1 + b ^ 2))

theorem star_square (z : Bivector) : star (star z) = -z := by
  ext i <;> simp [star]

theorem real_holst_denominator_pos (b : ℝ) : 0 < 1 + b ^ 2 := by positivity

theorem inverse_holst_left (b : ℝ) (z : Bivector) :
    inverseHolst b (holst b z) = z := by
  have h : (1 + b ^ 2) ≠ 0 := ne_of_gt (real_holst_denominator_pos b)
  ext i <;> dsimp [inverseHolst, holst] <;> field_simp <;> ring

theorem inverse_holst_right (b : ℝ) (z : Bivector) :
    holst b (inverseHolst b z) = z := by
  have h : (1 + b ^ 2) ≠ 0 := ne_of_gt (real_holst_denominator_pos b)
  ext i <;> dsimp [inverseHolst, holst] <;> field_simp <;> ring

/-- The entire real family has the same zero-source bivector equation.
Applying this to Cartan's equation still requires deriving that equation from
the actual action and proving the tetrad-to-torsion map invertible. -/
theorem holst_kernel (b : ℝ) (z : Bivector) : holst b z = 0 ↔ z = 0 := by
  constructor
  · intro h
    have hi := inverse_holst_left b z
    rw [h] at hi
    apply Prod.ext
    · funext i
      change z.1 i = 0
      simpa [inverseHolst] using congrArg (fun t : Bivector => t.1 i) hi.symm
    · funext i
      change z.2 i = 0
      simpa [inverseHolst] using congrArg (fun t : Bivector => t.2 i) hi.symm
  · rintro rfl
    ext i <;> simp [holst]

def potential (a V lam : ℝ) : ℝ := a + a ^ 3 / (3 * V ^ 2) - lam * a ^ 3 / 3

def lagrangian (C b a V lam av N : ℝ) : ℝ :=
  C * N * (potential a V lam + b ^ 2 * a * (a / V - av / N) ^ 2)

def momentumA (C b a V av N : ℝ) : ℝ :=
  2 * C * b ^ 2 * a * (av / N - a / V)

def momentumV (C b a V lam av N : ℝ) : ℝ :=
  C * (potential a V lam + b ^ 2 * a * ((a / V) ^ 2 - (av / N) ^ 2))

def reducedHamiltonian (C b a V lam p : ℝ) : ℝ :=
  a * p / V + p ^ 2 / (4 * C * b ^ 2 * a) - C * potential a V lam

theorem legendre_energy_zero (C b a V lam av N : ℝ) (hN : N ≠ 0) :
    momentumA C b a V av N * av + momentumV C b a V lam av N * N -
      lagrangian C b a V lam av N = 0 := by
  dsimp [momentumA, momentumV, lagrangian]
  field_simp
  ring

theorem velocity_reconstruction (C b a V av N : ℝ)
    (hC : C ≠ 0) (hb : b ≠ 0) (ha : a ≠ 0) :
    a / V + momentumA C b a V av N / (2 * C * b ^ 2 * a) = av / N := by
  dsimp [momentumA]
  field_simp
  ring

/-- The primary Hamiltonian constraint follows from the specified momenta;
it is not supplied as a hypothesis. Lean's total division extends this
algebraic identity to degenerate coefficients; its physical Hamiltonian
interpretation is restricted to the regular nonzero-coefficient patch. -/
theorem primary_constraint (C b a V lam av N : ℝ)
    :
    momentumV C b a V lam av N +
      reducedHamiltonian C b a V lam (momentumA C b a V av N) = 0 := by
  dsimp [momentumV, reducedHamiltonian, momentumA]
  field_simp
  ring

theorem reduced_energy_square (C b a V lam p : ℝ)
    (hC : C ≠ 0) (hb : b ≠ 0) (ha : a ≠ 0) :
    reducedHamiltonian C b a V lam p =
      (p + 2 * C * b ^ 2 * a ^ 2 / V) ^ 2 / (4 * C * b ^ 2 * a) -
        C * (potential a V lam + b ^ 2 * a ^ 3 / V ^ 2) := by
  dsimp [reducedHamiltonian]
  field_simp
  ring

/-- This minor of the three-primary-constraint bracket matrix is nonzero
throughout the nonzero-Holst regular patch. Its derivation as a Poisson
bracket is independently checked by the CAS; Lean proves its nonvanishing. -/
theorem second_class_minor_nonzero (C b a : ℝ)
    (hC : C ≠ 0) (hb : b ≠ 0) (ha : a ≠ 0) :
    (2 * C * b * a) ^ 2 ≠ 0 := by
  exact pow_ne_zero 2 (by exact mul_ne_zero (mul_ne_zero (mul_ne_zero (by norm_num) hC) hb) ha)

/-- `k` denotes the analytically continued squared Holst coefficient, not the
square of an arbitrary real number. The additional term is dF₂/dV. -/
def transformedHamiltonian (C k a V lam pi : ℝ) : ℝ :=
  a * (pi - 2 * C * k * a ^ 2 / V) / V +
    (pi - 2 * C * k * a ^ 2 / V) ^ 2 / (4 * C * k * a) -
    C * potential a V lam + 2 * C * k * a ^ 3 / (3 * V ^ 2)

theorem time_dependent_canonical_shift (C k a V lam pi : ℝ)
    (hC : C ≠ 0) (hk : k ≠ 0) (ha : a ≠ 0) :
    transformedHamiltonian C k a V lam pi =
      pi ^ 2 / (4 * C * k * a) - C * a + C * lam * a ^ 3 / 3 -
        C * (1 + k) * a ^ 3 / (3 * V ^ 2) := by
  dsimp [transformedHamiltonian, potential]
  field_simp
  ring

/-- Algebraic GR-FLRW matching at the continued squared coefficient -1.
This does not establish admissibility of a complex connection or its reality
conditions under the original Hermitian two-sided Theta derivative. -/
theorem self_dual_clock_hamiltonian (C a V lam pi : ℝ)
    (hC : C ≠ 0) (ha : a ≠ 0) :
    transformedHamiltonian C (-1) a V lam pi =
      -(pi ^ 2 / (4 * C * a)) - C * a + C * lam * a ^ 3 / 3 := by
  rw [time_dependent_canonical_shift C (-1) a V lam pi hC (by norm_num) ha]
  field_simp
  ring

theorem no_real_self_dual_square (b : ℝ) : b ^ 2 ≠ -1 := by
  nlinarith [sq_nonneg b]

def continuedSpinCoefficient (B d : ℝ) : ℂ :=
  ((B : ℂ) + Complex.I * (-1 + Complex.I * (d : ℂ))) / 2

/-- For any Hermitian Pauli matrix, the coefficient in Omega+Omega† changes
from B to B-d after the proposed imaginary-rotation continuation. -/
theorem hermitian_pair_after_continuation (B d : ℝ) :
    continuedSpinCoefficient B d +
      starRingEnd ℂ (continuedSpinCoefficient B d) = ((B - d : ℝ) : ℂ) := by
  have htwo : starRingEnd ℂ (2 : ℂ) = 2 := by
    exact Complex.conj_ofNat 2
  apply Complex.ext <;>
    simp [continuedSpinCoefficient, htwo, Complex.mul_re, Complex.mul_im] <;> ring

theorem generated_scale_after_continuation (a V r : ℝ) :
    V * (a / V - (a / V - r)) = V * r := by ring

theorem original_scale_requires_zero_defect (V d : ℝ) (hV : V ≠ 0) :
    V * d = 0 ↔ d = 0 := by
  exact mul_eq_zero.trans (or_iff_right hV)

/-- After the original Hermitian readout has restricted the closed-FLRW
clock ansatz to a(V)=c*V, its GR-clock scale Euler residual cannot vanish at
two distinct positive clock values. This is a restricted ansatz obstruction,
not a no-go for real slices of biquaternionic geometry in general. -/
theorem no_closed_real_constant_ratio_trajectory (c lam V W : ℝ)
    (hV : 0 < V) (hW : 0 < W) (hVW : V ≠ W)
    (hELV : c ^ 2 + 1 - lam * c ^ 2 * V ^ 2 = 0)
    (hELW : c ^ 2 + 1 - lam * c ^ 2 * W ^ 2 = 0) : False := by
  have hpositive : 0 < c ^ 2 + 1 := by positivity
  have hcoefficient : lam * c ^ 2 ≠ 0 := by
    intro hz
    have hzero : lam * c ^ 2 * V ^ 2 = 0 := by rw [hz]; simp
    rw [hzero] at hELV
    linarith
  have hdifference : (lam * c ^ 2) * (V ^ 2 - W ^ 2) = 0 := by
    nlinarith [hELV, hELW]
  have hsquares : V ^ 2 = W ^ 2 :=
    sub_eq_zero.mp ((mul_eq_zero.mp hdifference).resolve_left hcoefficient)
  exact hVW ((sq_eq_sq₀ (le_of_lt hV) (le_of_lt hW)).mp hsquares)

/-- A central anti-Hermitian U(1) generator cancels in the pure pair. -/
theorem temporal_center_phase_cancels (u : ℝ) :
    Complex.I * (u : ℂ) + starRingEnd ℂ (Complex.I * (u : ℂ)) = 0 := by
  apply Complex.ext <;> simp

/-- A real central generator instead gives a dilation, not a phase. -/
theorem temporal_center_real_is_dilation (u : ℝ) :
    (u : ℂ) + starRingEnd ℂ (u : ℂ) = ((2 * u : ℝ) : ℂ) := by
  simp
  ring

/-- For a nonzero real boost, membership of the spatial derivative in
i Herm_2 forces the scalar coefficient to have zero real part. -/
theorem scalar_phase_spatial_reality (z : ℂ) (B : ℝ) (hB : B ≠ 0)
    (h : (z * (B : ℂ)).re = 0) : z.re = 0 := by
  have hz : z.re * B = 0 := by simpa using h
  exact (mul_eq_zero.mp hz).resolve_right hB

/-- Cancellation of the apparent extra d g term under a simultaneous
right-carrier connection transformation. No reality-preserving gauge group
is inferred from this algebraic identity. -/
theorem right_texture_covariance {R : Type*} [Ring R]
    (x dx A B g dg ginv : R) (hginv : g * ginv = 1) :
    (dx * g + x * dg) + A * (x * g) -
      (x * g) * (ginv * B * g + ginv * dg) =
      (dx + A * x - x * B) * g := by
  have hcancel : (x * g) * ginv = x := by
    rw [mul_assoc, hginv, mul_one]
  simp only [mul_add, add_mul, sub_mul]
  simp only [← mul_assoc, hcancel]
  abel

/-- The two independent homogeneous Cartan equations have the ordinary
torsion-free solution for every real coefficient. This applies only when
the lapse and boost variations are both actually available. -/
theorem independent_real_Cartan_solution (b B w x : ℝ)
    (hB : B + b * w - x = 0) (hw : -w + b * (B - x) = 0) :
    w = 0 ∧ B = x := by
  have hp : b * (B + b * w - x) = 0 := by rw [hB]; ring
  have hproduct : (1 + b ^ 2) * w = 0 := by nlinarith [hp, hw]
  have hwzero : w = 0 :=
    (mul_eq_zero.mp hproduct).resolve_left (ne_of_gt (real_holst_denominator_pos b))
  constructor
  · exact hwzero
  · apply sub_eq_zero.mp
    simpa [hwzero] using hB

/-- The pure pair commutes with the involution on the WHOLE carrier, not
only on scalar matrices. Thus an anti-Hermitian generated tetrad receives
no derivative contribution from the Hermitian part of Theta. -/
theorem pure_pair_star_covariance {R : Type*} [Ring R] [StarRing R]
    (x dx A : R) :
    Star.star (dx + A * x + x * Star.star A) =
      Star.star dx + A * Star.star x + Star.star x * Star.star A := by
  simp only [star_add, star_mul, star_star]
  abel

end UBT.Hamiltonian.PalatiniHolst
