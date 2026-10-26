# Full composite chain-rule variation of the sharp-volume candidate

**Exact off-shell functional identity, 2026-10-25. NOT a determined UBT Euler–Lagrange equation, Hamiltonian or unique action.** Builds on merged #755. The connection is explicitly nonzero and composite, not frozen.

Assume a regular oriented nondegenerate tetrad in the real Lorentz slice, E_mu=D_mu Theta/sqrt(N0), and let e_mu^a denote its components. For the **conditional** sharp-pairing choice, the collapsed kinetic term is
\[
S_{\rm vol}[\Theta]=2N_0\int_M d^4x\,e[\Theta],\quad e=\det(e_\mu{}^a)>0.
\]
Its off-shell first variation with compact support and orientation fixed is
\[
\delta S_{\rm vol}=2N_0\int d^4x\,e\,e_a{}^\mu\,\delta e_\mu{}^a.
\]
Write P^a for the fixed real-linear component extractor from W_L and D_mu Theta=partial_mu Theta+A_mu[Theta]Theta-Theta B_mu[Theta]. Then
\[
\delta e_\mu{}^a=N_0^{-1/2}P^a\big[
D_\mu(\delta\Theta)+(\delta A_\mu)\Theta-\Theta(\delta B_\mu)
\big].
\]
The variations δA,δB must include **all** induced dependencies through the composite e, metric-compatible omega(e,T), and any (unproved) torsion law T[Theta]. Because the composite connection may be defined implicitly, the resulting operator \(\mathcal L_\Theta:\delta\Theta\mapsto\delta e\) can require implicit linearized inversion; do not treat it as simply ∂+A−B when varying.

Using the natural pairing between component covectors and tetrad variations, a compact exact formal Euler–Lagrange condition is
\[
\boxed{\mathcal L_\Theta^*(e\,e_a{}^\mu)=0,}
\]
where * is the formal adjoint with integration measure d4x and implicit connection variation included. (The constant factor 2N0 is irrelevant to the zero condition.) **This is a structural identity only:** neither L_Theta nor its adjoint is determined by locked axioms until the torsion-selection/composite-connection response is specified. If L depends on δe implicitly, solve that linearized system before drawing PDE, Hessian or degree-of-freedom conclusions.

The zero-connection Jacobian branch makes the determinant integrand a pullback volume form and locally a boundary term; this does NOT carry over automatically to the full nonzero composite-connection branch. Conversely nonzero A,B do not ensure nontrivial propagating modes.

A useful elementary test is the determinant differential \(d\det e=\det e\,\mathrm{tr}(e^{-1}de)\). The accompanying SymPy regression tests this identity for a generic nonzero tetrad and a generic perturbation, and an exact nonzero-connection 1D model e=∂x q+a(q)q showing how a composite connection produces an extra bulk variation: for S=∫e dx, δS=∫[∂xδq+(a+qa')δq]dx, hence the local EL equation is a+qa'=0 (with compact δq). This 1D example is *not* claimed to be a UBT gravity reduction; it only validates the chain-rule logic.

**Next required selector:** define T[Theta] or an equation determining it with no independent propagating field, specify admissible Omega and measure on complex time, compute full linearized map L_Theta, then determine constrained Hessian/Dirac brackets and derive H and full S from an independent physical principle. Do not claim completion until this is accomplished.
