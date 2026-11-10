# Inverse-physics research: fermionic information, bosonic interactions, and causal constraints

**2026-11-10 | status: HYPOTHESIS + existing QFT results + exact no-signalling lemma.**
This is not a new proven UBT dynamics, an explanation of spin-statistics, or evidence of instantaneous/FTL signalling.

## Proposed hypothesis and its restricted interpretation

Working hypothesis H-FBI: fermionic modes can furnish finite-occupancy, parity-graded information degrees of freedom; selected bosonic modes can mediate dynamical interactions and transmit signals. This is an operational **role distinction in selected regimes**, not an ontological equivalence:
- Both bosons (photons, phonons) and fermions (electrons, etc.) can carry/encode classical and quantum information.
- Fermions participate in interactions, and bosons are not all force mediators (Higgs and composites).
- Entanglement/nonlocal correlation is not instantaneous controllable communication.
- In ordinary QFT a fermion field is a quantum field transforming spinorially; a Clifford grade-even representation of a spinor does not dictate Bose or Fermi exchange algebra. The latter requires the quantum (anti)commutator and a consistent spin-statistics construction.

## Hard kinematic difference: CAR and CCR

For independent fermionic modes:
\[
\{c_i,c_j^\dagger\}=\delta_{ij},\quad
\{c_i,c_j\}=0\quad\Rightarrow\quad (c_i^\dagger)^2=0.
\]
Single-mode fermion Fock space has states |0>,|1>; Pauli exclusion provides finite occupation.

For independent bosonic modes:
\[
[b_i,b_j^\dagger]=\delta_{ij},\quad[b_i,b_j]=0.
\]
Single-mode boson occupation n=0,1,2,... is unbounded in the ideal algebra. This does not imply any universal information-capacity advantage without specifying energy, particle number and protocol constraints.

Fermionic parity is \((-1)^F\) on the *quantum* Fock representation; it is not the geometric grade automorphism of Cl(1,3). Physical fermionic observables obey even-parity superselection in the usual formulation. Even local observables in disjoint spacelike regions commute, although elementary fermionic fields may anticommute at spacelike separation. The relevant causal test is the algebra of **measurable observables**, not the sign of the raw fields.

## Exact no-signalling calculation

For any bipartite density matrix \(\rho_{AB}\) and any completely positive trace-preserving local quantum channel \(\mathcal E_A(X)=\sum_k M_k X M_k^\dagger\) satisfying \(\sum_k M_k^\dagger M_k=I_A\):
\[
\rho_B' = \operatorname{tr}_A[(\mathcal E_A\otimes \mathrm{id}_B)(\rho_{AB})]
=\operatorname{tr}_A \rho_{AB}
=\rho_B.
\]
This follows from cyclicity of the partial trace for operators acting entirely on A. Hence any deterministic local operation on A, without post-selection or subsequent classical communication, leaves all Bob measurement probabilities unchanged. Correlations can change conditionally on an Alice outcome, but Bob cannot detect that choice without receiving its result. A nonlocal hidden-state update is not a communication channel.

For example \(|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2\) has \(\rho_B=I/2\). Alice applying I, Z, or a nonselective projective measurement does not change \(\rho_B\).

*Scope:* this ordinary tensor-product demonstration illustrates the operational no-signalling theorem. For fermionic spatially separated regions, parity-graded tensor products, local observable algebras and allowed physical operations must be handled correctly; do not assume naively factorized fermionic modes in place of local parity-even observables.

## Evidence and constraints

- Sen(De) et al., Phys. Rev. A 75, 022331 (2007), DOI 10.1103/PhysRevA.75.022331: information capacity comparisons depend on energy and occupancy constraints; both bosonic and fermionic channels carry information.
- Fermionic quantum operations respecting superselection and no-signalling: Phys. Rev. A 104, 032411 (2021), DOI 10.1103/PhysRevA.104.032411.
- Kalarde et al., "Fermions are fundamentally more nonlocal than Bosons," arXiv:2606.12363 (preprint, June 2026): under specified quantum network resource and indistinguishability assumptions, fermionic correlations outperform certain bosonic/distinguishable-particle protocols *without claiming FTL communication*. Treat as a recent theoretical result, not independent experimental proof of UBT.
- Physics beyond naive local tomography: fermionic parity superselection can constrain local operational state composition; do not universalize earlier finite-dimensional qubit Jordan reconstruction to every fermionic subsystem.

## UBT-specific inverse selection gates

**Gate F1: operational criterion.** Define what counts as "information": accessible classical capacity, quantum capacity, Holevo information, mutual information, parity charge, or correlation witness. Fix the encoding, source, channel, receiver and energy budget.

**Gate F2: graded quantum reconstruction.** Determine whether a graded composition law with fermionic CAR, observable-even locality and purification can be derived from a precise minimal operational principle. A Clifford geometric grade is not enough.

**Gate F3: common dynamics.** Start with a single full Clifford candidate action and explicitly identify physical fermionic Grassmann/operator content versus bosonic geometric fields. Derive any interaction vertex and a consistent Hamiltonian; do not claim that \(Cl^-\) equals fermions or \(Cl^+\) equals bosons (or vice versa).

**Gate F4: no-signalling and stability.** Show vanishing spacelike commutators of *observables* (microcausality), unitary/positive time evolution and correct characterstic cones. Any claim of instantaneous control is falsified unless an explicit operational channel and causal completion are demonstrated, compatible with known constraints.

**Gate F5: independent tests.** Construct matched fermionic-versus-bosonic quantum networks with the SAME operational resources and predict an independently testable correlation gap. Do not train on and then re-label existing network results as predictions.

## Status verdict

- CAR/CCR occupation identities: established quantum algebra.
- CPTP no-signalling theorem: established exact result, under stated local channel assumptions.
- Relative nonlocal resource separation in specified fermionic quantum network models: published preprint claim; scope-limited and not UBT-specific.
- Fermions as uniquely 'instantaneous information': NOT SUPPORTED.
- Fermions as occupancy-limited distinguishable quantum information and bosonic fields as selected mediators: meaningful **conditional heuristic**.
- Emergence of CAR, CCR, quantum statistics, SM and torsion from one \(\Phi\): OPEN.

Related: [inverse axiom reconstruction](README.md), [Clifford grading vs fermion parity](CLIFFORD_GRADING_VS_FERMION_PARITY_2026_11_10.md), [full Clifford odd gate](FULL_CLIFFORD_ODD_SECTOR.md).
