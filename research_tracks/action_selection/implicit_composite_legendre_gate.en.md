# Implicit composite-geometry response and the physical Legendre gate

**Conditional exact implicit-function identities, 2026-10-25. Not a fundamental action, Hamiltonian, or selected torsion law.** Continues #756 with the nonzero composite connection retained.

Let q denote eight real components of the sole fundamental Theta, v their real-time derivatives (spatial and psi jets may also be included), and z a **collective non-independent composite variable** representing real tetrad and torsion data and reconstructed connection. On a selected function space and after fixing genuine gauge redundancies, suppose a **complete** implicit system
\[
F(z,q,v)=0
\]
has been derived from locked tetrad/reconstruction relations **plus a genuine yet-to-be-derived torsion selector**. If F_z is invertible on the chosen reduced spaces, then
\[
z_{,q}=-F_z^{-1}F_q,\qquad z_{,v}=-F_z^{-1}F_v.
\]
These are formal Fréchet-operator relations in field theory, not necessarily finite matrices or local operators. Singular F_z may indicate gauge, branches, or ill-posed reconstruction; singularity is not automatically a physical constraint.

For any explicitly declared **candidate** density l(q,v,z) (possibly differential), define its fully reduced density L(q,v)=l(q,v,z(q,v)). The full momentum and reduced kinetic Hessian obey
\[
p=l_v+l_z z_v,\qquad
W=L_{vv}=l_{vv}+l_{vz}z_v+z_v^T l_{zv}+z_v^T l_{zz}z_v+\sum_I l_{z_I}z_{I,vv}.
\]
For local algebraic z and smooth finite-dimensional variables these are literal matrices. For composite spacetime derivatives, replace partial derivatives by variational/Fréchet derivatives with integration by parts and boundary conditions; the formula is only a schematic operator version. Crucially, **the last term does not vanish unless the auxiliary z are stationary for l (l_z=0) or z is affine in v**. Treating the connection as fixed erases z_v and can change Hessian rank and constraints.

If z is instead determined by genuine auxiliary stationarity l_z=0, the conditional Schur-complement identity applies:
\[
\boxed{W=l_{vv}-l_{vz}\,l_{zz}^{-1}\,l_{zv}}
\]
when l_zz is invertible. But UBT's composite connection is NOT known to be a stationary auxiliary field of an adopted l; using Schur complement without proving l_z=0 is unjustified.

A regular canonical Hamiltonian \(H=p\cdot v-L\) exists only after a physical choice of l, full elimination, appropriate Hessian inversion or Dirac-Bergmann reduction for singular W, and gauge closure. Nothing here selects l, T[Theta], symplectic structure, or bounded energy.

**Minimal exact nonzero-composite toy witness** (not a UBT reduction): let l=1/2 v²+1/2 z² and F=z-a v=0 with a constant nonzero a. Then L=1/2(1+a²)v² and p=(1+a²)v; freezing z would incorrectly give W=1. A distinct stationary auxiliary example l=1/2 m v²+bvz+1/2 c z² yields z=-(b/c)v and W=m-b²/c. Both show why the choice of implicit relation matters. Tests: tests/test_implicit_composite_legendre_gate.py.

**Next falsifiable UBT gate:** derive a torsion relation and show that the real physical operator F_z exists/inverts on a nondegenerate background; compute the principal symbol of the reduced Theta Euler–Lagrange equations and the constraint brackets. Only then claim a microscopic Hamiltonian.
