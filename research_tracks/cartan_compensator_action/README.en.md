<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: cartan-compensator.provenance -->
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

# Parallel Cartan compensator / Stelle–West action programme

**2026-10-28 · C_working · separate from PR #807 · NO CANONICAL PROMOTION**

This is a *new comparison theory and a proposed UBT embedding problem*, not a
reinterpretation of the minimal one-connection UBT model. In particular, none
of the no-go results or conditional statuses in PR #807 are amended here.
There is no claim of a completed action, degree-of-freedom count, or prediction.

<!-- BILINGUAL-UNIT: cartan-compensator.references -->
## Verified antecedents and exact scope

- Stelle & West, *Spontaneously broken de Sitter symmetry and the
  gravitational holonomy group*, Phys. Rev. D **21** (1980) 1466,
  https://doi.org/10.1103/PhysRevD.21.1466. Their (anti-)de Sitter gauge
  construction uses a symmetry-breaking compensator and a nonlinear
  redefinition of gauge fields to recover an Einstein–Cartan geometry.
- Westman & Złośnik, *Exploring Cartan gravity with dynamical symmetry
  breaking*, Class. Quantum Grav. **31** (2014) 095004,
  https://doi.org/10.1088/0264-9381/31/9/095004;
  https://arxiv.org/abs/1302.1103. They classify polynomial **Cartan-model**
  action candidates and allow the compensator norm to become dynamical.
  Particular choices give scalar–tensor sectors, while other choices
  propagate torsion: not every member reproduces pure GR.
- Westman & Złośnik, *An introduction to the physics of Cartan gravity*,
  Ann. Phys. **361** (2015) 330–376,
  https://doi.org/10.1016/j.aop.2015.06.013.
- Nikjoo & Złośnik, *Hamiltonian formulation of gravity as a spontaneously-
  broken gauge theory of the Lorentz group*, Class. Quantum Grav. **41**
  (2024) 045005, https://doi.org/10.1088/1361-6382/ad1c84,
  https://arxiv.org/abs/2308.01108. Their **different** complexified-Lorentz
  model provides a direct warning: mode counts depend sensitively on the
  parameter and reality branch (generic nonzero beta: three complex
  degrees of freedom; beta=0: no local modes; GR-related beta=±i).
  These results cannot be imported as UBT's mode count.

<!-- BILINGUAL-UNIT: cartan-compensator.axioms -->
## [AX-C] Explicit comparator axioms, not UBT axioms

C1. Work on an oriented smooth 4-manifold M. Choose G=SO(1,4) as the
**comparison model** and invariant internal metric
eta=diag(-1,+1,+1,+1,+1). This enlarges, rather than merely renames, a
physical Lorentz connection.

C2. Independent variables: a real G-connection 1-form A^{AB}=-A^{BA}
and a real compensator 0-form V^A in the defining five-vector
representation. Let E^A:=D_A V^A and F^{AB}:=dA^{AB}+A^A{}_C∧A^{CB}.
All internal contractions use eta and epsilon_{ABCDE}. No background
spacetime metric or independent tetrad is needed in this comparator.

C3. Require locality, G-gauge invariance, diffeomorphism invariance,
a real action, and an explicitly prescribed boundary variational
principle. "At most two derivatives" alone does **not** give a finite
classification of local polynomials. For the finite *seed* below, use
only the monomials F∧F, E∧E∧F, E∧E∧E∧E with one epsilon-contracted V,
and constant real coefficients. This is a defined truncation, not the
most general Cartan action.

C4. Restrict the GR comparison to regular fixed-norm patches
V^2=ell^2>0, ell≠0, with rank-four transverse E^A. The fully dynamical
V^2 branch is an additional hypothesis that requires new analysis.

<!-- BILINGUAL-UNIT: cartan-compensator.ubt -->
## [AX-U?] The missing, explicit UBT embedding obligation

The *existing* UBT field is Theta ∈ C⊗H ≅ Mat(2,C), with **eight real
components**; on the previous branch its local transformation is
X → exp(i alpha) S X S†. No canonical G=SO(1,4) five-vector field V^A,
G action on generic Theta, or equivariant map
Phi: Theta → V satisfying Phi(g·Theta)=g·Phi(Theta) has been established.

