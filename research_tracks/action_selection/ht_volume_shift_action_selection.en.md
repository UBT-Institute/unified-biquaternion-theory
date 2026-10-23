# Constant composite kinetic energy is an HT integration-constant shift

**C-tier exact algebraic identity; 2026-10-24. NOT a selection or microscopic derivation of the unique UBT action.** Inputs: [canonical Lorentz-jet volume collapse](lorentz_jet_volume_boundary.en.md), [adopted gravity postulate](../../canonical/gr_closure/gravity_dynamical_postulate.en.md), [action registry](../../canonical/ACTION.en.md). The existing full-action gap remains OPEN.

## Identity
On the **declared Lorentz-real nondegenerate branch**, the already classified minimal kinetic density is \(\mathcal L_{\rm kin}=\alpha\nu_E\) with \(\alpha=4cN_0\) constant. Consider the *comparison sum* of this volume contribution and the already adopted Palatini–Henneaux–Teitelboim gravity action:
\[
S_{\rm trial}=S_{\rm Pal}[E,\omega]-\kappa^{-1}\int\Lambda(\nu_E-dC_3)+\alpha\int\nu_E .
\]
This is a diagnostic combination, NOT a declaration of a new canonical UBT action or a derivation that the two pieces arise from the same microscopic rule.

For constant \(\alpha\), set \(\Lambda'=\Lambda-\kappa\alpha\). Direct algebra gives the exact functional identity
\[
\boxed{S_{\rm trial}=S_{\rm Pal}[E,\omega]-\kappa^{-1}\int\Lambda'(\nu_E-dC_3)+\alpha\int dC_3.}
\]
On a closed region or with a boundary prescription holding the appropriate C3 flux fixed, the last term contributes no bulk Euler equations. Accordingly the constant volume coefficient is **not an independently identifiable bulk gravitational coupling** in this HT sector: it simply relabels the allowed integration constant. Variation with respect to C3 still yields \(d\Lambda=0\), hence \(d\Lambda'=0\) for constant alpha. This does not compute the numerical value of \(\Lambda_0\) or Newton's coupling \(\kappa\), and boundary observables may retain sensitivity to the surface term if boundary conditions permit it.

## Sharp limitations
- If the effective coefficient depends on a dynamical \(\Theta\) scalar, \(F(\Theta)\nu_E\), the substitution \(\Lambda'=\Lambda-\kappa F\) instead produces an extra \(\int F\,dC_3\), which is **not generally a boundary term**: \(F\,dC_3=d(FC_3)-dF\wedge C_3\). The independent auxiliary equation becomes \(d(\Lambda'+\kappa F)=0\); discarding the derivative coupling would be wrong.
- If a different matter action or sector independently fixes a physical zero of vacuum energy, matching requires that extra input. Do not infer universal equivalence across sectors from this gravity-only identity.
- The minimal kinetic Lorentz-slice volume collapse was already known; the new contribution is the explicit comparison with the **HT auxiliary integration constant** in the merged gravity postulate.
- The Palatini curvature term and its coefficient do **not** follow from the constant composite energy. Selecting the fundamental action still requires a microscopic principle that yields nontrivial curvature/connection dynamics, healthy constrained energy and sourced sector reductions.
- An integration-constant relabeling does not make arbitrary history-dependent scalar energies or indefinite unconstrained kinetic directions harmless.

## Falsifiable next gate
Seek an intrinsically derived \(\Theta\)-invariant source that generates \(\epsilon E E R(\omega)\) with its coefficient **without** inserting an independent sector action. If no such mechanism is derivable, record the present classical gravity action honestly as a **minimal adopted dynamical postulate**, not as a theorem of the kinematic axioms.

Exact regression: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_ht_volume_shift.py' -v\` (SymPy).
