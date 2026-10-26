<!-- BILINGUAL-UNIT: contortion_stabilizer_invisibility -->
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


# Stabilizer contortion: tetrad invisibility does not imply connection uniqueness

**2026-10-25; conditional exact local kinematic result.** Applies to the non-null V reconstruction of canonical/CANONICAL_DEFINITIONS.md, not automatically to arbitrary Theta carriers, a selected canonical action, or physical on-shell gauge inequivalence.

## Construction

Let an oriented Lorentzian tetrad e be nondegenerate and V a smooth non-null vector on a patch. Suppose a metric-compatible Gamma0 satisfies
```
nabla^(Gamma0)_mu V^a = e_mu^a
```
in tetrad components, equivalently nabla_mu V^nu = delta_mu^nu with appropriate frame/coordinate conversion. Define another metric-compatible Lorentz connection by shifting its contortion by C with
```
C_{a mu b} = -C_{b mu a},  C_{a mu b} V^b = 0.
```
Then, identically,
```
(nabla^(Gamma0+C)_mu - nabla^(Gamma0)_mu) V^a
    = C^a_(mu b) V^b = 0.
```
Therefore the **same chosen** Theta = sqrt(N0) V^a u_a and tetrad satisfy E_mu = N0^-1/2 D_mu Theta for both connections, provided the spin/vector carrier dictionary and the pure Lorentz pair are the one used in the canonical local reconstruction. Hence the locked sharp composite metric also agrees. This is a local fiber of connection reconstructions over identical Theta, E and g, not a derivation of a globally defined functional Gamma[Theta].

The shifts preserve metric compatibility by antisymmetry of their two internal indices. The pointwise vector space has 12 real dimensions for non-null V. Its timelike-V rest frame decomposition 3+1+3+5 is algebraic only.

## Why curvature can differ

For the matrix-valued connection one-form omega0 and shift C,
```
F(omega0+C)-F(omega0) = D_(omega0) C + C wedge C.
```
Choose a smooth C(x) in the transverse kernel over a local patch such that C(p)=0 while its first derivative at p is not zero (e.g. C=f(x) Ctilde(x), f(p)=0 with df(p) nonzero, and Ctilde(p) nonzero in a two-form component with an appropriate derivative direction). Then at p the curvature variation is (d f wedge Ctilde)(p), and can be nonzero. Thus equal Theta, E and g do NOT imply equal connection curvature; torsion generally also differs. This construction is off-shell. Full dynamical equations might distinguish or remove C.

## Integrability identity is necessary but not a selector

For any chosen omega, D_mu Theta = sqrt(N0) E_mu implies
```
[D_mu,D_nu] Theta = sqrt(N0)(D_mu E_nu - D_nu E_mu),
```
where the derivative on E on the RHS here acts on its *internal carrier* only (there is no affine correction yet). If coordinate-covariant tetrad derivatives are used, include the antisymmetric affine contribution consistently, which is related to torsion. This identity is satisfied automatically by both reconstructed connections since it is the commutator of the defining covariant derivatives; it does not independently select C. In particular, differing F can be balanced by differing D E / torsion while preserving E itself.

## Consequence for the Hamiltonian programme

A functional depending only on Theta and its composite first-jet metric cannot distinguish the connection shifts **within this reconstructed solution family**, provided no hidden dependence on omega or its derivatives remains in the chosen functional. Curvature, torsion, Dirac coupling, and higher covariant derivatives can distinguish them. Do not claim that all diffeomorphism/Lorentz-invariant local actions are blind to C, nor that these shifts are physical propagating modes or gauge transformations.

A defensible selection test must derive the connection/contortion equation from the same Theta-only dynamical principle, or exhibit an independent identity (not the defining integrability tautology) fixing transverse C; then check whether the resulting C is a local, covariant, unique functional of Theta and whether Hamiltonian constraints close. An arbitrary choice C=0 is a particular reconstruction, not an axiom-free selection.

**Grounding:** canonical/CANONICAL_DEFINITIONS.md section 3; research_tracks/action_selection/composite_contortion_kernel.en.md; transverse_contortion_dual.en.md; two_sided_metric_covariance.en.md.
