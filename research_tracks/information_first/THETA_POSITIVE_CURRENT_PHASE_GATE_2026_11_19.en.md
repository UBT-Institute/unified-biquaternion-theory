<!-- BILINGUAL-UNIT: theta-positive-current-phase-gate-2026-11-19 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional flat Klein-Gordon/Dirac and observer-flow comparators; NOT an on-shell physical UBT Noether current, time or quantum-collapse derivation.
UBT-AI-PROVENANCE-END
-->
# Conserved observer probability from one Theta: Noether sign and Dirac-phase compatibility gates

<!-- UNIT: scope -->
## Scientific scope: a positive local Gram is not a conserved charge

The locked UBT field is one full biquaternion \(\Theta\in\mathbb C\otimes\mathbb H\simeq M_2(\mathbb C)\), with canonical first jet \(E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta\in W_L=i\,\mathrm{Herm}_2\) in the classical branch, and sharp-central metric \(g_{\mu\nu}I_2=\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)\). The previously derived operational positive response \(\rho_N=T_NT_N^\dagger/\operatorname{tr}(T_NT_N^\dagger)\) uses an observer-selected \(N>0\), hence a Hermitian \(\dagger\), and is NOT the geometric metric or a Noether current. The microscopic single-\(\Theta\) action remains unselected. We test the precise missing interface rather than inserting a global time, a compensator field, a second physical field or Born collapse.

<!-- UNIT: kg -->
## Flat phase Noether current has an indefinite sign

As a **flat-background complex scalar comparator only**, take a matrix-valued field \(T\), fixed Minkowski \(\eta=\operatorname{diag}(-1,1,1,1)\), and
\[
\mathcal L_{\rm KG}=-\operatorname{tr}\big((\partial_\mu T)^\dagger\partial^\mu T+m^2T^\dagger T\big),\qquad
(\Box-m^2)T=0.
\]
Its central global \(U(1)\) phase symmetry \(T\mapsto e^{i\alpha}T\) has the real on-shell conserved current (one overall charge-sign convention)
\[
\boxed{
j^\mu_{\rm KG}=-i\,\operatorname{tr}\big(T^\dagger\partial^\mu T-(\partial^\mu T^\dagger)T\big),
\quad\partial_\mu j^\mu_{\rm KG}=0.}\tag{A}
\]
For \(T_\pm(t)=e^{\mp imt}B\), with fixed \(B=\operatorname{diag}(2,1)\) and \(m>0\), both solve the displayed flat equation, yet
\[
\boxed{j^0_{\rm KG}[T_+]=10m,\qquad j^0_{\rm KG}[T_-]=-10m.}\tag{B}
\]
Thus this conserved phase current is NOT a universal positive detector intensity.

For the superposition \(T_\Sigma=2\cos(mt)B\), also a flat on-shell solution,
\[
j^0_{\rm KG}[T_\Sigma]=0,\qquad
\operatorname{tr}(T_\Sigma^\dagger T_\Sigma)=20\cos^2(mt),\qquad
\frac{d}{dt}\operatorname{tr}(T_\Sigma^\dagger T_\Sigma)=-20m\sin(2mt).
\]
So the positive pointwise Gram response is not automatically a conserved charge either. A positive-frequency restriction can make (B) positive but requires a selected notion of positive frequency, which does not follow from the canonical local full-\(\Theta\) axioms or an imposed global cosmological clock. All cases are **comparator solutions only**, not physical on-shell Lorentz-real UBT.

<!-- UNIT: phase -->
## Central scalar phase still conflicts with the locked classical metric

