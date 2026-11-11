import Mathlib

/-!
# Algebraic biquaternion metric: exact central Jordan identity

A biquaternion is represented as a complex scalar plus three complex
Hamilton basis components.  This file does not presume a physical
reality condition, a covariant connection, dynamics, or an independent
volume density. The theorem holds over the full complex carrier.
-/

namespace UBTBiquaternion

structure BQ where
  s : ℂ
  u : ℂ
  v : ℂ
  w : ℂ

def mul (a b : BQ) : BQ :=
  ⟨a.s*b.s-a.u*b.u-a.v*b.v-a.w*b.w,
   a.s*b.u+a.u*b.s+a.v*b.w-a.w*b.v,
   a.s*b.v-a.u*b.w+a.v*b.s+a.w*b.u,
   a.s*b.w+a.u*b.v-a.v*b.u+a.w*b.s⟩

/-- Quaternion conjugation: DOES NOT conjugate complex coefficients. -/
def sharp (a : BQ) : BQ := ⟨a.s,-a.u,-a.v,-a.w⟩

def central (z : ℂ) : BQ := ⟨z,0,0,0⟩

/-- Symmetric conjugate product. -/
noncomputable def jordan (a b : BQ) : BQ :=
  ⟨((mul (sharp a) b).s + (mul (sharp b) a).s)/2,
   ((mul (sharp a) b).u + (mul (sharp b) a).u)/2,
   ((mul (sharp a) b).v + (mul (sharp b) a).v)/2,
   ((mul (sharp a) b).w + (mul (sharp b) a).w)/2⟩

def metricPairing (a b : BQ) : ℂ :=
  a.s*b.s+a.u*b.u+a.v*b.v+a.w*b.w

/-- The metric-valued Jordan product is CENTRAL for ALL complex biquaternions.
It is not necessarily real without a Lorentz-real restriction. -/
theorem jordan_is_central (a b : BQ) :
    jordan a b = central (metricPairing a b) := by
  cases a with
  | mk as au av aw =>
    cases b with
    | mk bs bu bv bw =>
      simp only [jordan, mul, sharp, metricPairing, central, BQ.mk.injEq]
      constructor
      · ring
      constructor
      · ring
      constructor
      · ring
      · ring

/-- Symmetry of the complex bilinear metric. -/
theorem metricPairing_symmetric (a b : BQ) :
    metricPairing a b = metricPairing b a := by
  dsimp [metricPairing]
  ring

/-- One complex scalar alone does not imply a real Lorentzian metric:
the scalar of an arbitrary complex biquaternion can be complex. -/
theorem complex_scalar_example :
    metricPairing ⟨Complex.I,0,0,0⟩ ⟨1,0,0,0⟩ = Complex.I := by
  simp [metricPairing]

end UBTBiquaternion
