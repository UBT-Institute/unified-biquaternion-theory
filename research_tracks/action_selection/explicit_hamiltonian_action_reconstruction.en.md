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

# Explicit Hamiltonian-to-action reconstruction on the 8-real Theta carrier

**Constructive conditional theorem.** This is a family of explicit actions **once** an invariant two-form and a Hamiltonian are chosen; it is not a proof that locked UBT axioms uniquely choose the physical action.

Let \(q\in\mathbb R^8\), \(J^2=-I\), \(K^T=K\), \(J^TKJ=K\), and \(\Omega=KJ\) be the constant nondegenerate antisymmetric form from #717. Fix a *prescribed* spatial measure \(d\mu\). For any real differentiable Hamiltonian density functional \(H[q]\), consider
\[
\boxed{S_{\Omega,H}[q]=\int dt\left[-\frac12\int_\Sigma d\mu\ q^T\Omega\,\partial_tq-H[q]\right].}
\]
For compactly supported variations (or appropriate endpoint/boundary conditions):
\[
\delta S=\int dt\int_\Sigma d\mu\ \delta q^T[-\Omega\partial_tq-\delta H/\delta q].
\]
Thus Euler–Lagrange equations are
\[
\boxed{\Omega\partial_tq=-\frac{\delta H}{\delta q},\qquad
\partial_tq=-\Omega^{-1}\frac{\delta H}{\delta q}.}
\]
This uses exactly the convention \(\iota_{\dot q}\Omega=dH\) with \(\Omega(X,Y)=X^T\Omega Y\), as in #717. The minus sign in the kinetic term is essential; it may differ in other sign conventions. This is a first-order phase-space action directly on Theta, requiring **no independent momentum field**. Its symplectic form is the **selected** Omega and its Hamiltonian is exactly the **selected** H, not newly derived data.

For the simplest invariant quadratic \(H_2=\frac12\int d\mu\ q^TKq\), use \(\Omega^{-1}=-JK^{-1}\) to obtain \(\dot q=Jq\). For an invariant local nonlinear density \(H_\lambda=H_2+\frac{\lambda}{4}\int d\mu\ (q^TKq)^2\), the flow is
\[
\boxed{\dot q=[1+\lambda(q^TKq)]Jq}.
\]
Both are invariant under the same declared representation whenever it preserves K and commutes with J, and both admit the same Omega and well-defined actions. Thus even the explicit action reconstruction **does not** select unique physics. For spatially varying fields, add an independently justified Hamiltonian density and derive its boundary/constraint structure; the formal prescription by itself neither generates gravity nor Lorentz covariance, nor a physical Hamiltonian that is bounded below (K has inertia 2+,6-).

**Crucial gate:** the locked Theta axioms do not yet fix (a) a physical density/foliation in complex time, (b) the physical presymplectic structure after composite-metric constraints, or (c) an independent principle selecting H. Until these are established, call the above \(S_{\Omega,H}\) an explicit *candidate family*, never the finalized \(S_{\mathrm{UBT}}\). The GR, Dirac, torsion, psi and constraint reductions are not derived by this algebraic reconstruction.

This result makes the action stage constructive and shows exactly what mathematical information is missing before the final selection.
