<!-- BILINGUAL-UNIT: rh-transfer.scope -->
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

# Can the reported RH proof determine UBT dynamics?

**2026-11-21 · C_working · LEAN-PENDING · research, not canonical physics.**

<!-- BILINGUAL-UNIT: rh-transfer.what -->
## What is actually transferable?

The [author's note](https://alpo.ge/remark.pdf) and the [source-linked proof map](https://github.com/nasqret/riemann-rev) identify iterated *automorphic* theta lifts, divisibility-versus-size estimates using Bost slopes, and positive weights over Galois characters. A characteristic error balance is
\[
\frac{x}{m}+m,\qquad m\asymp\sqrt{x}.
\]
Here \(x\) is an arithmetic scale and \(m\) counts lifts. Neither is a physical UBT mode or mass. Arithmetic positivity does not mean positive physical Hamiltonian energy. The lifts between number-theoretic unitary groups do not automatically act on the one canonical UBT field. The finite Fourier/metaplectic analogy is separately tested in merged PR #910.

<!-- BILINGUAL-UNIT: rh-transfer.obstruction -->
## Exact obstruction: symmetry and a symplectic form do not select time evolution

On the *existing* eight-real biquaternion value space, take invariant \(B\), \(JX=iX\), and \(\Omega(X,Y)=B(X,JY)\). For each real \(\lambda\) define only a **toy** generator:
\[
b(X)=B(X,X),\qquad H_\lambda(X)=\tfrac12 b(X)+\tfrac{\lambda}{4}b(X)^2.
\]
Every generator retains the declared global phase and Lorentz congruence invariance and the same \(\Omega\). With \(\iota_{\dot X}\Omega=dH_\lambda\), exact differentiation gives
\[
\boxed{\dot X=(1+\lambda b(X))\,iX},\qquad \frac{d}{dt}b(X)=0.
\]
Indeed \(dH_\lambda(Y)=(1+\lambda b)B(X,Y)\) and \(\Omega(\dot X,Y)=-B(J\dot X,Y)\). For initial fields with \(b\ne0\), changing \(\lambda\) changes the time rate while preserving all those symmetries. There is no spatial propagation. This sharpens the previously documented Hamiltonian nonuniqueness result; it does not derive the UBT action.

<!-- BILINGUAL-UNIT: rh-transfer.gate -->
## The one potentially productive transfer gate

Identify a **specific arithmetic theta-lift kernel** \(\mathcal L\) and its source/target representation spaces. Only then attempt to prove a two-sided-connection intertwining law and compatibility with actual constraints and energy:
\[
\mathcal L D_\mu=D'_\mu\mathcal L,\qquad
\mathcal L(\ker\mathcal C)\subseteq\ker\mathcal C',\qquad
H_{\rm phys}\big|_{\ker\mathcal C/\mathcal G}\ge0.
\]
These equations are **tests to pose, not results**. A unitary oscillator representation, an arithmetic positive Fourier weight and a positive physical energy are three different properties. If such a genuine intertwiner cannot be formulated without adding ad hoc UBT ontology, close this transfer direction as unsupported.

<!-- BILINGUAL-UNIT: rh-transfer.status -->
## Verification and status

Five exact local SymPy 1.14.0 checks confirm the displayed finite-dimensional Hamilton equation and conservation identity. Reproducible test source: research_tracks/action_selection/tests/test_rh_theta_lift_selector.py. This is not an implementation of the real RH proof, its theta lifts, an on-shell physical UBT dynamics or a ghost cure. **LEAN-PENDING; independent bilingual semantic review pending. Dynamics OPEN.**
