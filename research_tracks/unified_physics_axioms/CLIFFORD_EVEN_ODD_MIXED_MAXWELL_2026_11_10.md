# Inverse Clifford dynamics: hidden propagation from even–odd mixing

**Status: exact calculation for an explicitly selected flat-space toy action; NOT a derivation of UBT, its Maxwell sector or its microscopic action. 2026-11-10.**

## The key correction to the bare a=b=m=0 branch

An odd-vector's *diagonal* free quadratic coefficients a=b=m=0 do NOT imply the odd vector is auxiliary, pure gauge, or nonpropagating if it couples through derivatives to the even Clifford grades. The correct physical count comes from the entire coupled kinetic and constraint system. The earlier separate-vector invariant classification remains valid only when the even fields are held fixed or odd–even cross interactions are excluded.

### Exact counterexample: a first-order Maxwell action

Let B_{\mu\nu}=-B_{\nu\mu} be an independent real antisymmetric tensor (grade-2/even) and V_\mu a real polar vector (grade-1/odd) on a fixed Minkowski background eta=(+---). Define F_{\mu\nu}(V)=partial_mu V_nu-partial_nu V_mu and
\[
S[B,V]=\int d^4x\left[\frac14 B_{\mu\nu}B^{\mu\nu}
-\frac12 B_{\mu\nu} F^{\mu\nu}(V)\right].
\]
The action is local, Lorentz invariant, parity even (B and F both ordinary rank-two antisymmetric tensors), and invariant under the **emergent U(1)-type gauge transformation** V_mu -> V_mu + partial_mu alpha with B fixed. However it is **NOT invariant under the independent Clifford grade sign flip V -> -V with B fixed**: the B.F term changes sign. Therefore it is incompatible with an exact grade-Z2 symmetry taken as an independent physical postulate. A Clifford grading automorphism is an algebraic property, not automatically a symmetry of a proposed action.

The B variation is algebraic:
\[
\delta_B S =\frac12\int d^4x (B^{\mu\nu}-F^{\mu\nu})\delta B_{\mu\nu},
\quad\Rightarrow\quad B=F.
\]
Substitution yields
\[
S_{\rm eff}[V]=-\frac14\int d^4x F_{\mu\nu}F^{\mu\nu}.
\]
The V variation of the original action is
\[
\delta_V S=\int d^4x(\partial_\mu B^{\mu\nu})\delta V_\nu,
\quad\Rightarrow\quad\partial_\mu B^{\mu\nu}=0,
\]
under suitable boundary conditions. Combining B=F gives Maxwell's source-free equation partial_mu F^{mu nu}=0. Under Maxwell gauge reduction and standard falloff, the resulting field has two physical propagating transverse modes. These are **photon/vector** modes, NOT gravitational-wave polarizations.

Crucial reverse interpretation: **the odd vector has zero stand-alone a,b,m yet is NOT removable**; the even bivector B is the actual algebraic auxiliary field in this example. Integrating out B creates kinetic dynamics for V. Consequently the principle “set all odd quadratic coefficients to zero” does not select a biquaternion-only physical theory.

### Algebraic completion of square

\[
\frac14 B^2-\frac12 B\cdot F
=\frac14 (B-F)^2-\frac14 F^2.
\]
On shell B=F; at Gaussian functional-integral level integrating B contributes a determinant/normalization subject to the chosen measure and regularization. No claim is made about the full quantum path integral or a generated gauge sector from UBT.

## General block diagnostic

For arbitrary even u and odd v perturbations, a mixed Hessian takes the form
\[
H(p)=\begin{pmatrix}A(p)&M(p)\\M^\dagger(p)&C(p)\end{pmatrix}.
\]
Setting C's diagonal kinetic coefficients to zero does not set M to zero. If A is an invertible derivative-free even block, eliminating u gives \(C_{\rm eff}=C-M^\dagger A^{-1}M\), which is *generically quadratic in momenta when M is first order*. This is exactly how a kinetic pole can be induced on the initially bare odd block.

If an action has an exact independently imposed grade-flip symmetry, all terms with one odd factor and arbitrarily many even factors are prohibited, unless other transformed odd quantities restore total even grading. In that case the present simple B.F example is not admissible; nonzero odd fluctuations can still occur through even powers of the odd field and need not be gauge.

## What does this tell us about minimal physical principles?

1. Relativity/parity permits the first-order coupling. An additional grade-Z2 invariance would forbid it, but the **operational origin** of that invariance is not established.
2. Whether B is independent or composite from a single Theta is essential: the algebraic derivation here treats B as an **independent** even field. If B is constrained to be a bilinear of Theta's derivatives, its variation and constraint algebra differ. Never transfer the Maxwell conclusion without varying that dependence.
3. A first-order action can have a larger-looking field content with no extra physical modes after constraints, but that is different from declaring one algebraic grade irrelevant.
4. We must classify full even–odd invariant cross terms and their principal-symbol rank before asserting an odd-sector no-go or a truncation.
5. GR, Standard Model, fermion spin/statistics, thermodynamics and information principles are independent target gates; this simple action proves none of them.

## Next calculation

Build the full quadratic mixed Hessian around a specified Lorentz-covariant UBT background, with all composite tetrad/metric/spin-connection variations. Test whether exact grade-Z2 is consistent with observed electromagnetic and fermionic sectors before invoking it as a selection axiom. Then compute Dirac–Bergmann constraint ranks and constrained characteristics. Compare with previously documented canonical UBT failures of bare matched-pairing actions and spin-current flat-affine branch.

Related:
- [Full Clifford odd-sector gates](FULL_CLIFFORD_ODD_SECTOR.md)
- [Flat odd-only classification](CLIFFORD_ODD_FLAT_QUADRATIC_BASIS_2026_11_10.md)
- [Action registry](../../canonical/ACTION.en.md)
