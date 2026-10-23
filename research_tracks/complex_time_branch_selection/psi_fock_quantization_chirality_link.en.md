<!-- BILINGUAL-UNIT: psi-fock.header -->
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

# ψ-Fock quantization and chirality–winding correlation: an attempted derivation

**Track type:** RESEARCH TRACK — OPEN DERIVATION ATTEMPT  
**Date:** 2026-09-15  
**Verdict:** PARTIAL/CONDITIONAL — see §6 for the precise scope.  
**Czech edition:** `psi_fock_quantization_chirality_link.cs.md`  
**Bilingual policy:** `../../BILINGUAL_CONTENT_POLICY.en.md`  
**Verification script:** `../../tools/verify_psi_fock_chirality_selection.py`  
**Cross-references:**
- `canonical/chirality/step1_psi_parity.tex` — definition of the Dirac operator and chirality sectors
- `canonical/chirality/gap_c1_closure.tex` — Gap C1 status and T2\_GAUGE condition
- `psi_branch_selection.en.md` — gap G3, the parent track

<!-- BILINGUAL-UNIT: psi-fock.scope -->
> **Scope.** This document tests whether the requirement that the second-quantized
> ψ-mode Hamiltonian of Θ be bounded below dynamically forces the correlation
> (n>0, left-handed) + (n<0, right-handed), as an analogue of the Dirac-sea
> argument for the standard Dirac equation. The result is **PARTIAL/CONDITIONAL**:
> the free-theory Fock Hamiltonian does not produce this selection, and
> additional input — labelled **NEW AXIOM CANDIDATE** — is required.
> No canonical file, gap status, or CLAIMS.yaml entry is modified.

---

<!-- BILINGUAL-UNIT: psi-fock.sec1 -->
## 1. Setup and starting point

<!-- BILINGUAL-UNIT: psi-fock.dirac-operator -->
### 1.1 The Dirac operator and chirality sectors

Following `canonical/chirality/step1_psi_parity.tex`, Lemma 2 and Proposition 3,
the relevant Dirac operator on the UBT field Θ in the flat ψ-sector is

$$
\mathcal{D} = i\gamma^\mu \nabla_\mu + \gamma^5 \partial_\psi.
$$

The ψ-parity operator $P_\psi : \psi \mapsto -\psi$ acts as $\gamma^5$ on the
spinorial component of Θ. The two chirality sectors (eigenspaces of $P_\psi$)
are

$$
\mathcal{H}_- \;(P_\psi = -1),
\qquad
\mathcal{H}_+ \;(P_\psi = +1).
$$

The chiral representation is used throughout:
$$
\gamma^0 = \begin{pmatrix}0 & I_2 \\ I_2 & 0\end{pmatrix}, \quad
\gamma^5 = \begin{pmatrix}-I_2 & 0 \\ 0 & I_2\end{pmatrix}, \quad
\{\gamma^0,\gamma^5\} = 0.
$$

**Scope restriction.** This section treats the free, flat, gauge-field-free and
gravity-free kinetic action for Θ in the ψ-sector only. No gauge coupling, no
background, and no curved connection is introduced.

<!-- BILINGUAL-UNIT: psi-fock.sec2 -->
## 2. Mode expansion and coupled Weyl equations

<!-- BILINGUAL-UNIT: psi-fock.mode-expansion -->
### 2.1 Mode expansion

The ψ-Fourier expansion on the circle of radius $R_\psi$ is

$$
\Theta(Q,t,\psi) = \sum_{n \in \mathbb{Z}} \Theta_n(Q,t)\,e^{in\psi/R_\psi},
\qquad \Theta_n = \begin{pmatrix}\Theta_{L,n} \\ \Theta_{R,n}\end{pmatrix},
$$

where $\Theta_{L,n}$ and $\Theta_{R,n}$ are the left-handed and right-handed
two-component Weyl spinors at winding number $n$.

Substituting into $\mathcal{D}\Theta = 0$ and separating modes
(using $\partial_\psi \to in/R_\psi$), the block structure of $\mathcal{D}$
in the chiral representation gives the **coupled Weyl equations**:

$$
i\sigma^\mu \partial_\mu \Theta_{R,n} = \frac{in}{R_\psi}\,\Theta_{L,n}, \tag{A$_n$}
$$

$$
i\bar\sigma^\mu \partial_\mu \Theta_{L,n} = -\frac{in}{R_\psi}\,\Theta_{R,n}, \tag{B$_n$}
$$

