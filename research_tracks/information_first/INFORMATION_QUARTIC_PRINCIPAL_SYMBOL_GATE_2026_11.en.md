<!-- BILINGUAL-UNIT: information-hessian.scope -->
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

# Information-first UBT: quartic-potential pullback and fixed-coframe principal-symbol obstruction

**2026-11-08 · C_working · PROVED conditional algebraic identities and a necessary-sign obstruction; physical action selection OPEN.** English is the translation source. This does not introduce a new fundamental field, selected Hamiltonian, colour dynamics or multiverse.

<!-- BILINGUAL-UNIT: information-hessian.context -->
## Reuse of previous UBT results and exact scope

The previous work established (i) the full-Theta Lorentz-plus-phase polynomial potential basis through quartic order, (ii) the derived-H graded representative quotient with a complete finite differential inverse, and (iii) the observer-density/Fisher and moving-colour/multiplex diagnostics. Here we test the same **single full complex biquaternion** and the same potential basis, not a new axiom. Freeze the composite Minkowski coframe e=identity and physical omega, and restrict to a regular normalized-positive-H representative chart. This is a fixed-geometry **principal-symbol gate**, not a complete constrained gravitational perturbation analysis. English is the translation source.

\[
\mathcal H(\Theta)=\operatorname{Tr}(\Theta^\sharp\Theta^\dagger),\quad
\mathcal D(\Theta)=|\det\Theta|^2,\quad
\mathcal J(\Theta)=\mathcal D(\Theta)-\tfrac14\mathcal H(\Theta)^2,
\]
\[
V(\Theta)=m^2\mathcal H+\lambda_1\mathcal H^2
+\lambda_2\mathcal D,\qquad
\lambda_1,\lambda_2,m^2\in\mathbb R.
\]

<!-- BILINGUAL-UNIT: information-hessian.pullback -->
## The algebraic full-Theta potential becomes a derivative functional of a representative label [PROVED]

Reuse exactly the existing finite differential inverse h=2s sqrt(r/k), Y=(h/2s)e^{-1}dr, and X=hY. The Lorentz connection A is reconstructed algebraically (with derivatives of these fields) so that e is constant; it has NO independent contribution to the tested potential. In the normalized-H frame the existing Pauli identity gives J=4h² times the spatial norm of x. The following formulas hold for every sufficiently smooth timelike representative label r on a common regular chart; the gradient must remain timelike and nonzero. This is not a new independent scalar postulate, because r is the old norm Y². The spatial sum uses the fixed normalized-H frame of this chart, not a universal Lorentz-invariant split into time and space.

\[
\Theta=hI_2+X,\quad
X=i(x^0I_2-x^j\sigma_j),\quad
Y=X/h,\quad r=Y^aY_a<0,
\]
\[
s=\sqrt{\mathcal N_0}>0,\quad
k=\eta^{\mu\nu}\partial_\mu r\,\partial_\nu r<0,\quad
h^2=\frac{4s^2r}{k},\quad
x^a=\frac{h^2}{2s}e^{a\mu}\partial_\mu r,\quad
e_\mu{}^a=\delta_\mu{}^a,
\]
\[
\mathcal H=2(h^2-x^a x_a)=2h^2(1-r)
=\frac{8s^2r(1-r)}{k},
\]
\[
\boxed{\mathcal J=4h^2\sum_{i=1}^3(x^i)^2
=\frac{h^6}{s^2}|\nabla r|^2
=64s^4\frac{r^3|\nabla r|^2}{k^3}.}
\]

<!-- BILINGUAL-UNIT: information-hessian.reduced -->
## Explicit trial Lagrangian for the vertical representative label [PROVED identity]

Assume for this diagnostic only a gravity-only base action plus a separately specified potential contribution -V(Theta). Once the exact inverse eliminates h,Y,A in favour of fixed e and the label r, the base gravity action is constant along r and the potential becomes the exact first-derivative expression below. Thus a pointwise potential in the microscopic full-Theta variables can appear derivative-dependent in the holonomic quotient coordinate. This is a differential field change; a real Hamiltonian proof must restore all original constraints, boundary terms and allowed variations, and must never infer new propagating degrees of freedom from the substitution alone.

\[
u=\partial_t r,\quad \mathbf v=\nabla r,\quad
k=-u^2+|\mathbf v|^2,\quad
A=8s^2r(1-r),\quad
\beta=\lambda_1+\frac{\lambda_2}{4},
\]
\[
\boxed{\mathcal L_{\mathrm{vert}}
=-V=-m^2\frac{A}{k}
-\beta\frac{A^2}{k^2}
-64\lambda_2s^4\frac{r^3|\mathbf v|^2}{k^3}.}
\]

