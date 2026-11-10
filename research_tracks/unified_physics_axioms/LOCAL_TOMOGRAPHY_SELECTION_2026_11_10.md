# Inverse axiom selection II: local tomography, Jordan cones and complex spinors

**Status:** research track / qualified established mathematics + explicit counterexamples, 2026-11-10.
**Not claimed:** unique microscopic UBT field, unique action, gravity/SM/QFT reconstruction, superluminal signalling or quantum-gravity completion.

## 1. An operational condition that can select a scalar field

**Local tomography (LT).** For a composite AB, the statistics of product effects \(e_A\otimes f_B\), including their correlations, determine every physical state of AB. In a finite-dimensional locally tomographic non-signalling GPT, the real linear state-space dimensions obey \(d_{AB}=d_A d_B\), under the specified nonrestrictive product-effect span assumptions. This condition is not the same as saying that the states of A and B individually determine AB.

Consider the standard simple Euclidean Jordan/matrix-state families over \(\mathbb R,\mathbb C,\mathbb H\). Their real dimensions are:
\[
d_{\mathbb R}(n)=n(n+1)/2,\quad
d_{\mathbb C}(n)=n^2,\quad
d_{\mathbb H}(n)=n(2n-1).
\]
For two elementary two-level systems, standard matrix-size-composition \(n_A=n_B=2\to n_{AB}=4\) gives:

| Hermitian matrices | \(d(2)\) | \(d(4)\) | \(d(2)^2\) | Dimension equality? |
|---|---:|---:|---:|---|
| real | 3 | 10 | 9 | no |
| complex | 4 | 16 | 16 | yes |
| quaternionic | 6 | 28 | 36 | no |

**Scope warning:** quaternionic tensor composition requires extra structure; the 28-vs-36 comparison only refutes the **naive standard H_4(H) composite** as locally tomographic, not every conceivable quaternionic or quaternion-valued theory. A fundamental field with values in C⊗H is not the same thing as quaternionic-Hilbert-space quantum mechanics: C⊗H is isomorphic to the ordinary complex matrix algebra M2(C). Avoid falsely excluding UBT using this table.

## 2. Explicit real-theory witness (not dimension counting alone)

Set \(J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\). Its real tensor square \(K=J\otimes J\) is a real symmetric 4x4 matrix, because the transpose of each factor is -J. For arbitrary real symmetric 2x2 observables A,B:
\[
\operatorname{tr}[K(A\otimes B)]
=\operatorname{tr}(JA)\operatorname{tr}(JB)=0.
\]
Yet K is nonzero, symmetric, and K²=I4. Therefore the matrices
\[
\rho_\pm=\tfrac14 I_4\pm\tfrac18 K
\]
are two distinct valid real density matrices with eigenvalues 1/8 and 3/8 (each twice), indistinguishable by **all** local product effects. This disproves local tomography of standard two-rebit real quantum theory, under that composition rule.

By contrast, for complex Hermitian n-by-n matrices, the Hermitian products of local bases span the full Hermitian composite, and \(d_C(nm)=(nm)^2=n^2m^2\).

## 3. Stronger conditional selection theorem (not our novel theorem)

Barnum and Wilce, *Local Tomography and the Jordan Structure of Quantum Theory*, Foundations of Physics 44, 192–212 (2014), https://doi.org/10.1007/s10701-014-9777-1 (preprint https://arxiv.org/abs/1202.4513), using a result of Hanche-Olsen, show complex quantum theory with possible superselection under **all of**:
- finite-dimensional non-signalling probabilistic framework and appropriate definitions of composites;
- individual systems have Euclidean Jordan state structures (homogeneous and self-dual cones under stated conditions);
- composites are locally tomographic;
- at least one system has qubit structure;
- additional natural compatibility constraints as precisely given in that theorem.

Do **not** say “local tomography alone proves complex QM”: a classical probabilistic theory is itself locally tomographic. Nor assert this theorem automatically holds in arbitrary fermionic local QFT, gravitational gauge constrained sectors, or all infinite-dimensional theories. The inverse challenge for UBT is to explain independently why these assumptions are physically mandatory over the intended domain.

## 4. Link back to Minkowski cone and C⊗H

On the chosen complex two-level subsystem,
\[
X=x^0 I+\sum_i x^i \sigma_i,\quad
\det X=(x^0)^2-|\mathbf x|^2,\quad
X\ge0\iff x^0\ge|\mathbf x|.
\]
Normalized qubit states are a trace-one slice of this future Lorentz cone. The linear complex endomorphism algebra of S=C² satisfies:
\[
\operatorname{End}_C(S)=M_2(C)\cong C\otimes H.
\]
The map \(X\mapsto AXA^\dagger\) (A in SL2(C)) realizes the spin double cover of proper orthochronous Lorentz transformations on the Hermitian cone; its boosts do not preserve trace, so they are **not** deterministic normalized qubit gates. This is exact shared geometry, not evidence that a qubit is a spacetime event.

**Selection so far:** under local tomographic composition + Jordan/qubit hypotheses, conventional complex quantum kinematics is preferred among the explicitly compared alternatives. Together with a minimum complex 2-spinor **representation choice**, the natural endomorphism algebra is biquaternionic. The extra assumption “fundamental spacetime field equals that endomorphism algebra” remains unproved.

## 5. Necessary next inverse gates

**G-LT-1: applicability of local tomography.** Check which operationally separable subsystem pairs in relativistic QFT satisfy the finite-dimensional premise; explicitly account for parity superselection, gauge constraints, type-III local operator algebras, and gravitational edge modes. Failing a naive condition outside its domain does not invalidate the actual empirically tested phenomena.

**G-LT-2: minimal two-spinor selection.** Derive from actual measured spin-1/2, chiral behavior and Lorentz covariance exactly which representation assumptions are needed; distinguish two-component Weyl from four-component Dirac fields. Show a countermodel with ordinary complex QFT and no fundamental Theta.

**G-LT-3: dynamics.** The Jordan and cone theorems do **not** fix a unique action. To select S_UBT, derive additional invariant and derivative constraints, complete composite variation including torsion, and physical constrained Hamiltonian. In particular, an arbitrary symmetry-compatible \(R^2\) EFT term demonstrates underdetermination even after choosing the metric cone.

**G-LT-4: empirical held-out tests.** Recover the measured local quantum and relativistic responses, and generate genuinely new fixed-parameter predictions. No hand-inserted Einstein, Yang–Mills or Born dynamics may be labelled “derived”.

## 6. Tests and proof boundaries

Companion \`tests/test_inverse_axioms_local_tomography.py\` verifies dimension relations for real/complex/quaternionic Hermitian matrices, an exact real two-rebit invisible global correlation, and positivity/distinctness of the two witness states. These are finite exact algebraic checks. They do not prove the Barnum–Wilce theorem or UBT's fundamental uniqueness.

Links:
- Earlier first derivations: [FIRST_DERIVATIONS_2026_11_10.md](FIRST_DERIVATIONS_2026_11_10.md)
- [Inverse research plan](README.md)
- [Canonical action registry](../../canonical/ACTION.en.md)
- [Barnum–Wilce](https://arxiv.org/abs/1202.4513)
- [Review of GPTs](https://doi.org/10.1016/j.physrep.2023.09.001)
