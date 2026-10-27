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

# One invariant dynamics, many observer time generators

**2026-10-27. Refinement of causal shared reality in direct response to the observer-Hamiltonian suggestion.** Cross-references: `CAUSAL_ACCESS_SHARED_REALITY_HAMILTONIAN_GATE.md`, `OVERLAPPING_ALGEBRAS_HAMILTONIAN_GATE.md`, `RINDLER_MODULAR_TIME_CALIBRATION.md`, `research_tracks/causality/einstein_causal_principle.en.md`.

## 1. Distinguish global physics from local observer time

A generally covariant underlying UBT candidate action S[Theta,aux] (currently NOT selected) can admit distinct observer-specific generators H_O, tied to their proper-time parameter tau_O and causal accessible algebra A(D_O). These must be **compatible** on overlaps; they need not literally be equal as untransformed operators. In gravity, a local lapse/shift Hamiltonian may be a constraint generator plus gravitational boundary/edge terms; an observer-local modular Hamiltonian K_O=-log rho_(D_O) is different from a mechanical proper-time H_O unless a modular/thermal relation is independently established.

A physical event outside the observer's finite past light cone is not necessarily behind an event horizon. The proper domains are covariant causal diamonds/worldline pasts; Rindler observers and black hole observers may have genuine horizons. Even inaccessible regions can remain quantum-entangled with accessible ones, without allowing superluminal messaging.

## 2. Exact flat relativistic example, no arbitrary extra law

In 1+1 Minkowski with conserved H and P_x, the generator measured in proper-time units by an inertial observer moving at speed v, relative to the original time/space translations, is (with the usual sign convention)
  H_v=gamma_v (H-v P_x), gamma_v=(1-v²/c²)^(-1/2).
At v=0 it reduces to H. Distinct velocities change the generator; for a smooth finite-energy/momentum-bounded domain,
  H_(v+dv)-H_v ≈ gamma_v³(v/c²)(H-vP_x) dv -gamma_v P_x dv,
i.e. first-order continuous variation. The exact derivative simplifies to
  dH_v/dv=gamma_v³[(v/c²)H-P_x].
This derivative is a statement on a COMMON invariant domain; the unbounded operators need not be close in operator norm without a spectral cutoff.

Two inertial observers separated by an arbitrarily large spatial translation but with the same four-velocity can use the SAME H, because a translation-invariant Hamiltonian commutes with spatial translations. Thus spatial distance alone does not force different H. The underlying relativistic mass shell E²-c²p²=m²c⁴ is invariant, while observers measure different E.

## 3. Exact accelerated observer example with horizons

Use c=hbar=1 on right Rindler wedge x>|t|: t=rho sinh(eta), x=rho cosh(eta). Proper time for the observer rho=rho0 is tau=rho0 eta; if B is the boost generator in eta, its proper-time generator is
  H_(rho0)=B/rho0.
Two nearby rho's have different local energy redshift even though they share a *single wedge algebra* and horizon. Under the appropriate Lorentz-invariant-vacuum/QFT assumptions, K_wedge=2pi B+constant; thus
  H_(rho0)=(K_wedge-constant)/(2pi rho0).
This does NOT identify the state-dependent modular generator K of arbitrary causal diamonds with universal fundamental H. The observer dependence is calibration, not physically unrelated fundamental dynamics.

## 4. Strengthened shared reality as a dynamical gluing rule

Let observer O carry a causal algebra A_O, local proper-time derivation delta_O, and compatible record/state restrictions on overlap intersections. If two worldlines/frames share events, define a comparison map T_(O->O') transporting operators and their time parameters. Then require equality of the *transported physical predictions* and derivations where comparison is operationally meaningful, allowing lapse/boost factors:
  T_(O->O') (delta_O(A)) ≡ delta_O' (T_(O->O')A)
after correct proper-time reparametrization/coordinate transport.
This is a **conditional compatibility equation**, and needs to be formulated through the actual spacetime automorphism/connection to avoid requiring the impossible equality of distinct partial-time derivatives for different trajectories. A more invariant target is the common covariant field equations and their restriction to each causal diamond.

There is NO theorem that information loss across a horizon alone selects a unique generator: the mass counterexample in CAUSAL_ACCESS_SHARED_REALITY_HAMILTONIAN_GATE.md remains. What might be new in UBT is to derive the geometrical comparison transport, modular normalization and the common canonical generator from the *same Theta symplectic structure*.

## 5. Acceptance test for the one-Theta Hamiltonian

1. Build the local observer tetrads and physical causal diamonds from nondegenerate composite E(Theta,omega,K,w).
2. Compute local physical charges/energy generators and compare near observers, moving observers and horizon-separated algebras. Never simply insert a separate observer-dependent arbitrary Hamiltonian.
3. Compute restrictions of a shared CAR state, local modular generators where meaningful, their overlap/transport equations, and the causal propagation test at light speed c.
4. Derive the physical symplectic form and constrained Hamiltonian from one action, including boundary/edge contributions. Test Einstein+Dirac/FLRW limit and distinguish an observer proper-time H from the ADM Hamiltonian constraint.
5. Test nonuniqueness under invariant potential/mass deformations before asserting shared reality uniquely fixes coefficients.

**Status:** observer-dependent Hamiltonians are already explained by SR/GR transformations and causal restriction, without selecting a new universal microscopic Hamiltonian; the UBT-specific unification mechanism remains open.

Regression: `tests/test_information_observer_hamiltonian_covariance.py`.
