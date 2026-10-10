<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: A_attested
ai_assistance: disclosed
human_review: substantive
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Current consolidated status; fine-grained claims live in CLAIMS.yaml.
UBT-AI-PROVENANCE-END
-->

# STATUS OF UBT — 10 October 2026

This file is the current narrative status of Unified Biquaternion Theory.
Historical status snapshots remain in git history. Fine-grained theorem,
conditional, numerical, open-gap and forbidden-wording entries are maintained
in CLAIMS.yaml.

## Executive status

UBT is a mathematically developed research programme, not a completed theory of
everything.

The current strongest results are:
- exact biquaternionic/algebraic structures;
- projection-free covariant-tetrad metric kinematics and rank-ten local
  geometry;
- a conditional low-energy Einstein--\(\Lambda\) recovery branch;
- exact structural \(SU(3)\) results and an exact finite \(4\times3\)
  Stiefel/hidden-local-\(SU(3)\) collective rewrite;
- a cleaned theta/complex-time classification;
- explicit no-go boundaries for several older CMB and torus mechanisms.

The largest unresolved issue is still foundational:
\[
\boxed{\text{one unique microscopic UBT action and quantum measure are not finalized.}}
\]

Therefore no full Standard Model derivation, no UV-complete quantum theory and
no zero-parameter new precision prediction are currently claimed.

## 1. Fundamental action and quantum status

canonical/ACTION.en.md remains binding.

A single action family exists schematically as
\[
S_\Theta
=
\frac12\int\sqrt{-g}\,
\langle D_\mu\Theta,D^\mu\Theta\rangle
-
\kappa V[\Theta],
\]
but sign/normalization, complete potential selection, microscopic measure,
independent versus composite fields, full constrained Hessian and quantum
renormalization prescription are not all fixed.

Current status:
\[
\boxed{\text{DEFINED FAMILY, NOT FINALIZED}.}
\]

Until this is closed, sector-specific effective actions are reductions or
candidates, not additional fundamental actions.

## 2. GR / spacetime geometry

### Established local structure

The canonical metric is generated from the covariant tetrad
\[
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta
\]
through the central anticommutator relation on the Lorentz slice.

Established results include:
- local Lorentz signature under the stated slice assumptions;
- rank-ten tetrad-to-metric differential;
- six-dimensional Lorentz kernel;
- unique metric-compatible connection for specified torsion;
- Levi--Civita torsion-free branch;
- explicit affine Minkowski/constant-tetrad representers;
- local torsionful split-jet representers for smooth Lorentzian tetrads;
- exact generalized-Dirac/Clifford lift and constrained-rank criteria;
- algebraic split-jet auxiliary nonpropagation on the stated non-null branch.

Several naive direct routes are closed:
- one-sided invertible torsion-free connection for generic curvature;
- pure surjective split-jet constraint as a tetrad selector;
- kinematic determination of the numerical Newton constant.

### Einstein dynamics

A local Einstein--\(\Lambda\) infrared branch is recovered **conditionally**
once the required two-derivative effective action / Laplace-type Hessian
premise is supplied.

Within that recovered branch, standard Schwarzschild and linearized
Regge--Wheeler/Zerilli physics follow.

This is not yet an unconditional microscopic derivation from one finalized
\(\Theta\) action.

Open:
- microscopic Hessian and physical mode count;
- first-principles \(G\);
- quantum measure;
- null/global completion;
- full branch-selection dynamics.

## 3. Colour SU(3): exact structure versus QCD dynamics

### What is established

The selected complex three-dimensional carrier with Hermitian metric and
complex volume form has exact stabilizer \(SU(3)\).

The eight Gell-Mann directions admit the exact operator decomposition
\[
8=3_{\rm spin}+5_{\rm quadrupole}.
\]

The minimal norm-preserving two-sided raw-carrier algebra contains
\[
\mathfrak{so}(1,3)\oplus\mathfrak u(1)_{\rm phase},
\]
not full colour \(SU(3)\). Adding the missing raw-carrier colour directions
with the boost sector closes to \(\mathfrak{su}(1,3)\), which is incompatible
with simply retaining the present sharp/determinant GR core as an exact raw
carrier symmetry.

