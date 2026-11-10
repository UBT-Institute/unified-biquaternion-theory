# Clifford odd-sector inverse selection: complete quadratic flat-background basis

**2026-11-10; conditional exact flat-space result; OPEN fundamental action.**
Scope: a **real** Cl(1,3) field, decomposed into even part and an odd vector V plus axial vector A. Fixed Minkowski metric, ordinary derivative, orientation and parity invariance, local real quadratic densities with at most two derivatives, no external background tensors, modulo integrations by parts. This **does not** classify the entire nonlinear full-Clifford theory, composite metric, connection, curved torsion couplings or terms involving dynamical even fields.

## Inverse objective

We want an independently warranted principle that would force the odd sector to be auxiliary/gauge or produce healthy additional physics, rather than assuming the even C⊗H subalgebra as fundamental. The earlier note [CLIFFORD_ODD_QUADRATIC_SELECTION](CLIFFORD_ODD_QUADRATIC_SELECTION_2026_11_10.md) gave one representative restricted kinetic family. Here we close the **quadratic flat-background invariant-basis problem** under the assumptions above, not the microscopic action-selection problem.

## Complete basis argument

On fixed flat space, a parity-even scalar bilinear with zero derivatives for a polar vector V and axial/pseudovector A consists of V² and A². The bilinear V·A is parity-odd. A local invariant with one derivative and exactly two vectors cannot contract its three free spacetime indices to an ordinary scalar without additional fields or background vectors. With two derivatives, integration by parts moves derivatives onto one factor. The parity-even Lorentz-invariant Fourier kernel in each unmixed vector block is of the form
\[
K^{\mu\nu}(p)=\alpha(p^2)\eta^{\mu\nu}+\beta\,p^\mu p^\nu
\]
with alpha affine in p². Therefore there are exactly two independent two-derivative bulk invariants for each vector, conveniently F_{\mu\nu}F^{\mu\nu} and (partial·V)², plus analogous axial terms. The apparent third contraction partial_mu V_nu partial^nu V^mu equals (partial·V)² up to a total derivative. An epsilon-contracted quadratic derivative expression epsilon^{mu nu rho sigma} partial_mu V_nu partial_rho A_sigma is also a total derivative on flat space (commuting partials); the parity-even/odd behavior of epsilon-cross terms depends on the axial assignment but changes no bulk quadratic rank. For nontrivial curved/torsionful covariant derivatives and boundaries this reduction must be revisited.

Under parity invariance there is no bulk V–A mixing at this order (without parity-odd background fields). This gives **six** real quadratic parameters: kinetic a_V,b_V, mass m_V², and a_A,b_A,m_A². This parameter count is a restricted **flat quadratic basis theorem**, not a selection of their values.

For either X=V or X=A, signature eta=diag(+---):
\[
\mathcal L_X=-\frac{a_X}{4}F_{\mu\nu}(X)F^{\mu\nu}(X)
-\frac{b_X}{2}(\partial_\mu X^\mu)^2
+\frac{m_X^2}{2}X_\mu X^\mu.
\]
For a generic off-shell momentum p, its Euler operator up to the Fourier sign convention is
\[
K^\mu{}_\nu(p)=(m_X^2-a_Xp^2)\delta^\mu{}_\nu+
(a_X-b_X)p^\mu p_\nu.
\]
The vector space decomposes into a 3D subspace p·X=0 and one longitudinal line for p² ≠ 0; the eigenvalues are
\[
\lambda_T=m_X^2-a_Xp^2\quad(\text{multiplicity 3}),\qquad
\lambda_L=m_X^2-b_Xp^2.
\]
For p²=0 use the polynomial eigenvalue/determinant identity by continuation; the longitudinal/transverse projector itself is singular.

Hence det K=(m²-a p²)^3(m²-b p²) for each of V and A. The full parity-even, uncoupled odd-sector determinant is the product of these two expressions.

