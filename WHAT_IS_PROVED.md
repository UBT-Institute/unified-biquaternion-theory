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

# WHAT_IS_PROVED.md — Current map of proved, conditional and no-go results

**Status date:** 10 October 2026

This file is a current status map, not a chronological changelog. Historical
snapshots remain in git history. Fine-grained claim IDs and forbidden wording
are maintained in CLAIMS.yaml.

## Claim-level convention

- [L0]: exact algebraic/formal identity.
- [L1]: proved theorem within the explicitly stated UBT assumptions.
- [L1 conditional]: theorem after a declared physical/dynamical premise.
- [STD]: standard external mathematics/physics result used correctly.
- [NUM]/[OBS]: numerical result/observation, not a proof.
- [OPEN]: unresolved.
- [NO-GO]: the stated route is excluded under its assumptions.

## 1. Biquaternion / metric / GR sector

### Proved local geometry

| Claim | Status | Primary source |
|---|---|---|
| The central anticommutator of the covariant tetrad defines a Lorentzian metric on the declared Lorentz slice | [L1] | canonical/gr_closure/covariant_tetrad_rank_theorem.tex |
| The tetrad-to-metric differential has rank 10 with six-dimensional Lorentz kernel | [L1] | same; verification tools |
| Metric-compatible connection is uniquely Levi--Civita plus contortion for specified torsion | [L1] | canonical/gr_closure/gap_10omega_connection_elimination.tex |
| Every smooth local Lorentzian tetrad has a local single-\(\Theta\) split-jet/torsionful representer in the stated construction | [L1 local] | canonical/gr_closure/gap_10i_torsionful_local_representer.tex |
| Constant Lorentz tetrads, including Minkowski, have explicit affine single-\(\Theta\) representers | [L1] | canonical/gr_closure/gap_10i_integrability_selection.tex |
| The generalized-Dirac block lift reproduces the curved Clifford relation and gives the exact constrained metric-rank criterion | [L0/L1] | canonical/geometry/biquaternion_dirac_lift.tex; research_tracks/canonical_relation_generalized_dirac/ |

### Closed no-go / narrowing results

| Claim | Status |
|---|---|
| Naive one-sided invertible torsion-free connection cannot represent generic curved GR | [L1 NO-GO] |
| The pure surjective split-jet right-inverse constraint does not dynamically select the tetrad | [L1 NO-GO] |
| Current kinematic axioms do not determine the numerical Einstein-Hilbert coefficient/Newton constant | [L1 NO-GO] |
| Split-jet auxiliary variables are algebraic/nonpropagating on the stated non-null branch | [L1] |

### Einstein dynamics

A local Einstein--\(\Lambda\) infrared branch is recovered **conditionally**
once a suitable two-derivative effective action / Laplace-type Hessian premise
is supplied. Standard Schwarzschild, Regge--Wheeler and Zerilli physics then
follows in that recovered effective branch.

This is:
\[
\boxed{\text{DERIVED WITH ASSUMPTIONS, not an unconditional microscopic closure.}}
\]

Still open:
- final microscopic single-\(\Theta\) action;
- constrained quantum measure and physical mode count;
- first-principles Newton coefficient;
- global/null-patch completion;
- microscopic branch selection and full quantum stability.

## 2. Colour SU(3) sector

### Exact algebraic / geometric results

| Claim | Status | Source |
|---|---|---|
| The selected complex three-dimensional carrier with its Hermitian metric and complex volume form has stabilizer \(SU(3)\) | [L1] | research_tracks/T2_GAUGE/ |
| Quaternion-adjoint spin generators plus five quadrupoles span the eight Gell-Mann directions, \(8=3+5\) | [L1] | su3_spin_quadrupole_dynamical_bridge.md; verifier |
| Minimal norm-preserving two-sided raw-carrier algebra contains \(\mathfrak{so}(1,3)\oplus\mathfrak u(1)_{\rm phase}\), not full colour | [L1] | su3_raw_carrier_lie_closure.md |
| Adding the missing raw-carrier colour directions with boosts closes to \(\mathfrak{su}(1,3)\) | [L1] | same |
| A constrained complex \(4\times3\) Stiefel frame modulo local right \(SU(3)\) has exactly seven normalized real modes; adding the radial mode restores eight | [L1] | su3_stiefel_hls_rewrite.md |
| \(4\times3\) is the unique minimal Stiefel size matching the seven normalized modes | [L1] | su3_vs_u3_stiefel_count.md |
| The derived traceless frame current begins with the adjoint bilinear \(B\,\beta\,\partial\beta\) HLS vertex | [L1] | su3_stiefel_current_vertex.md |
| The Stiefel chart is singular at \(\rho=0\); a rank-three homogeneous frame cannot survive the raw-field origin | [L1 NO-GO for smooth continuation] | su3_stiefel_critical_origin_obstruction.md |
| \(SU(1,3)/SU(3)\cong S^1\times\mathbb C^3\); the exact composite frame bundle is topologically trivial | [L1 topology] | su3_coset_topology_instanton_boundary.md |

### HLS / emergent-gauge boundaries

After an autonomous \(F_B^2\) term exists, the surface \(c_V=0\) restores
independent local
\[
SU(3)_Z\times SU(3)_B,
\]
while the locking operator reduces the symmetry to the diagonal.

Weak fixed-frame triplet loops:
- generate a positive transverse \(Z_B\);
- do not remove the finite HLS mass intercept;
- are quantitatively too weak, in their controlled regime, to generate a
  large pure-Yang--Mills hierarchy.

