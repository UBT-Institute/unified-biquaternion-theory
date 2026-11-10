# Information loss, observer-dependent entropy and emergent gravity: an inverse UBT research front

**2026-11-10 | speculative mechanism, anchored in established conditional horizon thermodynamics. No derivation of gravity from UBT.**

## User hypothesis, properly stated

Interactions in a possibly deeper information-bearing state space may cause some correlations to become inaccessible to a particular observer or subsystem; the reduction need not correspond to literal global destruction of information or to a textbook Landauer reset. Could observer-dependent entropy/energy balance then determine emergent geometry, in the spirit of holographic gravity?

This is a sharper claim than "every quaternion multiplication releases heat" (which is false) and "the released heat itself is gravity" (which simply places thermal energy into an already assumed stress tensor). Do not assume a simulation is physically proven; "simulation information loss" is a possible *interpretation* of reduced observability, not an independent physical axiom.

## Established comparators and constraints

- **Verlinde (2011):** heuristic entropic-force argument obtains Newtonian gravity from a holographic screen, postulated entropy gradient, screen temperature and equipartition; it does not by itself prove microscopic origin of those inputs. DOI 10.1007/JHEP04(2011)029, https://arxiv.org/abs/1001.0785.
- **Jacobson (1995):** assuming local causal Rindler horizons, entropy proportional to area, Unruh temperature, and Clausius \(\delta Q=T dS\) at every point, obtain Einstein equations as equation of state. DOI 10.1103/PhysRevLett.75.1260; https://arxiv.org/abs/gr-qc/9504004.
- **Eling, Guedens, Jacobson (2006):** non-equilibrium spacetime thermodynamics \(\delta S=\delta Q/T+d_iS\) is needed in certain curvature-corrected entropies; DOI 10.1103/PhysRevLett.96.121301. **Entropy production is a separate term from energy flux**, not a universal microscopic heating process that produces curvature.
- **Landauer:** thermal resetting an unbiased classical bit has ideal lower bound \(W\ge k_BT\ln2\) under standard conditions; it is **not** a universal conversion factor from lost distinguishability to gravitational energy.
- **Stress-energy:** heat already gravitates via \(T_{\mu\nu}\) in GR. This is distinct from *deriving the metric/connection* from informational constraints.

## Exact obstruction to "loss of reduced information always implies released heat"

For two qubits, start in |00> and apply a reversible entangling unitary (Hadamard on A followed by controlled-NOT) to obtain \(|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2\). The full state remains pure, S(AB)=0, but each local entropy changes from 0 to \(k_B\ln2\). For an ideal degenerate initial/final Hamiltonian, this state change does not in itself enforce any net heat flow into a bath. Therefore neither \(Q=k_BT\Delta S_A\) nor \(\Delta S_A>0\Rightarrow\) nonzero heat or curvature is universal. A selected interaction and thermal environment must be specified.

Pure algebraic rank loss in \(\mathbb C\otimes\mathbb H\simeq M_2(\mathbb C)\) is also not a physical entropy or energy law without selected state space, causal observable map, reservoir and energy budget.

## Candidate operational framework

Use a field / global state \(\Phi\) with observer-indexed accessible algebras \(\mathcal A(O)\) for causal regions \(O\), a physically justified restriction/coarse graining \(E_O\), and quantum states \(\rho_O\). Let \(\sigma_O\) be an admissible entropy-production functional from a specified dynamics, not defined to be always equal to von Neumann entropy increase (nonunital CPTP maps can decrease system entropy). A possible entropy balance is
\[
dS_O = \frac{\delta Q_O}{T_O}+d_i S_O
\]
only under a **derived or independently justified thermodynamic regime**. The stress-energy tensor must obey \(\nabla^\mu T_{\mu\nu}=0\) in the desired GR limit.

Candidate gravity closure: derive area-entropy density and local horizon temperature from the same information/Clifford dynamics, then enforce an appropriate local equilibrium or non-equilibrium identity for *all* local causal horizons; test whether the resulting equation is Einstein's (and in what approximation). Merely postulating \(S=A/(4G\hbar/c^3)\) and Unruh temperature and reproducing Jacobson is a **consistency check**, not a new UBT derivation of either \(G\) or gravity.

## Required proof gates

1. **States and accessibility:** define operational physical state space and local observables *without* postulating Cl(1,3) or the UBT metric. Establish how accessible information is measured, including entangled bosons/fermions and parity constraints.
2. **Loss vs correlation:** construct a concrete unitary/global (or alternative consistent) update and local reduction; quantify correlations, entropy production, mutual information and energy flux separately. Never identify all "lost information" with generated heat.
3. **Emergent geometry:** derive a covariant, Lorentz-compatible metric/tetrad and any torsion from \(\Phi\), not import GR by fiat. Show local positivity/hyperbolicity and proper causal horizons.
4. **Horizon entropy:** derive \(\delta S/\delta A\) (including coefficient and universality) from state counting or entanglement. Reproducing Bekenstein-Hawking area law as an input does not qualify.
5. **Thermal relation:** derive Unruh temperature, equilibrium/non-equilibrium entropy balance and gravitational coupling \(G\) from the microscopic information dynamics. Distinguish reversible Clausius heat flow from dissipative entropy production \(d_iS\).
6. **Einstein dynamics:** obtain tensor field equation for arbitrary matter flows with Bianchi compatibility, Newtonian limit, lensing, gravitational waves, vacuum solutions and correct tensor-mode count; test deviations and ghost/causal stability.
7. **Inverse discrimination:** demonstrate which extra assumptions are necessary and whether a generic complex Hilbert-space or M_n(C) theory duplicates the result — no post-hoc identification of the chosen algebra with a unique proof.

## Immediate mathematically checkable counterexample

A Bell entangling circuit gives local entropy increase without global entropy production; compute exact reduced states and entropy and verify global norm/purity, as companion test. This excludes a naïve universal proportionality \(Q_{\rm generated}=k_BT\Delta S_{\rm local}\).

## Status

- [STANDARD] Jacobson conditional Einstein equation-of-state and Verlinde entropic-force construction.
- [EXACT] local entropy increase under globally unitary entanglement without necessary reservoir heat.
- [OPEN] microscopic horizon entropy/area coefficient, derived \(G\), selected invariant UBT action and total composite Hessian.
- [SPECULATIVE] that observer-dependent information loss is the microscopic mechanism of spacetime emergence.

See [BIQUATERNION_INFORMATION_LOSS_LANDAUER_2026_11_10.md](BIQUATERNION_INFORMATION_LOSS_LANDAUER_2026_11_10.md), [inverse programme](README.md).
