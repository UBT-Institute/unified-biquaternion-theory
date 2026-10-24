# Lorentz boost gate for quaternionic spinor carriers

**C-tier representation theorem (2026-10-24), not a selection of the UBT Hamiltonian.** Refines draft #721 and the conditional obstruction #720. Locked Theta axioms and composite metric are not changed.

Let \(\Theta\in M_2(\mathbb C)\) and \(S\in SL(2,\mathbb C)\). Rotation-only left multiplication \(X\mapsto UX\), \(U\in SU(2)\), realizes two spin-half columns. But **uniform left multiplication** \(X\mapsto SX\) realizes two copies of the *same* left-Weyl representation \((\tfrac12,0)\); it does not give the standard Dirac carrier \((\tfrac12,0)\oplus(0,\tfrac12)\) for general boosts.

## Intertwiner obstruction including boosts

Under rotations, both the uniform-left carrier and the Dirac carrier decompose as two copies of the SU(2) fundamental. Any complex-linear intertwiner \(T\) commuting with all these rotations is a block \(2\times2\) matrix of scalar multiples of the \(2\times2\) identity (Schur's lemma), after grouping the two columns. Now consider the real boost subgroup \(S(u)=\exp(u\sigma_3/2)\), \(u\ne0\). The uniform-left carrier acts as \({\rm diag}(S,S)\), while the standard Dirac carrier acts as \({\rm diag}(S,(S^\dagger)^{-1})={\rm diag}(S,S^{-1})\). For any block \(T_{R,L}\) or \(T_{R,R}\) that would map a uniform-left Weyl copy to the right-Weyl copy, rotational equivariance forces \(T_{R,j}=a_j I_2\). Boost equivariance then gives \(a_jS=a_jS^{-1}\), and thus \(a_j=0\). Consequently the right-handed component of T vanishes; **no invertible Lorentz intertwiner exists** between uniform left multiplication and standard Dirac spinors. Spatial 2π sign agreement alone is not sufficient.

## Constructible candidate, not an axiomatic transformation

There is an explicit *candidate* two-sided/chirally projected Lorentz representation on the same biquaternion matrix without extra components:
\[
\boxed{\mathcal D_S(X)=SXP_L+(S^\dagger)^{-1}XP_R},\qquad
P_L=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad P_R=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
\]
It transforms the first column as \((\tfrac12,0)\), second as \((0,\tfrac12)\). For rotations \(U\), both sides reduce to \(UX\), and a 2π rotation changes sign. Its group property follows from \(P_LP_R=0\), \(P_L+P_R=I\) and \((S_1S_2)^{\dagger-1}=S_1^{\dagger-1}S_2^{\dagger-1}\).

**But** this right-projector/chiral assignment is not selected by the present UBT axioms. The projectors are a preferred right-module decomposition that must be derived or justified as gauge-equivalent data, not silently inserted. The transformation does not automatically preserve the real Lorentz tetrad slice \(W_L\) or the central anticommutator metric if applied directly to \(E_\mu=D_\mu\Theta/\sqrt{N_0}\). One must distinguish spinor Theta carrier from its induced geometric/tetrad representation, and establish an equivariant derivative/map between them.

**Next Hamiltonian selection gate:** derive a chirality grading/projectors from the native biquaternion structure or the locked complex-time geometry (without ad hoc fixed right frame), construct an equivariant covariant derivative and compatible physical presymplectic form, then test Dirac symbol square, positivity and constraints. The existence of this candidate alone is not the fundamental UBT Hamiltonian.

Exact SymPy regression: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_chiral_boost_gate.py' -v\`.
