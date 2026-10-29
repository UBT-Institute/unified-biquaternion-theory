<!-- BILINGUAL-UNIT: single-action.provenance -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: B_machine_verified
ai_assistance: disclosed
human_review: machine-verification
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Machine-verified against named sources or verifiers; individual attestation is not claimed.
UBT-AI-PROVENANCE-END
-->

# The single-action invariant of UBT

<!-- BILINGUAL-UNIT: single-action.physics-closure -->
## Physics closure audit

The [action and constrained-Hamiltonian audit](../research_tracks/action_selection/physics_closure_2026_10.en.md) classifies a restricted constant-coefficient geometric family and derives the full constrained Hamiltonian of the existing homogeneous Palatini–Holst comparator. The effective gravity postulate is an `AXIOMATIC_CANDIDATE`; its physical recovery claims are `CONDITIONAL`. The Holst and torsion coefficients remain unselected. Neither the restricted Hamiltonian nor the independent-connection vacuum equivalence finalizes `S_UBT[Theta]` or supplies a distinctive beyond-GR prediction.

<!-- BILINGUAL-UNIT: single-action.bare-splitjet-proof -->
## Bare-action proof boundary independent of the component count

The [dimension-independent proof](../research_tracks/action_selection/physics_closure_bare_action_2026_10.en.md) establishes the local variational core for any real Theta variation space. If the kinetic pairing is the same one defining the composite metric, the potential has no derivatives and algebraic jet variations freely span the tetrad, the bare action is `int nu_E F(Theta)`. With independent field variations stationarity transmits `F=0` and `dF=0`. At a critical zero every locally representable tetrad is stationary; an explicit regular closed-FLRW witness violates the Einstein condition for every cosmological constant. Its critical Hessian has no metric kinetic block. This excludes a GR derivation from that specified family, not all UBT actions or quantum completions. Lean proves the encoded algebra/calculus; the functional and curvature interpretations have independent analytic/CAS checks and explicit formal limits.

The author clarified that the proposed component count is provisional. Dimensions of the currently written core describe that model, not a derived physical minimality theorem. This proof assumes no fixed field dimension and selects no replacement carrier. Other pairings, derivative interactions or composite connection laws require their own consistent action and variation.

<!-- BILINGUAL-UNIT: single-action.rule -->
## Binding rule

UBT shall have exactly one fundamental action. The symbol
`S_UBT[Theta]` is reserved exclusively for that action. A sector-specific
functional may be called only a reduction, effective action, auxiliary action,
or historical candidate, and its derivation map from `S_UBT` must be stated.
Two inequivalent functionals must never both be cited as “the canonical UBT
action”.

The canonical source already defines a kinetic/potential family

`S_Theta = 1/2 int sqrt(-g) <D_mu Theta,D^mu Theta> - kappa V[Theta]`.

It explicitly leaves the kinetic sign/scale, `kappa`, and the form of `V`
as dynamical inputs and does not derive the complete gravitational action.
The current registry value is therefore:

```yaml
fundamental_action_family: S_Theta
source: canonical/THEORY/canonical/canonical_action.tex:46
status: DEFINED_FAMILY_NOT_FINALIZED
related_open_gap: UBT-FUND-GR-ACTION
```

Until finalization is complete, a bare reference to “the canonical action” is
not an admissible premise for closing a dynamical gap.

<!-- BILINGUAL-UNIT: single-action.inventory -->
## Conflicting formulas currently in canonical sources

