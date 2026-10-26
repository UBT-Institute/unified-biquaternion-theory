# Lorentz boost connection: surjective onto spatial TT perturbations at a point

**2026-10-26. Exact local kinematic construction; not a derived UBT graviton or full composite closure.** Continues merged #773 and integrated #770.

For restricted vector-lift e_i^a=N0^(-1/2)(partial_i v^a+omega_i^a_b v^b), at a regular local Lorentz frame choose v=(v0,0,0,0), v0 ≠0. Hold v fixed at the point and vary an so(1,3) connection. Its contribution is delta e_i^j=(v0/sqrt N0) delta omega_i^j_0. With locally identity background spatial tetrad, delta g_ij=delta e_i^j+delta e_j^i.

For ANY TT symmetric 3x3 H_ij (with wavevector along z: H=[[hplus,hcross,0],[hcross,-hplus,0],[0,0,0]]), define the boost coefficient
\[
\delta\omega_i{}^j{}_0=\delta\omega_i{}^0{}_j=
\sqrt{N_0}H_{ij}/(2v^0),\qquad i,j=1,2,3.
\]
All other components vanish. For signature (-,+,+,+), this is so(1,3) metric compatible since δω_i^T η+η δω_i=0. Its induced spatial perturbation is EXACTLY δg_ij=H_ij, giving a rank-two map onto the TT target. The spatial rotations that fix v contribute zero δe; these are separate from boosts. This complements the vanishing TT *bare gradient* principal symbol in #773: connection response can algebraically fill the gap.

**Crucial distinction:** the chosen delta omega here is an independent *test direction in the space of compatible geometries*. The one-field UBT has no independently variable connection. To show an actual TT mode, one must derive omega[Theta] including torsion selection, verify that some admissible delta Theta induces this delta omega and yields the two-dimensional TT image, and compute the full reduced Fourier symbol and positive Hamiltonian. This pointwise construction has no wave equation, masslessness proof, physical DOF count, stability proof or on-shell background claim. It is not a derivation of any gravitational dynamics.

The exact matrix test checks Lorentz compatibility and both TT amplitudes.
