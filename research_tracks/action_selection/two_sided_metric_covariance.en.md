# Two-sided covariant derivative: exact gauge covariance and central metric preservation

**Exact kinematic theorem; 2026-10-25. Does not select a fundamental Hamiltonian or an independent connection.** Uses locked Axiom C. The connection coefficients must ultimately be composite/auxiliary rather than additional fundamental propagating fields.

Define \(D_\mu X=\partial_\mu X+A_\mu X+XB_\mu\). Under a local invertible two-sided change \(X'=LXR\), require \(D'_\mu X'=L(D_\mu X)R\). The unique algebraic transformation rules for the connection coefficients acting on arbitrary X are
\[
\boxed{A'_\mu=LA_\mu L^{-1}-(\partial_\mu L)L^{-1},\quad
 B'_\mu=R^{-1}B_\mu R-R^{-1}(\partial_\mu R).}
\]
Direct expansion cancels both inhomogeneous derivatives.

For \(S\in SL(2,C)\), choose \(L=S,\ R=S^\dagger\) and let the covariant tetrad transform \(E'_\mu=S E_\mu S^\dagger\). The quaternion sharp in the 2×2 matrix representation is the matrix adjugate. For determinant-one S, \(S^\sharp=S^{-1}\); because adjugate reverses products,
\[
(E'_\mu)^\sharp=(S^\dagger)^{-1} E_\mu^\sharp S^{-1}.
\]
Therefore
\[
\tfrac12[(E'_\mu)^\sharp E'_\nu+(E'_\nu)^\sharp E'_\mu]
=(S^\dagger)^{-1}\Big(\tfrac12[E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu]\Big)S^\dagger
=g_{\mu\nu}I.
\]
Thus the locked sharp central metric is invariant. The canonical Lorentz slice \(W_L=i\,{\rm Herm}_2\) is preserved because \(S(iH)S^\dagger=i(SHS^\dagger)\).

**Critical distinction:** this transformation of E is a *vector/tetrad* Lorentz carrier; by itself it does **not** make Theta a Dirac spinor (the 2π central element cancels). The left-spinor and derived Dirac carrier discussions of #721–#726 remain separate. A covariant map relating the spinorial Theta carrier to the tetrad derivative must be derived before combining their generator algebras. The simple global phase \(\Theta\mapsto e^{i\alpha}\Theta\) is not an invariance of the sharp metric if E transforms with the same phase (#734).

**Dynamical gap:** proving the algebraic connection transformation does not derive A,B from Theta, determine torsion, identify physical first-class constraints, or close the hypersurface deformation algebra. Treating A,B as arbitrary independent fields would violate the locked one-fundamental-field rule. The next Hamiltonian task is to insert the *actual composite connection reconstruction* into this identity and calculate constraint brackets, including its field dependence.

Reproducibility: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_two_sided_metric_covariance.py' -v\`.
