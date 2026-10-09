# Theta-energy torus-modulus selection programme

Status: conditional research programme.

## Guardrail

The canonical UBT variable `tau=t+i psi` is not automatically the complex
modulus of a spatial torus. Introduce a separate symbol `tau_mod` until a
derivation identifies them.

## Target

Find a genuine compact modulus in the UBT action, Hessian, determinant or
partition function and derive an effective potential
[
V_{\rm eff}(\tau_{\rm mod},\bar\tau_{\rm mod}).
]

Then solve
[
\partial_{\tau_{\rm mod}}V_{\rm eff}=0
]
and test the Hessian at candidate modular fixed points such as the square and
hexagonal lattices.

## Required proof steps

1. derive the compact lattice/modulus from UBT geometry;
2. derive, rather than postulate, the theta/lattice sum entering V_eff;
3. prove the relevant modular covariance/invariance;
4. establish boundedness/coercivity or state flat directions;
5. certify local/global minima analytically or with rigorous interval bounds.

## Exit criterion

Either a selected modulus with stated assumptions and certified stability, or a
no-go theorem that the current canonical action leaves the modulus undetermined.


## First result — overall scale no-go

The historical one-loop radius-stabilisation route is now ruled out in its
minimal form.

For a uniformly rescaled massless torus Laplacian, the zero-mode-subtracted
Epstein zeta satisfies E_d(0)=-1 and the determinant depends only
logarithmically on the overall radius.  There is no finite isolated minimum.
If the logarithmic potential is symmetrised under radius inversion, the scale
direction is flat for every radius.

Therefore P4 is narrowed to a genuine dimensionless shape/complex-structure
modulus or to action-derived interactions/backreaction that break pure scale
covariance.  See one_loop_scale_no_go.md.
