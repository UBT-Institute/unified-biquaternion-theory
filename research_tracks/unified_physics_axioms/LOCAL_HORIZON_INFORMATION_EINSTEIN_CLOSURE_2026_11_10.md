# Inverse gravity closure: local horizon information balance to Einstein equations

**2026-11-10; status CONDITIONAL STANDARD RESULT + UBT selection gates OPEN.** This note is a *comparator* based on Jacobson's 1995 local-horizon thermodynamic derivation, not a proof of gravity, its microscopic origin, or unique UBT dynamics.

## What the inverse-reconstruction task must explain

Minimal starting desiderata: relativistic causal structure and operationally accessible information/correlations, including observer restrictions; any physical gravity equation or action must follow from specified extra principles and be independently tested. **No metric, horizon area entropy, Unruh temperature, Einstein–Hilbert action, or Newton coupling can be quietly treated as derived from generic noninjective biquaternion multiplication**. A simulated/reduced representation may lose information without actual destruction, energy release, or thermal entropy production.

## Conditional Jacobson computation (natural units c=hbar=k_B=1)

Assume a smooth Lorentzian manifold with local causal Rindler horizons. At an arbitrarily chosen point, consider a local null congruence with affine parameter lambda (zero at p) and tangent k^mu. Choose local equilibrium at p, so expansion theta and shear sigma initially vanish; ignore terms higher order in lambda. Raychaudhuri then gives
\[
\frac{d\theta}{d\lambda}=-\frac12\theta^2-\sigma_{\mu\nu}\sigma^{\mu\nu}
-R_{\mu\nu}k^\mu k^\nu
\quad\Rightarrow\quad
\theta(\lambda)=-\lambda R_{\mu\nu}k^\mu k^\nu+O(\lambda^2).
\]
Therefore the first-order horizon area response is
\[
\delta A=-\int\lambda R_{\mu\nu}k^\mu k^\nu\,d\lambda\,dA .
\]
Assume universal horizon entropy density S_H=eta A with eta>0. For approximately boost-Killing generator chi^mu=-kappa lambda k^mu, the horizon energy flux is
\[
\delta Q=-\kappa\int\lambda T_{\mu\nu}k^\mu k^\nu\,d\lambda\,dA,
\]
while the Unruh temperature is T_H=kappa/(2pi). Imposing reversible Clausius relation delta Q=T_H delta S for *every* local null horizon gives
\[
\eta R_{\mu\nu}k^\mu k^\nu=2\pi T_{\mu\nu}k^\mu k^\nu
\quad\forall\; k:\;g(k,k)=0 .
\]
The minus signs cancel in the chosen lambda convention. A symmetric tensor whose contraction with every null vector vanishes is proportional to the metric (in Lorentz signature in dimension >=3). Thus
\[
R_{\mu\nu}-\frac{2\pi}{\eta}T_{\mu\nu}=f(x)g_{\mu\nu}.
\]
Take covariant divergence, impose \(\nabla^\mu T_{\mu\nu}=0\), and use contracted Bianchi \(\nabla^\mu R_{\mu\nu}=\frac12\nabla_\nu R\). This gives \(\partial_\nu f=\frac12\partial_\nu R\), hence \(f=\frac12 R-\Lambda\) for constant Lambda. Therefore
\[
\boxed{R_{\mu\nu}-\tfrac12 Rg_{\mu\nu}+\Lambda g_{\mu\nu}
=\frac{2\pi}{\eta}T_{\mu\nu}.}
\]
Taking eta=1/(4G), the Bekenstein–Hawking density in natural units, the coefficient is \(2\pi/\eta=8\pi G\). Restoring SI units, \(8\pi G/c^4\).

**Critical logical scope:** this establishes Einstein dynamics *conditional on the assumed metric, local horizons, Unruh temperature, equilibrium, universal area entropy and stress-energy conservation.* It does not reconstruct the metric, G, area law, spin-statistics or UBT action.

## What happens with information loss or entropy production?

