# Explicit nondegenerate split-jet flat background and two-mode TT energy gate

## Existing results reused, not re-proved

This note joins three prior CONDITIONAL results: (i) split-jet surjectivity at non-null X and its Palatini pullback from research_tracks/action_selection/split_jet_palatii_variational_lift.en.md; (ii) local gravity-only phase-space/Dirac reduction preserving two GR tensor modes from research_tracks/action_selection/splitjet_spatial_dirac_2026_10.en.md; (iii) positivity of their nonzero-mode quadratic energy under the positive effective Einstein normalization from research_tracks/action_selection/full_spatial_dynamics_2026_10.en.md. No microscopic single-Theta action or curvature coupling is derived here.

## Explicit flat-background witness, including nonzero auxiliary components


\[
X^a=(1,0,0,0),\quad s=1,\quad
\omega_\mu{}^a{}_b=0,\quad
w_\mu=\delta_\mu^0,\quad
K_{Ji}{}^j{}_0=K_{Ji}{}^0{}_j=\delta_i^j.
\]
\[
E_\mu{}^a=\delta_\mu{}^a,\quad
\det E=1,\quad g_{\mu\nu}=\eta_{\mu\nu}.
\]
\[
h_{ij}^{\rm TT}=\begin{pmatrix}P&Q&0\\Q&-P&0\\0&0&0\end{pmatrix},
\quad E_0{}^0=1,\quad
E_i{}^j=\delta_i{}^j+\tfrac12 h_i{}^j.
\]
\[
\det E =1-\frac{P^2+Q^2}{4},\qquad
P^2+Q^2<4\Longrightarrow\det E>0.
\]
\[
\mathcal H_{\rm TT}^{(2)}
=\frac{M_{\rm Pl}^2}{4}
\left(\dot P^2+\dot Q^2+k^2(P^2+Q^2)\right)
\ge0,\qquad M_{\rm Pl}^2>0,\quad k^2\ge0.
\]


The chosen Lorentz generators K_J have nonzero time/spatial boost components, and satisfy the Lorentz Lie-algebra condition K_J^T eta+eta K_J=0. The relative-central real w provides the timelike column of E. Because X is constant, the displayed jets reproduce the unit tetrad *exactly*, not as a diagonal-Theta approximation. This is a local algebraic realization of Minkowski space in the Lorentz-real carrier sector of the full biquaternion theory; it is not a proof that this split-jet connection law is dynamically selected by a finalized fundamental action.

If the physical Lorentz connection omega is varied, the jet terms can be shifted algebraically to reproduce the same target tetrad: at X=e0 define Z_mu=s E_mu -omega_mu X, w_mu=Z_mu^0 and K_{J mu}^j{}_0=K_{J mu}^0{}_j=Z_mu^j. Thus the construction does NOT silently freeze the physical connection when claiming local kinematic realizability. Its on-shell value and the Cartan equations still come from the assumed Palatini functional.

## Nondegenerate TT fluctuation witness and bound

At fixed time, choose a Fourier wave vector along z and a symmetric TT wave in its two polarizations P,Q. The displayed coframe is exact at a chosen event and its metric is eta+h_TT+O(h_TT²). Its determinant is positive on P²+Q²<4, a *finite-amplitude algebraic* neighborhood. The plus/cross polarizations can be lifted by adjusting the independent split-jet boost coefficients, using the right inverse also when omega varies.

For an assumed positive-normalization Einstein/Palatini background with Lambda=0 and an allowed nonzero Fourier mode, the *reduced* quadratic gravity Hamiltonian displayed above is nonnegative. For k²>0 it is positive away from the zero perturbation, and the linearized equations are two independent oscillators with omega²=k². The k=0 sector requires its own global/boundary/gauge analysis. The present positivity is linearized and local on the regular flat branch; the determinant bound is algebraic, not a nonlinear stability proof.

## Distinguish rank, stability and the fundamental-action gap

The previous constrained radial scalar branch had a positive scalar Hamiltonian but rank E<=1; the current explicit split-jet benchmark has rank four *and* nonnegative TT gravity energy with no extra jet physical modes **provided** the curvature action, normalization and base constraint system are supplied. This does NOT eliminate the extra complex biquaternion components or determine their physical sign, nor establish a global metric, a unique vacuum, UV completion, nonlinear stability or generic ghost freedom. An arbitrary positive K for the remaining Theta sector is still forbidden.

The actual remaining proof obligation: derive the positive normalized curvature functional and any residual matter/complex-Theta kinetic terms from the *same* UBT action; verify their full mixed velocity Hessian, Dirac constraints and physical symplectic quotient on a nondegenerate background. The double requirement (full-rank tetrad, bounded physical Hamiltonian) is **conditionally compatible** but not yet a theorem of fundamental UBT.

## Verification scope

Lean in research_tracks/unified_physics_axioms/formal/SplitJetFullRankTTWitness.lean proves the exact finite determinant expression *as a definition*, its positivity condition, and quadratic TT-energy nonnegativity. It does NOT formalize the full split-jet matrix reconstruction, spin connection, continuum Dirac algebra or GR perturbations; these are represented by existing repository derivations and a new exact SymPy regression test covering the explicit Lorentz boost matrices, composite tetrad, arbitrary compatible omega variation and TT metric to first order. Do not describe the result as proof of full UBT stability.
