# ADR proposal: single-action falsification programme

**Status: PROPOSED / NOT ACCEPTED.** No change to locked canonical definitions, no new fundamental action in this PR. Supersedes nothing unless separately accepted after review.

## Decision candidates (joint decision; explicitly not already derived)

1. Treat psi as a compact S1 **coordinate** with radius Rpsi and physical Hamiltonian evolution in real t. This replaces the current canonical document's description of psi as dynamical; determine periodic domain, spin structures and operator normalization: the dimensionful eigenvalues of -d²/dpsi² on a circle of radius Rpsi are n²/Rpsi², not n² unless radius is set to 1.
2. Treat g as an **independent dynamical metric**. This contradicts the locked central composite identity g = sharp(E,E) as the definition; it must be explicitly amended or replaced, not called a consequence of Proposition 9 (which proves a no-go only for one minimal timelike branch).
3. Select a single real pairing with exact convention. Re Sc is an algebraic scalar extraction, but a fully specified involution and positive-energy analysis remain necessary. It cannot be identified silently with existing H(X)=Tr(X^sharp X^dagger) or a positive Hermitian form.

## Proposed model, not yet UBT

The proposed integral over M4 x S1 with measure sqrt(-g4) d4x dpsi is a 4D metric field theory with an internal periodic parameter, unless a full 5D geometry, g_psi psi, gauge constraints and transformation laws are specified. A genuine 5D Einstein-Hilbert term uses sqrt(|g5|) R5 and the correct dimensions. For the alternative product-fiber model, explicitly declare no dynamical g_psi psi, domain of psi and the derivative operator.

A bare YM F² term is an additional **postulate** not derivable from an algebraic auxiliary connection. Treat it as a candidate to falsify, not a closure of the original composite no-new-field programme.

## Acceptance gates

- Publish configuration space and independent versus derived fields, including A and B for the two-sided Theta derivative.
- Prove gauge invariance of pairing and the scalar potential under exactly the chosen local group.
- Variant (b): derive linearized Gauss generators, gauge-orbit tangent space, full kinetic form on the quotient and additional YM sector with its noncompact signature. The equality dim SL(2,C)=6 and six negative Theta directions is NOT a proof that those directions coincide. The rank depends on background stabilizers.
- Variant (a) only after (b) fails, with complete symmetry-breaking disclosure.
- ADM in t: primaries, secondaries, first/second class, physical mode count, reduced Hamiltonian boundedness, KK spectrum and GR infrared coefficient.
- Do not reclassify historical actions as reductions without an explicit derivation map.

## Stop condition

If both (a) and (b) fail **within the declared minimal model**, mark that model falsified; do not infer a theorem about every possible UBT completion. Do not introduce new reduced actions before full Dirac analysis.

## Implementation scope

The CI check introduced alongside this draft rejects **marked declarations** of S_UBT outside the designated canonical TeX file but permits references. It cannot reliably infer an unmarked prose or mathematical definition; repository-wide semantic inventory and human review remain required.
