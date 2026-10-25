# Torsion-trace integrating-factor theorem for the UBT Dirac-current bridge

**Exact conditional differential-geometric theorem; 2026-10-25.** Complements #728, not a fundamental Theta Hamiltonian or a completed UBT action.

Adopt the convention in #728:
\[
\nabla_\mu j^\mu=e^{-1}\partial_\mu(ej^\mu)+t_\mu j^\mu,\quad
t_\nu=T^\mu{}_{\mu\nu},\quad e=\sqrt{|g|}.
\]
Suppose a candidate current obeys \(\nabla_\mu j^\mu=0\). For a scalar integrating factor \(w>0\),
\[
e^{-1}\partial_\mu(e w j^\mu)
=w(\partial_\mu\log w-t_\mu)j^\mu.
\]
Therefore **if** \(t=d\phi\), the rescaled current \(\widehat j^\mu=e^\phi j^\mu\) satisfies \(\partial_\mu(e\widehat j^\mu)=0\), yielding a conserved hypersurface flux for vanishing side flux.

Conversely, demanding this identity **for every possible covariantly conserved test current** on a patch that admits arbitrary nonzero current values at a point forces \(\partial_\mu\log w=t_\mu\), hence \(dt=0\). On a simply connected contractible patch the Poincare lemma gives local \(\phi\); globally an integrating factor exists only when the cohomology class \([t]\in H^1_{\mathrm{dR}}(M)\) vanishes. A *single* special current can admit a factor without dt=0 because the weaker contraction \((d\log w-t)\cdot j=0\) suffices. Thus the universality quantifier is essential.

This provides a **sharp falsification gate** for the conditional Dirac-flux route: compute the torsion-trace one-form from the composite Theta connection and test \(dt=0\) (and global periods). In general metric-compatible torsion, dt need not vanish; no universal scalar reweighting can then convert the assumed covariantly conserved current into a coordinate divergence-free current.

A nonconstant w changes the candidate hypersurface pairing and does not by itself make a covariant presymplectic current of the full nonlinear Theta theory. Deriving its Dirac equation, self-consistent variation of tetrad, physical constraints, and the unique Hamiltonian remains open.

Note also that a correct torsionful Dirac equation from a Hermitian action might **directly** conserve a different density/current; this theorem does not prohibit that alternative.
