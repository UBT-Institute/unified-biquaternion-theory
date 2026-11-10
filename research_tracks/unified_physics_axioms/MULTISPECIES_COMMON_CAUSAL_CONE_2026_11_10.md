# Inverse UBT: two-species characteristic-cone selection

**2026-11-10 | status: exact conditional lattice comparator; NOT a fundamental UBT derivation of universal c, geometry, or gravity.**

## Question

Can operational information dynamics cause two inequivalent excitations in the *same* quantum network to share a unique long-distance causal cone? This is necessary for any universal emergent spacetime metric, but cannot be inferred merely from entanglement or common graph adjacency.

## Exact 1+1D two-species model

Work in units hbar=1. Let ell>0 be lattice spacing; take a two-component (pseudospin) Hilbert space and two flavors with Hermitian single-particle Bloch Hamiltonian
\[
H(k)=\frac{\sin(k\ell)}{\ell}\sigma_x\otimes V,\quad
V=\mathrm{diag}(v_A,v_B),\quad v_A,v_B>0.
\]
The spectrum is
\[
E_{s,\pm}(k)=\pm (v_s/\ell)\sin(k\ell),\qquad
v_{g,s,\pm}(k)=\partial_k E_{s,\pm}=\pm v_s\cos(k\ell).
\]
For k ell << 1 this has two continuum massless Dirac-like principal speeds v_A and v_B. At finite lattice spacing, dispersion is nonlinear and periodic. There are also additional gapless points (fermion-doubling-style artifacts) at Brillouin-zone edges; do not interpret this as exact Lorentz invariance or a complete fermionic field theory. The one-particle matrix expression is not itself a Fock-space statistics assignment; both bosonic and fermionic quantizations can require further choices/constraints.

The effective low-momentum characteristic polynomials in a 1+1D continuum description are
\[
p_s(\omega,k)=\omega^2-v_s^2k^2,
\quad
p_{\rm combined}=(\omega^2-v_A^2k^2)(\omega^2-v_B^2k^2).
\]
If v_A!=v_B, the principal characteristic set contains two distinct cones. No single Lorentz metric describes both modes as sharing the same null cone. Reparametrizing space and time simultaneously rescales both speeds but cannot remove their ratio v_A/v_B. This is a precise obstruction to **universal** emergent metric causality in this restricted model.

## Exact flavor exchange condition

Let F=I_2 ⊗ tau_x be the flavor swap operator. It is unitary, F²=I. Then
\[
F H(k) F^{-1} = \frac{\sin(k\ell)}{\ell}\sigma_x\otimes \mathrm{diag}(v_B,v_A).
\]
Demand invariance FHF^{-1}=H for all k: this implies v_A=v_B=v_*. Conversely equality suffices for invariance. The same condition gives coincident low-k cones.

**Important scope:** internal flavor interchange is an EXTRA postulate, not a consequence of information composability or Cl grading. Many observed massive and interacting fields have distinct dispersions in media. Exact microscopic interchange symmetry may be explicitly or spontaneously broken, and equal microscopic coefficients need not survive quantum corrections without protecting symmetry. This comparison does not prove that all Standard Model excitations are related by one such symmetry.

## Generalization and Clifford relevance

For distinct species s with anisotropic long-wave principal symbols
\[
p_s(\omega,\mathbf k)=\omega^2-\sum_i v_{s,i}^2 k_i^2,
\]
a universal effective null cone requires matching quadratic forms up to a positive overall conformal factor in a common spacetime frame. A simple common geometry emerges if every v_{s,i}=v_* in appropriate isotropic coordinates, but these equalities are additional dynamical symmetry/flow conditions, not implications of an abstract complex Hilbert or Clifford field-value algebra.

A Clifford system of anticommuting kinetic matrices gamma^i can linearize a chosen dispersion, but \(\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}\) does NOT determine the metric coefficients g or force all particle species to couple to the same emergent tetrad. Even/odd Clifford decompositions, fermion parity and entanglement are distinct issues.

## No circularity

1. This model starts with a fixed 1D lattice graph and time parameter; it does not derive spatial topology, Lorentzian signature or units.
2. The common cone is a **small-k** result; Lieb–Robinson velocity bounds, group velocity, front velocity and exact continuum microcausality must not be automatically identified.
3. The flavor-swap symmetry is inserted to see what it suffices to select, not derived from a minimal operational information principle.
4. It does not derive c, gravitational G, holographic entropy, horizons, torsion, Standard Model fields or a unique UBT action.
5. The 1+1D model has additional Brillouin-zone gapless points; continuum uniqueness and chiral spectrum require separate study.

## Next inverse gates

- C1: derive a common causal/observable algebra from operational composition and admissible interventions without first imposing metric adjacency.
- C2: derive or justify protection of a universal kinetic principal symbol in a realistic 3+1D system under radiative corrections and distinct spin/statistics.
- C3: find whether a single emergent Clifford coframe and covariant derivative with universal matter coupling follows, or is merely another selectable ansatz.
- C4: identify causal horizons and universal renormalized entanglement entropy, derive Newton G from microscopic scales, then test conditional Jacobson closure.
- C5: check physical gravitational tensor modes, Hamiltonian constraints, torsion, and existing canonical UBT no-go results. No claim of full gravity closure until these pass.

Related: [operational influence model](LOCAL_INFLUENCE_COMMUTATOR_2026_11_10.md), [area law](ENTANGLEMENT_BOUNDARY_AREA_G_SELECTION_2026_11_10.md), [horizon gravity](LOCAL_HORIZON_INFORMATION_EINSTEIN_CLOSURE_2026_11_10.md).
