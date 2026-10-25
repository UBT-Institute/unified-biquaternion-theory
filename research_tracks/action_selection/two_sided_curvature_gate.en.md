# Two-sided curvature identity: what it does and does not constrain

**Exact off-shell algebraic identity, 2026-10-25; NOT a derived Hamiltonian constraint.** Builds on merged #735. Let
\[
D_\mu X=\partial_\mu X+A_\mu X+XB_\mu,\qquad X'=LXR,
\]
with the corresponding connection laws established in #735. Direct expansion, paying attention to right multiplication order, yields
\[
\boxed{[D_\mu,D_\nu]X=F^L_{\mu\nu}X+XF^R_{\mu\nu}}
\]
where
\[
F^L_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu+[A_\mu,A_\nu],\qquad
F^R_{\mu\nu}=\partial_\mu B_\nu-\partial_\nu B_\mu-[B_\mu,B_\nu].
\]
The minus sign in the right commutator is essential. Under local changes, \(F^{L\prime}=LF^L L^{-1}\) and \(F^{R\prime}=R^{-1}F^R R\), hence the identity is covariant.

**Key logical separation:** This is a Ricci/integrability identity, not a primary or secondary Dirac–Bergmann Hamiltonian constraint. It says nothing about which initial data are dynamically admissible without a specified relation between A,B and Theta, plus dynamics. Nor is setting both curvatures to zero justified: the tetrad may be curved. Torsion and the spin connection reconstructed from the composite tetrad have to be inserted with correct frame/coordinate conventions. No independent A/B gauge bosons are introduced by this algebra.

On the locked branch \(E_\mu=N_0^{-1/2}D_\mu\Theta\), one has
\[
D_\mu E_\nu-D_\nu E_\mu=N_0^{-1/2}(F^L_{\mu\nu}\Theta+\Theta F^R_{\mu\nu})
\]
provided \(D_\mu\) acts on the biquaternion value and the coordinate labels carry no additional affine connection. This is an *off-shell* antisymmetric jet identity; identification with spacetime torsion requires the frame-connection and spacetime affine terms to be specified, not silently presumed.

**Next decisive derivation:** fix the allowed *composite* mapping \(A_\mu[\Theta], B_\mu[\Theta]\), including torsion prescription, then take functional derivatives of the resulting tetrad constraints on a chosen phase space and compute their Poisson brackets. The curvature identity itself cannot select \(H\), and diffeomorphism constraint closure must not be claimed from it alone.

Algebraic reproducer in tests/test_two_sided_curvature.py.
