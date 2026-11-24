<!-- BILINGUAL-UNIT: splitjet-composite-onshell-hessian-2026-11-24 -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Conditional finite-dimensional pullback theorem and exact toy tests, not a physical UBT action.
UBT-AI-PROVENANCE-END -->
# Split-jet gravity versus a strictly composite single-Theta action: Hessian gate

**24 November 2026 — C_working / L0 exact conditional algebra; UBT dynamics OPEN.**

## Distinct variational problems

The existing split-jet Palatini and MacDowell–Mansouri comparator varies auxiliary jet coordinates \(K_J,w\) independently. At non-null \(X\), its algebraic map to the tetrad has \(7\) inputs, rank \(4\), nullity \(3\) per spacetime row; over four rows the map has \(28\) inputs, rank \(16\), nullity \(12\). Auxiliary surjectivity enforces the full chosen Palatini tetrad equation **in that extended variational problem**. Declaring these coordinates auxiliary does not establish a unique reconstruction from the locked field \(\Theta\).

A strict one-field closure instead prescribes a single-valued differentiable geometry \(z=F[\Theta]\), including torsion and connections. At one fixed nonzero Fourier momentum, a regular linear response from a single \(M_2(\mathbb C)\) value fluctuation has \(8\) real input amplitudes. Consequently
\[
\boxed{\operatorname{rank}DF(\mathbf k)\le8,\qquad \operatorname{rank}DE(\mathbf k)\le8<16.}\tag{1}
\]
This is a fixed-frequency **symbol rank** statement, not a pointwise jet dimension count or a global obstruction to constrained gravity. It specifically forbids importing the extended \(28\)-variable surjectivity claim unchanged into the strict \(8\)-component physical variation.

## Second variation on and off a parent solution

For any twice differentiable parent action \(S_{\rm geo}[z]\), a smooth composite map \(F\), and compatible measures/boundaries, define \(S_{\rm red}[\Theta]=S_{\rm geo}[F(\Theta)]\). The chain rule gives
\[
\boxed{\delta^2S_{\rm red}[h,k]
=\delta^2S_{\rm geo}[DFh,DFk]
+\langle \mathcal E_{\rm geo},D^2F[h,k]\rangle.}\tag{2}
\]
On a genuine **parent** stationary point \(\mathcal E_{\rm geo}=0\), this reduces to
\[
\boxed{H_{\rm red}=(DF)^*H_{\rm geo}(DF).}\tag{3}
\]
Therefore a parent quadratic TT sector cannot become an elementary Theta TT fluctuation if the composite map's linear response has zero TT image. This is the case for the smooth isotropic congruence-carrier assumptions of `INVERSE_SPIN2_LITTLE_GROUP_DYNAMICS_GATE_2026_11_21.en.md`. It does not rule out an interacting composite massless pole, a different physical representation, nonlocal singular maps, or anisotropic vacuum.

If \(\mathcal E_{\rm geo}\ne0\), the \(D^2F\) term must be retained. The background might still be stationary for the **restricted** composite action; nevertheless it is not an Einstein/Palatini stationary point, so the new quadratic term cannot be identified as the parent's graviton by shortcut.

## Transparent exact counter-comparator

Take \(q\in\mathbb R^8\), with two quadratic spin-two-type composites
\[
Q_+=\frac{q_2^2-q_3^2}{2},\qquad Q_\times=q_2q_3,\qquad
z(q)=(q_0,\ldots,q_7,Q_+,Q_\times).
\]
The independently varied parent \(S_{\rm TT}=\tfrac12(z_8^2+z_9^2)\) has rank-\(2\) Hessian in its two last directions. At the isotropic \(q=0\), however, \(DQ_+=DQ_\times=0\), and
\[
\boxed{S_{\rm red}=\frac18(q_2^2+q_3^2)^2,\qquad H_{\rm red}(0)=0.}\tag{4}
\]
Adding an off-shell parent term \(\lambda z_8\) produces a reduced Hessian block \(\operatorname{diag}(\lambda,-\lambda)\) at \(q=0\); that contribution arises solely from \(\mathcal E_{\rm geo}\,D^2F\) and is **not** an on-shell parent TT excitation. The toy parent is a positive Euclidean quadratic comparator, NOT the physical Palatini symplectic or constraint-reduced Hessian.

## Decision gate

The extended split-jet branch has a conditional Einstein solution-set result but has NOT derived its free auxiliaries from a unique \(\Theta\) equation or established its whole quantum/Dirac quotient. The strictly composite branch must supply \(F[\Theta]\) (in particular its torsion selector), compute \(DF\) including implicit connection variations, and check a real on-shell reduced quadratic TT pole/Hessian. Independent auxiliary variation and a forced composite closure are **not equivalent by default**.

Exact test source: `tools/verify_splitjet_composite_onshell_hessian_gate_2026_11_24.py`. Tests verify algebraic ranks, Hessians and an off-shell control, not a real graviton, ghost freedom or physical dynamics. Lean, repository CI and independent semantic review pending.
