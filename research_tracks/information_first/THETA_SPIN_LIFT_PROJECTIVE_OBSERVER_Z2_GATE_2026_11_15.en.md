<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact scoped Spin-cover and observer-projective geometry identities; not a derivation of fermion Fock statistics, QED, GR, the Standard Model, or a new fundamental action.
UBT-AI-PROVENANCE-END
-->

# Quantum observer and spin lift gate: a central Z2 no-go for local Theta-to-Weyl projection, with projective holonomy

**2026-11-15 — mathematical level L0 conditional, full UBT quantum dynamics OPEN.**

**Research ordering:** one complete complex biquaternion Theta -> quantum states/observer readouts AND canonical gravity -> emergent fermionic charged modules and QED/GR -> classical Maxwell -> Standard Model. This note builds on canonical/geometry/biquaternion_tetrad.tex; research_tracks/information_first/ONE_THETA_DIRAC_EVOLUTION_PULLBACK_ACTION.md, BIQUATERNION_INTRINSIC_CAR_SPIN_STATISTICS_GATE.md and THETA_DIRAC_CHARGE_CURRENT_PROJECTED_U1_SOLDERING_GATE_2026_11_15.en.md. It does not change the locked tetrad definition.

## 1. Central Z2 theorem: no nonzero local covariant Weyl vector from a purely tensorial Theta carrier

The canonical Lorentz-real tetrad obeys
\[
E_\mu=N_0^{-1/2}D_\mu\Theta\in W_L=i\,{\rm Herm}_2,\qquad
\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}I.
\]
On the Lorentz-congruence realization of Theta, a local Spin^+(1,3)=SL(2,C) frame change acts as
\[
\Theta\mapsto S\Theta S^\dagger,\quad E_\mu\mapsto SE_\mu S^\dagger.
\]
At the central element z=-I_2 (the 2-pi spin-frame rotation), EVERY matrix in this representation is unchanged: z X z†=X. The same holds for all covariant tensor-valued jets (under a constant central frame transformation), the metric and local observer clock tensors, provided their representation descends to the proper Lorentz group.

Suppose a single-valued local map F made only from such tensorially transforming input is required to be equivariant into an ordinary left Weyl module:
\[
F[S\Theta S^\dagger,\ldots]=S F[\Theta,\ldots].
\]
Apply S=z=-I. The entire list of arguments is unchanged, but the right side becomes -F. Therefore
\[
\boxed{F=-F\quad\Rightarrow\quad F=0.}
\]
Likewise a Dirac spinor transforms by minus the identity under the central spin element and cannot arise as a nonzero deterministic local tensorial map. This is a simple exact representation-theoretic Z2 obstruction. It does not rely on smoothness, locality radius or equations of motion, only single-valued equivariance and absence of hidden spin-odd input.

**Scope:** This is NOT a no-go for quantized soliton/skyrmion operators, superselection sectors, spin-structure-associated quantum modules, disorder operators, nonlocal Wilson/holonomy constructions, genuine operator CAR algebra or a field Theta with a DIFFERENT fundamental left-spin transformation law. It does show that the old flat Dirac column map Theta=[u v] -> (u,epsilon conjugate(v)) under the assumed LEFT action Theta->STheta cannot silently be transferred to the canonical CONGRUENCE action: under -I the former changes sign and the latter does not.

The topological spin structure and the double-cover representation are not themselves additional local dynamical photon/electron fields. But they are mathematical input not yet dynamically selected by Theta.

## 2. Correction: K=Theta Theta† is not a Lorentz vector under geometric congruence

The earlier positive soldering comparator establishes:
- Under the *LEFT spinor representation* Theta->STheta, the bilinear K=Theta Theta† satisfies K->S K S†.
- Under a RIGHT unitary charge phase Theta->Theta R with RR†=I, K is invariant.

These are correct but do NOT imply the same Lorentz covariance if the SAME microscopic Theta uses geometric CONGRUENCE Theta->STheta S†. In that case
\[
K'=(S\Theta S^\dagger)(S\Theta S^\dagger)^\dagger
=S\Theta(S^\dagger S)\Theta^\dagger S^\dagger.
\]
This equals SKS† for unitary S, but not for generic nonunitary boosts. Explicitly for Theta=I and S=diag(exp(beta/2),exp(-beta/2)) with real beta:
\[
K'=\operatorname{diag}(e^{2\beta},e^{-2\beta}),\quad
SKS^\dagger=\operatorname{diag}(e^\beta,e^{-\beta}).
\]
They differ when beta!=0.

Thus K is a useful observer-spin object or left-spinor bilinear, but is NOT automatically a Lorentz four-vector in the canonical Theta-congruence representation. This removes an implicit shortcut from recent joint-soldering proposals; the canonical sharp E=DTheta metric cannot be replaced with i dK.

## 3. An observer clock repairs covariance of *projective readout* without choosing a sign

