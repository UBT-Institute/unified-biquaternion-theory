<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Restricted exact algebraic identities; not a proof of QED, GR, photons, or the fundamental UBT action.
UBT-AI-PROVENANCE-END
-->

# A vector U(1) inside ONE Theta: opposite column phases of the flat Dirac map versus the canonical tetrad

**2026-11-15. C_working.** Do not confuse this conditional flat-Dirac module with the same-field classical Lorentz-congruence representation.

Prior exact results are retained, not rediscovered: the one-Theta flat Dirac evolution in research_tracks/information_first/ONE_THETA_DIRAC_EVOLUTION_PULLBACK_ACTION.md, the vector/axial Lorentz centralizer in research_tracks/unified_physics_axioms/DIRAC_LORENTZ_CENTRALIZER_QED_GATE_2026_11_12.en.md, the right-multiplication Hermitian-slice no-go and metric test in the same unified_physics_axioms folder, and research_tracks/action_selection/central_phase_metric_gate.en.md.

## 1. Physical vector U(1) is NOT the central Theta phase

With the faithful biquaternion matrix \(\Theta=[u,v]\) and the existing invertible real-linear flat spinor map
\[
\epsilon=i\sigma_2,\qquad \psi_L=u,\quad\psi_R=\epsilon\bar v,
\]
consider
\[
R_\alpha=e^{i\alpha\sigma_3}
=\operatorname{diag}(e^{i\alpha},e^{-i\alpha}),\qquad
\boxed{\Theta\mapsto\Theta R_\alpha.}
\]
Then \(u\to e^{i\alpha}u\), \(v\to e^{-i\alpha}v\), hence
\[
\boxed{\psi_L\to e^{i\alpha}\psi_L,\qquad
\psi_R\to e^{i\alpha}\psi_R.}
\]
This is exactly the vector charge phase of a single Dirac particle. It commutes with the LEFT SL(2,C) Lorentz-spin action on Theta used by this flat comparator; unlike the residual transverse SO(2) generator, it does not distinguish the two spin polarizations.

By contrast, a CENTRAL Theta phase \(\Theta\mapsto e^{i\alpha}\Theta\) acts on these Dirac variables as \(\psi_L\to e^{i\alpha}\psi_L\), \(\psi_R\to e^{-i\alpha}\psi_R\), i.e. AXIALLY. Therefore the previous idea that an observer-invisible central Theta phase is automatically the electromagnetic vector U1 was conflating representations.

## 2. Exact global symmetry of the assumed flat Dirac evolution, including mass

The conditional flat first-order equation from the existing one-Theta bridge is
\[
i\partial_t\Theta=-\boldsymbol\sigma\cdot\mathbf p\,\Theta+
m\,\epsilon\bar\Theta\sigma_1,\quad\mathbf p=-i\nabla.
\]
Using \(\bar R_\alpha\sigma_1=\sigma_1R_\alpha\), the antilinear mass map obeys
\[
\epsilon\overline{\Theta R_\alpha}\,\sigma_1
=(\epsilon\bar\Theta\sigma_1)R_\alpha.
\]
For constant alpha the entire chosen flat Dirac equation is therefore equivariant. Also
\(\det(\Theta R_\alpha)=\det\Theta\), so the commuting-field mass comparator \(2m\operatorname{Re}\det\Theta\) is invariant. Actual Grassmann-odd fermions require the separately recorded graded mass and CAR analysis; this is NOT an independent proof of those statistics.

