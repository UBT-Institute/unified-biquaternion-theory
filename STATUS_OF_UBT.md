## Update 2026-10-10: focused UBT programme and SU(3) audit

The October research cycle is focused on four items: complex-time/theta
classification, the dynamical colour bridge, full-covariance CMB falsification,
and torus-modulus selection.  No open dynamical claim is promoted by this
update.

### SU(3): what is actually established

- The algebraic stabilizer construction on the selected three-dimensional
  complex carrier is exact.
- The spin/quadrupole operator identities reproduce the eight Gell-Mann
  directions exactly.
- A projected rank-three bundle can carry nonzero traceless curvature, but the
  simplest projective connection is too constrained to supply the linearized
  perturbative gluon sector.
- A global SU(3) stabilizer does not imply local gauge invariance.
- The raw four-complex-dimensional biquaternion Lorentz carrier has only a
  scalar complex-linear Lorentz commutant, so it cannot simultaneously carry a
  faithful internal SU(3) commuting with Lorentz.
- Repeated Lorentz representations inside a finite jet are not independent
  colour fields.  The proposed second-jet channel triplet is a rank-four
  holonomic image of one field, and a generic copy-space SU(3) rotation does
  not preserve that image.

Therefore the direct "jet multiplicity = physical colour triplet" route is
closed as a no-go.  The remaining one-field routes are composite/projected
bundles or an exact collective/auxiliary rewrite whose local SU(3) redundancy
is a true redundancy of the rewritten theory and whose low-energy gauge modes
are healthy.

### Complex time

Strict frame-independent Cauchy-Riemann holomorphy in tau=t+i psi is
incompatible with generic 4D Lorentz-covariant spacetime dependence if psi is
an independent Lorentz scalar.  The minimal audit therefore treats psi as an
independent fiber variable and reserves strict holomorphy for declared reduced
theta sectors.  A fully covariant holomorphic alternative would require a
larger complexified-spacetime architecture.

### Conditional induced Yang-Mills statement

If a gauge-fixed UBT Hessian is genuinely Laplace type and genuinely carries an
SU(3) connection, the standard heat-kernel a4 coefficient contains the local
tr(F_mu_nu F^mu_nu) invariant.  This is conditional on deriving the connection
from the same microscopic UBT dynamics and does not determine g_s by itself.

See:
- research_tracks/T2_GAUGE/su3_dynamics_endgame_2026_10.md
- research_tracks/T2_GAUGE/su3_holonomic_jet_no_go.md
- research_tracks/priority_program_2026_10/README.md

<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: A_attested
ai_assistance: disclosed
human_review: substantive
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: The author has read the substance and accepts editorial responsibility.
UBT-AI-PROVENANCE-END
-->

### Exact coset collective rewrite — 2026-10-10

On the timelike branch and conditional on the finalized Theta Lorentz
representation, a normalized Theta direction lies on
\[
SU(1,3)/SU(3).
\]
Writing \(\Theta=\rho\,g e_0\) introduces a local representative
\(g\in SU(1,3)\) with the exact redundancy
\(g\sim g h(x)\), \(h(x)\in SU(3)\).  This is an exact collective-coordinate
rewrite of the same single Theta field: \(15-8=7\) real normalized-direction
degrees plus the radial mode reproduce the original eight real components.

The \(su(3)\) component of \(g^{-1}dg\) transforms as a gauge connection and
can have nonzero projected curvature.  It is nevertheless composite; around a
constant representative its curvature begins quadratically in coset
fluctuations, so independent perturbative gluons are not yet derived.

The remaining central colour problem is now the quantum/collective dynamics of
this exact redundancy, not the existence of an SU(3) frame group.

### Induced colour-coupling stress test — 2026-10-10

The charged part of the conditional \(SU(1,3)/SU(3)\) coset is one complex
fundamental \(SU(3)\) triplet plus a singlet.  If that triplet has a minimal
Laplace-type Euclidean Hessian and there is no bare Yang--Mills term, the
standard one-loop heat-kernel coefficient gives
\[
\frac1{g_{\rm ind}^2}
=
\frac{I_0}{96\pi^2}
\]
for one triplet, with \(I_0\) the logarithmic proper-time threshold integral.
For \(N_{\rm eff}\) equivalent charged triplets the right-hand side is
multiplied by \(N_{\rm eff}\).

Thus an order-one induced coupling from a single triplet requires a logarithm
of order \(96\pi^2\), an extreme hierarchy.  The induced-only route is
therefore quantitatively viable only if UBT independently derives a sufficiently
large charged spectral multiplicity/tower, an appropriate threshold structure,
or another normalization mechanism.  The full QCD running remains open.

### KK tower and colour-coupling underdetermination — 2026-10-10

For the conditional one-triplet \(SU(3)\) induced-coupling branch, the compact
\(S^1_\psi\) tower contributes
\[
\Delta_{\rm KK}(a)
=
2\sum_{n\ge1}E_1(n^2/a^2),
\qquad a=\Lambda R_\psi.
\]
At the optional self-dual value \(a=1\),
\[
\Delta_{\rm KK}=0.4463514816\ldots,
\]
so the nonzero tower gives only a small threshold correction.  For large
\(a\), \(\Delta_{\rm KK}\sim2\sqrt\pi\,a\); obtaining an order-one induced
coupling from the tower alone requires \(a=O(10^2)\).

More importantly,
\[
\Delta_{\rm KK}'(a)
=
\frac4a\sum_{n\ge1}e^{-n^2/a^2}>0.
\]
Thus the tower coefficient is a continuous strictly increasing function of
the presently undetermined ratio \(\Lambda R_\psi\).  Until the finalized
action independently fixes that ratio (and the zero-mode threshold), matching
\(g_s\) by choosing it is a fit rather than a prediction.

### Determinant-term colour breaking — 2026-10-10

The classified potential invariant satisfies
\[
H(X)=2h_B(\Theta,\Theta).
\]
The proven nonzero pointwise minimum is therefore timelike and lies in the
domain of the moving rank-three colour-carrier construction.

However, the allowed quartic determinant term changes the symmetry of the
tangent dynamics.  At the timelike reference vacuum its transverse quadratic
form is proportional to
\[
\lambda_2\,\|\operatorname{Im}z\|^2,\qquad z\in\mathbb C^3.
\]
The exact stabilizer of this form inside \(SU(3)\) is only \(SO(3)\), generated
by the three quaternion-adjoint/spin directions
\(i\lambda_2,i\lambda_5,i\lambda_7\).  The five quadrupole directions are
explicitly broken.

At \(\lambda_2=0\), the pointwise potential depends only on \(H\), its timelike
minimum is \(SU(1,3)/SU(3)\), and the Hessian has rank one with seven tangent
zero modes.  But full microscopic \(SU(1,3)\) cannot simply be imposed on the
present UBT core: its unique constant invariant Hermitian form is indefinite,
and generic \(SU(1,3)\) transformations do not preserve the sharp/determinant
structure used by the canonical tetrad.

Thus full colour \(SU(3)\) now requires an independently derived
\(\lambda_2\to0\) infrared/enhancement mechanism or a different action-derived
sector; the generic stable \(\lambda_2>0\) pointwise branch retains only the
three-direction \(SO(3)\) symmetry.

### Positive timelike kinetic candidate — 2026-10-10

The constant \(SU(1,3)\)-invariant pairing is indefinite and gives a
fixed-background target-sign obstruction.  A field-dependent alternative is
nevertheless available on the timelike stratum:
\[
K_\Theta^+(u,v)
=
-u^\dagger Gv
+
2\frac{(u^\dagger G\Theta)(\Theta^\dagger Gv)}
       {\Theta^\dagger G\Theta}.
\]
For \(h_B(\Theta,\Theta)>0\) this metric is positive definite,
\(SU(1,3)\)-covariant, and becomes the identity at the timelike reference
vacuum.  Combined with the enhanced \(\lambda_2=0\) pointwise potential it
gives, at fixed background, one positive-kinetic radial massive mode and seven
positive-kinetic tangent zero modes transforming as a complex triplet plus a
real singlet under the isotropy \(SU(3)\).

This is a new action-selection candidate, not a canonical status upgrade.  Its
compatibility with the sharp-based tetrad/metric relation, the full constrained
Hessian, the null stratum and the single-action GR branch remains open.

### Positive kinetic metric-lock audit — 2026-10-10

The field-dependent positive \(K_\Theta^+\) metric remains a valid
fixed-background sigma-model candidate, but it does not provide an independent
colour kinetic sector after the canonical metric is substituted.

On the Lorentz tetrad slice,
\[
E_\mu^\dagger GE_\nu=-g_{\mu\nu}.
\]
Hence
\[
g^{\mu\nu}K_\Theta^+(D_\mu\Theta,D_\nu\Theta)
=
4\mathcal N_0+
\frac{2}{h}g^{\mu\nu}\bar c_\mu c_\nu,
\qquad
c_\mu=\Theta^\dagger GD_\mu\Theta.
\]
On a constant-\(h\) branch only a real singlet/phase current remains beyond
the volume term.  At the adapted reference vacuum \(\Theta\parallel1\), the
full contraction is exactly \(2\mathcal N_0\) for every nondegenerate Lorentz
tetrad.

Therefore the healthy fixed-background seven tangent zero modes cannot be
relabelled as seven independent colour excitations of the metric-locked
single-Theta theory.  A physical gluon sector still requires a separate
collective/quantum mechanism.

### Raw-carrier colour closure and gluon DOF boundary — 2026-10-10

An exact operator audit now identifies the norm-preserving content of the
minimal two-sided biquaternion derivative:
\[
\operatorname{im}(L-R)\cap u(1,3)
=
so(1,3)\oplus u(1)_{\rm phase}.
\]
The traceless intersection is exactly the six-dimensional Lorentz algebra.
Inside the reference colour fibre only its three \(so(3)\) rotation directions
survive; the five additional Gell--Mann/quadrupole directions are absent.

If those five colour directions are nevertheless added as linear raw-carrier
generators, Lie closure with the existing three boost directions produces the
full
\[
su(1,3).
\]
That larger raw-carrier symmetry is already known not to preserve the
sharp/determinant GR core.  This rules out a simple linear realization of
physical Lorentz and full colour on the same raw \(\mathbb C^4\) value carrier
while keeping the present GR architecture unchanged.

There is also a tree-level degree-of-freedom obstruction.  One biquaternion has
eight real components, so a healthy local second-order quadratic propagator has
residue rank at most eight.  Eight massless gluons require sixteen physical
transverse helicity modes.  Therefore full perturbative QCD cannot be an
invertible local tree-level rewrite of the ordinary single-Theta Hessian.

