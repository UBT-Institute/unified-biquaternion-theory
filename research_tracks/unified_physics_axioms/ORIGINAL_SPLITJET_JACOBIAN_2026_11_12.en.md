# Original split-jet chart: explicit finite-dimensional Jacobian

**Status:** exact local algebra for the declared timelike Lorentz-real chart; continuum measure, regulator, and complex-Theta quantization remain open.

## Exact coordinate chart

Use the rest-frame chart in `research_tracks/action_selection/splitjet_spatial_dirac_2026_10.en.md`. Fix a future timelike carrier X with r=sqrt(X^2)>0 and Lorentz boost L(X), so L^{-1}X=r e_0. For each mu, set R=L^{-1}K_{J mu}L, q=L^{-1}Q_mu, with

R^0_i=R^i_0=b_i, R^i_j=-R^j_i=z_{ij}, and w_mu scalar.

Then q^0=r w_mu and q^i=r b_i. The three z_ij are the stabilizer coordinates. In the ordered variables (b_1,b_2,b_3,w,z_12,z_13,z_23), the map to (q^1,q^2,q^3,q^0,z_12,z_13,z_23) has determinant magnitude r^4. Lorentz L has determinant +1 on vectors and the induced conjugation has determinant +1 on the six-dimensional bivector representation. Thus, for one spacetime column, with the explicitly declared flat coordinate measures,

|det d(Q_mu,z_mu)/d(K_{J mu},w_mu)|=r^4.

For four independent spacetime columns, with X held fixed, the determinant magnitude is r^16. The full transformation including X has a block triangular Jacobian, so its X derivatives do not change the determinant:

dX dK_J dw = r^{-16} dX dQ dz,

up to a constant orientation/coordinate normalization. With fixed omega and s>0, Q_mu=s E_mu - D_mu^omega X, and the derivative dQ/dE=s I_16 gives

dX dK_J dw = (s/r)^16 dX dE dz.

For a discretization with M independent spacetime points, this factor is the product over sites of (s/r(x))^16, with a separately defined measure for the connection and the Grassmann sector.

## What this proves, and what it does not

The factor (s/r)^16 is nonconstant if the **original** K_J,w measure is taken flat in these coordinate components. Hence the statement that the parent Q-integral has unit Jacobian does not, by itself, prove equality of the original split-jet quantum theory and Einstein–Cartan–Dirac quantum theory. A *pushforward/adapted* measure proportional to (r/s)^16 dX dK_J dw cancels this factor and gives a flat dX dE dz measure, but this is a **choice of measure**, not a prediction from the UBT microscopic action.

Even if X and z are pure gauge classically, a field-dependent factor can matter quantum mechanically unless the full gauge-invariant measure and FP/BV procedure are specified. Its behavior at r=0 is singular, so the calculation cannot be extrapolated across null carrier patches.

The L(X) dependence produces off-diagonal X derivatives in the full Jacobian but does not alter the determinant because the X coordinate is retained. It *does* matter in the canonical cotangent lift; this is consistent with the existing momentum-shift theorem.

## Minimal quantization gate

To claim exact quantum equivalence on a regular timelike patch one must:
1. declare the microscopic measure on X,K_J,w (or its BV extension) and verify gauge invariance;
2. account for this r^{-16} factor in the original variables, not only in the auxiliary Q-parent;
3. demonstrate that the residual stabilizer and carrier quotient cancels the relevant volume without anomalous Jacobians;
4. prove matching of invariant observables and boundary conditions.

This local result neither proves nor disproves that a full complex-biquaternionic measure has additional physical degrees of freedom.
