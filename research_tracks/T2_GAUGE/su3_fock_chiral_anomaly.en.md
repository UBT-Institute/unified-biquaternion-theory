<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: su3-fock-chiral-anomaly.provenance -->
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

# SU(3) exterior Fock anomalies and the missing chiral quark spectrum

**Status: exact conditional representation-theory consequences; physical fermions/QCD NOT derived.** This extends the proved canonical SU(3) stabilizer in canonical/su3_derivation/su3_stabilizer_exterior_fock.tex, not a competing construction. A physical left-handed Weyl interpretation of each Fock block is **an extra explicit assumption**, not a UBT theorem.

## 1. Canonical colour carrier

The existing Hermitian and oriented complex-volume stabilizer is SU(3). Exterior degree sectors are one singlet, one triplet, one antitriplet, and one singlet, with the proved second-quantized Gell-Mann action.

\[
V=\operatorname{span}_{\mathbb C}\{I,J,K\},\qquad
\Lambda^\bullet V=\mathbf1\oplus\mathbf3\oplus\overline{\mathbf3}\oplus\mathbf1,\qquad
T^a=\frac{\lambda^a}{2},\qquad
\widehat T^a=\sum_{i,j=1}^{3}c_i^\dagger T^a_{ij}c_j.
\]

## 2. Cubic anomaly, conditional on Weyl chirality

If each degree sector represents **one left-handed Weyl multiplet**, the total SU(3) cubic anomaly vanishes algebraically: the conjugate degree-two representation cancels the degree-one contribution, while the singlets contribute zero.

\[
\mathcal A_3^{abc}=
\operatorname{Tr}_{\Lambda^\bullet V}
\left(\widehat T^a\{\widehat T^b,\widehat T^c\}\right)
=\mathcal A_{\mathbf3}^{abc}+\mathcal A_{\overline{\mathbf3}}^{abc}=0.
\]

The independent exact checker evaluates all 288 tensor entries (8 choices of first index and 36 unordered remaining index pairs), including nonzero conjugate witnesses:

\[
\operatorname{Tr}_{\mathbf3}(T^8\{T^8,T^8\})=-\frac{\sqrt3}{6},
\qquad
\operatorname{Tr}_{\overline{\mathbf3}}(\overline T^8\{\overline T^8,\overline T^8\})=+\frac{\sqrt3}{6}.
\]

Assigning **opposite** Weyl chirality to the two colour blocks instead changes the anomaly sign and invalidates this cancellation. Formal fermionic ladder matrices do not prove physical Lorentz spinor statistics or chirality.

## 3. Colour-compatible hypothetical U(1)

Let the extra U(1) generator commute with colour and be scalar on every exterior degree. Under the same Weyl assumption, mixed-colour, mixed gravitational and cubic Abelian anomaly traces are exactly:

\[
Y=\sum_{k=0}^3 y_k\Pi_k,\qquad
\operatorname{Tr}(Y\widehat T^a\widehat T^b)=
\frac{y_1+y_2}{2}\delta^{ab}.
\]

\[
\operatorname{Tr}Y=y_0+3y_1+3y_2+y_3,\qquad
\operatorname{Tr}Y^3=y_0^3+3y_1^3+3y_2^3+y_3^3.
\]

Cancelling the mixed colour and gravitational anomalies gives:

\[
y_2=-y_1,\qquad y_3=-y_0.
\]

Then the Abelian cubic trace vanishes automatically. This is a **two-parameter charge family**, not a uniquely derived Standard Model hypercharge.

## 4. Affine fermion-number ansatz

Further restrict U(1) to an affine function of the exterior number operator. Cancellation of its colour-mixed anomaly fixes the offset, but not the overall normalization:

\[
Y=aN+b\mathbf1,\qquad N=\sum_i c_i^\dagger c_i,\qquad
\boxed{3a+2b=0,\quad Y=a\left(N-\frac32\right).}
\]

\[
(y_0,y_1,y_2,y_3)=\left(-\frac{3a}{2},-\frac a2,+\frac a2,+\frac{3a}{2}\right).
\]

All listed gauge and gravitational anomaly traces then cancel. The conjugate colour blocks have opposite charges and admit an invariant bilinear mass pairing; the singlets pair too. This candidate representation is therefore **vectorlike as a gauge spectrum**, not a proof of the chiral Standard Model.

## 5. Compare with a Standard Model quark generation

In all-left-handed notation, the quark part of one physical generation contains a weak doublet with two colour triplets, and two separately charged colour antitriplets:

\[
Q_L:\;2\times\mathbf3_{1/6},\qquad
u_R^c:\;\overline{\mathbf3}_{-2/3},\qquad
d_R^c:\;\overline{\mathbf3}_{+1/3}.
\]

The Standard Model colour and mixed-colour anomaly sums are:

\[
\mathcal A_{SU(3)^3}=2-1-1=0,\qquad
\mathcal A_{SU(3)^2U(1)}\propto
2\left(\frac16\right)-\frac23+\frac13=0.
\]

A single exterior Fock carrier contains only **one** triplet and **one** antitriplet block; it cannot provide both distinct conjugate charges or the weak-doublet multiplicity without a further **dynamically derived** chiral/weak sector. Leptons are also required for the complete electroweak anomaly audit.

## 6. Reproducibility and strict limitations

Verification: tools/verify_su3_fock_anomalies.py (22 exact checks, including all cubic tensor components), tests/test_su3_fock_anomalies.py, and dedicated CI workflow. **No SU(3) gauge dynamics, quark propagator, Lorentz spinor chirality, hypercharge, physical anomaly cancellation, or new fundamental action is claimed.** The proved colour algebra is retained unchanged. Next mathematical gate: derive a chiral Lorentz-spinor/weak carrier and its multiplicities from the same microscopic Theta theory, then retest all anomalies and its dynamical Yang-Mills sector.
