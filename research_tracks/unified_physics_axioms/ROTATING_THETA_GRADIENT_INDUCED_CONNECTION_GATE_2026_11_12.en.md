# Rotating biquaternion gradients: induced connection, a curved witness, and the 4D rank obstruction

**Date:** 2026-11-12  
**Status:** exact differential-geometric derivation for the toy immersion; its realization in the locked physical UBT metric remains **OPEN**. This note proposes no axiom change or final gravitational dynamics.

## 1. The idea worth testing

Let a smooth map Theta be valued in a vector space equipped with a fixed nondegenerate real bilinear pairing <.,.>. Let E_mu=partial_mu Theta and define an induced metric g_mu_nu=<E_mu,E_nu>, restricted to a patch where g is nondegenerate.

Differentiate g and use the symmetry of second partial derivatives to obtain the exact formula

Gamma^rho_mu_nu
= g^{rho sigma} <partial_mu partial_nu Theta, partial_sigma Theta>.

Thus **the Levi-Civita connection is computable from the first and second jets of Theta**. The changing orientation of tangent vectors E_mu can produce a nontrivial intrinsic connection and Riemann curvature, even though partial_mu partial_nu Theta commute. With a flat ambient pairing, the intrinsic curvature obeys Gauss's equation
R_mu_nu_rho_sigma
= <B_mu_rho,B_nu_sigma> - <B_mu_sigma,B_nu_rho>,
where B_mu_nu is the component of partial_mu partial_nu Theta perpendicular to the tangent span (up to conventional index/sign ordering). The essential criterion is the existence of genuinely *normal* variations of E_mu, not the mere noncommutativity of quaternion basis elements.

## 2. Exact real-quaternion sphere witness (2D toy, NOT 4D gravity)

For real imaginary quaternion units e_i, define
Theta(theta,phi)=R[sin(theta)cos(phi)e_1+sin(theta)sin(phi)e_2+cos(theta)e_3].
Using quaternion conjugation sharp and the real scalar pairing
g_ab=Sc((partial_a Theta)^sharp partial_b Theta), we get
g_theta theta=R^2,
g_phi phi=R^2 sin^2(theta),
g_theta phi=0.

Consequently Gamma^theta_phi phi=-sin(theta)cos(theta),
Gamma^phi_theta phi=cot(theta),
and Gaussian curvature K=1/R^2.
This confirms that a gradient *of a multicomponent quaternion field*, by itself, may reconstruct nonzero connection and curvature **when the target space has a normal direction relative to the lower-dimensional immersed domain**. SymPy verifies the metric, Christoffels and curvature.

## 3. Why this does not overturn the existing 4D pure-gradient no-go

Locked 4D UBT has E_mu=N0^{-1/2}D_mu Theta in the fixed real 4D Lorentz slice W_L={it 1+x^j e_j}; the sharp Gram metric is real and central without a trace or Re projection.

If D_mu=partial_mu and all E_mu lie in this *fixed* W_L, then integration gives locally Theta=Theta_constant+sqrt(N0)Y^a(x)u_a with real Y^a and constant Lorentz basis u_a. Whenever the 4x4 Jacobian partial_mu Y^a is nondegenerate, Y^a are local coordinates. The 4D metric is exactly the pullback of flat Minkowski and Riemann curvature vanishes. In 2D the sphere construction has ambient dimension 3 and domain dimension 2; its tangent vectors have an extra normal direction, so this obstruction does not apply. Quaternionic multiplication E_mu E_nu being noncommutative alone does NOT imply curvature: constant noncommuting basis gradients can yield flat geometry.

To exploit Theta's full eight-real-dimensional coefficient space in a 4D immersion, one would need a real nondegenerate physical bilinear on the relevant tangent 4-plane compatible with canonical sharp and local Lorentz symmetry. Simply taking Re of a complex Gram form or silently abandoning W_L changes the locked physical metric and cannot be called a canonical UBT derivation. Alternatively retain W_L and derive a nontrivial **composite connection** D_mu Theta, including torsion/relative left-right contributions, whose first jet is not a pure-coordinate gradient. The full coupled implicit system and action-level dynamics remain open.

## 4. Independent connection and gauge ambiguities

If one obtains a matrix orientation U(x) and sets omega=U^{-1}dU, the Maurer–Cartan equation gives d omega+omega wedge omega=0. **A rotating frame is not by itself nonzero curvature**. A nonflat projection (such as a Berry connection with nonzero curvature), a genuine curved embedding, or a nonholonomic composite connection is needed. Check transformation laws and whether the projection is physically selected rather than imposed.

## 5. Next canonical gate

Without redefining the locked metric, calculate E_mu=N0^{-1/2}[partial_mu Theta+A_mu[Theta]Theta-Theta B_mu[Theta]] for a physically admissible 4D background, derive Gamma[e], R[e] and its complete linearized response including delta A and delta B; then test the full Theta Hessian, gauge constraints, spin-2 propagation, energy signs, and light-cone characteristics. Do not infer dynamics solely from the curved 2D immersion.

**Verdict:** The user's proposed rotating Theta gradient **can** reconstruct a connection and nonzero induced curvature in mathematically controlled settings. Whether the canonical 4D Theta field has the required normal/geometric freedom or composite connection and dynamics remains a sharp open question.