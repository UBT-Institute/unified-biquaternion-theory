<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# G1: an explicitly curved Lorentzian metric from a biquaternion, and its linear-mode obstruction

**2026-10-28 · C_working · PR #809 only · NO CANONICAL PROMOTION.**
This is the next gate of the conformal/causal/shared-reality track.
It tests whether Theta's *existing complex matrix degrees of freedom*
can contain geometric curvature without introducing an independent
tetrad, while distinguishing geometry from a viable gravitational
dynamics. **It does not derive two graviton modes, Einstein equations
or the full SU(2,2) Cartan connection.**

## 1. Precisely declared representation and bilinear

Use ONE trial carrier Theta∈C⊗H≅Mat₂(C), **not** a claim that
the full UBT Theta must have exactly eight real components. Write

\[
 Q=(u_0+i v_0)I+\sum_{j=1}^3(u_j+i v_j)\sigma_j.
\]

The already classified real invariant form, in the
SL(2,C) congruence / constant-phase representation, is

\[
 H(Q)=\mathrm{Tr}(Q^\sharp Q^\dagger)
 =2(u_0^2+v_0^2-\mathbf u^2-\mathbf v^2).
\]

Its real bilinear polarization normalized to unit Minkowski
coefficients is

\[
 B(P,Q)=\tfrac14\{H(P+Q)-H(P)-H(Q)\}.
\]

Thus B has real signature (2,6), not the positive (8,0) metric
of the SU(2,2) future tube. On a regular selected branch take

\[
 g_{\mu\nu}[\Theta,\Omega]
     :=B(D_\mu^\Omega\Theta,D_\nu^\Omega\Theta).
\]

With the ordinary *pure Lorentz* two-sided covariant derivative,
`DTheta=dTheta+Omega Theta+Theta Omega†`, this expression is
locally SL(2,C)-invariant if Omega transforms as a connection;
a constant overall U(1) phase also preserves B. A local phase
requires its **own** compatible connection and is not generated
by the cancelling central phase of the pure Lorentz pair.

The expression does **not** inherit full SU(2,2) invariance:
it is an explicitly reduced Lorentz-branch test, not a resolution
of the G/K→G/P obstruction T2. More importantly, it is not
identified with the locked central anticommutator metric of UBT:
that equivalence would need a separate, noncircular proof.
The connection is set to Omega=0 in the following chart.
No connection field equation or microscopic action is assumed.

## 2. A nonflat metric with no independent tetrad input

Choose real coordinates t,x,y,z and a real trial scale kappa.
Let

\[
 \boxed{\Theta=tI+x\sigma_1+y\sigma_2+z\sigma_3
                   +i\kappa tx\,\sigma_1.}
\]

There is exactly one additional *imaginary* matrix direction
beyond the four Hermitian coordinate directions. Direct
polarization of dTheta gives

\[
 \boxed{g=\eta-\mathrm d(\kappa tx)\otimes\mathrm d(\kappa tx),}
\]
\[
 ds^2=dt^2-dx^2-dy^2-dz^2
       -\kappa^2(x\,dt+t\,dx)^2,\quad
 \eta=\mathrm{diag}(1,-1,-1,-1).
\]

Put Delta=1-kappa² x² and
A=1+kappa²(t²−x²). On Delta>0 and A>0,
a completely explicit real coframe is

\[
 e^0=\sqrt{\Delta}\,dt
     -\frac{\kappa^2tx}{\sqrt{\Delta}}\,dx,\qquad
 e^1=\sqrt{A/\Delta}\,dx,\qquad
 e^2=dy,\qquad e^3=dz.
\]

It has det(e)=sqrt(A)≠0 and
g=eta_ab e^a e^b. Hence the matrix tetrad
`E_mu=i sum_a e^a_mu sigma_a` lies in
i·Herm₂ as required by the old Lorentz-real
readout convention. This is a *gauge choice derived
from the metric*, not a unique natural SU(2,2)-covariant
tetrad construction.

With R^rho_{sigma mu nu} =
∂_mu Γ^rho_{nu sigma}−∂_nu Γ^rho_{mu sigma}
+Γ^rho_{mu lambda}Γ^lambda_{nu sigma}
−Γ^rho_{nu lambda}Γ^lambda_{mu sigma},
the exact result is

\[
 R^t{}_{x t x}
 =\frac{\kappa^2(1+\kappa^2t^2)}
       {[1+\kappa^2(t^2-x^2)]^2},
 \qquad R_{txtx}(0)=\kappa^2.
\]

This is genuinely **curved** when kappa≠0.
At the origin the (t,x)-sector Ricci values are
`Ric_tt=-kappa²`, `Ric_xx=+kappa²`,
but `Ric_yy=Ric_zz=0`. It is NOT
an Einstein metric for nonzero kappa. Therefore
one cannot cite this construction as an on-shell GR
solution or as a gravity action derivation.

The constructed g uses an *indefinite* invariant
bilinear, not the positive invariant future-tube
metric. No contradiction with T1 arises.
This is a counterexample only to the OVERBROAD
claim that **every** derivative-only Theta metric
must be flat; the earlier theorem concerns the
specific pure-gradient tetrad e=d(phi).

## 3. Full-rank jet versus physical metric rank

At a flat affine background
`Theta_0=x^a sigma_a`, the four Hermitian
jet directions span a nondegenerate Lorentz
subspace. Write variation in tangent and normal
directions as `delta Theta=u^a sigma_a+n^I N_I`
where `B(sigma_a,N_I)=0` and `N_I` are
constant target normals. Then exactly

