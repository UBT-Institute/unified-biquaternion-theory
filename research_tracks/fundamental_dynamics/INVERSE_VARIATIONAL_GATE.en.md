# Inverse-variational gate for one-field UBT dynamics

**Integrated subtask of PR #770 (2026-10-26).** This is a mathematical rejection/acceptance *necessary condition* for proposed Theta equations, NOT a derivation of a unique UBT action.

Represent the single biquaternion field Theta by real coordinates q^A, A=1..8. Suppose a complete candidate evolution system has been proposed as local differential Euler–Lagrange expressions F_A[q]=0 on a specified real-time slice and psi domain. Include every induced dependence of the composite Lorentz tetrad, metric, two-sided connection and torsion law on q and its jets. Let ell_F be its Fréchet linearization.

If F_A=delta S/delta q^A for a twice differentiable **real** action and variations with compact spacetime support, commuting second variations imply
\[
\int d^dx\, h^A(\ell_F k)_A=\int d^dx\, k^A(\ell_F h)_A.
\]
Thus \(\boxed{\ell_F=\ell_F^*}\) as formal differential operators, modulo boundary terms. This is a necessary Helmholtz test. Gauge identities, dependent field equations, equation multipliers or unusual nonlocal actions require explicitly specifying the appropriate reduced/extended variational problem; self-adjointness of an arbitrary presentation F is not a sufficient characterization of the physical action.

**Exact finite-dimensional regression:** For constant matrices M,C and smooth potential V, let F=M q_ddot+C q_dot+grad V. Then ell_F=M d_t²+C d_t+Hess(V). Its formal adjoint is M^T d_t²-C^T d_t+Hess(V). Thus F is formally self-adjoint iff M=M^T and C=-C^T. A representative Lagrangian with these properties is
\[
L(q,\dot q)=\tfrac12\dot q^T M\dot q-\tfrac12 q^T C\dot q-V(q),
\]
using Euler–Lagrange convention d/dt(dL/dq_dot)-dL/dq=F. The antisymmetric C yields a gyroscopic term; symmetric velocity damping violates this simple unconstrained local action test. This is a diagnostic model, *not* UBT dynamics.

**Nonuniqueness persists:** for any scalar potential V invariant under all *proved* full-field symmetries, changing V by an independent invariant changes F while retaining formal self-adjointness. Therefore meeting Helmholtz conditions does not fix the kinetic sign, torsion source, Hamiltonian or vacuum.

**Actual test order for one-Theta UBT:**
1. Prove a complete single-valued map z[q] for composite (E,T,omega,A,B), or formulate the actual constrained variational problem without independent new fundamental fields.
2. Compute full Frechet derivative including delta A[Theta], delta B[Theta], delta T[Theta], and all adjoints with measure/boundary conditions fixed.
3. Test Helmholtz symmetry and closure of Noether identities for candidate Theta flow. If failed, reject the proposed equations as stated rather than inserting a compensating term by hand.
4. Only then derive one consistent L, symplectic current and primary/secondary Hamiltonian constraints. Verify physical positivity and GR/Dirac/YM/psi reductions.

**Current state:** no physically selected F_A or T[Theta] exists, so the actual UBT Helmholtz condition cannot yet be evaluated. This necessary-condition theorem is not itself a selection principle or an S_UBT definition.