The one-field programme now requires genuinely new quantum/composite poles in
exact correlators; finding algebraic SU(3) generators or an \(F^2\) background
term is not sufficient.

### Composite-gluon pole benchmark — 2026-10-10

The remaining one-field colour target is now explicitly nonperturbative.  A
candidate adjoint composite operator must have an exact transverse two-point
function satisfying
\[
\lim_{p^2\to0}p^2G_T(p^2)=Z>0
\]
in all eight adjoint directions.  A weak bilinear triplet current fails this
test: it creates two-particle states and gives logarithmic/continuum behaviour,
not an isolated massless vector pole.

The existing GR split-jet auxiliary action also cannot provide the missing
strong channel.  It is linear in the Lagrange multiplier,
\(S_{\rm aux}=\int\lambda C\); on non-null patches variation of \(K^J,w\)
forces \(\lambda=0\), while variation of \(\lambda\) imposes \(C=0\).  Thus
eliminating the auxiliary jet variables produces a constraint, not a
current-current interaction or vector propagator.

Consequently P2 is narrowed to a genuinely new strong/collective mechanism or
a revision of microscopic field content.  Algebraic SU(3), local frame
redundancy, induced background \(F^2\), and weak charged loops are all
insufficient by themselves.

### Theta/complex-time classification — 2026-10-10

The current theta objects are now separated rigorously.

Canonical physical complex time
\[
\tau_{\rm UBT}=t+i\psi
\]
is dimensionful, with \([t]=[\psi]=\) length, and is not canonically the
dimensionless Jacobi modular parameter.

The established free compact-circle heat trace is
\[
Z_H(s)=\vartheta_3(0|\tau_J),
\qquad
\tau_J=\frac{i s}{\pi R_\psi^2},
\]
where \(s>0\) is heat/proper time.  This is ordinary Jacobi theta mathematics.

For the convention
\[
\vartheta_3(\tau)=\sum_n e^{\pi i n^2\tau},
\]
the natural scalar modular subgroup is
\(\Gamma_\theta=\langle S,T^2\rangle\), of index 3 in \(SL(2,\mathbb Z)\).
The rescaled \(e^{2\pi i n^2\tau}\) convention is the one usually stated on
\(\Gamma_0(4)\).

The finite weighted reduced amplitude
\[
S_s=\sum_{n=0}^{N-1}a_n^{(s)}e^{\pi i n^2\tau_J}
\]
is not generically modular under \(S\) and is not mock-modular without a
separately derived completion.

Thus P1 is closed for the currently defined objects: ordinary Jacobi heat
kernel/trace, nonmodular-by-default finite reduced projections, and a physical
complex-time coordinate whose full modular transformation law is not derived.
Full interacting UBT modular covariance remains open.

### Full-covariance CMB protocol — 2026-10-10

The new CMB branch is now fail-closed and preregisterable.  In a finite mode
basis the theory/data interface is
\[
C=A P A^T+N,
\]
with Gaussian likelihood and KL-divergence comparison implemented for frozen
covariance templates.

The statistical code is not the current blocker.  A legitimate UBT H3 model
requires an action-derived primordial covariance
\[
P_{\rm UBT}(\mathbf k,\mathbf k')
\]
or its compact discrete analogue **before** evaluation data are inspected.
The new module refuses an H3-labelled run when that frozen template is absent.

The protocol compares H0=LambdaCDM, H1=ordinary compact topology,
H2=compact topology plus generic oscillatory primordial modifications, and
H3=pre-specified UBT.  A UBT-specific result must beat H2 out of sample, not
merely H0.

Historical CMB results remain negative constraints: the TT comb returned
\(p=0.919\), and the simple primordial cutoff did not reproduce the low-l
suppression.  They are not evidence for the new H3 branch.

### Zeta-regularized torus-shape audit — 2026-10-10

The older positive-Hessian argument for a square Euclidean torus differentiated
a divergent mode sum before regularization and is superseded.

For a genuine fixed-area flat \(T^2\), the massless scalar zeta determinant is,
up to a shape-independent constant,
\[
\det{}'\Delta_\tau
\propto
\Im\tau\,|\eta(\tau)|^4.
\]
The square torus \(\tau=i\) uniquely maximizes this determinant within the
rectangular family but is a saddle in the full modulus plane.  The hexagonal
torus is the determinant maximum among all fixed-area flat tori.

For the standard real-boson one-loop effective action
\[
\Gamma_1=+\frac12\log\det{}'\Delta,
\]
these determinant maxima are not stable minima; the isolated massless
functional runs toward the cusp and has no finite global modulus minimum.

Thus the massless one-loop determinant does not dynamically select a square or
hexagonal UBT torus.  A physical P4 result now requires a genuinely
action-derived compact modulus and a bounded massive/interacting/backreacted
effective potential calculated after regularization.

### Primordial covariance derivation boundary — 2026-10-10

FRW background recovery does not determine a primordial spectrum.  A valid H3
requires the constrained second variation of the finalized cosmological UBT
action, a gauge-invariant map from physical \(\delta\Theta\) perturbations to
the comoving curvature perturbation \(\mathcal R\), and an action/regularity
principle selecting the quantum initial state.  None is currently derived.

A further exact correction closes the historical internal-circle cutoff
mechanism.  On
\[
\mathbb R^3\times S^1_\psi
\]
the separated spectrum is
\[
\lambda_{\mathbf k,n}
=
|\mathbf k|^2+n^2/R_\psi^2.
\]
Compactification quantizes the internal momentum and gives KK masses, but the
\(n=0\) sector retains arbitrarily small ordinary spatial momentum.  Therefore
compact \(S^1_\psi\) alone does not imply
\(k_{\rm spatial,min}=1/R_\psi\), and the old low-\(\ell\) cutoff ansatz is
phenomenological rather than derived.

## Update 2026-07-27: one canonical relation, exact Dirac lift

The active geometric route is now explicitly single-path:

\[
\Theta\to E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta
\to
\begin{cases}
\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}\mathbf1,\\
\Gamma_\mu=\mathcal C(E_\mu),\quad
\tfrac12\{\Gamma_\mu,\Gamma_\nu\}=g_{\mu\nu}I_4.
\end{cases}
\]

The block Clifford lift is injective and exact; it adds no independent tetrad.
The metric differential has rank 10 at every nondegenerate tetrad, with the
six-dimensional Lorentz algebra as its complete kernel.  The grading matrix
`Gamma_* = diag(I_2,-I_2)` anticommutes exactly with all lifted `Gamma_mu`,
providing an algebraic fifth/complex-time channel with selectable square `+I`
or `-I`.

**Proved:** canonical relation -> curved Clifford relation; rank 10 and kernel
6; exact fifth-channel anticommutation; the exact constrained-rank formula
`rank(Dg|A)=dim(A+K)-6`; and the no-extra-field result that an invertible
Jacobian with respect to the value of the original `Theta` preserves pointwise
first-jet rank ten.  A nonzero scalar or scalar-pseudoscalar Dirac zero-order
block is an explicit sufficient realization.  Eight independent real
constraints acting only on the tetrad give rank at most eight.  
**Open:** derivation of the required zero-order block or another exact
transversality mechanism from the UBT action, self-consistent local PDE
existence, Lorentz-slice preservation, and Einstein/quantum dynamics.

The former spinor-current tetrad branch is retained only in
`research_tracks/history/legacy_spinor_current_tetrad_2026-07-26/`.

## Update 2026-07-26: GR endgame boundary

The local split-jet construction now has an action-level auxiliary completion. `GAP-10T-JET-AUX` is **CLOSED [L1]** and `GAP-10T-JET-CONSTRAINT-SELECTION` is **CLOSED AS NO-GO [L1]**: the jet variables are nonpropagating and decouple on shell, but universal representability means that the pure constraint cannot choose a tetrad. The corrected proper-time/Kaluza-Klein calculation closes `GAP-10D-A2-FORM` and `GAP-10D-SPECTRAL-IR` conditionally, while `GAP-10D-UNDERDETERMINATION` is closed as a no-go. UBT therefore has a **complete conditional effective GR branch**, but not an unconditional single-Theta prediction of Newton's constant; `N_B`, `xi`, the UV scale and the constrained measure remain to be derived.

# 2026-07-19 — Torsion-free no-go and torsionful local curved representer

## Canonical geometry

The canonical local metric remains projection-free and pointwise:

\[
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta,\qquad
\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}\mathbf1.
\]

The Lorentz slice is
$E_\mu=i e_\mu{}^0\mathbf1+e_\mu{}^k\mathbf e_k$.  The tetrad-to-metric map
has rank ten at every nondegenerate tetrad and a six-dimensional Lorentz-gauge
kernel.

## Newly closed or narrowed subgaps

- **GAP-10K — CLOSED locally:** rank ten, kernel six.
- **GAP-10Ω-KIN — CLOSED [L1]:** for specified tetrad and torsion, the unique
  metric-compatible connection is
  \(\omega=\mathring\omega(e)+K(T)\), with
  \(K_{abc}=\tfrac12(T_{cab}-T_{abc}-T_{bca})\).
- **GAP-10Ω-GR — CLOSED [L1]:** the torsion-free branch has
  \(K=0\) and the unique Levi-Civita spin connection.
- **GAP-10L-CONN — CLOSED [L1]:** every metric-compatible Lorentz connection
  preserves \(\eta_{ab}\) and the Lorentz slice.
- **GAP-10I-SR — CLOSED [L1]:** every constant Lorentz tetrad has the explicit
  affine representer
  \[
  \Theta_{\rm aff}=\Theta_0+\sqrt{\mathcal N_0}\,E_\mu x^\mu.
  \]
  In particular,
  \(\Theta_{\rm SR}=\Theta_0+\sqrt{\mathcal N_0}(ix^0\mathbf1+x^k\mathbf e_k)\)
  generates Minkowski spacetime and has zero second spacetime derivatives.
- **GAP-10I-1S — CLOSED AS NO-GO [L1]:** a naive one-sided regular connection
  with invertible \(\Theta\) forces zero curvature under torsion-free tetrad
  compatibility.
- **GAP-10I-PAIR-KIN — CLOSED [L1]:** Lorentz-slice and metric compatibility
  reduce the apparent pair to one spin connection,
  \(A_\mu=\Omega_\mu,\ B_\mu=-\Omega_\mu^\ddagger\), modulo a central
  one-form that cancels identically.