A direct finite-jet multiplicity interpretation is also closed as a physical
colour-triplet mechanism.

### Exact Stiefel / hidden-local rewrite

On the nonzero timelike branch, the normalized sector admits an exact
collective description
\[
Z\in\mathbb C^{4\times3},
\qquad
Z^\dagger GZ=-I_3,
\qquad
Z\sim Zh(x),\quad h(x)\in SU(3).
\]

Degree count:
\[
24-9-8=7,
\]
and the radial mode restores the original eight real one-biquaternion
components.

The \(4\times3\) size is uniquely minimal for this construction.

The derived vertical frame current begins as
\[
C_{\mu,0}
=
\frac12
\left(
\beta\,\partial_\mu\beta^\dagger
-
(\partial_\mu\beta)\beta^\dagger
\right)_0+\cdots ,
\]
giving a genuine adjoint HLS current vertex without adding a new fundamental
UV field.

### Weak fixed-frame boundary

Weak triplet loops can generate a positive transverse gauge kinetic response,
but:
- the fixed-frame HLS phase retains a vector mass;
- conserved-current transversality does not perturbatively cancel that mass
  intercept;
- the induced weak coefficient is too small for a useful large pure-Yang--Mills
  hierarchy unless the nominal coupling/log is already outside the controlled
  weak regime.

Thus weak one-loop induction is a sign/existence benchmark, not a QCD
derivation.

### Finite-radius preferred target

The raw-field origin is not a smooth HLS endpoint. The timelike field space has
cone form
\[
ds^2=d\rho^2+\rho^2ds_7^2
\]
with measure proportional to \(\rho^7d\rho\), and signature \((1,3)\) has
complex Witt index one; a rank-three homogeneous frame cannot survive
\(\rho=0\).

The preferred target is therefore finite radius:
\[
\boxed{
\rho_0>0,\qquad
Z_B>0,\qquad
c_V\to0,\qquad
\lambda_2\to0,\qquad
M_\beta^2>0.
}
\]

After an autonomous \(F_B^2\) exists, the zero-locking surface
\[
c_V=0
\]
restores independent local
\[
SU(3)_Z\times SU(3)_B,
\]
while the locking term preserves only the diagonal.

This makes zero locking technically natural once reached, but does not prove
that RG evolution reaches it.

### Determinant anisotropy

The determinant-sensitive tangent anisotropy is naturally represented as a
symmetric \(\mathbf6\) spurion with physical stabilizer
\[
SO(3)\subset SU(3).
\]

In an autonomous gauge EFT its canonical Higgs pattern has rank five: the
three antisymmetric Gell-Mann directions are unbroken and five symmetric
directions are broken.

A QCD-like unbroken colour phase therefore requires
\[
\lambda_2\to0
\]
or an equivalent decoupling mechanism.

The isolated colour sigma sector has enhanced \(SU(1,3)\) at
\(\lambda_2=0\), but the full sharp/GR core breaks that symmetry. The decisive
open mixed-sector quantity is
\[
\left.\beta_{\lambda_2}\right|_{\lambda_2=0}.
\]

### Global gauge topology

The normalized timelike coset has topology
\[
SU(1,3)/SU(3)\cong S^1\times\mathbb C^3.
\]

Hence the exact composite frame bundle is topologically trivial and carries no
independent second-Chern/instanton bundle sectors.

Full QCD topology would therefore require the emergent \(B_\mu\) functional
integral to become autonomous/non-invertible relative to the exact classical
one-\(\Theta\) frame rewrite.

### Colour verdict

\[
\boxed{\text{Algebraic and collective }SU(3)\text{ is strong; full QCD remains open.}}
\]

Required closure:
- controlled finite noncompact HLS phase;
- finite \(Z_B\) and zero locking mass;
- full two/three/four-point Yang--Mills 1PI structure;
- BRST/Slavnov--Taylor identities;
- gapped charged frame matter;
- autonomous topological sectors;
- compatibility with GR/sharp dynamics.

## 4. Theta / complex time

Canonical physical complex time is
\[
\tau_{\rm UBT}=t+i\psi,
\]
with \(t,\psi\) dimensionful.

It is not canonically the Jacobi modular parameter.

