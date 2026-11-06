<!-- BILINGUAL-UNIT: projective-winding.scope -->
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

# Information-first UBT: projective Z2 winding from shared observers, with no Fisher energy floor

**2026-11-05 · C_working · conditional projective-identifiability and no-Fisher-floor theorems.** English is the translation source. This note builds on the *merged* full-Theta observer-readout theorem while keeping physical UBT action selection and causal instruments OPEN.

<!-- BILINGUAL-UNIT: projective-winding.premise -->
## Full-Theta data, three clocks, and the domain [PROVED conditionally]

Use the FULL complex biquaternion Theta, not only its determinant or a real projection. Adopt the already merged three-clock result: the co-calibrated local qubit readouts are jointly injective on invertible matrices modulo nonzero complex scalars. The clocks are fixed, smooth positive Hermitian protocol data; completeness of tomographic measurements and the entire smooth psi-fiber history are **assumptions**, not derived UBT instruments. Keep the original tetrad and independent/composite connection treatment locked.

\[
\Theta:S^1_\psi\to GL_2(\mathbb C),\quad
N_0=I_2,\quad N_1=\operatorname{diag}(2,1/2),\quad
N_2=\begin{pmatrix}2&1\\1&1\end{pmatrix},
\]
\[
B_j=N_j^{-1/2},\quad
\rho_j[\Theta]=\frac{B_j\Theta N_j^{-1}\Theta^\dagger B_j}
{\operatorname{tr}(B_j\Theta N_j^{-1}\Theta^\dagger B_j)},
\quad \det \Theta(\psi)\ne0.
\]

<!-- BILINGUAL-UNIT: projective-winding.parity -->
## Exact parity-invariance theorem for joint observer histories [PROVED]

Suppose two smooth, periodic invertible full-Theta histories give the SAME three complete density records for every psi with the SAME calibrated clocks and protocols. The pre-existing projective tomography theorem implies pointwise Phi=c Theta. Since the matrices are invertible, c is unique and itself smooth, nowhere zero and periodic. The determinant relation proves an even integer shift of winding. Thus its parity is a readout invariant. This does not claim that an arbitrary actual physical detector has continuous access to the compact psi coordinate.

\[
\bigl(\forall \psi,\ \forall j\in\{0,1,2\}:
\rho_j[\Phi](\psi)=\rho_j[\Theta](\psi)\bigr)
\Longrightarrow \Phi(\psi)=c(\psi)\Theta(\psi),\
c:S^1\to\mathbb C^\times,
\]
\[
\nu(\det\Phi)-\nu(\det\Theta)
=\nu(c^2)=2\nu(c)\in2\mathbb Z,\qquad
\boxed{\,\nu(\det\Theta)\bmod2\ \text{is identifiable by ideal joint histories.}\,}
\]

<!-- BILINGUAL-UNIT: projective-winding.topology -->
## Projective fundamental group and the lift sign [PROVED]

The scalar inclusion in the exact quotient by complex rescalings induces multiplication by two on the fundamental group, because det(cI)=c squared. Consequently projective matrix loops have a binary homotopy class. It is the parity established above, not the full integer determinant winding. The explicitly normalized special-linear lift illustrates the sign monodromy. This group topology is standard mathematics, not a novel claim of physical spin, particle generations, string winding or a stable UBT excitation.

\[
1\longrightarrow\mathbb C^\times
\overset{c\mapsto cI_2}{\longrightarrow}GL_2(\mathbb C)
\longrightarrow PGL_2(\mathbb C)\longrightarrow1,
\]
\[
\pi_1(\mathbb C^\times)=\mathbb Z
\overset{\times2}{\longrightarrow}
\pi_1(GL_2(\mathbb C))=\mathbb Z
\longrightarrow\boxed{\pi_1(PGL_2(\mathbb C))=\mathbb Z_2}
\longrightarrow0,
\]
\[
\Theta_n(\theta)=\operatorname{diag}(e^{in\theta},1),\quad
\widehat\Theta_n(\theta)=
\operatorname{diag}(e^{in\theta/2},e^{-in\theta/2}),\quad
\widehat\Theta_n(2\pi)=(-1)^n\widehat\Theta_n(0).
\]

<!-- BILINGUAL-UNIT: projective-winding.observable -->
## A single clock can miss the winding that three clocks resolve [PROVED]

For nonzero amplitude r and integer n use the indicated full invertible matrix on the fiber. The diagonal clocks N0 and N1 give psi-independent densities and cannot distinguish any n. The nondiagonal clock N2 has an explicit sigma-y expectation value which depends on the winding phase. Three complete calibrated clock records can therefore reconstruct the projective loop and hence its parity, although a lone N2 binary observable cannot certify the full topological class from finite samples.

\[
\Theta_{r,n}(\psi)=\operatorname{diag}(r e^{in\psi/R},1),
\quad 0<r,\quad n\in\mathbb Z,\quad 0\le\psi\le2\pi R,
\]
\[
\partial_\psi\rho_{N_0}=\partial_\psi\rho_{N_1}=0,\quad
\operatorname{tr}(\sigma_y\rho_{N_2})
=\frac{2r\sin(n\psi/R)}
{4+r^2+2r\cos(n\psi/R)}.
\]

<!-- BILINGUAL-UNIT: projective-winding.fisher -->
## Positive Fisher sensitivity has no uniform topological energy floor [PROVED]

