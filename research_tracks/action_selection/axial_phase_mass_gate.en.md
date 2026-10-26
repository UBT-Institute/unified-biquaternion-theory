<!-- BILINGUAL-UNIT: axial_phase_mass_gate -->
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


# Axial phase gate for Dirac mass in a single biquaternion

**Exact conditional linear-algebra theorem (2026-10-25).** No claim that the UBT physical Hamiltonian has been selected.

Use the real-linear Weyl-dual map F from merged PR #724: for Theta=[psi,chi], set Psi=(psi,epsilon chi*). A central transformation Theta -> exp(i alpha) Theta induces Psi -> exp(i alpha Gamma) Psi, Gamma=diag(I2,-I2). Thus the phase acts **axially** on this derived Dirac carrier, not as the usual common electric phase. This statement is specific to F and its chosen right-column decomposition.

For a flat test Dirac Hamiltonian (c=hbar=1)
```
H(p)=[[-sigma.p, m I2],[m I2,+sigma.p]].
```
Direct multiplication gives
```
[H,Gamma]=2m [[0,-I2],[+I2,0]].
```
So the momentum-dependent kinetic part commutes with Gamma, while the ordinary real constant Dirac mass does not (unless m=0). If the induced axial U(1) is a **true exact continuous symmetry of the full dynamics**, this candidate bare mass is forbidden; if the central phase is instead a broken symmetry, a redundancy with different action, or an inapplicable transformation of the physical state space, the inference does not follow.

This does **not** derive a Higgs field, spontaneous breaking, masses or couplings in UBT. It does not establish that the locked composite metric is invariant under an arbitrary local or global central phase: that is an independent representation/metric compatibility gate, cf. draft #701. Classical massless axial symmetry may also suffer a quantum anomaly after coupling to gauge/gravity sectors; any exact quantum-symmetry claim requires anomaly calculations.

Next decision: determine whether the canonical symmetry action of Theta actually preserves the central metric, constraints, the physical presymplectic form and composite connection; then classify invariant first-order symbols. Do not add a mass term unless the symmetry selection supports it.

Reproducer: research_tracks/action_selection/tests/test_axial_phase_mass_gate.py.