**DO NOT write Theta=V or E=D_A Theta as if the two representations were
identical.** A five-vector compensator and an eight-real-component
biquaternion are not the same carrier. A non-injective map, quotient,
nonlinear realization, or altered faithful representation might be
possible, but its kernel, gauge covariance, reality condition,
physical field content and dynamics must be proved, not assumed.
An additional unconstrained V would be a new fundamental field.

UBT task U1: construct an explicit representation/quotient Phi and
extended G-connection A(Ω,...) compatible with Theta's declared
Lorentz/internal symmetries; otherwise declare this simply a
**non-UBT comparator**. A mere independent physical spin connection
ω∈so(1,3) cannot be substituted for A∈so(1,4): the coset
components A^{I4} are essential.

<!-- BILINGUAL-UNIT: cartan-compensator.rank -->
## Exact local rank lemma (first completed test)

On a fixed-norm patch choose unitary gauge
V^A=ell δ^A_4 with ell>0. Let I,J=0,1,2,3 and write
A^{IJ}=ω^{IJ}, A^{I4}=e^I/ell. Then

\[
 E^I=D_A V^I=\ell A^{I4}=e^I,\qquad
 E^4=D_A V^4=0,\qquad
 F^{IJ}=R^{IJ}(\omega)-\ell^{-2}e^I\wedge e^J
 \quad (G=SO(1,4)).
\]

For **every** prescribed set of 16 tetrad components e^I_mu,
choose A_mu^{I4}=e^I_mu/ell. The derivative of the defining map
with respect to the 16 broken-connection components is

\[
 \frac{\partial E^I_{\mu}}{\partial A^{J4}_{\nu}}
 =\ell\,\delta^I_J\delta^\nu_\mu,
 \qquad \operatorname{rank}=16.
\]

Therefore the *Cartan comparator* has a surjective tetrad map on this
patch, unlike the earlier **pure-Lorentz one-connection** map
E=D_Ω Theta. This does not refute the UBT no-go theorem: it changes
its connection group, carrier and assumptions.

For variable-norm V, the identity
V_A E^A=(1/2)d(V^2) follows from metric compatibility; fixed norm
makes E transverse to V. This geometrical identity alone is not a
dynamical equation or a no-ghost result.

<!-- BILINGUAL-UNIT: cartan-compensator.action -->
## [CANDIDATE-C] Polynomial action seed and actual GR reduction

With wedge products displayed, define a constant-coefficient **candidate
family** (not the exhaustive invariant basis)

\[
 S_{\mathrm{seed}}[A,V;a,b,c]=\int_M \epsilon_{ABCDE}V^E
 \left[
 a\,F^{AB}\wedge F^{CD}
 +b\,E^A\wedge E^B\wedge F^{CD}
 +c\,E^A\wedge E^B\wedge E^C\wedge E^D
 \right].
\]

Real coefficients carry the appropriate dimensions. For
V=ell δ_4, the b-term **algebraically** becomes

\[
 b\ell\int_M\epsilon_{IJKL}
 e^I\wedge e^J\wedge
 \bigl(R^{KL}(\omega)-\ell^{-2}e^K\wedge e^L\bigr).
\]

Thus a Palatini plus cosmological-volume structure is actually
present. The a-term also contains a Lorentz Euler term,
Palatini and volume terms on this branch. The coefficients
must be compared with measured G and Λ; their signs and
normalizations are not predicted by this construction.

**Conditional GR comparator:** on an invertible fixed-norm branch,
for a nondegenerate coefficient choice yielding the ordinary real
Einstein–Cartan/Palatini bulk action, independent ω variation implies
T^I=0 in spinless vacuum; e variation gives Einstein–Λ.
This is standard Cartan/Palatini equivalence, not UBT closure.
For the fully varied parent action one must also check the V and
broken-A equations; unitary gauge alone is not a substitute for
varying the unreduced action.

