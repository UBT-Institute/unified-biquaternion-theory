# Positive Dirac symplectic pullback: repair of one compatibility gate, not selection

2026-10-24. Direct exact eight-real-dimensional matrix verification. Compare merged #724 and draft #725. No UBT axiom change.

Let Theta=[psi,chi] in M₂(C), epsilon=[[0,1],[-1,0]], and let the **chosen** real-linear bijection F(Theta)=u=(psi,epsilon chi*)∈C⁴. Let real x collect Re/Im entries of Theta. Set Q=Jacobian_R(F), the invertible real 8×8 matrix. If J_D is block diagonal with four [[0,-1],[1,0]] blocks, the positive Dirac form pulled back to Theta is

\[
\Omega_D=Q^T J_D Q,\qquad G_D=Q^TQ.
\]

Both are constant; \(\Omega_D\) is skew and nondegenerate, and G_D is positive definite (indeed Q is orthogonal in this chosen normalization). For fixed real momentum p and mass m, take the ordinary Hermitian Dirac H_D(p)=[[-sigma·p,mI],[mI,sigma·p]] and du/dt=-iH_D u. The induced real generator A=Q^{-1} A_D Q obeys exactly
\[
\boxed{A^T\Omega_D+\Omega_D A=0}.
\]
Thus the failure in #725 is specific to the *different* candidate \(\Omega_B=B(X,iY)\). The latter has indefinite associated symmetric pairing (2,6); it is not \(\Omega_D\). The associated Dirac quadratic generator is a candidate on the chosen flat slice, not a derived unique UBT Hamiltonian.

**Lorentz subtlety:** the usual positive spinor norm u†u and its equal-time symplectic form are not invariant under pointwise nonunitary SL₂(C) boosts acting on spinors at a *fixed* time slice. Their relativistically meaningful conservation is formulated through the Dirac current and the induced hypersurface inner product ∫Σ n_μ \bar u γ^μ v dΣ, transforming Σ and its unit normal as well. A proof of this construction with UBT's *composite* tetrad, derivative and constraints is still missing.

**Gauge subtlety:** F is real-linear but not complex-linear, and a central U(1) phase on Theta induces opposite phases on the two Weyl chiralities. Its U(1) charge assignment is not automatically ordinary electromagnetic coupling. F also chooses a right-column split, which is not invariant under the unrestricted right-frame group explored in #723.

**Status:** exact finite-dimensional symplectic compatibility achieved after *selecting* a positive Dirac form; its selection from locked biquaternion axioms remains open. The physical next test is the composite tetrad induced hypersurface current and Dirac constraint algebra, without assuming the desired gravity action.

Reproduction: python -m unittest discover -s research_tracks/action_selection/tests -p 'test_dirac_positive_pullback.py' -v.
