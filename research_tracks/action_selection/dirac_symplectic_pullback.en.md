# Dirac pullback versus the invariant Theta symplectic form — explicit incompatibility

**C-tier conditional exact matrix test, 2026-10-24. Not a no-go for all UBT Hamiltonians.** Continues merged #717 and #724.

Use the *specific* eight-real-dimensional candidate Ω_B(X,Y)=B(X,iY), B(X,Y)=Re Tr(adj(X)Y†), and Theta=[psi,chi] with complex entries. Choose the antilinear Weyl map F(Theta)=(psi,epsilon chi*) where epsilon=[[0,1],[-1,0]]. On flat prescribed momentum p, let the usual four-complex-component Dirac generator be H_D=[[-sigma·p,m I],[m I,+sigma·p]], with units c=hbar=1. Transport Schrödinger flow dot u=-i H_D u through the real-linear invertible F to a real 8x8 generator A: dot x=A x.

For *any* constant real alternating matrix Ω, this linear flow preserves Ω iff
\[
\boxed{A^T\Omega+\Omega A=0.}
\]
Using the explicitly known Ω_B in the above real-coordinate basis, symbolic differentiation shows the obstruction is nonzero already at (m,p)=(1,0) and at (m,p_x,p_y,p_z)=(0,1,0,0). In the coordinate ordering x=(Re psi1,Im psi1,Re psi2,Im psi2,Re chi1,Im chi1,Re chi2,Im chi2), the mass-only obstruction includes the entry (row 3,column 5, 1-based)=2m. Thus even the ordinary Dirac mass evolution alone is **not** Hamiltonian with this specific native Ω_B. No scalar Hamiltonian function H on this 8-real linear phase space can generate this flow using Ω_B because a Hamiltonian vector field must preserve the symplectic form.

This is a clean distinction: the Weyl-duality identity in #724 gives correct Lorentz transformation *representations*; it does **not** establish compatible Hamiltonian mechanics. The usual positive complex Dirac symplectic form can be pulled back by F and is preserved by its unitary evolution for each momentum, but that form is not thereby proved to be the Lorentz-congruence-invariant Ω_B or the physical UBT form. Changing Ω would require an independent selector/derivation; imposing constraints might also alter the physical reduced symplectic form.

**Scope:** prescribed Fourier momentum and flat background; no derivation of dynamics of composite tetrad/connection, complex time psi, full gauge constraints, or unique action. The test concerns this *particular* F, H_D and Ω_B; it does not rule out other first-order operators or a constrained reduction.

Next step: classify symplectic-compatible Lorentz-equivariant first-order matrix symbols on the chosen UBT carrier, or derive a different physical Ω through an intrinsic reduction; demand mass-shell factorization and positivity **after** constraint reduction.

Check: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_dirac_symplectic_pullback.py' -v\`.
