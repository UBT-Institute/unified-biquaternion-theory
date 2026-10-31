<!-- BILINGUAL-UNIT: physics-closure.scope -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Physics closure audit: action freedom and a constrained Holst Hamiltonian

**28 October 2026; PR #807; C_working.** This report uses the existing covariant tetrad, split-jet and homogeneous calculations. It does not select a microscopic action. The effective gravity postulate is an `AXIOMATIC_CANDIDATE` with `CONDITIONAL` physical consequences. Its local mathematical implications remain valid under their stated assumptions; observational confirmation of UBT does not follow. English is the translation source.

<!-- BILINGUAL-UNIT: physics-closure.reuse -->
## Reused results and claim corrections

The rank theorem, split-jet right inverse, auxiliary multiplier theorem, Clifford trace classification, potential classification, determinant null Lagrangian and homogeneous curvature calculation already exist. Relevant sources are `canonical/ACTION.en.md`, `canonical/gr_closure/gravity_dynamical_postulate.en.md`, `formal/lean/UBT/GR/VolumePrincipalSymbol.lean`, `research_tracks/action_selection/clifford_palatini_trace_selector.en.md`, `research_tracks/action_selection/composite_palatin_holst_flrw.en.md`, and `research_tracks/observer_information_hamiltonian_2026_10_holst_causal_selector.en.md`. They are premises with their original scope, not new discoveries in this PR.

Einstein–Lambda recovery, Schwarzschild inclusion and its Regge–Wheeler/Zerilli reductions have status `CONDITIONAL` as UBT claims: they require the adopted gravity functional. Their mathematical implication is not retracted. Microscopic selection of that functional and direct on-shell selection by a finalized one-Theta equation remain `OPEN_GAP`. The current paired claim matrix and machine-readable gravity ledger now distinguish these levels. Older unpaired ledgers retain their historical text; their open microscopic gaps must not be read as disproof of the conditional effective branch.

The alpha ledger remains `OPEN_GAP`. Values near $B\simeq46.28$ are fitted/phenomenological inputs or numerical matches in alternative formulas, not a parameter-free derivation. The nearby historical values are not a measured universal constant. Algebraic colour carriers do not establish propagating QCD, and winding labels do not derive three chiral generations. No author signature, attestation date or provenance tier is changed.

<!-- BILINGUAL-UNIT: physics-closure.proof-outcome -->
## Dimension-independent proof outcome

The author clarified that the component count is provisional; this audit selects no replacement carrier. A new theorem uses an arbitrary real variation space. In the stated matched-pairing/free-jet bare family, stationarity gives only a critical zero of the volume weight and admits an explicit non-Einstein metric. Thus this family does not derive GR. Different kinetic channels, a dynamically selected jet closure or a derived quantum effective action remain outside that obstruction. The detailed proof, original-readout witness and formal limits are in the bare-action appendix. There are 7 new Lean declarations; the full functional/PDE conclusion is not claimed as a completely formalized spacetime theorem.

<!-- BILINGUAL-UNIT: physics-closure.details-index -->
## Detailed derivations

This is the single audit overview; paired appendices preserve the detailed equations, hypotheses, proofs and counterexamples.

- [Action family and independent variation](physics_closure_action_family_2026_10.en.md)
- [One-clock Hamiltonian and self-dual comparison](physics_closure_hamiltonian_2026_10.en.md)
- [Carrier, symmetry and common-connection theorem](physics_closure_carrier_2026_10.en.md)
- [Phase, texture and quotient checks](physics_closure_phase_texture_2026_10.en.md)
- [Real dilation and full chain variation](physics_closure_dilation_2026_10.en.md)
- [Dimension-independent bare-action proof](physics_closure_bare_action_2026_10.en.md)
- [Spin-source response and bulk coefficient identifiability](physics_closure_spin_source_2026_10.en.md)

<!-- BILINGUAL-UNIT: physics-closure.prediction -->
## Nonuniqueness, information principles and prediction boundary

For independent-connection spinless vacuum the entire real $b$ family has the same torsion-free metric equations. Its gravitational characteristics and all protocols confined to that identical metric branch cannot distinguish $b$. This strengthens the existing torsion-free restriction comparison by explicitly checking the invertible vacuum connection operator. Information-access budgets and causal sharing of records restrict protocols; without a new coupling or selection rule they do not remove this degeneracy. Off shell the operators differ, and sourced torsion or other boundary prescriptions may distinguish them. This is nonuniqueness under the tested constraints, not impossibility of a future stronger principle.

