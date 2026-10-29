<!-- BILINGUAL-UNIT: axial_cartan_symmetric_W_no_go -->
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


# Purely axial Cartan torsion versus symmetric Theta reconstruction defect

**2026-10-25 — conditional exact algebraic no-go, not an identification of the UBT spin current with the minimally coupled Dirac current.**

## Setting

In the canonical local non-null Gaussian representer, W_(mu nu)=g_(mu nu)-nabla^(LC)_mu V_nu is symmetric and the contortion obeys
```
K_(nu mu rho) V^rho = W_(mu nu).
```
Here K is antisymmetric in its outer indices (nu,rho), by metric compatibility.

For a minimally coupled Dirac matter spin current within the standard Einstein-Cartan/Hilbert-Palatini model, the algebraically sourced contortion is **totally antisymmetric** in three lowered spacetime indices (up to conventions and normalizations). This fact is conditional on minimal Dirac coupling; it is not established for the UBT Theta pure-pair current.

## Exact obstruction

Under total antisymmetry,
```
Q_(mu nu) := K_(nu mu rho) V^rho = -K_(mu nu rho) V^rho = -Q_(nu mu).
```
The reconstruction requires Q_(mu nu)=W_(mu nu)=W_(nu mu), so necessarily
```
W_(mu nu)=0,   Q_(mu nu)=0.
```
Conversely W=0 does not force K=0: nonzero totally antisymmetric contortion can remain if its contraction with V vanishes. The no-go is that purely axial contortion cannot source any *nonzero symmetric* W. In particular in branches with W!=0, standard minimal-Dirac-only Einstein–Cartan torsion cannot supply the required reconstructed geometry.

If V is timelike, a 3-form K with i_V K=0 is a spatial 3-form and has one algebraic independent component at the point. This is not a physical scalar particle prediction or a propagating degree of freedom. For a spacelike V the perpendicular subspace has Lorentzian signature; the same algebraic count remains 1.

## Scientific boundaries

- No calculation of the *actual* UBT Theta spin current is made here: minimal-Dirac axial current is only a benchmark.
- W may be zero in particular geometries; no obstruction is then asserted.
- Arbitrary metric-compatible contortion is not constrained to be a 3-form, so the previously identified twelve-dimensional transverse kernel and non-axial reconstruction remain available.
- The independent-connection Palatini field equation cannot be substituted for a Theta-only variation without proving the auxiliary elimination/chain rule.
- No Hamiltonian selection, full Einstein limit, physical ghost count, or new axiom is derived.

## Next test

Find the exact fixed-background UBT pure-pair spin-current formula and decompose its Cartan solution into vector trace, axial 3-form and mixed irreducible torsion pieces. Project K_Cartan V onto its symmetric and antisymmetric (mu,nu) components. Determine whether the symmetric part equals W, with correct source normalization and the composite Theta carrier map. A purely axial source gives identically zero symmetric projection, as proved above.

References: canonical/CANONICAL_DEFINITIONS.md section 3 (symmetric W in Gaussian reconstruction and conditional Palatini sector); research_tracks/action_selection/palatini_cartan_compatibility_gate.en.md.
