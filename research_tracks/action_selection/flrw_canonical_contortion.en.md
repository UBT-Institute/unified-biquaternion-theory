<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: flrw-canonical-contortion.provenance -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional special case of canonical torsion local representability, no on-shell UBT solution.
UBT-AI-PROVENANCE-END
-->

# Closed FLRW as an explicit special case of the EXISTING canonical contortion theorem

**Status: EXACT KINEMATIC SPECIALIZATION / DYNAMICAL OPEN_GAP.**
**Priority:** This construction is an application of pre-existing \`GAP-10I-TORSION-LOCAL\`, not an independent invention of a second connection or a first-principles gravitational action. See \`canonical/geometry/connection.tex\` and \`canonical/CANONICAL_DEFINITIONS.md\`. It corrects the missing rotational spin component in \`connection_closed_flrw.en.md\`. The latter's boost-only \(A=f\sigma_i\upsilon^i\) reproduces the metric but is **not** by itself the guaranteed metric-compatible spin lift.

## 1. Existing theorem, specialized without extra fields

On a local cosmic-time patch, take a closed FLRW geometry with the quotient of the unit group sphere \(\Sigma=(2I)\backslash SU(2)\),
\[
ds^2=-dt^2+a(t)^2\sum_{i=1}^3\upsilon^i\otimes\upsilon^i,\qquad
d\upsilon^i=-\epsilon^i{}_{jk}\upsilon^j\wedge\upsilon^k.
\]
The spatial coframe is globally defined under the left deck action, and the curvature is \(+1/a^2\). Write \(H=\dot a/a\) and select the timelike *concurrent-vector candidate*
\[
V^\mu=V(t)\delta^\mu_t,\qquad V(t)=t-t_0>0.
\]
Using the Levi--Civita connection,
\[
\mathring\nabla_t V^t=1,\qquad
\mathring\nabla_i V^j=HV\delta_i^j.
\]
The existing canonical contortion theorem prescribes
\[
K_{\nu\mu\rho}
=\frac{(g_{\mu\nu}-\mathring\nabla_\mu V_\nu)V_\rho
-V_\nu(g_{\mu\rho}-\mathring\nabla_\mu V_\rho)}{V^2_{\rm norm}} .
\]
Its only nonzero mixed components, up to symmetries, are
\[
\boxed{
K^i{}_{jt}=\left(\frac1V-H\right)\delta^i_j,\qquad
K^t{}_{ij}=\left(\frac1V-H\right)g_{ij}.
}
\]
Consequently
\[
\boxed{\nabla^\Gamma_\mu V^\nu=\delta_\mu{}^\nu,\qquad
T^0=0,\quad T^i=\left(H-\frac1V\right)e^0\wedge e^i.}
\]
In particular the torsion is pure FLRW-compatible vector torsion and is zero iff \(H=1/V\), i.e. \(a(t)=a_\star V(t)\) locally. All expressions are singular at \(V=0\); no global-in-time regularity is implied.

## 2. Full metric-compatible Lorentz and biquaternion spin connection

Choose \(e^0=dt,\ e^i=a\upsilon^i\). The corresponding metric-compatible Cartan connection obeys
\[
\boxed{
\omega^i{}_0=\omega^0{}_i=\frac1V e^i,\qquad
\omega^i{}_j=-\epsilon^i{}_{jk}\upsilon^k.
}
\]
Its rotation contribution is essential; the original boost-only connection of draft PR #685 omitted it.

On the canonical Lorentz-real \(2\times2\) Pauli representation \(\Theta=i\sqrt{\mathcal N_0}V I\), choose the **single** spin connection, not an independent left/right pair,
\[
\boxed{
\Omega=\frac12\left(\frac aV-i\right)\sigma_i\upsilon^i,
\qquad A=\Omega,\qquad B=-\Omega^\dagger .
}
\]
The boost part is Hermitian and the spatial rotation part anti-Hermitian. Direct matrix algebra gives
\[
\boxed{
D\Theta=d\Theta+\Omega\Theta+\Theta\Omega^\dagger
=i\sqrt{\mathcal N_0}(I\,dt+a\sigma_i\upsilon^i).
}
\]
Thus the canonical central metric **and** the metric-compatible spin/tetrad postulate hold with no new dynamical fields assumed.

Write \(f=a/(2V)\), \(c=f-i/2\), \(b=-f-i/2\). The coefficients of \(\upsilon^1\wedge\upsilon^2\) in the left/right curvatures are
\[
(F_A)_{12}=\left(-2c+2ic^2\right)\sigma_3,\quad
(F_B)_{12}=\left(-2b+2ib^2\right)\sigma_3,\quad
\boxed{(F_A)_{12}=(F_B)_{12}
=i\left(\frac12+2f^2\right)\sigma_3.}
\]
The time-space coefficients are \((F_A)_{ti}=\dot f\,\sigma_i\) and \((F_B)_{ti}=-\dot f\,\sigma_i\).
Therefore spatial connection curvatures are nonzero but cancel in the commutator acting on the *scalar* \(\Theta\), whereas
\[
\boxed{
D^2\Theta=F_A\Theta-\Theta F_B
=i\sqrt{\mathcal N_0}(\dot a-a/V)\,\sigma_i\,dt\wedge\upsilon^i
=i\sqrt{\mathcal N_0}\sigma_i T^i .
}
\]
These equalities connect the original UBT connection commutator to Cartan torsion in this **particular compatible representation**; they are NOT the universal identity \([D,D]\Theta=T\) for unrelated arbitrary \(A,B\). Nonzero \(\mathcal R(\omega)\) remains possible even if \(D^2\Theta=0\), because curvature may annihilate the particular \(\Theta\).

## 3. Exact conditional dynamic obstruction

The canonical definitions already classify \`GAP-10T-PALATINI\`: in a minimal Hilbert--Palatini branch with **zero matter spin current**, the invertible algebraic Cartan equation sets \(T^a=0\). For the above \(\Theta\)-representer this demands \(a=a_\star V\).

Independently, if one **also** imposes the standard *imported* GR vacuum closed-FLRW equation with a constant cosmological constant,
\[
\frac{\dot a^2+1}{a^2}=\frac{\Lambda}{3},
\]
then inserting \(a=a_\star V\) yields
\[
\frac{\dot a^2+1}{a^2}
=\frac{a_\star^2+1}{a_\star^2V^2},
\]
which cannot equal a spacetime constant on a time interval. Hence this **one-representer, spinless minimal Palatini, closed FLRW, vacuum-\(\Lambda\)** combination has no nondegenerate solution on an interval. It is **not** a no-go for full UBT or arbitrary spinning matter: an independently derived nonzero spin current, another suitable \(\Theta\), generalized holonomy, or a different gravitational action may evade it.

### Irreducible torsion decomposition

Geometric algebra regards metric-compatible torsion as a vector-valued bivector. Its Lorentz components divide into the trace, axial-vector, and residual tensor representations:
\[
\boxed{\dim_{\mathbb R}(TM\otimes\Lambda^2T^*M)=4\cdot6=24=4+4+16.}
\]
The decomposition must not be confused with the finite field or a count of propagating particles. With convention \(T^\lambda{}_{\mu\nu}=\Gamma^\lambda{}_{\mu\nu}-\Gamma^\lambda{}_{\nu\mu}\) and trace \(\mathfrak t_\mu=T^\nu{}_{\mu\nu}\), our solution satisfies:
\[
\boxed{
\mathfrak t_0=3(H-1/V),\quad \mathfrak t_i=0,\qquad
T^\lambda{}_{\mu\nu}
=\frac13(\delta^\lambda_\nu\mathfrak t_\mu
-\delta^\lambda_\mu\mathfrak t_\nu).
}
\]
The axial-vector and residual tensor sectors vanish identically: this example has only trace torsion.

Under minimal Einstein–Cartan–Dirac coupling, the standard fermionic spin current sources only axial torsion. It therefore cannot independently support this pure-trace torsion in that restricted model. Nothing is inferred about as-yet uncomputed UBT spin currents or nonminimal matter.

Standard references: https://doi.org/10.1103/PhysRevD.104.064036 ; https://doi.org/10.1140/epjc/s10052-019-7536-3 .

## 4. What changed relative to previous research

- The **existence** of curved single-\(\Theta\) kinematic representers using composite torsion was ALREADY closed locally in the repository. Our previous claim of an entirely new closure was too strong.
- We have now *specialized* the existing theorem to closed FLRW with explicit coframe, boost and rotation, algebraic torsion and cancellation in \(D^2\Theta\).
- This specializes the previously open question: determine the \(\Theta\)-derived spin current and action, check whether the required \(T^i\) is selected on shell and remains finite, then obtain \(\zeta[\Theta]\). No claim of a physical CMB fit is warranted.
- The Clifford bivector/rotor language is a representation of this geometry, not a newly imposed independent algebra or a substitute for the canonical \(\Theta\) dynamics.

**Verifications:** \`tools/verify_flrw_canonical_contortion.py\` and \`tests/test_flrw_canonical_contortion.py\`. These check the specialized connection/torsion/curvature identities, not the full UBT Euler--Lagrange equations.
