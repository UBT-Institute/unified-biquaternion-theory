# Inverse UBT: boundary Bell pairs, area law, and the conditional value of G

**2026-11-10 | Exact finite-model result, NOT a derivation of GR or microscopic UBT.**

## Why this test

The previous local-horizon thermodynamic derivation requires the microscopic entropy-area density eta before it can produce a value for Newton G. Can informational composition and locality select an area law rather than a volume law without presupposing gravity? Distinguish *one* explicit locality-motivated construction from a universal selection theorem.

## Exact cubic-network construction

Let a region consist of L³ cubic sites of edge length ell, with one qubit Bell pair per nearest-neighbor edge crossing the boundary into the complement. Count outward bonds along all six face directions: N_cut=6 L². Assume all these Bell pairs are independent, crossing a physical boundary of area A=6(L ell)². Tracing out the exterior member of each pair yields maximally mixed interior boundary qubits, hence
\[
S_A/k_B=N_{\mathrm{cut}}\ln2=6L^2\ln2=\frac{\ln2}{\ell^2} A .
\]
This is exact **in the chosen product-of-Bell-pairs state** with this cubic lattice and normalization; it demonstrates why local boundary correlations CAN produce area scaling. For n independent crossing pairs per microscopic link, or qudit local dimension d, eta=n ln(d)/ell². None of n,d,ell is selected by general quantum information or the Clifford algebra.

### Counterexample: volume law within the same Hilbert-space composition

Entangle each of the L³ interior qubits with a distinct exterior qubit. The state is again a product of maximally entangled pairs, but the pairings may be spatially long range. Its interior entropy is
\[
S_A/k_B=L^3\ln2,
\]
a volume law. This is a legitimate global pure quantum state, though not necessarily a low-energy local-ground-state configuration. Therefore *composability and the existence of entanglement alone do not force an area law*. Selecting particular low-energy vacua, finite-range correlations, appropriate local Hamiltonians and scale dependence is extra physical input. Not all local QFT states obey pure area laws; divergent UV entropy coefficients and subleading terms need regularization.

## Conditional Newton coupling (natural units)

In natural units \(\hbar=c=k_B=1\), the Jacobson comparator assumes \(S_H=\eta A\) and obtains \(8\pi G=2\pi/\eta\). If and only if we further **identify the toy lattice boundary Bell-pair entropy** with the universal *gravitational horizon entropy density* and set one crossing qubit pair per unit cell,
\[
\eta=\frac{\ln2}{\ell^2},\qquad
G_{\mathrm{eff}}=\frac{\ell^2}{4\ln2}.
\]
For n pairs of local dimension d per boundary link, \(G_{\mathrm{eff}}=\ell^2/[4n\ln d]\). This is a **conditional dimensional reparameterization**, NOT a novel prediction of G. The microscopic length ell and precise mapping from lattice cut to physical causal horizon are unselected. The actual horizon entropy law, gravitational edge modes, regulator dependence and renormalization of G are not supplied by the qubit calculation.

## More stringent published comparator

Jacobson's *Entanglement Equilibrium and the Einstein Equation* (PRL 116, 201101, 2016, https://doi.org/10.1103/PhysRevLett.116.201101) obtains a conditional relation between local entanglement equilibrium in small geodesic balls at fixed volume and the Einstein equation for first-order variations of conformal quantum matter, with a qualification for nonconformal matter. This is NOT equivalent to saying a Bell-pair network already produces spacetime gravity. The state/geometry variation, vacuum modular energy and entropy-area piece must be derived consistently in the selected microscopic UBT.

Further area-law discussion and counterexamples: https://www.nature.com/articles/s42005-025-02125-x ; https://www.nature.com/articles/s41586-024-07325-z .

## Selection gates (no circularity)

- **A1:** derive an operational causal adjacency/network and an effective spatial geometry from pregeometric information axioms; otherwise ell and boundary area are assumed.
- **A2:** select a vacuum/low-energy state or dynamics with area-dominated entanglement without postulating Bell-pair crossing state.
- **A3:** identify physical horizon algebra and count edge/entanglement degrees; regulate and renormalize eta, including bosonic and fermionic sectors and constraints.
- **A4:** obtain universal eta and microscopic length/coupling without fitting measured G.
- **A5:** derive local temperature, energy flux and an Einstein-type field equation while preserving Bianchi identities and any UBT torsion/complex metric structure.
- **A6:** check new independent observables and distinguish generic complex qubit networks from specific C⊗H / Cl(1,3) UBT dynamics.

## Verdict

**PROVED, restricted:** area-law coefficient for independent Bell bonds across a cubic boundary.
**PROVED, restricted:** admissible volume-law state under alternate long-range Bell pairing.
**CONDITIONAL:** G=ell²/(4 ln2) if toy network eta is assumed to equal universal gravitational horizon density in natural units.
**OPEN:** microscopic geometry, universal horizon entropy, gravitational dynamics and any unique UBT realization.