Choose a fixed two-outcome unsharp sigma-y measurement with strength kappa. Its classical Fisher information is nonnegative and, at the starting phase, exactly the displayed nonzero function for n nonzero and r positive. Yet it goes to zero with r. A uniform inequality for amplitudes at most one half bounds the entire fiber integral. The proof uses a denominator at least three, an absolute Bloch expectation at most two r divided by three, and a phase derivative at most eight r divided by nine. These elementary bounds are valid without inserting any microscopic energy functional.

\[
E_\pm=\tfrac12(I_2\pm\kappa\sigma_y),\quad0<\kappa\le1,\qquad
p_\pm=\tfrac12(1\pm\kappa b_y),\quad
F_\psi=\frac{\kappa^2(\partial_\psi b_y)^2}
{1-\kappa^2 b_y^2},\quad b_y=\operatorname{tr}(\sigma_y\rho_{N_2}),
\]
\[
F_\psi(0)=\frac{\kappa^2n^2}{R^2}
\left(\frac{2r}{4+2r+r^2}\right)^2
\xrightarrow{r\to0^+}0,
\]
\[
0<r\le\tfrac12\Longrightarrow
F_\psi(\psi)\le\frac89\frac{\kappa^2n^2r^2}{R^2},\quad
\int_0^{2\pi R}F_\psi\,d\psi
\le\frac{16\pi}{9R}\kappa^2n^2r^2\xrightarrow{r\to0^+}0.
\]

<!-- BILINGUAL-UNIT: projective-winding.complete -->
## The no-floor result persists for finite complete multi-clock readouts [PROVED]

To retain complete local information and strictly positive outcome probabilities, replace the binary effect by the six-outcome unsharp Pauli protocol for each of the three clocks. For fixed positive clocks and kappa below one, the probabilities have a uniform positive lower bound. As r goes to zero, all the corresponding density derivatives with respect to psi are uniformly of order r times n/R. Thus the whole joint Fisher functional goes to zero quadratically, although for every positive r the loop remains invertible and carries the same nontrivial projective parity when n is odd. At r equal to zero the local density is well defined but the determinant vanishes and winding ceases to be defined. No uniform spectral gap, ghost freedom or physical energy bound has been derived.

\[
E_{a,\pm}=\tfrac16(I_2\pm\kappa\sigma_a),\quad
a\in\{x,y,z\},\quad0<\kappa<1,\quad
\sum_{a,\pm}E_{a,\pm}=I_2,\quad
p_{j,a,\pm}\ge(1-\kappa)/6>0,
\]
\[
\partial_\psi\rho_{N_j}[\Theta_{r,n}]
=O(r|n|/R)\quad(r\to0^+),\qquad
\mathcal J_{\rm joint}(r):=
\int_0^{2\pi R}\sum_{j,a,\pm}
\frac{(\partial_\psi p_{j,a,\pm})^2}{p_{j,a,\pm}}\,d\psi
=O(r^2n^2/R)\to0.
\]

<!-- BILINGUAL-UNIT: projective-winding.samples -->
## Finite samples cannot certify the parity [PROVED witness]

Full smooth calibrated access was essential. Two distinct smooth invertible histories can agree at each chosen sample yet have opposite parity, because their unobserved interpolation is unconstrained. For the exact sample points below the nontrivial loop has the same complete measured matrix values as the constant loop. No finite-sample topological inference is justified without a validated regularity, bandwidth or derivative bound.

\[
\phi(\theta)=\theta+\tfrac\pi2(1-\cos\theta),\quad
\Theta_{\rm hidden}(\theta)=
\operatorname{diag}(e^{i\phi(\theta)},1),\quad
\nu(\det\Theta_{\rm hidden})=1,
\]
\[
\Theta_{\rm hidden}(0)=
\Theta_{\rm hidden}(\pi)=
\Theta_{\rm hidden}(2\pi)=I_2
=\Theta_{\rm constant}(\theta).
\]

<!-- BILINGUAL-UNIT: projective-winding.limits -->
## Physical closure requirements [OPEN]

This is a theorem about a **chosen local observer protocol on unconstrained invertible full matrices**, not about selected on-shell UBT configurations. The scalar phase multiplication used in the classification need not preserve the locked sharp tetrad, and the merged observer density does not automatically descend to the gravity-only representative quotient (the independent counterexample remains in draft PR #832). No physical observer coupling to psi, information-current equation, unique Hamiltonian, stability of winding or global spin interpretation is obtained. The relevant next gate is to construct a physical causally accessible calibration/information functional on the actual reduced UBT phase space and test whether its projective parity survives the constraints and yields a derived *positive* energy barrier. Information positivity alone cannot do so.

<!-- BILINGUAL-UNIT: projective-winding.checks -->
## Verification and reuse

Twelve focused tests, including exact determinant and monodromy identities, the explicit off-diagonal clock response, the strict six-effect POVM, vanishing phase Fisher metric and numerical full-protocol scaling, passed locally. These tests certify only finite matrix algebra and explicit witnesses; the topological exact-sequence argument is supplied analytically, not formalized in Lean. Independent bilingual semantic review and GitHub CI are separate gates. Reused: the merged observer-clock tomography at research_tracks/information_first/THETA_OBSERVER_RELATIVE_INFORMATION_CHANNEL_2026_11.en.md, the open information-gravity-quotient witness in PR #832, and the unmerged Fisher/QFI nonselection branch PR #828. No priority claim for standard topology and no fundamental UBT action selection.
