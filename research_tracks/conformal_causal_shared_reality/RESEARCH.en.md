<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# Conformal causality and shared reality: a theorem-first UBT bridge

**2026-10-28 · C_working · independent of PR #807 and PR #808.**
This is a conditional study of **one** matrix chart X∈Mat₂(C) of the
possibly larger or differently realized UBT carrier. It does not fix
Theta's fundamental component count or identify complex time psi with
the four imaginary Minkowski coordinates. Nothing here selects an action.

## Three principles kept distinct

**[G] Biquaternion geometry:** C⊗H≅Mat₂(C) is an established
algebraic realization. Use a 2×2 matrix chart W only as a test sector.
No fundamental carrier size is inferred from chart dimension.

**[C] Finite signal speed and causal order:** If a Lorentzian spacetime
and its causal order are given, Zeeman (1964) constrains their *global*
causal automorphisms in dimension at least three to the inhomogeneous
Lorentz group and positive dilations (subject to the stated hypotheses).
It does NOT derive a local SU(2,2) gauge bundle, an Einstein action or
a metric scale from finite speed alone. SO(2,4) is the local conformal
algebra of flat 4D Minkowski space; choosing its Cartan geometry is a
separate proposed completion.

**[SR] Shared reality, operational AXIOM CANDIDATE:** Each causal
diamond O carries a local observable algebra A(O) and a compatible
state prescription omega_O. For nested regions O1⊂O2 require
A(O1)⊂A(O2) and omega_O2|A(O1)=omega_O1; for spacelike separated
regions require microcausality. Overlap agreement is necessary but,
in a quantum setting, is not sufficient for a joint global state
(the quantum marginal/extension problem is separate). This principle
is not yet a dynamical law, symplectic form or action selector.

## Test chart, causal quadratic form and interior metric

Let W=X+iY∈Mat₂(C), X=X†, Y=Y†, Y positive definite.
This is the **future tube** T_+ of complexified Minkowski space.
Every Hermitian X=x^mu sigma_mu has

\[
 \det X=(x^0)^2-(x^1)^2-(x^2)^2-(x^3)^2.
\]

The subgroup SL(2,C) acts by X→SXS† and Y→SYS†,
preserving det X and the forward cone Y>0; translations by
Hermitian H and positive real dilations also preserve T_+.
The full SU(2,2) action is fractional linear in a suitable realization.
The symmetric domain is G/K with
G=SU(2,2), K=S(U(2)×U(2)); dim G=15, dim K=7.

The canonical (scaled) positive Hermitian metric on T_+ is

\[
 h_W(dW,dW)=\operatorname{Tr}
  (Y^{-1}dW\,Y^{-1}dW^\dagger)
 =\left\|Y^{-1/2}dW\,Y^{-1/2}\right\|_{\rm HS}^2\ge0.
\]

It is strictly positive for nonzero dW. At Y=I, with
dW=Σ_mu (dx_mu+i dy_mu)σ_mu,
h=2Σ_mu[(dx_mu)^2+(dy_mu)^2], i.e. signature (8,0).
Hence any smooth pullback Theta*:h to a real four-manifold is
positive semidefinite, never a nondegenerate Lorentz metric.
**THEOREM T1 [analytic, conditional on the future-tube chart]:**
A Lorentzian UBT tetrad cannot be recovered by *only* pulling back
this natural positive metric. This does **not** forbid other bilinear
forms, covariant jets, soldering maps, Cartan reductions, or dynamics.

The tube condition Y>0 means that the boundary Y=0 containing
ordinary Hermitian Minkowski X is NOT a regular interior point.
Similarly, the repository's i·Herm tetrad reality convention does
not by itself select a tube interior or specify the role of psi.

## The key missed group-theoretic obstruction

There are TWO different homogeneous spaces:

\[
 \mathcal T_+=G/K,\quad K=S(U(2)\times U(2)),\quad\dim=8;
 \qquad
 \overline{\mathbb M}^{1,3}=G/P,\quad\dim=4,
\]

where P is the parabolic stabilizer of a real null line in SO(2,4)
(or its preimage in the spin cover SU(2,2)).
The identity-component Levi/unipotent structure is
P≈(Spin(1,3)×R_{>0})⋉R^4 (modulo finite centers).
Its maximal compact subgroup has dimension 3 (Spin(3)).
The maximal compact K has dimension 7.

