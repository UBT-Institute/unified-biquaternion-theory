import Mathlib

/-!
# Conditional full-rank split-jet TT energy compatibility

Finite algebraic core only.  The actual split-jet right inverse,
Palatini variational pullback, gravity-only Dirac reduction and
TT wave dynamics are proved separately in established repository
tracks, under an assumed Einstein/Palatini base action.

This file does NOT derive that action from a complex-Theta theory,
nor does it prove nonlinear stability or remove extra Theta ghosts.
-/

namespace UBTSplitJetTTWitness

/-- Exact determinant of a spatial triad I + h_TT/2, where
h_TT has entries (p,q;q,-p) in the first two directions. -/
noncomputable def tetradDetFactor (p q : ℝ) : ℝ :=
  1 - (p^2+q^2)/4

/-- Finite-amplitude transverse-traceless perturbations preserve
positive tetrad determinant in the indicated open neighborhood. -/
theorem tetrad_det_positive {p q : ℝ}
    (h : p^2+q^2 < 4) :
    0 < tetradDetFactor p q := by
  unfold tetradDetFactor
  linarith

/-- Flat-space quadratic Hamiltonian density on the 2-mode TT sector,
with mu=M_Pl²/4>0 and k2>=0.  vP,vQ are time derivatives, not canonical
momenta. A common overall positive normalization is irrelevant. -/
def ttEnergy (mu k2 p q vP vQ : ℝ) : ℝ :=
  mu * (vP^2 + vQ^2 + k2*(p^2+q^2))

theorem tt_energy_nonnegative
    {mu k2 p q vP vQ : ℝ}
    (hmu : 0 < mu) (hk : 0 ≤ k2) :
    0 ≤ ttEnergy mu k2 p q vP vQ := by
  unfold ttEnergy
  positivity

/-- The two *different* requirements are compatible in this
conditional gravity TT comparator: positive determinant and
nonnegative reduced TT energy. -/
theorem fullrank_compatible_with_positive_tt
    {mu k2 p q vP vQ : ℝ}
    (hmu : 0 < mu) (hk : 0 ≤ k2) (hsmall : p^2+q^2 < 4) :
    0 < tetradDetFactor p q ∧
      0 ≤ ttEnergy mu k2 p q vP vQ := by
  exact ⟨tetrad_det_positive hsmall, tt_energy_nonnegative hmu hk⟩

end UBTSplitJetTTWitness