On that conditional branch the metric wave characteristic obeys $g^{\mu\nu}k_\mu k_\nu=0$, so $c_{\rm GW}=c$ as in GR. [GW170817/GRB170817A](https://arxiv.org/abs/1710.05834) supplies a published comparison bound $-3\times10^{-15}\le(c_{\rm GW}-c)/c\le7\times10^{-16}$ under its emission-delay assumptions. This is a GR baseline check, not distinctive confirmation of UBT or a measurement of $b$. With spinless vacuum alone there is no nontrivial beyond-GR prediction from this family. A source/torsion experiment would require the same action to derive the normalized spin current and every allowed torsion coefficient first. [Kostelecky–Russell–Tasson](https://arxiv.org/abs/0712.4393) constrain specified fermion–background-torsion couplings; their limits cannot be transferred to an unspecified UBT coefficient. The homogeneous comparator is not a fitted cosmology or an observational prediction.

The precise remaining obstruction is that neither the complete single-Theta action, its composite connection law, its physical fluctuation quotient nor its source normalization has been selected. A surjective kinematic right inverse supplies none of these by itself. Full spatial variations, primary/secondary constraints and physical mode stability remain `OPEN_GAP`. The strongest new calculational result here is the constrained Hamiltonian and its coefficient-dependent strata for the already specified comparator.

<!-- BILINGUAL-UNIT: physics-closure.verification -->
## Verification and exact formal scope

| Result | Scientific status | Verification | Formal boundary |
|---|---|---|---|
| Real bivector inverse, square and zero kernel | PROVED | `formal/lean/UBT/Hamiltonian/PalatiniHolst.lean`; independent SymPy matrix | No derivation of the field Cartan equation |
| Comparator momentum/constraint, zero canonical energy, velocity inversion, completed square | PROVED | Same Lean module; direct CAS differentiation | Finite algebraic identities only |
| Continued canonical GR match and Hermitian-pair readout obstruction | PROVED | Same Lean module; `tests/test_holst_selfdual_canonical_gr.py` | Matching is algebraic; no admissible microscopic self-dual branch established |
| Carrier, phase, gauge-cancellation and real Cartan algebra | PARTIAL | Same Lean module; `tests/test_holst_carrier_assumptions.py` | Six new Lean lemmas; exact matrix witnesses are checked in CAS; general equivariant bundle/PDE classification is LEAN-PENDING |
| Conditional real-dilation variation and closed de Sitter example | CONDITIONAL | `tools/verify_physics_closure.py`; same carrier test | Imported action and distinguished relative jet; no new UBT postulate or unrestricted Dirac theorem |
| Bare weighted-volume stationarity and non-Einstein witness | PARTIAL | `formal/lean/UBT/GR/BareSplitJet.lean`; `firstVariation_at_vacuum`; `tools/verify_bare_splitjet_selection.py` | Dimension-independent algebra/calculus and finite contradiction; smooth functional and curvature interpretation is LEAN-PENDING and checked independently |
| Full homogeneous Poisson matrix, Dirac brackets and constraint strata | CONDITIONAL | `tools/verify_physics_closure.py`; `tests/test_physics_closure.py` | LEAN-PENDING: Poisson/Dirac definitions and geometric reduction |
| Finite differences, covariance, trajectory convergence and precision | NUMERICALLY_TESTED | Same executable verifier, fixed seed and tolerances | Selected regular samples, not proofs |
| Generic torsionful single-Theta dynamics and new physical prediction | OPEN_GAP | Exact missing inputs stated above | LEAN-PENDING: full action, variational spaces and PDE constraints |
| Claim that the one-clock Palatini reduction automatically enforces all Einstein equations | REFUTED | Preserved exact normal-constraint counterexample | Only the stated homogeneous ansatz is excluded |

Run `python tools/verify_physics_closure.py` and `python -m pytest -q tests/test_physics_closure.py tests/test_holst_selfdual_canonical_gr.py tests/test_holst_carrier_assumptions.py tests/test_composite_palatin_holst_flrw.py`. The verifier emits package versions, every exact check, the seed, finite-difference errors, independent integrator convergence and precision residuals. Run `lake build UBT --wfail`, the existing Lean checker and the axiom audit separately. No unchecked theorem source or successful numerical comparison is formal verification. Independent bilingual semantic approval is required before merge; a structurally matched translation alone does not close that gate.

<!-- BILINGUAL-UNIT: physics-closure.full-spatial -->
## Full spatial dynamics after metric reduction

The [full spatial calculation](full_spatial_dynamics_2026_10.en.md) derives the local refoliation bracket within a declared reduced canonical metric family, selects the Einstein trace ratio and relative curvature coefficient, and gives the complete vacuum metric evolution and two flat tensor modes. Its canonical phase space and off-shell refoliation requirement are explicit additional assumptions. It does not select the microscopic Theta action, the Newton magnitude, the Holst coefficient or the extra-sector dynamics.

<!-- BILINGUAL-UNIT: physics-closure.spatial-jet-dirac -->
## Canonical jet reduction of the chosen gravity branch

The [local spatial Dirac reduction](splitjet_spatial_dirac_2026_10.en.md) constructs an equivalent gravity-only parent, retains the field-dependent carrier-momentum shift, and eliminates the mixed auxiliary constraint blocks without changing the base brackets. The additional jet variables contribute no local physical mode on a regular non-null chart. This resolves the jet part of the metric phase-space bridge for the chosen action, while the origin and positive normalization of that action and all additional complex/matter sectors remain open.

<!-- BILINGUAL-UNIT: physics-closure.flat-jet-torsion -->
## Flat-jet quadratic torsion action test

The [flat-jet torsion calculation](flat_jet_torsion_action_2026_10.en.md) varies the declared flat-Lorentz/closed-real-dilation configuration space fully. Every constant-coefficient parity-even quadratic torsion action reduces there to a conformal scalar action. The positive Einstein-sign combination has a negative reduced scalar kinetic direction; the opposite sign gives a positive scalar energy but no tensor sector. A regular curved on-shell witness fails the Einstein vacuum equation for every cosmological constant. This excludes this precise branch as a generic GR origin, while nonflat jets, other relative actions and microscopic selection remain open.

<!-- BILINGUAL-UNIT: physics-closure.free-jet-tensor -->
## Free-jet tensor principal test

The [free-jet tensor calculation](free_jet_torsion_principal_2026_10.en.md) allows curved Lorentz jets and unrestricted real dilation on a timelike isotropic branch. The supplied quadratic torsion family regains a tensor time kinetic term with positive Einstein-sign normalization, but algebraic variation of all rotational jet auxiliaries removes the spatial TT gradient for every coefficient choice, including singular choices. This is a necessary principal-block obstruction, not a complete mode count. A regular exact original-field stationary background is non-Einstein for every cosmological constant. An additional derived connection law or functional is needed before this family can recover the GR tensor wave operator; microscopic selection remains open.

<!-- BILINGUAL-UNIT: physics-closure.composite-connection-rank-20261031 -->
## Physical Lorentz-connection variation: exact normal-cokernel boundary

The [paired exact projection audit](composite_lorentz_variation_rank_2026_10.en.md)
does not repeat the earlier Cartan, Holst or split-jet results.
For fixed non-null real carrier X, a **pure physical Lorentz**
connection perturbation induces a tetrad response with rank 12,
but its composite canonical metric response has rank **9**:
the normal Euler projection along the carrier-induced spacetime
vector V is absent from this one variation channel.
A distinct *relative* real dilation restores rank **10**
algebraically, but is not a selected physical connection.

In the fixed-gamma Clifford lower-order comparator, the previous
24-to-8 spin contraction and the rank-9 metric projection form
a joint 24-to-16 map with kernel dimension **8**. This is
a pointwise algebraic visibility count and not an off-shell
physical-mode theorem; the full operator varies its gamma matrices
and curvature. The next microscopic gate is the admissible
single-Theta variation bundle and the surviving normal
equation after all constraints, not an independently imported
Palatini or a freely selected connection. Exact 11/11 tests;
C_working, dynamical action OPEN.

<!-- BILINGUAL-UNIT: physics-closure.normal-transport-adjoint-20261031 -->
## Carrier Euler variation: transport is weaker than the normal metric equation

[Exact local formal-adjoint witness](composite_normal_transport_adjoint_2026_10.en.md)
continues the rank-9 physical-Lorentz-only metric variation result
from PR #817. With a fixed scale, regular e=D_omega X/s
and an independently varied Lorentz omega, the carrier
Euler equation is the covariant divergence of the tetrad
Euler density. When the fixed-tetrad connection source C_omega
vanishes, the joint carrier/Lorentz equations still admit
P^mu_a=lambda V^mu X_a, with
partial_mu(lambda V^mu)+s lambda=0 rather than lambda=0.
A smooth timelike chart with X=x and lambda=t^-5
gives a **nonzero symmetric metric Euler source** annihilating
all 24 Lorentz variations and all 4 carrier Euler equations.

This is a constructed formal-adjoint source, NOT a
stationary solution of the unfinalized S_UBT or an
action-level no-go. The previously known independently
varied relative dilation w detects this residual source
algebraically, but the physical permission and dynamics
of w still require one selected fundamental action.
11/11 exact SymPy controls; C_working, action OPEN.

<!-- BILINGUAL-UNIT: physics-closure.theta-normal-adjoint-20261031 -->
## Full X plus physical Lorentz variation: normal adjoint kernel

The [exact restricted adjoint audit](theta_normal_adjoint_kernel_2026_10.en.md)
goes beyond the prior rank-9 fixed-X result by varying both the
original Lorentz-real field X and its physical Lorentz connection.
The field Euler equation is the covariant divergence of the
independent tetrad Euler density, NOT the whole tetrad equation.

A nonzero normal source E^mu_a=h V^mu X_a is invisible to
every antisymmetric connection variation. A local first-order
transport equation for h also annihilates its field Euler
variation. An explicit timelike h=(-X^2)^(-5/2) source and
a prescribed EXTERNAL metric-source functional demonstrate
both cancellations with 13 exact independent SymPy tests.
The test is strengthened by a nonzero-curvature SO(3) stabilizer
connection with omega_mu X=0: the actual defining tetrad remains
regular, and the simultaneous normal adjoint kernel persists.
A second homogeneous transport family confirms local profile
nonuniqueness, not physical propagating modes.
The full restricted verifier now has 13 exact SymPy tests.
The external functional is NOT an admissible UBT microscopic
action, and no physical non-Einstein on-shell claim follows.

The action-level selection problem now is whether the ACTUAL
Euler-source image of a chosen single-complex-Theta action
intersects this formal kernel after physical Cartan sources,
all Clifford grades, relative jets, boundaries and constraints.
C_working; single-Theta dynamics remain OPEN.

<!-- BILINGUAL-UNIT: physics-closure.exact-relative-weyl-norm-gate -->
## Exact relative dilation: normal recovery and norm-only degeneracy

The [paired exact-Weyl selection audit](exact_relative_weyl_norm_gate_2026_10.en.md)
reuses the previously known closed relative-dilation
construction, rather than presenting it as a new field mechanism.
If an exact scalar phi is INDEPENDENTLY varied with X, the
coupled variation delta X=epsilon X, delta phi=-epsilon
gives delta e=epsilon e with no derivative of epsilon.
With the existing 9-dimensional Lorentz metric image, the
pointwise metric response reaches rank 10 and detects the
normal formal Euler source of PR #819.

If phi must instead be a **Lorentz-invariant ultralocal
function only of X squared**, the uniquely compensating
choice is phi=-log(abs(X squared))/2. This forces
X contracted with e to vanish, hence the regular coframe
and its canonical sharp metric degenerate (rank at most 3).
The result is a scoped no-go for that norm-only route,
not for full complex Theta, its independent Clifford grades,
derivative closures or the unfinished single action.
11 exact SymPy regressions; microscopic dynamical selection OPEN.

<!-- BILINGUAL-UNIT: physics-closure.full-theta-hermitian-relative-20261031 -->
## Full Theta: Hermitian-determinant relative center and curved sharp witness

The [paired full-Theta audit](full_theta_hermitian_compensator_2026_10.en.md)
reuses the existing Hermitian/anti-Hermitian split of the SAME
four-complex-component biquaternion. On a nondegenerate
positive-Hermitian patch, insisting that the entire defining
jet remain on the classical i-Hermitian slice, together with
a traceless SL(2,C) spin connection, **forces**
w=-d log(det H)/2. The full remaining matrix condition
requires the normalized H to be covariantly parallel;
choosing w from its trace alone does not enforce that.

This built-in field-dependent relative jet permits a
local scaling variation of the ORIGINAL Theta with
delta e=epsilon e and a nonzero normal Euler pairing,
without a separate scalar field. An explicit nonflat
sharp-metric witness has det e=-1-4ab z^2,
R^x_yxy=-12ab at the spatial origin, and noncommuting
SU(2) curvature. The complete original sharp metric and
4-by-4 Clifford anticommutator are checked in
20 exact local SymPy regressions.

The mechanism is conditional kinematics, not microscopic
action selection. Positive H reduces the allowed spin
holonomy, central complex phase covariance is not automatic,
and the Hermitian determinant is not holomorphic in the
unrestricted complex field. The actual connection equations,
physical torsion constraints and reduced healthy dynamics
remain OPEN.

<!-- BILINGUAL-UNIT: physics-closure.dynamics-reuse-H-MM-adjoint -->
## Integrated dynamics audit and derived-H MM adjoint gate

The [consolidated evidence ledger](dynamics_reuse_hermitian_mm_adjoint_2026_10.en.md)
explicitly reuses the existing GR conditional action, Palatini/Cartan
and split-jet proofs, ADM modes, and the documented first-principles
action nonselection. It gives a new restricted **formal differential
adjoint-injectivity** theorem: for a gravity-only pullback of the
already chosen MM/Palatini action, free algebraic K_J variations,
the original X Euler equation and a joint H/X scale variation
enforce the complete tetrad Euler equation even if the relative
one-form is derived as w=-d ln(det H)/2 instead of varied freely.
The complete fixed-e Cartan equation follows afterward.
15/15 local exact SymPy regressions passed.

**Crucial connection separation:** varpi is the defining H-parallel jet spin and omega is the independently varied physical spin in the geometric action. The older auxiliary coordinate may be shifted as K_J=K_old+omega-varpi; the separate variable is not selected from the original full-Theta bimodule. Identifying varpi with torsion-free physical omega would force a parallel timelike direction and exclude generic nonzero-Lambda Einstein vacua. The proof does not establish full solution-set equivalence without this separation.

**Non-negotiable representation gate:** this assumes K_J is a
separate real-linear auxiliary action on the X jet. Using the SAME
SL(2,C) spin coefficient on H and X violates this premise:
H reality excludes the boost directions needed for the rank.
An anti-Hermitian-only projection is not complex linear on
unrestricted Theta. The full two-sided/graded intertwiner and
its admissible action, extra complex sectors and physical
constraints remain OPEN. No additional gravity ansatz was adopted.

<!-- BILINGUAL-UNIT: physics-closure.full-theta-graded-reallinear -->
## Full-Theta equivariant graded auxiliary jet: representation gate resolved in real-linear category

The [paired exact construction](full_theta_reallinear_graded_jet_2026_10.en.md)
introduces no new fundamental field or gravity functional.
An algebraic sl2(C) auxiliary tensor K acts only on the
already-existing anti-Hermitian component P_-(Theta),
via K P_-(Theta)+P_-(Theta) K†. This **real-linear**
graded jet is exactly Lorentz-equivariant under local
SL2(C) congruence while preserving the Hermitian
parallelism constraint and the canonical central-sharp
metric. Independent K at a non-null carrier has rank 12
in its coframe response; the existing determinant-derived
relative w cancels local REAL scaling gradients.

The same theorem excludes nonzero COMPLEX-linear maps
on Mat2(C) annihilating every Hermitian direction.
The constructed graded jet is not equivariant under an
independent central complex phase. This phase is already
known not to be a homogeneous gauge of the locked sharp
metric (old #701 theorem); no new phase no-go is claimed.
18 exact local SymPy regressions cover the result.
The previous MM conditional Euler-pullback theorem can
use this **explicit candidate representation**, but
microscopic action selection, phase/time admissibility,
complex matter and Dirac constraint closure remain OPEN.
