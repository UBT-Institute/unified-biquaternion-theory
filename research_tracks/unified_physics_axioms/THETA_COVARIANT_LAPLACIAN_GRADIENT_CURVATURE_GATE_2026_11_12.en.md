# Covariant Laplacian-gradient curvature gate for UBT

**Status:** rigorous conditional operator identities and local kinematic witnesses; NO final Theta-only dynamics. Date: 2026-11-12.

## 1. Canonical constraints and dimensions

Locked geometry: E_mu=N0^(-1/2) D_mu Theta; g_mu_nu 1=(E_mu^sharp E_nu+E_nu^sharp E_mu)/2. Classical slice W_L={i t 1+x^j e_j}, with sharp the quaternion conjugation, fixing central complex i. Paired derivative D_mu X=partial_mu X+A_mu X-X B_mu; commutator is [D_mu,D_nu]X=F^A_mu_nu X-X F^B_mu_nu. Pure Lorentz spin connection is not automatically an independent U(1) connection.

Coordinate bookkeeping: canonical/fields/theta_field.tex explicitly states tau=z^0=t+i psi within q=z^mu e_mu, so 8 real coordinates for full q already include t and psi. Adding another 2 for tau without an independent extra variable double-counts. The current locked metric is 4D; a compact psi fiber exists in the active version, but no full nondegenerate 5D or 10D canonical metric/action has been proved. Do not conflate Theta's eight real *value* components with domain dimensions.

The existing first-jet gravitational restrictions are conditional: bare metric-locked kinetic density is exactly 2 N0 sqrt(|g|) in 4D (canonical/gr_closure/gap_10d_theta_hessian_principal_symbol.tex), and the frozen-connection Lorentz-real flat linearization produces only pure-gauge h_mu_nu (research_tracks/action_selection/linearized_flat_theta_pure_gauge_no_go.en.md). Neither proves a no-go for all composite UBT dynamics.

## 2. Direct response: gradient of the covariant Laplacian

On a torsion-free spacetime with metric-compatible connection on Theta's bundle, let Box_E act on Theta, Box_(T* tensor E) on bundle-valued one-forms, and let the induced curvature endomorphism be script_F_mu_nu=[D_mu,D_nu]. The Laplacian-gradient commutator obeys, with standard Ricci sign convention,

Box_(T* tensor E)(D_mu Theta)-D_mu(Box_E Theta)
= Ric_mu^nu D_nu Theta + 2 script_F^nu_mu D_nu Theta + (D^nu script_F_nu_mu) Theta.

The last terms are operator actions on Theta. Curvature convention may reverse the Ricci sign. Torsion gives additional terms and must be audited with canonical contortion.

A lone D_mu Box Theta is third order; if Box Theta=J is on shell, it gives D_mu J, not a new independent field equation. The commutator cancels the leading third derivatives, making the curvature explicit. If Theta is a trivial scalar with zero internal curvature, this commutator reads only Ricci and cannot detect Schwarzschild's Ricci-flat Weyl curvature. Retain the two-index curvature operator and its action on tetrads to detect full gravity.

## 3. Pauli/biquaternion square: exact constant-B example

With constant Pauli matrices sigma_i and a connection commuting with them (or a covariantly constant Clifford action), let P_plus=D_t+sum_i sigma_i D_i, P_minus=D_t-sum_i sigma_i D_i. An exact identity is

P_plus P_minus =
D_t^2 - sum_i D_i^2
+ sum_i sigma_i [D_i,D_t]
- (i/2) epsilon_ijk sigma_k [D_i,D_j].

For a constant B field choose (as a **test**, not a derived UBT gauge potential)
D_t=partial_t, D_x=partial_x, D_y=partial_y+i q B x, D_z=partial_z.
Then [D_x,D_y]=i q B and

P_plus P_minus = D_t^2-D_x^2-D_y^2-D_z^2+q B sigma_z.

This was checked by SymPy on a two-component polynomial field. The B term survives even though B is constant. This exhibits the relation between a second-order wave/Laplacian operator and connection curvature, with no derivative of B required. In full UBT, verify the Pauli/connection compatibility: the raw quaternion-valued left/right connection may not commute with constant sigma_i.

## 4. A genuine Theta-coefficient composite: nonzero constant curvature

For a selected complex coefficient column chi=(Theta_0,Theta_1,Theta_2,Theta_3)^T on a patch with chi^dagger chi>0, let u=chi/sqrt(chi^dagger chi). The Berry-like candidate is a=-i u^dagger du and f=da=-i du^dagger wedge du. Unlike a pure-phase d alpha, f is not identically zero. Locally, with p(x)=1/2+B L x in 0<p<1,

u=(sqrt(1-p), sqrt(p) exp(i y/L),0,0)^T,
a=p(x)/L dy, f=B dx wedge dy.

Thus an explicit Theta-coefficient *texture* admits a smooth constant nonzero two-form. However: (i) this selected positive norm/projective quotient is not yet proved Lorentz-equivariant or consistent with the sharp/W_L metric; (ii) this u by itself does not generate a full nondegenerate canonical tetrad; (iii) f=O((delta u)^2) around a constant u background, so a linearized photon does **not** appear there. This is a kinematic possibility, not a QED derivation.

## 5. Higher-dimensional geometric possibility and rank gate

The compact psi fiber suggests a *research-only* Kaluza-Klein-type metric
ds5^2=g_mu_nu dx^mu dx^nu + Phi^2(d psi + kappa a_mu dx^mu)^2.
Its off-diagonal connection would have curvature da; Phi is a radion, **not** automatically the Standard Model Higgs. But extending the SAME real Lorentz slice W_L and sharp Gram formula to 5 tangent vectors E_A is impossible for a nondegenerate 5D metric: G_AB=e_A^a eta_ab e_B^b, with e a 5x4 matrix, hence rank(G)<=4. Any 5D realization must enlarge the real carrier or derive a distinct fiber metric without silently altering the canonical 4D lock.

## 6. Dynamic gate and falsifiers

1. Compute A_mu[Theta] and B_mu[Theta] from an *actually selected* composite connection/torsion law; vary these along with Theta in the single action.
2. Compute kinetic Hessian, principal symbol, constraints, positive energy; check two photon and two graviton helicities, scalar mode spectrum, and absence of ghosts.
3. Derive physical EM curvature and Maxwell equations from the same action, including linearized nonzero field strengths and constant B configurations.
4. Prove that geometric optics has characteristic cone g^mu_nu k_mu k_nu=0 and transports light on null geodesics.
5. Do not mistake algebraic factorization or a Berry curvature witness for a fully derived UBT dynamical sector.

**Verdict:** The proposed covariant gradient of the Theta Laplacian points to a genuine curvature-sensitive operator; the more basic source of the curvature is noncommutativity of D_mu, visible directly in the factorized first-order operator. Dynamics remains open.