# Inverse UBT: algebraic noninjectivity, quantum erasure and Landauer's principle

**2026-11-10 | Status:** exact elementary algebra and quantum-channel comparator; UBT-specific selection/action and saturation of Landauer bound **OPEN**.

## Hypothesis

Microscopic reversibility need not imply that a locally accessible subsystem retains all its initial information. Physical distinguishability may be lost under reduced dynamics while the inaccessible environment acquires correlations or records. The user's point about multiplication is therefore relevant, but three distinct operations must never be conflated:
- unknown factorization of a product;
- an algebraically noninjective map when one factor is fixed;
- a physical irreversible reset channel with a thermal implementation.

## Real quaternion vs biquaternion multiplication

The real Hamilton quaternion algebra H is a normed division algebra; for any a != 0, the fixed-left-multiplication map L_a(q)=a q is invertible with L_a^{-1}(b)=a^{-1}b. Multiplication of two unknown factors (a,q) to one product is many-to-one because the full input has twice as many coordinates; **this is not automatically erased physical information** when the factors or environment are retained.

For complex biquaternions H⊗C ≅ M2(C), zero divisors exist. Let P=diag(1,0), X1=diag(1,0), X2=I. Then P X1=P X2=P although X1!=X2. L_P is a noninjective complex linear map on M2(C); its kernel consists of matrices with zero first row, and has complex dimension two. This is a precise loss of algebraic distinguishability under an externally selected projection. But **P X is not a normalized density matrix channel on its own** and does not imply any heat production.

## CPTP reset using biquaternion matrices

Take K0=|0><0| and K1=|0><1| in M2(C). They obey K0†K0+K1†K1=I. Then for every density matrix rho:
\[
E(\rho)=K0\rho K0^\dagger + K1\rho K1^\dagger = |0\rangle\langle0|.
\]
This is a completely positive trace-preserving reset and destroys all distinctions between initial reduced density matrices as seen from its output.

The reduced channel admits a reversible global implementation: SWAP system S with an environment qubit E initially |0>. For |psi>_S|0>_E the global unitary returns |0>_S|psi>_E. This does **not** destroy global information: it moves it. Mixed and entangled input cases require extending the channel and keeping appropriate reference correlations; the global swap still implements the local reset.

**Clarification**: K0 and K1 lying in the biquaternion matrix algebra is a *representation* of a standard quantum channel. The existence of a Kraus decomposition alone does not prove UBT produces irreversible dynamics uniquely or that matrix multiplication physically erases a bit.

## Landauer link and limits

For reset of a fully unknown unbiased bit in a cyclic implementation with a reservoir at positive temperature T, the textbook thermodynamic lower bound for erased one bit is W_min = k_B T ln2 (with conventional ideal degenerate memory and quasistatic limiting assumptions), and heat must be dumped to environment under an appropriate setup. A merely noninjective algebraic map gives no T, Hamiltonian, work protocol or bath, hence predicts **no** Landauer energy. Quantum corrections, finite-time constraints, energy spectra, correlations and reservoir size can affect practical work/heat bounds.

The thermodynamic **reversible ideal limit** can saturate the Landauer bound while its logical map remains irreversible. A physical protocol approaching saturation needs a specified bath and control scheme, not arbitrary collisions, and “all interactions erase one bit at the Landauer limit” is false.

## Connection to a candidate information principle

**Candidate IP-reduced:** there is a larger operationally composable positive quantum state space with reversible/causal evolution; accessible subsystems can undergo noninjective reduced channels via interactions and discarding environments; erasure costs are determined by physical thermodynamics and second-law constraints. Whether global evolution is strictly unitary remains a *testable/conditional premise*, not to be silently inserted as an axiomatic necessity of UBT.

Required UBT derivation chain:
1. derive from minimal relativity/information axioms the appropriate algebra of physical states (not postulate M2(C) in advance);
2. select the subsystem structure and physically observable projections via a justified experiment/readout map;
3. derive reduced CPTP dynamics (or a more general operationally consistent alternative) from a single action and environmental coupling;
4. derive/verify the system-bath entropy balance, precise thermodynamic assumptions, and Landauer-like bound, including correlations;
5. check compatibility with fermionic parity superselection, bosonic CCR, spin-statistics, gravity/torsion and energy conservation;
6. predict a measurable constraint inaccessible to a mere arbitrary matrix rewriting of standard quantum mechanics.

## Status/claims

- **EXACT algebra:** nonzero real quaternion multiplication invertible; rank-one biquaternion left multiplication noninjective.
- **EXACT quantum theory:** the K0,K1 reset is CPTP and admits a global SWAP unitary dilation.
- **ESTABLISHED thermodynamics:** conditional Landauer minimum work for resetting an unbiased bit in standard thermal setup; saturation is a limiting protocol, not an automatic property of interactions.
- **OPEN UBT:** physical projection selected by information axioms; dynamical mechanism; temperature/entropy coupling; any novel prediction or proof of UBT.

References:
- Landauer bound overview: https://pmc.ncbi.nlm.nih.gov/articles/PMC11119825/
- Thermodynamics of computation review: https://pubmed.ncbi.nlm.nih.gov/40345217/
- Stinespring dilation / quantum channels: https://doi.org/10.1109/TIT.2008.917696

Related: [inverse physics programme](README.md), [fermionic information and entanglement](ENTANGLEMENT_SPIN_STATISTICS_INVERSE_2026_11_10.md).
