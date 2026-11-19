<!-- BILINGUAL-UNIT: gr-fixed-carrier-volume-no-go-2026-11-17 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional exact local theorem; fundamental single-Theta action still open.
UBT-AI-PROVENANCE-END
-->
# Conditional volume-only no-go with unrestricted auxiliary contortion

<!-- UNIT: scope -->
## Exact hypothesis and relation to earlier work
This is an exact **local conditional** obstruction: the affine flat field does not extremize the metric-locked kinetic volume when contortion is varied over all smooth metric-compatible auxiliary choices obeying the single-Theta vector-jet equation. It is not a no-go for a genuine dynamically selected K[Theta], generic eight-real biquaternions, added Theta potential, quantum effective action or a non-volume gravitational term. No independent fundamental field is proposed. Compare the already known stabilizer ambiguity in research_tracks/action_selection/exact_stabilizer_torsion_ambiguity.en.md and canonical/gr_closure/gap_10i_torsionful_local_representer.tex.

<!-- UNIT: theorem -->
## Exact necessary-and-sufficient coframe realization theorem

Let \(s=\sqrt{\mathcal N_0}\), \(X=X^a u_a\in W_L\), \(X^2=\eta_{ab}X^aX^b\ne0\), and
\[
e_\mu{}^a=s^{-1}(\partial_\mu X^a+\omega_\mu{}^a{}_bX^b),\quad
\omega=\mathring\omega(e)+K,\quad\omega_{\mu ab}=-\omega_{\mu ba}.
\]
Metric: \(g_{\mu\nu}=\eta_{ab}e_\mu{}^ae_\nu{}^b\).
**Local coframe criterion:** a smooth nondegenerate e can be represented with some metric-compatible omega if and only if
\[
\boxed{X_a e_\mu{}^a=(2s)^{-1}\partial_\mu(X^2).} \tag{1}
\]
Necessity follows from \(X\cdot(\omega X)=0\). For sufficiency define
\[
Y_\mu{}^a=s e_\mu{}^a-\partial_\mu X^a-\mathring\omega_\mu{}^a{}_b(e)X^b
\quad (X_aY_\mu{}^a=0),
\]
\[
\boxed{K_\mu{}^a{}_b=(Y_\mu{}^aX_b-X^aY_{\mu b})/X^2.} \tag{2}
\]
Then K is Lorentz antisymmetric and KX=Y, hence (1) is sufficient. Any additional stabilizer form CX=0 changes torsion without changing e. This is an existing geometric ambiguity, not a physical gauge theorem.


<!-- UNIT: witness -->
## Explicit compactly supported nonstationarity witness

On a patch \(U\) where \(X^2<0\), start with \(X^a=sx^a\), \(e_\mu{}^a(0)=\delta_\mu^a\), \(K=0\). For smooth compactly supported f with nonzero integral put
\[
P^a{}_b=\delta^a_b-X^aX_b/X^2,\qquad
e_\mu{}^a(\varepsilon)=\delta_\mu^a+\varepsilon f(x)P^a{}_\mu.
\]
Then \(P^2=P\), \(\mathrm{tr}P=3\), \(XP=0\), and (1) is satisfied for every small epsilon. Equation (2) gives an **exact** smooth K realizing e(epsilon); the perturbed coframe stays invertible. Since \(P\) has eigenvalues (0,1,1,1),
\[
\det(e_\mu{}^a(\varepsilon))=(1+\varepsilon f)^3.
\]
The metric-locked quadratic Lorentz-invariant Theta kinetic term obeys
\[
S_{\rm kin}=2\mathcal N_0\int\det(e)\,d^4x,\qquad
\left.\frac{d}{d\varepsilon}\left[S_{\rm kin}(\varepsilon)-S_{\rm kin}(0)\right]\right|_0
=\boxed{6\mathcal N_0\int_U f\,d^4x\ne0}. \tag{3}
\]
The subtracted action is finite. Fixed X=sx leaves no nonzero infinitesimal coordinate transformation that fixes the carrier, and proper local Lorentz transformations preserve det e, so this deformation is not either such gauge transformation.


<!-- UNIT: meaning -->
## Physical conclusion and immediate fork
The local affine flat background is not a stationary point of the **pure locked kinetic volume** on this enlarged auxiliary-K constraint manifold. The arbitrary admissible coframe has 16 minus 4 = 12 local slots at fixed nonnull X; the connection has further stabilizer ambiguity, already documented. Neither number counts physical propagating DOF. No implication is made that this enlarged space equals the full single-Theta physical solution space. The previously studied strict gradient branch E=dX has a null-Lagrangian Jacobian volume and is a *different* constrained variation.

Thus either derive a constitutive, covariance-respecting K[Theta] selector that excludes this witness and admits healthy curved solutions, or derive a physically motivated non-volume action from Theta. The algebraic curvature invariant and parameter redundancies do not themselves fix this choice. The full constrained multiplier system in the paired document is the appropriate equation framework for a specified action, but it cannot select the action.

<!-- UNIT: verify -->
## Verification
Exact symbolic checks: tools/verify_gr_fixed_carrier_volume_no_go_2026_11_17.py (projector, determinant, Lorentz-antisymmetric K right inverse, norm compatibility). The smooth connection existence uses Levi-Civita(e) for nondegenerate coframes and the pointwise right inverse; no assumption on invertibility of A=I-J_E. Full CI, independent bilingual review, Lean, off-slice and on-shell composite Hamiltonian checks pending. Research only, no canonical promotion.