**THEOREM T2 [standard Lie-group argument, conditional on G/K model]:**
No G-equivariant map f:G/K→G/P exists.
Proof. If f is equivariant, f(eK)=gP for some g∈G. For every k∈K,
f(eK)=f(kK)=k·f(eK), hence g^{-1}Kg⊂P. The image is compact and
has dimension 7. Every compact subgroup of P is contained up to
conjugation in a maximal compact subgroup of dimension 3.
Contradiction. QED.

*Scope:* No pointwise **fully G-equivariant** reduction from a single
future-tube field to a null-ray conformal compensator. This is NOT
a no-go for a map using the first jet J¹Theta, an independent
conformal Cartan connection, a boundary/degenerate regime,
additional constrained structure, or a smaller symmetry group.
**An actual construction must exhibit its transformation law.**

## What a genuinely new conformal Cartan closure must accomplish

For Lorentzian conformal Cartan geometry one works with a principal
P-bundle and a Cartan connection whose local decomposition can be
written, with convention-dependent signs, as

\[
 \mathcal A=e^aP_a+\tfrac12\omega^{ab}M_{ab}
                  +bD+f^aK_a.
\]

The soldering 1-forms e^a are **part of this connection**.
Simply declaring e=pi_P(A) *imports* tetrad geometry; it does not
derive it from Theta. A normal Cartan connection may be
uniquely constructed from a PRE-EXISTING conformal class, which
likewise is not a derivation of that class from Theta.

Define a proposed gauge-covariant first-jet map (if one exists)
\[
 \mathcal E:J^1\Theta\times \{\mathcal A\}
       \longrightarrow T^*M\otimes\mathbb R^{1,3},
 \qquad e^a_\mu=\mathcal E^a_\mu(\Theta,D_\mu\Theta,\mathcal A).
\]
One must prove: (i) correct G/P gauge covariance; (ii) a
Lorentz-real, invertible coframe; (iii) rank of the allowed
variational map equals 16 on a regular patch; (iv) no use of
independent e as a hidden input; (v) whether the new connection
is physical and what independent DOF it carries.

A fake solution is any construction with e_mu^a=A_mu^{P_a}
freely independent and no equation or constraint tying it to Theta.
Such a model may be legitimate gravity, but is NOT a Theta-origin
proof.

**OPEN / NOT COMPUTED:** equivariant first-jet bridge, conformal
action invariant classification, unrestricted Dirac algebra,
ghost/stability analysis, and GR reduction.

## Phase and the complex-time caveat

Do not conflate the ordinary matrix-tube phase W→e^{iα}W with
the compact disk automorphism Z→e^{iα}Z. The latter does occur
in a suitable SU(2,2) action, but after the Cayley transform the
tube action is NOT simply linear phase multiplication.
Counterexample: W=diag(1,-1)+iI belongs to T_+;
iW=-I+i·diag(1,-1) does not belong to T_+.
Neither "phase is absent" nor "phase is Wick rotation
t↔psi" is established. Preserve the old UBT phase question
as OPEN, without forcing a choice.

## Information is a proposed filter, NOT a shortcut to an action

For a faithful reference state with a well-defined/regulated modular
Hamiltonian K_O=-log rho_O, the entanglement first law gives
delta S_O=delta< K_O > near that reference state. For special
conformal vacuum balls, K_O has a local geometric expression.
Jacobson (2016) links small-ball entanglement equilibrium at
fixed volume to the Einstein equation under explicit hypotheses;
the nonconformal case needs an extra conjectural input.
This does NOT create a classical symplectic form for Theta or
fix the coefficients of a UBT action. Test an explicit
Theta-dependent map from causal diamonds and their states to
the Cartan/metric variations, including the entropy-area
normalization and matter stress tensor, before claiming selection.

## Finite research gates, in order

1. **G0 — Chart audit:** exact Hermitian/determinant/cone/phase
   tests; domain, signatures and stabilizers explicitly stated.
   This note and tests supply finite algebra and the analytic
   obstruction T1–T2; not a complete Lean proof.
