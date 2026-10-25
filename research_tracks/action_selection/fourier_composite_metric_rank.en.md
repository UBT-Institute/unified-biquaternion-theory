<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: fourier-normal-metric-rank.provenance -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact frozen Fourier first-jet rank, not Euler-Lagrange principal symbol.
UBT-AI-PROVENANCE-END -->
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

# Frequency-sensitive rank of the single-Theta composite metric

**Status: KINEMATIC LINEARIZATION PROVED; ON-SHELL RANK OPEN.** This extends the already merged geometric-rank and composite-spin results, rather than selecting a new fundamental UBT action.

## Background and field variations

Use a local nondegenerate flat coframe and a timelike field value. The following conditions hold at one point, not on a globally constant-Theta configuration:

\[
X^a=(r,0,0,0),\qquad
e_\mu{}^a=\delta_\mu{}^a,\qquad
q=\sqrt{\mathcal N_0}>0,\qquad \eta=\mathrm{diag}(-1,1,1,1).
\]

For the Fourier first jet, vary the original field and all Lorentz boosts and rotations. The rotations annihilate the timelike field at that point:

\[
\delta e_\mu{}^0=\frac{k_\mu\xi^0}{q},\qquad
\delta e_\mu{}^i=\frac{k_\mu\xi^i+r\beta_\mu{}^i}{q},\qquad
h_{\mu\nu}=2\eta_{ab}e_{(\mu}{}^a\delta e_{\nu)}{}^b.
\]

The normal metric component is constrained exactly:

\[
\boxed{h_{00}=-\frac{2k_0\xi^0}{q}.}
\]

## Exact Jacobian ranks

For nonzero temporal frequency the symmetric metric perturbation map is surjective:

\[
\boxed{
k_0\ne0:\quad \operatorname{rank}J_g=10,\quad
\operatorname{rank}J_e=13.
}
\]

For strictly static **field** Fourier amplitudes with nonzero spatial wave vector the metric rank drops, despite the unchanged tetrad rank:

\[
\boxed{
k_0=0,\ \mathbf{k}\ne0:\quad
\operatorname{rank}J_g=9,\quad
\operatorname{rank}J_e=13.
}
\]

At zero Fourier momentum the ranks are:

\[
\boxed{
k_\mu=0:\quad \operatorname{rank}J_g=9,\quad
\operatorname{rank}J_e=12.
}
\]

All metric perturbations except the normal component remain achievable in the static sector. The verified right inverse for nonzero temporal frequency is:

\[
\xi^0=-\frac{qh_{00}}{2k_0},\quad \xi^i=0,\quad
\beta_0{}^i=\frac{qh_{0i}+k_i\xi^0}{r},\quad
\beta_i{}^i=\frac{qh_{ii}}{2r},\quad
\beta_i{}^j=\frac{qh_{ij}}r\ (i<j),\quad
\beta_j{}^i=0\ (i<j).
\]

## Physical meaning and caveats

This is the linearized expression of the invariant unit-clock relation:

\[
g^{\mu\nu}\partial_\mu r\,\partial_\nu r=-q^2,\qquad
h_{00}=-\frac2q\partial_0\delta r
\quad\text{in the specified local frame}.
\]

The missing static normal direction belongs to the map from underlying field perturbations to metric perturbations. It does **not** prohibit a static physical metric with time-dependent Theta/connection representatives, or imply a no-go for Newtonian gravity. Nor is this the symbol of the coupled Palatini–Holst **field equations**. The connection curvature equations may enforce additional constraints. The physical Hamiltonian and tensor spectrum have not been computed.

## Next decisive calculation

Linearize the coupled unrestricted composite Euler equations on a nondegenerate on-shell background of the clearly labeled comparison action. Calculate the curvature-sensitive spin block and its principal symbol, quotient local Lorentz and diffeomorphism gauge, and test the remaining normal Hamiltonian condition. The fundamental UBT action must independently justify any curvature operator before physics claims.

**Repo grounding:** merged PR #686 and merged PR #694; `canonical/geometry/connection.tex`; `canonical/ACTION.en.md`. **Checker:** `tools/verify_fourier_composite_metric_rank.py` and focused pytest.
