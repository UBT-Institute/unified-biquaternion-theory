# Three-phase reduction: exact U(1)^3 / U(1)_diag gate

**Status:** exact linear-algebra result for three commuting phase sectors, not a derivation of QED or an assertion about the canonical Theta action.

Let phi=(phi1,phi2,phi3)^T be local phase coordinates (locally on a torus). Define relative differences theta1=phi1-phi2, theta2=phi2-phi3. The map

B=[[1,-1,0],[0,1,-1]]

has rank 2 and kernel span{(1,1,1)}. Hence three independent U(1) phases modulo the diagonal common phase yield U(1)^2 (globally the quotient torus), not a single U(1). The third difference phi3-phi1=-(theta1+theta2) is dependent.

A symmetric relative-phase quadratic form is

Q(phi)=(phi1-phi2)^2+(phi2-phi3)^2+(phi3-phi1)^2=phi^T K phi,

K=[[2,-1,-1],[-1,2,-1],[-1,-1,2]]=3 I-J.

Its eigenvalues are exactly (0,3,3), with zero eigenvector (1,1,1). This is a graph Laplacian identity. It demonstrates that a common phase drops out, but leaves **two** nonzero modes, not one. A putative three-phase reduction to exactly one photon requires an additional justified dynamical constraint, mass gap, or quotient. A fixed 120-degree offset (1,omega,omega^2), omega^3=1 and 1+omega+omega^2=0, is a special balanced configuration, not a general identity forcing a field mode to vanish.

For connection one-forms a=(a1,a2,a3), relative combinations a1-a2 and a2-a3 are invariant under a simultaneous common shift a_j -> a_j+d lambda, but this by itself is NOT the ordinary electromagnetic gauge transformation of a charged fermion. To obtain one low-energy Maxwell field, specify a remaining local U(1), its charged representation, a nondegenerate gauge-invariant F^2 kinetic term, and how the other relative vector mode is removed or becomes massive without a ghost. Merely quotienting a diagonal U(1) gives U(1)^2.

The three real quaternion generators I,J,K instead satisfy [I,J]=2K and generate SU(2), not U(1)^3; do not identify the commuting three-phase torus with the noncommuting quaternion phase manifold. The canonical Lorentz slice and sharp metric still impose independent gates.

**Relevance to UBT:** the cancellation of a common central term in the two-sided derivative is analogous at the level of a linear kernel, but the three-phase graph Laplacian is an explicitly proposed model, not a consequence of the canonical UBT action. No physical prediction for electric charge, alpha, or QED loop coefficients follows.