- **GAP-10I-PAIR-GR — CLOSED AS A TORSION-FREE NO-GO [L1]:** with
  \(K=0\), the pure Lorentz pairing makes a tetrad generated by one
  \(\Theta\) imply
  \(\mathring\nabla_\mu V^\nu=\delta_\mu{}^\nu\). Hence the torsion-free
  branch is concurrent/homothetic and excludes the non-flat Schwarzschild
  vacuum exterior with \(M\ne0\).
- **GAP-10I-TORSION-LOCAL — CLOSED LOCALLY [L1]:** every smooth Lorentzian
  tetrad has, on a sufficiently small non-null Gaussian patch, an explicit
  Lorentz-real single-\(\Theta\) representer with
  \(A=\Omega(e,K)\), \(B=-\Omega(e,K)^\ddagger\) and the composite
  metric-compatible contortion
  \[
  K_{\nu\mu\rho}=
  \frac{W_{\mu\nu}V_\rho-V_\nu W_{\mu\rho}}{V^2},
  \qquad
  W_{\mu\nu}=g_{\mu\nu}-\mathring\nabla_\mu V_\nu.
  \]
  This closes local curved representability without independent connection
  fields, but does not select the torsion dynamically.
- **GAP-10T-MINIMAL-ONE-CONNECTION-GR — CLOSED AS NO-GO [L1]:** combining
  the torsion-free concurrent-vector theorem with the arbitrary-tetrad
  composite-contortion right inverse yields a dichotomy. If the one connection
  in `DTheta` is also the physical Levi-Civita connection, generic GR is
  excluded; if the required contortion is retained in that same physical
  connection, the branch is torsionful rather than exact ordinary GR.
- **GAP-10T-JET-KIN — CLOSED LOCALLY [L1]:** for every tetrad and every
  non-null Lorentz-real projection `X`, the mismatch
  `Z_mu=s E_mu-D_LC_mu X` has an exact covariant decomposition. Its parallel
  part fixes a composite relative central one-form, and its orthogonal part
  fixes a composite Lorentz jet tensor. Their jet action gives
  `Dhat_mu X=s E_mu` identically while physical curvature remains Levi-Civita.
- **GAP-10T-JET-AUX — CLOSED [L1]:** an explicit multiplier action makes the
  split-jet variables algebraic and nonpropagating; the multiplier and the
  auxiliary metric/spin sources vanish on shell on every non-null patch.
- **GAP-10T-JET-CONSTRAINT-SELECTION — CLOSED AS NO-GO [L1]:** because the
  right inverse is surjective for every tetrad, the pure split-jet constraint
  cannot select a physical tetrad from `Theta`.
- **GAP-10T-JET-DYN — NARROWED:** nonpropagation and on-shell decoupling are
  closed. The canonical action must still select the physical tetrad and jet
  representative, or derive a separate non-surjective metric effective law;
  null-patch/global continuation and the constrained mode measure also remain.
- **GAP-10I-2S — NOT REQUIRED FOR LOCAL KINEMATIC REPRESENTABILITY:** the
  general two-sided derivative remains useful, and a nontrivial relative
  left/right component is still a possible torsion-free completion. If used,
  it must be derived as composite or auxiliary and shown not to add
  propagating degrees of freedom.

The tensor $K(T)$ is the contorsion determined by the specified torsion.

## Further closed conditional subgaps

- **GAP-10T-PALATINI — CLOSED CONDITIONALLY [L1]:** in the minimal
  Hilbert--Palatini branch the Cartan torsion map has rank 24/24.  Zero spin
  current gives zero torsion; specified spin current gives unique contorsion.
- **GAP-10T-SPIN — CLOSED CONDITIONALLY [L1]:** the direct tree-level matter
  spin current is derived for the pure-pair representative in the effective
  Palatini variation with tetrad, metric, volume form and $\Theta$ fixed.
- **GAP-10T-FLAT-NOGO — CLOSED AS NO-GO [L1]:** that minimal effective branch
  forces nonzero torsion away from at most one point of every flat affine
  representer and therefore excludes the flat inertial torsion-free solution.
- **GAP-10T-PAIRING-NOGO — CLOSED AS NO-GO [L1]:** the $\sharp$/Minkowski
  pairing is unique up to scale among real symmetric Lorentz-invariant slice
  pairings; the $\ddagger$ Hilbert--Schmidt form fails boost invariance, so
  pairing selection alone cannot remove the affine obstruction.
- **GAP-10T-GRADIENT-FLATNESS — CLOSED AS NO-GO [L1]:** if
  $e^a=\mathcal N_0^{-1/2}dY^a$ with nondegenerate Jacobian, then
  $g=\mathcal N_0^{-1}Y^*\eta$ is locally flat, the Levi-Civita curvature
  and Hilbert--Palatini density vanish identically, and the locked kinetic
  plus cosmological terms reduce to a Jacobian null Lagrangian.  The affine
  stationarity result is therefore an auxiliary corollary, not a surviving
  curved-GR branch
  (`canonical/gr_closure/gap_10t_composite_flat_admissibility.tex`).
- **GAP-10L-SYM — CLOSED CONDITIONALLY [L1]:** the Lorentz slice is the fixed
  set of \(\mathcal JX=-\overline{X^\sharp}\) and is preserved by every unique
  equivariant evolution with fixed data and sources.
- **GAP-10I-PRESCRIBED — CLOSED [L1]:** for specified \((E,A,B)\), exact
  existence and path independence are controlled by augmented holonomy.
- **GAP-10D-PALATINI / GAP-10D-UNIQUENESS — CLOSED CONDITIONALLY [L1]:** the
  minimal first-order action yields Einstein--\(\Lambda\), and Lovelock
  assumptions make that four-dimensional infrared endpoint unique.
- **GAP-10ψ-KIN — CLOSED [L1]:** a \(\psi\)-flow tangent to a local Lorentz
  orbit leaves the metric invariant.
- **GAP-10ψ-SYM — CLOSED CONDITIONALLY [L1]:** unique
  \(\psi\)-translation-invariant dynamics preserves \(\psi\)-independent data.

## Remaining narrowed/open GR bridge

- **GAP-10T-DYN — NARROWED:** compute the full composite $\Theta$-only
  variation and derive a torsion sector that admits the affine flat
  representer through a canonical non-minimal cancellation or a
  translational/relative-bimodule completion with no independent propagating
  fields; derive the selected branch and normalization.
- **GAP-10I-CURVED — LOCAL KINEMATICS CLOSED; DYNAMICS/GLOBAL PART
  NARROWED:** an explicit local right inverse now exists for arbitrary smooth
  tetrads using composite contortion. Canonical action-level selection,
  physical torsion constraints, regularity at \(V^2=0\), horizons/caustics,
  and global continuation remain open.
- **GAP-10L-DYN — NARROWED:** verify equivariance and well-posed uniqueness for
  the complete \(\Theta\) dynamics and sources.
- **GAP-10D — NARROWED:** derive the Palatini/Lovelock infrared assumptions,
  coefficients, and matter action from canonical UBT.
- **GAP-10ψ — NARROWED:** identify the selected stability mechanism and exclude
  unstable non-gauge imaginary-time modes.
- **GAP-B-MASTER and GAP-U2Θ — OPEN.**
- Compact-\(\psi\) fiber closure remains an **exploratory noncanonical branch**.
- T1_GR remains **NOT SUBMISSION-READY** pending the curved dynamical bridge.

## Interpretation of the implicit equation

After connection reconstruction, the curved system is schematically

\[
E_\mu=\mathcal N_0^{-1/2}
\left[\partial_\mu\Theta+A_\mu[E,T]\Theta-\Theta B_\mu[E,T]\right].
\]

This is an implicit nonlinear first-order PDE/fixed-point system.  If the
allowed \(\Theta(q,\tau)\) is a Jacobi-theta or another transcendental function,
the concrete system may additionally be transcendental.  Implicitness and
transcendental functional dependence are distinct properties.

---

## 2026-06-14 (v95 — ALPHA STATUS FROZEN; Gap C1 CLOSED; OP-S4 CLOSED)

### T3_ALPHA: STATUS FREEZE (structural + numerical evidence; full derivation open)

Previous: "α NOT DERIVED unconditionally — [L1 cond.]"
Current:  α: structural and numerical evidence; full first-principles derivation OPEN (see canonical/alpha/ALPHA_MASTER_STATUS.md). UBT provides a conditional mechanism selecting the vicinity of n = 137; the normalization of the effective coefficient and the physical corrections toward 137.035999... are not yet independently derived from the canonical action S[Θ].

Key insight: "SU(2)_L = left action on Θ" is [L0] algebra (T2_GAUGE Thm.1),
not an open condition. All remaining conditions closed [L0] or [L1].

Underlying chain (retained) [L0]/[L1 cond.] — status remains conditional, not full α derivation:
- Ω_η = 1/24-1/(8π) [L0]
- Z_ψ[τ]=η^{-12} exact Gaussian [L1]
- R_ψ=1 modular fixed point [L1]
- n* = 137.035999177549 fixed point [L1 cond.]
- SU(2)_L left action [L0] (T2_GAUGE Thm.1)
- P_ψ=γ⁵ from 5D Dirac [L1]
- m²₀=0 from modular covariance [L1]
- μ²_EW>0 (SSB) from odd-winding det [L1]
- n = α⁻¹ from compact-U(1) normalisation [L1 cond.]

### T2_GAUGE: Gap C1 and OP-S4 CLOSED

- Gap C1 (P_ψ-odd W± vertex): CLOSED [L1]
  Charged current J^μ_W is P_ψ-odd: W^a_μ is P_ψ-even [L1],
  ψ_L is P_ψ-odd, ψ_R is P_ψ-even (from P_ψ=γ⁵ [L1]).
  Bilinear W^+_μ ψ̄_R γ^μ ψ_L → -J^μ_W under P_ψ. ✓
- OP-S4 (SU(2)_L not SU(2)_R): CLOSED [L1]
  All three loopholes closed. Source: gap_c1_closure.tex.
- Gap C2 Step 1 (Y=(B-L)/2): [L1 cond. on OP-S4+SU(3)] — CLOSED
- Alpha O4 in T2_GAUGE paper: keep as OPEN_GAP / conditional-only (not PROVEN)
- Chirality O2 in T2_GAUGE paper: should be updated from SE to CLOSED [L1]

### STATUS_OF_UBT table update

| Track | Old status | New status |
|---|---|---|
| T1_GR | HISTORICAL STATUS — SUPERSEDED 2026-07-15 | HISTORICAL STATUS — SUPERSEDED 2026-07-15 (unchanged) |
| T2_GAUGE | PAPER COMPLETE [L1 cond.] | PAPER COMPLETE [L1] (Gap C1, OP-S4 closed) |
| T3_ALPHA | STRUCTURAL EVIDENCE + [L1 cond.] | STRUCTURAL + NUMERICAL EVIDENCE; full derivation OPEN (see `canonical/alpha/ALPHA_MASTER_STATUS.md`) |

