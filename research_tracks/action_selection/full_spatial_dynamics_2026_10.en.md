<!-- BILINGUAL-UNIT: spatial-dynamics.scope -->
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

# Full spatial dynamics in a restricted reduced metric family

**2026-10-29; C_working; CONDITIONAL.** English is the translation source. This calculation selects the Einstein kinetic ratio and relative curvature normalization within an explicitly supplied reduced Hamiltonian family. It includes arbitrary spatial dependence, local lapse variations, the evolution equations and the flat tensor modes. It does not finalize the microscopic single-Theta action. This is a reproducible restricted geometrodynamics calculation, not a claim of a new general-relativity theorem.

<!-- BILINGUAL-UNIT: spatial-dynamics.assumptions -->
## Phase space, conventions and selection hypothesis

Work on a smooth oriented spatial manifold of dimension **3**, with positive spatial metric and a symmetric conjugate momentum density of weight **1**. Use a compact slice without boundary, or compactly supported smearings and variations. Sufficient regularity for the displayed derivatives and integrations by parts is assumed. Set the light speed to **1** and normalize the lapse to displacement along the unit geometric normal. No homogeneous or preferred-clock restriction is imposed.

The spatial metric is the spatial restriction of the existing canonical central-sharp metric. It is not a new fundamental field or a replacement readout. The essential conditional input is that, after the physical Lorentz/jet reduction, its phase space is the following canonical cotangent space and admits arbitrary local metric variations. The existing kinematic right inverse alone does not prove this symplectic input for full UBT.

\[
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta,\qquad
\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}\mathbf1,
\qquad h_{ij}=g_{ij},\quad h=\det(h_{ij})>0.
\]
\[
\{h_{ij}(x),\pi^{kl}(y)\}=\delta^k_{(i}\delta^l_{j)}\delta(x-y),
\quad \pi=h_{ij}\pi^{ij},\quad Q=\pi^{ij}\pi_{ij},
\quad \mathcal H=\frac{a}{\sqrt h}(Q-\chi\pi^2)-b\sqrt h\,{}^{(3)}R+c_0\sqrt h.
\]
\[
H[N]=\int N\mathcal H,\qquad
D[\xi]=\int\pi^{ij}\mathcal L_\xi h_{ij}
=-2\int\xi^i h_{ij}\nabla_k\pi^{jk}.
\]

The constants are real, spatially independent comparison coefficients. The ansatz is ultralocal and quadratic in momentum, with only scalar curvature and a constant in the potential. Momentum derivatives, higher curvature, matter, physical torsion, extra fields and noncanonical Dirac brackets are outside this family. Requiring the **off-shell** normalized Lorentzian hypersurface-deformation algebra is an additional selection hypothesis. It has not been derived from the locked Theta kinematics or the information principles. Rescaling the Hamiltonian and lapse together changes a normalization convention; here the geometric lapse normalization is fixed.

<!-- BILINGUAL-UNIT: spatial-dynamics.bracket -->
## Functional bracket before any spatial restriction

The momentum derivative and the derivative-of-lapse part of the curvature variation are

\[
\frac{\delta H[N]}{\delta\pi^{ij}}
=\frac{2aN}{\sqrt h}(\pi_{ij}-\chi\pi h_{ij}),\qquad
\frac{\delta(-b\int N\sqrt h R)}{\delta h_{ij}}
=-b\sqrt h\left[N(\tfrac12h^{ij}R-R^{ij})+\nabla^i\nabla^jN-h^{ij}\Delta N\right].
\]

Here unadorned curvature and covariant derivatives are spatial. All algebraic terms cancel under exchange of the two lapse functions. The kinetic–kinetic bracket cancels pointwise, and the potential–potential bracket vanishes. Contracting the remaining symmetric tensors gives

\[
(\pi_{ij}-\chi\pi h_{ij})(\nabla^i\nabla^jM-h^{ij}\Delta M)
=\pi^{ij}\nabla_i\nabla_jM-(1-2\chi)\pi\Delta M.
\]

Integrate once by parts. Products of first lapse derivatives cancel against the symmetric momentum tensor. The exact result is

