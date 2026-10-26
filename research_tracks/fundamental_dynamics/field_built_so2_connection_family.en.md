<!-- BILINGUAL-UNIT: field-built-so2-connection-family -->
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

# Field-built SO(2) stabilizer connections: a concrete covariance-respecting torsion non-selection theorem

**Status: exact local counterexample within the restricted Lorentz-real two-vector lift (26 October 2026).** The English text is the source; Czech is a corresponding working edition. Not a final UBT action, physical torsion measurement, or theorem about unrestricted two-sided biquaternionic representations.

## Assumptions

Work on an oriented, time-oriented Lorentzian four-dimensional tetrad patch, with fixed positive N0 and a metric-compatible Lorentz connection omega. The two real Lorentz vector components V and W satisfy D V = sqrt(N0) e and D W = 0; for readability absorb sqrt(N0) into e in the formulas below. Require V timelike, W noncollinear with V and e invertible. Only proper, orthochronous local Lorentz transformations are used; the construction explicitly employs the orientation pseudotensor epsilon.

## Covariant one-parameter family

Define

\[
r=\sqrt{-V^2}>0,\quad
S=W-\frac{V\cdot W}{V^2}V,\quad
s=\sqrt{S^2}>0,\quad
U=\frac Vr,\quad N=\frac Ss,
\]
\[
J^a{}_b=\eta^{ac}\epsilon_{cbde}U^dN^e,\qquad
\alpha=N_a e^a,\qquad
\boxed{\omega_\lambda{}^a{}_b=\omega^a{}_b+\frac{\lambda}{r}J^a{}_b\alpha.}
\]

Here lambda is any fixed real dimensionless number; lambda=0 and lambda=1 already give two distinct parameter-free geometric recipes. The same algebra works for a Lorentz scalar function lambda(V²,W²,V·W). J generates rotations in the plane orthogonal to both V and W. Since J and alpha are constructed tensorially from V, W, e and the oriented volume form, C_lambda=(lambda/r)J alpha transforms homogeneously in the Lorentz adjoint representation. Therefore omega_lambda is a valid connection whenever omega is one. The SO(2) stabilizer is not silently declared a gauge redundancy.

## Exact tetrad and torsion identities

Antisymmetry of epsilon and orthogonality of N to U imply

\[
J^T\eta+\eta J=0,\qquad JV=JW=0,
\]
\[
D^{\omega_\lambda}V=D^\omega V=e,\qquad
D^{\omega_\lambda}W=D^\omega W=0,
\]
\[
\boxed{
T^a(\omega_\lambda)-T^a(\omega)=
\frac{\lambda}{r}J^a{}_b\,\alpha\wedge e^b.
}
\]

Both V and W remain covariantly constrained, and the generated tetrad and metric are identical for the entire family. Thus metric compatibility, proper local Lorentz covariance, no new independent fields, and the two-vector first-jet identities do NOT uniquely pick a spin connection.

## First-jet action blindness theorem

Consider any differentiable local density L(V,W,DV,DW,g) where the connection enters **only through those two covariant first derivatives** and the metric g is determined from their composite tetrad. Keep V and W fixed and vary the connection within the common SO(2) stabilizer: delta omega V=delta omega W=0. Consequently delta(DV)=delta(DW)=delta g=0, so

\[
\boxed{\delta_C S_{1\rm jet}=0}\quad\text{for every stabilizer-valued }C.
\]

This identity holds off shell for the declared density class. Even a mathematically well-defined first-jet kinetic, potential or volume functional cannot distinguish omega and omega_lambda; merely imposing local Lorentz symmetry does not fix the stabilizer. A selector would need new information not contained in these first jets, such as curvature/torsion or second covariant jets, an additional constraint, or a proved physical equivalence quotient. This is a *conditional action-selection obstruction*, not a theorem that all possible single-Theta actions lack dynamics.

## Smooth flat-background witness

On the interior of the future timelike cone in Minkowski space, use

\[
\eta=\operatorname{diag}(-1,+1,+1,+1),\quad
e^a=dx^a,\quad V^a=x^a,\quad W^a=(0,1,0,0),\quad\omega=0.
\]
At \(p=(r,0,0,0)\), \(r>0\),
\[
J^2{}_3=1,\quad J^3{}_2=-1,\quad \alpha=e^1,
\]
\[
\Delta T^2=\frac{\lambda}{r}e^1\wedge e^3,\quad
\Delta T^3=-\frac{\lambda}{r}e^1\wedge e^2,\quad
\boxed{\Delta T^a{}_{bc}\Delta T_a{}^{bc}=\frac{4\lambda^2}{r^2}}.
\]

The normalized S and U and hence C_lambda are smooth on a neighborhood of p. The initial omega=0 has zero torsion. For nonzero lambda, the field-built connection has nonzero torsion with a nonzero Lorentz scalar norm (computed at p). Therefore the alternatives are not related by an ordinary local Lorentz gauge rotation preserving the tetrad geometry and torsion tensor up to frame transformation.

## Interaction with covariant time-qubit projectors

The projectors of PR #785 are built from the ordered pair (V,W). A transformation in their common SO(2) little group fixes both carriers and therefore their algebraic projectors. In the rest frame of V, with S along the x direction, the residual spin generator is proportional to i sigma1 and Q=sigma1; the generator commutes with Q. Consequently the stabilizer shift cannot cancel the nonzero transverse DQ of PR #785. A different transport law or an off-slice sector remains necessary for a truly parallel pair.

## Explicit limitations and action-selection gate

The construction is a **kinematic non-selection** result, not a proof that every lambda is a physical on-shell solution. Parity could constrain this epsilon-odd family if parity is imposed as an independent full O(1,3) symmetry; the result only assumes SO+(1,3). Torsion-free or additional dynamical equations can select a branch, but must be derived rather than silently inserted. Other Lorentz-covariant selectors, e.g. a Levi-Civita-based composite contortion, can be defined; existence of a selector is not the same as its uniqueness.

No unique S_UBT or Hamiltonian follows from these first-jet identities. The reduced action must vary all field-built connection contributions via the full composite chain rule of merged PR #772. To decide whether the stabilizer is auxiliary, constrained or propagating requires the final field equations and Dirac analysis.

## Reproducibility

A symbolic test checks J in so(1,3), preservation of V and W, torsion norm, covariance under a nontrivial proper Lorentz boost, and the vanishing commutator of the residual spin generator with Q. The test is limited to the explicitly declared algebraic branch.