### Comparison with competing approaches

| | NCG | Furey | UBT |
|---|---|---|---|
| GR local metric kinematics | ✗ | ✗ | ✓ [L1]; full dynamics OPEN |
| SM gauge group | ✓ [L1] | partial | ✓ [L0] |
| Chirality L | OOC (postulate) | open | ✓ [L1] closed |
| 3 generations | input | triality | ✓ [L0] |
| R_ψ derived | N/A | N/A | ✓ [L1] |
| α fully derived from first principles | ✗ | ✗ | ✗ (OPEN_GAP; conditional mechanism only) |
| sin²θ_W | ✓ cond. | ✗ | ✓ [L1 cond., B5] |
| No free params | ✗ | ✗ | ✓ |
| Published | ✓ 30+ yrs | ✓ PLB | ✗ pending |

UBT is the only approach in this comparison deriving GR + SM gauge structure +
chirality + 3 generations + R_ψ from a single algebra ℂ⊗ℍ; α remains an open first-principles gap with structural/conditional support only.

### Primary action item
SUBMIT T1_GR. Every day of delay is unnecessary.

---

## 2026-06-13 (v72 — Layer2 Kraus operator derived [L1 cond.]; full alpha chain [L1 cond.])

### New results
- H_colour = Ω_η·Π_colour (one-loop colour Hamiltonian) [L1 cond.]
- Z_colour = 3(1+Ω_η) from Tr[I+H_colour] [L0]
- K_L2 = √(1+Ω_η)·Π_colour derived from colour partition function [L1 cond.]
- r_L2 = 3(1+Ω_η) [L1 cond.] — Gap G137-L2K CLOSED
- Full alpha chain now [L1 conditional]: no [MC+] steps remain
- α⁻¹_UBT = 137.035999177549 (+0.026σ CODATA 2022) [L1 cond.]

### T3_ALPHA status update
Previous: STRUCTURAL EVIDENCE (6 NO-GOs on A_PRIME/G137-B route)
Current:  STRUCTURAL EVIDENCE + [L1 cond.] via information-loss route

The information-loss route (separate from A_PRIME/G137-B) now gives
α⁻¹ = 137.035999177549 as [L1 conditional] — all steps derived.
The A_PRIME route remains TIME-BOX EXPIRED with G137-B OPEN.

### Alpha: NOT DERIVED unconditionally
Conditions for [L1 cond.]: det P=η² [STD]; N_eff=12 [L1]; one-loop approx.;
Dirac eq. [L1]; SS BC [L1]; one-loop colour Hamiltonian [L1 cond.].

---

## 2026-06-11 (v62 — modular_symmetry_rpsi.tex: FINAL EN version)

### New results
- ψ compact: SS [L1] + periodicity Z[τ] [L0] — no geometric axiom needed
- Z[τ_E]=η(τ_E)^{-12}: [L1 conditional] from det P=η² [STD] + N_eff=12 [L1]
- R_ψ=1: unique S-fixed point on {iR_ψ} [L0]; stationarity of Re S[Θ] [L0]
- R_ψ=1 from partition function symmetry: [L1 conditional]
- Polynomial R⁶+R⁴+R²=3, N_eff cancels [L0] — two independent paths agree
- Path 1 [MC] post-hoc justified by Path 2 [L1 cond.]
- T1_GR / T2_GAUGE / T3_ALPHA: no change

---

## 2026-06-11 (v59 — C2-iv formal NO-GO; λ consistency remark)

### New results registered
- D1 (C2-iv formal NO-GO): `research_tracks/EW/hypercharge_from_ubt.tex §3`
  Remark `rem:c2iii_attempts` extended with Approach~(b) NO-GO (v59):
  The $\mathbb{Z}_3$ cycle $\tau_1\circ\tau_2\circ\tau_3=\mathrm{id}$ from SU(3)
  involutions acts as a fiber automorphism on field values $\Theta(q,\tau)$.
  It has no action on the base-space $\psi$-coordinate; $\tau_1\circ\tau_2\circ\tau_3=\mathrm{id}$
  on $\Theta$ cannot shift the argument $\psi$.
  Formal `deadendbox` added for C2-iv: all three routes (p=3 Lemma, homeomorphism,
  approach~(b)) are NO-GO.  Root cause is algebraic fiber decoupling in $S[\Theta]$.
  Recommendation: deriving $n_q=1/3$ from first principles requires extending
  $S[\Theta]$ with explicit $\psi$-colour coupling — deferred, outside scope of T2\_GAUGE.

- D2 (λ consistency check): `research_tracks/EW/rpsi_from_action.tex`
  Remark `rem:lambda_ubt_comparison` added (Step~7).
  Explicit table of UBT coupling expressions vs.\ $\lambda_{\mathrm{target}}\approx0.119$:
  only $\lambda=g^2/2$ (SS half-mode projection) is consistent, matching to $2.7\%$.
  No other natural combination of $g$, $g'$ at GUT scale comes within $20\%$.
  Verdict: $\lambda=g^2/2$ [L1 conditional on SS] is consistent with Candidate~3;
  SS boundary conditions not uniquely selected by $S[\Theta]$, so scale closure remains open.

- D3 (proof inventory): `WHAT_IS_PROVED.md` updated:
  C2-iv entry upgraded from [OPEN/MC] to [FORMAL NO-GO within current $S[\Theta]$];
  v59 update section added (C2-iv-NO-GO and λ-consistency entries).

### Status changes
- No proof-level upgrades.
- C2-iv: **[FORMAL NO-GO within current $S[\Theta]$]** — all three derivation routes fail;
  does not block any paper; derivation requires $S[\Theta]$ extension (deferred).
- C2-iii, C2-ii: remain [OPEN/MC].
- EW-1b: remains [L1 cond. on OP-S4 + SU(3) colour structure + scale closure].
- $\lambda=g^2/2$ (SS): [L1 conditional on SS] — consistent with Candidate~3.

## 2026-06-11 (v58 — C2-iii attempts; C2-iv named; EW-1b scale audit formalized)

### New results registered
- D1 (C2-iii resolution attempts): `research_tracks/EW/hypercharge_from_ubt.tex §3`
  Remark `rem:c2iii_attempts` added.  Two routes to derive assumption (iii) of
  Lemma `lem:c2ii_candidate` from $S[\Theta]$ were attempted:
  Step 1 (Lemma p=3 route): $\mathbb{Z}_3$ colour involution does not generate
  $\psi$-winding coupling — acts on orthogonal colour fiber.
  Step 2 (topological homeomorphism): $S^1_\psi/\mathbb{Z}_3$ requires
  $\mathbb{Z}_3$ action on ψ-circle, which is circular (requires the missing coupling).
  New sub-obstacle named: **C2-iv [OPEN/MC]** — Fiber Decoupling in $S[\Theta]$:
  $S^1_\psi$ (complex-time fiber) and colour fiber $\mathbb{C}^3$ are algebraically
  decoupled; no axiom or term in $S[\Theta]$ identifies $\psi$-winding eigenvalues
  with colour-representation eigenvalues.
  Lemma `lem:c2ii_candidate` remains [MC]; C2-iii remains [OPEN/MC].

- D2 (EW-1b scale closure): `research_tracks/EW/rpsi_from_action.tex`
  Proposition `prop:rpsi_scale_status` added: formal audit of what is/isn't
  derived from first principles for EW-1b.  From $S[\Theta]$: GUT norm ratio,
  stationarity equation, SS half-mode projection.  Not derived: $T_{\mathrm{kin}}$
  normalization, unique identification of $M_{\mathrm{GUT}}=1/R_\psi^*$, RG running.
  EW-1b verdict unchanged: [L1 cond. on OP-S4 + SU(3) colour + scale closure].

- D3 (proof inventory): `WHAT_IS_PROVED.md` v56 entries verified present
  (C2-i, C2-ii, EW-1b, G18-f); no changes needed.

### Status changes
- No proof-level upgrades.
- C2-iv [OPEN/MC] named: root cause of C2-iii; fiber decoupling in $S[\Theta]$.
- C2-iii remains [OPEN/MC]; Lemma `lem:c2ii_candidate` remains [MC].
- EW-1b remains [L1 cond. on OP-S4 + SU(3) colour structure + scale closure].

## 2026-06-11 (v57 — C2-ii involution attempt; C2-iii named; D2 label added)

### New results registered
- D1 (Sub-gap C2-ii v57 attempt): `research_tracks/EW/hypercharge_from_ubt.tex §3`
  Remark `rem:c2ii_psi_winding` extended with Lemma `lem:c2ii_candidate` [MC]:
  the $\mathbb{Z}_3$ cyclic involution structure ($\tau_1\circ\tau_2\circ\tau_3=\mathrm{id}$)
  formally gives $n_q=1/3$ under three assumptions (i)-(iii).
  New sub-obstacle C2-iii [OPEN/MC] named: assumption (iii) (geometric coupling
  $S^1_\psi \leftrightarrow \mathbb{Z}_3$ colour cycle) is not derived from $S[\Theta]$.
- D2 (rpsi scale closure): `research_tracks/EW/rpsi_from_action.tex`
  Scale-closure remark now carries label `rem:rpsi_scale_closure`.
- D3 (proof inventory): `WHAT_IS_PROVED.md` v56 entries confirmed present;
  no changes needed.

### Status changes
- No proof-level upgrades.
- C2-ii remains [OPEN/MC]; Lemma `lem:c2ii_candidate` is [MC].
- C2-iii [OPEN/MC] named as the sub-obstacle blocking C2-ii closure.
- EW-1b remains [L1 cond. on OP-S4 + SU(3) colour structure + scale closure].

## 2026-06-11 (v56 — C2-ii/scale-closure status sync)

### New results registered
- D1 (Sub-gap C2-ii): `research_tracks/EW/hypercharge_from_ubt.tex §3 Rem rem:c2ii_psi_winding`
  now explicitly states the current algebraic obstacle; C2-ii remains [OPEN/MC].
- D2 (EW-1b scale closure): `research_tracks/EW/rpsi_from_action.tex` updated with
  formal status remark; EW-1b remains [L1 conditional on OP-S4 + SU(3) colour structure + scale closure].
- D3 (proof inventory sync): `WHAT_IS_PROVED.md` synchronized for C2-i, C2-ii,
  EW-1b and G18-f exact ODE-f entry.