Use the already established positive Lorentz clock N and the observer-normalized matrix
\[
T_N=N^{-1/2}\Theta N^{-1/2},\quad
\rho_N=T_NT_N^\dagger/\operatorname{tr}(T_NT_N^\dagger).
\]
Under the joint geometric congruence Theta'=STheta S†, N'=SNS†, let
\[
\boxed{U_N=N'^{-1/2} S N^{1/2}}.
\]
Then U_N† U_N=I, and for S in SL2 and fixed det N, det U_N=1. Thus U_N belongs to SU(2) and
\[
T'_{N'}=U_N T_N U_N^\dagger,\quad
\rho'_{N'}=U_N\rho_N U_N^\dagger.
\]
So an observer-relative nondegenerate spectral projector of rho is a well-defined SU2-covariant PROJECTIVE quantum observable on a patch where rho has distinct eigenvalues. At S=-I we have U_N=-I: rho and its eigenprojector do not change, whereas an assigned spin-half eigenvector does change sign. The clock yields **projective covariance**, not a canonically selected spinor vector; local phase gauge remains.

This comparison is a conditional quantum-information readout, not a microscopic selection of the clock, a Hilbert space of charged particles, a UBT QED gauge action or fermionic CAR.

## 4. Concrete 2-pi spin lift via one Theta-derived positive projective state

Focus first on observer-rest-frame SU2 rotations (not generic boosts). Choose a positive Hermitian K0=I+r sigma1, 0<r<1, realizable as K0=Theta0 Theta0† for Theta0=sqrt(K0). Set
\[
S(\varphi)=\exp(i\varphi\sigma_3/2),\quad
K(\varphi)=S(\varphi)K_0S(\varphi)^\dagger,\quad
P_+(\varphi)=\frac{K(\varphi)-(1-r)I}{2r}.
\]
Then P_+ is a rank-one Hermitian projector for all phi, P_+(2pi)=P_+(0), and a continuous spin lift
\[
|\psi(\varphi)\rangle=S(\varphi)\frac{(1,1)^T}{\sqrt2}
\]
has |psi(2pi)>=-|psi(0)>. Therefore NO single-valued equivariant spinor map of the projector can produce the signed vector around the loop.

A different, single-valued representative of the same projective path is
\[
|v(\varphi)\rangle= (e^{i\varphi},1)^T/\sqrt2.
\]
Its Berry connection and geometric phase are
\[
a=-i\langle v|dv\rangle=\tfrac12d\varphi,\quad
\oint a=\pi,\quad
\boxed{e^{i\oint a}=-1}.
\]
This is an EXACT comparator showing how projective transport can encode a 2-pi sign that local tensorial data cannot choose. The phase is path/geometric and does not by itself certify exchange antisymmetry, spin-statistics, an electron, its charge or a physical photon.

For the full two-level pure-state parameterization
\[
|v(\theta,\varphi)\rangle=
(\cos(\theta/2),e^{i\varphi}\sin(\theta/2))^T,
\]
the local Berry connection a=sin²(theta/2)dphi gives
\[
f=da=\tfrac12\sin\theta\,d\theta\wedge d\varphi,
\quad \boxed{\int_{S^2}f=2\pi,\quad c_1=1}.
\]
This is the standard projective-state Hopf-line-bundle obstruction to a global smooth eigenvector gauge. It is a theorem about CP1 quantum kinematics, not a derivation of the electromagnetic U1 connection.

**Lorentz warning:** eigenprojectors built from bare K=Theta Theta† fail generic boost covariance. Their observer-relative analogues from rho_N, as in section 3, do possess the correct induced SU2 covariance. Ordinary positive matrix eigenvectors cannot be declared full-SL2 Weyl spinors by fiat.

## 5. Implications for the next real quantum-UBT gate

The one-Theta programme now faces a sharper choice than "read a spinor from the four complex entries":
1. **Change the physical representation through a derived spin lift**: identify a spin-structure-compatible quantum Hilbert/module and a Spin(1,3) action carrying the central -I sign, while Theta's classical congruence tensor data remain unchanged. Explain how the lift or local fermionic operator is derived, rather than silently inserting a reference spinor.
2. **Construct projective transport/inter-point correlations** from observer-relative rho_N; compute holonomy and determine whether any selected quantum operator module carries genuine CAR and the spin-statistics theorem hypotheses. A Berry holonomy of -1 is insufficient by itself.
3. **Check the canonical tetrad simultaneously** under the full composite D[Theta] and its quantum variations. Compute an on-shell coupled quadratic Hessian, physical charge first-class constraints and two healthy photon modes; distinguish Lorentz spin holonomy from internal electromagnetic U1.
4. **Only after this** derive QED and the classical curved Maxwell limit, and then attempt the complete chiral SM spectrum.

The already recorded BIQUATERNION_INTRINSIC_CAR_SPIN_STATISTICS_GATE.md provides a local single-mode CAR algebra inside M2(C), but neither its grading/polarization nor many-mode locality is selected by the observer projective path. The older theta_fermion_emergence.tex and theta_quantum_structure.tex contain stronger historical statements about winding parity and fermionic statistics; audit those against the current explicit CAR and exchange-path objections rather than promoting them as proved here.

## Verification

Seven scoped SymPy/pytest checks (2026-11-15) pass locally, covering central Z2 blindness on Theta tensor jets; algebraic zero of any equivariant Weyl component; the nonunitary-boost K counterexample; observer-clock SU2 covariance; signed 2pi eigenline lift of a periodic projector; Berry -1 equatorial holonomy; and unit CP1 first Chern integral. Regression: tests/test_theta_spin_lift_observer_gate.py.

**Status:** exact representation-theoretic and projective bundle kinematics; no UBT fermions, QED or GR derived. Maintain the existing locked canonical action/tetrad and record failures rather than replacing them silently.
