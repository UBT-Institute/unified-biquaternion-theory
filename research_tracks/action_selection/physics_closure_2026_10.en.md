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
Palatini or a freely selected connection. Exact 9/9 tests;
C_working, dynamical action OPEN.