### Status changes
- No proof-level upgrades.
- C2-ii remains [OPEN/MC].
- EW-1b remains conditional on scale closure.

## 2026-06-11 (v55 — D1/D2/D3 results; copilot-instructions updated to v55)

### New results registered
- D1 (Sub-gap C2-i closure): `research_tracks/EW/hypercharge_from_ubt.tex §3` updated.
  Lemma `lem:Bq_from_su3` added: $B_q=1/3$ from SU(3) colour-singlet constraint
  [L1 conditional on SU(3) colour structure from UBT].
  Sub-gap C2-i: [OPEN/MC] → [L1 cond. on SU(3)].
  Gap C2 Step 1 conditionality upgraded: [L1 cond. on OP-S4 + C2-i] →
  [L1 cond. on OP-S4 + SU(3) colour structure from UBT].
  New residual sub-gap C2-ii [OPEN/MC]: $U(1)_B$ from $\psi$-winding — does not block papers.
- D2 (EW-1b after C2-i): Corollary `prop:sin2_thetaW_corollary` added to
  `research_tracks/EW/weinberg_angle_ew1_rg.tex §7`.
  $\sin^2\theta_W(M_Z)\approx0.231$ [L1 conditional on OP-S4 + SU(3) colour structure + scale closure].
  Conditionality on sub-gap C2-i removed.
- D3 (FRW ODE-f exact solutions): Proposition `prop:ode_f_full_dynamics` added to
  `canonical/gr_closure/frw_cosmological_solutions.tex §3`.
  Exact closed-form solutions: dust (Si/Ci integrals), radiation (Bessel $J_{1/4}$/$Y_{1/4}$).
  G18-f conditionality upgraded: [L1 cond. on Friedmann + quasi-static] →
  [L1 cond. on Friedmann branch only] (quasi-static approximation removed).

### Status changes
- Sub-gap C2-i: [OPEN/MC] → [L1 cond. on SU(3) colour structure from UBT]
- Gap C2 Step 1: [L1 cond. on OP-S4 + C2-i] → [L1 cond. on OP-S4 + SU(3) colour structure]
- New sub-gap C2-ii: [OPEN/MC] — $U(1)_B$ from $\psi$-winding; does not block any paper
- EW-1b ($\sin^2\theta_W$): conditionality on C2-i removed; now [L1 cond. on OP-S4 + SU(3) + scale]
- G18-f (ODE-f conditionality): [L1 cond. on Friedmann + quasi-static] →
  [L1 cond. on Friedmann branch only]
- T1_GR: historical status superseded by the 2026-07-15 covariant-tetrad audit.
- T2_GAUGE: still PAPER COMPLETE (unchanged).

## 2026-06-11 (v54 — D1/D2/D3 results; copilot-instructions updated to v54)

### New results registered
- D1 (Gap C2 Step 1): `research_tracks/EW/hypercharge_from_ubt.tex` created.
  $Y=(B{-}L)/2$ established [L1 conditional on OP-S4 + sub-gap C2-i].
  Sub-gap C2-i (fractional quark winding $B_q=1/3$ from SU(3)) remains [OPEN/MC].
- D2 (OP-S4 minimality): Remark `rem:minimality_anomaly` added to
  `canonical/chirality/step4_no_wr_derivation.tex §4`.
  Anomaly-safe (conditional on C2-i); unitarity deferred to EW-2 (open item, not inconsistency).
- D3 (FRW ODE-f): Proposition `prop:ode_f_solutions` added to
  `canonical/gr_closure/frw_cosmological_solutions.tex §3`.
  $\kappa\mathcal{T}_0 = \kappa\rho$; quasi-static solutions $f \propto a^{-3(1+w)}$
  established [L1 conditional on Friedmann + quasi-static $R_\psi \ll H^{-1}$].
- `copilot-instructions.md` updated to v54.

### Status changes
- Gap C2 Step 1: OPEN → PARTIALLY CLOSED ([L1 cond.] on OP-S4 + C2-i); sub-gap C2-i [OPEN/MC]
- OP-S4 minimality: documented in Remark (anomaly-safe conditional on C2-i; EW-2 deferred)
- FRW ODE-f: Proposition added; conditionality narrowed to [L1 cond. on Friedmann + quasi-static]
- T2_GAUGE: NEAR READY → PAPER COMPLETE (all sections done; chirality OP-S4 [L1 cond.])
- T1_GR: historical status superseded by the 2026-07-15 covariant-tetrad audit.

## 2026-06-11 (T3_ALPHA downgrade — STRUCTURAL EVIDENCE)

### Status changes
- T3_ALPHA: CONDITIONAL → STRUCTURAL EVIDENCE (time-box expired, 6 NO-GOs)
- G137-B: NARROWED → OPEN/NO-GO-RECORD (formal gap statement added)

### No new results
- No proof-level changes to any other track.
- T1_GR: historical status superseded by the 2026-07-15 covariant-tetrad audit.
- T2_GAUGE: still NEAR READY (unchanged).

## 2026-06-10 (v51 — copilot-instructions update and OP-S4 table fix)

### New results registered
- OP-S4 summary row added to T2_GAUGE table: full algebraic exclusion of $SU(2)_R$ [L1 conditional]
- `copilot-instructions.md` updated to v51 with precise task descriptions D1–D5

### Status changes
- T2_GAUGE: OP-S4 now has explicit summary row in claims table (was only in changelog/WHAT_IS_PROVED)

## 2026-06-10 (v50 — GAP-C and OP-S4 conditional closures)

### New results registered
- GAP-C sub-gap: $g_{0i}=0$ in comoving frame — [L1 conditional] via Lem.~4.1
  (spatial-averaging argument formalised); source: `canonical/gr_closure/frw_cosmological_solutions.tex`
- FRW in UBT solution space [L1], Friedmann equations [L1] — new entries G16/G17
- FRW Θ-ansatz upgraded to field-equation-matched result [L1 conditional] — entry G18
- Gap C1 Step 4: $SU(2)_R$ geometric decoupling [MC] — new entry C1-S4
- OP-S4 Loopholes 1 and 2 closed [L1 conditional], Loophole 3 closed [STD]

### Status changes
- GAP-C: OPEN → PARTIALLY CLOSED ([L1]+[L1 conditional]+[L1 conditional])
- OP-S4: PARTIAL → CLOSED [L1 conditional] (all loopholes closed conditionally/STD)

### New canonical files
- `canonical/gr_closure/frw_cosmological_solutions.tex` — added to `latex_roots.txt`
- `canonical/chirality/step4_no_wr_derivation.tex` — added to `latex_roots.txt`

## 2026-05-20 (v42 — analytické výsledky)

### Nové [L0] výsledky
- FRW N=2\dot a^2 z Cliffordovy projekce [L0]
- Z_1loop(\tau=i) = 2 z SU(2) twist sektorů [L0]
- B = 12^{3/2}\cdot(2\eta)^{1/4} z SU(2) twist [L0+MC]

### Nové [L1 conditional]
- Q\in\mathbb{Z} z U(1)_{\rm EM} holonomy na S^1_\psi při R\cdot\Lambda=1 [L1 cond.]

### Gap G137-B stav
- NARROWED: zbývá 1 MC krok (Mellin normalizace η)
- Fyzikální mechanismus: η⁻²·θ₃·θ₄² z SU(2) twist sektoru [L0]

### Zenodo v2 release: PŘIPRAVENO na víkend
<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# STATUS_OF_UBT.md — Single Source of Truth

**Author**: Ing. David Jaroš  
**Date**: 2026-05-18 *(last updated — rigour pass 2026-05-18)*  
**Purpose**: Authoritative one-file description of the real current state of every
major UBT track.  All other status files are subordinate to this document.
When in conflict, this file governs.

> **Governance rule**: This file is updated only when a track changes status,
> a gap is solved or killed, or a paper is submitted.  Date every significant change.

---

## Executive Summary

UBT has one submission-ready result (T1_GR), one paper-complete result (T2_GAUGE),
and one blocked result (T3_ALPHA).

| Track | Status | Paper | Verdict |
|-------|--------|-------|---------|
| **T1_GR** — GR Recovery | 🔶 NOT SUBMISSION-READY — DYNAMICAL BRIDGE OPEN | `papers/UBT_GR_Submission.tex` | Submit to arXiv within 2 weeks |
| **T2_GAUGE** — Gauge Sector | ✅ PAPER COMPLETE | `papers/UBT_Gauge_Submission.tex` | Submit after T1_GR clears initial review |
| **T3_ALPHA** — Fine Structure Constant | 🟡 STRUCTURAL EVIDENCE + [L1 cond.] | `information_loss_alpha_self_consistency.tex` + `layer2_kernel_derivation.tex` + `gap_A_proof.tex` | α⁻¹_UBT=137.035999177549 (+0.026σ) [L1 cond.] via info-loss route. A_PRIME/G137-B: TIME-BOX EXPIRED. α NOT DERIVED unconditionally. |
| **quantum_ubt** — Quantum UBT Scope | 🔶 SCOPED | Research notes | graviton kvantizace [STD], NCG [MC] |

**No speculative tracks are active.**  Consciousness/CTC content is frozen in
`speculative_extensions/`.  No new branches are being opened during the cleanup window.

**Execution control**: Top-10 priority/gap implementation instructions and locked
sequencing are maintained in `ROADMAP.md` under
`Implemented Top-10 Priority/Gaps Program (Execution-Control Layer)`.


## 2026-05-21 (v41 — opravy a nové výsledky)

### Opraveno
- Gap G137-B: chybný NO-GO odstraněn, starý blok smazán
- Status: NARROWED (ne NO-GO)
- Algebraická identita η⁻²·θ₃·θ₄² = 2η(i) [L0] zapsána

### Nové výsledky
- Weinberg RG: 1-loop výsledek 0.185, 2-loop [STD] 0.231
- FRW N konzistence: dimenzionální problém formalizován [OPEN]
- Gap G137-B minimální teorém: přesná formulace zbývajícího kroku
- τ₁∘τ₂∘τ₃=id ověřeno z Pauliho matic [L0]

### Zbývá
- Gap G137-B: odvodit proč η⁻²·θ₃·θ₄² z S[Θ] na T³ při τ=i
- FRW N: fixovat dimenzionální projekci η_B → spinorový prostor
- C2 Step 1: plný důkaz p=3,q=2 z ℂ⊗ℍ

