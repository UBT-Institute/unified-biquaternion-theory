<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: flat-gradient-dirac.provenance -->
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

# Exact Dirac constraints of the pure-gradient composite-tetrad branch

**Status: DERIVED_WITH_ASSUMPTIONS / OPEN_GAP for full UBT.**
**Purpose:** Go beyond the boundary-action identity of open PR #680 by performing a complete local canonical constraint classification of **that restricted action**, not a separate UBT action. This does not assume a final UBT Hamiltonian, cosmology, or CMB detection.

## 1. Clearly stated assumptions

Use canonical \(\Theta\in\mathbb C\otimes\mathbb H\), composite tetrad \(E_\mu=N_0^{-1/2}D_\mu\Theta\) and central anticommutator metric. On a simply connected Lorentz-real local patch, impose **all** restrictions:
- The full two-sided connection is locally gauge-trivial and represented by \(D_\mu=\partial_\mu\) on this branch.
- \(\Theta=\Theta_\star+i\sqrt{N_0}(y^0I+y^j\sigma_j)\), where \(y^a(x)\) are 4 real functions.
- The Jacobian \(J_\mu{}^a=\partial_\mu y^a\) is invertible, with fixed positive orientation \(\det J>0\). Thus \(g=y^*\eta\) is locally flat and \(\sqrt{-g}=\det J\).
- Restrict variations to the \(y^a\) subspace **before** varying, with no independent metric/connection variations, no curvature or YM kinetic action and a derivative-free real potential \(U(\Theta(y))\).
- For the canonical discussion take a spatial slice \(\Sigma\) compact without boundary, or boundary conditions annihilating all spatial surface terms. All statements are local in field space; a globally exact generator need not exist for nontrivial topology.

Under these assumptions the *restriction of the already-declared kinetic/potential family* is
\[
S_{\rm red}=\int dt\,d^3x\, F(y)\det J,\qquad F(y)=4cN_0-U(\Theta(y)).
\]
This is the restricted density identified by PR #680, not a fundamental canonical action. The coefficient \(c\) and \(U\) are inputs.

## 2. Exact velocity Hessian and primary constraints

Use coordinate order \(x^0=t,x^1,x^2,x^3\). Define the spatial cofactors
\[
M_a(y)=\frac1{3!}\epsilon_{abcd}\epsilon^{ijk}
(\partial_i y^b)(\partial_j y^c)(\partial_k y^d),\qquad
\epsilon_{0123}=\epsilon^{123}=+1.
\]
Because the determinant is multilinear in its rows,
\[
\det J = \dot y^a M_a,\qquad
M_a\partial_i y^a=0\quad(i=1,2,3).
\]
The momenta and velocity Hessian are **exactly**
\[
\boxed{\pi_a=\frac{\partial\mathcal L_{\rm red}}{\partial\dot y^a}
=F(y)M_a,\quad
W^{\rm velocity}_{ab}=\frac{\partial\pi_a}{\partial\dot y^b}=0.}
\]
Therefore **all 4** phase-space constraints
\[
\boxed{\phi_a(x)=\pi_a(x)-F(y(x))M_a(x)\approx0}
\]
are primary. The bulk Legendre transform is
\[
\mathcal H_c=\pi_a\dot y^a-F(y)\dot y^a M_a=0,
\qquad H_T=\int_\Sigma d^3x\,\lambda^a\phi_a
\]
up to explicit boundary contributions.

## 3. An exact generating functional and Poisson closure

Define \(G(y)\) locally by \(\partial G/\partial y^0=F(y)\), for example
\[
G(y)=\int_0^{y^0}F(s,y^1,y^2,y^3)\,ds.
\]
Let
\[
\mathcal W[y]=\int_\Sigma
G(y)\,dy^1\wedge dy^2\wedge dy^3.
\]
By the pullback variation of the target 3-form, integration by parts (no spatial boundary), and \(d[G\,dy^1\wedge dy^2\wedge dy^3]
=F\,dy^0\wedge dy^1\wedge dy^2\wedge dy^3\), its *full spatial functional derivative* is
\[
\boxed{\frac{\delta\mathcal W}{\delta y^a(x)}=F(y(x))M_a(x).}
\]
This includes the derivative terms in \(\delta/\delta y^a\); replacing the functional derivative by the ordinary partial derivative of \(G\) would be incorrect.

Hence the exact constraints are
\[
\phi_a=\pi_a-\delta\mathcal W/\delta y^a.
\]
Functional second derivatives of \(\mathcal W\) commute under the stated smooth/boundary assumptions:
\[
\boxed{\{\phi_a(x),\phi_b(x')\}=0,\qquad
\{\phi_a,H_T\}=0.}
\]
Thus **4 first-class constraints, 0 secondary constraints**, and no local degrees of freedom:
\[
\boxed{N_{\rm phys}=\tfrac12(2\cdot4-2\cdot4)=0}
\]
per space point in the **restricted** \(y^a\) theory. A canonical transformation \(\Pi_a=\pi_a-\delta\mathcal W/\delta y^a\) sends the constraint surface to \(\Pi_a=0\). All admissible bulk variations are null directions of the reduced presymplectic form; boundary/topological degrees of freedom are not excluded.

## 4. Crucial noncommutativity of restriction and variation

The four first-class transformations \(y^a\mapsto y^a+\varepsilon^a(x)\) are **effective gauge degeneracies of the reduced total-divergence functional**, not a proof of 4 additional local gauge symmetries of the original single-\(\Theta\) UBT theory.

The full UBT equations would follow from varying \(\Theta\), all independent connection variables and any complete action **first**, then imposing a branch. This need not equal varying \(S_{\rm red}\). Similarly, the fixed-background \(8\)-component kinetic Hessian and light-cone polynomial in PR #679 and PR #681 have different independent variables and assumptions and must not be mixed with these zero-bulk-Hamiltonian constraints.

## 5. Exact scalar/tensor perturbation consequence

Since \(g_{\mu\nu}=\eta_{ab}\partial_\mu y^a\partial_\nu y^b\), every invertible \(y\) configuration is locally isometric to Minkowski. Around \(y^a=x^a+\varepsilon\xi^a(x)\),
\[
\delta g_{\mu\nu}=\partial_\mu\xi_\nu+\partial_\nu\xi_\mu,
\qquad
\boxed{\delta R_{\mu\nu\rho\sigma}=0.}
\]
The metric perturbation is pure coordinate gauge. It generates neither gauge-invariant scalar curvature perturbations nor physical tensor gravitational waves in this branch. Consequently the physical \(\Theta\to\zeta\) bridge required for CMB cannot come from this gradient-only truncation. The synthetic \(S^3/2I\) mode kernel of PR #669--#673 remains mathematical and observationally gated.

## 6. Independent verification and next physical action step

- \`tools/verify_flat_gradient_dirac.py\` checks the exact 4x4 determinant Hessian, all spatial cofactor orthogonality identities, and the field-theory Euler functional derivative \(\delta\mathcal W/\delta y^a=FM_a\) for all 4 components with unrestricted symbolic spatial first and symmetric second jets.
- \`tests/test_flat_gradient_dirac.py\` asserts its zero residuals; these algebraic checks corroborate, not replace, the general differential-form proof.
- With connections unfrozen, compute the velocity Hessian and mixed Dirac brackets on a **nondegenerate curved solution**. Derive positive-energy reduced modes, a physical \(\Theta\to\zeta\) map and real cosmological transfer functions before making an observational claim.

**No fundamental GR recovery, topology selection, parameter-free CMB spectrum, or physical ghost-freedom is asserted here.**
