<!-- BILINGUAL-UNIT: palatini_cartan_compatibility_gate -->
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


# Palatini–Cartan compatibility gate for concurrent Theta geometry

**Status: conditional geometric/variational compatibility test (2026-10-25), not a derivation of the UBT master action.**

## Two separately established ingredients
1. Canonical non-null local representer: with one Lorentz connection Gamma metric-compatible, Theta=sqrt(N0) V^a u_a and nabla^Gamma_mu V^nu=delta_mu^nu, equivalently g_mu nu=nabla^Gamma_mu V_nu. Its torsion is generally nonzero and the reconstructing contortion includes a 12-dimensional transverse kernel.
2. For the independently varied **minimal** Hilbert–Palatini action with invertible tetrad, its connection equation is algebraic and invertible in 24 torsion components, schematically M(T)=kappa spin_current. If spin_current=0 then T=0 and Gamma=Gamma_LC. Both assertions are conditional on the chosen Palatini action and independent-connection variations.

## Strong compatibility obstruction
If these *two* requirements are imposed at once with vanishing spin current then
```
nabla^LC_mu V^nu=delta_mu^nu.
```
Commuting the torsion-free derivatives immediately yields
```
R^rho_{sigma mu nu}(LC) V^sigma=0.
```
Generic curved geometries do not have a nonzero concurrent vector, notably the Schwarzschild exterior is excluded in the existing canonical no-go. Thus simply selecting the zero-spin Palatini torsion solution does not generically coexist with the locked pure-Lorentz-pair reconstruction. This is a conditional incompatibility of branches, NOT a no-go for all UBT/GR limits.

In the torsionful branch, commuting the full affine covariant second derivative and correctly treating the extra derivative index gives (with convention [nabla_mu,nabla_nu] acting on a contravariant vector = R^rho_{sigma mu nu} V^sigma - T^lambda_{mu nu} nabla_lambda V^rho for *tensorial second derivatives*)
```
R^rho_{sigma mu nu}(Gamma) V^sigma = T^rho_{mu nu}
```
when nabla_mu V^rho=delta_mu^rho. This is an integrability identity (torsion can balance curvature); it is not a fresh independent equation selecting the 12 kernel components. Signs depend on the convention for torsion and R.

## Nonzero spin source: actual selection condition

Let K_Cartan[e,spin_current] denote the unique metric-compatible contortion determined by the *chosen* HP + matter connection equation, and K0[e,V] the particular Gaussian contortion reconstructing the Theta tetrad. Compatibility requires
```
(K_Cartan)^rho_{mu nu} V^nu = W_mu^rho
```
with W the LC derivative defect from canonical/CANONICAL_DEFINITIONS.md, equivalently
```
K_Cartan - K0 belongs to ker(K -> K V).
```
This is a nontrivial 12-component image constraint on the spin source plus the chosen e,V. The other 12 algebraic contortion components are then determined by the Cartan equation **only after** a source is specified; there is no guarantee an allowable Theta-derived spin current satisfies the condition.

The full Theta-only variation is **not** the independent-omega HP variation. Eliminating an independent auxiliary omega by its equation is permissible in a candidate theory only with a careful equivalence/constraint proof; if omega was stipulated composite ab initio, the variation must include delta omega[Theta] and induced delta e[Theta]. The existing pure-pair matter spin-current result must be inserted and checked with correct sign conventions and representation carrier; a generic symbolic J is not a derived UBT source. No new torsion mass term or adjustable lambda is selected here.

**Next gate:** compute M(T) projected onto the 12-dimensional image and kernel of contraction with V; substitute the actual canonical source and test 12 image compatibility equations on a nonflat background. Only then is there a chance to prove unique composite contortion and proceed to full Hamiltonian constraint analysis.

References: canonical/CANONICAL_DEFINITIONS.md §3 (GAP-10T-PALATINI conditional, GAP-10I-TORSION-LOCAL), research_tracks/action_selection/{composite_contortion_kernel,transverse_contortion_auxiliary_variation,contortion_stabilizer_invisibility}.en.md.
