<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Complex-Theta norm gate: why delta h(real X)=0 does not protect spinor mass

**2026-10-26. Explicit counterexample; full action and Grassmann structure remain open.**

Fix a real decomposition Theta=X+iY with Hermitian X,Y, and define the Lorentz-real norm h(X)=det X on a timelike Hermitian chart. The familiar real split-jet norm condition delta h(X)=tr(adj(X)delta X)=0 constrains only the **real projection** delta X; it says nothing about delta Y unless the action imposes an additional linked condition. The spinor mass candidate from the antilinear Dirac bridge is M(Theta)=2m Re det Theta.

**Counterexample.** Let X=I_2, Y=I_2, Theta=(1+i)I_2. Choose delta X=0 and delta Y=t diag(1,0) (t real). Then delta h(X)=0 exactly; nevertheless det(Theta+i t diag(1,0))=(1+i)^2+i t(1+i)=2i-t+i t, so Re det Theta shifts by -t, and delta M=-2m t. Thus the real norm constraint cannot protect the mass term on the full complex carrier even infinitesimally.

**Exact complex determinant criterion.** At arbitrary complex invertible Theta, delta Re det Theta=Re tr(adj Theta deltaTheta); with delta Im det Theta=Im of same. Imposing BOTH real/imaginary determinant variations zero is a codimension-two **infinitesimal** condition generically, but is not automatically a gauge symmetry or a Dirac constraint. Re(detTheta)=constant alone is codimension one locally; its restriction and the real norm constraint are independent on a generic complex chart. Do not treat determinant invariance as a dynamical consequence of delta h(real X)=0.

**Spinor kinetic limitation.** The invertible real-antilinear map Theta=(u,v)→Psi_D=(u,epsilon bar v) fixes the *representation*, not the kinetic presymplectic form. If Theta is a commuting complex bosonic field, no local invertible ordinary field redefinition changes its Grassmann parity; classical Dirac kinetic brackets/CAR therefore cannot be claimed. One can still formulate a classical commuting Dirac-like equation, but quantizing it as spin-1/2 fermionic matter requires a derived or explicitly postulated graded state space and spin-statistics mechanism. Likewise the bare determinant mass fails the full split-jet shift if those shifts act on the same complex carrier.

**Next criterion for genuine closure:** construct a single action with an explicit symmetry map on X,Y,Q, test shift invariance of all terms, derive fermionic graded canonical momenta (or another valid spin-statistics mechanism), and perform the constraint analysis. The simple real norm condition is not enough.

Regression: tests/test_information_complex_norm_spinor_mass.py.
