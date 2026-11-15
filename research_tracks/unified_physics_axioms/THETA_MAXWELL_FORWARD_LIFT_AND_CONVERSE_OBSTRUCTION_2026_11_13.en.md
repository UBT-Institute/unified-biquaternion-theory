<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact conditional flat-background identities and a local composite-tetrad witness; does not establish a fundamental Maxwell/Einstein UBT action.
UBT-AI-PROVENANCE-END
-->

# Source-free Maxwell waves lift to a free Theta wave equation: exact forward bridge, explicit failed converse

**2026-11-13 — C_working.** Continuation of the preferred current work programme, the 2026-11-12 Maxwell–Riemann–Silberstein biquaternion bridge, and the direct relative Theta bivector gate. No canonical axiom or independently propagating gauge field is added.

## 1. Choose one fixed local affine background, not an additional dynamical field

Use faithful Pauli coordinates sigma_0=I, sigma_j standard Pauli, on four *physical* real coordinates (t,x,y,z), c=1, Minkowski signature (-,+,+,+). The canonical W_L=i Herm_2 and sharp metric are unchanged.

Define the reference Theta configuration
\[
\bar\Theta(x)=I+i(tI+x\sigma_1+y\sigma_2+z\sigma_3),\quad
\partial_\mu\bar\Theta=i\sigma_\mu,\quad
\Box\bar\Theta=0.
\]
The background has H_bar=I, and the flat tetrad i sigma_mu, giving a nondegenerate central-sharp Minkowski metric. On a sufficiently small neighbourhood of the origin, barTheta is invertible. It is a fixed local reference configuration for the algebraic construction; it is **not** declared a second fundamental field.

For complex Maxwell Riemann–Silberstein F_j=E_j+i B_j define the traceless biquaternion matrix
\[
\Phi=i\sum_{j=1}^3F_j\,\sigma_j.
\]
For a formal amplitude epsilon, define the ONE complete field
\[
\boxed{\Theta=(I+\epsilon\Phi)\bar\Theta}.
\]
Then the previously studied *relative traceless candidate* is exactly
\[
{\rm tf}(\Theta\bar\Theta^{-1})=\epsilon\Phi,\quad
{\rm tf}(X)=X-\tfrac12{\rm tr}(X)I.
\]
Under a congruence Lorentz transformation of both Theta and barTheta, this relative field transforms by similarity and therefore lies in the complex (anti-)self-dual bivector representation, as verified in prior notes. This does not select the physical interpretation of barTheta, fix global gauge/frame dependence, or derive dynamics.

## 2. First-order Maxwell identity in the Pauli representation

Define the right-acting first-order matrix operator
\[
Q\Phi=-\partial_t\Phi+\sum_{j=1}^3(\partial_j\Phi)\sigma_j.
\]
Using sigma_j sigma_k=delta_jk I+i epsilon_jkl sigma_l, an exact identity is
\[
\boxed{
Q\Phi=i(\nabla\cdot\mathbf F)I+
\bigl(\nabla\times\mathbf F-i\partial_t\mathbf F\bigr)\cdot\boldsymbol\sigma.
}
\]
For real E,B, **Q Phi=0 is equivalent to all four source-free Maxwell equations**:
div E=div B=0, curl E=-partial_t B, curl B=partial_t E.

Let \(P=\partial_t+\sum_j (\partial_j \cdot)\sigma_j\), with the same RIGHT multiplication convention. Then
\[
P Q=-\partial_t^2+\sum_j\partial_j^2=\Box
\]
on every matrix-valued smooth field. Hence Q Phi=0 implies Box Phi=0. This is an exact rewriting of ordinary Maxwell dynamics, not its derivation from UBT.

## 3. The surprising product identity and forward theorem

By the product rule, since barTheta is affine,
\[
\begin{aligned}
\Box\Theta
&=\epsilon\bigl[(\Box\Phi)\bar\Theta+
2(-\partial_t\Phi\,\partial_t\bar\Theta+
\partial_j\Phi\,\partial_j\bar\Theta)\bigr]\\
&=\epsilon\bigl[(\Box\Phi)\bar\Theta+2i Q\Phi\bigr].
\end{aligned}
\]
Therefore
\[
\boxed{Q\Phi=0\ \Longrightarrow\ \Box\Theta=0.}
\]
This is an exact local lifting theorem: ANY sufficiently smooth *source-free Maxwell field* can be packaged into a single Theta obeying the componentwise flat wave equation using the displayed affine background. It is not a claim that the canonical, composite **covariant** operator D†D equals this flat Box, or that the action selects these packaged fields.

**Plane wave checked exactly:** set theta=k(z-t), F=e^{i theta}(1,i,0) and
\[
\Phi=i e^{ik(z-t)}(\sigma_1+i\sigma_2).
\]
Then QPhi=0, BoxPhi=0, and Box[(I+epsilon Phi)barTheta]=0, checked by SymPy without truncating epsilon. Physical real E=Re F and B=Im F are mutually transverse, with k omega.

## 4. Local restoration of the *exact locked UBT tetrad*

