<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- BILINGUAL-UNIT: su3-su2-even-fock.provenance -->
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

# SU(3)–SU(2): even-Fock representation and quark anomaly audit

**Status: conditional exact representation theorem, not a derivation of dynamical UBT matter.** Starting point: the proved biquaternionic colour stabilizer and its exterior Fock carrier. No new fundamental UBT fields or action are declared.

## Colour multiplicity obstruction

The canonical colour representation is

\[
V_c=\operatorname{span}_{\mathbb C}\{I,J,K\},\qquad
\mathcal F_c=\Lambda^\bullet V_c
=\mathbf1\oplus\mathbf3\oplus\bar{\mathbf3}\oplus\mathbf1.
\]

Schur's lemma yields the exact commutant

\[
\operatorname{End}_{SU(3)}(\mathcal F_c)
\simeq M_2(\mathbb C)\oplus\mathbb C\oplus\mathbb C.
\]

A connected commuting weak group may mix the colour singlets, but cannot act nontrivially on the unique colour triplet or antitriplet because a one-dimensional weak character is trivial. Thus a colour-triplet weak doublet cannot live inside the single original Fock carrier. The direct matrix-commutator rank calculation confirms the full complex commutant. This result is restricted to that representation.

## Hypothetical weak carrier and minimal extension

Introduce a **hypothetical** weak doublet representation space, not a newly postulated microscopic field:

\[
W=\mathbb C^2,\quad
\mathcal F_{\rm even}=\Lambda^{\rm even}(V_c\oplus W),\quad
\dim_{\mathbb C}\mathcal F_{\rm even}=1+10+5=16.
\]

Its colour restriction is exactly

\[
\mathcal F_{\rm even}\big|_{SU(3)}
\simeq4\cdot\mathbf1\oplus2\cdot\mathbf3
\oplus2\cdot\bar{\mathbf3}\simeq2\mathcal F_c.
\]

The right-hand side has the content of two original colour Fock carriers. Among whole copies of the original representation, that is the minimum multiplicity needed for a weak quark doublet and two independent conjugate quark singlets. This algebraic isomorphism does not identify a weak field in Theta.

## Hypercharge and full generation spectrum

Assign the following **candidate** occupation-count hypercharge:

\[
Y=-\frac13N_c+\frac12N_w,\quad
N_c=\sum_{i=1}^{3}c_i^\dagger c_i,\quad
N_w=\sum_{i=4}^{5}c_i^\dagger c_i.
\]

Assuming that the listed states are left-handed Weyl multiplets, the decomposition has exactly the familiar generation including a sterile conjugate neutrino:

\[
\begin{aligned}
Q_L&:(\mathbf3,\mathbf2)_{+1/6},&
u^c&:(\bar{\mathbf3},\mathbf1)_{-2/3},&
d^c&:(\bar{\mathbf3},\mathbf1)_{+1/3},\\
L_L&:(\mathbf1,\mathbf2)_{-1/2},&
e^c&:(\mathbf1,\mathbf1)_{+1},&
\nu^c&:(\mathbf1,\mathbf1)_0.
\end{aligned}
\]

The occupation sectors are:

| Sector | Multiplicity | Name | Charge |
|---|---:|---|---:|
| `(0,0)` | 1 | `nu^c` | 0 |
| `(0,2)` | 1 | `e^c` | +1 |
| `(1,1)` | 6 | `Q_L` | +1/6 |
| `(2,0)` | 3 | `u^c` | -2/3 |
| `(2,2)` | 3 | `d^c` | +1/3 |
| `(3,1)` | 2 | `L_L` | -1/2 |

This reproduces the **well-known** exterior-Fock embedding associated with SU(5) and Spin(10):

\[
\Lambda^{\rm even}\mathbb C^5
=\Lambda^0\mathbb C^5\oplus\Lambda^2\mathbb C^5
\oplus\Lambda^4\mathbb C^5
\simeq\mathbf1\oplus\mathbf{10}\oplus\bar{\mathbf5}.
\]

It is not a derivation of a physical SU(5) or Spin(10) gauge symmetry.

## Gauge and global anomalies

The following traces vanish, **conditional on the physical Weyl interpretation**:

\[
\mathcal A_{SU(3)^3}\propto2-1-1=0,\quad
\mathcal A_{SU(3)^2Y}\propto2\left(\frac16\right)-\frac23+\frac13=0.
\]

\[
\mathcal A_{SU(2)^2Y}\propto3\left(\frac16\right)-\frac12=0,\quad
n_{SU(2)\,\mathrm{doublets}}=3+1=4\equiv0\pmod2.
\]

\[
\operatorname{Tr}Y=6\left(\frac16\right)+3\left(-\frac23\right)
+3\left(\frac13\right)+2\left(-\frac12\right)+1=0.
\]

\[
\operatorname{Tr}Y^3=6\left(\frac16\right)^3
+3\left(-\frac23\right)^3+3\left(\frac13\right)^3
+2\left(-\frac12\right)^3+1=0.
\]

The weak doublet parity is even, so the Witten global obstruction is absent in this conditional spectrum. Local non-Abelian cubic and Abelian-mixed traces are checked directly using the actual lifted matrices, not only their dimensions.

## Hypercharge assumptions and uniqueness caveat

For a more general affine occupation-number charge,

\[
Y'=aN_c+bN_w+c\mathbf1,\quad
\operatorname{Tr}Y'=8(3a+2b+2c),\quad
\mathcal A_{SU(3)^2Y'},\mathcal A_{SU(2)^2Y'}\propto3a+2b+2c.
\]

the cubic Abelian trace factorizes:

\[
\operatorname{Tr}(Y')^3
=4(3a+2b+2c)(9a^2+6ab+6ac+5b^2+4bc+2c^2).
\]

Anomaly cancellation alone leaves a continuous family. Assuming that the empty Fock vacuum has zero hypercharge and imposing the conventional quark normalization singles out the displayed direction:

\[
c=0,\quad3a+2b=0,\quad a=-\frac13,\quad b=\frac12.
\]

Those choices are **additional assumptions**, not consequences of UBT dynamics. The standard hypercharge normalization is not a first-principles parameter prediction.

## Evidence and remaining dynamical gap

**Exact within the assumed representation:** Schur commutant obstruction, colour-module doubling, generation branching, charge table, all local perturbative anomaly identities, and the weak global parity test. The independent SymPy implementation supplies twenty-five checks, including the complete cubic-colour tensor and exact commutant rank; pytest and dedicated CI accompany this note.

**Open:** deriving the weak carrier, even parity and Lorentz chirality from the single-action Theta Hessian; obtaining real chiral propagators, gauge invariance, Yang–Mills kinetic terms, masses, Yukawa couplings and the observed generation structure. The representation embedding is standard mathematics, not evidence of a solved UBT unification. Next gate: derive or exclude a Lorentz-commuting weak multiplicity sector from the unique eventual action.

Sources: `canonical/su3_derivation/su3_stabilizer_exterior_fock.tex`, `research_tracks/T2_GAUGE/su3_fock_chiral_anomaly.en.md`, and `canonical/ACTION.en.md`.
