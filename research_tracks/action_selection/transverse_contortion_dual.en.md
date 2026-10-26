<!-- BILINGUAL-UNIT: transverse_contortion_dual -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# Transverse contortion kernel as a spatial dual

**Status:** exact pointwise algebraic parametrization, conditional on an oriented nondegenerate Lorentzian four-space and a non-null vector V. C-tier research note (2026-10-25). Not a dynamical torsion-selection rule.

## Setup

The existing reconstruction determines K only up to C with
```
C_{a m b} = -C_{b m a},  C_{a m b} V^b = 0.
```
Fix orientation and spacetime volume form epsilon_{abcd}. Then
```
C_{a m b} = epsilon_{ab cd} V^c Z_m^d,   V_d Z_m^d = 0.
```
The map Z -> C is an isomorphism from four copies (one per m) of V-perpendicular vectors to the kernel of contraction by V on antisymmetric 2-forms. This follows from the Hodge dual in V-perpendicular 3-space and non-nullness of V. The overall normalization and orientation convention can be absorbed into the definition of Z. For fixed m the dimensions are 3 -> 3, hence 12 for all m.

For completeness, choose Z from C (depending on epsilon-sign conventions) via a constant factor times `epsilon^{d a b c} V_c C_{a m b}/V^2`, with the factor fixed by the epsilon-contraction identity. No sign or normalization convention affects the isomorphism statement.

## Representation-theoretic decomposition

If V is timelike, in its local rest frame Z_m^i forms a 4 by 3 array. Split the covector m into time and spatial parts. The temporal row gives a spatial 3-vector, while the spatial 3 by 3 matrix splits into:
- scalar spatial trace: 1;
- antisymmetric part: 3;
- symmetric traceless part: 5.

Thus 12 = 3 + 1 + 3 + 5 under the rest-frame SO(3). These are **algebraic representation sectors**, not physical particle spins, propagating excitations, SU(3) generators, or a chiral selection law. For spacelike V the stabilizer is SO(1,2), and the SO(3) terminology does not apply.

A further torsion or variational equation may eliminate or relate these sectors. The locked Theta kinematics alone do not.

## Why setting Z=0 is not a derivation

The particular Gaussian reconstruction K0 sets the kernel C=0, but this chooses one solution of an underdetermined algebraic equation. Such a choice is not justified by the existing UBT equations as a canonical dynamical selection, and cannot be used silently to claim unique Hamiltonian, Dirac coupling or graviton modes.

## Next reproducible check

Linearize the constrained map Theta -> E -> g and the chosen composite pair (A[Theta], B[Theta]) jointly on a non-null flat patch. Explicitly include Z-sector variations, local Lorentz and diffeomorphism directions, and any gauge constraints. Test whether the resulting equations actually constrain all 12 kernel directions. Only then consider principal symbols and physical phase-space mode counting.

**Sources:** canonical/CANONICAL_DEFINITIONS.md (local torsion reconstruction), research_tracks/action_selection/composite_contortion_kernel.en.md (rank 12), research_tracks/action_selection/linearized_flat_theta_pure_gauge_no_go.en.md (restricted flat no-go).
