<!-- BILINGUAL-UNIT: chiral-interaction.scope -->
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

# Chiral currents and winding: exact interaction audit

**Scope: FINITE ALGEBRA; PHYSICAL SELECTION OPEN.** This continues `psi_fock_quantization_chirality_link.en.md`. We audit the proposed route from its free Hamiltonian to the interaction argument in `canonical/chirality/gap_c1_closure.tex`. The calculation uses the declared Dirac-sector representation, without replacing the original biquaternionic Θ, its covariant tetrad, or its single-action requirement. No identification of internal quaternionic left multiplication with Lorentz chirality is derived here.

<!-- BILINGUAL-UNIT: chiral-interaction.projectors -->
## Projectors and the Dirac adjoint

Let the chirality matrix be a Hermitian involution anticommuting with every Dirac vector matrix. The adjoint of a projected spinor carries the opposite projector. This follows by moving the projector through the time matrix; conjugating a label without this step gives the wrong bilinear.

\[
C=\gamma^5,\quad C^\dagger=C,\quad C^2=I,\quad
C\gamma^\mu+\gamma^\mu C=0,\quad P_L=(I-C)/2,\quad P_R=(I+C)/2.
\]
\[
\bar\psi=\psi^\dagger\gamma^0,\quad
\overline{\psi_L}=\bar\psi P_R,\quad
\overline{\psi_R}=\bar\psi P_L,\quad
P_L\gamma^\mu=\gamma^\mu P_R.
\]

<!-- BILINGUAL-UNIT: chiral-interaction.zero -->
## The proposed opposite-chirality vector current vanishes

**Theorem.** For arbitrary spinors, the bilinear used as the charged current in the cited C1 note vanishes identically.

**Proof.** Anticommutation and the involution identity give the projector sandwich below. Multiplication by either external spinor preserves zero. An internal generator commuting with the Dirac projectors does not change this conclusion. Calling the zero expression odd does not establish a nonzero weak vertex or any selection mechanism.

\[
(I-C)\gamma^\mu(I-C)
=\gamma^\mu-(C\gamma^\mu+\gamma^\mu C)+C\gamma^\mu C=0,
\]
\[
P_L\gamma^\mu P_L=0,\qquad
\boxed{\bar\chi_R\gamma^\mu\psi_L=0}.
\]

<!-- BILINGUAL-UNIT: chiral-interaction.even -->
## The actual left vector current is even

**Theorem.** The nonzero left vector current is even under simultaneous internal chirality transformation of both spinors.

**Proof.** Conjugation changes the signs of both Dirac matrices in its Hermitian-space kernel and preserves the projector. The signs therefore cancel. For the time component and a normalized left spinor, the current equals unity, so evenness is not a vacuous statement about zero. With an even gauge field and a commuting internal generator the vertex remains even. This is the internal transformation tested by the C1 argument; it is not a derivation that coordinate reflection equals internal chirality.

\[
J_L^\mu=\bar\chi_L\gamma^\mu\psi_L
=\bar\chi\gamma^\mu P_L\psi=\chi^\dagger K_L^\mu\psi,
\quad K_L^\mu=\gamma^0\gamma^\mu P_L,
\]
\[
C^\dagger K_L^\mu C=K_L^\mu,\qquad
\chi\mapsto C\chi,\ \psi\mapsto C\psi\quad\Longrightarrow\quad J_L^\mu\mapsto J_L^\mu.
\]
\[
K_L^0=P_L,\qquad\psi=(1,0,0,0)^T,\quad\chi=\psi,\quad J_L^0=1.
\]

<!-- BILINGUAL-UNIT: chiral-interaction.interaction -->
## Winding conjugacy survives chiral-diagonal interactions

**Theorem.** Add the same interaction to both winding signs, commuting with the chirality involution. The two resulting matrices remain conjugate. Hermiticity of the Hamiltonian and interaction, and unitarity of the involution, turn this into unitary spectral equivalence.

**Proof.** Expand the conjugation of the sum. Commutation and the involution identity preserve the interaction. The displayed eigenmatrix identity transports every column, including degenerate eigenspaces. Multiplication by the chirality matrix preserves each chiral norm separately. Thus winding reversal preserves the energies and chiral-weight possibilities.

This permits unequal left and right interactions, including a left-only one. Spatial kinetic matrices and minimally coupled chiral vector kernels commute with the chirality matrix when internal generators act on a separate internal index. Those finite algebraic premises are checked independently. An infinite differential operator additionally requires a common invariant domain and boundary conditions; those are not proved here.

