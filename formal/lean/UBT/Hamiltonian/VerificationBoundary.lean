import UBT.GR.VolumeVariation
import UBT.GR.VolumePrincipalSymbol
import UBT.GR.CompositeActionStationarity
import UBT.Action.PsiRestHamiltonian

/-!
# Hamiltonian verification boundary

This module collects already-formalized statements used in the October 2026
Hamiltonian research track. It does NOT assert that a unique microscopic
single-Theta action or its full Dirac--Bergmann Hamiltonian has been derived.

The first-jet density theorem concerns the specified determinant model with a
field-dependent additive connection shift; it is not a general statement about
torsionful composite actions.
-/

namespace UBT.Hamiltonian

open UBT.GR.VolumeVariation

/-- For the specified four-dimensional determinant-density model, the
common-covector second Frechet variation vanishes. This is a precise,
conditional principal-symbol result, not a complete Hamiltonian derivation. -/
theorem determinantDensityCommonCovectorSymbol
    (c : ℝ) (f : Vec → ℝ) (b : Vec → Mat)
    (x : Vec) (p : Mat) (k u v : Vec) :
    firstJetSymbol c f b x p k u v = 0 :=
  firstJetSymbol_eq_zero c f b x p k u v

/-- A surjective composite metric differential allows the metric field
equation to be recovered from stationarity in all composite directions. -/
theorem metricEquationFromSurjectiveCompositeVariation
    {R V W : Type*}
    (dMetric : V → W) (metricEL : W → R)
    (hSurj : Function.Surjective dMetric)
    (zero : R)
    (hStationary : ∀ v, metricEL (dMetric v) = zero) :
    ∀ w, metricEL w = zero :=
  UBT.GR.metricEquationOfCompositeStationarity
    dMetric metricEL hSurj zero hStationary

end UBT.Hamiltonian
