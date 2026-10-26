# SU(3) selection gate: biquaternion automorphisms versus eight-dimensional adjoint representation

**2026-10-26; exact structural obstruction, not a full no-go for emergent color.**

The associative complex biquaternion algebra is B=H tensor_R C ≅ Mat_2(C), complex dimension 4 / real dimension 8. Its commutator Lie algebra satisfies [B,B]=sl_2(C), real dimension 6, while the complex scalar center Z(B)=C I has real dimension 2. Thus the eight *coordinates* of B are NOT the eight generators of su(3).

Every unital C-linear algebra automorphism of Mat_2(C) is inner (Skolem–Noether), Aut_C(B)=PGL_2(C), real dimension 6. Consequently an **effective** SU(3) action by continuous C-linear multiplicative automorphisms of one B cannot exist: an infinitesimal injective Lie algebra homomorphism su3 (real dimension 8) to sl2(C) (real dimension 6) is impossible. In fact every Lie homomorphism from simple su3 into this target must be zero: its kernel is an ideal, so nonzero implies injective.

This excludes SU(3) **as a nontrivial algebra-automorphism symmetry of one canonical biquaternion**. It does NOT exclude an emergent SU(3) realized on composites, three copies of B, an independently derived rank-three internal bundle, or as a representation on an eight-real-dimensional vector space *after introducing extra structure*. SU(3)'s adjoint action on su3 provides a real 8-dimensional orthogonal representation, but transporting that action to the underlying real vector space of B by arbitrary linear identification does NOT preserve B's original associative product or its canonical Lorentz action. Therefore choosing the adjoint representation solely because both spaces have dimension eight is a change of dynamical assumptions, not derivation.

**Hamiltonian significance.** In a genuine su3 Yang–Mills sector, independent color gauge fields A_mu^a and Gauss-law constraints can remove unphysical polarizations of those gauge connections. They do not automatically remove six wrong-sign kinetic directions of original Theta: this requires a specified gauge action on Theta, first-class constraints emerging from ONE action, closure without anomalies, and positivity of the *reduced* Hamiltonian. One cannot infer eight first-class Theta constraints from eight generators. Gauge group dimension counts gauge directions only after field content/representation and action are fixed.

**Open constructive alternatives, ranked:**
1. Derive a natural three-dimensional complex internal module from Theta composites, with an invariant positive Hermitian form and determinant; then SU(3) may act there. Determine whether this is more than an additional postulate.
2. Examine three distinguishable physical channels/modes in the quantum observable algebra and their unitary mixing, while imposing shared-reality gauge covariance.
3. Require explicit reduction to quark fundamental triplets, gluon adjoint octet, anomalous representation consistency, and a healthy QCD-like Gauss constraint algebra.

Reproduction: tests/test_information_su3_biquaternion_obstruction.py.