## 2026-05-20 (v39)
- Tests: 539 PASS, 2 FAIL (only .git missing in ZIP — CI OK)
- find_repo_root: fallback to pyproject.toml [FIX]
- Gauge PDF: compiled ✓
- NCG B₀ PDF: compiled ✓
- GR arXiv ZIP: ready ✓
- Zenodo v2 package: prepared ✓
- C2: Dirac on T² [MC/candidate — p=3,q=2 derivation pending]
- Hosotani: Wilson line minimum computation [T6]
- Gap G137-B: NO-GO verdict removed, narrowed to algebraic identity [L0-B1]
- FRW: explicit T_μν computation [T8]

## 2026-05-19 (v33)
- C2 uniqueness: [L1 family check] — gravitational anomaly selects n=1
- Gap G137-B: 5 NO-GO, formal downgrade memo added
- Gauge abstract: updated with [L1 family check]
- Higgs: m²_eff < 0 [MC/NUM], CW potential benchmark phi_min=0 [NUM]
- FRW+dS: de Sitter Λ=3H² [Prop.] formalized (Cor.)
- ΔN_eff: g*_total=198 < 389 → [TENSION] recorded
- Zenodo v2 checklist: updated, awaiting author instruction

## 2026-05-19 (v35)
- ΔN_eff: reformulated as CONDITIONAL TENSION (g* open problem)
- Python: ImportError fixed (ubt.spectral stub added)
- Gauge PDF: compiled [T3]
- NCG B₀ PDF: compiled [T4]
- GR arXiv ZIP: ready [T5]
- Zenodo v2 checklist: finalized [T6]
- Hosotani mechanism: new route for Higgs SSB [T8]
- C2: Dirac quantisation argument [T9]

## 2026-05-18 Rigour pass

### Opravy
- GR paper: Cl⁺₁,₃ (even subalgebra) opraveno [P1]
- GR paper: indefinitní vnitřní součin pro $\mathcal N$ zaveden [P1]
- N_eff: dvě různé routes jasně odděleny [P3]
- ΔN_eff: napětí závisí na g*(T_dec); pro benchmark g*≥427 OK, numerický práh je ~389 [P5]
- Gap C2 Step 1: blokér formalizován [P4]

### Aktuální stav
- arXiv: GR ZIP ready po P1/P9/P10/P14/P15
- Gap G137-B: NARROWED, minimální teorém formulován [P7]
- Weinberg: [CONDITIONAL on C2 Step 1]
- Alpha: NOT DERIVED

## 2026-05-18
- GR paper: arXiv ready (Cl^+, indefinite bilinear opraveny)
- Gauge PDF: compiled locally in `papers/UBT_Gauge_Submission.pdf`
- NCG B₀ PDF: compiled locally in `papers/ncg_poisson_B0_derivation.pdf`
- Python testy: 4/4 targeted scaffold files PASS; full `tests/` collection still has unrelated missing deps/modules
- GR arXiv ZIP: `/tmp/ubt_gr_arxiv.zip` ready
- Gap G137-B: Eisenstein $E_4$ route checked --- [NO-GO], gap remains OPEN
- ΔN_eff: g* scan gives Planck-safe threshold $\sim389$; explicit field-content bound remains $120.75\le g_*\le216.75$
- FRW: formal Proposition recorded in `frw_from_ubt.tex`
- Soliton: first numerical result added in `src/ubt/solitons/regularization.py`

## 2026-05-18 (v32)
- Gauge PDF: zkompilován [T1]
- NCG B₀ PDF: zkompilován [T2]
- Python testy: 4/4 PASS [T3]
- GR arXiv ZIP: ready [T4]
- Gap G137-B: Eisenstein E_4 route aktivní [T5] --- current verdict [NO-GO]
- ΔN_eff: g* scan, konzistentní pro g*≥389 [T6]
- FRW: formální Proposition [T7]
- Soliton: první numerický výsledek [T10]

## 2026-05-17

| Item | Prev status | New status | Source |
|------|-------------|------------|--------|
| NCG B₀ paper | draft pending | compiled PDF (6 pages, 0 fatal errors) | `papers/ncg_poisson_B0_derivation.pdf` |
| Gauge Submission PDF | pending | compiled PDF (8 pages, 0 fatal errors) | `papers/UBT_Gauge_Submission.pdf` |
| ΔN_eff prediction | OPEN (uncomputed) | computed: 0.131/mode, 1.569 naive total; benchmark 0.247 for g*=427 | `research_tracks/quantum_ubt/delta_neff_prediction.tex` |
| Gap G137-B Casimir T³ | unexplored | EXPLORED & CLOSED: B_Casimir ≪ B_phenom; ratio ~1.3×10⁻³ | `research_tracks/T3_ALPHA/mellin_insertion_B.tex §8` |
| FRW from UBT (GAP-C) | OPEN | First steps: refined ansatz formulated; Friedmann [Prop.] | `research_tracks/quantum_ubt/frw_from_ubt.tex` |
| Higgs from S[Θ] (EW-2) | OPEN | First steps: tree-level check (no V(Θ)); CW setup described | `research_tracks/EW/higgs_from_theta.tex` |
| T-dualita | [NO-GO local ansätze] | [NO-GO local ansätze; OPEN globally] | `research_tracks/T3_ALPHA/mellin_insertion_B.tex` |
| C2 uniqueness | OPEN/MC frozen | OPEN/MC frozen — anomálie cesta neselektuje n=1 | unchanged |

## Status update 2026-05-14

| Item | Prev status | New status | Source |
|------|-------------|------------|--------|
| EW-1b (R_psi from S[Θ]) | CONDITIONAL | PROVED [L1 conditional] | rpsi_from_action.tex |
| N_eff=12 SU(2) twist | [L1] | [L1] confirmed | step2_AUDIT.tex |
| N_eff loop-counting | [OPEN/MC] | [OPEN/MC frozen] | step2_AUDIT.tex |
| Proton decay prediction | — | defined τ_p~10³⁴ yr | falsifiable_prediction_sheet.md |
| Anomaly cancellation | OPEN | OPEN (Σ Q³≠0 charge-only) | anomaly_cancellation.tex |
| C2 uniqueness | OPEN | OPEN/MC frozen | colour_charge_lattice.tex |
| Gap G137-B | NARROWED | NARROWED (τ=i [OBS]) | mellin_insertion_B.tex |

## 2026-05-14 update
- Anomaly cancellation (chiral): [NUM/L1 conditional on C2]
- EW-1b: PROVED [L1 conditional]
- T-duality: lemma formulated [OPEN/MC]
- Gap G137-B: T³ volumetric factor identified as source of 3/2 exponent

---

## T1_GR — General Relativity Recovery (current covariant-tetrad status)

**Status**: RESEARCH DRAFT — not submission-ready  
**Canonical manuscript**: `papers/UBT_GR_Submission.tex`

### Proved local kinematics and connection structure

| Claim | Status | Source |
|---|---|---|
| Central Lorentz metric from the anticommutator of `E_mu=N0^(-1/2)D_mu Theta` | PROVED locally | `canonical/gr_closure/covariant_tetrad_rank_theorem.tex` |
| Tetrad-to-metric differential has rank 10; kernel has dimension 6 | PROVED locally | same; `tools/verify_covariant_tetrad_rank.py` |
| Specified tetrad and torsion uniquely determine the metric-compatible frame connection | PROVED [L1] | `canonical/gr_closure/gap_10omega_connection_elimination.tex` |
| Torsion-free classical branch gives the unique Levi-Civita spin connection | PROVED [L1] | same; `tools/verify_gap_10omega_connection.py` |
| Metric-compatible connection preserves the Lorentz slice | PROVED [L1] | same |
| Every constant Lorentz tetrad has an explicit affine single-Theta representer | PROVED [L1] | `canonical/gr_closure/gap_10i_integrability_selection.tex` |
| Minkowski representer has zero second derivatives | PROVED [L1] | same; `tools/verify_gap_10i_integrability.py` |
| Naive one-sided invertible curved route forces zero curvature | PROVED NO-GO [L1] | same |
| Two-sided derivative satisfies exact left/right curvature identity | PROVED [L1]; identity alone is not an existence theorem | same |
| Pure Lorentz pairing reduces A,B to one spin connection | PROVED [L1] | `canonical/gr_closure/gap_10i_paired_connection_audit.tex`; `tools/verify_gap_10i_paired_connection.py` |
| Torsion-free pure Lorentz pairing implies a concurrent vector and excludes the non-flat Schwarzschild vacuum exterior for M!=0 | PROVED NO-GO [L1] | same |
| Every smooth Lorentzian tetrad has a local single-Theta representer with explicit composite metric-compatible contortion | PROVED LOCALLY [L1] | `canonical/gr_closure/gap_10i_torsionful_local_representer.tex`; `tools/verify_gap_10i_torsionful_local_representer.py` |

### Open dynamical bridge

| Gap | Status |
|---|---|
| GAP-10T-PALATINI — minimal algebraic torsion equation | CLOSED CONDITIONALLY [L1] |
| GAP-10T-SPIN — direct fixed-background matter current | CLOSED CONDITIONALLY [L1] |
| GAP-10T-FLAT-NOGO — minimal affine torsion-free branch | CLOSED AS NO-GO [L1] |
| GAP-10T-PAIRING-NOGO — Lorentz-invariant pairing escape route | CLOSED AS NO-GO [L1] |
| GAP-10T-DCOMP-WL-SECTOR — Lorentz-real W_L subsector | CLOSED CONDITIONALLY [L0] |
| GAP-10T-DCOMP-LIN-OFFRES — linearized off-resonance flatness | CLOSED CONDITIONALLY [L1] |
| GAP-10T-DCOMP-LIN-REALFREQ — frozen real-frequency curved-mode sector | CLOSED AS NO-GO [L1] |
| GAP-10T-DCOMP-RES — six-dimensional real-exponential symbol sector | OPEN |
| GAP-10T-GRADIENT-FLATNESS — exact-gradient composite branch | CLOSED AS NO-GO [L1] |
| GAP-10T-DYN — canonical self-consistent D-composite variation and torsion completion | NARROWED |
| GAP-10I-PAIR-KIN — no-new-field Lorentz reduction | CLOSED [L1] |
| GAP-10I-PAIR-GR — torsion-free GR under the pure Lorentz pair | CLOSED AS TORSION-FREE NO-GO [L1] |
| GAP-10I-TORSION-LOCAL — local representer with composite contortion | CLOSED LOCALLY [L1] |
| GAP-10I-2S — relative bimodule action | NOT REQUIRED FOR LOCAL KINEMATICS; optional torsion-free route |
| GAP-10I-PRESCRIBED — augmented-holonomy criterion for specified coefficients | CLOSED [L1] |
| GAP-10I-CURVED — self-consistent curved-space generation | LOCAL KINEMATICS CLOSED; DYNAMICS/GLOBAL NARROWED |
| GAP-10L-SYM — preservation by unique equivariant dynamics | CLOSED CONDITIONALLY [L1] |
| GAP-10L-DYN — verify canonical equivariance/well-posedness | NARROWED |
| GAP-10D-PALATINI / UNIQUENESS — conditional infrared endpoint | CLOSED CONDITIONALLY [L1] |
| GAP-10D — derive infrared assumptions and coefficients from UBT | NARROWED |
| GAP-10ψ-KIN / SYM — gauge and symmetry protection mechanisms | CLOSED / CLOSED CONDITIONALLY [L1] |
| GAP-10ψ — canonical selection and physical stability | NARROWED |
| GAP-B-MASTER — perturbation bridge from original master dynamics | OPEN |
| GAP-U2Θ — canonical generation of the full Schwarzschild tetrad/lapse | OPEN |