The determinant-sensitive anisotropy is a symmetric \(\mathbf6\) physical
spurion with \(SO(3)\) stabilizer and the corresponding rank-five Higgs pattern
if promoted into an autonomous gauge EFT.

### What is not proved

Full QCD is **not derived**.

The preferred open endpoint is
\[
\rho_0>0,\qquad
Z_B>0,\qquad
c_V\to0,\qquad
\lambda_2\to0,\qquad
M_\beta^2>0,
\]
followed by:
- full Yang--Mills 1PI two/three/four-point structure;
- BRST/Slavnov--Taylor consistency;
- gapped frame matter;
- autonomous Yang--Mills topological sectors;
- compatibility with the sharp/GR core.

The decisive unresolved source term is the mixed sharp/GR contribution to
\[
\left.\beta_{\lambda_2}\right|_{\lambda_2=0}.
\]

## 3. Theta / complex-time sector

Established for the currently defined objects:

\[
\tau_{\rm UBT}=t+i\psi
\]
is a dimensionful physical UBT coordinate and is not canonically the
dimensionless Jacobi modular parameter.

For the compact-circle heat trace,
\[
\tau_J=\frac{i s}{\pi R_\psi^2},
\]
and ordinary Jacobi-theta transformation theory applies.

For
\[
\vartheta_3(\tau)=\sum_n e^{\pi i n^2\tau},
\]
the natural scalar theta subgroup is
\[
\Gamma_\theta=\langle S,T^2\rangle
\]
of index 3 in \(SL(2,\mathbb Z)\).

Generic finite weighted theta-like reductions are not modular forms by default
and are not mock-modular without a separately derived completion.

Strict frame-independent microscopic holomorphy in \(t+i\psi\), with \(\psi\)
an independent Lorentz scalar, is incompatible with generic Lorentz-covariant
spacetime dependence under the stated assumptions.

Open: full interacting UBT modular covariance.

## 4. CMB / cosmology sector

A strict H0--H3 full-covariance likelihood/KL interface is implemented.

The current H3 physics chain is **not complete**. A valid UBT prediction needs:
\[
S_{\rm scalar}^{(2)}
\to
\delta\Theta\to\mathcal R
\to
\text{state prescription}
\to
P_{\rm UBT}.
\]

Compact internal \(S^1_\psi\) gives
\[
\lambda_{\mathbf k,n}=|\mathbf k|^2+n^2/R_\psi^2
\]
and therefore KK masses, but it does **not** imply a three-dimensional spatial
IR cutoff \(k_{\rm spatial}\ge1/R_\psi\).

Historical CMB comb/cutoff tests remain negative or phenomenological
constraints on those specific ansätze, not positive UBT evidence.

## 5. Torus / modulus sector

For a genuine fixed-area flat two-torus, standard zeta regularization gives
\[
\det{}'\Delta_\tau\propto\Im\tau\,|\eta(\tau)|^4.
\]

Consequences:
- the older termwise positive-Hessian argument is not a valid regularized
  stability proof;
- the square torus is a determinant maximum inside the rectangular family but
  a saddle in full moduli space;
- the hexagonal torus is the fixed-area determinant maximum;
- the isolated standard positive bosonic one-loop log determinant has no
  finite global modulus minimum.

Therefore the isolated massless one-loop branch does **not** dynamically select
a stable UBT torus modulus.

Open: action-derived massive/interacting/backreacted
\(V_{\rm eff}(\tau_{\rm mod},\bar\tau_{\rm mod})\).

## 6. Alpha / numerical-structure sector

Several exact theta/eta identities and reproducible numerical relations exist,
but the fine-structure constant is **not derived from first principles**.

In particular, numerical closeness of candidate expressions to
\(\alpha^{-1}\) remains [OBS]/conditional until every input is derived from the
same finalized action without using \(\alpha\), 137, or a fitted target value.

The primary alpha derivation gap remains open.

## 7. Single-action and quantum status

canonical/ACTION.en.md is authoritative:

\[
\boxed{\text{fundamental action family defined, not finalized}.}
\]

Still open:
- microscopic measure;
- unique real variational principle;
- complete constrained Hessian;
- quantum path integral;
- UV completion/renormalization closure;
- all sector reductions from one action;
- a zero-parameter quantitative prediction.

No completed quantum theory of UBT is claimed.

## 8. Superseded interpretations that must not be revived

- Physical UBT complex time is not automatically the Jacobi modular parameter.
- Compact internal \(\psi\) does not automatically impose a spatial CMB cutoff.
- Algebraic \(SU(3)\) generators are not by themselves QCD gluons.
- A heat-kernel \(F^2\) term for a composite frame is not by itself eight
  independent gluon kinetic terms.
- The weak fixed-frame HLS phase is not an interacting massless-QCD phase.
- The massless one-loop determinant does not prove square-torus stabilization.
- The repository currently has no first-principles numerical derivation of
  \(\alpha\), \(G\), or another new precision observable.

## 9. Authoritative status sources

Use together:
- CLAIMS.yaml — fine-grained claim ledger;
- STATUS_OF_UBT.md — current narrative status;
- ROADMAP.md — current priorities;
- CLAIMS_MATRIX.en.md / CLAIMS_MATRIX.cs.md — public status matrix;
- DERIVATION_INDEX.md — derivation/source navigation;
- canonical/ACTION.en.md — single-action guardrail.

When this file conflicts with an older research note, the newer explicit
status/override and CLAIMS.yaml take precedence.
