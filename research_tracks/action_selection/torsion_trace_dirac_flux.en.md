# Decisive torsion-trace gate for a physical Dirac charge in UBT

Status: exact differential-geometric identity under stated conventions, not a derivation of the full UBT dynamics or its Hamiltonian. Follows composite-Dirac-current track #727.

Let \(\nabla_\mu V^\lambda=\partial_\mu V^\lambda+\Gamma^\lambda{}_{\mu\nu}V^\nu\) and \(T^\lambda{}_{\mu\nu}=\Gamma^\lambda{}_{\mu\nu}-\Gamma^\lambda{}_{\nu\mu}\). For a metric-compatible connection with density \(e=\sqrt{|g|}\), \(\partial_\mu\log e=\Gamma^\lambda{}_{\mu\lambda}\). Therefore
\[
\boxed{\nabla_\mu j^\mu=\frac1e\partial_\mu(ej^\mu)+t_\nu j^\nu,\qquad t_\nu:=T^\mu{}_{\mu\nu}.}
\]
Thus **covariant conservation** \(\nabla_\mu j^\mu=0\) implies \(\partial_\mu(ej^\mu)=-e\,t_\mu j^\mu\), and does NOT generally imply conserved hypersurface Dirac charge \(\int_\Sigma d\Sigma_\mu j^\mu\).

The exact no-leak criterion for that particular current is \(t_\mu j^\mu=0\) pointwise or vanishing of its spacetime integral for the compared slices, plus the usual side-boundary condition. The stronger torsion-trace-free condition \(t_\mu=0\) suffices for all currents. Neither condition has yet been derived from the locked Theta axioms. Alternatively the *actual* Dirac equations derived with a Hermitian torsionful action might carry an improved current / Levi-Civita divergence; these equations and that action must be demonstrated rather than asserted. Purely totally antisymmetric torsion has zero torsion trace, while generic metric-compatible torsion need not.

**Why this matters to Hamiltonian-first UBT.** A covariant Dirac inner product is usable as a symplectic source only after this flux gate. In the composite geometry \(e=e(\Theta,\partial\Theta)\), the full presymplectic current also receives induced tetrad and connection variations. A test-field Dirac current cannot be identified with it by replacement of symbols.

## Exact algebraic local example

Use Minkowski \(\eta_{\mu\nu}=\mathrm{diag}(-1,1,1,1)\) and the metric-compatible connection
\[
\Gamma^\lambda{}_{\mu\nu}=\delta^\lambda_\mu v_\nu-\eta_{\mu\nu}v^\lambda
\]
for a nonzero constant covector v. Its lower-index connection \(\Gamma_{\lambda\mu\nu}=\eta_{\lambda\mu}v_\nu-\eta_{\mu\nu}v_\lambda\) obeys \(\Gamma_{\nu\mu\lambda}+\Gamma_{\lambda\mu\nu}=0\), hence \(\nabla\eta=0\). Its torsion trace is \(t_\nu=3v_\nu\) in 4D, even though \(e=1\). This explicitly disproves an automatic equivalence of \(\nabla_\mu j^\mu=0\) and \(\partial_\mu j^\mu=0\) for arbitrary metric-compatible torsion.

Research outcome: require a torsion-trace identity, physical current improvement, or a derived constraint before using the Dirac hypersurface flux to select the UBT symplectic form/Hamiltonian.
