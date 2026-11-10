# Entanglement and statistics as separate inverse principles of UBT

**Status:** research / standard algebraic comparison and a hard no-go, 2026-11-10. Fundamental UBT dynamics and emergence of both statistics OPEN.

## Clarification of hypothesis

The user-intended "instantaneous information component" is **quantum entanglement/correlation**, *not controllable instantaneous transfer of a message*. Do not equate a conditional update of a state assignment with a physical signal. Fermionic states may be entangled, but so may bosonic states; entanglement is not exclusive to either sector and does not itself select the exchange statistics.

Instead distinguish three operationally separate mathematical structures:
1. **Spin/Lorentz representation**: action of Spin(1,3), including central 2pi rotation.
2. **Exchange statistics/quantum operator algebra**: CAR vs CCR (or appropriate algebraic QFT observables); fixed only with further locality, positivity, spectra assumptions.
3. **Multipartite correlations/entanglement**: separability with respect to a specified subsystem decomposition and admissible local observable algebras, incorporating fermion-parity superselection when relevant.

## A precise inverse clue from two-particle spin

Let the central element of Spin(1,3) corresponding to a full 2pi rotation be z=-1. A spin-j irreducible representation satisfies
\[
D_j(z)=(-1)^{2j} I.
\]
Thus central character +1 corresponds to integer spin and -1 to half-integer spin. In the standard relativistic local QFT under positive-energy, positive-norm and standard field-locality hypotheses, the **spin-statistics theorem** relates this central character to Bose/Fermi exchange algebra. It does not follow from central character or geometric Clifford grade alone.

This character is NOT the geometric grade automorphism alpha(X_k)=(-1)^k X_k. A Clifford-even spinor represented using Hestenes machinery may have D(z)=-1 under left spin action, whereas a Clifford-even bivector observable transforms by conjugation and has D(z)=+1. The same even algebraic carrier can therefore represent both transformation types. This is a representation distinction, not a gradewise particle classification.

## Fermionic Clifford algebra vs bosonic Weyl algebra

For n independent fermion modes c_i, CAR yield
\[
\{c_i,c_j^\dagger\}=\delta_{ij},\ \{c_i,c_j\}=0.
\]
Define Majorana operators \(q_{2i-1}=c_i+c_i^\dagger,\quad q_{2i}=i(c_i^\dagger-c_i)\). Then \(\{q_a,q_b\}=2\delta_{ab}\). This is the **complex Clifford algebra of fermionic MODE space**, not canonically the real Lorentzian spacetime Clifford algebra Cl(1,3). For n fermionic modes its Fock space has dimension 2^n, with a finite-dimensional matrix representation of the complex CAR algebra.

Bosonic oscillator modes obey \([b_i,b_j^\dagger]=\delta_{ij}I\). In canonical quadratures \([Q_i,P_j]=i\delta_{ij}I\), forming a Heisenberg/Weyl/CCR algebra with symplectic structure. **No finite-dimensional complex matrices can satisfy this exact CCR**, since trace([Q,P])=0 but trace(iI)=iN != 0. Thus a *single finite-dimensional Clifford algebra by itself* cannot algebraically contain the **exact** bosonic oscillator CCR as operators in a faithful finite-dimensional representation. Ordinary bosonic field excitations must use an additional infinite-dimensional representation, field-mode limit, or an emergence mechanism with a carefully specified approximation.

This is an important boundary against the overstrong statement "full Cl(1,3), with its 16 real components, already contains all bosons and fermions." It may **encode field components** and their Lorentz representations, but that does not furnish the quantum Fock operator algebras automatically. Quantizing a bosonic field with components valued in Cl can produce an infinite-dimensional CCR representation; this adds quantization and is not merely the finite algebra itself.

## Entanglement is not signalling

For any bipartite density matrix rho_AB, any local trace-preserving quantum channel E_A gives
\[
\mathrm{Tr}_A[(E_A\otimes \mathrm{id}_B)(\rho_{AB})]=\mathrm{Tr}_A(\rho_{AB}).
\]
Entanglement can be present and supply nonclassical correlation, but unconditioned local measurement statistics on B remain unchanged. Fermionic bipartitions must respect parity-superselection, graded tensor products and physically measurable even subalgebras. No instantaneous communication is inferred or attributed to the original hypothesis.

## Information principle candidate (a hypothesis, not derived)

**IP-graded:** physical theory admits operationally composable state/observable algebras with (i) a causal, positive physical state space, (ii) allowed nonclassical multipartite correlations, (iii) a representation of spacetime symmetries, (iv) a physically meaningful exchange operation and (v) local observable (graded) commutation requirements. The boson/fermion distinction is to be *derived* from covariance, positive energy, locality and exchange, rather than assigned to geometric Clifford grades.

What this does NOT yet fix:
- whether the entire microscopic field must be real full Cl(1,3), its complexification, or a spinor module;
- a unique fundamental UBT action and composite metric/torsion;
- CAR/CCR as deductions from only relativity + unspecified information;
- the standard model gauge/representation content or the proper physical vacuum.

## First mathematical selection gates

1. **G1 two-particle exchange:** construct physically admissible local observables and exchange transformations from the same operational composition rule; compare bosonic and fermionic parity sectors without inserting CAR or CCR at the outset.
2. **G2 spin-statistics:** state and check exact hypotheses needed for connection between central spin character z=-1 and statistics. Identify which are already assumed in proposed UBT; do not treat known theorem as a new UBT proof.
3. **G3 Clifford compatibility:** distinguish grade automorphism, spinor left action, adjoint multivector action, and Fock fermion parity. Provide representation dictionary for all.
4. **G4 entanglement:** compare admissible fermionic and bosonic bipartite entanglement/correlation measures at equal resources; preserve no-signalling.
5. **G5 single dynamical action:** only after the field vs operator-algebra distinction is resolved, attempt a full composite constrained Hessian and quantum-state construction, recovering measurable bosons/fermions and their interactions from one theory.

## Claim ledger

- [STD] central spin element acts as (-1)^(2j); local relativistic QFT spin-statistics under its assumptions.
- [STD exact] finite CAR Majorana–Clifford mapping; infinite-dimensional CCR no-go via trace.
- [STD] entanglement need not transmit information and exists in bosonic and fermionic systems.
- [OPEN] operational principle uniquely requiring a fundamental full Clifford UBT field and a selected action.
- [OPEN] emergence of CAR, CCR, QFT, GR, SM, and thermodynamics from that action.
- [REJECTED] identification of Clifford grade parity with fermion parity; exclusive fermion entanglement; FTL inference.

Related:
- [Fermionic info versus bosonic interactions](FERMION_INFORMATION_BOSON_INTERACTION_2026_11_10.md)
- [Grading / parity distinction](CLIFFORD_GRADING_VS_FERMION_PARITY_2026_11_10.md)
- [Unified inverse research program](README.md)
