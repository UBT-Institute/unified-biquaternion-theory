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

## 5. A further exact gate: internal psi winding is not graviton helicity

Under locked Axiom B, \(\psi\) is the **spatial scalar** imaginary-time coordinate. In a Fourier/Jacobi expansion
\[
\Theta(x,t,\psi)=\sum_{n\in\mathbb Z}\Theta_n(x,t)e^{in\psi},
\]
the integer \(n\) is a character of the *internal* translation group \(U(1)_\psi\), not automatically the spatial little-group helicity. Spatial rotations act on \(\Theta_n\) through its actual biquaternion representation; scalar-labelled copies retain the original weights.

A tempting identification \(\psi\mapsto\psi+\chi(R)\), turning internal phase translations into ordinary spatial rotations \(R\in SO(3)\), would need a continuous group homomorphism \(\chi:SO(3)\to U(1)\). There is **no nontrivial homomorphism**: the Lie algebra \(\mathfrak{so}(3)\) is generated by its commutators, whereas \(\mathfrak{u}(1)\) is abelian. For a homomorphism derivative \(d\chi\),
\[
d\chi([J_x,J_y])=[d\chi(J_x),d\chi(J_y)]=0
\quad\Rightarrow\quad
\boxed{d\chi=0,\qquad\chi(R)=1.}\tag{4}
\]
This excludes a **global direction-independent phase locking**, not a \(k\)-dependent spin connection or nontrivial associated bundle.

There is a second, topological diagnostic over the momentum-direction sphere \(S^2\). A massless helicity-\(h\) complex polarization line has first Chern number \(c_1=-2h\), with a north/south transition of winding
\[
t_h(\varphi)=e^{-2ih\varphi},\qquad
c_1=\frac{1}{2\pi i}\int_0^{2\pi}t_h^{-1}\partial_\varphi t_h\,d\varphi=-2h.
\]
Thus a graviton's **individual helicity lines** have \(c_1(\mathcal L_{+2})=-4\) and \(c_1(\mathcal L_{-2})=+4\). A fixed scalar \(e^{in\psi}\), taken with its momentum-independent global basis, instead has \(c_1=0\), for **every integer \(n\)**. No everywhere-nonzero smooth identification of that trivial line with either graviton helicity line exists. This is established massless-representation topology (Palmerduca and Qin, *Graviton topology*, JHEP 11 (2024) 150, https://doi.org/10.1007/JHEP11(2024)150 ; *Helicity is a topological invariant of massless particles*, Phys. Rev. Research 7 (2025) L022001, https://doi.org/10.1103/PhysRevResearch.7.L022001 ), NOT a discovery of UBT.

**Scope matters.** The direct sum of opposite complex helicity lines can be topologically trivial, even though each helicity line is not; this argument rules out a naive identification of **individual scalar winding modes** with helicity lines, not all possible paired polarization carriers. A nontrivial \(\hat k\)-dependent projector, genuine rotational index, momentum-space Berry connection or interacting collective pole could alter the bundle. None has been derived from the locked \(\Theta\) action. Nor does a fixed-axis \(SO(2)\to U(1)\) character establish full spatial \(SO(3)\) covariance: choosing the axis by hand changes the problem.

**Regression:** the SymPy verifier \`psi_winding_vs_graviton_helicity_topology_gate\` checks the exact \(\mathfrak{so}(3)\) commutators, vanishing \(\mathfrak{so}(3)\to\mathfrak{u}(1)\) homomorphism, helicity transition windings \(0,\pm2,\pm4\), and momentum-independent internal basis. These checks confirm the specified algebra and winding integrals, not any UBT field equation, dynamical physical bundle or Hamiltonian.

## 6. Decisive next gate and status

Identify which of the three very different objects the proposed **full tensor/Jacobi Theta** means: (a) an eight-real-value biquaternion field with infinitely many scalar-labelled Fourier coefficients; (b) a quadratic mode-density interaction/readout; or (c) an actual independently transforming rank-2 physical carrier. Cases (a) and (b) do not bypass the preceding conditional linear helicity-2 no-go. Case (c) must first be derived consistently from Axiom A instead of importing an independent metric/tensor field. Then derive an *on-shell* physical covariant presymplectic current and Dirac constraints from one single-valued Theta-only action, before testing a Hamiltonian or emergent collective graviton.

**Exact verification:** tools/verify_jacobi_projective_mode_dynamics_gate_2026_11_24.py and research_tracks/fundamental_dynamics/tests/test_jacobi_projective_mode_dynamics_gate_2026_11_24.py; local SymPy 1.14.0 exact checks at \(N=2,3,4\), the \(N=3\) FFT counterexample, projective heat non-symplecticity and two distinct positive generators. The all-\(N\) rank theorem is analytic; finite tests alone do not prove it. **UBT action OPEN; physical helicity-2 OPEN; Lean and semantic review pending. Do not merge as a physics claim.**