For a dynamical norm, put V^A=ρ(x)δ^A_4. Then
E^I=ρ A^{I4}, E^4=dρ. No claim follows that ρ is an auxiliary
field or has positive kinetic energy. Writing a metric-Hodge
"kinetic term" using g(E) may require inverses and is **not**
automatically part of the polynomial background-free class.
Polynomial invariants or a bounded polynomial truncation must
generate any norm dynamics explicitly. A generic dynamical norm
may produce an additional scalar, so "exactly two modes" is a
filter, not an inherited property.

<!-- BILINGUAL-UNIT: cartan-compensator.finiteness -->
## Finite-classification caveat and proof of underdetermination

A bounded total polynomial degree, a fixed finite set of
representations and finite jet order yield a finite-dimensional
space of polynomial contractions: it is a linear subspace of a
finite-dimensional monomial space, then quotiented by identities
and exact forms. However, C1–C2 plus "polynomial" *without*
a degree bound allow infinitely many invariant terms; for example,

\[
 \int_M (V^2)^n\,\epsilon_{ABCDE}V^E\,
 E^A\wedge E^B\wedge E^C\wedge E^D,
 \qquad n=0,1,2,\ldots.
\]

These are algebraically independent as varying-norm
polynomials (not on a fixed-norm slice). Consequently, a
"Lovelock-type classification of ALL UBT actions" is not yet
a theorem from the short axiom list. The standard Lovelock theorem
classifies a restricted *metric* gravitational endpoint; it does
not select this microscopic A,V or Theta action or a unique
compensator representation.

<!-- BILINGUAL-UNIT: cartan-compensator.filters -->
## Falsification gates (mandatory order)

1. **Representation gate:** establish Phi(Theta), extended gauge
   action and admissible reality slice explicitly, with no
   hidden new propagating fields. FAIL ⇒ this remains Cartan,
   not a UBT gravitational action.
2. **Parent-variation gate:** vary the full S[A,V] before symmetry
   reduction; account for boundary terms, all A, V equations,
   rank of the tetrad map and torsion constraints.
3. **Dirac gate:** calculate the *spatially unrestricted* primary,
   secondary and tertiary constraints and Poisson matrix. For
   phase-space dimension 2N and F first-class / S second-class
   constraints, N_phys=(2N−2F−S)/2 **per space point**
   where regular. Minisuperspace is a diagnostic, not this proof.
4. **Linear spectrum:** on a nondegenerate Lorentzian solution,
   identify physical helicities, scalar/vector/tensor sectors,
   positive reduced kinetic form, hyperbolicity and no tachyon.
   Check reality and self-dual branches separately.
5. **IR Einstein gate:** derive local GR with two real graviton
   helicities and no extra *light* mode; distinguish this from
   exact two-DOF gravity at every scale.
6. **Prediction gate:** only after the preceding gates,
   preregister one observable (including coefficient inputs,
   error budget, and comparison null model), not a fitted result.

**First decision:** the local rank gate for the *Cartan comparator*
passes (proved above). The critical UBT representation/embedding
gate is **OPEN**, and the full Dirac/spectrum tests are **NOT DONE**.
This track must not promote GR recovery, parameter selection,
or a first UBT prediction.

<!-- BILINGUAL-UNIT: cartan-compensator.boundary -->
## Relation to existing UBT work; merge boundary

- Existing restricted one-connection no-go:
  canonical/gr_closure/gap_10t_minimal_one_connection_gr_no_go.tex.
- Existing constrained Holst calculation, finite restricted operator
  basis, and conditional GR audit: PR #807,
  research_tracks/action_selection/physics_closure_2026_10.en.md.
- Existing eight-real-component Theta invariant and kinetic signature
  checks: canonical/ACTION.en.md and
  research_tracks/action_selection/theta_potential_invariants.en.md.

This is a **parallel research track only**. No changes to PR #807,
canonical action, claim matrix or effective GR postulate are licensed
by its existence. Keep a new PR in draft and do not merge as a
physical theorem without the gate evidence above.

<!-- BILINGUAL-UNIT: cartan-compensator.verification -->
## Verification

The exact rational checks in `tests/test_cartan_compensator_seed.py` pass all 4 cases. LEAN-PENDING: the finite rank calculation has no compiled Lean proof in this track. These tests do not establish the embedding, parent field variation, physical constraint reduction or spectrum. Independent bilingual semantic review remains pending.