where $\sigma^\mu = (I_2, \vec\sigma)$ and $\bar\sigma^\mu = (-I_2, \vec\sigma)$
in the mostly-plus Lorentzian convention.

**Note on signs.** The coupling constants in (A$_n$) and (B$_n$) have opposite
signs: $+in/R_\psi$ vs. $-in/R_\psi$. This is a direct consequence of
$\gamma^5\partial_\psi$ (not $i\gamma^5\partial_\psi$) in the Dirac operator.
Under $n \to -n$, equations (A$_n$) and (B$_n$) exchange roles with a sign
change, and the system maps to its own complex conjugate.

### 2.2 Effective mass squared

Substituting (A$_n$) into (B$_n$):

$$
i\bar\sigma^\mu\partial_\mu\cdot \frac{R_\psi}{in}\cdot i\sigma^\nu\partial_\nu \Theta_{R,n}
= -\frac{in}{R_\psi}\Theta_{R,n}.
$$

Using the Weyl identity $i\bar\sigma^\mu\partial_\mu \cdot i\sigma^\nu\partial_\nu = -\Box$:

$$
-\Box\,\Theta_{R,n} = -\frac{(in)(-in)}{R_\psi^2}\,\Theta_{R,n} = \frac{n^2}{R_\psi^2}\,\Theta_{R,n},
$$

$$
\Bigl(\Box + \frac{n^2}{R_\psi^2}\Bigr)\Theta_{R,n} = 0.
$$

**Result:** effective mass squared $m_n^2 = n^2/R_\psi^2 \geq 0$, **symmetric** in $n$.
This is consistent with `verify_psi_branch_selection.py` check V8 and with
`experiments/research_tracks/three_generations/st3_complex_time_generations.tex`.

<!-- BILINGUAL-UNIT: psi-fock.sec3 -->
## 3. Hamiltonian construction and chirality-sector structure

<!-- BILINGUAL-UNIT: psi-fock.hamiltonian-matrix -->
### 3.1 ψ-sector Hamiltonian matrix in the chirality basis

From the Lagrangian $\mathcal{L} = \bar\Theta(\mathcal{D})\Theta$, the
contribution of the $\gamma^5\partial_\psi$ term to the Hamiltonian density
for mode $n$ is

$$
H_\psi^{(n)} = \frac{n}{R_\psi}\,\gamma^0\gamma^5.
$$

In the chiral representation:

$$
\gamma^0\gamma^5 = \begin{pmatrix}0 & I_2 \\ I_2 & 0\end{pmatrix}
\begin{pmatrix}-I_2 & 0 \\ 0 & I_2\end{pmatrix}
= \begin{pmatrix}0 & I_2 \\ -I_2 & 0\end{pmatrix}.
$$

**Observation (verified: A8).** In the chirality basis $(\Theta_L, \Theta_R)$,
the matrix $\gamma^0\gamma^5$ is **purely off-diagonal**: the diagonal
(chirality-preserving) $L$–$L$ and $R$–$R$ blocks are both zero.
Thus $H_\psi^{(n)}$ couples $\Theta_L \leftrightarrow \Theta_R$ with equal
strength; it does **not** give different energies to the two chirality sectors.

**Observation (verified: A1).** The eigenvalues of $\gamma^0\gamma^5$ are $\pm i$
(purely imaginary), each with multiplicity 2. Consequently $H_\psi^{(n)}$
alone is not Hermitian; the 4D spatial kinetic term is required for a
well-defined Hermitian Hamiltonian. The combined Hamiltonian has real
eigenvalues $\pm|n|/R_\psi$ (see §3.2).

**Observation (verified: A4, B2).** Under $n \to -n$, the off-diagonal coupling
block satisfies

$$
\text{block}(+n) + \text{block}(-n) = 0.
$$

This is a **structural sign flip**, not a selection: the mixing angle in the
$L$–$R$ plane rotates by $\pi$ when the winding number changes sign.

<!-- BILINGUAL-UNIT: psi-fock.eigenvalues -->
### 3.2 Energy eigenvalues

At zero 4D spatial momentum (rest frame), the mode-$n$ constraint matrix is

$$
M_n(E) = E\,\gamma^0 + i\,\frac{n}{R_\psi}\,\gamma^5.
$$

**Proposition (verified: A2, A3).** $\det M_n(E) = \bigl(E^2 - n^2/R_\psi^2\bigr)^2$.
Hence the energy eigenvalues are $E = \pm|n|/R_\psi$, each with multiplicity 2,
for **all** $n$. The spectrum is identical for $n$ and $-n$.

*Proof sketch.* Direct symbolic computation; see `verify_psi_fock_chirality_selection.py`
check A2 and A3. $\square$