## Dynamical branches (conditional)

- a=b=0 and m²≠0: no derivatives; the homogeneous unsourced field has X=0. With an admissible algebraic source, X is generally nonzero but auxiliary. On integrating it out, the even sector receives local contact operators.
- a>0, b=0, m²>0: the usual free Proca model on Minkowski space. The algebraic divergence equation m² partial·X=0 removes the extra component, leaving **three** healthy massive vector polarizations with the standard kinetic sign.
- a>0, b=0, m²=0: free Maxwell-type gauge theory X→X+partial chi; **two** local propagating physical polarizations.
- b≠0 (and a≠0): a longitudinal kinetic pole is present. It must be tested for negative norm/energy, constraints, coupling and hyperbolicity before assigning physical significance. For spatially homogeneous velocities the Hessian in variables (X0,X1,X2,X3), with metric (+---), has diagonal entries (-b,a,a,a). For a>0,b>0 this explicitly has a negative X0 kinetic coefficient, but no claim is made that every other b ≠ 0 theory is healthy or unhealthy after constraints.
- m²=0=a=b: the field does not enter this quadratic density; whether it is truly gauge, redundant, or simply unconstrained requires its interactions, measure and constraint algebra. This is NOT evidence of actual elimination.

The polarizations counted above are **vector-sector modes** on fixed flat space, NOT tensor gravitational-wave polarizations and NOT additional modes measured by LIGO.

## Constraints on UBT inference

1. Ordinary Lorentz invariance, parity, local quadraticity and second-order derivatives **cannot select** a=b=0, b=0 or any unique mass; they admit inequivalent auxiliary, Proca and Maxwell branches. This is an exact nonuniqueness demonstration within the specified model class.
2. The full Clifford algebra can therefore contain odd propagating excitations without violating these *symmetries alone*. More physics is needed to select the even biquaternion reduction.
3. A grading-symmetric action can make X=0 a consistent vacuum truncation but does not remove nonzero excited solutions when the kinetic block is present.
4. Terms involving the dynamical even fields, Clifford bilinear readout, parity-odd backgrounds, local spin connection, curvature, torsion, and fermion matter can couple/mix V,A; they may introduce entirely new constraints. This flat result may not be promoted to the full UBT Hessian.
5. Restricting all even fields and geometry to a fixed Minkowski background is a diagnostic, not an assertion that GR is fundamentally prior to UBT.

## Reverse-engineering next gates

- **Selection gate S1:** derive from operational/composition/information principles a symmetry or constraint that *forbids* the odd kinetic terms, or a mass hierarchy that makes the odd fields heavy in the observable IR.
- **S2:** derive the unique full-field scalar pairing/reality prescription and classify parity-even invariant terms involving both even and odd Clifford grades, allowing the full composite tetrad and connection (do not import EH or Yang–Mills by fiat).
- **S3:** run the full Dirac–Bergmann algorithm, gauge-reduced symbol and well-posedness/energy analysis, not merely determinant calculations.
- **S4:** recover two GR tensor polarizations, fermionic spin/SM representations, thermodynamic/information observables and compare with established experimental limits from the SAME selected action.
- **S5:** compute independent discriminator beyond the known data used to build axioms, without post-hoc tuning.

## Verification

The companion test file tests the two-eigenvalue characteristic polynomial, Hessian rank on homogeneous velocities, epsilon-derivative boundary identity and Proca/Maxwell/auxiliary distinction. Its exact SymPy checks were run locally and passed (4 tests); no full repository CI or Lean proof is claimed.

Related:
- [Full Clifford odd-sector gates](FULL_CLIFFORD_ODD_SECTOR.md)
- [Previous restricted quadratic comparison](CLIFFORD_ODD_QUADRATIC_SELECTION_2026_11_10.md)
- [Inverse physical reconstruction](README.md)
- [Canonical action registry](../../canonical/ACTION.en.md)
