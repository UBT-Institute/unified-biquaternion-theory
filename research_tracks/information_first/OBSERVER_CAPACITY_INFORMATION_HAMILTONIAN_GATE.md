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

# Observer complexity and finite information capacity: operational Hamiltonian equivalence

**2026-10-27. Additional testable dimension of causal shared reality: the observer need not extract all causally incoming information.** Connects `CAUSAL_ACCESS_SHARED_REALITY_HAMILTONIAN_GATE.md`, `OBSERVER_DEPENDENT_CAUSAL_HAMILTONIANS.md`, `SHARED_REALITY_PRINCIPLE.md`, and the existing information-first selector.

## 1. Observer capacity is not just distance or velocity

An operational observer O is a physical information-processing device. Specify (i) causally reachable algebra A(D_O), (ii) allowed preparations, POVMs, interactions, and processing protocols P_O (with physical energy, timing, and computational budget), (iii) finite accessible output memory R_O, and (iv) proper-time calibration tau_O. Observer complexity means *physical operational capabilities*, not human consciousness. A sensor or finite CAR register is an equally valid observer. An observer can be near a source yet unable to infer its parameter because its measurement basis/noise/processing loses the relevant information; another at the same event with a different detector can distinguish it.

A final record R with at most M distinguishable labels obeys
  I(X:R) <= log_2(M)
for a CLASSICAL preparation label X (mutual information in bits), and for a quantum ensemble E={(p_x,rho_x)} with arbitrary POVM and parameter-independent postprocessing it obeys the Holevo bound
  I(X:R) <= chi(E)=S(sum_x p_x rho_x)-sum_x p_x S(rho_x).
Thus I(X:R)<=min(chi(E),log_2 M) per single constrained record, with causally accessible states substituted into E. This is NOT a universal cumulative bound across arbitrarily many repeated experiments, nor does raw stored-bit count quantify computational cost without a stated protocol. Restricted measurement families generally lower accessible information below chi.

For a parametric model and a parameter-INDEPENDENT observation channel, classical Fisher information satisfies the data-processing inequality F_after(theta)<=F_before(theta) under regularity conditions. This is a statement about precision of inference, not a law selecting the physical theta.

## 2. Exact two-observer / two-Hamiltonian diagnostic

Take a qubit in the initial |+x> state, with family H_mu= hbar mu sigma_z, where mu=mc²/hbar. Then
  <sigma_z>(t)=0,
  <sigma_x>(t)=cos(2mu t).
Observer O_z permitted only sigma_z readout on this preparation sees p(z=±1)=1/2 for all mu and t. Its Fisher information about mu is **exactly zero**. Observer O_x permitted sigma_x readout sees
  p_x(+|mu,t)=cos²(mu t),
hence F_mu=4t² away from singular probability points. These observers can be co-located and have the SAME causal past; their inferential difference comes from measurement capability, not different fundamental laws or different objective state histories.

Now add an independent binary symmetric readout channel (flip probability epsilon, 0<=epsilon<=1/2):
  p_noisy=epsilon+(1-2epsilon)cos²(mu t).
At mu t=pi/4 (balanced outcome), the exact noisy Fisher information becomes
  F_mu^noisy=4t²(1-2epsilon)².
In terms of physical mass m it is F_m^noisy=4c⁴t²(1-2epsilon)²/hbar². At epsilon=0 it matches ideal X detection; at epsilon=1/2 it vanishes. This is a fully explicit information-capacity/measurement-quality effect compatible with the fixed microscopic Hamiltonian H_mu.

Define the **observer-specific empirical equivalence relation**
  H ~_O H' iff P_H(r|p,t)=P_H'(r|p,t)
for every preparation/measurement/time protocol p in P_O (and appropriate causal transport). Under O_z with the fixed |+x> preparation, every H_mu lies in a single equivalence class, while O_x distinguishes generic mu. Therefore different observers can assign different effective model classes / reconstruct different generators FROM LIMITED DATA; it would be a mistake to assert they have literally different fundamental Hamiltonians. In general the restriction of a global unitary evolution to A(D_O) need not be a closed unitary evolution, so an observer may have a quantum channel rather than any autonomous Hermitian H_O.

## 3. Shared reality with capability-aware comparison

The shared-reality requirement is equality of transported predictions for the **overlap of causally accessible, actually performable experimental protocols**, with compatible extension of local states where possible. High-capacity observations refine, rather than contradict, low-capacity observations when marginalization/coarse-graining maps are consistent. If P_small⊂P_large and both sample a common state/evolution, observational equivalence classes obey
  [H]_(P_large) subseteq [H]_(P_small)
on the same admissible model family. Strong capabilities can reveal distinctions otherwise hidden.

A separate issue is observer-dependent time: inertial observers with relative velocity measure H_v=gamma(H-vP), while accelerated observers have different proper-time/region-dependent generators, independently of measurement fidelity. These proper-time generators should not be confused with a reconstruction from inaccessible information or a state-dependent modular K_D=-log rho_D.

## 4. What would actually select one UBT Hamiltonian?

One could attempt a physically motivated **information-optimal dynamics** criterion relative to finite observer resources, with a concrete causal quantum channel E_O[Theta], admissible measurement resources and an independently derived optimization principle. But maximizing measured information without a budget/regularizer can be arbitrary, and selecting the observing instrument is NOT the same as selecting microscopic field dynamics. The existing no-selection counterexample for invariant masses survives any mere causal compatibility / limited-capability postulate.

To make this useful for UBT:
1. Construct observer-accessible algebras and CAR measurement channels from the actual Theta-derived composite tetrad and real causal diamonds.
2. Supply physical resource limits from the microscopic Theta theory (time/energy/memory/coupling), rather than invent arbitrary entropy weights.
3. Compute how the same candidate one-Theta dynamics appears in co-located, near, boosted, and horizon-limited observers, and show empirical equivalence class refinement for increasing capacities.
4. Ask whether the measured relative entropy or modular energy responds to physical changes in the Theta-derived geometry; verify the full symplectic/Dirac constraints and see whether invariant Hamiltonian deformations survive.
5. Only declare unique H if a new independently justified physical principle excludes the residual family. Maintain `canonical/ACTION.en.md` status `DEFINED_FAMILY_NOT_FINALIZED`.

This supplies a concrete, falsifiable **capacity-aware** shared-reality framework without treating finite information or observer intelligence as a magical source of quantum measurement outcomes.

Local algebraic regression: `tests/test_information_observer_capacity_selector.py`.

External grounding: Holevo accessible-information bound https://lim.physics.ucdavis.edu/teaching/files/qi-notes-partiii.pdf ; local-objectivity/accessible-information discussion https://www.nist.gov/publications/amplification-inference-and-manifestation-objective-classical-information ; Fisher-information data-processing overview https://www.tara.tcd.ie/tara8/server/api/core/bitstreams/8587b815-7d7f-47c2-9461-4afbb338b2e6/content .
