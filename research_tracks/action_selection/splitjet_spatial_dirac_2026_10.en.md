<!-- BILINGUAL-UNIT: splitjet-dirac.scope -->
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

# Local Dirac reduction of the gravity-only split-jet parent

**2026-10-29; C_working; CONDITIONAL.** English is the translation source. The [full spatial metric calculation](full_spatial_dynamics_2026_10.en.md) assumed a canonical reduced metric phase space. This note resolves the additional jet part of that assumption for the already chosen gravity-only action: its auxiliary extension preserves the base Dirac brackets and adds no local physical mode. It does not select the base action from microscopic Theta dynamics.

<!-- BILINGUAL-UNIT: splitjet-dirac.assumptions -->
## Domain and independent variables

Use smooth fields on a regular non-null internal-vector chart, a nondegenerate Lorentz tetrad, fixed positive normalization, and a compact spatial slice without boundary or compactly supported variations. The local constraint ranks and the base symplectic quotient must be regular. The metric remains the canonical central-sharp metric. The base action is supplied, has no explicit dependence on the redundant carrier or jet kernel, and admits a first-order constrained Hamiltonian representation. The chosen spinless Palatini–HT gravity action is the intended base; its ordinary connection, Lorentz, simplicity and HT reductions remain base operations, not new results here.

\[
s=\sqrt{\mathcal N_0}>0,\quad X^2=\eta_{ab}X^aX^b\ne0,\quad
Q_\mu=K_{J\mu}X+w_\mu X,\quad
sE_\mu=\partial_\mu X+\omega_\mu X+Q_\mu.
\]

The vector notation is the Lorentz-real gravity carrier of the declared two-sided derivative, not a replacement field algebra or a choice of the fundamental number of Theta components. The physical curvature uses the independent variational Lorentz connection, while the jet correction is separate. The remaining complex-Theta, imaginary-time and matter sectors are not removed by restricting this calculation to the gravity functional.

<!-- BILINGUAL-UNIT: splitjet-dirac.coordinates -->
## Adapted jet coordinates and the required momentum shift

The existing rank theorem gives local adapted coordinates consisting of the image and the stabilizer. The stabilizer has dimension **3** for each spacetime index, hence **12** in total. This is a local point transformation with a carrier-dependent frame. Its full cotangent lift is

\[
k_\mu=(K_{J\mu},w_\mu)=k_\mu(X,u_\mu),\quad u_\mu=(Q_\mu,z_\mu),
\]
\[
P_X=p_X+\sum_\mu (\partial_X k_\mu)^T p_{k_\mu},\qquad
P_{u_\mu}=(\partial_{u_\mu}k_\mu)^T p_{k_\mu},
\]
\[
p_X\,\delta X+\sum_\mu p_{k_\mu}\,\delta k_\mu
=P_X\,\delta X+\sum_\mu P_{u_\mu}\,\delta u_\mu.
\]

One must not identify the bare carrier momentum with the adapted one off the constraint surface. All constraint momenta below are in the adapted canonical chart. The corrections from all spacetime columns add to the same carrier momentum.

A concrete smooth chart on the future timelike component uses the following Lorentz boost. The rest-frame matrix has arbitrary spatial antisymmetric components, which are the kernel coordinates.

\[
r=\sqrt{(X^0)^2-\sum_i(X^i)^2}>0,\quad X^0>0,\quad
L^0{}_0=X^0/r,\quad L^0{}_i=L^i{}_0=X^i/r,\quad
L^i{}_j=\delta^i_j+\frac{X^iX^j}{r(X^0+r)},
\]
\[
q=L^{-1}Q,\quad w=q^0/r,\quad
R^0{}_i=R^i{}_0=q^i/r,\quad R^i{}_j=-R^j{}_i,\quad K_J=LRL^{-1}.
\]

Then the image is recovered exactly and the auxiliary chart is invertible. The explicit test point and its derivatives retain transverse carrier variations; the carrier is not frozen to its rest axis. Other non-null charts need their own smooth stabilizer frame. No continuation through the null locus is claimed.

