<!-- BILINGUAL-UNIT: c5.scope -->
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

# Independent complex tau: geometry and action tests

Date: 2026-10-08. Status: **DERIVED_WITH_ASSUMPTIONS / OPEN_GAP**. This author-requested research alternative keeps an independent complex tau in addition to complex spacetime. It does not replace the canonical time choice, central metric, single-field architecture, or action registry. The source baseline is commit `2102540b0beb06d3abe707ba941c2a46cae394b9`.

The main result is a separation of three questions: a fifth Clifford direction removes a specific rank defect; an exact completed coframe remains flat; and a dynamical embedding or auxiliary-jet construction needs its own complete variation. The continuation below proves a restricted auxiliary-action obstruction, not a no-go for all UBT.

<!-- BILINGUAL-UNIT: c5.domain -->
## Domain and conventions

\[
Z^A=(z^0,z^1,z^2,z^3,\tau)\in\mathbb C^5,
\quad z^\mu=x^\mu+i y^\mu,\quad \tau=s+i\psi,
\quad \Theta:\mathbb C^5\longrightarrow\mathbb C\otimes\mathbb H\simeq\mathbb C^4.
\]

All ten real coordinate parameters are independent. Tau is not identified with the first spacetime coordinate. Holomorphy is an additional assumption, used only when stated. The field-value dimension and the coordinate dimension differ. Quaternion conjugation sharp does not conjugate complex coefficients; in the matrix representation it is the adjugate. Its determinant polarization is the fixed nondegenerate complex bilinear form B. Units and the fixed global jet normalization are absorbed into the displayed fields. Physical cosmological and variational tests below explicitly choose a real Lorentzian model; they do not settle the physical interpretation of all ten parameters.

<!-- BILINGUAL-UNIT: c5.rank -->
## Rank and the fifth Clifford direction [L1]

For five covariant derivatives with values in the same four-dimensional complex carrier,

\[
g^{(0)}_{AB}=B(E_A,E_B)=JQJ^T,
\qquad \mathrm{rank}_{\mathbb C}g^{(0)}\leq4.
\]

This follows from the rectangular size of J and does not assume ordinary derivatives. It is a rank defect of this unchanged prescription, not an objection to the canonical four-dimensional tetrad-to-metric rank theorem.

The existing Clifford lift supplies

\[
\mathcal C(E)=\begin{pmatrix}0&E\\E^\sharp&0\end{pmatrix},
\qquad \Gamma_*=\mathrm{diag}(I_2,-I_2),
\qquad \widetilde\Gamma_A=\mathcal C(E_A)+u_A\Gamma_*.
\]
\[
\tfrac12\{\widetilde\Gamma_A,\widetilde\Gamma_B\}
=\bigl[B(E_A,E_B)+u_Au_B\bigr]I_4.
\]

If the first four derivatives form a basis and the fifth form is chosen as below, the Schur complement gives

\[
g_5=g^{(0)}+u\otimes u,\quad u=\lambda d\tau,
\qquad \det g_5=\lambda^2\det g_4\ne0.
\]

The form u and its normalization are extra input in this alternative; their dynamical origin is not proved. The fifth Clifford matrix already exists in the repository and is not a new discovery here.

<!-- BILINGUAL-UNIT: c5.signature -->
## Spinors, reality and string comparison

A five-complex-direction Clifford module can use four complex components. A full ten-dimensional complex Dirac module has 32 components; a Weyl module has 16 complex components, and the Majorana–Weyl module in Lorentz signature has 16 real components. A biquaternion alone is therefore not the full ten-dimensional Lorentz spinor. Solving the linear anticommutation constraints for matrices of the same size, the symbolic checker finds only the zero matrix for all five chosen generators together.

The real part of a nondegenerate complex symmetric metric has real signature (5,5): multiplication by the complex unit reverses its sign. A Hermitian signature (p,q) instead becomes (2p,2q). A real signature (1,9) requires another reality/metric prescription; a Lorentzian five-dimensional real model is a separate choice.

The critical RNS superstring dimension follows from its worldsheet anomaly balance,

