# QED matching gate for quantized split-jet UBT

**Status: conditional comparator, not emergent electromagnetism.**

A quantum UBT that claims to reproduce known physics must reproduce the renormalized low-energy QED sector, not merely the Einstein–Dirac kinetic term.

## Required effective action

Introduce an **independent** U(1) connection A and charge q as a comparator, with F=dA and D_mu psi=(partial_mu+spin_connection_mu+i q A_mu)psi. Then

S_IR = S_EC-Dirac[E,omega,psi,barpsi;A] - (1/4) integral d^4x |E| F_mu_nu F^mu_nu + S_HT.

This is an extension of the prior independent-fermion comparator. Neither A nor its coupling q has yet been derived from the single biquaternionic Theta field. No charge quantization, alpha prediction, or electron mass prediction follows from adding these terms.

## Classical and quantum consistency gates

1. U(1) symmetry: A_mu -> A_mu - partial_mu alpha, psi -> exp(i q alpha)psi, barpsi -> barpsi exp(-i q alpha). The field strength and covariant derivative transform appropriately; the split-jet shift acts on X,Q but leaves E,omega,A,psi invariant. Thus the independent U(1) symmetry commutes with the auxiliary shift in this comparator.
2. Photon modes: Maxwell first-class Gauss constraint removes the unphysical longitudinal/time components, leaving two local transverse photon polarizations on a regular background.
3. Ward–Takahashi: k_mu Gamma^mu(p+k,p)=S^{-1}(p+k)-S^{-1}(p) with the charge stripped from the proper vertex. A symmetry-preserving regulator yields Z1=Z2. A nonzero Proca photon mass is forbidden by unbroken local U(1).
4. Quantum beta function: with one charged Dirac fermion, the leading perturbative QED running is beta(e)=e^3/(12 pi^2)+O(e^5), in a conventional mass-independent scheme and energies above the fermion threshold. Matching this does NOT predict the observed alpha without specifying a boundary condition or microscopic matching.
5. Four-fermion Einstein–Cartan torsion contact terms are higher-dimension EFT operators. They can modify amplitudes and mixing at gravitationally suppressed order; the exact QED limit is obtained only in the appropriate decoupling/low-energy limit, not as an assertion that the full interacting theory is pure QED.

## Next genuinely UBT-specific task

Construct A_mu as a connection on a well-defined U(1) subbundle or identify an independent gauge component in the full complex-Theta covariant derivative. Prove its transformation law, nondegenerate Maxwell kinetic term, absence of additional propagating ghost modes, minimal fermion coupling, and charge representation. Then compute the one-loop vacuum polarization and vertex/fermion self-energy and verify the Ward identity and QED beta function. Without that construction, the comparator is a consistency target, not a derivation.