<!-- BILINGUAL-UNIT: information-hessian.sign -->
## Exact homogeneous-gradient principal-symbol sign obstruction [PROVED, restricted]

At a regular fixed-coframe background with r<0, u=partial_t r nonzero and spatial gradient zero, calculate the exact second derivatives of -V with respect to the time derivative and any spatial derivative of the vertical label. With metric convention (-,+,+,+), a regular unconstrained scalar mode would require positive Ktt and negative Kxx in this foliation. The exact mass-independent identity below contradicts this pair when the quartic coefficients are nonnegative: both desired inequalities would make Ktt-3Kxx positive, whereas the identity is nonpositive. Even with both quartic coefficients zero, equality prevents strict healthy signs. The quadratic mass coefficient m² cancels exactly. This is **not** a theorem that the full UBT has a ghost: the chosen background is not proved on-shell for the augmented action and the label might be removed by its full Dirac constraints.

\[
K_{tt}:=\left.\frac{\partial^2\mathcal L_{\mathrm{vert}}}
{\partial u^2}\right|_{\mathbf v=0}
=\frac{6m^2A}{u^4}-\frac{20\beta A^2}{u^6},
\]
\[
K_{ij}:=\left.\frac{\partial^2\mathcal L_{\mathrm{vert}}}
{\partial v_i\partial v_j}\right|_{\mathbf v=0}
=\left(\frac{2m^2A}{u^4}
-\frac{4\beta A^2}{u^6}
+\frac{128\lambda_2s^4r^3}{u^6}\right)\delta_{ij},
\]
\[
\boxed{K_{tt}-3K_{xx}
=-\frac{128s^4r^2}{u^6}
\left[4\lambda_1(1-r)^2+\lambda_2(1+r+r^2)\right]\le0}
\quad(\lambda_1,\lambda_2\ge0),
\]
\[
1+r+r^2=(r+\tfrac12)^2+\tfrac34>0.
\]

<!-- BILINGUAL-UNIT: information-hessian.bounded -->
## Why nonnegative quartic coefficients are the relevant stability screen [PROVED rays]

The independent classified quartic basis is H² and |det Theta|². Taking lambda1<0, or separately lambda2<0, produces an explicit full complex-Theta ray along which the quartic potential goes to minus infinity. Thus lambda1,lambda2>=0 are necessary for the quartic polynomial to be globally bounded below. The displayed two matrices certify the necessity independently; they do NOT claim that arbitrary lower-order choices plus a nonnegative quartic automatically give a globally stable complete field theory. There may be more complicated stabilizing terms beyond quartic order, additional constrained domains or independent derivative invariants; they are outside this gate.

\[
M_1=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
\mathcal H(tM_1)=-t^2,\quad \mathcal D(tM_1)=0,\quad
V_4(tM_1)=\lambda_1t^4,
\]
\[
M_2=\operatorname{diag}(1,i),\quad
\mathcal H(tM_2)=0,\quad \mathcal D(tM_2)=t^4,\quad
V_4(tM_2)=\lambda_2t^4,\qquad t\in\mathbb R.
\]

<!-- BILINGUAL-UNIT: information-hessian.tilt -->
## The J-only proposal: instantaneous rest branch and wrong-sign time coefficient after tilt [PROVED]

The previously proposed information-sensitive trial V=lambda J has no quadratic time derivative at a homogeneous label background, although its spatial-gradient Hessian is positive. For any tilted timelike label gradient, J itself has strictly positive second derivative with respect to the chosen time derivative; hence the Lagrangian contribution -lambda J has negative fixed-time kinetic coefficient for lambda>0. For lambda<0 the homogeneous spatial-gradient term instead has the wrong sign. These are principal-coefficient tests within the stated chart, not a gauge-invariant physical Hamiltonian signature. They show why the earlier positive potential Hessian in the three constant boost parameters did NOT establish a healthy propagating mode.

\[
\left.\frac{\partial^2\mathcal J}{\partial u^2}\right|_{\mathbf v=0}=0,\qquad
\left.\frac{\partial^2\mathcal J}{\partial v_i\partial v_j}
\right|_{\mathbf v=0}=-\frac{128s^4r^3}{u^6}\delta_{ij}>0,
\]
\[
\frac{\partial^2\mathcal J}{\partial u^2}
=\frac{384s^4r^3|\mathbf v|^2
(|\mathbf v|^2+7u^2)}
{(|\mathbf v|^2-u^2)^5}>0
\quad(r<0,\ k<0,\ |\mathbf v|>0),
\]
\[
(r,u,|\mathbf v|,s)=(-1,-2,1,1)
\quad\Longrightarrow\quad
\frac{\partial^2\mathcal J}{\partial u^2}=\frac{3712}{81}.
\]