\[
\beta^i=h^{ij}(N\partial_jM-M\partial_jN),\qquad
\nabla_i\pi=\sqrt h\,\partial_i(\pi/\sqrt h),
\]
\[
\boxed{\{H[N],H[M]\}=ab\,D[\beta]
+2ab(1-2\chi)\int\beta^i\nabla_i\pi.}
\]

The divergence and trace-gradient terms are independent off shell. At a locally flat metric, momentum with only its transverse diagonal component depending on the first coordinate has zero divergence but a nonconstant trace. Conversely, opposite first and second diagonal components depending on the first coordinate give zero trace and nonzero divergence. The local lapse jets can test each coefficient. Equality to the required momentum generator for arbitrary data therefore holds precisely when

\[
\boxed{ab=1,\qquad\chi=\tfrac12.}
\qquad
\{D[\xi],H[N]\}=H[\mathcal L_\xi N],\qquad
\{D[\xi],D[\zeta]\}=D[[\xi,\zeta]].
\]

The last two identities follow from the canonical momentum map for spatial diffeomorphisms and the scalar-density weight of the Hamiltonian. Together they give the full spatial first-class algebra of this selected metric family. They do not compute the unreduced split-jet, complex-Theta or matter constraint algebra.

A periodic exact witness makes the trace obstruction visible without a boundary term:

\[
h_{ij}=\delta_{ij},\quad \pi^{ij}=\operatorname{diag}(0,\sin x,0),\quad
N=1,\quad M=\sin x,\quad x,y,z\in[0,2\pi],
\]
\[
D[\beta]=0,\qquad
\int\beta^i\nabla_i\pi=(2\pi)^2\int_0^{2\pi}\cos^2x\,dx=4\pi^3.
\]

