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

# OI-6 — Connected reversible entanglement and the missing interaction axiom

**Status:** elementary conditional quantum-control mathematics [STD]; derivation of the interacting carrier from information [OPEN]. This is a comparison with existing work, not a new UBT physical result.

## A. What the previous countermodel does not have

The minimal tensor product of generalized bits permits connected local SO(n) rotations and is locally tomographic, yet contains only separable states. Thus continuous reversible pure-state transitivity is weaker than an actual reversible interaction coupling distinct subsystems. This note adds the interacting dynamics **only in the standard complex two-qubit Hilbert model**, as an explicit conditional comparator.

## B. OI-6-T8 — Local reversible groups cannot create entanglement

A local tensor-product unitary maps product pure states to product pure states and separable mixtures to separable mixtures. It preserves the spectrum of each reduced pure-state density matrix up to a local unitary conjugation. Therefore local unitary dynamics cannot entangle an initially separable state.

$$
(U_A\otimes U_B)(\rho_A\otimes\rho_B)
(U_A^\dagger\otimes U_B^\dagger)
=(U_A\rho_AU_A^\dagger)\otimes(U_B\rho_BU_B^\dagger).
$$

**OI-6-T8 [STD, conditional]:** local reversible operations do not supply the missing nonlocal interaction. The assumption of connected local reversible symmetries by itself cannot close OI-6.

## C. OI-6-T9 — One continuous interaction can generate entanglement

Assume the standard complex two-qubit tensor-product Hilbert space and the nonlocal Hamiltonian consisting of a Pauli-X product. Since its square is identity, its continuous reversible evolution has an exact elementary form:

$$
H_{\rm int}=\sigma_x\otimes\sigma_x,\quad
U(t)=e^{-itH_{\rm int}}=\cos t\,I_4-i\sin t\,(\sigma_x\otimes\sigma_x).
$$

For the initial product state, the reduced-state purity is below unity for intermediate nontrivial evolution parameters. A pure bipartite state has this property precisely when it is entangled.

$$
U(t)|00\rangle=\cos t\,|00\rangle-i\sin t\,|11\rangle,\quad
{\rm Tr}\,\rho_A(t)^2=1-\frac12\sin^2(2t).
$$

**OI-6-T9 [STD, conditional]:** this explicit unitary path creates a maximally entangled state at t=pi/4 from a product state, while remaining continuously reversible. Nothing here derives the existence or coupling constant of the nonlocal Hamiltonian from information alone.

## D. OI-6-T10 — Local controls plus one interaction close the full Lie algebra

With unrestricted independent local SU(2) controls, the anti-Hermitian generators span the local direct-sum Lie algebra. Commutators with one nonzero XX coupling generate all Pauli products: local rotations change the first Pauli axis, then the second, producing every two-body Pauli direction. Together with the local basis these are all traceless anti-Hermitian two-qubit generators:

$$
\mathfrak l_{\rm loc}
=\operatorname{span}_{\mathbb R}\{i\sigma_a\otimes I_2,\ iI_2\otimes\sigma_b:
a,b\in\{x,y,z\}\},\qquad \dim\mathfrak l_{\rm loc}=6.
$$

$$
\operatorname{Lie}\langle\mathfrak l_{\rm loc},
i\sigma_x\otimes\sigma_x\rangle=\mathfrak{su}(4),\qquad
\dim\mathfrak{su}(4)=15.
$$

**OI-6-T10 [STD, conditional]:** one continuously controllable XX interaction and all independently controllable local SU(2) directions generate the full su(4) Lie algebra. The same conclusion holds when XX is replaced by any single nonzero Pauli-product coupling with both factors nonidentity. The exact Pauli-commutator calculation and real basis count are verified by the script. This is the standard quantum controllability Lie-rank criterion, not a unique UBT prediction.

## E. Why this does not reconstruct Theta or quantum theory

The two-qubit vector space and the vectorization of the canonical UBT biquaternion field are both complex four-dimensional carriers. Their vector-space isomorphism is trivial and does **not** specify a physically preferred tensor factorization, multiplication-preserving isomorphism, UBT tetrad, metric, action or ghost-free dynamics. The two-qubit Hilbert model, its Hermitian operators, complex amplitudes and nonlocal coupling were assumed before the calculation.

The literature theorem of de la Torre, Masanes, Short and Müller (2012) identifies the standard complex two-qubit theory from **already-fixed local qubit structure plus existence of a continuous reversible interaction** within its stated framework. Masanes, Müller, Pérez-García and Augusiak (2014) extend the comparison to locally tomographic Euclidean-ball systems. These are already-published classification results, not independent novel derivations made here.

### E.1 — OI-6-T11: The vector-carrier identification is not an algebra isomorphism

The Skolem–Noether theorem states that every unital complex-algebra automorphism of the full matrix algebra is inner conjugation by an invertible matrix, modulo a central nonzero scalar. Its complex dimension is therefore smaller than the full two-qubit special-unitary group:

$
\operatorname{Aut}_{\mathbb C\text{-alg}}(M_2(\mathbb C))
\simeq\operatorname{PGL}_2(\mathbb C),\qquad
\dim_{\mathbb R}=6,\qquad \dim_{\mathbb R}\operatorname{SU}(4)=15.
$

To see the concrete obstruction independently of dimension counting, identify the same four-component complex vector with a matrix through column-major vectorization and let the entangling unitary act **linearly on the vectorized matrix**. Two orthogonal idempotents have zero product, but after the resulting vector action their images need not have zero product:

$
\Phi_t(E_{00}E_{11})=0,\qquad
\Phi_t(E_{00})\Phi_t(E_{11})
=-i\cos t\sin t\,I_2\ne0,\qquad
\Phi_t=\operatorname{vec}^{-1}e^{-it\sigma_x\otimes\sigma_x}\operatorname{vec}.
$

**OI-6-T11 [STD, conditional]:** a general reversible two-qubit SU(4) transformation is not a unital multiplicative automorphism of the biquaternion algebra M2(C). The calculation is a counterexample to a naive identification of qubit controllability with UBT algebraic symmetry. It does not determine which multiplication-compatible transformations, if any, are physical UBT gauge transformations. The full vector carrier and algebra structure must be distinguished.

Reference: [Skolem–Noether for finite-dimensional central simple algebras](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_7).

## F. Reproducibility, gates, and prior art

The standard-library script research_tracks/ontological_information_axioms/verify_entangling_lie.py passed 11/11 local tests on 2026-11-11, and the executed file's Git blob SHA matched the GitHub copy exactly. Tests include all Pauli-pair commutators, 6 versus 15 Lie dimensions, all Pauli two-body interaction types, an exact reversible entangling path, local purity and global Pauli orthogonality. Unit tests reproduce standard finite algebra; they are not physical experiments.

**G-OI6-7 [OPEN]:** independently motivate a nonlocal reversible interaction from an information/composition principle rather than inserting an entangling generator. **G-OI6-8 [OPEN]:** show why the operational local carrier must be complex, two-level and composed as a Hilbert tensor product. **G-OI6-9 [OPEN]:** map the selected carrier and interactions to the noncommutative multiplication, Theta covariant derivative, local constraints and stable UBT action; then check GR and SM limits.

- de la Torre, Masanes, Short and Müller, *Deriving Quantum Theory from Its Local Structure and Reversibility*, Physical Review Letters (2012), https://doi.org/10.1103/PhysRevLett.109.090403 .
- Masanes, Müller, Pérez-García and Augusiak, *Entanglement and the three-dimensionality of the Bloch ball*, Journal of Mathematical Physics (2014), https://doi.org/10.1063/1.4903510 .