The former compact-ψ fiber-average closure, phase-projection metric, and
`Gamma=Re(Omega)` formula are historical or exploratory only.  The canonical
GR route is the covariant tetrad, unique connection reconstruction, and
left/right integrability program.

### Next action

Derive from the canonical UBT action whether the composite-contortion branch
is selected (or whether an auxiliary torsion-free relative action is selected),
then prove physical torsion compatibility and global continuation near the explicit
Minkowski solution.  Only after that should the repository attempt on-shell
Schwarzschild/Kerr/FRW construction or an Einstein dynamical bridge.

---

## T2_GAUGE — Standard Model Gauge Structure

**Status**: PAPER COMPLETE — all sections §1–§9 complete; chirality OP-S4 [L1 conditional]; α at STRUCTURAL EVIDENCE
**Confidence**: HIGH for algebraic sector; MEDIUM for chirality claim
**Paper**: `papers/UBT_Gauge_Submission.tex` (compiled PDF)

### Solved Algebra Pieces (Zero New Work Needed)

All claims below are [L0] algebraic identities or [L1] proved theorems.

| Claim | Level | Source |
|-------|-------|--------|
| ℂ⊗ℍ ≅ Mat(2,ℂ) ≅ Cl₁,₃(ℝ) | [L0] | `canonical/algebra/biquaternion_algebra.tex` |
| 𝔰𝔲(3) from ℤ₂×ℤ₂×ℤ₂ involutions | [L0] | `canonical/su3_derivation/su3_from_involutions.tex` |
| Quarks in **3**, gluons in **8**, EW/strong decoupling | [L0] | `canonical/interactions/sm_gauge.tex` |
| Triqubit one-hot detects every single `X_i`/`Y_i` as leakage (`GAP-SU3-TRIQUBIT-LEAKAGE`) | **[L1 CLOSED]** | `canonical/interactions/gap_su3_triqubit_qec.tex` |
| Present one-hot encoding fails single-`X_i` correction and general `Z_i` detection (`GAP-SU3-TRIQUBIT-QEC`) | **[L1 NO-GO]** | Knill--Laflamme witness in `gap_su3_triqubit_qec.tex` |
| SU(2)_L from left norm-preserving action | [L0] | `canonical/interactions/sm_gauge.tex §SU2` |
| SU(2)_L acts on left-chiral doublets (Gap C1 closed) | [L1] | `canonical/chirality/step3_gap_C1_resolution.tex` |
| SU(2)_R geometric decoupling via ψ-parity (Gap C1 Step 4) | [MC] | `canonical/chirality/step4_no_wr_derivation.tex §3 Thm 3.1` |
| Loophole 1 (n<0 coupling) observationally decoupled | [L1 conditional] | `canonical/chirality/step4_no_wr_derivation.tex Cor 3.2` |
| Loophole 3 (KK decoupling, R_ψ→0) | [STD] | `canonical/chirality/step4_no_wr_derivation.tex Prop 4.3` |
| Loophole 2 (spontaneous breaking) — no light $SU(2)_R$ doublet in minimal $S[\Theta]$ | [L1 conditional] | `canonical/chirality/step4_no_wr_derivation.tex §4 (Lemma no_doublet)` |
| Minimality: anomaly-safe (cond. on SU(3) colour); unitarity deferred to EW-2 | Remark | `canonical/chirality/step4_no_wr_derivation.tex §4 Rem rem:minimality_anomaly` |
| Full algebraic exclusion of $SU(2)_R$ (OP-S4) | **[L1 conditional]** — all three loopholes closed; conditional on Step 1 Lem 4 + minimality of $S[\Theta]$ | `canonical/chirality/step4_no_wr_derivation.tex §4` |
| U(1)_Y from right scalar phase | [L0] | `canonical/interactions/sm_gauge.tex §U1` |
| U(1)_EM from ψ-cycle phase | [L0] | `canonical/interactions/qed.tex` |
| Three generations from ψ-winding | [L0] | `canonical/n_eff/` |
| Hypercharge quantisation from Dirac condition | [L0] | `canonical/qed_phi_const/appendix_alpha_geometry.tex §1` |
| $Y=(B{-}L)/2$ from OP-S4 + SU(3) colour (Gap C2 Step 1) | **[L1 cond. on OP-S4 + SU(3) colour structure from UBT]** | `research_tracks/EW/hypercharge_from_ubt.tex §2 Lem lem:hypercharge_formula` (v56) |
| Sub-gap C2-i: $B_q=1/3$ from UBT SU(3) colour-singlet constraint | [L1 cond. on SU(3) colour structure from UBT] | `research_tracks/EW/hypercharge_from_ubt.tex §3 Lem lem:Bq_from_su3` (CLOSED v56) |
| Sub-gap C2-ii: $U(1)_B$ from $\psi$-winding | [OPEN/MC] | `research_tracks/EW/hypercharge_from_ubt.tex §3 Rem rem:c2ii_psi_winding`; Lem `lem:c2ii_candidate` [MC] added v57; C2-iii obstacle named (does not block papers) |

The triqubit theorem is a representation-level quantum-simulation encoding result. It does not derive a physical noise model, decoder/recovery, or a Matrix/simulation ontology.

### Open Physical Gaps

