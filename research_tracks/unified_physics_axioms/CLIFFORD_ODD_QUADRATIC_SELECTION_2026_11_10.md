# Full Clifford inverse-selection: first quadratic odd-sector calculation

**2026-11-10 | research calculation | conditional, not canonical dynamics.**

## Geometry and convention

Real \(Cl_{1,3}\) with \(\gamma_0^2=+1\), \(\gamma_i^2=-1\) has grades \(1,4,6,4,1\), for dimension 16. Its even subalgebra \(Cl^+_{1,3}\cong M_2(\mathbb C)\cong\mathbb C\otimes\mathbb H\) is 8-real-dimensional. Let \(I=\gamma_0\gamma_1\gamma_2\gamma_3\), \(I^2=-1\), and write the odd part \(\Phi_-=V+IA\), with vector fields \(V=V^\mu\gamma_\mu\), \(A=A^\mu\gamma_\mu\). Vector and axial-vector representations have the same proper Lorentz transformation but opposite conventional parity. Multiplication by an invertible \(\gamma_0\) maps odd to even as vector spaces; this alone does not identify or remove physical degrees of freedom.

## Invariant quadratic seed: explicit assumptions and scope

For a prescribed Lorentzian background and the *restricted* two-derivative scalar-contracted family (not an exhaustive invariant-basis classification for vector fields), choose
\[
\mathcal L_{\mathrm{odd},2} =
-\frac12 k_V(\nabla_\mu V_\nu)(\nabla^\mu V^\nu)
-\frac12 k_A(\nabla_\mu A_\nu)(\nabla^\mu A^\nu)
-k_{VA}(\nabla_\mu V_\nu)(\nabla^\mu A^\nu)
-\frac12 m_V^2 V^2-\frac12 m_A^2 A^2-\mu V\cdot A.
\]
Parity invariance in the standard vector/axial assignment excludes \(k_{VA}\) and \(\mu\); it does not set \(k_V\) or \(k_A\) to zero. This seed is only a comparison, **not** the fundamental UBT action and not a healthy vector-field action by itself. Additional invariants \((\nabla\cdot V)^2\), \((\nabla_\mu V_\nu)(\nabla^\nu V^\mu)\), antisymmetric derivatives, torsion couplings, curvature couplings, mixing with \(\Phi_+\), and boundary equivalences must be included in the next complete classification.

On a local flat background each vector component in this restricted ansatz has a Fourier block (up to signature conventions)
\[
C(p^2)=
\begin{pmatrix}
m_V^2+k_V p^2&\mu+k_{VA}p^2\\
\mu+k_{VA}p^2&m_A^2+k_Ap^2
\end{pmatrix},\qquad
\det C=(m_V^2+k_Vp^2)(m_A^2+k_Ap^2)-(\mu+k_{VA}p^2)^2.
\]
Its highest \(p^4\) coefficient is \(k_Vk_A-k_{VA}^2\). In the parity-invariant case this becomes \(k_Vk_A\). Thus if both \(k_V,k_A\ne0\), **the parity symmetry alone does not remove the two derivative-bearing odd fields**. Some modes may still be constrained, unstable or unphysical: a principal-symbol count is NOT a complete Dirac degree-of-freedom count. In particular the simple \((\nabla V)^2\) vector kinetic form is generally indefinite in Lorentzian signature and cannot establish positive-energy physical propagation.

## Exact auxiliary counterexample and consistent truncation test

For a finite real quadratic model of even variable \(u\) and odd variable \(v\):
\[
L=\tfrac12 a u^2+buv+\tfrac12 c v^2,\quad c\ne0.
\]
Varying \(v\) gives \(v_*=-bu/c\), and substitution gives
\[
L_{\rm eff}=\tfrac12(a-b^2/c)u^2.
\]
This is an *exact algebraic illustration* of odd-sector elimination; \(v_*\) need not vanish. It is NOT the result of varying the actual full Clifford UBT action.

For a \(\mathbb Z_2\) grading-symmetric action \(S[u,v]=S[u,-v]\), the equation \(\delta S/\delta v|_{v=0}=0\) holds in source-free configurations, so \(v=0\) can be a consistent classical invariant subspace if well-posed evolution preserves it. **That is not a gauge quotient and does not eliminate nonzero odd fluctuations**: a nondegenerate odd kinetic Hessian still permits excited initial data. A linear odd source breaks the simple truncation; a quantum path integral over odd fluctuations can also modify the even effective action.

## New no-go boundary

**Conditional result QO-1:** Local Lorentz covariance together with ordinary parity does NOT force the entire odd sector of a full \(Cl_{1,3}\) multivector field to be algebraically auxiliary or gauge redundant. The restricted invariant family displays independent nonzero derivative terms \(k_V,k_A\) compatible with both symmetries. A new physical selection principle or action-derived constraint is necessary to justify a biquaternion-only propagating sector.

**Not proven:** that the full Clifford UV completion exists, that \(k_V,k_A\) are selected, that the odd modes are healthy, that torsion or Standard Model sectors are recovered, that \(\Phi_-=0\) is dynamically selected, or that the actual composite-connection constrained Hessian has this block.

## Next non-optional calculations

1. Decide whether the full field is real \(Cl_{1,3}\) or complexified \(Cl_{1,3}\otimes\mathbb C\) and specify involutions, parity, chirality and the observable map. Complexification doubles real field components and cannot be silently identified with the real even subalgebra.
2. Enumerate a basis of local Clifford scalar invariants to second derivatives modulo integration by parts, Fierz/Clifford, Nieh–Yan and other relevant identities.
3. Include real metric readout, spin-connection and torsion as **composite or independent explicitly identified variables**; vary the *entire* action, not frozen-metric sector fragments.
4. Use constraint/Hamiltonian analysis and a gauge-reduced kinetic principal symbol to test if odd fields are auxiliary/gauge/heavy/propagating, with stability and hyperbolicity.
5. Derive a one-action map to gravity, fermions, gauge sectors and information/quantum observables, and test the known GR/SM/QFT/thermodynamic limits. Reuse all known canonical UBT no-go gates rather than silently restarting.

## Related repository sources

- [Odd-sector gates](FULL_CLIFFORD_ODD_SECTOR.md)
- [Inverse physics reconstruction](README.md)
- [Canonical action registry](../../canonical/ACTION.en.md)
- [Canonical spin-current/flat-affine obstruction](../../canonical/gr_closure/gap_10tdyn_10d_canonical_action_audit.tex)
- [Residual SO(2) Hamiltonian branch](../fundamental_dynamics/residual_so2_commutator_hamiltonian.en.md)

**Verification:** companion small SymPy test covers the determinant polynomial, decoupled parity case and auxiliary Schur complement. It is not a physical stability test.
