# Two-sided complex-biquaternion Lorentz stabilizer and central phase obstruction

**Status: exact result in the standard Hermitian 2x2 Lorentz-vector realization. Mapping this realization to the canonical UBT sharp and W_L is a separate required check.**

Identify H_C with M_2(C). Encode a real Lorentz vector as X=x^0 I+sum_{j=1}^3 x^j sigma_j, where x^mu are real and sigma_j are Pauli matrices. Then X^dagger=X and det X=(x^0)^2-|x|^2.

Consider T(X)=u L X R^{-1} with L,R in SL(2,C) and u=exp(i chi) a central unit phase. Suppose T maps *every* Hermitian 2x2 matrix to a Hermitian matrix. Set A=u L and B=R^{-1}. The requirement A X B=(A X B)^dagger=B^dagger X A^dagger for all Hermitian X implies B=t A^dagger with t a nonzero real scalar. Proof: multiply by (A^dagger)^{-1} on left and A^{-1} on right to obtain C X=X C^dagger, C=(A^dagger)^{-1}B. With X=I, C=C^dagger. Commuting with all Hermitian X forces C=t I with t real.

Hence R^{-1}=t u^* L^dagger. The SL determinant conditions give 1=t^2 (u^*)^2, so t=+/-1 and u^2=1. Thus the only allowable central unit phases on the full real Hermitian slice are u=+/-1. The transformation reduces to X'=+/- L X L^dagger; the identity-connected, time-orientation-preserving branch is X'=L X L^dagger. Its determinant is invariant, and SL(2,C) double-covers the proper orthochronous Lorentz group. The discrete overall minus reverses time orientation of timelike vectors and is not a continuous electromagnetic U(1).

**Implication:** a central U(1) acting by multiplying the *entire physical Lorentz-vector carrier* is obstructed in this standard realization. The left/right SL(2,C) parameters are linked by the Hermitian reality condition; independent SL(2,C)_L x SL(2,C)_R cannot be counted as physical internal gauge symmetry without extending the field space.

**Limitations:** this is a stabilizer calculation for the Hermitian-matrix representation, not yet a proof that the canonical UBT sharp or its specific W_L uses precisely this representation. It does not exclude U(1) acting on an independent charged fermion module, an internal fiber, or a different metric-preserving representation. Maxwell dynamics and QED remain unproved.

**Next gate:** locate the canonical sharp/ ddagger axioms, match their real slice to this Hermitian model, and determine any internal centralizer of the physical Lorentz representation on the full field module.
