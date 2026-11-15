# Explicit Lorentz-slice central phase obstruction (conditional on sharp definition)

**Status: exact algebraic worked example; identification with the canonical sharp axiom still pending.**

Let H_C=C tensor H, with central complex i and quaternion basis e_j satisfying e_j^2=-1, e_j e_k+e_k e_j=-2 delta_jk. Embed a Lorentz vector as E=t+i sum_j x_j e_j for real t,x_j. Define quaternion conjugation sharp_Q by e_j^sharp_Q=-e_j and i^sharp_Q=i. Then

E^sharp_Q=t-i sum_j x_j e_j,
E^sharp_Q E=t^2-|x|^2,

which has Lorentz signature (+---) (opposite to the (-+++) convention in the canonical metric, an overall sign convention issue). Under central u=exp(i alpha), (uE)^sharp_Q(uE)=u^2 E^sharp_Q E, not E^sharp_Q E except u^2=1. Also uE generally leaves the real Lorentz-vector subspace W_L.

In contrast, define an anti-involution sharp_H combining quaternion conjugation with complex conjugation. Then i^sharp_H=-i, and u^sharp_H u=1; however E^sharp_H E for the same E is not the above Lorentz norm (it is generally noncentral), so one cannot switch sharp to sharp_H without rederiving the canonical metric and W_L.

This example demonstrates a *structural tension*: the natural quaternion-conjugate Lorentz quadratic form and a freely acting central phase on the entire tetrad are not simultaneously invariant under the same sharp_Q.

The repo canonical metric is explicitly g I=(E_mu^sharp E_nu+E_nu^sharp E_mu)/2 on W_L, without a Hermitian trace substitution. The precise axiom for canonical sharp must be identified before claiming a definitive UBT no-go.

**Alternative to test:** let the physical Lorentz tetrad remain neutral and let U(1) act on a separate charged Grassmann spinor module, or derive an internal action that preserves the Lorentz slice. Such a construction still needs an independently dynamical gauge field and its Maxwell action. No QED derivation or alpha prediction is established.