**Scope of claim.** This is a rest-frame, zero-gauge-field, flat-spacetime result.
It does not extend automatically to the full curved or gauge-coupled theory.

<!-- BILINGUAL-UNIT: psi-fock.sec4 -->
## 4. Second quantization and normal ordering

<!-- BILINGUAL-UNIT: psi-fock.normal-ordering -->
### 4.1 Fock space and fermion normal ordering

Expand $\Theta_n$ in terms of positive- and negative-frequency solutions of
$({\Box + n^2/R_\psi^2})\Theta = 0$. For a Dirac-type field, canonical
quantization imposes **anticommutation relations**:

$$
\{a_{n,s},\, a^\dagger_{n',s'}\} = \delta_{nn'}\delta_{ss'}, \quad
\{a_{n,s},\, a_{n',s'}\} = 0,
$$

where $s$ labels the positive-energy solutions (which mix $\Theta_L$ and $\Theta_R$;
see §3.2).

The formal Hamiltonian before normal ordering contains negative-energy modes.
**Normal ordering** (Wick ordering, Dirac-sea prescription for fermions) replaces:

$$
H_{\rm naive} = \sum_{n,s} E_{n,s}\, a^\dagger_{n,s} a_{n,s}
\quad\longrightarrow\quad
H_{\rm NO} = \sum_{n,s} |E_{n,s}|\, a^\dagger_{n,s} a_{n,s}
\;+\;\text{(antiparticle terms)},
$$

where negative-energy creation operators are reinterpreted as positive-energy
antiparticle annihilation operators via $a_{n,s} \leftrightarrow b^\dagger_{n,s}$.

**Result (verified: A7, B3).**

$$
H_{\rm NO} = \sum_{n \in \mathbb{Z},\, s} \frac{|n|}{R_\psi}\,
\bigl(a^\dagger_{n,s} a_{n,s} + b^\dagger_{n,s} b_{n,s}\bigr) + \text{const},
$$

where $a^\dagger_{n,s}$ creates a particle of type $(n,s)$ and $b^\dagger_{n,s}$
creates an antiparticle. The coefficient $|n|/R_\psi \geq 0$ is the same for
all $n$ (both positive and negative), and for all solutions $s$ (regardless
of their $L$–$R$ composition). The normal-ordered Hamiltonian is **bounded below
by zero**.

### 4.2 No free-theory chirality selection

**Main negative result.** The normal-ordered free-theory ψ-Fock Hamiltonian is

1. **Symmetric under $n \to -n$:** the coefficient $|n|/R_\psi$ is unchanged.
2. **Not chirality-selective:** the energy eigenstates at mode $n$ are
   superpositions of $\Theta_L$ and $\Theta_R$ (the mixing angle changes sign
   under $n \to -n$, but the spectrum does not). No selection of
   (n>0, left-handed) + (n<0, right-handed) emerges.
3. **Bounded below for all $(n, \text{chirality})$ combinations:** normal
   ordering gives a non-negative spectrum for every winding number and every
   choice of creation/annihilation basis.

**Warning (analogous to the warning in the task statement about
`step4_fpe_equivalence.tex`).** Every claim about commutators, normal ordering,
and the cyclic structure of the Hilbert space must be stated explicitly.
The result above relies on:
- Anticommutation of $a_{n,s}$ with $a^\dagger_{n,s}$: explicitly stated.
- Reinterpretation of negative-energy modes: standard Dirac procedure, explicitly invoked.
- The off-diagonal form of $\gamma^0\gamma^5$: verified symbolically in check A8.

No step is justified by "it follows from normal ordering" without the explicit
algebraic step.

<!-- BILINGUAL-UNIT: psi-fock.sec5 -->
## 5. What does change under $n \to -n$: the mixing-angle sign flip

<!-- BILINGUAL-UNIT: psi-fock.sign-flip-detail -->
### 5.1 L–R mixing angle

Although the spectrum is symmetric, the **structure of the energy eigenstates**
changes under $n \to -n$. The positive-energy eigenstate of $M_n(E)$ at $E = +|n|/R_\psi$
involves the combination $\Theta_L - i\,\mathrm{sign}(n)\,\Theta_R$ (schematically).
Explicitly (at rest, $n > 0$):

$$
u_+ \;\propto\; \Theta_L - i\Theta_R \quad (n > 0),
\qquad
u_+ \;\propto\; \Theta_L + i\Theta_R \quad (n < 0).
$$

