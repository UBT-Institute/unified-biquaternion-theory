# Central-phase selection gate from the locked sharp metric

**Exact conditional algebraic theorem (2026-10-25).** This is a physical correction to a possible over-reading of draft #731, not a derived fundamental Hamiltonian. A related phase/metric obstruction was already investigated in #701; do not claim novelty over that track.

Locked Axiom C defines E_mu=N0^(-1/2) D_mu Theta and the central metric
\[
g_{\mu\nu}1=\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu).
\]
Sharp is quaternion conjugation, **not** conjugation of the commuting complex unit. Hence for a central phase z=e^{iα} and the **conditional covariance law E_mu→zE_mu**,
\[
\boxed{g_{\mu\nu}\longmapsto z^2g_{\mu\nu}.}
\]
For a nondegenerate real metric to remain pointwise *unchanged*, z²=1, so z∈{+1,-1}; full continuous central U(1) cannot act by simple multiplication on E while preserving the locked metric. Generic z also fails to preserve the real Lorentz tetrad slice W_L. This is algebraic and holds for every pair E_mu,E_nu, not just the flat example.

The assumption about E is satisfied for **global constant** central phase of Theta whenever the specified D_mu is complex-linear and transforms equivariantly without compensating connection changes. A local Theta phase with derivatives of α is not covered absent a specified D transformation. One could instead construct a distinct symmetry with compensating field/connection transformations or a phase neutral induced E, but that mechanism must be derived consistently with the no-new-independent-field rule and the fixed central metric.

**Consequences for Hamiltonian-first UBT:** the axial-phase mass commutator theorem of #731 remains a correct matrix identity for the chosen real-linear Weyl map, but its application as a **fundamental exact U(1) selector forbidding Dirac mass is not justified** on the canonical Lorentz branch. The physical phase symmetry must be established before the associated charge constraint and Hamiltonian selection; no bare phase-U(1) first-class constraint may be assumed.

This result is independent of selecting a symplectic structure and does not specify the correct H. Next concrete gate: determine the actual induced transformation of the composite two-sided D_mu Theta, then compute constraint brackets in the physical Lorentz slice with that transformation—not with a silently assumed central U(1).

Exact simple symbolic check: research_tracks/action_selection/tests/test_phase_sharp_metric_gate.py.
