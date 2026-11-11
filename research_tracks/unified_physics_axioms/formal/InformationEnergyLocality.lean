import Mathlib

/-!
# Conditional energy/information routing optimization

This model compares one long transmission with two half-distance
transmissions at a fixed useful payload. The link-cost law is an
assumption, NOT a derivation from UBT, the speed of light, or Landauer.
No physical spacetime geometry is reconstructed here.
-/

namespace UBTInformationEfficiency

/-- Assumed per-hop overhead alpha and convex quadratic transport cost beta*d².
The distance and its metric meaning are INPUTS, not derived. -/
def directCost (alpha beta d : ℝ) : ℝ :=
  alpha + beta * d ^ 2

/-- One intermediate relay, two equal segments. -/
def relayCost (alpha beta d : ℝ) : ℝ :=
  2 * alpha + beta * d ^ 2 / 2

/-- An exact selection threshold: relaying wins iff the convex
transport saving exceeds its extra interaction overhead. -/
theorem relay_cheaper_iff (alpha beta d : ℝ) :
    relayCost alpha beta d < directCost alpha beta d ↔
      2 * alpha < beta * d ^ 2 := by
  unfold relayCost directCost
  constructor <;> intro h <;> linarith

/-- Counterexample: with no distance-dependent transmission cost,
an additional hop is always more expensive when overhead is positive. -/
theorem direct_wins_no_transport
    (alpha d : ℝ) (h : 0 < alpha) :
    directCost alpha 0 d < relayCost alpha 0 d := by
  unfold directCost relayCost
  nlinarith

/-- Positive transport cost can favor relaying in an explicit example. -/
theorem numerical_relay_wins :
    relayCost 1 1 4 < directCost 1 1 4 := by
  norm_num [relayCost, directCost]

/-- A purely local-cost principle without transport dependence
cannot force relay selection; it gives the opposite preference. -/
theorem numerical_direct_wins :
    directCost 1 0 4 < relayCost 1 0 4 := by
  norm_num [relayCost, directCost]

end UBTInformationEfficiency