\[
H_m=-im\gamma^0C,\quad CH_mC=H_{-m},\quad CV=VC,\quad
\boxed{C(H_m+V)C=H_{-m}+V}.
\]
\[
CAC=B,\quad AX=XD,\quad C^2=I\quad\Longrightarrow\quad
B(CX)=CAX=(CX)D.
\]
\[
V=\begin{pmatrix}V_L&0\\0&V_R\end{pmatrix},\quad
V_L^\dagger=V_L,\quad V_R^\dagger=V_R,\quad
[C,\gamma^0\gamma^\mu]=[C,\gamma^0\gamma^\mu P_L]=0.
\]

<!-- BILINGUAL-UNIT: chiral-interaction.example -->
## Explicit asymmetric example

A real diagonal interaction may change the chiral balance. It still cannot correlate that change with the sign of winding: the characteristic polynomial is even in the winding mass and conjugation preserves the separate component norms. This does not extend the earlier equal-weight theorem to interacting states; it proves equality of the available weights between the two winding signs.

\[
H_{m,a,b}=\begin{pmatrix}a&-im\\im&b\end{pmatrix},\quad a,b\in\mathbb R,\quad
\det(EI-H_{m,a,b})=(E-a)(E-b)-m^2.
\]
\[
(L,R)\mapsto(-L,R),\qquad\|-L\|^2=\|L\|^2,\qquad\|R\|^2=\|R\|^2.
\]

<!-- BILINGUAL-UNIT: chiral-interaction.reflection -->
## Reflection is not winding parity

The cited C1 note also uses an index-parity multiplier for coordinate reflection. These are different operations. Reflection reverses the Fourier index; the multiplier belongs to a half-period translation. A single positive-winding mode is neither reflection-even nor reflection-odd. The explicit coefficient counterexample is formalized in Lean. Identifying either operation with internal chirality requires a further intertwining map on a specified space; the sign of winding alone does not provide it.

\[
(\mathcal R f)(\psi)=f(-\psi),\quad (\mathcal R\widehat f)_n=\widehat f_{-n},\qquad
(\mathcal T f)(\psi)=f(\psi+\pi R_\psi),\quad(\mathcal T\widehat f)_n=(-1)^n\widehat f_n.
\]
\[
\widehat f_n=\delta_{n,1},\quad(\mathcal R\widehat f)_1=0,\quad
(\mathcal R\widehat f)_{-1}=1,\quad\mathcal R\widehat f\ne\pm\widehat f.
\]

<!-- BILINGUAL-UNIT: chiral-interaction.gap -->
## What remains to be derived

The recorded conditional closure in `canonical/chirality/gap_c1_closure.tex` cannot be used as a proved interaction premise: its proposed vector current is zero, its correct replacement is even under the stated internal transformation, and reflection is confused with index parity. This research audit flags the source; it does not silently rewrite the canonical registry. The parent chirality track must treat the physical derivation as unresolved.

A successful selector must derive a failure of the displayed winding covariance in the actual action, admissible domain, background or physical state selection, and establish the internal-gauge-to-Lorentz-chirality dictionary. Merely inserting a left projector, choosing a winding sign, or labeling a vacuum does not derive that choice. A winding-dependent or chirality-mixing term is outside the theorem, but is not automatically a successful mechanism. No such new term or boundary condition is postulated here.

<!-- BILINGUAL-UNIT: chiral-interaction.verification -->
## Verification

`formal/lean/UBT/Action/ChiralInteraction.lean` formalizes the general ring identities, normalized matrix projector sandwiches, current evenness, interaction conjugacy, eigenmatrix transport, and coefficient reflection counterexample. The exact CI/compiler/kernel/axiom evidence is in `reports/lean_chiral_interaction_2026_09_16.json`.

`tools/verify_chiral_current_interaction.py` independently checks all four vector matrices, a nonzero current, arbitrary Hermitian chiral-diagonal blocks, the spatial and left-current kernels, the asymmetric characteristic polynomial and the reflection example with SymPy. NumPy checks eigenbasis transport in `12` cases, including degeneracies. Its record is `reports/chiral_current_interaction_2026_09_16.json`; the test is `tests/test_chiral_current_interaction.py`.

**LEAN-PENDING:** infinite operator domains, Fourier function-space realization, full-action coupling selection and the representation dictionary. The displayed finite characteristic example and explicit nonzero-current witness are checked by CAS; the general Lean theorems prove the structural identities. No induced gravitational coupling or RH implication follows.