Plain \(\partial_\mu\Theta\) for a nonzero plane wave generally leaves W_L. Merely projecting away its Hermitian part is **forbidden** by canonical Axiom C.

Instead reuse the previously studied derived relative **candidate** from
research_tracks/action_selection/full_theta_hermitian_compensator_2026_10.en.md.
Set
\[
H=(\Theta+\Theta^\dagger)/2,\quad
\Omega_\mu=-\tfrac12(\partial_\mu H)H^{-1}
+\tfrac14{\rm tr}(H^{-1}\partial_\mu H)I,\quad
w_\mu=-\tfrac12{\rm tr}(H^{-1}\partial_\mu H),
\]
and define
\[
D_\mu\Theta=\partial_\mu\Theta+\Omega_\mu\Theta+
\Theta\Omega_\mu^\dagger+w_\mu\Theta,\quad
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta.
\]
On every smooth patch with **positive-definite H**, Omega is traceless, w real, and
\[
\partial_\mu H+\Omega_\mu H+H\Omega_\mu^\dagger+w_\mu H=0
\]
holds *exactly*. Thus D_mu Theta is anti-Hermitian, i.e. E_mu∈W_L, and the physical central-sharp metric is real without any artificial projection.

At the coordinate origin, barTheta=I; for the plane wave with epsilon real, H has eigenvalues \(1\pm\epsilon\), hence is positive-definite if |epsilon|<1, and stays so on a sufficiently small patch. Its tetrad is a continuous perturbation of the flat invertible tetrad at epsilon=0, so it remains nondegenerate for sufficiently small epsilon. Independently, a SymPy spot check with \(\epsilon=1/10,k=2,\mathcal N_0=1\) yields
\[
e^a{}_\mu(0)=
\begin{pmatrix}
98/99&0&10/99&0\\
0&100/99&0&0\\
-1/10&0&1&-1/10\\
1/99&0&-10/99&1
\end{pmatrix},
\quad
\boxed{\det e(0)=9800/9801\ne0}.
\]
The full central-sharp metric is Lorentzian and nondegenerate in a neighbourhood; no independent physical gauge field is used.

**Crucial:** the local H-reconstructed Omega is a *selected comparator* satisfying the reality constraint, not yet derived from an action nor proved to be the actual globally equivariant physical spin connection of the metric with a dynamically selected torsion. Its metric/tetrad transport and perturbation equations need independent audit. Also the flat componentwise Box Theta in section 3 is generally **not** the covariant Box_D Theta under this nonzero composite connection.

## 5. Explicit converse counterexample: Theta's free wave equation does NOT select Maxwell

Take the SAME affine barTheta, zero connection, and a nonzero constant anti-Hermitian offset
\[
\Theta=\bar\Theta+i a\sigma_1,\quad a\in\mathbb R\setminus\{0\}.
\]
Then \(\Box\Theta=0\) EXACTLY. Its canonical tetrad remains \(\partial_\mu\Theta=i\sigma_\mu\in W_L\), with exactly the same flat metric.

But the would-be electromagnetic field-strength observable
\[
\Psi={\rm tf}(\Theta\bar\Theta^{-1})
={\rm tf}(i a\sigma_1\bar\Theta^{-1})
\]
does **not** satisfy Maxwell's first-order equation. At the origin,
\[
\boxed{Q\Psi\big|_0=a\sigma_1\ne0}.
\]
This was explicitly verified in SymPy. Therefore the implication
\[
\boxed{\Box\Theta=0\ \not\Longrightarrow\
Q\,{\rm tf}(\Theta\bar\Theta^{-1})=0}
\]
fails, even in a flat and exactly canonical-real-tetrad branch.

The counterexample is a kinematic, single-Theta exact obstruction to claiming Maxwell from the unmodified bare wave equation. It does not exclude a stronger first-order UBT operator, dynamically selected constraints, a local information principle, an altered composite action or another observable map. Inserting QPsi=0 as an axiom would only relabel Maxwell, not derive it.

## 6. Main advance and next decisive computation

**Proved with stated assumptions:** source-free Maxwell solutions admit a local single-Theta lift solving flat BoxTheta=0 and a compatible nondegenerate *candidate composite* Lorentz-real tetrad.

**Disproved in the same restricted model:** bare BoxTheta=0 and a canonical flat tetrad DO NOT force the relative traceless field strength to obey Maxwell. The missing ingredient is a first-order constraint/dynamical selection that removes unwanted scalar/longitudinal modes.

**NEXT GATE:** from a mathematically specified single-Theta action, compute the linearized **composite** Euler–Lagrange operator including delta Omega[Theta], delta w[Theta], principal symbol, primary/secondary constraints and energy; establish (or falsify) that the physical quotient of those equations satisfies the first-order Maxwell right-Weyl equation QPsi=0, with two propagating helicities. This must be done before assigning physical photons to the present lift. Do not add an independent Maxwell action by fiat. Only then test curved null-geodesic propagation and information-based selection.

**Verification:** exact symbolic algebra and 4x4 tetrad arithmetic in local SymPy. Intended regression: tests/test_theta_maxwell_lift_converse_gate.py. No completed UBT dynamics or physical photon has been proved.
