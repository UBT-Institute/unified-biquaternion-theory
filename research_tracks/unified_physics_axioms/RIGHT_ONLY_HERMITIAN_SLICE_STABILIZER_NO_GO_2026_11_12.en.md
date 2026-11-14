# Exact right-only stabilizer of the Hermitian Lorentz slice

**Result: proved for the standard Hermitian realization W_H={X in M_2(C): X^dagger=X}. Applicability to canonical UBT W_L and sharp requires an explicit isomorphism.**

Let U in GL(2,C) be fixed and require XU in W_H for every X in W_H. Hermiticity yields U^dagger X=XU for every Hermitian X. Setting X=I gives U^dagger=U. Then [U,X]=0 for every Hermitian X. Since I,sigma_1,sigma_2,sigma_3 span M_2(C) over C, U lies in the center, U=lambda I, lambda real and nonzero. Conversely every nonzero real scalar U preserves W_H. If U in SL(2,C), det U=lambda^2=1 implies U=+I or U=-I. If in addition det(XU)=det X for all X, again lambda^2=1. The identity-connected right-only Lorentz-slice stabilizer in SL(2,C) is trivial.

Contrast: coupled left/right transformations X -> L X L^dagger preserve the slice and Lorentz determinant and realize Spin^+(1,3); these are Lorentz frame transformations, not an additional internal gauge group. Right-only transformations of an independent matter module need not obey the same restriction as right-only transformations of the geometric vector X.

**UBT caveat:** canonical tetrad E_mu=N0^(-1/2) D_mu Theta, with sharp-defined metric and a specific real Lorentz slice W_L. A field redefinition Theta -> Theta U does not necessarily induce E_mu -> E_mu U unless the connection transforms appropriately; even when it does, it must obey B_mu=-Omega_mu^ddagger up to common center. Thus this proof excludes continuous right-only stabilizers of the standard Hermitian geometric slice, not all conceivable internal symmetries of canonical UBT.

**Next:** identify canonical W_L/sharp concretely; determine if the Hermitian identification is a faithful intertwiner for right multiplication. If yes, the above right-only no-go transfers. If no, calculate the stabilizer in the actual canonical representation. Keep a separate fermionic module for the surviving vector U(1) candidate and require a kinetic term and charge coupling.
