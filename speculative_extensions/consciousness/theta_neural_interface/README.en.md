<!-- BILINGUAL-UNIT: theta-neural.overview -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Theta–neural interface: a substrate-neutral speculative track

**SPEC-THETA-NEURAL-001 — SPECULATIVE; C_working; 2026-11-02.** Translation source: this English edition. The [Czech edition](README.cs.md) has the same content. The machine-readable claim ledger is [status.json](status.json).

The question is whether a physical collective mode of the full UBT field can couple to measured neural activity without requiring microtubules as the unique carrier. This track supplies a falsifiable sequence of research gates and a checked classical response comparator. It supplies no established mechanism of consciousness, no quantum-coherence result, and no derived biological alternative to Orch-OR.

<!-- BILINGUAL-UNIT: theta-neural.architecture -->
## Canonical boundary

The starting object remains the full biquaternionic or declared matrix representation of the single field, with complex time:

$$
\Theta(q,\tau)\in\mathbb C\otimes\mathbb H,\qquad \tau=t+i\psi.
$$

There is no scalar ansatz for the full field and no change to its component count, tetrad, metric, action, or connection. The scalar effective coordinate below would describe one observable of a full-field configuration. It is not a replacement for that configuration. No new fundamental field or particle is introduced. All effective couplings and frequencies are assumptions until derived and calibrated.

The imaginary coordinate is not itself a consciousness observable. A bare field phase may be gauge dependent. Compactness, winding, or a toroidal picture alone provides neither a biological resonator nor protection from thermal decoherence. No projection, trace readout, or internal-coordinate average is introduced as a new definition of the canonical metric.

<!-- BILINGUAL-UNIT: theta-neural.inventory -->
## Existing material and biological candidates

The older [psychon draft](../psychons.tex) is historical and explicitly speculative. It uses the superseded quaternionic-time notation and contains unestablished coupling and scale assignments. Its numerical mass/range estimates and particle interpretation are not inputs to this track. The older [bistable model](../../solution_consciousness_model_P3/consciousness_model_solution.tex) assumes a potential and does not derive a neural coupling. A deterministic gradient descent in a double-well potential does not by itself produce spontaneous recurrent switching; noise or additional dynamics would have to be specified.

| Candidate | Role to investigate | Present status |
|---|---|---|
| Microtubules | One possible material intermediary | SPECULATIVE as the carrier of the proposed UBT mode |
| Membranes and ion-channel assemblies | Measurable polarization/current response | SPECULATIVE as the carrier of the proposed UBT mode |
| Collective neural-network activity | A measured coarse variable against which to compare response | SPECULATIVE as the carrier of the proposed UBT mode |
| A toroidal or topological mode | A mathematical candidate requiring an observable and stability calculation | SPECULATIVE; no biological microtorus is inferred |

The track does not rank these candidates. Identifying a biological effect of microtubule manipulation does not alone establish quantum processing or a UBT coupling. Microtubules may remain one intermediary even if the hypothetical physical mode is collective.

<!-- BILINGUAL-UNIT: theta-neural.bridge -->
## The first gate: a physical observable

Let the measured coordinate be a small polarization perturbation along a specified experimental probe direction, normalized by a nonzero calibration scale. Let the hypothetical collective coordinate be a normalized real functional of a full-field configuration and a reference background:

$$
s=t/t_0,\qquad x(s)=\widehat{\boldsymbol e}\cdot\delta\boldsymbol P(t)/P_0,
\qquad z(s)=\bigl(\mathcal F[\Theta](t)-\mathcal F[\Theta_0](t)\bigr)/F_0.
$$

Here the time scale, polarization scale, and functional scale are fixed positive calibration constants. The probe direction belongs to the apparatus, not to a preferred fundamental frame. Both effective coordinates are dimensionless and real. The coordinate symbol already reserved for the UBT base space is not reused for a new field.