| Gap | Description | Priority |
|-----|-------------|----------|
| EW-1 | Weinberg angle sin²θ_W — **DEAD END for pure algebra** (algebra cannot fix g'/g) | Keep dead-end statement for algebra-only route |
| EW-1b | EW1+RG branch ($\sin^2\theta_W^{\mathrm{GUT}}=3/8 \rightarrow \sin^2\theta_W(M_Z)\approx0.231$) | [L1 cond. on OP-S4 + SU(3) colour structure + scale closure] — C2-i conditionality removed (v56); tracked in `research_tracks/EW/weinberg_angle_ew1_rg.tex §7 Prop prop:sin2_thetaW_corollary` |
| EW-2 | Higgs doublet VEV from S[Θ] | Deferred to separate Higgs paper |
| C2-i | $B_q=1/3$ from SU(3) colour-singlet constraint | **CLOSED [L1 cond. on SU(3) colour structure from UBT]** — v56 |
| C2-ii | $U(1)_B$ from $\psi$-winding topology | [OPEN/MC] — Lem `lem:c2ii_candidate` [MC] v57; C2-iii sub-obstacle [OPEN/MC]; does not block any current paper |
| C2-iii | Geometric coupling $S^1_\psi \leftrightarrow \mathbb{Z}_3$ colour cycle | [OPEN/MC] — blocks C2-ii closure; does not block papers; Steps 1+2 attempted v58, Approach (b) v59 (see Rem. rem:c2iii_attempts) |
| C2-iv | Fiber Decoupling: $S^1_\psi$ (imaginary-time) and colour fiber $\mathbb{C}^3$ are algebraically decoupled in $S[\Theta]$ | **[FORMAL NO-GO within current $S[\Theta]$]** — v59; all 3 routes NO-GO; root cause of C2-iii; does not block papers; derivation deferred (requires $S[\Theta]$ extension) |
| Y2 | Yukawa couplings | Open |
| Dynamical confinement | Wilson loop area law | Clay Millennium Problem |

### Confidence

**Overall**: PAPER COMPLETE — submit after T1_GR clears initial review.

**Honest statement to use in paper**: The Weinberg angle sin²θ_W ≈ 0.231 cannot
be derived from algebra alone (dead-end no-go for pure algebraic fixing of g'/g).
The EW1+RG route gives $\sin^2\theta_W(M_Z)\approx0.231$ [L1 cond. on OP-S4 +
SU(3) colour structure + scale closure]; conditionality on sub-gap C2-i removed (v56).

### Next Action

Submit T2\_GAUGE paper after T1\_GR submission clears initial review.

Master status file: `canonical/gauge/GAUGE_MASTER_STATUS.md`

---

## T3_ALPHA — Fine Structure Constant

**Global Objective**: Derive α⁻¹_bare = 137 (integer) without fitting.
Full derivation (137.036) requires solving Gap G137-B first.

**Status**: STRUCTURAL EVIDENCE — downgraded 2026-06-11 after six NO-GOs; α remains NOT DERIVED

### Active Routes

| Route | Status | Confidence | Blocker | Continue? |
|-------|--------|------------|---------|-----------|
| **A_PRIME: V_eff Prime Attractor** | **TIME-BOX EXPIRED** | HIGH (conditional) | Gap G137-B | NO — 6 NO-GOs on record |

**What is proved in A_PRIME**:
- N_eff^twist = 12 — [L1]: closed on the SU(2)-twist route; the independent
  scalar-loop count remains N_eff^loop = 3 [L1], and the identification
  twist = loop is still OPEN/[MC] (see `canonical/n_eff/step2_AUDIT.tex`)
- V_eff structure has a motivated prime/winding/entropy route, but the full
  derivation from S[Θ] remains conditional.
- n*(B_phenom) = 137 for B_phenom ≈ 46.298 [L1] (conditional on B)
- Prime stability of n* is a structural property [L0]
- $\vartheta_3(0|i)/\eta(i)=\sqrt{2}$ [STD], Ramanujan form
  $B=12^{3/2}\cdot2^{1/8}\cdot\vartheta_3(0|i)^{1/4}$ [OBS]
- Seeley-DeWitt consistency checkpoint: $a_2$ Einstein-Hilbert reproduction
  [Prop.], $a_4\propto\vartheta_3(0|i)$ remains [MC]/OPEN

**What remains open in A_PRIME** (Gap G137-B):
- Derive B_phenom ≈ 46.298 from S[Θ] without using α as input.
- B₀ = 8π (one-loop, proved) gives n* ≈ 65, not 137.
- The missing factor ≈ 1.84 corresponds to a Kac-Moody level or higher-loop correction.

### Gamma Entropy Audit Results (2026-05-11)

The Gamma/prime-factorization entropy interpolation audit produced the following
high-precision numerical results (all at B_Ram **[OBS]**, not derived from S[Θ]):

| Quantity | Value | Status |
|----------|-------|--------|
| n1 (V1 stationary point) | 136.9890996341 | [L1] given B_Ram |
| α⁻¹_exp (CODATA 2018) | ≈ 137.036 | [PHENOM] |
| n3 (V3 stationary point) | 137.0905214131 | [DERIVATION CANDIDATE] given B_Ram |
| λ_exact (exact stationarity) | 0.4622175427 | **[OBS]** |
| λ_frac (linear fractional) | 0.4624199099 | **[OBS]** |

**Bracket property** [OBS]: n1 < α⁻¹_exp < n3.
The measured fine-structure constant inverse lies strictly between the V1 and V3
stationary points — a structurally suggestive observation that does **not** close
G137-B.

**B_Ram** = 12^(3/2) · 2^(1/8) · θ₃(0|i)^(1/4) ≈ 46.2809 — **[OBS] only**.
Not derived from S[Θ].

**λ** — fit parameter — **[OBS] only**. No derivation from S[Θ] is known.
Nearest candidate constant: 37/80 = 0.4625 (0.06% deviation from λ_exact — NUMERIC_ONLY, no UBT meaning).

**G137-B remains OPEN. Alpha is NOT DERIVED.**

Cross-references:
- `canonical/alpha/gamma_entropy_alpha_refinement_status.tex` — LaTeX status document
- `reports/gamma_entropy_alpha_interpolation_audit.md` — full numerical audit

### Parked Routes

| Route | Reason | Revival condition |
|-------|--------|-------------------|
| A1: Gauge Normalization | Conditional on Gap EW-1 (pure-algebra Weinberg route is dead end; EW-1b conditional) | Only if EW-1b is closed in T2_GAUGE |
| A2: Symmetry-Breaking Projection | Same blocker as A1 (EW-1 + EW-2) | Same |

### Dead-End Routes

| Route | Verdict | Evidence |
|-------|---------|----------|
| **A3: Theta/Modular Route** | **DEFINITIVELY FAILED** | Exhaustive search — no modular invariant = 137.036 |
| **A4: Layer 2 Coding Constraint** | **DEFINITIVELY FAILED** | Proved impossible: coding fixes spectrum, not coupling magnitude |

Archive: `reports/failed_routes_graveyard.md`

### Decision Gate Outcome (2026-06-11)

- The 4-week modular bootstrap time-box expired without closing Gap G137-B.
- Six routes are now on record as NO-GO; see `research_tracks/T3_ALPHA/mellin_insertion_B.tex`.
- ✅ Conditional integer-137 companion note written: `research_tracks/T3_ALPHA/integer_137_note.tex` (2026-06-11).
- Primary effort is redirected to T1_GR submission and T2_GAUGE completion.
- **Do not pursue** A1, A2, A3, A4, or any new alpha route without explicit instruction.

### Modular symmetry sync (2026-06-11, updated to FINAL)

| Claim | Status | Source |
|-------|--------|--------|
| $\psi$ compact from SS boundary condition | [L1] | `su2_twist_neff12.tex` |
| $\psi$ compact from periodicity $|Z[\tau+1]|^2=|Z[\tau]|^2$ | [L0] | `modular_symmetry_rpsi.tex Prop~\ref{prop:compact}` |
| $Z[\tau_E]=\eta(\tau_E)^{-12}$ from $\det P=\eta^2$ [STD] + $N_{\mathrm{eff}}=12$ [L1] | [L1 conditional] | `modular_symmetry_rpsi.tex Prop~\ref{prop:Z}` |
| $\tau_E=i$ unique S-fixed point on $\{iR_\psi : R_\psi>0\}$ | [L0] | `modular_symmetry_rpsi.tex Def~\ref{def:sdp}` |
| $\mathrm{Re}\,S[\Theta]$ stationary at $\tau_E=i$ (modular flow) | [L0] | `modular_symmetry_rpsi.tex Prop~\ref{prop:Smod}` |
| $R_\psi=1$ fixed point from $Z[\tau]$ symmetry | [L1 conditional] | `modular_symmetry_rpsi.tex Thm~\ref{thm:fixed}` |
| Polynomial $R^6+R^4+R^2=3$, unique solution $R=1$ | [L0] | `modular_symmetry_rpsi.tex Thm~\ref{thm:poly}` |
| $N_{\mathrm{eff}}$ cancels — result holds for any $N_{\mathrm{eff}}$ | [L0] | `modular_symmetry_rpsi.tex Thm~\ref{thm:poly}` |
| S-invariance of $S_{\mathrm{eff}}$ (Path 1 condition) | [MC] post-hoc justified by Path 2 | `modular_symmetry_rpsi.tex §7` |
| S-invariance of $S[\Theta]$ from first principles | [OPEN] | not yet derived |
| Implications for $\alpha$: $\tau=i$ algebraically preferred | [L0] (consequence) | `modular_symmetry_rpsi.tex §8` |
| Alpha | **NOT DERIVED** | — |
| Conditions for [L1 cond.]: $\det P=\eta^2$ [STD]; $N_{\mathrm{eff}}=12$ [L1]; one-loop approx. [technical] | explicit | `modular_symmetry_rpsi.tex Prop~\ref{prop:Z}` |

Master portfolio file: `canonical/alpha/ALPHA_PORTFOLIO_MASTER.md`  
Detailed route audit: `canonical/alpha/ALPHA_MASTER_STATUS.md`  
Gamma entropy audit: `canonical/alpha/gamma_entropy_alpha_refinement_status.tex`,
`reports/gamma_entropy_alpha_interpolation_audit.md`

---

## Exploratory Tracks

### Side Ideas Worth Preserving

| Topic | Location | Status | Note |
|-------|----------|--------|------|
| ΔN_eff ≈ 0.046 (CMB-S4 prediction) | `research_tracks/` | OPEN | Above CMB-S4 threshold; publishable as prediction |
| Structural colour confinement (algebraic) | `canonical/su3_derivation/` | PROVED [L0] | Distinct from dynamical confinement; include in T2_GAUGE |
| ASD Weyl condition and twistor correspondence | `canonical/geometry/` | PROVED [L1] | Include in T1_GR appendix or follow-on paper |
| Hecke eigenvalue lepton mass ratios | `research_tracks/hecke_bridge/` | [MC] — strong (0.02%) | Corroborates A_PRIME; preserve, do not publicise as proved |

### Frozen Items

| Topic | Location | Reason frozen |
|-------|----------|---------------|
| Complex Consciousness Theory / Psychons | `speculative_extensions/complex_consciousness/` | No mathematical closure; frozen indefinitely |
| Closed Timelike Curves | `speculative_extensions/appendices/` | Speculative; no experimental anchor |
| p-adic dark sector | `research_tracks/p_universes/` | Interesting; deferred beyond 21-day window |
| Cosmological solutions (GAP-C) | `canonical/gr_closure/frw_cosmological_solutions.tex` | PARTIALLY CLOSED — FRW [L1]; Θ-ansatz [L1 conditional]; $g_{0i}$ comoving [L1 conditional] — v50 |

---

## Deprecated Claims

| Old Claim | Where It Appeared | Why Deprecated | Replacement |
|-----------|-------------------|----------------|-------------|
| Weinberg angle derivation is a CRITICAL PRIORITY | `canonical/alpha/weinberg_angle_derivation.md`, `reports/ew_mixing_status.md` | No-go argument proves pure algebra cannot fix g'/g; continuous deformations of the SU(2)_L × U(1)_Y embedding change tan θ_W continuously | State pure-algebra DEAD END + EW-1b conditional branch in T2_GAUGE paper §6 |
| "Four active α routes" | `canonical/alpha/alpha_derivation_routes.md` (dated 2026-04-27) | Routes A3 and A4 are definitively killed (exhaustive scan + proved impossibility) | One primary route (A_PRIME), two parked, two killed |
| Chirality Gap C1 as merely MOTIVATED [SE] | `reports/gauge_status_matrix.md` (line 70), `reports/chirality_gap.md` | Formal proof exists: `canonical/chirality/step3_gap_C1_resolution.tex` | C1 is [L1] PROVED — SU(2)_L acts on left-chiral doublets |
| α⁻¹ = 137.036 claimed derivable via B_base/k=1 Kac-Moody route | Multiple early α documents | 27+ approaches exhausted; k=1 has not been proved; this specific number is not the claim | Claim is α⁻¹_bare = 137 (integer), conditional on Gap G137-B |
| N_eff=12 (SU(2) twist route) | [L1] | step2_AUDIT.tex §Final verdict: N_helicity=2 [L1], N_eff=12 [L1], B₀=8π [L1] |
| N_eff=12 (loop counting, independent) | [OPEN/MC] | step2_AUDIT.tex: N_charge double-counting unresolved |

**Note 2026-05-14**: The SU(2)-twist route gives N_eff=12 [L1] (step2_AUDIT.tex). The earlier loop-counting route remains [OPEN/MC]. These are two separate claims; both are tracked.

---

## Repository Public Face

| Document | Status |
|----------|--------|
| `docs/comparison_table.html` | ✅ Vytvořeno — srovnávací tabulka teorií |

---

## Key Source Files

| Purpose | File |
|---------|------|
| What is proved (complete map) | `WHAT_IS_PROVED.md` |
| Cross-track claims matrix | `CLAIMS_MATRIX.md` |
| Derivation level standard | `DERIVATION_STATUS_STANDARD.md` |
| GR claim-to-proof matrix | `reports/GR_claim_to_proof_matrix.md` |
| GR claim strength table | `reports/GR_claim_strength_table.md` |
| GR consolidated review | `reports/GR_REVIEW_MASTER.md` |
| GR canonical manuscript | `papers/UBT_GR_Submission.tex` |
| Alpha portfolio master | `canonical/alpha/ALPHA_PORTFOLIO_MASTER.md` |
| Alpha route detail | `canonical/alpha/ALPHA_MASTER_STATUS.md` |
| Gauge sector truth | `canonical/gauge/GAUGE_MASTER_STATUS.md` |
| Forward plan | `ROADMAP.md` |
| Contradictions resolved | `reports/contradictions_resolved.md` |
| File cleanup log | `reports/files_merged_deleted_redirected.md` |
| Repo integrity check | `reports/repo_integrity_check.md` |
