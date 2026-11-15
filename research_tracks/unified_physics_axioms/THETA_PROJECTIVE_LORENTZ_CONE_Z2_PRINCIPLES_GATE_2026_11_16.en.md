<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact algebraic/topological group identities and finite-matrix diagnostics only; NO fundamental physical dimension count, spin-statistics theorem, Einstein dynamics, QED photon or one-Theta action derived.
UBT-AI-PROVENANCE-END
-->

# Reverse-engineering 3+1 causality and Spin Z2 from the projective biquaternion: a rank and covariance gate

**16 November 2026; L0 exact mathematics, physical identification OPEN.**

This continues INVERSE_FIRST_PRINCIPLES_DEPENDENT_DIMENSIONS_GATE_2026_11_16.en.md and THETA_SPIN_LIFT_PROJECTIVE_OBSERVER_Z2_GATE_2026_11_15.en.md. It examines an underlying mathematical unity of a 2-level observer, Minkowski causal structure and a spin double cover, WITHOUT treating eight real Theta values as eight spacetime dimensions or declaring a global phase a canonical UBT gauge symmetry.

## 1. Exact 8 -> 1+1+3+3 local parameter census

On the invertible field-value stratum Theta in GL(2,C), ordinary matrix polar decomposition is unique:
\[
\boxed{\Theta=HU,\ H=(\Theta\Theta^\dagger)^{1/2}>0,\ U=H^{-1}\Theta\in U(2).}
\]
H has four real parameters, U four. Decompose H into positive overall scale plus the three Bloch coordinates of
\[
\rho={H^2\over \mathrm{tr}(H^2)}
={\Theta\Theta^\dagger\over\mathrm{tr}(\Theta\Theta^\dagger)}
={1\over2}(I+\mathbf r\cdot\sigma),\quad |\mathbf r|<1.
\]
A unitary U has a central U1 phase and three projective SU2/SO3 coordinates. Hence (locally)
\[
\boxed{8=1_{\rm scale}+1_{\rm center\ phase}
+3_{\rm observer\ density}+3_{\rm relative\ unitary}.}
\]
All four entries of Theta remain one complex biquaternion. No eight-dimensional spacetime has been obtained.

If one makes a MATHEMATICAL quotient by all nonzero complex scalars, the resulting manifold is
\[
\boxed{PGL(2,\mathbb C)=GL(2,\mathbb C)/\mathbb C^\times
\simeq B^3\times PU(2)\simeq B^3\times SO(3).}
\]
It has six real dimensions. This is a diffeomorphism of manifolds (not an assertion that the product law factors into an independent boost group and rotation group). Crucially, the canonical physical W_L tetrad need not be invariant under Theta -> complex scalar times Theta. Thus this quotient is not yet a quotient by physical UBT gauge and does NOT establish six physical propagating modes.

For a single N=I normalized observer readout, the tangent Jacobian of Theta -> rho has generic real rank 3 and kernel dimension 5. At Theta=I with Theta=I+epsilon Phi and Phi=sum_j(a_j+i b_j)sigma_j, the exact first derivative is
\[
\delta\rho=\sum_{j=1}^3 a_j\sigma_j.
\]
The five invisible infinitesimal directions are the scale, center phase and three unitary rotations. Other observers/relative transport can recover some of them; they must not automatically be declared gauge.

## 2. PGL(2,C) IS the proper connected Lorentz group as an abstract Lie group

For invertible Q define its action on Hermitian 2x2 matrices X by
\[
\boxed{\Lambda_Q(X)={QXQ^\dagger\over|\det Q|}.}
\]
This is a homomorphism under Q multiplication, is unchanged under Q -> c Q (c nonzero complex), preserves Hermiticity and the future positive cone, and obeys
\[
\det\Lambda_Q(X)=\det X.
\]
On X=x^0 I+x^j sigma_j, \(\det X=(x^0)^2-|\mathbf x|^2\).
The resulting map is the familiar isomorphism
\[
\boxed{PGL(2,\mathbb C)\cong PSL(2,\mathbb C)\cong SO^+(1,3)}
\]
and has the standard double cover SL(2,C) -> SO^+(1,3) with kernel +/-I. The group-theoretic identification by itself does NOT make an arbitrary projective Theta value into the physical gravitational tetrad or spin frame. That requires a Lorentz-equivariant soldering map selected from the ONE Theta action.

## 3. Positive two-level quantum records and the future Minkowski cone

For a Hermitian matrix
\[
X=x^0 I+\mathbf x\cdot\sigma,
\quad \mathrm{spec}(X)=x^0\pm|\mathbf x|,
\]
one has the EXACT equivalence
\[
\boxed{X\ge0\quad\Leftrightarrow\quad x^0\ge|\mathbf x|}.
\]
Thus the convex cone of unnormalised positive qubit states is, as a cone, precisely the 3+1-dimensional Minkowski **future causal cone**. Null X correspond to rank-one pure rays, interior X to positive definite mixed states. For nonzero X, the section \(\operatorname{tr}X=1\) is the Bloch ball:
\[
\rho=X/\mathrm{tr}X
=\frac12(I+\mathbf r\cdot\sigma),\quad\mathbf r=\mathbf x/x^0.
\]
This is a standard algebraic two-spinor/Lorentz-cone fact, not a new physical emergence result. It is a compelling REVERSE-ENGINEERING BRIDGE: if a minimal complex two-level positive operational record is dynamically selected, it carries a natural 3+1 causal cone without inserting the Minkowski determinant by hand.

