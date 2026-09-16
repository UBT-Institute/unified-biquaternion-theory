import Mathlib

/-!
# Correct rest-mode Hamiltonian of the declared free psi-sector candidate

One 2x2 chirality block is used for each of the two spectator spin components.
This is finite matrix algebra, not a new fundamental field or a derivation
of the candidate Dirac sector from the full biquaternionic action.
-/

noncomputable section
namespace UBT.Action.PsiRestHamiltonian
open scoped Matrix

abbrev Mat := Matrix (Fin 2) (Fin 2) ℂ

def gamma0 : Mat := !![0, 1; 1, 0]
def gamma5 : Mat := !![-1, 0; 0, 1]
def hamiltonian (m : ℝ) : Mat :=
  !![0, -Complex.I * (m : ℂ); Complex.I * (m : ℂ), 0]

theorem derived_hamiltonian (m : ℝ) :
    hamiltonian m = (-Complex.I * (m : ℂ)) • (gamma0 * gamma5) := by
  ext i j : 2
  fin_cases i <;> fin_cases j <;>
    simp [hamiltonian, gamma0, gamma5, Matrix.vecMul, dotProduct, Fin.sum_univ_succ]

theorem hermitian (m : ℝ) : (hamiltonian m)ᴴ = hamiltonian m := by
  ext i j : 2
  fin_cases i <;> fin_cases j <;> simp [hamiltonian, Matrix.conjTranspose_apply]

theorem square (m : ℝ) : hamiltonian m * hamiltonian m =
    ((m : ℂ) ^ 2) • (1 : Mat) := by
  ext i j : 2
  fin_cases i <;> fin_cases j <;>
    simp [hamiltonian, Matrix.vecMul, dotProduct, Fin.sum_univ_succ,
      mul_assoc, ← pow_two]

theorem characteristic (m E : ℝ) :
    (((E : ℂ) • (1 : Mat)) - hamiltonian m).det =
      (E : ℂ) ^ 2 - (m : ℂ) ^ 2 := by
  simp [hamiltonian, Matrix.det_fin_two, mul_assoc, ← pow_two]

theorem winding_conjugation (m : ℝ) :
    gamma5 * hamiltonian m * gamma5 = hamiltonian (-m) := by
  ext i j : 2
  fin_cases i <;> fin_cases j <;>
    simp [hamiltonian, gamma5, Matrix.vecMul, dotProduct, Fin.sum_univ_succ]

/-- Every nonzero-energy eigenstate has equal chiral weights, componentwise. -/
theorem equal_chiral_weights (m E : ℝ) (L R : ℂ) (hE : E ≠ 0)
    (hL : (-Complex.I * (m : ℂ)) * R = (E : ℂ) * L)
    (hR : (Complex.I * (m : ℂ)) * L = (E : ℂ) * R) :
    ‖L‖ ^ 2 = ‖R‖ ^ 2 := by
  have h₁ := congrArg (fun z : ℂ => (z * star L).re) hL
  have h₂ := congrArg (fun z : ℂ => (z * star R).re) hR
  simp [Complex.mul_re, Complex.mul_im] at h₁ h₂
  have he : E * ((L.re ^ 2 + L.im ^ 2) - (R.re ^ 2 + R.im ^ 2)) = 0 := by
    nlinarith [h₁, h₂]
  have hz := (mul_eq_zero.mp he).resolve_left hE
  simp [Complex.sq_norm, Complex.normSq_apply]
  linarith

theorem zero_energy_trivial (m : ℝ) (L R : ℂ) (hm : m ≠ 0)
    (hL : (-Complex.I * (m : ℂ)) * R = 0)
    (hR : (Complex.I * (m : ℂ)) * L = 0) : L = 0 ∧ R = 0 := by
  have hm' : (m : ℂ) ≠ 0 := by exact_mod_cast hm
  exact ⟨(mul_eq_zero.mp hR).resolve_left (mul_ne_zero Complex.I_ne_zero hm'),
    (mul_eq_zero.mp hL).resolve_left (mul_ne_zero (neg_ne_zero.mpr Complex.I_ne_zero) hm')⟩

def annihilation : Mat := !![0, 1; 0, 0]

/-- The actual one-mode CAR identity, rather than a prescribed energy modulus. -/
theorem car : annihilation * annihilationᴴ + annihilationᴴ * annihilation = 1 := by
  ext i j : 2
  fin_cases i <;> fin_cases j <;>
    simp [annihilation, Matrix.vecMul, dotProduct, Fin.sum_univ_succ]

theorem negative_mode_reordering (E : ℝ) :
    (- (E : ℂ)) • (annihilation * annihilationᴴ) + (E : ℂ) • (1 : Mat) =
      (E : ℂ) • (annihilationᴴ * annihilation) := by
  rw [← car, smul_add]
  module

end UBT.Action.PsiRestHamiltonian
