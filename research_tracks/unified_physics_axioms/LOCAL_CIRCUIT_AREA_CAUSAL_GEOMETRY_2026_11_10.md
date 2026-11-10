# Local information dynamics: entanglement area bound does not derive causal geometry

**2026-11-10 | Proven conditional finite-circuit bound; UBT fundamental geometry and action OPEN.**

## Setup and proof

Let a finite graph G=(V,E) represent q-dimensional quantum degrees at vertices, and choose a region A. Assume an initially factorized pure state across the A/complement partition, and a depth-d circuit of unitary two-site gates, each gate acting along an edge in E. At most d|∂E A| gates straddle the cut. Local gates entirely within A or its complement do not change Schmidt rank across the cut. A gate across two q-dimensional degrees admits an operator Schmidt decomposition of at most q² products; acting on a state with Schmidt rank r increases rank at most to q²r. Thus
\[
r_A^{\rm out}\le q^{2d|\partial_E A|},\qquad
S_A\le k_B\ln r_A^{\rm out}\le 2k_B\,d\,|\partial_E A|\ln q.
\]
For a nearest-neighbor L×L×L cubic region, |\partial_E A|=6L², so
\[
S_A\le 12k_B d L^2\ln q.
\]
At fixed depth independent of L, this is a rigorous *area-law upper bound*. It is not an entropy-area equality. If depth grows with L or dynamics has long-range interactions, it does not imply universal area scaling. Most importantly: this construction **assumes a locality graph**; that graph cannot be declared derived.

## Exact counterexample: mutual information is not distance or a signal channel

A bipartite Bell state (|00>+|11>)/sqrt2 has I(A:B)=2 ln 2, while its reduced states are each I/2. Pick H_int=0, so there is no coupling between A and B. The entanglement nevertheless exists and is stationary if local terms also vanish. Therefore state-dependent correlation is not sufficient to infer interaction adjacency, causal signal time, or spatial metric. In particular MI alone cannot fix the dimensions, Lorentzian signature, or absolute scale of emergent geometry.

Even high MI between two subsystems is consistent with large separation, and a large local interaction is compatible with a product state at a specific time. A geometric distance reconstructed solely from MI is a *model-dependent ansatz*, requiring independently justified locality, state family and dynamics.

## Consequence for an information-first derivation of UBT

A plausible necessary bundle of principles is:
(i) operational states, indistinguishability and composition;
(ii) admissible entanglement and physically accessible observables;
(iii) reversible or consistently open-system dynamics;
(iv) a finite causal influence relation or microcausal local algebra;
(v) positive energies / stable observables.

These do not yet select Cl(1,3), C⊗H, a unique action, dimension 3+1 or gravity. In fact the theorem above works for generic local qudit systems, so it provides no UBT uniqueness evidence.

A route toward a noncircular geometry derivation would start with **operational influence**, e.g. norm of a commutator between later local observables and earlier operations; derive a characteristic cone or Lieb–Robinson type bound from an explicitly selected microscopic dynamics. An LR bound gives an effective graph information-propagation speed but alone does not yield exact relativistic Lorentz symmetry. Next derive effective distances, signature and universal low-energy speed; only afterward define causal horizons. Then derive the area-law coefficient and stress-energy flux from the *same* dynamics and test a Jacobson-type thermodynamic closure. A pre-existing Lorentzian metric/area-law coefficient must not be silently imported.

## Verification status

Four companion finite-model tests ran locally: cubic boundary count, symbolic gate-rank entropy bound, Bell reduced state and mutual information, and Bell entanglement at zero coupling. They verify special algebraic checks, NOT the general theorem by exhaustive enumeration and NOT UBT or Einstein dynamics.

## Next falsifiable gates

G1: derive graph from allowed microscopic couplings without presupposing spacetime geometry.
G2: establish observable influence bounds for entangled bosonic/fermionic states, respecting parity and no-signalling.
G3: exhibit universal long-distance Lorentzian cones independently of state-dependent entanglement.
G4: obtain a horizon entropy *equality* and universal coefficient, not just an area upper bound.
G5: derive a physical gravitational action/equation and determine G, tensor modes and torsion from a common UBT construction; distinguish from generic complex-qudit lattice models.

Related:
- [Entanglement boundary area model](ENTANGLEMENT_BOUNDARY_AREA_G_SELECTION_2026_11_10.md)
- [Conditional horizon gravity](LOCAL_HORIZON_INFORMATION_EINSTEIN_CLOSURE_2026_11_10.md)
