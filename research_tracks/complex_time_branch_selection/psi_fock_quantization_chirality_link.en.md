<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

<!-- BILINGUAL-UNIT: psi-fock.header -->
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

# ψ-Fock chirality: corrected Hamiltonian and exact rest-state weights

**Status: PARTIAL/CONDITIONAL.** The finite algebra is separated from the unproved full-action and infinite-dimensional Fock-space claims. This revises the attempt merged in PR #651.

<!-- BILINGUAL-UNIT: psi-fock.scope -->
## 1. Scope and conventions

We test the declared free, flat, gauge-free Dirac-sector candidate from `canonical/chirality/step1_psi_parity.tex`. Its derivation from the unique biquaternionic action remains open. The matrices below are a representation of this candidate, not a replacement of the original Θ or its covariant tetrad.

The displayed matrices obey the mostly-minus convention. Combining them with a mostly-plus Weyl time matrix, as the previous version did, is inconsistent. This convention choice is local to this calculation.

\[
\gamma^0=\begin{pmatrix}0&I_2\\I_2&0\end{pmatrix},\quad
\gamma^5=\begin{pmatrix}-I_2&0\\0&I_2\end{pmatrix},\quad
\sigma^\mu=(I_2,\vec\sigma),\quad\bar\sigma^\mu=(I_2,-\vec\sigma),\quad
\eta=\operatorname{diag}(1,-1,-1,-1).
\]
\[
\mathcal D=i\gamma^\mu\partial_\mu+\gamma^5\partial_\psi,\qquad
R_\psi>0,\quad n\in\mathbb Z,\quad m=n/R_\psi.
\]

<!-- BILINGUAL-UNIT: psi-fock.mode-expansion -->
## 2. Modes and coupled equations

With the stated convention, the two Weyl equations imply the Klein–Gordon equation with nonnegative squared mass. The derivation does not divide by the winding number and includes the zero mode.

\[
\Theta=\sum_{n\in\mathbb Z}\begin{pmatrix}L_n\\R_n\end{pmatrix}e^{in\psi/R_\psi},\quad
i\sigma^\mu\partial_\mu R_n=imL_n,\quad
i\bar\sigma^\mu\partial_\mu L_n=-imR_n.
\]
\[
(i\bar\sigma^\mu\partial_\mu)(i\sigma^\nu\partial_\nu)=-\Box,\quad
(im)(-im)=m^2,\quad(\Box+m^2)L_n=(\Box+m^2)R_n=0.
\]

<!-- BILINGUAL-UNIT: psi-fock.hamiltonian-matrix -->
## 3. Derivation of the Hermitian Hamiltonian

At zero spatial momentum, substitute the time dependence into the declared equation and multiply by the time matrix. This derives the factor missing in the previous version. The Hamiltonian is already Hermitian at rest; no spatial term is needed to repair it. Taking absolute values of imaginary eigenvalues of the uncorrected matrix is not a physical energy calculation.

\[
\Theta_n(t)=u e^{-iEt},\quad(E\gamma^0+im\gamma^5)u=0
\quad\Longleftrightarrow\quad Eu=H_m u,
\]
\[
\boxed{H_m=-im\gamma^0\gamma^5=
\begin{pmatrix}0&-imI_2\\imI_2&0\end{pmatrix}},\quad
H_m^\dagger=H_m,\quad H_m^2=m^2 I_4.
\]
\[
(\gamma^0\gamma^5)^\dagger=-\gamma^0\gamma^5,\qquad
\operatorname{spec}(\gamma^0\gamma^5)=\{+i,-i\}.
\]

<!-- BILINGUAL-UNIT: psi-fock.eigenvalues -->
## 4. Exact spectrum and winding symmetry

For nonzero winding the real energies have multiplicity two each. At zero winding the rest Hamiltonian vanishes and its kernel has dimension four. Conjugation by the chirality matrix preserves both component norms and reverses the winding.

\[
\det(E\gamma^0+im\gamma^5)=\det(EI_4-H_m)=(E^2-m^2)^2,
\quad E=\pm|m|,\quad\gamma^5 H_m\gamma^5=H_{-m}.
\]

<!-- BILINGUAL-UNIT: psi-fock.sign-flip-detail -->
## 5. Equal chiral weights, not left dominance

**Theorem.** Every nonzero-energy rest eigenstate has equal left and right norms. For nonzero winding every nonzero rest eigenstate has nonzero energy.

**Proof.** The coupled eigenvalue equations give the following identities. Since the energy is real and nonzero, the equal real parts imply equal norms. At zero energy and nonzero winding the same equations force both components to vanish.

The sign of the winding changes a relative phase, not a probability imbalance. In particular, the previously proposed “left-dominant projection” cannot select these nonzero-winding rest eigenstates: they are exactly balanced. The zero-winding, zero-energy kernel can contain pure chiral states and is excluded from this conclusion.

