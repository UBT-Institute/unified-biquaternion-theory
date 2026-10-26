# Exact nonlinear no-curvature theorem for the zero-connection Theta branch

**Exact local differential-geometric theorem (2026-10-25); stronger than the linearized frozen-connection observation in draft #739. Not a UBT Hamiltonian.**

Use locked Axiom C with a fixed constant N0>0, and take a simply connected open patch in the real physical spacetime slice where the two-sided connection vanishes identically in the chosen trivialization, A_mu=B_mu=0, so D_mu Theta=partial_mu Theta. Assume every E_mu=N0^(-1/2)partial_mu Theta belongs to the locked *fixed real Lorentz subspace* W_L=span_R(iI,e_1,e_2,e_3), and the tetrad is nondegenerate.

Since all first derivatives lie in this constant real vector subspace, locally there are real scalar functions y^a(x) and a constant complex-biquaternion Theta_* with
\[
\Theta(x)=\Theta_*+\sqrt{N_0}\left(i y^0(x)I+\sum_{k=1}^3 y^k(x)e_k\right).
\]
The tetrad coefficients are e_mu^a=partial_mu y^a; therefore the **locked sharp anticommutator metric** is
\[
\boxed{g_{\mu\nu}=\eta_{ab}\partial_\mu y^a\partial_\nu y^b.}
\]
Nondegeneracy means the Jacobian ∂y/∂x is invertible. By the inverse function theorem, y^a are local coordinates, making g exactly Minkowski there. Consequently the Levi-Civita Riemann tensor vanishes **to every nonlinear order**, \(\boxed{R^\rho{}_{\sigma\mu\nu}[g]=0}\), not merely at first order.

This is a conditional *zero connection* theorem, not a claim all curvature requires *torsion* specifically. Composite connections with nonzero curvature and/or special torsionful representations can evade its assumptions. Nonzero connection coefficients can be pure gauge, too: nonzero A,B alone do not guarantee a curved metric. No inference about dynamical gravitons, physical reduced mode count or the existence of the UBT Hamiltonian follows.

A nontrivial coordinate example: y^0=t, y^1=x+κt², y²=y, y³=z gives (t,x)-block g=[[4κ²t²-1,2κt],[2κt,1]] (det=-1), nonzero Christoffel Γ^x_tt=2κ but identically zero Riemann. A separate SymPy regression verifies all 2D Riemann components vanish, demonstrating a coordinate-dependent metric need not be curvature.

The theorem is stated on a real slice; it imposes no claim about off-slice ψ holomorphy or stability. The test does not change canonical axioms. A physical dynamical principle must constrain allowed composite connections; merely choosing a desired curved metric and solving algebraically for A_mu does not determine the Hamiltonian.