These are **not** chirality eigenstates (neither is a $\gamma^5$-eigenstate).
They differ by a phase rotation in the $L$–$R$ plane ($e^{\pm i\pi/2}$).

### 5.2 Structural observation

The sign flip of the L–R coupling (verified: A4, B2) means that if one defines
a projection onto the "left-dominant" energy eigenstate, this projection selects
$n>0$ modes. However:
- This projection is **not a consequence of the free Hamiltonian being bounded below**;
  it is an additional definition.
- In the presence of gauge coupling ($SU(2)_L$ acting on $\Theta_L$ only), the
  gauge-invariant physical sector could in principle exhibit a correlated structure.
  But this requires the gauge coupling, not the free-theory Hamiltonian.
- The identification of "left-dominant" modes with "matter" is an additional
  physical input; see §7.

<!-- BILINGUAL-UNIT: psi-fock.sec6 -->
## 6. Verdict

<!-- BILINGUAL-UNIT: psi-fock.main-result -->
### 6.1 Mathematical verdict: PARTIAL/CONDITIONAL

The attempt to derive chirality–winding correlation from Hamiltonian boundedness
below yields the following three-part result:

**NO-GO (free theory):** Normal ordering of the free ψ-Fock Hamiltonian does NOT
dynamically select the pairing (n>0, left-handed) + (n<0, right-handed). The
normal-ordered Hamiltonian is bounded below for ALL (n, chirality) combinations,
with coefficient $|n|/R_\psi$ independent of $\mathrm{sign}(n)$ and of chirality.
Second quantization alone cannot replace the structural assumption in
`canonical/chirality/gap_c1_closure.tex`.

**STRUCTURAL OBSERVATION (partial):** The UBT Dirac operator $\mathcal{D} = i\gamma^\mu\nabla_\mu + \gamma^5\partial_\psi$ produces energy eigenstates whose L–R mixing angle flips sign under $n \to -n$. This is a genuine structural difference between positive and negative winding numbers, but it is a kinematic property of the mode functions, not a dynamical selection from the Hamiltonian spectrum.

**CONDITIONAL:** If one adds a **NEW AXIOM CANDIDATE** (see §7) identifying a
preferred vacuum sector, and if the SU(2)$_L$ gauge coupling is P$_\psi$-odd
(as argued in `canonical/chirality/gap_c1_closure.tex`, conditional on T2\_GAUGE),
then the combination of the vacuum axiom, the gauge coupling, and the mode-function
structure gives a consistent picture of (n>0, left-handed) as matter and
(n<0, right-handed) as antimatter. But this combination is conditional, not derived.

**Gap C1 status is unchanged.** This document does not close Gap C1. It provides a
more precise characterisation of what second quantization does and does not contribute
to the problem. Gap C1 remains CLOSED CONDITIONALLY on T2\_GAUGE, as stated in
`canonical/chirality/gap_c1_closure.tex`.

<!-- BILINGUAL-UNIT: psi-fock.sec7 -->
## 7. New axiom candidates

<!-- BILINGUAL-UNIT: psi-fock.axiom-candidates -->
The following assumptions were required to make the selection argument work. Each
is explicitly labelled as a NEW AXIOM CANDIDATE and is not a consequence of the
free kinetic action:

**NEW AXIOM CANDIDATE A (vacuum selection):**
> The physical Fock vacuum is the vacuum in which the energy eigenstates of the
> positive-energy sector for $n>0$ are the "matter sector" and those for $n<0$
> are the "antimatter sector." This is not derivable from $H_\psi^{(n)}$ being
> bounded below; it is an additional cosmological or boundary condition.

**NEW AXIOM CANDIDATE B (L-dominant projection):**
> The physical particle states are those whose energy eigenstate has dominant
> $\Theta_L$ component (i.e., the $u_+ \propto \Theta_L - i\Theta_R$ states for
> $n>0$). This projects onto the left-chirality-correlated modes but requires
> defining "dominance" as an additional criterion.

These candidates are distinct from, and independent of, T2\_GAUGE (the condition
that $SU(2)_L$ = left action on Θ). They would need to be derived from the full
UBT action $S[\Theta]$ or established as additional fundamental postulates.

<!-- BILINGUAL-UNIT: psi-fock.sec8 -->
## 8. Verification

<!-- BILINGUAL-UNIT: psi-fock.verification -->
### 8.1 Script and results

Run

```bash
python tools/verify_psi_fock_chirality_selection.py
```

