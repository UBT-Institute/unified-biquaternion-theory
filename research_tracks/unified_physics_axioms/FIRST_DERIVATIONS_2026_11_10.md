# First inverse derivations: operational physics -> axioms

**2026-11-10. Research status: partial conditional theorems and counterexamples, NOT selected UBT dynamics.**

## I. Relativity fixes a transformation family, not its branch

Assume relativity of inertial frames, spacetime homogeneity, spatial isotropy, linear/regular reciprocal inertial transformations and group composition. For collinear velocities the resulting Ignatowsky family is:

\[
x'=(x-vt)/\sqrt{1-Kv^2},\qquad
t'=(t-Kvx)/\sqrt{1-Kv^2}.
\]

Relativity alone does not determine K. Galilean kinematics has K=0; K>0 yields a Lorentzian invariant cone with finite c=1/sqrt(K). The observed propagation of light selects the finite-c positive branch, and experiments determine c. Other branches require scrutiny of global and empirical assumptions. In the Lorentz branch ds²=-c²dt²+d x². No curvature, gravity, spinor structure, or action is derived.

Reference: Pelissetto and Testa, Am. J. Phys. 83, 338 (2015), DOI 10.1119/1.4901453.

## II. Informational axioms reconstruct quantum theory only in a specified class

Operational preparations and measurements with probabilities, mixing and composition define a convex state-space framework. Classical and nonclassical theories both obey this general structure. A known reconstruction of finite-dimensional complex quantum theory uses causality, perfect distinguishability, ideal compression, local distinguishability, pure conditioning and purification (Chiribella, D'Ariano, Perinotti, Phys. Rev. A 84, 012311, 2011, DOI 10.1103/PhysRevA.84.012311). Purification *alone* is not sufficient. An alternative physical reconstruction was given by Masanes and Mueller (arxiv:1004.1483).

Therefore the candidate information principle cannot remain a bare slogan. Specify operations, distinguishability, composition, local tomography, purification and other domain assumptions before invoking any reconstruction theorem. Neither the action nor gravity follows automatically from these premises.

## III. An exact intersection of Lorentz geometry and qubit information

Use Pauli matrices with sigma_i sigma_j=delta_ij I+i epsilon_ijk sigma_k. For real coordinates define

\[
X=x^0 I+\sum_{i=1}^3 x^i\sigma_i,\qquad
\det X=(x^0)^2-\sum_i(x^i)^2.
\]

Proof: (x.sigma)^2=|x|² I and X(x0 I-x.sigma)=((x0)²-|x|²)I. The Hermitian X is positive semidefinite exactly for x0>=|x|, i.e. the future Lorentz cone. The normalized trace-one section is the Bloch ball:

\[
\rho=(I+r.\sigma)/2,\quad |r|\le1,\quad
\det\rho=(1-|r|^2)/4.
\]

For A in SL(2,C), X -> AX A^\dagger preserves det X and implements the double cover of proper orthochronous Lorentz transformations. **General SL(2,C) boosts do not preserve trace** and are not deterministic trace-preserving qubit gates; SU(2) rotations preserve both positivity and trace.

Choosing the minimal complex spinor S=C² and all its complex-linear endomorphisms gives

\[
\mathrm{End}_{\mathbb C}(S)=M_2(\mathbb C)
\cong \mathbb C\otimes\mathbb H,
\]
via e_k -> -i sigma_k. This is a precise conditional representation result. It does **not** establish that relativity plus information requires a single fundamental biquaternion-valued Theta field: the minimal complex spinor and full endomorphism algebra were extra assumptions. Real-tetrad GR plus ordinary QFT is an explicit rival ontology. Distinguish mathematical equivalence of representations from uniqueness of physical ontology.

## IV. Why a general information principle does NOT fix the action

For normalized smooth classical distributions of fixed support,

\[
D_{\mathrm{KL}}(p_\theta\Vert p_{\theta+d\theta})
=\tfrac12 I_{ij}d\theta^i d\theta^j+O(\|d\theta\|^3),
\]
where I_ij=E[(partial_i ln p)(partial_j ln p)] is Fisher information. It is positive semidefinite on statistical parameters, not a Lorentzian spacetime metric. It does not imply a unique real UBT action or a torsion source. Landauer erasure cost also does not select gravitational dynamics.

Countermodel to uniqueness: for any diffeomorphism-invariant S0 compatible with an observed low-energy limit, the family

\[
S_\lambda=S_0+\lambda\int d^4x\,\sqrt{|g|}\,R^2
\]
has the same kinematical symmetries and Minkowski vacuum at the stated level (with suitable background conditions) but generically different curved-space dynamics. Relativity, c and unspecified information monotonicity do not select lambda. In the existing UBT action registry, the fundamental action remains DEFINED_FAMILY_NOT_FINALIZED.

## V. Gravity, gauge and thermal limits as inverse constraints

Universal long-range gravitational soft coupling may be obtained *conditionally* if Lorentz-invariant S-matrix theory and a massless spin-two mode with the required pole structure are postulated (Weinberg, Phys. Rev. 135, B1049, 1964). This does not uniquely select Einstein–Cartan or biquaternion dynamics. An intrinsic spin current can algebraically source torsion in a chosen Einstein–Cartan action; its on-shell necessity in the full composite UBT action remains OPEN.

Standard Model gauge representation and anomaly conditions, thermodynamic probability/coarse-graining, neutrino chirality, and other empirically observed structures each add independent constraints. The M2(C) representation identity alone does not imply SU(3)xSU(2)xU(1), particle masses or the second law.

## VI. Resulting provisional root principles

- B1 OPERATIONS: physical states have measurable effects/probabilities and systems can be composed.
- B2 SPACETIME RELATIVITY: homogeneous/isotropic regular inertial transformations and relativity; select finite positive K from empirical c, rather than treating c as logically independent.
- B3 QUANTUM RECONSTRUCTION: operational distinguishability, local composition/tomography, compression and purification subject to a precise known reconstruction theorem (candidate assumptions, not proven minimal).
- B4 DYNAMICS/CONSISTENCY: require a well-defined local or explicitly nonlocal state evolution, covariance, physical positive modes, conservation and a gauge-reduced initial-value/scattering formulation; no unique action yet follows.
- B5 CORRESPONDENCE: empirical GR, standard QFT/SM, thermodynamic and many-body tested limits with one parameter map, not imported as exact microscopic equations.

These are **inferred candidate principles**, not a theorem that they are logically independent, minimal, or imply all established physics. B3 includes potentially redundant requirements; explicit axiom-removal countermodels are needed.

### Proven/conditional inference graph

- (B2 + observed positive K) -> Lorentz invariant metric cone [STD, conditional].
- (B1 + exactly stated informational-reconstruction hypotheses) -> finite-dimensional complex quantum theory [external theorem, conditional].
- (minimal complex two-spinor + full End_C) -> M2(C) = complex biquaternions [exact standard algebra identity].
- (Lorentz cone + qubit cone) -> common Hermitian 2x2 positive cone structure [exact, conditional].

**Not established:**
- minimal principles -> unique microscopic field Theta;
- biquaternions -> single UBT action, SU(3)xSU(2)xU(1), Einstein dynamics, nonzero torsion, FTL signalling, third gravitational-wave polarization or quantization of spacetime.

### Next required mathematical gates

1. Establish or refute a truly independent operational principle selecting minimal complex two-spinors over alternative representations.
2. Enumerate invariant actions modulo identities and prove any parameter/derivative selection rather than tune coefficients to output laws.
3. Perform complete composite variation of complex Theta, metric and contortion, then the gauge-reduced Hessian and causal characteristic analysis.
4. Test all sectors on held-out observations, with actual physical detector couplings and distinguishable predictions.

## Reproducible algebra check

The accompanying test checks Pauli products, determinant, qubit determinant and non-trace-preserving boost. Such a check supports algebraic consistency but cannot prove the uniqueness of UBT.

## Reference anchors

- https://doi.org/10.1119/1.4901453
- https://doi.org/10.1103/PhysRevA.84.012311
- https://arxiv.org/abs/1004.1483
- https://doi.org/10.1103/PhysRev.135.B1049
- ../../canonical/ACTION.en.md
- ./README.md