| Source | Measure/domain | Real scalar prescription | Classification |
|---|---|---|---|
| `THEORY/canonical/canonical_action.tex` | `sqrt(-g) d4x` | abstract pairing | declared canonical family; sign, scale, `kappa`, and potential not finalized |
| `appendices/appendix_ACTION_review.tex` | `sqrt(-g) d4x` | complex trace/Hermitian terms | postulated GR + Yang–Mills + matter effective action, not a Theta-only derivation |
| `bridges/theta_quantum_structure.tex` | `sqrt(|det G|) d4x dτ` | abstract pairing | higher-dimensional quantum candidate; cited derivation is not the current canonical source |
| `8pi_common_origin.tex` | `d4x dψ` | `Re Tr` | induced-gravity candidate/attempt |
| `qm_emergence/step4_fpe_equivalence.tex` | `d4x` | both `Sc` and `Re(Sc)` variants | ordering/reality candidates for a QM reduction |
| `qm_emergence/step2_schrodinger_emergence.tex` | `sqrt(-g) d4x` and `d4x` | dagger product | relativistic scalar reduction candidates |
| `qm_emergence/step1_fpe_check.tex` | `dQ dT` | complex kinetic form | nonrelativistic effective candidate |
| `alpha/prime_selection_principle.tex` | `d4x dτ dτbar` | unspecified contraction | modular-sector candidate |
| `symmetry/effective_vs_fundamental_breaking.tex` | `sqrt(-g) d4x` | placeholder `L_UBT` | placeholder, not a definition |
| `n_eff/step2_AUDIT.tex` | `d4x dψ` | `Sc` | scalar-loop reduction used for an audit |

These formulas differ in integration domain, reality prescription, independent
fields, and dynamical content. They are therefore not interchangeable
notations for one established action.

<!-- BILINGUAL-UNIT: single-action.requirements -->
## Finalization requirements

The finalized `S_UBT[Theta]` must specify, without sector-dependent replacement:

1. configuration space and whether `psi` is a coordinate or a field;
2. microscopic integration measure and quotient/Jacobian;
3. a real-valued biquaternionic pairing;
4. all independent versus composite connections and metrics;
5. derivative order, potential, boundary terms, and free parameters;
6. the full Euler–Lagrange equations and gauge-fixed Hessian;
7. stability of physical and `psi` modes;
8. explicit reduction maps to the GR, Yang–Mills, matter, and QM effective
   actions.

Dimensional consistency, symmetry, and boundedness are necessary tests, not a
selection proof. The action is selected only if its unconstrained variation is
well defined and the claimed sector actions follow from it rather than being
inserted as additional fundamental terms.

The first theorem-critical subtask now has an exact result for a sharply stated
ansatz. For a generic `X=rho(Theta)` in `Mat(2,C)`, under
`X -> exp(i alpha) S X S^dagger` with `S` in `SL(2,C)`, every real local
polynomial potential of degree at most four is

\[
 V(X)=V_0+m^2H(X)+\lambda_1H(X)^2+\lambda_2|\det X|^2,
 \qquad H(X)=\operatorname{Tr}(X^\sharp X^\dagger).
\]

The quadratic invariant space has dimension `1` and the quartic invariant
space has dimension `2`. The exact rank proof and an independent rational
checker are recorded in
`research_tracks/action_selection/theta_potential_invariants.en.md`. The
positive Hermitian quantity `Tr(X^dagger X)` is excluded by an explicit
nonunitary boost counterexample. This classification fixes the invariant basis,
not the real coefficients.

The boundedness problem for this complete quartic family is also exact. It is
bounded below precisely in the following coefficient regions: `lambda1 > 0`
with `lambda2 >= 0` and arbitrary `m^2`; or `lambda1 = 0`, `lambda2 > 0`,
`m^2 <= 0`; or the constant case `lambda1 = lambda2 = m^2 = 0`. More
importantly, every coefficient choice has the noncompact ray

\[
 X_t=t\begin{pmatrix}1&0\\0&0\end{pmatrix},
 \qquad H(X_t)=|\det X_t|^2=0,
\]

on which `V(X_t)=V0`. Therefore potential tuning alone cannot make the generic
field-space potential coercive. This ray alone does not exclude a nonzero
minimum or determine isolation modulo symmetries. The exact proof,
witness rays, and CI checker are recorded in
`research_tracks/action_selection/theta_potential_stability.en.md`.
`research_tracks/action_selection/biquaternionic_potential_vacuum.en.md`
constructs a nonzero global minimum for `lambda1>=0`, `lambda2>0`,
`m^2<0` and gives its nonnegative Hessian in all eight real field directions.
Coefficient selection and a compatible nondegenerate spacetime background
remain open. The full action, including its derivative, gauge and constraint
structure, must determine the physical fluctuations.

## Conditional Hamiltonian bridge (new, not finalization)

