<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Complex-time holomorphy versus Lorentz covariance

**Status:** exact no-go for global frame-independent holomorphy with a
Lorentz-scalar imaginary-time fiber. This narrows the theta/complex-time audit
and directly affects the SU(3) jet-multiplicity route.

## 1. Assumptions to be tested

Assume:

1. (t=x^0) is ordinary physical time and transforms under four-dimensional
   Lorentz boosts;
2. (psi) is an independent Lorentz-scalar fiber coordinate;
3. a generic field satisfies strict holomorphy in
   [
   	au=t+ipsi
   ]
   in every inertial frame.

The Cauchy--Riemann condition is then
[
partial_psiTheta=i,partial_tTheta.
]

## 2. Boost no-go

Consider a boost in the (x) direction. With a conventional sign choice,
[
partial_{t'}=gamma(partial_t+vpartial_x).
]
If (psi) is a Lorentz scalar, the same holomorphy condition in the boosted
frame requires
[
partial_psiTheta=i,partial_{t'}Theta
=igamma(partial_t+vpartial_x)Theta.
]

Combining with the unboosted Cauchy--Riemann equation gives
[
(gamma-1)partial_tTheta+gamma v,partial_xTheta=0.
]
Applying the same argument to the opposite boost (-v) gives
[
(gamma-1)partial_tTheta-gamma v,partial_xTheta=0.
]

For every nontrivial boost,
[
v
e0,qquadgamma
e1,
]
the two equations imply
[
partial_tTheta=0,qquad
partial_xTheta=0,
]
and hence
[
partial_psiTheta=0.
]
Repeating for boosts in the other spatial directions yields a spacetime-
constant field on the connected patch.

Therefore
[
oxed{
	ext{strict holomorphy in }t+ipsi
+	ext{ scalar }psi
+	ext{ frame-independent Lorentz covariance}
}
]
admits no generic spacetime-dependent field.

## 3. What the theorem does not say

It does not forbid:

- using a Jacobi-theta holomorphic variable in a reduced/preferred-frame
  spectral model;
- analytic continuation in a parameter called complex time;
- a fiber coordinate (psi) whose dynamics is not constrained by global
  Cauchy--Riemann equations;
- a fully complexified spacetime in which the imaginary coordinate partners
  transform together as a Lorentz vector.

It forbids silently using all three claims simultaneously:
generic 4D Lorentz covariance, scalar independent (psi), and strict
holomorphy in (t+ipsi) in every frame.

## 4. Two consistent architecture branches

### Branch A — Lorentz-scalar fiber psi

Treat
[
Theta=Theta(x^mu,psi)
]
with (psi) an independent Lorentz scalar. Then (partial_psiTheta) is an
independent fiber jet unless the action imposes another constraint.

Theta/Jacobi holomorphy may still appear in a reduced solution class or
spectral transform, but is not a universal microscopic Cauchy--Riemann
constraint.

This branch keeps open the Lorentz-compatible colour candidate
[
left(
Box_4Theta^ho, 
partial^hopartial_sigmaTheta^sigma, 
partial_psi^2Theta^ho
ight),
]
whose three copy indices have the same derivative order.

### Branch B — covariantly complexified spacetime

If holomorphy is to be fundamental and Lorentz covariant, the imaginary
coordinate partners must transform with the real spacetime coordinates, e.g.
schematically
[
z^mu=x^mu+i y^mu.
]
Then (y^0=psi) is not an isolated Lorentz scalar: boosts mix it with the
imaginary spatial partners.

This is a larger coordinate architecture and must be declared explicitly.
It is not equivalent to the minimal model with one independent scalar
imaginary-time fiber.

## 5. Repository consequence

The statement in `canonical/fields/theta_field.tex` that the GR recovery
assumes classical holomorphy in (	au) must be read as a **restricted-sector
assumption**, not a global Lorentz-covariant microscopic condition, unless the
full complexified-coordinate transformation law is supplied.

Likewise the reduced Jacobi-theta bridge is not evidence that the microscopic
field must obey a frame-independent Cauchy--Riemann equation in physical
(t,psi).

## 6. Decision for P1/P2

The current minimal route should use Branch A provisionally:

- keep (t) as physical Lorentz time;
- treat (psi) as an independent internal/fiber variable in the action-level
  audit;
- do not impose strict microscopic holomorphy;
- reserve holomorphy for declared reduced theta sectors.

Then test whether the action supplies a kinetic/measure structure in the
(psi) direction. If it does, the same-order three-copy Lorentz multiplicity
becomes a legitimate SU(3) candidate. If it does not, the colour bridge fails.

A future full-complex-spacetime branch can be studied separately, but it must
not be conflated with the minimal complex-time-fiber theory.