This tests an off-shell identity; the witness is not asserted to satisfy the Hamiltonian constraint. Homogeneous truncation hides this term. Vanishing brackets only on a restricted constraint surface do not prove the required off-shell structure functions. Alternative second-class or preferred-foliation branches are not excluded: the distinction is explicit in [Bellorín–Restuccia, equations 8–18](https://arxiv.org/pdf/1004.0055). The broader canonical programme is associated with [Hojman–Kuchař–Teitelboim](https://doi.org/10.1016/0003-4916(76)90112-3); no priority is claimed here.

<!-- BILINGUAL-UNIT: spatial-dynamics.evolution -->
## Selected evolution and the remaining free constants

Put the selected ratio into the same Hamiltonian. The complete vacuum metric evolution, before a spatial symmetry restriction, is

\[
\dot h_{ij}=\frac{2aN}{\sqrt h}(\pi_{ij}-\tfrac12\pi h_{ij})+\mathcal L_\xi h_{ij},
\]
\[
\dot\pi^{ij}=-\frac{aN}{\sqrt h}
\left[2\pi^{ik}\pi_k{}^j-\pi\pi^{ij}-\tfrac12h^{ij}(Q-\tfrac12\pi^2)\right]
+b\sqrt h\left[N(\tfrac12h^{ij}R-R^{ij})+\nabla^i\nabla^jN-h^{ij}\Delta N\right]
-\tfrac12c_0N\sqrt h\,h^{ij}+\mathcal L_\xi\pi^{ij},
\qquad\mathcal H=0,\quad\mathcal H_i=-2h_{ij}\nabla_k\pi^{jk}=0.
\]

The Lie derivative of momentum is that of a contravariant density of weight **1**. Lapse and shift are independent local multipliers. If included as canonical coordinates, their momenta vanish and their preservation yields the four displayed secondary constraints. No extra local constraint arises from preserving this closed metric algebra.

For nonzero kinetic coefficient the Legendre map is invertible on the six spatial metric velocities. With the usual boundary prescription it gives

\[
K_{ij}=\frac{\dot h_{ij}-\mathcal L_\xi h_{ij}}{2N},\qquad
\pi^{ij}=\frac{\sqrt h}{a}(K^{ij}-Kh^{ij}),\qquad b=\frac1a,
\]
\[
S_{\rm red}=b\int dt\,d^3x\,N\sqrt h
\left(K_{ij}K^{ij}-K^2+{}^{(3)}R-2\Lambda\right),\qquad
c_0=2b\Lambda,\quad a=2\kappa,\quad b=\frac1{2\kappa}.
\]

This is the Einstein–Lambda effective action under the stated assumptions. The algebra leaves the nonzero Newton normalization and cosmological coefficient free. It does not choose the Holst coefficient, derive a source normalization, or prove that this reduced action comes from the microscopic Theta functional. Positive tensor energy selects the positive normalization branch; it does not determine its magnitude.

<!-- BILINGUAL-UNIT: spatial-dynamics.modes -->
## Two tensor modes and an explicit dynamical solution

For the flat vacuum benchmark set the cosmological coefficient to zero, choose unit background lapse and zero shift, and solve the linearized constraints and gauge conditions. For nonzero spatial wave vector the transverse traceless symmetric subspace has dimension **2**. Its quadratic Hamiltonian and equations are

\[
H^{(2)}_{\rm TT}=\int\left[a\,p^{ij}_{\rm TT}p_{ij}^{\rm TT}
+\frac b4\partial_k\gamma^{ij}_{\rm TT}\partial_k\gamma_{ij}^{\rm TT}\right],\quad
\dot\gamma^{\rm TT}_{ij}=2a p^{\rm TT}_{ij},\quad
\dot p^{ij}_{\rm TT}=\frac b2\Delta\gamma^{ij}_{\rm TT},
\]
\[
\ddot\gamma^{\rm TT}_{ij}=ab\Delta\gamma^{\rm TT}_{ij}=\Delta\gamma^{\rm TT}_{ij},\qquad
\gamma^{\rm TT}=\begin{pmatrix}A&B&0\\B&-A&0\\0&0&0\end{pmatrix}\cos(k(z-t)),\qquad
p^{\rm TT}=\dot\gamma^{\rm TT}/(2a).
\]

Both polarizations have positive nonzero-mode quadratic energy precisely on the branch with positive kinetic and curvature coefficients. The negative conformal direction of the unreduced metric kinetic form is removed by the metric constraints and gauge reduction; it is not an extra tensor polarization. Counting the twelve metric phase-space coordinates and four first-class constraints gives **2** local configuration modes. This flat perturbative result proves neither nonlinear global energy positivity nor stability of additional Theta, imaginary-time, physical-torsion or matter modes. The displayed wave is a linearized solution of this reduced branch, not a newly derived microscopic Theta solution.

<!-- BILINGUAL-UNIT: spatial-dynamics.verification -->
## Verification and exact closure boundary

`tools/verify_spatial_constraint_closure.py` and `tests/test_spatial_constraint_closure.py` check the tensor contractions, all six momentum and metric kinetic derivatives at a non-diagonal rational metric, volume variation, independent bracket coefficients, the periodic obstruction, Legendre inversion and the two-polarization wave. The analytic functional proof above supplies the integration-by-parts and spatial covariance steps.

An independent NumPy implementation computes curvature from Christoffels using Fourier differentiation in all spatial directions. It evaluates the Poisson bracket by central finite differences of the curvature functional along the kinetic Hamiltonian flow, without inserting the analytic curvature-variation formula. Deterministic nonhomogeneous periodic fields use grids of **12** and **20** points in each direction and steps **0.0002** and **0.0001**, including a non-Einstein trace coefficient and a nonunit coefficient product. The absolute acceptance tolerance is **0.000002**. A separate conformal-metric curvature identity tests the numerical curvature implementation.

`formal/lean/UBT/Hamiltonian/SpatialClosure.lean` encodes **6** finite algebraic cores: coefficient selection, trace contraction, inverse kinetic contraction, tensor-wave coefficient, its normalized specialization and nonnegative tensor energy. Their compiled status and exact source hashes are recorded in `reports/full_spatial_dynamics_2026_10_29.json`. No local Lean runtime is available. The continuum functional bracket, reduction to the canonical metric phase space and complete UBT dynamics remain LEAN-PENDING beyond those finite cores.

The [earlier ADM audit](adm_gr_hessian_constraint_audit.en.md) assumed the metric algebra; this calculation derives it within the explicit family. The [bare-action obstruction](physics_closure_bare_action_2026_10.en.md) is not evaded merely by writing this curvature Hamiltonian. The next unresolved bridge is the derivation of this reduced symplectic/action structure and its positive coefficient from the same microscopic Theta theory, with every induced tetrad/connection variation and all additional sectors included. The microscopic action status remains `DEFINED_FAMILY_NOT_FINALIZED`; the effective GR conclusion remains `CONDITIONAL`.
