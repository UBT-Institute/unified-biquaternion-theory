# Holomorphic jet non-selection test for the Hamiltonian-first UBT programme

**Exact kinematic result, 2026-10-25.** This checks whether locked complex time and the central first-jet metric alone force a time-evolution generator. They do **not**. It does *not* establish physically inequivalent gravitational solutions; diffeomorphism/gauge quotient and dynamics remain to be supplied.

Work in a permitted flat local derivative branch D_mu=partial_mu, with quaternion units e_j²=-1 and the locked Lorentz slice W_L={i a⁰1+Σaʲe_j}. Put τ=t+iψ and choose real λ:
\[
\Theta_0=i\tau\,1+\sum_{j=1}^3x^j e_j,\qquad
\Theta_\lambda=\Theta_0+i\lambda\tau^2\,1.
\]
Both are entire holomorphic in τ and satisfy the Cauchy–Riemann identity ∂ψΘ=i∂tΘ. On the physical ψ=0 slice their first covariant jets are W_L-valued. At (t,ψ,x)=(0,0,0), the fields and their first jets coincide:
\[
\Theta_\lambda=\Theta_0,\quad
\partial_t\Theta_\lambda=\partial_t\Theta_0=i1,\quad
\partial_j\Theta_\lambda=\partial_j\Theta_0=e_j,
\]
so the central-antocommutator metric has the same nondegenerate local value, \(\eta=\operatorname{diag}(-1,1,1,1)\) up to the fixed N₀ scaling. But their second real-time jets differ:
\[
\partial_t^2\Theta_0=0,\quad
\partial_t^2\Theta_\lambda=2i\lambda\,1.
\]
Thus holomorphy, a specified first jet and the locked composite metric **at a point** do not determine the next jet. This remains true while the time tetrad is nondegenerate on a sufficiently small real-time patch, \(1+2\lambda t\ne0\).

**Crucial scope:** these are kinematically allowed first-jet configurations, **not claimed to solve a common finalized UBT field equation**. The different second derivative may be coordinate/gauge-related on the flat subbranch and is not by itself a proof of physically distinct degrees of freedom or of nonuniqueness after the Hamiltonian constraints. A dynamical evolution equation and its gauge constraints are exactly what must decide which local jets are on shell. Compatibility of the full \(\psi\)-dependent real-Lorentz slice is a separate unsolved dynamical issue; the example is asserted on \(\psi=0\) only.

Separately, the established nonuniqueness result from #716 shows that even choosing a canonical phase space and internal symmetries allows invariant Hamiltonians differing by a quartic potential. The present example isolates the distinct failed hope that complex-time holomorphy and first-jet geometry *alone* act as a dynamical law.

**Decision gate:** formulate physical initial-data constraints (including torsion, the real slice and \(\psi\) conditions), derive their closed brackets and a nontrivial generator \(\mathcal H\) from an independent physically motivated principle. Only then reconstruct the action; first-order symplectic reconstruction of #732 cannot by itself pick \(\mathcal H\).