\[
 \boxed{\delta g_{\mu\nu}
  =\partial_\mu u_\nu+\partial_\nu u_\mu.}
\]

Normal variations do not enter at linear order,
because the background embedding has zero
second fundamental form. The tangential
variation is the Lie derivative of eta, so the
linearized Riemann tensor vanishes.
The explicit family above makes the even-order
behavior transparent:
`g(epsilon)=eta−epsilon² d(kappa tx)^2`.
Thus `d g/depsilon|_0=0`.

**THEOREM G1-LIN [restricted analytic]:** The
first-jet metric B(dTheta,dTheta) on the affine
Lorentz-real background has no gauge-invariant
linearized graviton metric perturbations from its
eight real embedding fields. It is not a
linearized GR theory on that background without
additional dynamics, altered background, connection
data or extra geometric structure. This says
nothing universal about quantum emergence or all
possible UBT completions.

The physical (symmetric) metric has ten independent
components: insisting on a rank-16 map from Theta
jets to a **gauge-fixed** derived coframe is not
the appropriate criterion. Six Lorentz frame
directions are gauge. At an affine nondegenerate
background the variation of metric with respect
to the 32 freely varied real jet components has
rank 10; only tangential jet directions enter
to first order, and their integrability for
actual fields makes the spacetime perturbation
pure diffeomorphism.

## 4. Broader four-real first-jet restriction

**THEOREM G1-4R [restricted analytic]:**
For four real scalar fields phi^i with invertible
Jacobian, any coframe of the form
`e^a_mu=E^a_i(phi) partial_mu phi^i`
with a *fixed* target coframe E defines
\[
 g=\phi^*(\gamma),\qquad
 \gamma_{ij}=\eta_{ab}E^a_i E^b_j.
\]
The inverse-function theorem makes phi a local
diffeomorphism; hence every such g is locally
diffeomorphic to the **same** prescribed target
metric gamma. It cannot realize arbitrary
independent linearized gravitational degrees
of freedom modulo diffeomorphisms. The special
case E^a_i=delta^a_i has Riemann=0, as tested
in G1_NEGATIVE_CONTROL.

An arbitrary nonconstant target E can give a
curved metric (even a maximally symmetric
Einstein metric), but this *imports that curvature
as a target geometry*. It is not derived
gravitational dynamics.

The extra imaginary components in the eight-real
matrix trial admit nontrivial *normal embedding*
curvature, as shown in section 2. This does not
establish that eight components are sufficient
to represent every 4D Einstein geometry or to
support spin-2 propagation.

## 5. Full SU(2,2) candidate and Cartan connection: boundary

Candidate A (project Re DTheta to a Lorentz
coframe) becomes the restricted four-real
pullback or the above indefinite 8-real
induced-metric construction after a choice
of Lorentz-real slice. It does not supply a
canonical **full SU(2,2)-equivariant**
projection. The G/K stabilizer K does
not preserve the required Lorentz four-plane;
a P-reduction must be specified and derived.

Candidate B (a null-ray/tractor compensator)
is obstructed as a pointwise fully G-equivariant
map G/K→G/P by T2; a jet-dependent reduction
is **still OPEN**, not disproved. A Cartan
connection with freely chosen soldering component
e^a is legitimate gravity but not proof that
it arose from Theta. A jet-dependent conformal
Cartan reduction, its exact transformation,
and its full parent-action variation remain
unconstructed.

**DO NOT claim G1 is solved:** the curved example
passes Lorentz signature and nonzero curvature,
but fails the full SU(2,2) covariance/dynamics
requirements; the tractor route is still open.
This is a *PARTIAL constructive result plus an
exact linearized obstruction*, not a selected action.

## 6. Recommended research decision

Preserve PR #807 (matched-pairing/free-jet bare
action no-go), PR #808 (SO(1,4) comparator) and
PR #809 independently. The next task is to test
a *dynamically justified* covariant connection
and/or jet-derived P-reduction that can supply
nontrivial first-order graviton fluctuations.
Do not move prematurely to an information-derived
action: first specify the causal cone and
normalization for the same Theta-derived metric.
Only then impose the operational Shared Reality
state-consistency axiom and any Jacobson-style
entanglement equilibrium.

## Verification

Run

```bash
python -m unittest discover -s tests -p 'test_theta_induced_geometry.py' -v
```

Seven exact SymPy checks locally passed for:
the invariant pairing, SL(2,C) congruence and
global phase, induced metric and determinant,
derived coframe, nonzero Riemann tensor,
linearized normal/tangent response, and rank-10 jet map.
The analytic G1-4R inverse-function theorem
argument is not a Lean proof. These checks
do NOT certify a field-theoretic action,
constraint algebra, physical ghosts, quantum
dynamics, or observational predictions.

## 7. Causal / shared-reality scale limitation [STD + conditional inference]

If g is Lorentzian and f(x)>0, then g'=f(x)^2 g has exactly the
same pointwise timelike, null and spacelike cones and the same
causal-order relations (with fixed time orientation). Therefore
finite signal speed and any [SR] rule based *only* on causal
accessibility, overlap of diamonds and consistency of their
locally shared records cannot determine the conformal scale
f(x). This is not a failure of [SR]: it identifies the minimum
additional quantitative datum needed for a gravity law.

An entropy/area density or an energy calibration may introduce
such a scale, but its absolute coefficient (e.g. Newton's G
or a Planck area) must then be derived or declared and measured,
not inferred from cone preservation. A Jacobson-type first-law
condition must carry these explicit normalizations. This is
a scoped underdetermination theorem, **not** a no-go for a richer
quantitative shared-reality principle.