2. **G1 — Jet/soldering:** either construct a nontrivial
   Theta-derived Lorentz coframe with its full covariance
   and 16-rank certificate, or exhibit a counterexample/no-go.
   Compare to the existing #807 one-connection no-go.
3. **G2 — Information bridge:** specify shared-state extension
   axioms and calculate their variational consequence for
   one concrete finite causal diamond. Do NOT assume an area
   law coefficient or modular-time identification without proof.
4. **G3 — Action classification:** after G1–G2, enumerate
   constant-coefficient polynomial invariants up to an
   explicit maximum total degree; distinguish imported
   symmetry-breaking coefficients from derived ones.
5. **G4 — Full Dirac and spectrum:** spatially unrestricted
   first-/second-class constraints, reduced signs, helicities,
   causal hyperbolicity and GR limit; only then preregister
   a UBT-specific measurable prediction.

**Stop after G1 for adversarial review.** Failed G1 is a genuine
valuable result about this route; it is not grounds to discard the
fundamental bikvaternionic project or erase earlier tracks.

## Reuse / isolation

- PR #807 documents the matched-pairing/free-jet bare-action no-go,
  the restricted Holst Hamiltonian, and provisional Theta carrier.
- PR #808 documents the *distinct* SO(1,4) five-vector Cartan
  comparator and its exact full-rank broken-connection map.
- Do not touch their branches, canonical/, claim matrices or
  their author/provenance records. This track starts from master.
- No promotion to the final UBT action, no automatic merge.

## Primary sources

- E. C. Zeeman, *Causality Implies the Lorentz Group*, J. Math.
  Phys. **5** (1964) 490, https://doi.org/10.1063/1.1704140
- A. Čap and J. Slovák, conformal parabolic Cartan geometry
  reference: https://www.mat.univie.ac.at/~cap/files/Srni20-beamer-3.pdf
- Conformal Cartan soldering and normality treatment:
  https://intlpress.com/site/pub/files/_fulltext/journals/atmp/2018/0022/0008/ATMP-2018-0022-0008-a001.pdf
- SU(2,2) Hermitian tube realization:
  https://doi.org/10.1016/j.jnt.2026.02.009
- T. Jacobson, *Entanglement Equilibrium and the Einstein
  Equation*, PRL **116** (2016) 201101,
  https://doi.org/10.1103/PhysRevLett.116.201101

## Canonical sharp-vs-dagger comparison [PROVED, restricted; OPEN as dynamics]

The paired G1_CANONICAL_SHARP_BRIDGE.en.md / .cs.md note audits
the actual canonical anticommutator against the earlier
Hermitian-dagger Gram comparator. The canonical sharp pairing
is complex bilinear and central for arbitrary Mat(2,C) jets,
but it is not automatically real; the dagger comparator is
real and phase invariant but **not** the locked metric.
At a regular point of the previously displayed curved example,
C_tt=1, C_xx=-2i whereas B_tt=1, B_xx=-2, for kappa=1.
No common unit phase fixes that mismatch. Algebraic
factorization of B into a real coframe is not the same
thing as obtaining the canonical metric from DTheta.

A new exact pure-gradient theorem: for Theta=X+iY,
rank(dX)=4 and Im C(dTheta,dTheta)=0 with zero connection,
Y satisfies the Minkowski Killing equation in X coordinates;
the resulting regular central metric is flat. This is **not**
a no-go for complex Theta: an explicit non-i-Hermitian affine
complex frame has an exactly real Minkowski canonical metric.
The missing constructive ingredient is a non-tautological
Theta-derived **two-sided** covariant connection giving
a curved, real canonical central metric from its own jets.
G1 PARTIAL; no physical action has been selected.

<!-- BILINGUAL-UNIT: conformal-causal.integration-verification -->
## Integrated verification scope

The paired G1 notes in this directory are research comparisons, with analytic arguments and finite exact SymPy regression tests. Their PROVED labels describe the stated analytic or algebraic result under its assumptions, not a complete UBT field theory. LEAN-PENDING: these new conformal-track arguments have no compiled Lean proof. Finite coordinate examples, sampled causal intervals and rank calculations do not prove a physical spectrum, global PDE existence or a selected microscopic action. G1 remains PARTIAL.
