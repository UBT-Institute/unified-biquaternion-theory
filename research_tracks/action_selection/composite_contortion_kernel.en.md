<!-- BILINGUAL-UNIT: composite_contortion_kernel -->
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


# Composite-contortion contraction: twelve-dimensional local kernel

**2026-10-25 — conditional pointwise algebraic result; not a physical propagating-mode count or a unique UBT connection.**

## Grounding and conventions

The canonical local construction in `canonical/CANONICAL_DEFINITIONS.md` defines a non-null vector V, a symmetric tensor W with W_(mu nu) V^nu=0 in its Gaussian realization, and metric-compatible contortion K_(nu mu rho)=-K_(rho mu nu) satisfying K_(nu mu rho) V^rho=W_(mu nu). The exhibited solution is

```
K0_(nu mu rho)=(W_(mu nu) V_rho - V_nu W_(mu rho))/V^2.
```

The contraction equals W_(mu nu) precisely when W_(mu rho) V^rho=0; the Gaussian-vector construction supplies this condition. Antisymmetry in the outside indices is explicit. This solution is not unique.

## Exact kernel rank

At a point with V^2 not equal to zero, choose an orthonormal frame in which V lies in a single frame direction. For each fixed mu, K_(nu mu rho) is an antisymmetric two-tensor (6 components); contraction with V has image the three-dimensional covector subspace annihilating V and kernel the three-dimensional space of transverse two-forms. Four values of mu therefore give:

- input dimension 4 * 6 = 24;
- image dimension 4 * 3 = 12;
- kernel dimension 4 * 3 = 12.

In coordinate-free notation the kernel consists of all C_(nu mu rho)=-C_(rho mu nu) with C_(nu mu rho) V^rho=0. Accordingly **all** pointwise solutions of the contraction equation are K=K0+C with C in this 12-dimensional kernel. No dynamical/gauge counting follows from this algebraic rank alone.

## Linearization at a simple affine background

Take flat metric eta, \bar V^mu=x^mu+c^mu on a patch with \bar V^2 != 0, \bar W=0 and \bar K0=0. Perturb g=eta+epsilon h and V^mu=\bar V^mu+epsilon v^mu. The first-order variation of W is

```
delta W_(mu nu) = h_(mu nu)
  - partial_mu [ h_(nu sigma) bar V^sigma + eta_(nu sigma) v^sigma ]
  + delta Gamma(LC)^rho_(mu nu) bar V_rho,

delta Gamma(LC)^rho_(mu nu) =
 (1/2) eta^(rho lambda) [partial_mu h_(lambda nu)
                          +partial_nu h_(lambda mu)
                          -partial_lambda h_(mu nu)].
```

IMPORTANT: Here the sign of the LC Christoffel perturbation is **plus**, because W=g - partial V_flat + Gamma V_flat. Using `partial_mu V_nu - Gamma^rho_(mu nu) V_rho` gives the above sign.

Since \bar W=0, the linearized **particular** contortion is

```
delta K0_(nu mu rho) =
 (delta W_(mu nu) bar V_rho
  -bar V_nu delta W_(mu rho)) / bar V^2.
```

The Gaussian integrability condition must be imposed to ensure delta W is symmetric and delta W_(mu nu) bar V^nu=0. Linearizing V^2=epsilon rho^2 and the gradient representation can provide these restrictions; generic independent h,v do not automatically satisfy them. A general contortion perturbation also contains delta C transverse to bar V. Differentiating the transverse condition at Cbar=0 gives delta C_(nu mu rho) bar V^rho=0.

These are linearizations of the **selected particular algebraic reconstruction**, not of a unique canonical UBT connection. The implicit relation E=N0^-1/2 D[Theta,K]Theta and the carrier map must be linearized jointly; treating h,v,K as independent physical degrees of freedom would be invalid.

## Next dynamical gate

Derive a Theta-only equation (if possible) that fixes/eliminates the 12 transverse contortion components without postulating their values. Check the full composite Jacobian, Lorentz/diffeomorphism gauge identities and torsion constraints before counting any propagating gravitational modes or claiming a selected Hamiltonian.

## Reproducible finite rank check

For V=(1,0,0,0), enumerate the 24 antisymmetric triples (mu,nu,rho) with nu<rho and form the 16x24 contraction matrix M_(nu,mu); exact rational row reduction gives rank 12, nullity 12. The proof above is independent of computation.
