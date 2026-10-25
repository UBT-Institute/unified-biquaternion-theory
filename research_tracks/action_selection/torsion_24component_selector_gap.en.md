# The 24-component torsion selection gap in Hamiltonian-first UBT

**Exact pointwise geometric count, 2026-10-25. Not a torsion equation or fundamental Hamiltonian.**

The locked axiom reconstructs a metric-compatible frame connection from a nondegenerate tetrad and *specified* torsion: omega=omega_LC(e)+K(T). Fix e and use an orthonormal frame. The spin connection has 4×6=24 independent coefficients omega_mu^[ab]. Torsion has 4×6=24 independent T^a_[mu nu]. At each point the map between metric-compatible connection differences (contortion) and torsion is a linear isomorphism (the uniqueness of metric-compatible connection at fixed torsion). Thus the geometric reconstruction **does not constrain those 24 degrees of freedom by itself**.

In particular, in a local flat background ebar_mu^a=delta_mu^a, omegabar=0 and small perturbation delta e, delta omega,
\[
\delta T^a{}_{\mu\nu}=
\partial_\mu\delta e_\nu{}^a-\partial_\nu\delta e_\mu{}^a
+\delta\omega_\mu{}^a{}_\nu-\delta\omega_\nu{}^a{}_\mu.
\]
This is an algebraic linear *relation*, not an evolution equation for torsion. Assigning arbitrary delta T and using the invertible map generates a connection but does not prove that delta T follows from Theta; it may overparametrize the no-extra-field theory.

The frozen-connection pure-gauge result of #739 and the unconstrained curved witness of #741 are compatible: fixing delta omega can be too restrictive; choosing it freely can be too permissive. The admissible middle must follow from a **single-Theta composite torsion law and its constraints**, which locked axioms have not yet uniquely supplied. Any candidate torsion functional T[Theta,DTheta,...] must be compatible with the full tetrad identity, Lorentz covariance, local solvability and gauge degeneracy; derivative dependence can raise PDE order and requires a principal-symbol and constraint analysis. Simple component counting cannot prove physical propagating degrees of freedom; diffeomorphism and Lorentz gauge directions must be reduced.

**Decision point:** before announcing H_UBT or S_UBT, explicitly derive or independently justify the torsion selector, solve for the implicit composite connection, identify the admissible initial-data manifold, compute reduced presymplectic form and full Hamiltonian constraint algebra. The geometric formula omega(e,T) alone cannot perform that selection.
