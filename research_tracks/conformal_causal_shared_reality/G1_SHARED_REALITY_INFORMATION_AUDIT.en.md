<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: shared-reality-information-audit -->
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

# G1/SR: Shared reality and information: audit

**2026-10-28 · PR #809 · C_working · OPEN.**

## Repo constraints [PROVED]

The master note research_tracks/action_selection/no_positive_invariant_linear_slice.en.md proves the conditional no-positive-invariant-linear-slice theorem for the stated congruence representation. It is NOT a no-go for a nonlinear constrained or physical quotient space. The separate master hamiltonian_first_foundations.en.md proves a symmetry-preserving family of distinct Hamiltonians: the microscopic dynamics needs another selector. The supplied audit's exact R1 kinetic identity was not independently located or verified here.

\[
\operatorname{inertia}(H)=(2,6),\qquad
W\subseteq\mathbb C\otimes\mathbb H,\quad
SL(2,\mathbb C)W=W,\quad H|_W>0\Longrightarrow W=\{0\}.
\]

## Shared reality as operational consistency [AX CANDIDATE]

Observers need not report identical components in different frames. They must agree on gauge-invariant outcomes for the same physical overlap after the covariant transport of observations. Give each finite causal diamond D its local observable algebra and compatible reference state:

\[
\omega_{D_1}|_{\mathcal A(D_1\cap D_2)}
=\omega_{D_2}|_{\mathcal A(D_1\cap D_2)},\quad
\omega_{gD}(\alpha_g(A))=\omega_D(A).
\]

For spacelike separated algebras impose:

\[
[A,B]=0\quad\text{for spacelike separated local observables}.
\]

Add operational no-signalling and the existence/compatibility of global state extensions as independent obligations. Two distinct global probability distributions in the test share identical single-observer marginals, but not correlations. Neither a unique global state nor unique dynamics follows from shared local marginals.

## Transverse physical norm [PROVED, restricted]

For massive vector Proca plane waves, the on-shell divergence equation implies transversality, and the timelike momentum has a spacelike orthogonal complement. With the conventional physical sign:

\[
k_\mu\varepsilon^\mu=0,\quad k^2=m^2>0,\quad
-\eta|_{k^\perp}>0,\qquad \dim k^\perp=3.
\]

For massless Maxwell waves the transverse space has a null gauge direction and the physical positive inner product is defined on the quotient:

\[
k^2=0,\qquad k^\perp/\operatorname{span}(k),
\qquad\dim=2,\quad -\eta>0\text{ on quotient}.
\]

These are vector polarization statements, not a derivation of R1 or graviton helicities. Even equations of motion and their transversality do not fix the energy sign. An exact oscillator counterexample is:

\[
L_\pm(q,\dot q)=\pm\tfrac12(\dot q^2-\omega^2q^2),\quad
\ddot q+\omega^2q=0,\quad
H_\pm=\pm\tfrac12(\dot q^2+\omega^2q^2).
\]

Ghost freedom requires the sign of the reduced Hamiltonian and physical inner product after gauge and second-class constraints, not only Lorentz-covariant transversality.

## Fisher, relative entropy and modular information [PROVED finite example, AX CANDIDATE]

Fisher information on normalized probability families is positive semidefinite by construction. A chosen Cauchy cut may be observer-dependent without breaking Lorentz covariance, but covariance and choice of local probabilities require proof. Neither positive Fisher nor positive relative entropy automatically makes an indefinite kinetic operator healthy. For a faithful finite binary state:

\[
D(\rho_\epsilon\Vert\sigma)
=(\tfrac12+\epsilon)\ln(1+2\epsilon)
+(\tfrac12-\epsilon)\ln(1-2\epsilon)
=2\epsilon^2+\tfrac43\epsilon^4+O(\epsilon^6).
\]

Its positive Hessian defines a symmetric information metric, not an antisymmetric symplectic two-form. For faithful reference states the relative-entropy identity and first law read:

\[
D(\rho\Vert\omega)
=\Delta\langle K_\omega\rangle-\Delta S\ge0,
\qquad \delta S=\delta\langle K_\omega\rangle
\quad\text{to first order}.
\]

Extending these finite formulas to local quantum fields may require algebraic relative entropy or regulators. Jacobson's small-ball argument uses an already defined metric, fixed volume, reference vacuum, area normalization and matter assumptions; it does not produce the full microscopic UBT action by itself.

## A falsifiable UBT information gate [OPEN]

Propose a quantitative functional only as a candidate:

\[
\mathcal I_D[\Theta,\rho]
:=D\!\left(\rho_D\Vert\omega_D[\Theta]\right),\qquad
\mathcal I=\sum_D w_D\,\mathcal I_D.
\]

The Theta-dependent reference state, covariant region weights, observable algebra and avoidance of double counting overlapping diamonds must be constructed, not asserted. A principal causal cone plus shared local records does not fix lower-order dynamics: distinct Klein-Gordon mass parameters share the same principal symbol:

\[
P_m(k)=\eta^{\mu\nu}k_\mu k_\nu-m^2,\qquad
\sigma_2(P_m)(k)=\eta^{\mu\nu}k_\mu k_\nu.
\]

A real selector must additionally determine a positive constrained phase space, symplectic/presymplectic dynamics, a Theta-to-Lorentz-metric map, entropy normalization and a predictive choice between candidate flows. Do not infer Maxwell/Proca, Einstein or a specific kinetic R1 solely from overlap consistency.

## Verification, stop and sources [OPEN]

Seven exact tests in tests/test_shared_reality_information_gate.py were executed locally. Next bounded scientific task: choose one finite causal diamond with an explicitly Theta-derived reference state and local observable algebra, derive the constrained information variation, and verify it changes the dynamical selector without importing a metric or energy sign. G1 remains PARTIAL; do not modify PR #807/#808 or canonical theories and do not merge this draft.

Context: https://doi.org/10.1103/PhysRevLett.116.201101 and https://doi.org/10.1103/PhysRevD.95.046003 . Microcausality and operations: https://doi.org/10.1103/sxkx-sy9g .

