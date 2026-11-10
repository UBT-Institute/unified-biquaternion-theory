# Full Clifford extension: when does the odd sector disappear?

**Status:** OPEN research hypothesis, 2026-11-10. Does not supersede canonical biquaternion UBT.

## Decision from inverse axioms

Do not assume the 8-real-dimensional even subalgebra is a fundamental truncation. Compare a full field \(\Phi=\Phi_+ + \Phi_-\in Cl_{1,3}\) (16 real dimensions) to the even field \(\Theta=\Phi_+\in Cl_{1,3}^+\cong\mathbb C\otimes\mathbb H\) (8 real dimensions). The full graded algebra has dimensions grade 0:1, grade 1:4, grade 2:6, grade 3:4, grade 4:1. Even=0+2+4; odd=1+3. The *odd linear subspace is not a subalgebra*: odd*odd is even. Clifford sign convention here uses \(\gamma_0^2=+1\) and \(\gamma_i^2=-1\).

The odd sector is a module over the even algebra and can be represented as \(X_- \gamma_0\in Cl^+_{1,3}\) for a chosen invertible unit timelike vector \(\gamma_0\). This is a vector-space isomorphism, **not evidence of gauge redundancy**, and the reference vector's Lorentz transformation must be tracked.

## Rigorous elimination alternatives

**Auxiliary odd sector.** Given a real scalar invariant action \(S[\Phi_+,\Phi_-]\), variation with respect to the odd field may give a pointwise algebraic equation \(C\Phi_-+B^\dagger\Phi_+=0\), where \(C\) is nonsingular and derivative-free. Substitution gives the Schur-complement quadratic Hessian
\[
H_{\mathrm{eff}}=A-BC^{-1}B^\dagger.
\]
This modifies even-sector couplings. It does not imply that the odd field was identically zero; sources can induce nonzero odd composites.

**Gauge sector.** A physical disappearance requires first-class constraints and explicit gauge transformations; 8 algebraic basis components cannot be declared unphysical just by an invertible representation map. Count physical pairs after Dirac–Bergmann reduction.

**Propagating odd sector.** If the odd block contains a kinetic principal symbol, formal elimination \(C(\partial)^{-1}\) is generally nonlocal; the propagating poles and couplings remain and must be tested. A heavy odd field can yield a low-energy even effective action with corrections, not a fundamental absence.

**Consistent truncation.** Setting \(\Phi_-=0\) is consistent only if \(\delta S/\delta\Phi_-|_{\Phi_-=0}=0\), including all terms and sources, and evolution preserves the surface. For example an exact \(\mathbb Z_2\) grading symmetry \(\Phi_-\mapsto-\Phi_-\) forbids terms odd in \(\Phi_-\) in the vacuum, but does not remove odd excitations. Terms linear in \(\Phi_-\) induced by matter sources spoil vacuum truncation unless separately controlled.

## Mandatory physical gates

1. Fix Clifford signature, involutions, Lorentz action, orientation/parity and complexification conventions; do not count complex components as real or confuse spacetime pseudoscalar with central external imaginary unit without explicitly defining the embedding.
2. Enumerate independent invariant terms through a chosen derivative order respecting local Lorentz, diffeomorphism, relevant parity/gradation and matter symmetries. Maintain **one** fundamental action, not arbitrary even and odd sector actions.
3. Derive both Euler–Lagrange equations for all independent vs composite fields, including tetrad, metric and torsion variations where used.
4. Compute kinetic principal symbols, full constraints and reduced Hessian; distinguish algebraically eliminated, gauge, nondynamical constrained, heavy and genuinely propagating odd sectors.
5. Compare the reduced even action explicitly with the existing canonical UBT action registry and the spin-current flat-affine obstruction. A successful reduction must not merely postulate GR.
6. Test matter representations, parity/chirality, anomaly consistency and the measured two-tensor-polarization GR response; additional modes must have derived detector couplings and experimental constraints.
7. If no odd contribution is physically needed, explain whether the full field is redundant or only an effective UV completion; do not identify this with a proof of the uniqueness of biquaternions.

## Toy elimination vs real proof

For a symmetric quadratic block (on suitable real function spaces)
\[
S_2=\frac12\langle u,Au\rangle+\langle u,Bv\rangle+\frac12\langle v,Cv\rangle,
\]
if C is invertible and contains no derivatives of v, the solution is \(v=-C^{-1}B^\dagger u\). The effective quadratic form is \(A-BC^{-1}B^\dagger\). This identity is exact but **does not establish that the actual UBT odd-sector Hessian meets its hypotheses**. A singular C demands constraints; a derivative C yields nonlocal effective operators unless restricted by an appropriate expansion.

## Research status

OPEN: existence of a selected Clifford-valued fundamental action; algebraic elimination of the odd field in UBT; parity-invariant vacuum; induced spin/torsion terms; quantum Hilbert-space positivity; empirical selection. This track is a comparison model, not a claim that 16-component Theta already solves the UBT dynamical gaps.

References: ../unified_physics_axioms/README.md; ../../canonical/ACTION.en.md; ../spin_torsion_information/README.md.
