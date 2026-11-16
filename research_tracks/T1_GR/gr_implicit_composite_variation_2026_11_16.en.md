<!-- BILINGUAL-UNIT: gr-implicit-composite-variation-2026-11-16 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Formal conditional chain rule, not a UBT action derivation.
UBT-AI-PROVENANCE-END
-->
# Implicit composite variation in canonical GR recovery

<!-- UNIT: scope -->
## Status and assumptions
[RESEARCH / CONDITIONAL] Canonical GR tetrad remains E_mu=N0^(-1/2)D_mu Theta with central sharp metric and a metric-compatible omega=omega_LC(E)+K. Treat Theta and contortion K as provisional independent variables for this implicit-variation diagnostic. No replacement of canonical action, representation or metric is proposed. Boundary conditions, functional-analytic domains, gauge fixing, and constraints must be specified before the inverse exists.

<!-- UNIT: equation -->
## Exact implicit chain rule
Write the defining jet schematically as J(Theta,E,K), including the dependence of omega_LC(E) on derivatives of E. Let J_E be its full Fréchet derivative; it is generally a **differential operator**, not an ordinary finite matrix. The equation and variation are
```text
E = J(Theta,E,K),     F=E-J(Theta,E,K)=0
A = I - J_E
A delta E = J_Theta delta Theta + J_K delta K
delta E = A^(-1) (J_Theta delta Theta + J_K delta K), if A invertible
S_red[Theta,K] = S[Theta,E(Theta,K),K]
EL_Theta(S_red) = S_Theta + J_Theta^* (A^*)^(-1) S_E
EL_K(S_red)     = S_K + J_K^* (A^*)^(-1) S_E
```
The starred operators are formal adjoints with the same integration measure and boundary conditions used to define the Euler derivatives. The expressions are valid only when A and its adjoint admit the indicated inverses in the chosen gauge/function spaces. Their interpretation must also account for the fact that K is physical contortion, not a completely free arbitrary connection independent of E.

<!-- UNIT: distinction -->
## Connection-source interpretation and constraints
The fixed-E Palatini source is not by itself the reduced contortion equation. The latter includes J_K^* (A^*)^(-1) S_E; it may cancel or enhance fixed-E currents depending on the actual action, and no cancellation can be inferred from symmetry alone. The earlier Lorentz-orbit rank test concerns the *direct* map J_K and does not establish a rank or a no-go for the full reduced differential equations without A's analysis. If A has a kernel, naive elimination fails and a separate constrained variation or Fredholm solvability analysis is necessary. For a left null vector l of A, the linearized compatibility condition is l^* (J_Theta delta Theta+J_K delta K)=0; in infinite-dimensional settings functional analytic qualifiers are essential.

<!-- UNIT: existing -->
## Relation to canonical calculations
The existing frozen torsion-free W_L composite analysis, canonical/gr_closure/gap_10t_dcomposite_linearized.tex, already obtains det(I-A_symbol)=(1-q)^6 for its specific frozen **real-exponential symbol**, q=lambda dot s, and nonvanishing for real Fourier k. That result must not be mistaken for invertibility of the global variable-coefficient operator, especially for torsionful branch B. It is not newly re-proved here. The split-jet auxiliary completion A is algebraically surjective but does not choose a metric; this is a distinct selection obstruction.

<!-- UNIT: locked -->
## Metric-locked kinetic term
On the exact classical central metric constraint, with <D_mu Theta,D_nu Theta> = N0 g_munu and the conventional scalar kinetic contraction L=1/2 sqrt(-g) g^munu <D_mu Theta,D_nu Theta>, one has L=2 N0 sqrt(-g) in four dimensions. This identity is conditional on the chosen precise pairing and admissible Lorentz slice. It means this contracted kinetic scalar alone becomes a volume term on the constrained branch and cannot, merely by rewriting, yield the Einstein curvature kinetic term. Off-constraint variations and the correct composite functional derivatives require separate calculation.

<!-- UNIT: gates -->
## Next decisive calculations
(1) Derive J_Theta,J_E,J_K from the finalized **paired** biquaternion derivative including connection reconstruction and reality constraints. (2) Choose actual on-shell background and analyze A's kernel/range with gauge quotient, rather than assuming invertibility. (3) Derive the exact reduced Euler current from the finalized action. (4) Analyze physical Hessian and no-go/selection criteria for both architectures. (5) Lean, full CI and bilingual independent semantic verification remain pending. No promotion to canonical GR.
