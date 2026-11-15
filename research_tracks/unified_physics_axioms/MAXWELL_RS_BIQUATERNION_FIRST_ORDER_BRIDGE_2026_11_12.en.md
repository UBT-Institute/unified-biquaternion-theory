# Exact Maxwell–Riemann–Silberstein–biquaternion first-order bridge

**Status:** algebraic equivalence to classical Maxwell equations (with or without electric sources), NOT a derivation of Maxwell dynamics from canonical UBT Theta. Units c=epsilon0=mu0=1. Central complex imaginary i commutes with quaternion units bold i,j,k.

Let E,B be real vector fields, J real electric current, rho real charge density. Set F=E+i B, and the pure biquaternion f=F_x bold_i+F_y bold_j+F_z bold_k. Define nabla_H=bold_i partial_x+bold_j partial_y+bold_k partial_z. The Hamilton product yields nabla_H f = -(div F) 1 + (curl F)_H.

Define D=nabla_H-i partial_t. Then the single biquaternion equation

D f = -rho 1 + i J_H

is equivalent to all four real Maxwell equations:
div E=rho; div B=0; curl E=-partial_t B; curl B=partial_t E+J.
Proof: scalar part -div(E+iB)=-rho gives the two divergence equations. Vector part curl(E+iB)-i partial_t(E+iB)=i J; its real part gives curl E+partial_t B=0, imaginary part curl B-partial_t E=J.

Taking divergence of curl F-i partial_t F=i J and using div F=rho yields partial_t rho+div J=0. Thus current conservation is a compatibility condition.

For rho=J=0 the equation D f=0 is equivalent to the free Maxwell equations. Plane-wave solutions have two physical transverse polarizations after the reality condition E,B real is enforced.

Important: this is the classical Riemann–Silberstein encoding already known in the literature; no claim of mathematical novelty. The complex duality rotation f -> exp(i theta) f rotates E and B, and is not the electromagnetic gauge transformation A -> A+d alpha.

The canonical bridge Maxwell_complete_derivation.tex defines A_mu=partial_mu phi/e, which has zero curvature for smooth phi, while canonical/interactions/qed.tex separately postulates a dynamical A_mu and -F^2/4. The exact quaternionic equation above provides a nonzero field-strength representation **without** demanding a pure-gradient potential, but does not derive its first-order equation from the canonical action for Theta.

**Next decisive gate:** construct an explicit Lorentz-equivariant map P from the canonical Theta jets (Theta,DTheta,...) to f, and prove P(Euler-Lagrange[Theta]) implies D f=-rho+i J_H without inserting Maxwell equations or an independent Maxwell kinetic term as premises. Verify compatibility with sharp, W_L, torsion, sources, and energy positivity.
