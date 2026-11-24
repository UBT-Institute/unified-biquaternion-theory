<!-- BILINGUAL-UNIT: rh-theta-harmonic-tt-transfer-2026-11-24 -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
UBT-AI-PROVENANCE-END -->
# RH automorphic theta lifting versus a genuine graviton: exact selection tests

**24 November 2026 — C_working, exact conditional L0 algebra; physical action OPEN.**

## The RH correspondence is not a Fourier field redefinition

The 2026 Alpöge/Claude RH argument chains automorphic **theta lifts between different unitary groups** to amplify arithmetic multiplicity. Its oscillator/Weil machinery does not supply a map from physical \(\Theta\in M_2(\mathbb C)\) to UBT tetrads, a torsion law, or time evolution. The formal RH result was independently kernel-checked (https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/), but the interpretation of its theta lift as UBT dynamics would be a wholly separate theorem.

An invertible change of basis cannot add modes or change Hamiltonian signs. A noninvertible representation lift might select composite sectors, so the invertible no-go cannot dismiss it. Yet an actual linear intertwiner for the **same physical spatial little group** cannot turn input helicities \(0,\pm1\) into \(\pm2\) without a new tensorial kernel or composite target sector. The number-theoretic unitary groups cannot be identified with the physical \(SO(3)\) without proof.

## The isotropic harmonic/heat kernel has zero TT image

For \(a>0\), consider the symmetric traceless derivative of an isotropic scalar Gaussian:

\[
K_{ij}(k)=
\left(\partial_{k_i}\partial_{k_j}-\frac{\delta_{ij}}3\Delta_k\right)e^{-a|k|^2}
=4a^2e^{-a|k|^2}\left(k_ik_j-\frac{\delta_{ij}}3|k|^2\right).
\tag{1}
\]
\[
P_{ij}=\delta_{ij}-\hat k_i\hat k_j,\qquad
\Pi_{ij}{}^{lm}=\frac12(P_i{}^lP_j{}^m+P_i{}^mP_j{}^l)-\frac12P_{ij}P^{lm},
\qquad \boxed{\Pi_{ij}{}^{lm}K_{lm}(k)=0.}\tag{2}
\]
\[
Q_+=\frac{x^2-y^2}{2},\qquad Q_\times=xy,\qquad
L_z=x\partial_y-y\partial_x,\qquad
\boxed{L_zQ_+=-2Q_\times,\quad L_zQ_\times=2Q_+.}\tag{3}
\]
\[
H_{\rm osc}=-\frac12\Delta+\frac12r^2,\qquad
\Phi_0=e^{-r^2/2},\qquad \Phi_{+,\times}=Q_{+,\times}\Phi_0,\qquad
\boxed{H_{\rm osc}\Phi_0=\frac32\Phi_0,\quad H_{\rm osc}\Phi_{+,\times}=\frac72\Phi_{+,\times}.}\tag{4}
\]
\[
T_{ij}(s)=\sum_{n\in\mathbb Z^3}
\left(n_in_j-\frac{\delta_{ij}}3|n|^2\right)e^{-\pi s|n|^2}=0,\qquad s>0.\tag{5}
\]

It transforms as a rank-two tensor but (2) shows it is longitudinal/scalar at its own momentum, with **zero transverse-traceless graviton projection**. This holds for any rotational scalar function of \(|k|^2\), not only the Gaussian. Tensor rank two is not helicity two.

## Oscillator representation does contain a two-quantum weight-two sector

The Gaussian-oscillator toy (3) has proper SO(2) weight \(2\); the exact oscillator identity (4) gives energy \(7/2\) instead of vacuum \(3/2\), a gap \(2\). This is an **analogy** to the polynomial/Fock sector of the Weil representation, NOT the arithmetic automorphic theta lift itself or a massless spin-two bound state.

The additional lattice control (5) is an exact identity for the cubic lattice: sign flips remove off-diagonals, permutations equalize diagonals, and tracelessness forces zero. Any shifted/anistropic lattice construction introduces directional input and must separately pass isotropy and geometry-selection checks.

## What would count as genuine transfer

A UBT application would have to exhibit the actual source/target physical representations, an explicit kernel compatible with the *two-sided* covariant \(\Theta\) derivative and central-sharp metric, a well-defined gauge/constraint quotient, and an interacting **isolated massless TT pole with positive residue** plus universal coupling. A two-particle oscillator spin-two representation alone does not meet these conditions. Check Weinberg–Witten assumptions before interpreting composite massless helicity \(2\) as a graviton. No microscopic UBT Hamiltonian is inferred. Cross-reference drafts PR #909 and PR #911.

**Tests:** `research_tracks/action_selection/tests/test_rh_theta_harmonic_tt_transfer_2026_11_24.py` checks (1)-(4) exactly and a finite version of the cubic symmetry in (5); the infinite sum and all-\(k\) identities follow analytically. Not a full field-theory test. LEAN-PENDING; CI/review pending.
