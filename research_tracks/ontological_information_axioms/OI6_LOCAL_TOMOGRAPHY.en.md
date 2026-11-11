<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# OI-6 — Can local tomography select complex amplitudes?

**Status:** standard finite-dimensional matrix mathematics [STD]. The derivation of an operational information principle, a specific Hilbert-space field, or a UBT physical law remains [OPEN]. We do not claim priority over established quantum-foundations research.

## A. Explicit operational assumption

Local tomography means: correlations of all joint **product measurements** determine a composite state uniquely. This is an extra testable composition axiom, not a consequence of mere existence, distinguishability, finite signalling speed, or logical consistency. Compare conventional real and complex Hilbert quantum models with the standard tensor composition rule.

## B. OI-6-T3 — Real two-level systems have a hidden global degree of freedom

Choose the real antisymmetric matrix J and its two-site tensor product W:

$$
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
W=J\otimes J,\quad W^T=W,\quad W^2=I_4,\quad
\mathrm{Tr}(W)=0.
$$

The following two global real density matrices and their spectral projectors are distinct and positive:

$$
\rho_\pm=\frac{I_4\pm W}{4},\qquad
P_\pm=\frac{I_4\pm W}{2},\qquad
\mathrm{Tr}(\rho_+P_+)=1,\quad
\mathrm{Tr}(\rho_-P_+)=0.
$$

Every admissible single-rebit effect A or B is real symmetric. By antisymmetry of J, its trace pairing with either effect vanishes. Therefore all product-measurement statistics are identical:

$$
\mathrm{Tr}[(A\otimes B)(\rho_+-\rho_-)]
=\frac12\mathrm{Tr}(AJ)\,\mathrm{Tr}(BJ)=0.
$$

**OI-6-T3 [STD]:** real quantum theory with conventional tensor products violates local tomography even though a permitted *global* real-symmetric measurement distinguishes the states perfectly. This is a concrete textbook counterexample, not a novel UBT discovery. The symmetric global operator space splits into local products and an extra antisymmetric-antisymmetric sector spanned by W.

## C. OI-6-T4 — The complex two-level model is locally tomographic

With complex amplitudes, the local Pauli-Y operator is Hermitian, unlike in the real model. Its two-site product recovers the otherwise hidden observable:

$$
\sigma_y=iJ,\qquad
\sigma_y\otimes\sigma_y=-W,\qquad
\mathrm{Tr}(\rho_+\sigma_y\otimes\sigma_y)=-1,\quad
\mathrm{Tr}(\rho_-\sigma_y\otimes\sigma_y)=1.
$$

The Pauli products form an orthogonal real basis of all complex Hermitian bipartite operators. Their local joint statistics therefore determine any complex two-qubit density matrix.

$$
K_{\mathbb R}(n)=\frac{n(n+1)}{2},\qquad
K_{\mathbb C}(n)=n^2,\qquad
K_{\mathbb R}(4)=10>3^2=9,\qquad
K_{\mathbb C}(4)=16=4^2.
$$

**OI-6-T4 [STD]:** within the restricted choice of conventional real versus complex Hilbert-space quantum theory with standard composites, local tomography rejects the real model and is satisfied by the complex model. It is a conditional *discriminator*, not the derivation of quantum amplitudes from information alone.

## D. Explicit countermodel to uniqueness and UBT bridge

Classical probabilistic bits also satisfy local tomography. Thus neither local tomography nor a binary information capacity independently selects complex Hilbert quantum theory. Stronger reconstruction theorems exist when Jordan-algebra and composite-system assumptions are added; those assumptions must be listed rather than silently imported. Quaternionic composition introduces further subtleties and is not resolved by this two-model comparison.

The previous OI-6 Weyl calculation selected a Pauli triple **only after assuming** a complex two-component, linear, isotropic Hamiltonian. Local tomography supplies a distinct possible *selection criterion* for complex amplitudes. It does not select the observed spatial dimension, the canonical complex biquaternion Theta field, a preferred action, or ghost-free GR/SM dynamics. No change to canonical/ or WHAT_IS_PROVED.md is justified.

## E. Falsifiers and next proof gates

**OI-6-G1 [OPEN]:** justify local tomography from independently operational premises, or identify consistent physically viable theories in which it fails. **OI-6-G2 [OPEN]:** exclude classical and general probabilistic theories without assuming complex amplitudes or a Bloch sphere. **OI-6-G3 [OPEN]:** establish composition, dynamics and Clifford/Theta embedding without inserting Lorentz geometry or complex quantum theory by hand.

## F. Reproducibility and known prior art

The standard-library script research_tracks/ontological_information_axioms/verify_local_tomography.py contains 8 unit tests covering exact real matrix rank, positive global states, indistinguishable product effects, perfect global discrimination, a complete complex Pauli-product basis and a classical countermodel. These tests check this finite mathematical setting; they cannot establish an ontological axiom.

- Hardy and Wootters (2010), *Limited Holism and Real-Vector-Space Quantum Theory*: https://arxiv.org/abs/1005.4870 .
- Barnum and Wilce (2014), *Local tomography and the Jordan structure of quantum theory*: https://doi.org/10.1007/s10701-014-9777-1 .
- *Quantum computation is the unique reversible circuit model for which bits are balls* (2018): https://doi.org/10.1038/s41534-018-0123-x .