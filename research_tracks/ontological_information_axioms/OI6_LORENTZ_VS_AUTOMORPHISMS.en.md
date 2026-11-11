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

# OI-6: Lorentz congruence versus biquaternion automorphisms

**Status:** exact textbook matrix algebra [STD] under a selected complex carrier; physical UBT field transformation and action [OPEN]. No original physics claimed.

## A. Three distinct actions

Let B be the complex matrix algebra, H its Hermitian real subspace, and fix column-major vectorization. For a determinant-one spinor g and a two-qubit unitary V distinguish

$$
\mathbb B=M_2(\mathbb C),\quad H=\mathrm{Herm}(2,\mathbb C),\quad
g\in SL(2,\mathbb C),\quad V\in SU(4).
$$

$$
\mathcal A_g(X)=gXg^{-1},\qquad
\mathcal L_g(X)=gXg^\dagger,\qquad
\mathcal U_V(X)=\mathrm{vec}^{-1}(V\,\mathrm{vec}X).
$$

The first is a unital multiplicative algebra automorphism; the second preserves H and the Minkowski determinant; the third preserves the Euclidean vector norm. These are distinct structures and cannot be identified solely by the carrier dimension.

## B. OI-6-T12 — Boost incompatibility and the common rotation subgroup

For nonzero rapidity eta consider the diagonal Lorentz spinor. The congruence does not fix the identity, whereas every algebra automorphism must:

$$
g_\eta=\begin{pmatrix}e^{\eta/2}&0\\0&e^{-\eta/2}\end{pmatrix},\quad
\mathcal A_{g_\eta}(I_2)=I_2,\quad
\mathcal L_{g_\eta}(I_2)=\begin{pmatrix}e^\eta&0\\0&e^{-\eta}\end{pmatrix}.
$$

Therefore a nontrivial boost congruence is not a unital algebra automorphism. Conversely, similarity by the same nonunitary boost maps the Hermitian Pauli-X matrix outside H:

$$
\mathcal A_{g_\eta}(\sigma_x)
=\begin{pmatrix}0&e^\eta\\e^{-\eta}&0\end{pmatrix}
\notin H\quad(\eta\ne0).
$$

**OI-6-T12 [STD].** A_g=L_g as maps on all matrices if and only if g is unitary: equality evaluated at the identity gives gg†=I; the converse follows from inverse equaling adjoint. For g in SL2C the common spinorial subgroup is SU2 (spatial rotations, modulo sign). This is an obstruction to demanding the *same action* be both an algebra automorphism and Lorentz congruence, not an obstruction to Lorentz-covariant UBT field representations.

## C. OI-6-T13 — Vectorization has a built-in product factorization

The standard vectorization identity gives exact tensor-product actions:

$$
\mathrm{vec}(AXB)=(B^T\otimes A)\mathrm{vec}X,\quad
\mathrm{vec}\mathcal A_g(X)=((g^{-1})^T\otimes g)\mathrm{vec}X,\quad
\mathrm{vec}\mathcal L_g(X)=(\bar g\otimes g)\mathrm{vec}X.
$$

Both factors are invertible, so the Schmidt rank in this particular row-column bipartition is preserved. Hence neither matrix action changes a separable rank-one vector into an entangled rank-two vector. A nonunitary factor is a local invertible filter, not a deterministic Hilbert-unitary gate.

**OI-6-T13 [STD].** The entangling SU4 dynamics found in the earlier research track cannot be supplied by these matrix actions under the fixed vectorization factorization. The physical tensor factorization of the UBT field remains unselected [OPEN].

## D. OI-6-T14 — Normalized entanglement is not a Lorentz scalar

For the normalized pure vector obtained from a nonzero matrix X, concurrence depends on both determinant and Frobenius norm. A boost keeps the former but changes the latter:

$$
C(\mathrm{vec}X)=\frac{2|\det X|}{\mathrm{Tr}(XX^\dagger)},\quad
C(\mathrm{vec}I_2)=1,\quad
C(\mathrm{vec}\mathcal L_{g_\eta}(I_2))=\frac1{\cosh(2\eta)}.
$$

**OI-6-T14 [STD].** Lorentz determinant invariance does not imply normalized quantum-entanglement invariance. The boost is not a norm-preserving two-qubit gate. The rank is unchanged, however; this distinguishes the discrete separability class from quantitative concurrence. The correspondence is a representation analogy, not a claim that spacetime points are physical two-qubit states.

## E. OI-6-T15 — Generic entangling SU4 dynamics breaks the Hermitian null cone

Under the standard two-qubit XX interaction, the vectorized Hermitian rank-one projector becomes a complex non-Hermitian full-rank matrix:

$$
E_{00}=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
U_\theta=e^{-i\theta\sigma_x\otimes\sigma_x},\quad
\mathrm{vec}^{-1}(U_\theta\mathrm{vec}E_{00})
=\begin{pmatrix}\cos\theta&0\\0&-i\sin\theta\end{pmatrix}.
$$

$$
\det E_{00}=0,\qquad
\det(\mathrm{vec}^{-1}(U_\theta\mathrm{vec}E_{00}))
=-i\cos\theta\sin\theta\ne0\quad(0<\theta<\pi/2).
$$

**OI-6-T15 [STD].** The arbitrary SU4 unitary action is not automatically an allowed Lorentz transformation on Hermitian paravectors, nor an automorphism of biquaternion multiplication. The physical UBT interaction must be derived with its own constraints and involutions.

## F. Canonical UBT boundary and next gates

The canonical UBT file canonical/geometry/biquaternion_dirac_lift.tex uses E_mu from derivatives of Theta and a central metric identity with the **sharp** involution. Its Lorentz paravector slice and sharp operation have not been identified here with the ordinary Hermitian slice and dagger. Nor has the field Theta been shown to transform by any of the three compared actions. There is no change to the canonical geometry, action, degree-of-freedom count or ghost claims.

**G-OI6-10 [OPEN]:** derive the sharp-compatible action on Theta and E_mu. **G-OI6-11 [OPEN]:** distinguish field/frame transformations from dynamical two-qubit gates. **G-OI6-12 [OPEN]:** establish a stable action and its constraint algebra, without assuming the desired representation.

## G. Reproduction and established mathematical references

The standard-library Python script verify_lorentz_algebra_carrier.py contains 12 tests covering invariants, vectorization, multiplicativity, Hermiticity, rank, concurrence and generic SU4 nonpreservation. All 12/12 tests of the exact GitHub script passed in local Python execution on 2026-11-11; its local Git blob SHA 14049662bcad8daa81c3ae92332706cb1827ec69 matches the uploaded file. Independently executed NumPy calculations also confirm the key formulas. These are mathematical checks, not experimental support for UBT.

- Tübingen lecture notes on Lorentz spinors: https://www.math.uni-tuebingen.de/de/forschung/maphy/lehre/ws-2025-26/grar/dateien/notes.pdf .
- MathWorld on column-major vectorization: https://mathworld.wolfram.com/MatrixVectorization.html .
- Milne, *Algebraic Groups*, Skolem–Noether theorem: https://www.jmilne.org/math/Books/iAG2022.pdf .