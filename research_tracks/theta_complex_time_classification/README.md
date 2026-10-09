# Theta / complex-time analytic classification track

Status: active research track; no new canonical claim.

## Objective

Classify the actual UBT theta kernel rather than importing properties from a
similarly named Jacobi function.

The first task is notation separation:
- `tau_UBT = t + i psi` is canonical complex time;
- Jacobi `tau_J` is a modular parameter in the upper half-plane;
- `z` is the Jacobi elliptic argument.

No equality among these variables is assumed.

## Tests

1. Write the exact UBT/reduced kernel in `(z,tau_J)` notation where possible.
2. Determine convergence domain and singular set.
3. Check T and S transformations:
   `tau_J -> tau_J+1` and `tau_J -> -1/tau_J`.
4. Determine whether the kernel is scalar modular, vector-valued modular,
   Hermitian theta, mock-modular, or outside these classes.
5. Identify the quadratic form/lattice and candidate Weil representation.
6. Examine the boundary Im(tau_J)->0+ and only then ask whether resurgent/Stokes
   continuation is mathematically relevant.
7. Keep the physical interpretation of `psi` separate from analytic continuation.

## Deliverable

A theorem or obstruction note with explicit transformation matrices, weight,
multiplier, domain and proof-level status. Numerical pattern matching alone is
insufficient.
