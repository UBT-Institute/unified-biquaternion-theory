# Inverse physical symmetry: Clifford grading is not fermion parity or an independent odd-field sign symmetry

**Date:** 2026-11-10. **Status:** exact algebraic distinction + explicit QED comparator; microscopic UBT selection OPEN.

## Problem and necessary correction

The preceding note [CLIFFORD_EVEN_ODD_MIXED_MAXWELL_2026_11_10.md](CLIFFORD_EVEN_ODD_MIXED_MAXWELL_2026_11_10.md) correctly states that \(B\cdot F(V)\) changes sign under the *independent internal field-only* flip \(V\mapsto-V\) with \(B,\partial,\gamma\) fixed. But calling that operation simply "Clifford grading symmetry" conflates **two different transformations**.

For homogeneous Clifford grade \(k\), the grade automorphism is
\[
\alpha(X_k)=(-1)^k X_k,\qquad \alpha(XY)=\alpha(X)\alpha(Y).
\]
In real \(Cl_{1,3}\), \(\alpha(\gamma_\mu)=-\gamma_\mu\), \(\alpha(I)=I\), \(\alpha(B)=B\) for bivectors and \(\alpha(V)=-V\) for vectors. With \(I=\gamma_0\gamma_1\gamma_2\gamma_3\), the automorphism is inner algebraically, \(\alpha(X)=IXI^{-1}\); this is **not** a claim it is an allowed internal gauge transformation of the same physical background or a proper orthochronous Lorentz transformation.

A vector derivative \(D=\gamma^\mu\partial_\mu\), treated as a Clifford-valued operator with fixed coordinate derivative, also has \(\alpha(D)=-D\). Hence:
\[
\alpha(D\wedge V)=\alpha(D)\wedge\alpha(V)=(-D)\wedge(-V)=D\wedge V.
\]
Thus the geometric bivector \(F=D\wedge V\) is even under the **full algebra automorphism**, and the scalar \(B\cdot F\) is invariant. By contrast, applying only \(V\to -V\) with D and B held fixed sends \(F\to-F\), violating that independent field-only symmetry.

One must specify whether the transformation acts on the entire Clifford-valued geometric expression, the field configurations alone at fixed background/basis, or the physical spacetime arguments and frames. Applying an algebra automorphism to all objects is a mathematical covariance statement and does *not by itself supply a nontrivial physical selection rule*.

## Three distinct Z2 operations

1. **Grade automorphism** \(\alpha\): changes signs according to multivector grade in the *entire algebra* including odd Clifford geometric operators.
2. **Field-only odd flip** \(\beta: \Phi_+\mapsto\Phi_+,\Phi_-\mapsto-\Phi_-\), while the derivative, tetrad, background, sources and measurement maps are held fixed. This is an additional *candidate internal physical symmetry*. It can forbid terms linear in \(\Phi_-\), but is **not implied merely by the existence of a Clifford \(\mathbb Z_2\)-grading**.
3. **Fermion parity** \((-1)^F\): acts as \(-1\) on fermionic *quantum field operators* (Grassmann odd, in an appropriate representation) and +1 on bosons. It is distinct from the geometric grade of the Clifford algebra. A Clifford grade-1 vector field can be bosonic (e.g. a gauge connection) and a Dirac spinor can be described using an even multivector under an appropriate representation.

Ordinary spacetime parity \(P:(t,\mathbf x)\to(t,-\mathbf x)\) is likewise not these operations. A polar vector and axial vector differ in P, but P is not full Clifford grade inversion, nor automatically fermion parity.

## QED comparator — why fermion parity cannot remove ordinary gauge couplings

The standard QED term is
\[
\mathcal L_{\rm int}=-e\bar\psi\gamma^\mu A_\mu\psi .
\]
Under fermion parity \(\psi\mapsto-\psi,\;\bar\psi\mapsto-\bar\psi\), the term is invariant because it contains two fermionic factors; \(A_\mu\), a bosonic spacetime vector, is unchanged. Thus observed fermion statistics do not enforce an internal sign reversal of all **geometric grade-odd** vector fields. Mapping fermion parity onto Clifford grade flip without a field/representation dictionary would be an unjustified identification.

## Consequence for inverse UBT reconstruction

- There is no selection theorem from Lorentz invariance + parity + fermion parity alone forcing all Clifford odd modes to be unphysical, auxiliary, or absent.
- Full-algebra grading **does not universally forbid** an even-bivector/odd-vector first-order mixing term because a geometric derivative itself has odd grade.
- An optional **field-only** Z2 symmetry may forbid such terms in a fixed-background ansatz, but requires an independent operational reason and must be tested against EM, chiral fermions, Standard Model matter couplings and the proposed composite connection readout.
- Even if \(\beta\) is a symmetry, configurations with nonzero odd kinetic fluctuations may still exist. \(\beta\) is not in general a gauge redundancy.
- Explicit parity violation in weak interactions means any proposal imposing physical spatial parity P on the full fundamental dynamics must provide a demonstrated mechanism for its breaking; spacetime parity and \(\beta\) should not be conflated.
- The exact choice between the full \(Cl_{1,3}\) and even \(\mathbb C\otimes\mathbb H\) remains OPEN. The coherent next test is a **single full mixed Hessian** with the real/complex observable map, and complete composite tetrad/torsion variation, not a separate odd kinetic-zero choice.

## Verification boundaries

Finite Clifford grade-sign identities and QED fermion-parity signs are exact algebra. Companion [test_inverse_clifford_grading_parity.py](../../tests/test_inverse_clifford_grading_parity.py) checks signs and the mixed-term distinction. No physical spacetime or quantum S-matrix theorem is claimed.

**Status:** CLAUSE CORRECTION to the previous odd-sector mixing note, no retroactive reclassification as a unique fundamental action.

References:
- [Earlier first-order Maxwell comparator](CLIFFORD_EVEN_ODD_MIXED_MAXWELL_2026_11_10.md)
- [Full Clifford extension](FULL_CLIFFORD_ODD_SECTOR.md)
- [Action registry](../../canonical/ACTION.en.md)
