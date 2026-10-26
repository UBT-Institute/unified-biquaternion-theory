# Mandatory Euler–Lagrange chain rule after eliminating composite geometry

**Integrated continuation of merged UBT Fundamental Dynamics PR #770 (2026-10-26).** An exact inverse-variational step, not a new fundamental UBT action.

Take the sole dynamical field q=vec_R(Theta), and denote the *non-independent* composite tetrad/connection/torsion data by z=Z[q] (possibly involving derivatives of q). Let a provisional differentiable density/action S_ext[q,z] be an algebraic computational device; it must not add an independent fundamental z field. Define the actual reduced functional S_red[q]=S_ext[q,Z[q]].

For arbitrary compactly supported δq, its first variation is
\[
\delta S_{\rm red}=\langle E_q,\delta q\rangle+\langle E_z,DZ[q]\,\delta q\rangle
+\text{boundary}
=\langle E_q+(DZ[q])^*E_z,\delta q\rangle+\text{boundary}.
\]
Consequently the **correct reduced Euler–Lagrange equation** is
\[
\boxed{E_q+(DZ[q])^*E_z=0.}
\]
Here the star denotes formal adjoint, with spacetime measure, time/psi boundaries and integrations by parts specified. If Z is implicitly determined by F(z,q,jets(q))=0, the derivative DZ is the solution of F_z DZ=-F_q (Fréchet operators). The formula is fully compatible with a **nonzero** connection and should be applied to its complete two-sided operator A[Theta],B[Theta] as well as torsion, not by independently varying these as fundamental fields.

The common shortcut "vary q holding z fixed, set E_q=0, then impose z=Z[q]" misses (DZ)^*E_z and is equivalent only under demonstrable exceptional conditions: E_z=0 along the composite relation, or (DZ)^*E_z=0. An auxiliary *stationary* elimination (E_z=0) is one sufficient case but has NOT been established for UBT's metric-compatible spin connection or torsion.

**Exact nontrivial witness.** For one coordinate q(t), v=q_dot, let z=a v with nonzero constant a and S_ext=∫dt (v²+z²)/2. This is a toy with a nonzero velocity-dependent composite variable, NOT the UBT action. Its reduced Lagrangian is L_red=(1+a²)v²/2 and
\[
E_q=-q_{tt},\quad E_z=z,\quad DZ=a\partial_t,\quad
(DZ)^*E_z=-a\partial_t z=-a²q_{tt}.
\]
Thus E_red=-(1+a²)q_tt rather than -q_tt. The correct canonical momentum is p=(1+a²)q_dot and Hamiltonian H=p²/[2(1+a²)], whereas freezing z gives a wrong momentum and energy. The equations happen to have the same zero-set for a constant a, but their symplectic structure and Hamiltonian differ: an important distinction for UBT's action-selection program.

**Necessary gates before claiming S_UBT, L_UBT or H_UBT:**
1. derive a *single-valued and gauge-reduced* composite reconstruction Z[Theta], including torsion selector and its functional response;
2. find and justify the unique real scalar action candidate (kinetic pairing, complex-time integration measure, interactions);
3. calculate E_red by the full boxed chain rule, its Helmholtz/Noether checks and linearized principal symbol;
4. derive covariant presymplectic current, physical primary/secondary constraints, reduced Hamiltonian and energy positivity;
5. verify GR, spin/gauge and psi limits quantitatively.

This lemma cannot itself select the dynamical torsion equation or unique action. It prevents a mathematically invalid substitution step while pursuing them.