A general process need not satisfy reversible Clausius equality. In a suitable near-equilibrium regime, write
\[
dS=d_eS+d_iS,\qquad d_eS=\delta Q/T,\qquad d_iS\ge0.
\]
In Eling–Guedens–Jacobson non-equilibrium horizon thermodynamics the entropy production term can account for internal/gravitational dissipation and modifications in the entropy functional, but a generic d_iS does **not** imply a universal local term in Einstein's equations and cannot be equated with arbitrary loss of distinguishability. The shear term of Raychaudhuri is quadratic and may matter at higher order/non-equilibrium, while in the equilibrium derivation its leading contribution is fixed to vanish at p. A UBT microscopic model must calculate actual entropy production from physical dynamics; it must also preserve covariant conservation and the appropriate Bianchi/Noether identities in the GR limit.

## A concrete no-go: noninjectivity does not fix G

Take a rank-one P in C⊗H≈M2(C). The left map X→PX has nontrivial kernel, so it loses accessible algebraic distinctions. But the map contains no observer, metric/horizon, temperature, area, \(\hbar\), \(c\), or Newton coupling. Its rank/kernel are dimensionless. One cannot infer \(\eta=1/(4G)\), \(S\sim A\), or an Einstein tensor from it without new inputs. More broadly the same noninjective map and reset channel exist in generic M2(C) quantum mechanics; no UBT uniqueness follows.

Likewise a unitary entangling circuit can increase reduced-state entropy without dumping heat to a thermal bath. A **quantum channel** and its entropy flow, not mere algebraic multiplication, must be derived and coupled to geometry.

## What would constitute actual UBT progress?

**G0 -- causal/state foundations.** Define operational access and local subalgebras or quantum channels directly from information/composition postulates, not from assumed Cl geometry; respect bosonic and fermionic entanglement, fermion parity and no-signalling.

**G1 -- geometry without presupposition.** Derive a Lorentzian effective metric and null cones from the minimal axioms. In existing UBT the metric from composite tetrad is rank constrained and real Lorentz only on a classical slice: explicitly handle this rather than treating the metric as fundamental.

**G2 -- area law without insertion.** Count horizon-accessible states or entanglement and derive S_H=eta A, including a finite, universal eta; area law cannot be simply borrowed from Bekenstein–Hawking.

**G3 -- temperatures and flux.** Establish Unruh/KMS behavior and a locally measured stress-energy flow in the derived geometry. Derive and justify reversible/irreversible entropy balance, without setting heat generated = info lost by definition.

**G4 -- coupling and dynamics.** Derive eta from microscopic scales and obtain the tensor field equations; simultaneously compute torsion, local Lorentz connection, Hamiltonian constraints and all physical degrees of freedom. Make sure eta>0 and no ghost modes occur, and recover the GR Newtonian lensing and gravitational-wave limits.

**G5 -- predictive discrimination.** Exhibit a numerical consequence not used to select premises. Determine if M_n(C), a generic spinor bundle, or another operational theory reproduces all derivations without the special biquaternion claim.

## Reproducible symbolic consistency checks

Companion tests verify:
- null-cone tensor condition in signature (+---) fixes a symmetric matrix to an arbitrary metric multiple;
- \(\eta=1/(4G)\) gives \(2\pi/\eta=8\pi G\);
- Raychaudhuri linear-order expansion with zero initial expansion/shear;
- metric-proportional freedom cannot be fixed by null contractions alone (cosmological constant).

These are **checks of classical identities**, not numerical simulations or experimental validations of UBT.

References:
- T. Jacobson, "Thermodynamics of Spacetime: The Einstein Equation of State" (1995), https://arxiv.org/abs/gr-qc/9504004
- C. Eling, R. Guedens, T. Jacobson, "Non-equilibrium Thermodynamics of Spacetime" (2006), https://arxiv.org/abs/gr-qc/0602001
- E. Verlinde, "On the Origin of Gravity and the Laws of Newton" (2011), https://arxiv.org/abs/1001.0785

Related research: [Holographic information loss gravity](HOLOGRAPHIC_INFORMATION_LOSS_GRAVITY_2026_11_10.md), [Biquaternion information loss](BIQUATERNION_INFORMATION_LOSS_LANDAUER_2026_11_10.md), [inverse programme](README.md).
