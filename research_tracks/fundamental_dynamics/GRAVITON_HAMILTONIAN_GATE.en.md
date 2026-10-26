<!-- BILINGUAL-UNIT: GRAVITON_HAMILTONIAN_GATE -->
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


# Graviton existence and Hamiltonian — concrete acceptance test

**2026-10-26 | integrated UBT Fundamental Dynamics track | benchmark, NOT a claim that UBT contains a graviton.**

## Fundamental single-field premise

The only fundamental field is the 8-real-component biquaternion Theta. The canonical geometric equations are the nonzero-composite two-sided derivative E_mu=(D_mu Theta)/sqrt(N0)∈W_L, the sharp anticommutator metric, and omega(e,T)=omega_LC(e)+K(T). No independent metric, spinor, gauge boson or torsion fields can be added to make a desired result true. As established in MASTER_DERIVATION.en.md and canonical/ACTION.en.md, the dynamically selected T[Theta], microscopic kinetic term, real measure on complex time and the reduced symplectic form do not exist yet. Consequently a graviton CANNOT be declared derived from the kinematic metric rank theorem or a test-field gravitational-wave ansatz.

## Exact target: helicity-2 count and energy

Take a genuinely *on-shell* real Lorentzian background Theta_bar admitting a flat local limit and a complete derived Theta equation F[Theta]=0. Compute full linearization ell_F, including delta A, delta B, delta T and induced delta e and delta g, after gauge reduction. For a physical wave with nonzero spatial k along z, use symmetric spatial perturbation h_ij (6 components). The TT projector is
\[
P_{ij}=\delta_{ij}-\hat k_i\hat k_j,\quad
\Lambda_{ij,kl}=\tfrac12(P_{ik}P_{jl}+P_{il}P_{jk})-\tfrac12P_{ij}P_{kl}.
\]
This acts on the 6D real vector space of symmetric 3x3 matrices and has EXACT rank two, independent of any UBT dynamics. For k parallel to z it leaves
\[
h^{TT}=\begin{pmatrix}h_+&h_\times&0\\ h_\times&-h_+&0\\0&0&0\end{pmatrix}.
\]
Two TT components are only **candidate physical polarizations**; they are not propagating until the linearized UBT principal symbol has two healthy null dispersive channels and the full constraints eliminate other physical modes or predict and test deviations.

The standard healthy **target benchmark** in a suitable normalized TT sector is
\[
L^{(2)}_{\rm TT}=\tfrac12(\dot h_+^2+\dot h_\times^2)-\tfrac12 k^2(h_+^2+h_\times^2),
\quad
H^{(2)}_{\rm TT}=\tfrac12(p_+^2+p_\times^2)+\tfrac12 k^2(h_+^2+h_\times^2),\quad p_\lambda=\dot h_\lambda.
\]
These formulae are a *benchmark for the GR endpoint*, NOT a chosen or derived UBT Lagrangian/Hamiltonian. In position space the k² term is the spatial gradient energy. Speed of light and normalization have been set to one, with standard boundary conditions. Exact Hamilton equations yield ddot h_lambda+k² h_lambda=0, so omega²=k² and energy is nonnegative for real k. A full UBT proof must derive this structure *from Theta only*, not adopt it as its own action.

## Actual go/no-go checks

1. **Reconstruction:** derive a single-valued physical composite map Theta↦(e,A,B,T), or a justified gauge/constraint quotient. Derive delta T rather than freezing the connection.
2. **Principal symbol:** compute the gauge-reduced Fourier principal symbol of the full linearized Theta E-L system and induced TT projection. Demonstrate two independent massless helicity-2 solutions with omega²=c²k² (or quantify an observationally acceptable alternative).
3. **Energy and constraints:** compute the reduced covariant presymplectic form, genuine canonical H, Dirac–Bergmann constraint algebra, norms and sign of TT kinetic terms. Reject a ghost, tachyon or spurious additional undetermined mode.
4. **Nonlinear extension:** demonstrate propagation on nonflat backgrounds, GR Einstein limit, and coupling to a conserved derived stress tensor.
5. **Particles AFTER gravity:** decompose small fluctuations of Theta around the proven vacuum by representations of the actual stabilizer and spacetime symmetry; derive their dispersion, quantization/statistics, masses and gauge charges from the same action. Counting components, labels or Fourier harmonics is not particle generation.

**Present verdict: NOT PROVED.** Mathematical calculation performed here is the TT-projection rank 2 and the conditional healthy GR benchmark. The genuine UBT principal symbol/Hamiltonian cannot be evaluated until a torsion selector and fundamental action or equivalent independently selected Hamiltonian flow exist.

Reproducer: tests/test_graviton_tt_hamiltonian_gate.py. Keep the evidence status separate from any benchmark.