\[
-imR=EL,\quad imL=ER,\quad
E\|L\|^2=\operatorname{Re}(-imL^\dagger R)
=\operatorname{Re}(imR^\dagger L)=E\|R\|^2.
\]
\[
E\ne0\ \Longrightarrow\ \boxed{\|L\|^2=\|R\|^2},\qquad
E=|m|,\ m\ne0\ \Longrightarrow\ R=i\operatorname{sign}(m)L.
\]

<!-- BILINGUAL-UNIT: psi-fock.normal-ordering -->
## 6. What finite fermion normal ordering proves

Assume fermionic canonical anticommutation relations. The single-mode identity below gives the actual particle–hole reordering, including the vacuum constant. For a finite collection of diagonal modes, subtracting the vacuum constant leaves a nonnegative energy for every occupation assignment. This does not construct an infinite-dimensional Fock space, its operator domain, or its vacuum renormalization. Positivity refers to the subtracted Hamiltonian, not an arbitrary additive constant.

\[
b=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
bb^\dagger+b^\dagger b=I_2,\quad
-\varepsilon bb^\dagger+\varepsilon I_2=\varepsilon b^\dagger b.
\]
\[
\varepsilon_k=|n_k|/R_\psi\ge0,\quad
H_{\mathrm{NO}}=\sum_{k\in F}\varepsilon_k(N_{a,k}+N_{b,k})\ge0,
\quad |F|<\infty,\quad N_{a,k},N_{b,k}\in\{0,1\}.
\]

<!-- BILINGUAL-UNIT: psi-fock.main-result -->
## 7. Selection verdict

The stated free rest-mode model is symmetric under winding reversal and all its nonzero-winding energy eigenstates have equal chiral weights. Finite fermion normal ordering retains nonnegative excitation energies for both winding signs; it does not select a winding–chirality correlation. Off-diagonal blocks alone would not have proved this conclusion; the equal-weight theorem and explicit symmetry do. No full-action no-go is asserted.

<!-- BILINGUAL-UNIT: psi-fock.axiom-candidates -->
## 8. Earlier axiom candidates

Candidate A assigned matter and antimatter labels by winding sign. This remains an additional interpretation and gives no chiral dominance. Candidate B required left-dominant energy eigenstates; it is incompatible with the nonzero-winding rest eigenstates just derived. Therefore the earlier claim that A+B together with T2_GAUGE already gives a consistent selection is withdrawn. An interacting derivation would have to specify its action, states and observables afresh. No new axiom is adopted.

<!-- BILINGUAL-UNIT: psi-fock.verification -->
## 9. Independent verification

`tools/verify_psi_fock_chirality_selection.py` checks the Weyl signature identity, the actual Hermitian matrix, its square, characteristic polynomial, winding conjugation, exact positive-energy eigenspaces, equal-weight identity and finite CAR reordering with SymPy. NumPy checks real eigenvalues and normalized eigenvectors for both winding signs and multiple positive radii. It rejects the old missing-factor matrix by an explicit Hermiticity check. No assertion is counted as verification merely because it repeats an assigned coefficient.

Run the script and `tests/test_psi_fock_chirality_selection.py`. The machine-readable record is `reports/psi_rest_hamiltonian_2026_09_16.json`.

<!-- BILINGUAL-UNIT: psi-fock.lean-status -->
## 10. Lean scope

`formal/lean/UBT/Action/PsiRestHamiltonian.lean` formalizes the individual chirality block, repeated for each spectator spin component: the derived factor, Hermiticity, square, characteristic polynomial, winding conjugation, equal chiral weights, triviality of zero-energy states at nonzero winding, and single-mode CAR reordering. Compiler, kernel and axiom-audit evidence is recorded separately in `reports/lean_psi_rest_hamiltonian_2026_09_16.json`.

**LEAN-PENDING:** the spacetime differential equations, infinite-dimensional Fock construction, and action-level UBT-to-Dirac bridge. The finite proofs do not discharge those premises.

<!-- BILINGUAL-UNIT: psi-fock.gap-update -->
## 11. Remaining physical gaps

The parent track is `psi_branch_selection.en.md`. G3-DYN remains OPEN. The source `canonical/chirality/gap_c1_closure.tex` records conditional closure on T2_GAUGE. The subsequent audit `chiral_current_interaction_audit.en.md` finds its current/parity argument invalid, so that recorded closure cannot be used as a proved premise. Physical chirality selection remains unresolved. The complete composite action, physical fluctuation measure, kinetic normalization and gravitational coefficient remain unresolved. The original biquaternionic field and covariant tetrad are unchanged; no canonical gap or author attestation is upgraded.
