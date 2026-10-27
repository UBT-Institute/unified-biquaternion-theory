<!-- BILINGUAL-UNIT: shared-reality-first-principles-restart -->
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

# Shared reality: restart from first principles and test Hamiltonian selection

**2026-10-27 — experimental research track, not a UBT axiom.** Preservation/merge: #798 information/shared-reality proposal and #796 algebraic connection theorem were merged into master before this continuation. #799 (33 changed files, conditional extended-field symplectic split) and #786 (merge conflicts) were intentionally NOT force-merged; all remain accessible in GitHub PR history.

## 1. Operational primitive (weak version SR0)

An observer O has a measurable-record algebra and a protocol. The admissible transformations g act on field configurations, protocols and record labels. SR0 requires equivariance of every operational prediction: transformed experiments yield properly transformed probability distributions, with invariant scalar summaries. In deterministic finite-dimensional models, this means if Phi_t is evolution and G_g transforms observers then Phi_t G_g = G_g Phi_t. This is operational covariance, not equality of components.

No new field, law of time evolution, entropy measure or Hamiltonian is assumed in SR0.

## 2. Direct nonselection test (an actual application)

Use a two-dimensional canonical symplectic diagnostic (q1,q2,p1,p2), with SO(2) observer rotations acting simultaneously on q and p. Define I=q1²+q2²,
H_0 = (p1²+p2²+I)/2,
H_lambda = H_0 + lambda I².

Both are invariant under SO(2). Consequently their Hamiltonian flows commute with the observer transformations and obey SR0. Nevertheless they are inequivalent evolutions for nonzero lambda:
dot(p)_lambda - dot(p)_0 = -4 lambda I q.
The rotationally invariant relational observable Q=q·p changes according to
dot(Q)_lambda - dot(Q)_0 = -4 lambda I².

This difference is itself observer invariant. Thus BOTH Hamiltonians are observer-consistent even though they yield measurably different predictions for the same initial relational data. This is a constructive counterexample to **SR0 uniquely selects H**. The model is not UBT or a representation of its full Lorentz/psi constraints. It proves only that an SR principle reducible to ordinary equivariance does not logically provide unique dynamics; analogous invariant deformations are already documented for UBT in hamiltonian_first_foundations.en.md.

## 3. Strong candidate SR1: relational overlap consistency (NOT yet sufficient)

For observers a,b with operational channels C_a, C_b applied to the same fundamental Theta history, introduce an overlap/comparison channel K_ab and require
K_ab(C_a(Theta)) = C_b(Theta) on shared observables,
K_bc ∘ K_ab = K_ac on triple overlaps,
and K_ab transports time-evolved histories consistently.

This is a precisely stated candidate *consistency condition* once channels, domains, probabilities and dynamics are separately defined. However if C_a and K_ab are simply invertible coordinate changes, SR1 reduces to SR0 and cannot select H. Even for non-invertible operational channels, compatibility alone can be satisfied by many dynamics. We must show a derived restriction of admissible generators, not assume one.

## 4. Stronger testable selector hypothesis SR2 (requires genuine input)

Choose independently justified observer-accessible distributions p_a(record | Theta, protocol), measures, reconstruction compatibility, and a concrete information functional J[Theta], with physical-time and complex-time prescriptions. Demand that observer overlaps obey SR1 *and* identify a unique evolution by a falsifiable information law (e.g. specified conserved information current or an explicitly defined variational objective). THEN calculate which allowed invariant deformations H_lambda violate this law.

Until a source for J, the measure, channels and variational class is derived, SR2 is an **unselected family of extra principles**, not proof of unique S_UBT or H_UBT. Fisher positivity alone is not bounded physical Hamiltonian energy; Maxwell/Proca transversality is not entailed by observer agreement.

## 5. Physics acceptance gate

To promote SR1/SR2 beyond an interpretation, explicitly prove that it excludes H_lambda for lambda ≠0 (or explains residual parameters) *without assuming the desired equations*, while preserving Lorentz covariance and composite Theta tetrad with nonzero two-sided connections. Then derive torsion selection, full Euler–Lagrange chain rule, symplectic/Dirac reduction, positive Hamiltonian, massless spin-2 propagation and eventually particle spectrum. A failed uniqueness test means SR does not deserve canonical axiom status.

**Decision as of this calculation:** SR0 nonselection PROVED by counterexample. SR1/SR2 usefulness OPEN. Do not add an axiom or assert a fundamental action.

Reproducer: research_tracks/fundamental_dynamics/tests/test_shared_reality_selection_counterexample.py (local SymPy unittest: 3 tests passed 2026-10-27).

Verification scope: the tests check weak operational covariance and the displayed counterexample; they do not select UBT dynamics. LEAN-PENDING: this note is not formalized and Lean/Lake is unavailable locally.
