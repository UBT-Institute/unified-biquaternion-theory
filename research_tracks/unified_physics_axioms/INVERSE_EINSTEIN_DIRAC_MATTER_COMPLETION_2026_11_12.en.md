# Einstein–Dirac matter completion of the adopted split-jet gravity comparator

**Status: CONDITIONAL IR comparator; NOT a derivation of fermions from Theta or a complete UBT microscopic action.**

## Grounding

The adopted candidate in `canonical/gr_closure/gravity_dynamical_postulate.en.md` already supplies the one-coupling Palatini + Henneaux–Teitelboim gravity action with regular split-jet surjectivity. The gravity-only Dirac quotient in `research_tracks/action_selection/splitjet_spatial_dirac_2026_10.en.md` is conditional on no additional dependence on redundant carrier/jet kernel. The Lorentz-only 9/10 metric rank obstruction in `research_tracks/action_selection/composite_lorentz_variation_rank_2026_10.en.md` is repaired by a **permitted independent relative dilation**; a common center that cancels is insufficient.

## Explicit conditional matter comparator

Let e=E(Theta,omega,K_J,w) be the existing composite tetrad on the regular non-null patch, with full permitted split-jet variations, and let psi be an **independent Grassmann-valued Dirac spinor**. Define

S_IR = S_G[e,omega,Lambda,C3] + S_D[e,omega,psi]

where S_G is exactly the canonical one-coupling gravity candidate and

S_D = integral d4x det(e) [ i/2 (bar(psi) gamma^a e_a^mu D_mu psi - (D_mu bar(psi)) gamma^a e_a^mu psi) - m bar(psi) psi ].

The spin connection enters the Dirac covariant derivative via (1/4) omega_mu^ab gamma_[a gamma_b]. No new tetrad is introduced. The shared Clifford identity yields (gamma^a e_a^mu p_mu)^2=g^mu nu p_mu p_nu I (up to convention for i).

## Chain variation and sourced Cartan equation

Write the independently varied parent Euler derivatives as E_e, C_omega and E_psi. The split-jet image variation has

delta_(K_J,w) S_IR = (DE_splitjet)^* E_e.

If the permitted image is surjective onto all tetrad variations, its equation implies E_e=0. Then the full omega variation

delta_omega S_IR = C_omega + (DE_omega)^* E_e

reduces to C_omega=0. With minimally coupled Dirac matter, this is the **sourced** Cartan torsion equation, not the vacuum T^a=0 equation. Under the ordinary invertible Einstein–Cartan algebraic torsion map, torsion is fixed by the axial spin density and is nonpropagating; eliminating it yields a contact axial-current four-fermion term with coefficient proportional to kappa (normalization/sign convention dependent). Spinor variation yields the torsionful Dirac equation, or equivalently the torsion-free Dirac equation plus induced contact interaction after elimination.

The Henneaux–Teitelboim variation still imposes d Lambda=0 and nu_e=dC3 locally. The tetrad equation includes the fermion stress tensor and the torsion-elimination corrections. No assertion is made that the cosmological integration constant is predicted.

## Exact failure modes

(1) If w is not an independent relative image direction, Lorentz-only variation has a missing metric-normal equation (rank 9/10) and the above inference fails.

(2) If a microscopic term depends independently on the Theta/jet kernel, the carrier shift is not a symmetry of the complete action. The gravity-only 0-extra-mode quotient cannot be reused without redoing the constraint analysis.

(3) The positive graviton TT Hamiltonian does not prove positivity of all complex Theta modes. Fermionic Hamiltonians require Grassmann quantization and a suitable physical Hilbert space; the ordinary bosonic Hessian positivity criterion does not directly apply.

(4) The adopted IR comparator **assumes** independent Dirac spinors, their Grassmann statistics, the action coefficients (including fermion mass), and the permitted split-jet variation bundle. It therefore proves no emergence of fermions, Born rule, unique UV action, numerical particle masses or ghost-free full UBT.

## Decision

The Einstein–Dirac IR *existence/matching* problem is conditionally solved for this supplied effective parent: the same composite tetrad can enter both sectors and the sourced Palatini connection equation remains algebraic. The **single-Theta microscopic closure** and physical spectrum remain OPEN. The next nontrivial test must supply a genuine Theta-to-spinor map or a justified independent matter sector, plus a microscopic selection rule for the allowed action terms; no amount of rewriting the standard Einstein–Cartan–Dirac comparator alone closes that gap.