The existing kinetic/potential family admits an exact fixed-background ADM
Legendre transform when its real kinetic pairing is nondegenerate. A normalized,
decoupled scalar channel then reduces exactly to the previously derived
dodecahedral test-field Hamiltonian. The same calculation establishes that an
unconstrained indefinite kinetic pairing has a negative-energy momentum
direction. See `research_tracks/action_selection/canonical_family_hamiltonian_bridge.en.md`
for hypotheses, equations, proof and remaining Dirac-constraint obligations.
**This does not change** `DEFINED_FAMILY_NOT_FINALIZED` or establish the
full composite-field Hamiltonian.

### Exact invariant kinetic-sector obstruction (conditional)

For the declared generic matrix representation and connected Lorentz/phase
congruence symmetry, the sole invariant real quadratic form is
`H(X)=Tr(X^sharp X^dagger)`; its full 8-real inertia is **(2,6)**.
At the proven pointwise quartic minimum `X0=i r I`, the four-dimensional
normal to the phase/boost orbit has kinetic inertia **(1,3)** while the
potential Hessian is positive there. With the connection frozen, the
three normal-vector modes grow exponentially for positive kinetic sign
(and the scalar normal mode grows for negative sign).
See Propositions 4-5 and the exact SymPy/pytest certificate in
`research_tracks/action_selection/canonical_family_hamiltonian_bridge.en.md`.
This is a **fixed-background no-go**, not a full constrained UBT ghost
proof: the zero-connection constant minimum has a degenerate tetrad.
Variation of the complete composite metric and connection and Dirac
constraint reduction may change the physical spectrum.

There is a second structural boundary: the bare family with connections
entering only through `D_mu Theta` has no derivatives of those
connections, hence no classical propagating Yang--Mills connection
kinetic term. Connection variations are algebraic. An induced
effective gauge action remains to be demonstrated, not presumed.
Neither conclusion selects a finalized fundamental action.

## Exact kinetic-spectrum obstruction in the existing quartic family

The Lorentz/phase-invariant quadratic pairing is
\(H(X)=2(|z_0|^2-\sum_{j=1}^3|z_j|^2)\), with real kinetic signature
\((2,6)\). Combining that pairing with the previously proved nonzero
quartic-potential minimum gives an exact transverse generalized
mass-squared spectrum containing one eigenvalue proportional to
\(+(4\lambda_1+\lambda_2)/c\) and three proportional to
\(-\lambda_2/c\). In the **unconstrained fixed-background realization**,
one or more long-wavelength modes are therefore unstable for every
nonzero real kinetic normalization \(c\). The velocity Hessian has full
rank eight; potential-orbit symmetries do not themselves generate
Theta-only primary constraints.

This is a new **conditional no-go** for a naive stable eight-component
realization, not a no-go for the full constrained/composite UBT theory.
See [theta_kinetic_spectrum.en.md](../research_tracks/action_selection/theta_kinetic_spectrum.en.md)
and the executable exact checker
tools/verify_theta_kinetic_spectrum.py. The fundamental action is
**still not finalized**: its dynamical constraints must be computed
before any ghost-free claim is upgraded.

### Bare-family gauge-connection limitation

When an independent connection appears **only algebraically** through
the covariant derivative of Theta, the minimal kinetic/potential family
contains no derivatives of that connection. Its fixed-background
connection Euler--Lagrange equations are algebraic and its connection
momenta vanish. Therefore a propagating Yang--Mills curvature kinetic
term does **not** follow at tree level from this bare family.
The full composite-metric variation, a derived induced gauge action,
or a separately justified curvature-dependent single action would
require additional analysis. See Proposition 6 in
[canonical_family_hamiltonian_bridge.en.md](../research_tracks/action_selection/canonical_family_hamiltonian_bridge.en.md).
The fundamental action remains **DEFINED_FAMILY_NOT_FINALIZED**.

**Stronger quadratic check:** when independent nonpropagating phase/boost
connections are actually varied and eliminated around the nonzero potential
minimum, they remove four orbit-tangent derivatives but leave the normal
kinetic signature (1,3) and its infrared instability. This excludes the
naive auxiliary-gauge repair on that fixed background, not a full constrained
UBT completion. See Proposition 7 of the Hamiltonian bridge and
`tools/verify_theta_auxiliary_connection_reduction.py`.