For the compact-circle heat trace,
\[
\tau_J=\frac{i s}{\pi R_\psi^2},
\]
and ordinary Jacobi theta mathematics applies.

For
\[
\vartheta_3(\tau)=\sum_n e^{\pi i n^2\tau},
\]
the natural scalar theta subgroup is
\[
\Gamma_\theta=\langle S,T^2\rangle,
\]
of index 3 in \(SL(2,\mathbb Z)\).

Generic finite weighted theta-like sums are not modular by default and are not
mock-modular without a derived completion.

Strict frame-independent microscopic holomorphy in \(t+i\psi\), with \(\psi\)
treated as an independent Lorentz scalar, conflicts with generic Lorentz
dynamics under the stated assumptions.

P1 is therefore closed for the currently defined free/reduced objects, while
full interacting modular covariance remains open.

## 5. CMB / cosmology

The full-covariance H0--H3 model-selection interface is implemented.

A valid UBT H3 prediction is still blocked by missing microscopic perturbation
physics:
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
|\mathbf k|^2+n^2/R_\psi^2
\]
and KK masses, but does not impose a spatial cutoff
\(k_{\rm spatial}\ge1/R_\psi\).

The historical low-\(\ell\) cutoff ansatz is therefore phenomenological, not
an action-level consequence of internal compactification.

Historical comb tests remain null constraints on those specific variants.

## 6. Torus / modulus programme

For a genuine fixed-area flat \(T^2\),
\[
\det{}'\Delta_\tau
\propto
\Im\tau\,|\eta(\tau)|^4.
\]

The older termwise positive-Hessian argument is superseded.

The square torus is a determinant maximum in the rectangular family but a
saddle in full moduli space; the hexagonal torus is the fixed-area determinant
maximum.

For the standard positive bosonic one-loop effective action, the isolated
massless determinant has no finite global modulus minimum.

Therefore P4 is closed as a no-go for **isolated massless one-loop modulus
selection**.

Open:
- action-derived genuine modulus;
- massive/interacting/backreacted bounded
  \(V_{\rm eff}(\tau_{\rm mod},\bar\tau_{\rm mod})\).

## 7. Alpha and numerical structures

The repository contains exact modular/theta identities and reproducible
numerical relations relevant to the fine-structure programme.

However:
\[
\boxed{\alpha\text{ is not derived from first principles}.}
\]

Any expression numerically close to \(\alpha^{-1}\) remains observational or
conditional until every coefficient and scale is derived independently from
the finalized action without target-value input.

The primary alpha derivation gap remains open.

## 8. Relation to the Standard Model and quantum gravity

UBT currently has:
- strong structural gauge-algebra work;
- partial/conditional electroweak and hypercharge tracks;
- no completed microscopic full Standard Model action;
- no complete anomaly/mass/Yukawa/QCD dynamical closure;
- no completed UV quantum-gravity theory.

It should therefore not be presented as empirically or formally replacing
the Standard Model plus General Relativity.

## 9. Quantitative prediction status

No zero-parameter numerical UBT prediction is currently registered as derived
from one unique finalized action.

The first accepted prediction must:
- be fixed before data comparison;
- include uncertainty/nuisance treatment;
- be reproducible;
- beat relevant generic alternatives rather than only a weak null.

## 10. Current priorities

1. finalize one microscopic action and quantum measure;
2. compute the finite-radius Stiefel/HLS phase flow and
   \(\beta_{\lambda_2}|_{\lambda_2=0}\);
3. derive the physical cosmological scalar Hessian and \(P_{\rm UBT}\);
4. derive or close the interacting torus-modulus potential;
5. obtain a preregistered quantitative prediction.

## Authoritative companion files

- CLAIMS.yaml — fine-grained status and forbidden wording;
- WHAT_IS_PROVED.md — compact theorem/no-go map;
- ROADMAP.md — current research priorities;
- CLAIMS_MATRIX.en.md / CLAIMS_MATRIX.cs.md — public claim matrix;
- DERIVATION_INDEX.md — source navigation;
- canonical/ACTION.en.md — single-action rule.

When an older research file conflicts with this status, its explicit newer
status override and CLAIMS.yaml take precedence.
