# Lorentz congruence versus the chosen Dirac carrier: axial current covariance test

**Exact finite SU(2) counterexample, 2026-10-25. Not a universal spinor no-go and not a fundamental UBT Hamiltonian.** Follows #724, #746–#748.

The locked real Lorentz tetrad W_L=i Herm_2 is preserved by E→S E S†, S∈SL2(C), and the sharp metric is preserved (#735). Ask whether the same congruence law on the *value* Theta makes F(Theta)=(xi,epsilon chi*) a Dirac spinor, where Theta=[xi,chi] and epsilon=[[0,1],[-1,0]].

Its putative temporal axial current is j5^0=||chi||²−||xi||². Choose Theta0=diag(1,0), S=epsilon∈SU2 (a spatial rotation). Then S Theta0 S†=diag(0,1). Accordingly
\[
j_5^0(\Theta_0)=-1,\qquad j_5^0(S\Theta_0 S^\dagger)=+1.
\]
For a genuine axial four-vector the temporal component is unchanged under proper spatial rotations. Hence **this map F under congruence action on Theta is not an intertwiner to the standard Dirac representation**, and its proposed axial bilinear is not a Lorentz-covariant axial source with this action.

**Precise limitations:** The canonical tetrad transforms by congruence, but the theory has NOT demonstrated that Theta itself *must* transform by the same congruence. An alternative spinorial left action for Theta (#721/#724) or a suitable composite conversion could carry a correct Dirac representation while its tetrad follows an induced vector representation; compatibility with E=N0^-1/2 DTheta must be proved. This counterexample excludes only the simultaneous unqualified identification (Theta congruence, fixed F, ordinary Dirac axial current). SU2 spatial rotation differs from the separate arbitrary right SU2 diagnostic of #747; it is a genuine congruence rotation preserving the Lorentz slice.

**Hamiltonian consequence:** Do not insert the axial bilinear from F as a unique spin-torsion source in a foundational Theta Hamiltonian until the Theta/tetrad representation and compatible symplectic form are fixed. This does not forbid torsion sources from other derived bilinears. The missing representation-intertwining law is prior to torsion equation selection and the full constraint algebra.

Reproducer: tests/test_congruence_axial_covariance.py.
