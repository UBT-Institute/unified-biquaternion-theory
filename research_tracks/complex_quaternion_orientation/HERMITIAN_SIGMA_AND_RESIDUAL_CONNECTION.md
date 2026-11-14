<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: pending
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Exploratory research note; not a canonical theorem or verified physical derivation.
UBT-AI-PROVENANCE-END
-->

# Complex quaternion orientation, Hermitian sigma model, and residual connection

Status: **research track / conditional algebraic derivations**, 2026-11-14. This is NOT an established UBT field equation or a derivation of Maxwell/QED. It must not be added to canonical claims without an audit.

## 1. Definitions and conventions

Let `B = C tensor_R H ~= M_2(C)`, with quaternion units `e_i e_j = -delta_ij + epsilon_ijk e_k`. The complex imaginary unit is central and distinct from quaternion units. Define `J = sum_i n_i e_i` with `n_i in C` and the *bilinear* constraint `n.n = sum_i n_i^2 = 1`; hence `J^2=-1`. The target `Q_C^2 = {n in C^3: n.n=1}` is real four-dimensional and diffeomorphic to `TS^2`. Writing `n=u+i v` yields `u.u-v.v=1, u.v=0`.

The quaternion-Hermitian involution is `(z0+z_i e_i)^dagger = conjugate(z0)-conjugate(z_i)e_i`. The scalar part satisfies `Sc(X^dagger X)=sum |z_i|^2`. In particular `Sc((partial J)^dagger partial J)=sum |partial n_i|^2`. This establishes an algebraically natural positive Hermitian quadratic form; it does NOT select a unique fundamental action.

## 2. Candidate model and status

On a fixed real Lorentzian metric of signature (+---), consider
`L = (kappa/2) g^{mu nu} partial_mu bar(n) . partial_nu n + Re[lambda(n.n-1)]`, kappa>0.
The spatial gradient energy and time kinetic energy are nonnegative on the constraint manifold. In local real coordinates q^a on Q_C^2, the kinetic Hessian is `kappa G_ab`, where `G_ab=partial_a u.partial_b u + partial_a v.partial_b v`; it is positive definite. Therefore there are four real configuration degrees of freedom **before any additional gauge constraints**. This only rules out negative kinetic directions in this isolated fixed-background sigma sector. It says nothing about the full UBT gravitation/connection Hessian, nor global dynamical stability.

The holomorphic form `partial n.partial n` differs from the Hermitian form and is not positive. The Hermitian form is not invariant under arbitrary active SO(3,C) rotations of n; its common continuous linear symmetry with the bilinear constraint is SO(3,R).

## 3. Composite connection, with sign audit

Choose a local oriented complex-orthonormal frame `(e1,e2,n)`, `e1 cross e2=n`, with `R in SO(3,C)`. Set `A=e1 . d e2`. For `e1'=cos(alpha)e1+sin(alpha)e2`, `e2'=-sin(alpha)e1+cos(alpha)e2`, one gets `A'=A-d alpha`, with complex alpha. This is a *passive frame* gauge freedom, not automatically an active symmetry of the sigma-model.

**Correction to the previous chat:** with the above orientation and definition, the curvature is
`dA = (1/2) n . (dn cross_wedge dn)`, i.e. in components
`F_mu_nu = n . (partial_mu n cross partial_nu n)`.
The previously stated negative sign was inconsistent with these conventions. For example on the real sphere, `e1=e_theta`, `e2=e_phi`, `A=-cos(theta)dphi`, so `dA=+sin(theta)dtheta wedge dphi`.
If `f_mu_nu=(1/2)n.(partial_mu n cross partial_nu n)`, then **F_mu_nu=2 f_mu_nu**, not -2 f. The 2-form `F=(1/2)F_mu_nu dx^mu wedge dx^nu` is closed, `dF=0`, on smooth patches. It is a constrained composite curvature, not a general Maxwell field.

For a closed oriented 2-surface, `(1/4pi) integral n.(partial_1 n cross partial_2 n) d^2x` is the integer degree in the real S^2 case. Since Q_C^2 deformation retracts onto S^2, the corresponding cohomology class persists under complexification; verify integral normalization and global frame transitions when extending the charge statement. Nonzero degree prevents a single globally smooth frame on the pulled-back bundle.

## 4. Critical comparison with canonical UBT

The canonical metric uses `E_mu = D_mu Theta / sqrt(N0)` and its central anticommutator. This track has **not** defined a globally valid extraction map `Theta -> J` compatible with that tetrad or demonstrated equality with the canonical residual SO(2) connection. Identical abstract stabilizers do not prove identical bundles, representations, or dynamics.

Next checks:
1. Define J(Theta) on a non-null patch and compute its transformation under the existing two-sided UBT connections A_mu/B_mu; identify singular loci.
2. Compare the *same* frame bundles, connection transformations, and curvatures with the canonical residual SO(2) sector; include complexification/reality constraints.
3. Compute the coupled kinetic Hessian and first/second class constraints; test whether the imaginary connection component propagates or is auxiliary.
4. If proposing electromagnetism, independently derive a Maxwell kinetic term, source coupling, gauge charges, and the appropriate real physical field; `dF=0` alone is insufficient.
5. Test linear perturbations around n=(0,0,1) and topological sectors. Check whether the sigma model adds physical degrees of freedom inconsistent with UBT's canonical rank/constraint count.

## 5. Claim boundaries

- [ALG] Biquaternion Hermitian scalar form, Q_C^2 geometry, local connection, corrected curvature identity.
- [COND] Positive constrained kinetic Hessian for this specifically chosen fixed-background sigma action.
- [OPEN] Extraction from Theta, identification with UBT SO(2), coupled ghost freedom, QED/Maxwell emergence, physical charge quantization.
- [NO CLAIM] No new experimentally validated prediction; no GR/SM completion.
