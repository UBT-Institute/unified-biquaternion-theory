<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Complex-time holomorphy versus Lorentz covariance

**Status:** exact no-go for global frame-independent holomorphy with a
Lorentz-scalar imaginary-time fiber.

Assume that \(t=x^0\) is ordinary Lorentz time, \(\psi\) is an independent
Lorentz scalar, and a generic field obeys strict holomorphy in
\[
\tau=t+i\psi
\]
in every inertial frame.  The Cauchy--Riemann equation is
\[
\partial_\psi\Theta=i\,\partial_t\Theta.
\]

For a boost in the \(x\) direction,
\[
\partial_{t'}=\gamma(\partial_t+v\partial_x).
\]
Frame-independent holomorphy would also require
\[
\partial_\psi\Theta=i\,\partial_{t'}\Theta.
\]
Combining the two equations gives
\[
(\gamma-1)\partial_t\Theta+\gamma v\,\partial_x\Theta=0.
\]
Repeating for the opposite boost gives the same equation with the second term
reversed.  For any nontrivial boost this implies
\[
\partial_t\Theta=\partial_x\Theta=\partial_\psi\Theta=0.
\]
Repeating in the other spatial directions removes generic spacetime dependence.

Therefore strict microscopic holomorphy in \(t+i\psi\), an independent scalar
\(\psi\), and frame-independent four-dimensional Lorentz covariance cannot all
hold simultaneously for a generic dynamical field.

Two consistent branches remain:

1. **Scalar-fiber branch:** treat \(\Theta=\Theta(x^\mu,\psi)\), keep \(\psi\)
   as an independent Lorentz scalar, and reserve strict holomorphy for reduced
   theta/spectral sectors rather than the full microscopic field.
2. **Fully complexified-spacetime branch:** if holomorphy is fundamental, use
   complex coordinates \(z^\mu=x^\mu+i y^\mu\) whose imaginary partners
   transform covariantly with \(x^\mu\).

The current minimal audit uses branch 1 provisionally.  This theorem does not
by itself determine the action or the physical status of the \(\psi\) sector.

Verification: \`verification/theta_holomorphy_lorentz_no_go.py\`.
