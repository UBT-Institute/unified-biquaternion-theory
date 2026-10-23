# Scalar energy, gauge constraints and GR: cross-repository bridge

**Status:** C-tier working research note; no new UBT axiom, no microscopic action selected, no new prediction.  
**Date:** 2026-10-23  
**Baseline:** UBT master after #700 and #635 (commit `123c98cea7e1750edbf8d639264ec6a035e7a9b0`).

## Scope and provenance

- Historical diagnostic: [DavJ/research PR #3](https://github.com/DavJ/research/pull/3), `audits/scalar_g/README.md`, commit `9baee5f4410a38529252b28994ecfcd0acdb4db3`. **As checked on 2026-10-23, the PR was open, not merged.** Eighteen exact symbolic checks passed on its head; tests are not experiments or proofs of the present UBT.
- Current UBT definitions: [canonical/AXIOMS.md](../../canonical/AXIOMS.md), [canonical/ACTION.en.md](../../canonical/ACTION.en.md).
- Hamiltonian/symmetry obstruction: [canonical_family_hamiltonian_bridge.en.md](canonical_family_hamiltonian_bridge.en.md).
- First-jet and selection obstruction: merged [UBT PR #700](https://github.com/UBT-Institute/unified-biquaternion-theory/pull/700).
- Conditional Einstein–Lambda completion: merged [UBT PR #635](https://github.com/UBT-Institute/unified-biquaternion-theory/pull/635); [GR recovery ledger](../../canonical/gr_closure/gr_recovery_status.yaml).

This note is a comparison and a *test specification*, not a derivation of cosmological acceleration from scalar G.

## 1. Two distinct scalar objects

In the historical electromagnetic potential model,
```math
G_{\mathrm{old}}=c^{-2}\partial_t\phi+\nabla\cdot\mathbf A,
\qquad
G'_{\mathrm{old}}=G_{\mathrm{old}}-\Box\chi.
```
Under standard Maxwell gauge redundancy, `G_old` is not a gauge-invariant local observable. The smooth decaying pure gauge `chi=a exp(-r²/L²)` produces zero E and B but nonzero finite `integral G_old²`. The old energy product also fails its claimed mixed-sign scalar expansion. For a single unrestricted real vector, `L=-F²/4+lambda (div A)²/2` has an unbounded canonical Hamiltonian for either nonzero lambda. **This excludes that specific physical interpretation; it does not exclude a new constrained/composite UBT scalar.**

For canonical UBT, `E_mu=N0^(-1/2) D_mu Theta` and `g_mu nu 1=(E_mu^sharp E_nu+E_nu^sharp E_mu)/2` on the admissible real Lorentz slice. A candidate scalar `s[Theta,DTheta,...]` is **not** to be identified with `G_old` without a defined reduction map and gauge transformation law.

## 2. Cosmological acceleration is not negative local energy density

For an effective homogeneous perfect-fluid component in the Einstein limit (with cosmological constant absorbed into the effective fluid),
```math
\frac{\ddot a}{a}=-\frac{4\pi G_N}{3}
\left(\rho_{\mathrm{eff}}+\frac{3p_{\mathrm{eff}}}{c^2}\right).
```
Acceleration requires `rho_eff+3p_eff/c²<0` for that dominating component, not `rho_eff<0`. A positive vacuum density `rho_Lambda` with `p_Lambda=-rho_Lambda c²` suffices. Negative pressure and a negative kinetic Hamiltonian direction are logically different statements. Treat any negative scalar *energy* as an unproved claim, not as observation.

## 3. Where the current UBT already advances beyond the historical model

1. Axiom C gives a composite coframe and metric and a conditional local rank-ten construction. It does not yet derive a unique action or establish the complete constrained phase space.
2. The existing canonical-family bridge derives a fixed-background Hamiltonian and an invariant real quadratic kinetic signature `(2,6)` in the stated congruence representation. Its negative directions apply to the *unconstrained* test-field realization. A physical quotient could alter the verdict but must be exhibited.
3. Merged #700 rules out nontrivial dynamics for the specified natural algebraic first-jet, timelike Lorentz-real class; it does **not** rule out curvature, torsion, extra derivatives, complex branches or nonlocal/topological sectors. It also exhibits the action-selection ambiguity after admitting curvature/torsion terms.
4. Merged #635 adopts a *low-energy* Palatini/Henneaux–Teitelboim completion with one continuous action coupling and an auxiliary pair. Variation of the three-form gives `dLambda=0`, so `Lambda_0` is integration data. It supplies conditional local Einstein–Lambda recovery, **not a microscopic Theta-only selection theorem**, a value for Lambda, or a propagating dark-energy scalar.

## 4. Hypotheses to test, not assumptions to import

**H0 (economical null):** all candidate scalar excitations reduce to gauge/constraint/auxiliary data. The classical IR cosmology is Einstein–Lambda with no additional propagating scalar.

**H1 (healthy scalar):** a gauge-invariant composite `s[Theta]` survives the Dirac constrained phase-space quotient, with a nonnegative physical kinetic quadratic form, well-posed perturbations and a derived stress tensor. Its cosmological equation of state must follow from the selected action. H1 is not established and might be excluded by the final constraints.

**H2 (global/state selection):** microscopic/global UBT data constrain the unimodular integration constant `Lambda_0`. A relation to the numerical observed value must be calculated, not claimed from `dLambda=0` alone.

Do not insert an independent `lambda G_old²` term, adopt a ghost as dark energy, or count `Lambda_0` as a prediction.

## 5. Exact cross-track gates and falsification criteria

| Gate | Input | Required output | Failure criterion |
| --- | --- | --- | --- |
| G1: transformations | Explicit `Theta` gauge action and candidate `s` | Symbolic `delta_gauge s=0`, or a justified gauge-fixed/relational observable | Nonzero variation under a redundancy |
| G2: constraints | Proposed *single* `S_UBT[Theta]`, independent vs composite variables | Hessian rank, primary/secondary constraints, first-/second-class classification, DOF count | Unconstrained negative kinetic direction |
| G3: energy | Fully reduced Hamiltonian and boundary assumptions | Lower bound or a clearly specified stable physical sector | Negative-energy scaling family in physical initial data |
| G4: IR gravity | Same action plus reduction map `Theta -> E -> g` | Einstein–Lambda equations and matter coupling, without postulating a separate sector action | GR appears only by inserted EH term without a reduction |
| G5: cosmology | Derived stress tensor and homogeneous solution | `rho_s,p_s,w_s`; perturbation ghost/gradient checks | Acceleration inferred merely from negative local energy |
| G6: differentiation | H0 versus surviving H1/H2 | At least one parameter-controlled observable distinguishable from Einstein–Lambda | Only a reparameterization of an integration constant |

## 6. Smallest next derivation

**Start with G1–G2, not a new potential.** On the existing split-jet regular local patch, write the transformation of `E_mu=N0^(-1/2)D_mu Theta` under each declared internal and local Lorentz symmetry; test central scalar invariants made from `E`, its antisymmetric bivector `Sigma_mu nu`, and existing curvature/torsion objects. Categorize algebraically independent *invariants* without selecting coefficients. For each surviving invariant, establish whether it is auxiliary/constraint data in the already adopted IR sector before interpreting it as a scalar excitation. Next derive the full composite-Theta Hessian of a genuinely selected microscopic action **if and only if one is provided by an independent selection principle**. In the meantime the correct status is `UBT-FUND-GR-ACTION: OPEN`.

### Acceptance conditions for follow-up PRs

- Preserve `canonical/AXIOMS.md` and the one-fundamental-action rule.
- Quote hypotheses and boundary conditions explicitly; do not silently change Lorentz signature or conjugation conventions across repositories.
- Symbolically regress the historic negative tests (pure magnetic energy sign; smooth pure gauge; both Hamiltonian signs), preferably through independent matrix and component implementations.
- Compare candidate constraints with both #700's no-dynamics domain and #635's auxiliary HT pair.
- Provide English/Czech parity and reproducible scripts before promoting a C-tier claim; no automatic A-tier attestation.