The functional must be invariant under the declared physical gauge action, with the background and apparatus transformed consistently. Its perturbation must survive the constrained physical fluctuation space, and the neural coordinate and collective coordinate must not double count the same physical mode. A gauge orbit alone is not a physical oscillator. Neither this functional nor two independent healthy effective coordinates have been derived here. Failure of this gate rejects the proposed bridge before any consciousness interpretation.

<!-- BILINGUAL-UNIT: theta-neural.comparator -->
## Classical response comparator

Assume, solely for a local weak-response comparison, two independent healthy coordinates with unit dimensionless inertia, a real reciprocal coupling, and positive damping. The energy scale is a fixed positive constant. Primes mean differentiation with respect to dimensionless time:

$$
\frac{H}{E_0}=\frac12\left[(x')^2+(z')^2+\omega_n^2x^2+\omega_z^2z^2\right]-\kappa xz,
\qquad \omega_n,\omega_z,\gamma_n,\gamma_z>0,\quad\kappa\in\mathbb R.
$$

$$
x''+\gamma_nx'+\omega_n^2x-\kappa z=f(s),\qquad
z''+\gamma_zz'+\omega_z^2z-\kappa x=0.
$$

All coefficients and the force in these equations are dimensionless. Damping represents exchange with an unmodelled environment. There is no stochastic bath, density matrix, quantization, or objective-reduction law. The unit-inertia normalization and this truncation are adopted effective assumptions, not consequences of the UBT action. Converting any frequency to hertz requires an independently calibrated time scale; no EEG frequency is predicted.

<!-- BILINGUAL-UNIT: theta-neural.algebra -->
## Stability, energy, and response

For positive uncoupled frequencies, the quadratic potential is strictly positive exactly when its determinant is positive. The undamped squared normal frequencies are:

$$
K=\begin{pmatrix}\omega_n^2&-\kappa\\-\kappa&\omega_z^2\end{pmatrix},\qquad
\det K=\omega_n^2\omega_z^2-\kappa^2>0,
\qquad |\kappa|<\omega_n\omega_z.
$$

$$
\Omega_\pm^2=\frac{\omega_n^2+\omega_z^2\pm
\sqrt{(\omega_n^2-\omega_z^2)^2+4\kappa^2}}{2}.
$$

These statements follow from the positive leading principal minor and the characteristic polynomial of the real symmetric stiffness matrix. At equality there is a zero stiffness mode; beyond it the quadratic energy is unbounded below. The implementation rejects both cases. With strictly positive damping and strictly positive stiffness the unforced equilibrium is asymptotically stable: energy decreases, and the only invariant trajectory with both velocities zero is the zero equilibrium. The driven energy balance is:

$$
\frac{d(H/E_0)}{ds}=f x'-\gamma_n(x')^2-\gamma_z(z')^2.
$$

For harmonic forcing with the stated Fourier convention, solving the two linear equations gives:

$$
f(s)=\operatorname{Re}\!\left(f_\Omega e^{-i\Omega s}\right),\qquad
A=\omega_n^2-\Omega^2-i\gamma_n\Omega,\quad
B=\omega_z^2-\Omega^2-i\gamma_z\Omega,
$$

$$
\chi_x(\Omega)=\frac{B}{AB-\kappa^2}
=\frac{1}{A-\kappa^2/B},\qquad
\chi_z(\Omega)=\frac{\kappa}{AB-\kappa^2}.
$$

The neural autoresponse is even in the coupling, while the cross-response changes sign. Positive damping gives a passive neural response for positive drive frequency under this convention. The zero-coupling limit recovers the single neural oscillator. These are properties of the assumed classical comparator, not evidence for quantum coherence, a physical psychon, or consciousness.

<!-- BILINGUAL-UNIT: theta-neural.identifiability -->
## What would distinguish UBT?

Relabelling the second coordinate as an ordinary material oscillator leaves every equation and response above unchanged. A split resonance, long-lived correlation, or improved fit against a single oscillator therefore cannot identify a UBT origin. Even the coupling sign is not identifiable from the neural autoresponse alone. A missing extra resonance also cannot exclude an unconstrained theory that permits arbitrarily small coupling.

Use three explicit model classes: an uncoupled measured baseline, an ordinary coupled biological/environmental model, and a UBT-linked model whose observable and parameter restrictions are independently derived. Freeze the measured variable, physical units, bandwidth, noise model, calibration data, intervention, alternative models, and held-out comparison before looking for a signal. A future UBT claim requires a distinguishable held-out consequence beyond the ordinary coupled model and a noise/decoherence budget for any claimed quantum process. This repository supplies no biological data or preregistered experimental result.

<!-- BILINGUAL-UNIT: theta-neural.gates -->
## Research gates and stopping rules

| Gate | Required evidence | Current status |
|---|---|---|
| G0 | Explicit gauge-invariant observable and independent constrained physical mode | OPEN_GAP |
| G1 | Derived coupling to the measured material variable, normalization, and physical units | OPEN_GAP |
| G2 | Healthy effective spectrum and justified reduction from full UBT | OPEN_GAP; the adopted classical comparator alone is checked |
| G3 | Thermal noise, dissipation, and a decoherence calculation if quantum coherence is invoked | OPEN_GAP |
| G4 | A frozen consequence distinguishable from ordinary coupled biology | OPEN_GAP |
| G5 | Operational relation to a measured consciousness correlate | OPEN_GAP |

The next scientific step is G0, not fitting frequencies or naming a particle. Construct one explicit invariant functional in a specified admissible background and test whether its perturbation survives the constrained Hessian. If it is pure gauge, has an unhealthy kinetic sign, or double counts the neural variable, record the negative result and stop that candidate. If the first gate passes, derive G1 before ranking membranes, microtubules, or other biological carriers.

<!-- BILINGUAL-UNIT: theta-neural.verification -->
## Verification and reproduction

Run from the repository root with NumPy, SciPy, SymPy, and pytest installed:

```bash
python speculative_extensions/consciousness/theta_neural_interface/verify_model.py
python -m pytest tests/test_theta_neural_interface.py
python tools/check_bilingual_pairs.py --root .
```

The verifier checks the determinant, normal-mode roots, energy balance, response inversion, and coupling-sign invariance with SymPy. A separately formulated numerical first-order resolvent, eigenvalue stability check, and passivity check use a fixed random seed. Tests also compare forced time-domain integration with the analytic response and unforced energy loss with integrated dissipation, including marginal/unstable rejection and the zero-coupling baseline. [verification.json](verification.json) records versions, source hashes, tolerances, and results. These checks do not validate the unconstructed field functional or the biological interpretation.

**LEAN-PENDING:** Lean and Lake are absent in the authoring environment; no kernel-checked proof is supplied. Independent bilingual semantic review remains a separate pre-merge gate. Structural pairing or successful numerical checks do not replace that review and do not upgrade the physical claim or the editorial tier.

<!-- BILINGUAL-UNIT: theta-neural.references -->
## Primary literature and scope

- Hameroff and Penrose, [review of Orch-OR](https://doi.org/10.1016/j.plrev.2013.08.002): the comparator for the microtubule-based hypothesis, not evidence for a UBT mode.
- Tegmark, [brain-process decoherence calculation](https://arxiv.org/abs/quant-ph/9907009), and Hagan, Hameroff, and Tuszynski, [response on biological feasibility](https://arxiv.org/abs/quant-ph/0005025): competing model-dependent calculations; neither supplies a decoherence time for an undefined UBT observable.
- [Microtubule-stabilizer study in rats](https://doi.org/10.1523/ENEURO.0291-24.2024): a material/anesthetic intervention result, not a measurement of a UBT mode or quantum coherence.

Historical drafts retain their historical status. This is a new, narrowly scoped author-directed speculative investigation; it does not reactivate the old psychon ontology or close a canonical GR, gauge, or quantum gap.