<!-- BILINGUAL-UNIT: information-hessian.integrability -->
## Pointwise Bloch surjectivity does not imply three independent spatial channels [PROVED conditional]

Earlier information-first work showed that at a single event, the three Gaussian-boost parameters can sweep the complete interior qubit Bloch ball. But in the exact derived-H inverse the three spatial carrier components are derivatives of ONE smooth representative scalar r. With the fixed geometric observer clock N=I2, Pauli multiplication gives the local density and Bloch vector shown below. The scalar multiplier f may vary in space; nevertheless the Frobenius/helicity identity is EXACT. A vector field with nonzero helicity density, exemplified below, cannot be reconstructed as this chosen Bloch readout on any regular open neighborhood where its expression applies.

\[
Q=\Theta\Theta^\dagger=
\left(h^2+(x^0)^2+|\mathbf x|^2\right)I_2
-2x^0\mathbf x\cdot\boldsymbol\sigma,
\quad \mathbf x=\frac{h^2}{2s}\nabla r,
\]
\[
\rho_{N=I_2}=\tfrac12(I_2+\boldsymbol{\beta}_{\rm obs}\cdot\boldsymbol\sigma),
\quad
\boxed{\boldsymbol{\beta}_{\rm obs}
=-\frac{2x^0}{h^2+(x^0)^2+|\mathbf x|^2}
\frac{h^2}{2s}\nabla r=f\nabla r},
\]
\[
\boxed{\boldsymbol{\beta}_{\rm obs}\cdot
(\nabla\times\boldsymbol{\beta}_{\rm obs})=0},\qquad
\boldsymbol{\beta}_{\rm forbidden}(x,y,z)=\tfrac14(-y,x,1),\quad
\boldsymbol{\beta}_{\rm forbidden}\cdot
(\nabla\times\boldsymbol{\beta}_{\rm forbidden})=\tfrac18\ne0,\quad
|\boldsymbol{\beta}_{\rm forbidden}|<1\text{ when }|x|,|y|\le1.
\]

This pointwise-versus-field distinction is an integrability obstruction, not a universal QCD no-go. It applies only to this normalized-H representative chart and fixed observer clock; a varying detector frame, other physically derived internal connections or a different microscopic phase space could invalidate the stated restricted ansatz. The three values of the Bloch vector are NOT three independent propagating quark colours or three independent multiverse multiplex channels.

<!-- BILINGUAL-UNIT: information-hessian.implication -->
## Consequence for colour, information and psi multiplex [OPEN physics]

This single-field potential-only candidate does not furnish a healthy regular vertical scalar principal operator on every homogeneous timelike background under the nonnegative-quartic condition. The displayed four-dimensional pullback has no independent psi derivative, so it does not generate a stabilizing winding kinetic term on a compact psi fiber. Nor does it supply a local colour SU(3) connection, eight gluon poles, a calibrated physical decoder, or another spacetime. The viable follow-up is to derive allowed independent derivative invariants and a single source action, then compute the full coupled fixed-time Dirac constraint and symplectic reduction. A nonzero chosen Fisher information does not repair this missing dynamics.

\[
\lambda_1,\lambda_2\ge0
\quad\Longrightarrow\quad
\neg(K_{tt}>0\ \wedge\ K_{xx}<0)
\quad\text{on the specified homogeneous timelike label background},
\]
\[
\mathcal L_{\rm grav}(e,\omega)
+\mathcal L_{\rm vert}(r,\partial r)
\ \not\Rightarrow\
\text{a selected physical colour/multiplex Hamiltonian}.
\]

<!-- BILINGUAL-UNIT: information-hessian.tests -->
## Verification, provenance and reuse

Fourteen local SymPy tests check generic full-matrix Pauli invariants, exact holonomic pullback, recovery of the known affine-boost Gaussian representative, general fixed-coframe Hessian, cancellation of m², independent instability rays for negative quartic coefficients, the degenerate homogeneous J branch, a tilted wrong-sign kinetic witness, and the psi limitation. Bilingual structural and independent semantic validation remain mandatory GitHub gates; this is C_working and no Tier-A attestation is changed. Reused, not claimed anew: research_tracks/action_selection/theta_potential_invariants.en.md; derived_h_graded_representative_quotient_2026_11.en.md; research_tracks/information_first/THETA_COLOUR_MULTIPLEX_SELECTION_GATE_2026_11.en.md; and the merged information tomography. No continuum Lean formalization, on-shell model, physical measurement theory or full gravitational Dirac theorem is claimed.
