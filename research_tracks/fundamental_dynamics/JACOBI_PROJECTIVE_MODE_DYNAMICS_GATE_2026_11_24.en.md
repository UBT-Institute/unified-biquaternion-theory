<!-- BILINGUAL-UNIT: jacobi-projective-mode-dynamics-2026-11-24 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Exact restricted Fourier/projective algebra, not a proof of UBT dynamics, physical symplectic reduction, or a graviton.
UBT-AI-PROVENANCE-END
-->
# Jacobi mode lift: exact projective rank and dynamical selection gate

**24 November 2026. C_working; algebraic L0 conditional; no finalized action.** The reference construction is canonical/extensions/theta_fft_diagonalization.tex and the reduced Jacobi model canonical/bridges/theta_complex_time_bridge.md. The bridge contains an **explicit override**: its dimensionless Jacobi modulus \(t+i\phi\) is **not identified** with physical UBT \(\tau=t+i\psi\) without a separate map. The field of locked Axiom A is a single biquaternion value, not an arbitrary independent multiplet of spin-2 matrices. This note applies to reduced complex scalar mode amplitudes and to SO(3)-scalar-labelled copies of the fundamental \(M_2(\mathbb C)\) representation, not to a independently justified tensor carrier.

## 1. Rank-one tensor does not introduce independent matrix modes

Let \(a\in\mathbb C^N\setminus\{0\}\) and \(\rho=aa^\dagger\). The exact differential is
\[
D\rho_a[\delta a]=\delta a\,a^\dagger+a\,\delta a^\dagger.
\]
For \(\rho\) **unnormalized**, its real kernel is \(\{i\lambda a:\lambda\in\mathbb R\}\). Proof: project the equation \(D\rho_a[\delta a]=0\) orthogonally to \(a\), obtaining \(\delta a=c a\), and then \(c+\bar c=0\). Therefore
\[
\boxed{\operatorname{rank}_{\mathbb R}D\rho_a=2N-1\quad(a\ne0).}\tag{1}
\]
For the normalized projector \(P=aa^\dagger/(a^\dagger a)\), both positive scaling and overall phase are unobservable:
\[
\boxed{\ker DP_a=\mathbb C a,\qquad
\operatorname{rank}_{\mathbb R}DP_a=2N-2.}\tag{2}
\]
Thus \(P\) lives on \(\mathbb{CP}^{N-1}\), a manifold of real dimension \(2N-2\). The unnormalized rank-one cone has dimension \(2N-1\) and **cannot** itself have a nondegenerate two-form (odd dimension); after fixing normalization its natural Fubini–Study form is symplectic. At \(a=0\) the first differential of \(\rho\) vanishes; (1) is stated only away from zero. An arbitrary mixed state requires extra mixing/data, not merely a relabelling of the same vector.

In the stated 2D-lifted scalar model, diagonal Gaussian weighting \(D_\phi=\operatorname{diag}(e^{-2\pi\phi n^2})\) yields \(\rho_\phi=(D_\phi a)(D_\phi a)^\dagger\). The nonzero weights preserve rank one for finite real \(\phi\); no new independent physical state variable is created.

## 2. Two-axis FFT is not necessarily a quantum-state basis change

The note uses a two-dimensional same-sign FFT. For a unitary DFT matrix \(F\), that transform is \(F\rho F^T\), whereas a valid density-matrix change of basis is \(F\rho F^\dagger\). Both preserve algebraic matrix rank, but only the latter automatically preserves Hermiticity, trace and positive semidefiniteness.

**Exact counterexample:** for \(N=3\), \(a=(0,1,0)^T\), \(\rho=aa^\dagger\) has trace \(1\). Let \(F_{jk}=e^{-2\pi i jk/3}/\sqrt3\). Then
\[
\boxed{\operatorname{rank}(F\rho F^T)=1,\quad
\operatorname{tr}(F\rho F^T)=0,\quad
F\rho F^T\ne(F\rho F^T)^\dagger,}\tag{3}
\]
while \(\operatorname{tr}(F\rho F^\dagger)=1\) and \(F\rho F^\dagger\) remains a positive rank-one projector. The original FFT is not wrong as a **signal transform**; it is wrong to call its general output a physical density state without an additional construction. A same-sign FFT cannot independently manufacture an unconstrained spin-2 carrier.

## 3. Symplectic state geometry exists, but no unique generator follows

