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

# Hilbert energy versus canonical Theta Hamiltonian on a fixed ADM background

**C-tier conditional exact identity; 2026-10-23. Not the complete composite UBT source reduction or fundamental action.**

## Scope
Use the *already defined* fixed-background Theta family in [canonical_family_hamiltonian_bridge.en.md](canonical_family_hamiltonian_bridge.en.md), with eight real q^A, symmetric constant nondegenerate K_AB, coefficient c, fixed ADM N>0,N^i,h_ij, and metric-independent prescribed linear connection D_t q=dot q+Omega_0 q, D_i q. No composite variation of g[DTheta] is attempted. The externally specified connection must be held fixed under the Hilbert metric variation. Ignore boundary flux or impose appropriate compact-support/boundary data.

Write V^A=(D_t q)^A-N^i(D_i q)^A and w_i^A=D_iq^A. The Lagrangian is
\[
\mathcal L=N\sqrt h\left[\frac c{2N^2}K_{AB}V^AV^B-\frac c2h^{ij}K_{AB}w_i^Aw_j^B-U(q)\right].
\]
This is exactly the sector already in the repository, not a new action.

## Exact Hilbert tensor and canonical charge

Treating the metric as independent, the Hilbert tensor of this stipulated matter action is
\[
T_{\mu\nu}=c K_{AB}(D_\mu q)^A(D_\nu q)^B+
g_{\mu\nu}\left[-\frac c2g^{\alpha\beta}K_{AB}(D_\alpha q)^A(D_\beta q)^B-U\right].
\]
Let n^\mu be the ADM future unit normal, \xi^\mu=(\partial_t)^\mu=Nn^\mu+N^i(\partial_i)^\mu. Then
\[
\rho_H=T_{\mu\nu}n^\mu n^\nu=\frac c{2N^2}K(V,V)+\frac c2h^{ij}K(w_i,w_j)+U,\quad
j_i=T_{\mu\nu}n^\mu(\partial_i)^\nu=\frac cN K(V,w_i).
\]
The canonical momenta are \(\pi_A=c\sqrt h K_{AB}V^B/N\), so \(\sqrt h j_i=\pi_Aw_i^A\). The *exact canonical Hamiltonian* is
\[
\boxed{
H_{\rm can}=\int d^3x\sqrt h\,T_{\mu\nu}n^\mu\xi^\nu
-\int d^3x\,\pi_A(\Omega_0q)^A
}
\]
up to specified boundary terms. This includes the shift, and the temporal-connection correction is essential if \(\Omega_0\ne0\). When \(\Omega_0=0\) and the background admits \(\xi\) as a relevant symmetry, the canonical generator coincides with the stated stress-energy charge. For a background time-dependent metric or prescribed source, the instantaneous equality does not imply a conserved global energy. With a metric-dependent/spin connection the Hilbert variation acquires connection contributions; the displayed tensor is then incomplete.

## Interpretation and limitation

The sign of \(\rho_H\) inherits the indefinite (2,6) kinetic pairing in the unconstrained comparator; a matching Hilbert energy does not establish stability. The result makes no claim that \(\int Tn\xi\) is the total gauge-invariant gravitational energy or the Hamiltonian of a diffeomorphism-invariant composite single-Theta theory. In the latter, lapse/shift, metric, connection and theta jets are interdependent; one must derive the full variational chain rule, constraints, boundary charges and physical symplectic quotient from the same selected action. The working source registry [canonical/ACTION.en.md](../../canonical/ACTION.en.md) and post-#635 status still leave full action/source reduction OPEN.

## Minimal next test

Evaluate the complete composite time-dependent action's ADM Hessian, including all \(g[D\Theta]\) and connection chain-rule terms, *before* identifying a Hilbert tensor. Compare Noether/canonical charges in the resulting constrained theory, and test whether any physical negative-norm mode survives. Do not infer a new cosmological scalar from the fixed-background identity alone.

SymPy reproduction: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_energy_charge_bridge.py' -v\`.