**Timelike Lorentz-real branch:** assuming a consistent positive-Hermitian
Lorentz-real slice and an independent auxiliary SL(2,C) connection, the
radial scalar can be stable for positive kinetic normalization.
But the same exact algebraic connection equation forces its on-shell
covariant tetrad to have rank at most one on a prescribed metric.
Thus this naive stable reduction does not generate a nondegenerate
emergent UBT spacetime. See Proposition 8 of the Hamiltonian bridge
and tools/verify_theta_timelike_auxiliary_rank.py. Full composite-metric
variation may evade the restricted no-go and remains OPEN.

**Composite-metric result (stronger restricted no-go):** On the
Lorentz-real timelike branch with the central metric constructed from
the same covariant Theta derivative, the invariant kinetic contraction
is identically -8*N0. The minimal kinetic/potential action therefore
collapses to a volume term. Varying independent auxiliary boost
connections forces U(rho)=4*c*N0 at any nondegenerate tetrad;
for the nonconstant classified quartic this makes rho constant and
the tetrad degenerate. Proposition 9 proves this exactly for the
specified branch. It excludes that minimal completion, **not**
curvature-dependent or other dynamically justified single-Theta actions.

<!-- BILINGUAL-UNIT: single-action.falsification -->
## Precommitted falsification criterion

Once a finite-dimensional candidate family has been explicitly declared, the
minimal single-action programme fails if every admissible member fails at
least one of the following simultaneous tests:

- a nonzero, finite two-derivative Einstein–Hilbert coefficient in the infrared;
- stable physical fluctuations with no unremoved ghost or unstable `psi` mode;
- a derived Yang–Mills kinetic structure on the selected carrier;
- a consistent real measure and variational principle.

Failure is a result about the limits of the proposed UBT dynamics. It is not
permission to introduce another object under the same name without recording
a new theory choice and rerunning the complete comparison.

<!-- BILINGUAL-UNIT: single-action.prediction -->
## Quantitative-prediction guardrail

At present no zero-parameter quantitative UBT prediction is registered here as
derived from a unique fundamental action. A recovered or renormalized
coefficient calibrated from observation is not such a prediction. The first
accepted prediction must state its numerical value, uncertainty, experimental
observable, and all inputs before comparison with data.

<!-- BILINGUAL-UNIT: single-action.causal-test -->
## Einstein-style causal-consistency audit (no new action)

The measured light speed `c_light` is an **empirical consistency
constraint**, not a new microscopic variational or selection principle.
The final, gauge-reduced UBT equations must have a well-posed causal
initial-value problem compatible with the observed light cone. Any
additional cones must follow from the **same** action and be tested
against observation. Positivity of the physical Hamiltonian and
linearized stability are **separate** requirements.

An exact fixed-background result for the already studied invariant
eight-real-component kinetic family is

\[
\det P=256\kappa^8
\left(|\mathbf k|^2-\omega^2/c_{\rm light}^2\right)^8.
\]

Thus that **unconstrained conditional family** has one characteristic
cone despite its indefinite internal kinetic signature \((2,6)\).
Neither this determinant nor holomorphy in \(\tau=t+i\psi\)
establishes physical ghost freedom or the causal cones of the
full composite UBT action. See
[Einstein causal principle](../research_tracks/causality/einstein_causal_principle.en.md)
and the exact checker `tools/verify_ubt_causal_cone.py`.

<!-- BILINGUAL-UNIT: single-action.priority -->
## Programme priority and scope freeze

Until the fundamental action is finalized, new speculative sectors do not
count as progress on the canonical theory and must not introduce further
fundamental terms. The canonical physics order is:

1. finalize the already defined single action family;
2. vary it without fitting the result to a desired endpoint;
3. determine its Hessian, degrees of freedom, and stability;
4. derive sector reductions from that same object;
5. only then compare a preregistered quantitative prediction with data.

Lean work is prioritized for finite theorem-critical algebra already carrying
an L0 claim: the biquaternion/matrix/Clifford equivalence, tetrad-to-metric
rank and Lorentz kernel, contortion-to-torsion rank, and Lorentz-invariant
pairing no-go. Formal proofs of logical implications whose physical premises
remain assumed must be labelled as such and do not close action-level gaps.
