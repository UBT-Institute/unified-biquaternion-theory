<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# OI-6 — Sharp-compatible Lorentz metric covariance and a two-sided connection

**Status:** exact algebraic identities [STD] under an explicitly specified matrix representation; physical identification with the canonical UBT connection and action [OPEN]. No new UBT dynamics is claimed.

## A. Define sharp carefully, not as Hermitian adjoint

In the standard Pauli representation of the complexified quaternion algebra, the quaternion basis is represented by negative imaginary Pauli matrices. Complex-linear quaternion conjugation is the two-by-two adjugate, not the Hermitian adjoint:

$$
\mathbf e_k=-i\sigma_k,\qquad
X^\sharp=(\mathrm{Tr}X)I_2-X=\operatorname{adj}X,\qquad
(XY)^\sharp=Y^\sharp X^\sharp,\qquad
XX^\sharp=(\det X)I_2.
$$

**OI-6-T16 [STD, conditional].** The polarized determinant supplies a central, complex-bilinear pairing on the full biquaternion matrix algebra:

$$
\frac12(X^\sharp Y+Y^\sharp X)
=B(X,Y)I_2,\qquad
B(X,Y)=\frac{\det(X+Y)-\det X-\det Y}{2}.
$$

The identity follows by expanding matrices in the Pauli basis, or directly from the Cayley–Hamilton identity for two-by-two matrices. For the anti-Hermitian paravector slice used in the referenced canonical Pauli representation, its quadratic form has signature (-+++). It is not necessary to truncate the full complex biquaternion algebra to establish the complex-bilinear identity.

## B. OI-6-T17 — Exact Lorentz covariance of the central metric

Take the standard spinorial Hermitian congruence for a determinant-one complex matrix. Because sharp is an anti-automorphism, it transforms contragrediently under congruence:

$$
X'=gXg^\dagger,\quad g\in SL(2,\mathbb C),\quad
(X')^\sharp=(g^\dagger)^{-1}X^\sharp g^{-1}.
$$

This yields an exact central metric identity for arbitrary complex X and Y, and also preserves the anti-Hermitian real paravector slice:

$$
\frac12\bigl((X')^\sharp Y'+(Y')^\sharp X'\bigr)
=(g^\dagger)^{-1}
\left[\frac12(X^\sharp Y+Y^\sharp X)\right]g^\dagger
=B(X,Y)I_2.
$$

**OI-6-T17 [STD, conditional].** Lorentz boosts need not be unital automorphisms of matrix multiplication to preserve this central UBT-type metric identity. The earlier no-go concerned imposing **both conditions on the same full algebra action**; it does not invalidate the standard Lorentz congruence. For g with nonunit determinant the pairing instead scales by the absolute determinant squared.

## C. OI-6-T18 — A two-sided connection is covariant under local spin actions

As an architectural **candidate**, let a complex matrix field transform by the same congruence and define a two-sided covariant derivative. For a local g(x), assign the usual gauge transformation to a left connection, with its adjoint on the right:

$$
D_\mu\Theta=\partial_\mu\Theta+A_\mu\Theta+\Theta A_\mu^\dagger,\quad
\Theta'=g\Theta g^\dagger,\quad
A_\mu'=gA_\mu g^{-1}-(\partial_\mu g)g^{-1}.
$$

Expanding the derivative of the product cancels the terms containing derivatives of g and its adjoint, giving exact covariance even when g depends on spacetime:

$$
D_\mu'\Theta'=g(D_\mu\Theta)g^\dagger,\qquad
E_\mu=\frac{D_\mu\Theta}{\sqrt{\mathcal N_0}}
\ \Longrightarrow\
E_\mu'=gE_\mu g^\dagger
\quad\text{if }\mathcal N_0'=\mathcal N_0.
$$

**OI-6-T18 [STD, conditional].** These equations provide an explicit internally consistent local spin-covariant **comparator** for the canonical tetrad relation, assuming an invariant normalization and the chosen two-sided representation. They do not establish that the UBT dynamical principle selects this connection, nor that the full Theta field obeys any required reality condition. Additional coordinate and frame transformations are not supplied by this elementary comparator.

## D. OI-6-T19 — Boost and rotation infinitesimal actions are different

For infinitesimal g=I+epsilon K, the congruence acts on a field as KTheta+Theta K-dagger. For an anti-Hermitian rotation generator this is a commutator (and a derivation); for a Hermitian boost generator this is an anticommutator (and not a derivation of the matrix algebra).

$$
\delta_K\Theta=K\Theta+\Theta K^\dagger,\quad
K^\dagger=-K\Rightarrow\delta_K\Theta=[K,\Theta],\quad
K^\dagger=K\Rightarrow\delta_K\Theta=\{K,\Theta\}.
$$

**OI-6-T19 [STD].** This gives a precise operational distinction between a boost acting on the Lorentz paravector carrier and an inner algebra automorphism. It is not an independent derivation of Lorentz invariance from information.

## E. UBT constraints and open scientific gaps

The canonical Clifford/Dirac file canonical/geometry/biquaternion_dirac_lift.tex uses E_mu=D_mu Theta/sqrt(N0), the central sharp identity and a complex biquaternionic field. This note matches its **Pauli sharp representation conditionally**, but has not audited every canonical connection component, complex-time derivative or UBT gauge redundancy. No UBT action, Hamiltonian constraint, spectrum or ghost freedom is established.

**G-OI6-13 [OPEN]:** identify the actual canonical sharp/connection definitions and prove or refute equivalence to this two-sided comparator. **G-OI6-14 [OPEN]:** derive the allowed local spin transformation on Theta from a physical action, including the normalization, tetrad rank and the possible degenerate sector. **G-OI6-15 [OPEN]:** compute the constrained Hamiltonian Hessian and check stable propagating degrees of freedom, then GR and SM limits.

## F. Reproducible checks and established references

The standard-library script verify_sharp_spin_covariance.py has 13/13 exact local tests passed on 2026-11-11, with a matching Git blob hash 410296d8c877bbeacb002c2686b1b7b1750785e9. Tests cover sharp anti-automorphism, determinant polarization, Lorentz covariance, signature (-+++), the local two-sided connection and its derivative terms. This is a mathematical verification only, not a physics experiment or a validated UBT dynamical theorem.

- MIT OpenCourseWare, *The Lorentz Group and the Pauli Algebra*: https://mitocw.ups.edu.ec/resources/res-8-001-applied-geometric-algebra-spring-2009/lecture-notes-contents/Ch3.pdf .
- Spinor Lorentz congruence and determinant preservation: https://www.math.uni-tuebingen.de/de/forschung/maphy/lehre/ws-2025-26/grar/dateien/notes.pdf .
- UBT canonical relation: canonical/geometry/biquaternion_dirac_lift.tex (internal source, not independent validation).