For a LOCAL alpha(x), an external standard-gauge comparator
\[
\mathscr D_\mu\Theta=\partial_\mu\Theta-iq a_\mu\Theta\sigma_3,
\quad R=e^{iq\alpha\sigma_3},\quad a'_\mu=a_\mu+\partial_\mu\alpha
\]
satisfies \(\mathscr D'_\mu(\Theta R)=(\mathscr D_\mu\Theta)R\). Here \(a_\mu\) is an ASSUMED comparator, not a field derived from Theta. No gauge kinetic coefficient, Gauss law or photon follows from this identity.

## 3. The central sharp metric survives, but the real tetrad does NOT

In M2(C), quaternion sharp is adjugation. Since det R=1, \(R^\sharp R=I\). If the geometrical derivative could transform homogeneously as \(E'_\mu=E_\mu R_\alpha\), then the central sharp bilinear preserves the metric EXACTLY:
\[
\frac12((E'_\mu)^\sharp E'_\nu+(E'_\nu)^\sharp E'_\mu)
=R^\sharp (g_{\mu\nu}I)R=g_{\mu\nu}I.
\]
But the locked canonical reality condition additionally requires \(E_\mu\in W_L=i\operatorname{Herm}_2\). At a flat nondegenerate tetrad \(E_0=iI\),
\[
E_0'=iR_\alpha,\quad
E'_0+(E'_0)^\dagger=i(R_\alpha-R_\alpha^\dagger)
=-2\sin\alpha\,\sigma_3.
\]
This fails the canonical physical slice for generic alpha. In the direct right-only action the surviving diagonal subgroup is discrete \(R=\pm I\).

Furthermore right multiplication by R commutes with the flat Dirac LEFT SL2 spin action \(\Theta\mapsto S\Theta\) but fails to commute with canonical GEOMETRIC Lorentz congruence \(\Theta\mapsto S\Theta S^\dagger\) when \([R,S^\dagger]\ne0\). A rotation about sigma_1 is a concrete counterexample.

**Precise conclusion:** a genuine mass-preserving vector U1 appears in an existing single-Theta flat Dirac representation, but the same simple right-column action is NOT an independent gauge symmetry of the locked geometrical Lorentz slice. This is a scoped homogeneous-action obstruction, not a no-go for a nonlinear physical spinor/tetrad soldering map or a dynamically derived phase-neutral composite tetrad.

## 3b. Positive *noncanonical* comparison: a phase-neutral bilinear soldering is kinematically possible

There is a precise way to escape the direct right-multiplication reality failure, at the cost of changing the tetrad **map** (not an authorized revision of canonical UBT):
\[
\boxed{K[\Theta]=\Theta\Theta^\dagger.}
\]
Under the flat Dirac LEFT Lorentz action \(\Theta\mapsto S\Theta\), the Hermitian bilinear transforms as \(K\mapsto SKS^\dagger\), i.e. it has the correct four-vector Lorentz transformation. Under the physical Dirac vector phase \(\Theta\mapsto\Theta R_{\alpha(x)}\), it is *exactly invariant*, even for space-dependent alpha, since \(RR^\dagger=I\).

As a local comparison define an **alternative** tetrad
\[
\boxed{\widetilde E_\mu=i\,\partial_\mu K.}
\]
For any Hermitian K, these values lie in \(W_L=i\mathrm{Herm}_2\). Choose the smooth positive-definite matrix background
\[
K=(c+t)I+x\sigma_1+y\sigma_2+z\sigma_3,\quad
c+t>\sqrt{x^2+y^2+z^2},\quad c>0.
\]
It has a unique positive square root \(\Theta=K^{1/2}\in M_2(\mathbb C)\), so no second fundamental field has been introduced. The candidate legs are \(\widetilde E_\mu=i\sigma_\mu\), with the EXACT canonical sharp bilinear \(\widetilde g=\eta\), nondegenerate Minkowski. Moreover \(\widetilde E_\mu\) is right-U1 invariant while K transforms by Lorentz congruence. This is a **constructive kinematic example of a nonlinear spinor-to-geometric soldering map**, not a proof that UBT selects it.

**Two sharp limitations:**
1. Canonical UBT locks \(E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta\), **not** \(\widetilde E_\mu=iD_\mu(\Theta\Theta^\dagger)\). The positive example does NOT satisfy canonical Axiom C unless a derived, covariant, dynamically admissible composite two-sided derivative establishes equality. In the naive D=partial comparator, a Hermitian \(\Theta=K^{1/2}\) even gives Hermitian, not anti-Hermitian, derivatives. Do not silently replace the definition.
2. K is invariant under the **entire right U(2)**, not merely the one-dimensional electromagnetic vector phase. It therefore does not select the correct physical internal gauge group or its charges and cannot by itself generate a photon kinetic term.

This explicit positive comparator identifies a useful NEXT TEST: can the existing UBT composite connection (with its full variation, torsion and Lorentz slice) yield a physically selected phase-neutral tetrad bilinear and a smaller residual charged module *without* abandoning the locked E=DTheta definition? If not, the simple same-carrier geometrical and fermionic representations remain incompatible on this branch.

## 4. What still must be derived before calling this QED

1. A real Lorentz-covariant physical spinor observable from the SAME Theta and constrained geometric phase space that carries the vector phase without disrupting E in W_L.
2. A derived local first-class U1 generator, conserved charge and suitable gauge-covariant transport, not an independent a_mu added by hand.
3. Positive-norm massless two-helicity spin-one mode, Maxwell/QED Ward identities and appropriate charged matter currents.
4. Simultaneous gravitation from the same microscopic action, then semiclassical Maxwell and Standard Model matching.
5. Information/observer readouts as quantitative constraints on transport and states, not as an automatically unique Hamiltonian.

Regression: tests/test_theta_dirac_vector_u1_sharp_slice_gate.py checks these restricted matrix identities. The larger PR #897 remains draft with known CI failures, so these notes are NOT in master until the merge gates are cleared.
