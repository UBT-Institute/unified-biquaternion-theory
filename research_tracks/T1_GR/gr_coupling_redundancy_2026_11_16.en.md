<!-- BILINGUAL-UNIT: gr-coupling-redundancy-2026-11-16 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Classical equivalence audit; not a proof of a new gauge symmetry.
UBT-AI-PROVENANCE-END
-->
# Audit: are the apparent gravitational couplings physically redundant?

<!-- UNIT: question -->
## Original question [RESEARCH / CONDITIONAL]
Test whether apparent coefficients in a biquaternionic gravity action are gauge/redundant rather than fundamental. Do **not** add a field or posit a new gauge symmetry to rescue coefficients. Keep canonical single-Theta metric and connection restrictions unchanged. Distinguish normalization, unit convention, local gauge, topological boundary equivalence, and dynamical observability.

<!-- UNIT: classical -->
## Overall normalization and relative couplings
```text
S[a,b,c] = a I_R + b I_P + c I_m
S[lambda*a,lambda*b,lambda*c] = lambda*S[a,b,c], lambda != 0
delta S = 0 iff delta (lambda*S) = 0 (classical stationary equations)
For a != 0: effective ratios b/a and c/a remain invariant under common rescaling
T^a = D_omega e^a
d(e^a wedge T_a) = T^a wedge T_a - e^a wedge e^b wedge R_ab
```
Multiplying the **entire** classical action by a constant lambda != 0 leaves its stationarity equations unchanged, provided all sectors and boundary terms scale consistently. Thus one overall coefficient can be conventionally normalized when appropriate, and is not an independent classical coupling in isolation. This is not a local gauge symmetry. At fixed quantum hbar, exp(i lambda S/hbar) changes, so the quantum interpretation requires care. A separately normalized matter action can give observable gravitational-to-matter coupling; dimensionless ratios b/a or c/a are unaffected by common scaling. A change of units does not alter dimensionless observables. When a=0, the ratio parameterization is not valid and must be considered separately.

<!-- UNIT: parity -->
## Why the odd curvature coefficient may disappear in restricted sectors
For a torsion-free Levi-Civita connection the epsilon-curvature scalar P vanishes identically by first Bianchi, so b has no local bulk effect **on that restricted field space**. If torsion varies independently, the Holst-type epsilon-curvature density is not by itself universally a boundary term: Nieh–Yan says the difference between it and a particular torsion-square term is exact. With appropriate boundary conditions, an exact Nieh–Yan addition does not change bulk Euler equations, but a bare b*P may change the torsion-spin equation. An effective ratio b/a can be physically relevant with spin sources. Whether a particular b disappears in complete composite-Theta dynamics must be checked, not assumed.

<!-- UNIT: projective -->
## A four-vector ambiguity is a different question
An unrestricted metric-affine Einstein–Hilbert action has a projective transformation of its connection by a one-form that preserves its Ricci scalar. The canonical **metric-compatible Lorentz** connection generally cannot accept that shift because it induces nonmetricity. It does not automatically identify a,b as gauge parameters. The cancelling common central term of a two-sided bimodule derivative is a separate kinematic redundancy to audit in its own representation.

<!-- UNIT: classification -->
## Action quotient / equivalence tests
Classify coefficients by (i) common nonzero multiplication of the full classical action; (ii) legitimate invertible field redefinitions with specified observable map; (iii) algebraic identities and exact boundary densities under stated boundary conditions; (iv) actual local gauge transformations with generators and first-class constraints; (v) parameter combinations measurable through relative matter coupling or physical spectra. Do not confuse an unfixed parameter with an established gauge redundancy. A new 'one-parameter family' claim requires computing rank of the map from couplings to gauge-invariant observables, not just counting symbols.

<!-- UNIT: immediate -->
## Next exact UBT-specific gate
Evaluate the full two-sided biquaternionic Theta action with the derived E and omega, including its torsion and spin-current variation. Compare two actions differing in the odd coefficient **on the same admissible on-shell configurations** and compare physical response to spin and metric perturbations; if their gauge-invariant observables coincide, only then declare the parameter redundant on that sector. Determine the equivalence class for a by explicitly including the matter sector and ultimately hbar. These gates remain open.

<!-- UNIT: verification -->
## Verification
The overall-scaling identities and coupling-ratio invariance were checked with exact SymPy algebra. They are elementary classical identities, not a full UBT result. Existing canonical gravity coefficient-underdetermination result still applies. Bilingual semantic review, full CI, Lean, canonical constrained Hessian and on-shell response all pending; do not promote or merge before mandatory checks.
