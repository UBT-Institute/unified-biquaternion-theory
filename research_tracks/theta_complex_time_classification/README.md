# Theta / complex-time analytic classification track

Status: active research track; no new canonical claim.

## Objective

Classify the actual UBT theta kernel rather than importing properties from a
similarly named Jacobi function.

Notation is separated from the start:
- \(\tau_{\rm UBT}=t+i\psi\): canonical UBT complex time;
- \(\tau_J\): Jacobi modular parameter in the upper half-plane;
- \(z\): Jacobi elliptic argument.

No equality among these variables is assumed.

## Required tests

1. Write the exact UBT/reduced kernel in \((z,\tau_J)\) notation where possible.
2. Determine convergence domain and singular set.
3. Check \(T:\tau_J\mapsto\tau_J+1\) and
   \(S:\tau_J\mapsto-1/\tau_J\).
4. Classify the kernel as scalar/vector-valued modular, Hermitian theta,
   mock-modular, or outside these classes.
5. Identify the lattice/quadratic form and any candidate Weil representation.
6. Examine the boundary \(\operatorname{Im}\tau_J\to0^+\) before invoking
   resurgent/Stokes continuation.
7. Keep the physical interpretation of \(\psi\) separate from analytic
   continuation.

## Lorentz guardrail

The companion no-go proves that strict frame-independent Cauchy--Riemann
holomorphy in \(t+i\psi\) is incompatible with generic 4D Lorentz-covariant
spacetime dependence if \(\psi\) is an independent Lorentz scalar.  Therefore
holomorphy is provisionally treated as a reduced theta-sector property, not a
universal microscopic constraint.

## Deliverable

A theorem or obstruction note with explicit transformation matrices, weight,
multiplier, domain, and proof-level status.  Numerical pattern matching alone
is insufficient.