**Critical UBT caveat:** for the N=I matrix K=Theta Theta†, when the full fundamental Theta transforms in the canonical geometric congruence \(\Theta'=S\Theta S^\dagger\), then
\[
K'=S\Theta(S^\dagger S)\Theta^\dagger S^\dagger,
\]
which generally differs from SKS† for nonunitary Lorentz boosts. Hence the *algebraic* cone identification cannot by itself equate the current observer density with the canonical spacetime Lorentz-vector field. A physically selected observer clock N or a different derived intertwinement is needed; see THETA_SPIN_LIFT_PROJECTIVE_OBSERVER_Z2_GATE_2026_11_15.en.md.

## 4. Exact noncontractible projective loop and Z2 holonomy, with no local photon

Consider the exact **closed** GL2(C) loop
\[
\Theta(\varphi)=\begin{pmatrix}e^{i\varphi}&0\\0&1\end{pmatrix},
\quad0\le\varphi\le2\pi.
\]
Its projective class [Theta] is a loop in PGL2(C). A normalized determinant-one lift is
\[
S(\varphi)=e^{-i\varphi/2}\Theta(\varphi)
=\begin{pmatrix}e^{i\varphi/2}&0\\0&e^{-i\varphi/2}\end{pmatrix},
\]
which satisfies
\[
\boxed{S(0)=I,\qquad S(2\pi)=-I.}
\]
Hence the projective loop represents the nontrivial element of the Spin double-cover Z2. The determinant map on fundamental groups supplies the general proof: GL2(C) retracts to U2, pi1(GL2C)=Z; the center inclusion C* -> GL2C sends winding n to 2n because det(c I)=c²; therefore
\[
\boxed{\pi_1(PGL(2,\mathbb C))\cong \mathbb Z/2\mathbb Z.}
\]

The globally well-defined 1-form on invertible matrices
\[
a_{\det}=\tfrac12\mathrm{Im}\,\mathrm{tr}(\Theta^{-1}d\Theta)
=\tfrac12d\arg\det\Theta
\]
is locally FLAT, \(da_{\det}=0\), but along the displayed loop
\[
\boxed{\oint a_{\det}=\pi,\qquad
\exp(i\oint a_{\det})=-1}.
\]
For an ordinary closed scalar re-representation Theta -> c(phi) Theta with integer phase winding n, the integral changes only by 2pi n, so the sign is projective-representative-independent. A double loop has trivial +1 sign. This is a flat TOPOLOGICAL Z2 loop character, NOT Maxwell curvature, not a propagating photon, and not a proof of fermionic CAR or 2-particle exchange statistics. It is also not the path-dependent Berry phase of a generic CP1 ray: the two must remain distinct.

## 5. The decisive CANONICAL GR covariance obstruction

The mathematical group law on PGL2(C) uses Q -> SQ as a left frame action. The current canonical geometric Theta often transforms under local Lorentz changes by **CONGRUENCE**, Theta -> STheta S†. These are not the same action on Theta values.

For instance take Theta=I and a non-central SU2 rotation S=i sigma3. Congruence leaves Theta fixed, while left multiplication takes it to S!=cI. Hence its projective class has a nontrivial SU2 stabilizer under congruence, but an actual Lorentz-frame torsor has a free left action. No equivariant identification of this entire congruence stratum with a left-translation frame torsor can exist without extra data/representation changes.

This is a sharper version of the previous -I spinor no-go: PGL topology supplies a *candidate* universal Spin double cover, but the canonical physical transformation law does not automatically USE that cover as a physical spin-frame lift. The same issue blocks directly identifying the three invisible unitary parameters with independent electric gauge variables.

## 6. Falsifiable principle programme, not an ad hoc new axiom

Reverse engineering suggests a MINIMAL set of independent candidate requirements, each tested rather than imposed to reproduce a sector:
- **Operational positivity/composition:** recover an observer-state cone, not yet identify it with the spacetime cone; establish proper multi-observer compatibility.
- **Causal Lorentz compatibility:** prove the physical sharp tetrad and observer cone have the same causal characteristics, including local boosts, *without replacing* E=DTheta/sqrt(N0).
- **Dependent dimensions/physical quotient:** derive the actual gauge constraints, Jacobian ranks and Frobenius integrability; do not call any of the 8 Theta values additional physical coordinates.
- **Spin lift + graded quantization:** explain how a spin structure and a physical CAR net emerge without a one-valued tensor-to-Weyl map, and distinguish Z2 holonomy from fermionic exchange.
- **Single positive Hamiltonian:** select the dynamical reduction and symplectic constraints from a single Theta action, not an independent GR+QED action; detect whether an internal U1 curvature has two healthy photon helicities.
- **IR validation:** recover QED/Maxwell, Einstein GR and anomaly-free chiral SM with explicit derivation maps and falsifiable coupling predictions.

These conditions are not proven to be the unique or sufficient fundamental principles. The topological Z2 and Lorentz cone are genuine mathematical facts, but no microscopic Theta action or QED photon follows from them alone.

**Verification:** 12 targeted SymPy/pytest checks passed locally on 2026-11-16. Regression: tests/test_theta_projective_spin_topology_gate.py. They test finite-matrix identities, quotient tangent rank, spin-cover loops, phase winding invariance, cone determinant and canonical-congruence mismatch. The topology of pi1(PGL) follows the standard homotopy exact-sequence argument and is not proven by finite symbolic tests.
