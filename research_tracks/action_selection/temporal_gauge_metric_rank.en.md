<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: temporal-gauge-rank.provenance -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional pointwise rank; not a full UBT dynamical derivation.
UBT-AI-PROVENANCE-END -->
# Pointwise tetrad rank versus functional restrictions of a radial Theta field

**Status: DERIVED_WITH_ASSUMPTIONS; physical on-shell rank OPEN.** This refines, but does not supersede, the canonical metric-rank theorem, the local torsion reconstruction in `canonical/CANONICAL_DEFINITIONS.md`, and merged research on auxiliary connections and FLRW contortion.

## Algebraic realization

Take the canonical Lorentz-real one-connection pair with traceless spin lift. Simultaneously impose a timelike radial Theta and spatial time-gauge tetrad. These are restrictions, not generally two independent Lorentz gauge choices.

\[
D_\mu\Theta=i(\partial_\mu\rho)I+i\rho(\Omega_\mu+\Omega_\mu^\dagger),\qquad \Theta=i\rho I.
\]

The anti-Hermitian rotation part cancels from the derivative of scalar Theta, and the Hermitian boost part gives the spatial coframe columns. Define the coframe and its metric as

\[
E_\mu=\frac{D_\mu\Theta}{\sqrt{\mathcal N_0}},\quad
e_\mu{}^a=
\begin{pmatrix}
u&w_0{}^1&w_0{}^2&w_0{}^3\\
0&w_1{}^1&w_1{}^2&w_1{}^3\\
0&w_2{}^1&w_2{}^2&w_2{}^3\\
0&w_3{}^1&w_3{}^2&w_3{}^3
\end{pmatrix},\quad
u=\frac{\dot\rho}{\sqrt{\mathcal N_0}},\quad g=e\eta e^T.
\]

Here the boost coefficients form the matrix w. At a nondegenerate reference coframe u is unity, the temporal boost row vanishes, and the spatial triad W is the identity.

## Exact pointwise Jacobian

Linearizing at that reference gives

\[
\delta g_{00}=-2\delta u,\qquad
\delta g_{0i}=\delta w_0{}^i,\qquad
\delta g_{ij}=\delta w_i{}^j+\delta w_j{}^i.
\]

For any symmetric metric perturbation h, an explicit tangent-space right inverse is

\[
\delta u=-h_{00}/2,\quad
\delta w_0{}^i=h_{0i},\quad
\delta w_i{}^j=h_{ij}/2.
\]

Consequently the symmetric metric map has exact rank and nullity

\[
\boxed{\operatorname{rank}D_{(u,w)}g=10,\quad\dim\ker D_{(u,w)}g=3.}
\]

The null directions are precisely antisymmetric spatial triad perturbations, geometrically the rotation algebra. This is a pointwise off-shell rank statement, NOT the number of propagating modes.

## Important restriction hidden by that rank

The simultaneous radial form of Theta and temporal tetrad gauge imply

\[
e_i{}^0=0\quad\Rightarrow\quad\partial_i\rho=0\quad\Rightarrow\quad\rho=\rho(t).
\]

For an invertible spatial triad W and temporal boost vector b, define spatial metric gamma and ADM shift beta. Then

\[
\gamma=WW^T,\quad\beta=Wb,\quad
\boxed{N_{\rm ADM}^2=-g_{00}+\beta^T\gamma^{-1}\beta
=u^2=\dot\rho(t)^2/\mathcal N_0.}
\]

Thus the ADM lapse is spatially homogeneous within this **simultaneous** ansatz. The arbitrary spatially varying lapse perturbation cannot be represented as a field perturbation within this family even though every point has full Jacobian rank. The radial gauge has already used boost freedom; imposing tetrad time gauge too is an extra restriction, not a general gauge of the entire theory.

The FLRW minisuperspace itself has a smaller rank, while a separately assumed auxiliary-connection equation that sets every boost coefficient to zero produces a degenerate composite metric and corresponding Jacobian:

\[
\operatorname{rank}D_{(N,a)}g_{\rm FLRW}=2,\qquad
\operatorname{rank}D_{(u,w)}g\big|_{w=0}=1.
\]

The latter statement is specific to the minimal auxiliary-connection assumptions already examined in merged research; it is not the Cartan equation of an established full Theta action.

## Consequence for a Hamiltonian action

This restricted lapse has another exact consequence **if one substitutes it before varying a gravitational action**. For a local ADM action with lapse multiplier and Hamiltonian constraint density \(\mathcal H(x)\), independent lapse variations give the local Hamiltonian constraint. If one replaces the lapse by a function of time only *before varying*, the variation becomes spatially integrated:
\[
\frac{\delta S}{\delta N(t,x)}=0\quad\Rightarrow\quad\mathcal H(t,x)=0,
\qquad
\frac{\delta S|_{N=N(t)}}{\delta N(t)}=0
\quad\Rightarrow\quad\int_\Sigma d^3x\,\mathcal H(t,x)=0.
\]
The converse implication is **false**: cancellation among spatially different constraint densities can satisfy the integral while violating the local equations. Thus early radial/temporal restriction can change the constraint algebra and cannot be used to prove full GR recovery. Moreover, full variation before restriction need not equal restriction before variation. This is an ADM comparator statement, **not** an established Hamiltonian of UBT.

## Dynamical decision gate

The canonical torsion map is algebraically invertible in the specified minimal Palatini setup and its spin source must be derived from the **same composite** Theta action. Free boost variations cannot be counted as physical until the connection, torsion, diffeomorphism and Dirac constraints are imposed. On-shell rank, healthy tensor modes, and the Theta-to-CMB map are open. The existing curved contortion reconstruction proves conditional local geometric realizability, not that its connection satisfies the canonical equations of motion.

**Reproducibility:** `tools/verify_temporal_gauge_metric_rank.py`, `tests/test_temporal_gauge_metric_rank.py`. Run the focused CI before merge; do not change canonical files or assert an observational CMB fit.

**Review criterion:** An actual rank theorem for full UBT must be stated only after the action-derived source for spin and torsion, its complete constraint algebra, and the spatially dependent lapse sector have been analyzed on nondegenerate solutions.