\[
c_{\mathrm{total}}=D+D/2-26+11=\tfrac32D-15,
\qquad c_{\mathrm{total}}=0\Longrightarrow D=10.
\]

UBT has not supplied the required worldsheet theory, fermions, spectrum or anomaly cancellation [S1, S2]. Fourier momentum modes on a circle do not alone supply the independent string winding term. The zero-mode expression and its duality are only comparison tests:

\[
\frac{n^2}{R^2}+\frac{w^2R^2}{\alpha'^2},
\qquad R\leftrightarrow\alpha'/R,\quad n\leftrightarrow w.
\]

If tau parametrized a worldsheet instead, its parameters could not also be counted as extra target-space coordinates.

<!-- BILINGUAL-UNIT: c5.flat -->
## Exact coframe: flatness and a null action [L1]

Assume ordinary derivatives, constant B and nonzero constant lambda. For holomorphic fields, or for the corresponding real model, define

\[
Y=(\Theta^0,\Theta^1,\Theta^2,\Theta^3,\lambda\tau),
\qquad g_5=Y^*\eta_5,\quad \eta_5=\mathrm{diag}(-1,1,1,1,1).
\]

Nondegeneracy makes the square Jacobian invertible. Y are then local coordinates with constant metric, so the complete Riemann tensor vanishes. A nonconstant coordinate connection does not change that conclusion. A factor depending only on tau can also be integrated into the last coordinate. This is the extension of the repository's existing gradient-flatness result [U1], not a claim about arbitrary covariant derivatives.

On an oriented real patch, choose the orientation-preserving Jacobian branch. With compactly supported variations and a potential depending only on field values and tau, test the explicit composite functional

\[
S_{\mathrm{test}}=\mathcal T\int d^5Z\sqrt{|g_5|}
\left[\tfrac12 g_5^{AB}B(\partial_A\Theta,\partial_B\Theta)-V(\Theta,\tau)\right].
\]

The same pairing in the metric and kinetic term gives

\[
g_5^{AB}u_Au_B=1,\qquad
g_5^{AB}B(\partial_A\Theta,\partial_B\Theta)=4.
\]

Thus the density is a Jacobian times the field-value function below. It is a pullback of a fixed top-degree form. Its variation is an exact form by Cartan's formula and integrates to zero:

\[
F=2-V,\qquad S_{\mathrm{test}}=\mathcal T\int Y^*(F\,d^5Y),
\qquad \delta S_{\mathrm{test}}=0.
\]

Here the argument of F is understood after the coordinate substitution. The claim concerns local bulk variation on a fixed orientation branch, not a zero action value, singular Jacobians, global sectors or boundary dynamics. The checker verifies the Piola identity for general functions and a nonconstant potential. Varying the kinetic term while incorrectly holding its composite metric fixed misses this cancellation.

<!-- BILINGUAL-UNIT: c5.embedding -->
## FLRW geometry and embedding variation [L1]

For a positive scale factor with nonzero derivative, use a flat real ambient metric and the local embedding [S3]

\[
ds_5^2=-dU\,dV+d\mathbf X^2,\quad
U=a(t),\quad \mathbf X=a(t)\mathbf x,\quad
V=a(t)|\mathbf x|^2+f(t),\quad \dot f=1/\dot a.
\]

Its pullback is the spatially flat FLRW metric. Time and a have length units here; comoving coordinates are dimensionless. The spacelike unit normal and the second fundamental form, with the displayed sign convention, are

\[
n=(\dot a,\dot a|\mathbf x|^2-1/\dot a,\dot a\mathbf x),
\quad K_{\mu\nu}=n\cdot\partial_\mu\partial_\nu Y,
\quad K_{00}=\ddot a/\dot a,\quad K_{ij}=-a\dot a\delta_{ij},\quad K_{0i}=0.
\]

Gauss's equation yields curved intrinsic geometry even though the ambient curvature vanishes. A vanishing derivative of a invalidates this chart, not every possible embedding.

Now additionally assume the Einstein–Hilbert plus covariant matter functional on the induced metric. It is a conditional effective candidate, not a second fundamental UBT action. Compact support or the appropriate boundary terms are required. Varying Y, including the induced metric variation, gives [S4]

\[
\mathcal E^{\mu\nu}=G^{\mu\nu}-\kappa T^{\mu\nu},\qquad
\nabla_\mu(\mathcal E^{\mu\nu}\partial_\nu Y^I)=0,
\qquad \mathcal E^{\mu\nu}K_{\mu\nu}=0.
\]

The last equation uses matter conservation and the Bianchi identity. With a single normal it is weaker than the full Einstein equations. The repository's split-jet Palatini construction uses a different, surjective class of variations [U2]; this embedding obstruction does not invalidate that conditional result.

<!-- BILINGUAL-UNIT: c5.cosmology -->
## Conditional cosmological discriminator [L1]

Define the Einstein residual and assume conserved ordinary matter:

\[
H=\dot a/a,\quad \rho_X=3H^2/\kappa-\rho,
\quad p_X=(-2\dot H-3H^2)/\kappa-p,
\quad \dot\rho+3H(\rho+p)=0.
\]

The residual also obeys continuity. The normal equation and its first integral are

\[
\rho_X\ddot a/\dot a-3Hp_X=0,
\quad \frac{d}{dt}(a^3\dot a\rho_X)=0,
\quad \boxed{a^4H\rho_X=C},
\quad \boxed{3H^3-\kappa\rho(a)H-\kappa C/a^4=0}.
\]

This is the known Regge–Teitelboim integral [S5], reproduced for the chosen embedding. C is initial-data input, not a predicted constant. On an expanding branch its sign is the sign of the residual. Squaring the density relation loses that sign and must be supplemented with the unsquared equation. The branch with zero C and nonzero H recovers the Friedmann equations. A direct counterexample to automatic Einstein dynamics is

\[
\rho=p=0,\quad a(t)=a_*[(t-t_0)/t_*]^{3/4},\quad t>t_0,
\qquad G_{00}=\frac{27}{16(t-t_0)^2}\ne0,
\quad p_X/\rho_X=-1/9.
\]

It solves the embedding equation, but not the vacuum Einstein equation. Near the Einstein branch, a dominant conserved constant-w fluid gives the following first-order scaling in C:

\[
|\rho_X|\ll\rho,\quad H>0,\quad
\rho_X\simeq C/(a^4H_{\mathrm{GR}})\propto a^{-(5-3w)/2},
\quad w_X\simeq-(1+3w)/6.
\]

| Dominant fluid | Residual scaling | Residual pressure ratio |
|---|---|---|
| Radiation | a⁻² | −1/3 |
| Dust | a⁻⁵ᐟ² | −1/6 |
| Vacuum energy | a⁻⁴ | +1/3 |

The powers refer to a dimensionless scale-factor ratio. They are not valid when the correction dominates. This does not establish cold dark matter, accelerated expansion, or perturbative stability.

<!-- BILINGUAL-UNIT: c5.other -->
## Other retained limits

If ten-dimensional Einstein dynamics is separately assumed for the flat unwarped product with external and internal scale factors, the direct tensor calculation gives

\[
ds_{10}^2=-dt^2+a^2d\mathbf x_3^2+b^2d\mathbf y_6^2,
\quad H=\dot a/a,\quad S=\dot b/b,
\quad G_{00}=3H^2+18HS+15S^2.
\]
\[
G_{ii}/a^2=-2\dot H-3H^2-6\dot S-21S^2-12HS,
\quad G_{mm}/b^2=-3\dot H-6H^2-5\dot S-15S^2-15HS.
\]

Static internal dimensions require the following pressure condition, with vacuum contributions included in the total stress tensor:

\[
\rho-3p+2p_I=0.
\]

Internal curvature, warping, time dependence and other sources change this restricted test. It is not an action derivation or a stabilization mechanism [S6].

There is also a conditional complex-time obstruction. Holomorphic continuation of an autonomous unitary group with self-adjoint generator on a positive Hilbert space, together with ordinary nonzero real-period periodicity of the individual state in imaginary time, gives

\[
\Psi(s+i\psi)=e^{-isK}e^{\psi K}\Psi_0,
\quad (e^{LK}-1)\Psi_0=0,
\quad L\in\mathbb R\setminus\{0\}
\Longrightarrow \Psi_0\in\ker K.
\]

Analytic continuation must exist on that state. The implication follows from the real spectral theorem. Thermal correlation periodicity is a different condition. Noncompact continuation with the opposite imaginary sign can damp positive-generator modes, but does not derive a minimum length, energy quantization or the fine-structure constant.

<!-- BILINGUAL-UNIT: c5.continuation -->
## Continuation and canonical boundary

The complete next calculation is in [the auxiliary-action test](auxiliary_action.en.md): an explicit non-null split-jet candidate realizes arbitrary coframes, but the self-contracted kinetic family forces a critical zero-volume coefficient and has no derivative term in its quadratic bulk action there.

This narrows that candidate only. The finalized microscopic action, a derivative-dependent composite connection, its full Hessian and physical constraint quotient remain open. The action registry [U3] still takes precedence over older strong claims. No unconditional GR, string equivalence, alpha prediction or complete quantum theory is registered here. Existing canonical status labels are unchanged; the local machine-readable ledger records this scope.

The [wave-dynamics continuation](wave_dynamics.en.md) now tests a derivative-dependent composite family and the transverse complex fluctuations of the existing flat symplectic candidate. Both remain locally degenerate under their stated assumptions. It also separates a conditional hyperbolic dispersion relation from the unresolved derivation of that physical operator and examines the additional-time signature problem.

<!-- BILINGUAL-UNIT: c5.verification -->
## Verification

`verify_c5.py` checks 51 exact identities. `verify_c5_dynamics.py` checks 32 exact identities, including full tensor components, Piola cancellation and the FLRW first integral. `verify_auxiliary_action.py` checks 22 identities using SymPy and an independent Python Fraction implementation. `verify_wave_dynamics.py` adds 21 checks using the same two tool classes with separate implementations. Each script writes its named result JSON beside itself. Versions and limitations are recorded in those outputs and `status.json`; tests run the same derivations on temporary copies to avoid overwriting tracked evidence.

**LEAN-PENDING:** Lean and Lake executables were unavailable in the execution runtime; the generic rank, spectral and differential-geometric statements have not been formalized here. Analytic proofs accompany the identities; finite symbolic or rational checks do not establish complete physics, stability, empirical agreement or human review. The earlier gradient and split-jet results are explicitly credited [U1, U2, U4]. English was the translation source for this repository edition. Structural parity is machine checked; human semantic-equivalence review remains required before merge.

<!-- BILINGUAL-UNIT: c5.sources -->
## Sources

- [U1] [Existing gradient-flatness and volume result](../../canonical/gr_closure/gap_10t_composite_flat_admissibility.tex).
- [U2] [Split-jet Palatini variational lift](../action_selection/split_jet_palatii_variational_lift.en.md).
- [U3] [Single-action registry](../../canonical/ACTION.en.md).
- [U4] [Existing full fixed/value-dependent connection variation](../action_selection/biquaternionic_induced_gravity_boundary.en.md).
- [S1] David Tong, [String Theory](https://www.damtp.cam.ac.uk/user/tong/string/string.pdf).
- [S2] Antoine Van Proeyen, [Tools for supersymmetry](https://arxiv.org/abs/hep-th/9910030).
- [S3] Sheykin and Paston, [Friedmann cosmology in Regge–Teitelboim gravity](https://arxiv.org/abs/1511.09268).
- [S4] Paston and Sheykin, [Embedding theory as new geometrical mimetic gravity](https://doi.org/10.1140/epjc/s10052-018-6474-9).
- [S5] Paston and Sheykin, [From the Embedding Theory to General Relativity in a result of inflation](https://arxiv.org/abs/1106.5212).
- [S6] Das, Haque and Underwood, [Constraints and Horizons for de Sitter with Extra Dimensions](https://arxiv.org/abs/1905.05864).