The flat comparator central phase \(T\mapsto e^{i\alpha}T\) is furthermore NOT automatically a global symmetry of the **same locked classical geometry**. If its homogeneous transformation is applied to the original canonical first jets,
\[
\boxed{
g_{\mu\nu}[e^{i\alpha}E]=e^{2i\alpha}g_{\mu\nu}[E],\qquad
e^{i\alpha}E_\mu\in W_L\text{ for all }E_\mu\in W_L
\Longleftrightarrow e^{i\alpha}\in\{+1,-1\}.}\tag{C}
\]
The exact phase-weight-two compatibility obstruction had already been proved in \`research_tracks/action_selection/phase_central_metric_compatibility.en.md\`; the present note uses it to REJECT any identification of (A) with an established fundamental UBT Noether current. Merely writing a scalar-phase-invariant positive comparator Lagrangian cannot complete the geometric UBT action. The potential-sector phase and the physical Lorentz sector may have different realized symmetry groups.

<!-- UNIT: dirac -->
## Positive Dirac pullback: vector phase is a right quaternion rotation

There is a positive but different CONDITIONAL route. In the existing flat Dirac pullback study, express the original one-field matrix as \(\Theta=[\,\xi\ \chi\,]\), two complex columns, choose the fixed real-linear bijection
\[
\boxed{
F(\Theta)=u=\begin{pmatrix}\xi\\\varepsilon\chi^*\end{pmatrix},
\quad\varepsilon=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\quad u^\dagger u=\operatorname{tr}(\Theta^\dagger\Theta).}\tag{D}
\]
The standard Dirac comparator has conserved hypersurface current \(j^a_{\rm D}=\bar u\gamma^a u\) on its own equation, with \(j^0_{\rm D}=u^\dagger u\ge0\) in the usual oriented local orthonormal frame. Covariantly the positive inner product is a flux through a spacelike surface with transformed future normal, NOT an invariant pointwise positive Lorentz scalar. These claims refer to the **selected Dirac comparator**, not the unfinished single-\(\Theta\) gravitational action.

Here is the sharper exact phase mismatch: the ordinary Dirac **vector** phase \(u\mapsto e^{i\alpha}u\) induces on the original \(\Theta\)
\[
\boxed{
F\!\left(\Theta\,\operatorname{diag}(e^{i\alpha},e^{-i\alpha})\right)
=e^{i\alpha}F(\Theta).}\tag{E}
\]
That is a **right \(SU(2)\) quaternionic phase**, not a central scalar UBT phase. Conversely
\[
\boxed{
F(e^{i\alpha}\Theta)=
\operatorname{diag}(e^{i\alpha}I_2,e^{-i\alpha}I_2)F(\Theta),}\tag{F}
\]
which is the standard two-Weyl-block *axial* phase, not a vector phase. In chiral gamma convention, a nonzero Dirac mass term generically breaks it: for \(u_0=(1,0,1,0)^\mathsf T\), \(\bar u_0u_0=2\) but the (F)-transformed bilinear is \(2\cos(2\alpha)\).

For a constant right phase \(R_\alpha=\operatorname{diag}(e^{i\alpha},e^{-i\alpha})\), the homogeneous tetrad transformation \(E_\mu'=E_\mu R_\alpha\) preserves the full central sharp metric because \(\det R_\alpha=1\), but does **NOT** preserve the complete Lorentz-real slice. At \(\alpha=\pi/2\),
\[
\boxed{E_0=iI_2\longmapsto iI_2(i\sigma_3)=-\sigma_3\notin i\,\mathrm{Herm}_2.}\tag{G}
\]
Thus a vector-Dirac conservation law pulled back through the chosen \(F\) is NOT yet a conserved **physically admissible** UBT current for the classical geometric branch. This is a new explicit link between earlier positive Dirac symplectic pullback and the already proved right-unitary phase/metric gate. The distinction persists even if the pointwise positive norm is exactly preserved by \(F\).

<!-- UNIT: unitary -->
## Positive unitary flow cannot select a single outcome

A second instructive **first-order conditional** comparator is \(i\partial_tT=HT\) with \(H=H^\dagger\). Then \(Q=TT^\dagger\) obeys
\[
\boxed{\dot Q=-i[H,Q],\qquad
\frac{d}{dt}\operatorname{tr}(Q^n)=0\quad(n=1,2,\dots).}\tag{H}
\]
Consequently \(\rho=Q/\operatorname{tr}Q\) evolves by unitary conjugation with fixed eigenvalues, rank, entropy and purity. E.g. for \(T(0)=\operatorname{diag}(2,1)\), \(\operatorname{tr}Q=5\), \(\operatorname{tr}Q^2=17\), \(\operatorname{tr}\rho^2=17/25\) for every \(t\). No selective collapse to a rank-one readout follows from this closed positive unitary flow. This is a standard QM comparison and it explicitly presupposes a Hamiltonian and evolution parameter.

One must not conflate the observer unitary \(T\mapsto UT\) used here with an admissible **physical** transformation of all canonical \(E_\mu\): for \(U\in SU(2)\), left multiplication preserves the complex central sharp metric but generally exits \(W_L\). The **linked** congruence \(E_\mu\mapsto U E_\mu U^\dagger\) does preserve \(W_L\), but by itself is only a spin-frame operation and still preserves density eigenvalues. A candidate real \(\Theta\) theory needs a proper derived dynamical law, compatible symplectic form and the reduced constraint algebra.

Finally, even before dynamics, the observer norm
\[
h_N(\Theta)=\operatorname{tr}(T_N^\dagger T_N)
\]
changes under a varying reference \(N\) unless a compatible observer transport law is specified. For fixed nonzero \(B=\operatorname{diag}(2,1)\), \(N(t)=\operatorname{diag}(e^{2\lambda t},e^{-2\lambda t})\) (positive, unit determinant), and \(T_N=N^{-1/2}BN^{-1/2}\), one has
\[
\boxed{h_N(B)=4e^{-4\lambda t}+e^{4\lambda t},}\tag{I}
\]
which is generally time dependent. The example fixes the field value and is an observer-reference algebraic diagnostic, not an on-shell regular-tetrad UBT solution.

<!-- UNIT: next -->
## Requirements for a real UBT observer current

**Next action-level gate (not a new axiom).** Search for a conserved future-directed observer current \(J^\mu[\Theta,D\Theta;\,N]\) from a **selected** single-\(\Theta\) action, with all these properties:
\[
\boxed{\nabla_\mu J^\mu=0\text{ on shell},\qquad
J^\mu n_\mu\ge0\text{ for future normals with fixed sign convention},}
\]
plus (i) \(N\) and its comparison connection reconstructed from admissible real geometry, not a new background or field; (ii) a nondegenerate compatible physical presymplectic structure with correct ghost and DOF constraints; (iii) reduction to conditional observer Hilbert-Schmidt response in a controlled limit; (iv) phase transformation preserving the selected Lorentz-real \(D\Theta\) branch; and (v) \(\psi\)-sector and probability normalization stability. A Dirac-like comparator supplies positivity if its equation, inner product, physical Lorentz representation and reference transport are all justified, but it does NOT select them from the present UBT action.

Only once a physically positive conserved response and genuinely realizable complete detector effects are obtained should one attempt a stochastic instrument, decoherence or branch-selection law. "Unitarity" alone preserves purity, so it cannot supply a selective collapse. No claimed photon or Born prediction follows from the present toy currents. Existing sources: canonical/AXIOMS.md; canonical/ACTION.en.md; research_tracks/action_selection/phase_central_metric_compatibility.en.md; research_tracks/action_selection/dirac_positive_symplectic_pullback.en.md; research_tracks/action_selection/volume_presymplectic_current.en.md; research_tracks/information_first/THETA_COMPLETE_FILTER_NORM_GATE_2026_11_19.en.md. Exact SymPy checks: tools/verify_theta_noether_positive_current_gate_2026_11_19.py and tools/verify_theta_dirac_phase_current_compatibility_2026_11_19.py.