| Check | Description | Channel | Status |
|---|---|---|---|
| A1 | $\mathrm{eigenvals}(\gamma^0\gamma^5) = \{\pm i\}$ | SymPy | PASS |
| A2 | $\det(E\gamma^0 + i(n/R_\psi)\gamma^5) = (E^2 - n^2/R_\psi^2)^2$ | SymPy | PASS |
| A3 | Spectrum identical for $n$ and $-n$ | SymPy | PASS |
| A4 | Off-diagonal L–R coupling flips sign under $n \to -n$ | SymPy | PASS |
| A5 | Weyl equations give $m^2 = n^2/R_\psi^2$ | SymPy | PASS |
| A6 | $\{\gamma^0, \gamma^5\} = 0$ | SymPy | PASS |
| A7 | Normal-ordering coefficient $= |n|/R_\psi \geq 0$ | SymPy | PASS |
| A8 | Diagonal blocks of $(n/R_\psi)\gamma^0\gamma^5$ are zero | SymPy | PASS |
| B1 | Spectrum symmetric under $n \to -n$ (numerical) | NumPy | PASS |
| B2 | L–R coupling sign flip under $n \to -n$ (numerical) | NumPy | PASS |
| B3 | Normal-ordered positivity for all tested modes | NumPy | PASS |

All checks concern the 4×4 matrix algebra in the chiral representation, at rest
frame, in flat spacetime without gauge fields. They do NOT verify:
- curved-spacetime or Θ-dependent operators;
- infinite-dimensional Fock-space well-posedness;
- action-level derivation of gauge couplings or the UBT–SM dictionary.

<!-- BILINGUAL-UNIT: psi-fock.sec9 -->
## 9. Lean status

<!-- BILINGUAL-UNIT: psi-fock.lean-status -->
**LEAN-PENDING.** No compiled Lean proof exists for any claim in this document.
The 4×4 algebraic identities are in principle Lean-checkable (the chiral
representation is concrete and all operations are linear algebra over ℂ).
The infinite-dimensional Fock-space statement (Theorem in §4) requires functional-analysis
prerequisites beyond the current Lean proof queue. Reason for absence: insufficient
formalization infrastructure.

<!-- BILINGUAL-UNIT: psi-fock.sec10 -->
## 10. Relation to gap G3 and Gap C1

<!-- BILINGUAL-UNIT: psi-fock.gap-update -->
The gap table in `psi_branch_selection.en.md` lists:

> G3-DYN: Dynamic use of $\Gamma_*D_\psi$, its normalization, left/right action and action origin — OPEN

The present document is a partial exploration of G3-DYN. Specifically:

- The free-Hamiltonian route (second quantization + normal ordering alone) is
  **CLOSED AS NO-GO** for the specific claim that it selects (n>0,L)+(n<0,R).
- A residual structural observation (L–R mixing angle sign flip) is recorded but
  does not close G3-DYN.
- G3-DYN remains OPEN pending an action-level derivation.

Gap C1 in the canonical chirality sector (`canonical/chirality/gap_c1_closure.tex`)
remains CLOSED CONDITIONALLY on T2\_GAUGE. The present document adds a note that
the Fock-space route does not provide an independent closure of Gap C1; the
T2\_GAUGE conditional is not removed or weakened.

This document is cross-referenced from `psi_branch_selection.en.md`.

<!-- BILINGUAL-UNIT: psi-fock.sec11 -->
## 11. Summary

<!-- BILINGUAL-UNIT: psi-fock.summary -->
| Item | Status |
|---|---|
| Free ψ-Fock Hamiltonian bounded below | YES, for ALL (n, chirality); no selection |
| $n \to -n$ symmetry of spectrum | EXACT (verified A2, A3, B1) |
| L–R coupling sign flip under $n \to -n$ | STRUCTURAL OBSERVATION (verified A4, B2) |
| Dynamic selection of (n>0, L)+(n<0, R) from free $H$ | NO-GO (free theory) |
| Conditional selection with NEW AXIOM CANDIDATE A+B and T2\_GAUGE | CONDITIONAL |
| Gap C1 changed | NO — remains CLOSED CONDITIONALLY on T2\_GAUGE |
| G3-DYN changed | NARROWED: free-Hamiltonian sub-route is NO-GO; full G3-DYN OPEN |
| Canonical files changed | NONE |
| LEAN status | LEAN-PENDING throughout |

**Mathematical verdict: PARTIAL/CONDITIONAL.**
The free ψ-Fock Hamiltonian does not dynamically select (n>0, left-handed) + (n<0, right-handed).
The selection is conditional on NEW AXIOM CANDIDATES A and B together with T2\_GAUGE.
A structural L–R mixing sign flip under $n \to -n$ is established.
