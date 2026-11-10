# Reverse-engineering UBT: exchange, statistics, and entanglement

**2026-11-10 | exact conditional algebra and testable two-mode example | fundamental selection OPEN.**

## Objective, not assumed conclusions

Try to derive why physically composable information degrees of freedom have Bose and Fermi sectors, and whether the selected geometry is even biquaternion Cl+(1,3), full real Cl(1,3), or something else. **Do not assume UBT or Clifford algebra in the premises.** Entanglement is a correlation resource shared by both bosonic and fermionic systems and is **not** instantaneous signal transfer. No theorem says that "fermions contain instantaneous information" or that bosons are only force mediators.

## Minimal exchange calculation and exact scope

Let P12 exchange two **identical** excitations, with P12²=I. For a sector in which exchange acts as a scalar phase on the ray, P12|psi>=eta|psi>, unitarity gives |eta|=1 and the involution yields eta²=1; hence eta=+1 or -1.

+1 is the symmetric Bose sector; -1 is the antisymmetric Fermi sector.

**Assumption alert:** this is only a one-dimensional representation of the permutation exchange (and requires identifying the physical double exchange with identity for the chosen model). Unitarity and composability **do not force the representation to be one-dimensional**. Higher-dimensional irreducible S_n representations/parastatistics exist algebraically. In 2+1D, exchanges use the braid group; Abelian anyonic phases can be non ±1 and non-Abelian braid statistics exist. In 3+1D, under conventional local relativistic QFT and point-particle assumptions, the familiar spin-statistics connection requires locality, a positive-energy vacuum, positive physical state space and other standard theorem premises. The elementary Z2 step **does not by itself derive spin-statistics, Clifford geometry, or UBT**.

## Standard two-input/two-output comparator: boson bunching vs fermion antibunching

Consider two identical particles in input modes a and b of an ideal balanced coherent beamsplitter. For creation operators choose
\[
a^\dagger=(c^\dagger+d^\dagger)/\sqrt2,\qquad
b^\dagger=(c^\dagger-d^\dagger)/\sqrt2.
\]
Bosonic commuting creation operators give, on the vacuum,
\[
a^\dagger b^\dagger|0\rangle=\frac12[(c^\dagger)^2-(d^\dagger)^2]|0\rangle
=\frac{|2,0\rangle-|0,2\rangle}{\sqrt2}.
\]
Thus output occupation probabilities P(20)=1/2, P(11)=0, P(02)=1/2.

For fermionic creation operators with {c†,d†}=0 and (c†)²=(d†)²=0,
\[
a^\dagger b^\dagger|0\rangle=-c^\dagger d^\dagger|0\rangle
\]
under this mode convention. Thus P(11)=1, P(20)=P(02)=0. Physically such a beamsplitter for fermions may be realized by appropriate coherent two-mode mixing (e.g. electronic interferometry), not necessarily the same hardware as optical photons. Assumes identical internal states, negligible interactions, single occupancy of each input and perfect mode overlap. Nonidentical/distinguishable particles give different output probabilities.

This comparator is well-established quantum statistical interference, **not a new UBT prediction**. Its value is to give a concrete target any proposed information/Clifford reconstruction must recover.

## Entanglement does not distinguish the sectors

Encode Alice's logical qubit using two local modes with precisely one particle, and analogously Bob's qubit. Their logical Bell state (|00>+|11>)/sqrt2 has one ebit of mode/operational entanglement, and CHSH=2sqrt2 for the usual logical Pauli measurements. It can be constructed in both bosonic and fermionic mode algebras, with **locally parity-even number-conserving operations** for fermions. Important: a single delocalized fermion and mode entanglement require careful superselection handling; the two-party fixed-local-occupation example avoids the simplest parity obstacle. Entanglement alone cannot select exchange sign.

## Clifford relations and their limits

Fermion creation/annihilation CAR can be rearranged into Majorana operators satisfying a Euclidean Clifford relation of a *mode space*; this does not demonstrate the necessity of Lorentzian spacetime Cl(1,3). Bosonic CCR cannot be faithfully represented by finite matrices; hence neither complete Fock algebra is supplied by choosing a finite geometric Clifford representation alone. An additional field quantization, compositional construction, or derivation is necessary.

## Reverse selection criteria for genuine UBT progress

**E1:** derive which physical equivalence classes of permutations/exchanges must be considered from operational indistinguishability and composition, without inserting Bose/Fermi as axioms.

**E2:** state a separate locality/causal positivity axiom sufficient for the spin-statistics link (not merely assuming 2pi-sign equals exchange sign).

**E3:** implement exact local observable algebra including fermion parity superselection and bosonic symplectic CCR, *then* compare their spinor vs tensor representations.

**E4:** only then ask whether a single principle necessarily picks C⊗H, Cl(1,3), a Clifford module, or neither. Distinguish field-value algebra from creation/annihilation operator algebra.

**E5:** derive a single UBT action and use it to calculate independently constrained physical spectra/interactions, not postselect standard QFT outputs.

### Claims ledger

- **PROVED conditional:** scalar exchange representation + exchange involution gives eta=±1.
- **PROVED finite toy comparator:** ideal balanced beamsplitter P(11)=0 for bosons and 1 for fermions.
- **ESTABLISHED QFT:** spin-statistics correspondence under additional assumptions (not proved here).
- **OPEN:** derivation of scalar exchange-representation assumption, emergence of both statistics, unique fundamental Clifford geometry, and a fully selected UBT dynamics.
- **REJECT:** entanglement as exclusive fermionic feature; entanglement as FTL signaling.

Related: [entanglement and statistical inverse test](ENTANGLEMENT_SPIN_STATISTICS_INVERSE_2026_11_10.md), [fermion information vs boson interactions](FERMION_INFORMATION_BOSON_INTERACTION_2026_11_10.md), [inverse research programme](README.md).
