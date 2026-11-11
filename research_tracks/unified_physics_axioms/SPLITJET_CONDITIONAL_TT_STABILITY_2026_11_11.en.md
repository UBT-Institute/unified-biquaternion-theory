# Conditional stable tensor modes in the chosen split-jet Palatini comparator

## Strict provenance and scope

This track is NOT a proof of fundamental UBT stability and does NOT select a curvature term from biquaternion invariants. The previous work research_tracks/action_selection/split_jet_palatii_variational_lift.en.md proves conditional local classical equivalence of its freely varied split-jet auxiliary pullback to the independently *chosen* Palatini gravitational functional on non-null X patches. The source functional is written here explicitly so its unproved status is impossible to miss.

## Conditional linear tensor stability around a regular Minkowski background


\[
S_{\mathrm{SJHP}}[X,\omega,K_J,w]
=\frac{1}{4\kappa}\int\epsilon_{abcd}E^a\wedge E^b\wedge R^{cd}(\omega)
-\frac{\Lambda}{24\kappa}\int\epsilon_{abcd}E^a\wedge E^b\wedge E^c\wedge E^d.
\]
\[
\kappa>0,\qquad\Lambda=0,\qquad
g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu},\quad
h_{0\mu}=0,\ \partial_i h^{TT}_{ij}=0,\ h^{TT}_{ii}=0.
\]
\[
S_{\mathrm{TT}}^{(2)}
=\frac{1}{8\kappa}\int dt\,d^3x\left[
(\partial_t h_{ij}^{TT})^2-(\partial_kh_{ij}^{TT})^2\right].
\]
\[
H_{\mathrm{TT}}^{(2)}
=\frac{1}{8\kappa}\int d^3x\left[
(\partial_t h_{ij}^{TT})^2+(\partial_kh_{ij}^{TT})^2\right]\ge0.
\]
\[
\omega_{\mathbf k}^2=|\mathbf k|^2,\qquad
\ddot q_{\mathbf k,\lambda}+\omega_{\mathbf k}^2q_{\mathbf k,\lambda}=0.
\]


With the standard Einstein-Hilbert normalization of the chosen Palatini functional, the constrained tensor modes on Minkowski have the displayed TT quadratic action (up to boundary terms). Its derivation belongs to classical perturbative general relativity; it is an inherited comparator and NOT formalized from first principles in the new Lean file.

After spatial TT projection (two independent tensor polarizations per nonzero wave vector), the quadratic Hamiltonian is nonnegative for positive gravitational coupling. Every *nonzero wave-number* mode has a real frequency and oscillatory solutions, without exponentially growing TT linear modes. For suitable decaying/periodic boundary conditions the integral energy is conserved at this quadratic order. Pure-zero wave-number modes need a separate treatment; a free homogeneous mode may drift linearly, so strict Lyapunov stability is NOT asserted for those modes. The standard TT energy is quadratic and does not establish nonlinear global stability of Minkowski space.

## Why this does not complete fundamental UBT

The Palatini action is inserted as a candidate, not uniquely derived from complex Theta. Its coefficient, non-null jet patch, full quantum measure, connection/auxiliary constraint structure, and reduction of every non-tensor UBT mode remain to be established. The identity of all physical UBT modes with the two GR tensor polarizations has NOT been proven; a putative new UBT scalar/phase sector can introduce additional instabilities. The stability statement here is limited to the **conditional inherited TT sector**.

The companion branch research_tracks/unified_physics_axioms/NONDEGENERATE_BARE_CAUCHY_GATE_2026_11_11.en.md proves the distinct critical-zero sharp/Gram *bare* action has no geometric coercivity/evolution; the two action candidates must never be conflated. Positive TT energy does not repair that bare action. This comparison suggests the right research target: derive a genuine UBT-native geometric kinetic/principal operator from a single selected action and prove the physical Dirac reduction before claiming complete stability.

## Verification scope

Lean formal/SplitJetConditionalTTStability.lean proves nonnegative finite oscillator and TT density algebra, two-polarization sum positivity and cancellation of the energy derivative under assumed oscillator Hamilton equations. It does NOT prove Palatini-to-TT reduction, infinite-dimensional field theory energy estimates, geometric symplectic quotient or constraint closure. SymPy checks an explicit transverse-traceless symmetric matrix, Legendre transform, exact oscillator energy conservation, real wave solutions, and the homogeneous zero-mode caveat.

## Canonical references

- research_tracks/action_selection/split_jet_palatii_variational_lift.en.md
- research_tracks/unified_physics_axioms/NONDEGENERATE_BARE_CAUCHY_GATE_2026_11_11.en.md
- research_tracks/action_selection/physics_closure_2026_10.en.md
- canonical/ACTION.en.md