<!-- BILINGUAL-UNIT: splitjet-dirac.parent -->
## Equivalent first-order parent

Let the supplied base functional depend on the tetrad, physical connection and its own auxiliary variables. Introduce the following parent solely as an exact constrained rewrite:

\[
S_{\rm P}=S_0[E,\omega,\ldots]
+\int d^4x\,\lambda^\mu{}_a
\left(sE_\mu^a-\partial_\mu X^a-\omega_\mu{}^a{}_bX^b-Q_\mu^a\right).
\]

The multiplier is a vector density. Eliminating its constraint recovers the original composed gravity functional. Conversely, variation of the free image variables sets every multiplier to zero, and the base equations remain. Thus the independently varied tetrad in this parent is a rewrite variable, not an added fundamental physical field. The stabilizer coordinates are absent from the action. No jet kinetic or matter term is added.

Temporal carrier dependence produces the primary momentum relation. The spatial relations contain full spatial derivatives; they are not homogeneous constraints.

\[
p_{Xa}+\lambda^0{}_a=0,\qquad P_{Q_\mu a}=0,\qquad
P_{\lambda^\mu a}=0,\qquad P_{z^I}=0,
\]
\[
F_i=sE_i-\partial_iX-\omega_iX,\qquad
\lambda^i=0,\qquad Q_i-F_i=0.
\]

The last two equations follow by preserving the spatial primary constraints. One may eliminate the temporal pair, then the spatial multiplier pairs and the spatial image pairs. The original constraint matrix has nonzero mixed temporal/spatial entries; it must not be assumed block diagonal before this sequential reduction.

<!-- BILINGUAL-UNIT: splitjet-dirac.graph -->
## Why the physical Dirac bracket is unchanged

For any graph pair and any base-dependent function, including functions with spatial derivatives, write the constraint matrix and its exact inverse as

\[
\chi=(P_Q,Q-F),\qquad B_{IJ}=\{F_I,F_J\},\qquad
C=\begin{pmatrix}0&-I\\I&B\end{pmatrix},\qquad
C^{-1}=\begin{pmatrix}B&I\\-I&0\end{pmatrix}.
\]

No assumption that the image function commutes with base variables is used. A retained observable independent of the eliminated pair has zero bracket with its auxiliary momentum. The inverse's lower diagonal block therefore makes the entire Dirac correction vanish between any two retained observables. The result applies successively to the temporal multiplier graph, spatial multiplier graphs and spatial image graphs. For field theory, the matrix notation denotes kernels smeared on the stated domain; derivative couplings are retained. There is no inverse spatial differential equation or Green function in this auxiliary elimination.

After the second-class reduction, the canonical potential and Hamiltonian are

\[
\vartheta_{\rm red}=\vartheta_0+\int
\left(p_X\,\delta X+P_{Q_0}\,\delta Q_0+P_z\,\delta z\right),
\]
\[
H_{\rm red}=H_0+\int p_X\cdot(sE_0-\omega_0X-Q_0),\qquad
\dot P_{Q_0}=p_X,\qquad \dot p_X=\omega_0^Tp_X.
\]

The temporal image momentum and carrier momentum are first class, as are all stabilizer momenta. The supplied base constraint algebra is unchanged on their quotient: mixed contributions to base-constraint preservation are proportional to these extra constraints. This statement allows the base itself to have second-class constraints; it does not replace the Palatini simplicity reduction with a guessed metric bracket. In particular, the Lorentz connection response has not been frozen.

<!-- BILINGUAL-UNIT: splitjet-dirac.count -->
## Gauge generator, regular quotient and mode count

The carrier shift and compensating jet shift have the following generator on the remaining carrier/image coordinates:

\[
G[\varepsilon]=\int\left[\varepsilon\cdot p_X
-(\dot\varepsilon+\omega_0\varepsilon)\cdot P_{Q_0}\right],\qquad
\delta X=\varepsilon,\quad\delta Q_\mu=-D_\mu\varepsilon,\quad
\delta E=\delta\omega=0.
\]

The spatial image shifts are recovered from their eliminated graph equations. Use only shifts whose finite path stays within the chosen chart. If the temporal connection is included among canonical coordinates, its conjugate momentum receives terms proportional to the auxiliary primary constraint because the generator's coefficient is field dependent. These terms vanish on the quotient; they are not an extra physical spin source. Stabilizer shifts are generated by their adapted momenta. On the extra constraint surface the canonical potential is exactly the base potential, and on a regular local quotient all the additional fibre directions are removed.

| Added configuration coordinates | Count | Second-class constraints | First-class constraints |
|---|---:|---:|---:|
| Temporal carrier, image and multiplier | 12 | 8 | 8 |
| Spatial images and multipliers | 24 | 48 | 0 |
| Stabilizer coordinates | 12 | 0 | 12 |
| Total | 48 | 56 | 20 |

\[
\Delta\dim\Gamma_{\rm physical}=2(48)-56-2(20)=0.
\]

These are additions relative to the base phase space. They must not be added again to the base graviton count. For the supplied regular spinless Einstein branch, its **2** local tensor modes are preserved. A global HT integration datum is not counted as a new local mode. This is stronger than a mechanical analogue or an inclusion of presymplectic kernels, but remains a gravity-only result. It does not prove that all complex Theta directions are gauge, that additional matter couplings preserve this quotient, or that the microscopic action has positive energy.

<!-- BILINGUAL-UNIT: splitjet-dirac.verification -->
## Verification and the remaining microscopic obligation

`tools/verify_splitjet_spatial_dirac.py` checks the graph inverse with nonzero internal brackets, the unreordered **56**-constraint matrix with mixed temporal/spatial entries, temporal preservation and gauge chains, and an exact carrier-dependent cotangent map. Omitting the carrier-momentum shift gives an explicit failure. The shared-carrier test includes all spacetime columns. `tests/test_splitjet_spatial_dirac.py` preserves these cases.

An independent NumPy/SciPy implementation uses a periodic **3**-by-**3**-by-**3** grid, hence **27** spatial cells, and **4** internal real gravity coordinates. It constructs all spatial image-constraint gradients, including derivatives in all directions and variations of the physical connection, and numerically inverts their **648**-constraint matrix. Retained observables include coframe, connection and carrier momenta. The graph derivative is checked independently by central differences with step **0.00001** and tolerance **0.00000001**. The inverse tolerance is **0.00000000001** and the physical Dirac-correction tolerance is **0.0000000001**. This grid tests the spatial graph block; the other chains have the separate exact checks above.

`formal/lean/UBT/Hamiltonian/SplitJetDirac.lean` supplies **6** finite cores: both graph-inverse products over an arbitrary ring, zero graph correction, dimension cancellation, additive vertical invariance and the radial cotangent identity. The report `reports/splitjet_spatial_dirac_2026_10_29.json` binds source hashes, tool versions and compiled status. There is no local Lean runtime. The full continuum Dirac theorem and the base gravity reduction remain LEAN-PENDING as formalizations beyond those cores.

Derivative-dependent rewrites require an invertibility or constraint argument; they are not automatically harmless. The related general problem is treated by [Takahashi–Motohashi–Suyama–Kobayashi](https://arxiv.org/pdf/1702.01849). Here the explicit parent constraints supply the argument for this particular non-null gravity sector. The earlier [finite configuration quotient](mm_finite_splitjet_lift.en.md) and [presymplectic calculation](mm_composite_presymplectic_variation.en.md) are premises, not new discoveries. The curvature action, positive Newton normalization, full matter/complex-time coupling, and null/global/horizon continuation are still open microscopic obligations. The fundamental-action status remains `DEFINED_FAMILY_NOT_FINALIZED`; the gravity result remains `CONDITIONAL`.
