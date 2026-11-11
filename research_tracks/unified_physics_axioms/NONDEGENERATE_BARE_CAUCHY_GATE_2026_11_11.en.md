# Nondegenerate UBT bare-action Cauchy/coercivity obstruction

## Scope: a specific already-derived action family

This is a conditional sharpening of the existing critical-zero theorem in research_tracks/action_selection/physics_closure_bare_action_2026_10.en.md. It does NOT establish a universal UBT no-go or disprove stability of a selected curvature/connection effective action. Assume the free split-jet auxiliaries can span local non-null tetrad variations at fixed Theta, the sharp/Gram kinetic pairing is the very pairing used to define the composite metric, the bare derivative-free potential is F(Theta), and a smooth critical zero Theta_* exists. No independent curvature or kinetic term is present. Work in an oriented local patch and use compactly supported variations.

## Exact geometric flatness


\[
S_{\mathrm{bare}}=\int d^4x\,\det(E)\,F(\Theta),\qquad
F(\Theta_*)=0,\quad dF_{\Theta_*}=0.
\]
\[
S_{\mathrm{bare}}[\Theta_*,E]=0,\quad
\delta_E S_{\mathrm{bare}}=\delta_E^2 S_{\mathrm{bare}}=0,
\]
\[
a_{\alpha}(T)=1+\alpha T^2,\quad
\det E_\alpha=(1+\alpha T^2)^3>0\;(\alpha>0),
\]
\[
a_\alpha(0)=1,\quad \dot a_\alpha(0)=0,\quad
\ddot a_\alpha(0)=2\alpha,
\]
\[
R_\alpha(0)=12\alpha+6,\quad
R_1(0)=18,\quad R_2(0)=30.
\]


At fixed Theta_* the density vanishes for any admissible nondegenerate tetrad, so *every* pure geometric Fréchet derivative of the action vanishes, not just its Hessian. Therefore no strict positive quadratic coercivity estimate on an arbitrary freely varied tetrad direction can be deduced from this bare action. This is a failure of a useful dynamical positivity estimate, **not** evidence of a negative-energy ghost in this sector: the action is flat, not negative.

## Two distinct regular geometries with matching first initial jets

Use the existing split-jet FLRW realization of a prescribed scale factor with physical connection determined by the coframe and algebraic jets completing the original tetrad readout. The two illustrative choices of alpha displayed in the equations have positive determinant for every real T and identical initial tetrad and its first T derivative in the same chosen coframe. Nevertheless the standard closed FLRW scalar curvature gives distinct initial values of R. Hence the two smooth regular geometries are not related by a local isometry fixing the initial hypersurface. They are both stationary for the **specific critical-zero bare action**, provided the split-jet lift is admitted for each.

This is an explicit counterexample to claiming that the bare tetrad equations determine unique geometric accelerations from that first-order initial geometry in this minisuperspace family. Strict mathematical Cauchy well-posedness of any gauge-reduced full UBT PDE requires an additional analysis of its complete canonical data and gauge equivalences; we do not claim an all-purpose theorem for every conceivable initial-value formulation.

## Proof boundaries

Lean formal/NondegenerateBareCauchyGate.lean establishes exact flat density, failure of any positive quadratic tetrad bound in a free scalar variation, identical polynomial initial scales and different curvature witnesses as finite statements. The assignment of the closed FLRW curvature formula and the full split-jet action derivation are not Lean-formalized in this module. SymPy independently differentiates the two explicit scale factors, checks nonzero metric determinant, matching first initial tetrad jets, and their distinct Ricci/scalar curvature. It also checks exact flatness of the critical-zero density.

## Stability programme

An actual stable nondegenerate completion must (i) specify ONE selected real UBT action and a non-null regular on-shell background; (ii) identify all physical plus jet/connection gauge and second-class constraints; (iii) derive a nondegenerate physical principal symbol after reduction; (iv) construct a conserved, suitably coercive physical energy and show a well-posed, hyperbolic evolution. Adding an arbitrary positive norm, Palatini term, or theta-prime energy by assertion would not prove these requirements. The separately established split-jet Palatini construction is conditionally equivalent to an *assumed* Palatini action, but its curvature coefficient and its origin from native UBT dynamics remain open.

## Cross-checks

- research_tracks/action_selection/physics_closure_bare_action_2026_10.en.md
- research_tracks/action_selection/sharp_kinetic_volume_collapse.en.md
- research_tracks/action_selection/split_jet_palatii_variational_lift.en.md
- canonical/ACTION.en.md