For \(N=2\), a local coordinate \(z=a_1/a_0\) on \(\mathbb{CP}^1\) gives the Fubini–Study area form
\[
\Omega_{\mathrm{FS}}=\frac{i\,dz\wedge d\bar z}{(1+|z|^2)^2}.
\]
A phase evolution with Hermitian diagonal generator \(K\), \(a(t)=e^{-itK}a(0)\), induces \(z\mapsto e^{-it\Delta K}z\) and preserves \(\Omega_{\mathrm{FS}}\). A nonuniform Gaussian damping \(a(\phi)=e^{-\phi K}a(0)\) induces \(z\mapsto qz\), \(q=e^{-\phi\Delta K}\), and
\[
\left.\frac{\Phi_q^*\Omega_{\mathrm{FS}}}{\Omega_{\mathrm{FS}}}\right|_{z=0}=q^2.
\]
Unless \(q=1\), **heat damping is not Hamiltonian/symplectic evolution** on this fixed projective state space. This is a local exact non-preservation result, not a restriction on imaginary-time algorithms or extended dissipative systems.

Even with positive spectra and the same projective symplectic geometry, the two generators
\[
K_1=\operatorname{diag}(0,1,4),\quad
K_2=\operatorname{diag}(0,1,16)
\]
produce distinct observable projectors from \(a_0=(1,1,1)^T/\sqrt3\) at \(t=\pi/8\), despite both yielding norm-preserving unitary flow. Consequently \(\Omega_{\mathrm{FS}}\), positivity, phase symmetry and the mode representation do **not** select the physical dispersion law \(K\).

The chosen Jacobi kernel \(\exp(i\pi n^2 t-\pi n^2\phi)\) indeed satisfies the Cauchy–Riemann equation \(\partial_\phi a_n=i\partial_t a_n\). But replacing \(\pi n^2\) by any real \(\omega_n\) satisfies the same relation; choosing the Jacobi heat equation selects quadratic dispersion **as an assumption of this reduced model**, not as a corollary of locked UBT dynamics. Moreover its displayed phase sign must be reconciled with conventional \(e^{-itH}\) and positive Hamiltonian conventions if \(t\) were ever identified with physical time.

## 4. Impact on helicity and RH transfers

If each Fourier/Jacobi coefficient is simply a scalar-labelled copy of \(\Theta_n\in M_2(\mathbb C)\), spatial \(SO(2)\) little-group weights remain \(0,\pm1\) in every copy. An equivariant *linear* map from an arbitrary finite/direct-sum collection of these scalar-labelled modes to TT weights \(\pm2\) vanishes, by the same generator argument as INVERSE_SPIN2_LITTLE_GROUP_DYNAMICS_GATE_2026_11_21.en.md. Having many mode labels or pairing indices is not the same as having a physical rank-2 tensor representation. Spatial-angular-momentum labels, a nonisotropic physical vacuum or an independent tensor representation would alter assumptions and require a separate gauge/constraint audit.

The genuine RH-inspired local Howe/Weil symplectic construction of PR #910/#911 lives on a different **real eight-dimensional indefinite pairing** \(B,\Omega\), whereas \(\Omega_{\mathrm{FS}}\) is a positive projective-state symplectic form for a **chosen reduced vector amplitude**. They are not interchangeable. An explicit quotient/intertwiner compatible with the locked two-sided connection, physical tetrad, torsion and constraints is still missing. Finite Fourier-unitarity, arithmetic positivity and heat-kernel convergence cannot solve the physical action selection.

## 5. Decisive next gate and status

Identify which of the three very different objects the proposed **full tensor/Jacobi Theta** means: (a) an eight-real-value biquaternion field with infinitely many scalar-labelled Fourier coefficients; (b) a quadratic mode-density interaction/readout; or (c) an actual independently transforming rank-2 physical carrier. Cases (a) and (b) do not bypass the preceding conditional linear helicity-2 no-go. Case (c) must first be derived consistently from Axiom A instead of importing an independent metric/tensor field. Then derive an *on-shell* physical covariant presymplectic current and Dirac constraints from one single-valued Theta-only action, before testing a Hamiltonian or emergent collective graviton.

**Exact verification:** tools/verify_jacobi_projective_mode_dynamics_gate_2026_11_24.py and research_tracks/fundamental_dynamics/tests/test_jacobi_projective_mode_dynamics_gate_2026_11_24.py; local SymPy 1.14.0 exact checks at \(N=2,3,4\), the \(N=3\) FFT counterexample, projective heat non-symplecticity and two distinct positive generators. The all-\(N\) rank theorem is analytic; finite tests alone do not prove it. **UBT action OPEN; physical helicity-2 OPEN; Lean and semantic review pending. Do not merge as a physics claim.**
