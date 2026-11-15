<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Research hypotheses and exact restricted differential-geometric examples; no new fundamental action, independent extra dimension, GR, QM, QED or Standard Model derived.
UBT-AI-PROVENANCE-END
-->

# Inverse-first-principles UBT programme: dependent dimensions, rank/quotient gates and the metric-lock trap

**16 November 2026. Status: HYPOTHESIS + 10 scoped verified tests (L0 conditional mathematics).**

**Motivation.** UBT must not invent missing sectors by writing Maxwell, Dirac, Einstein, SU(3) or a photon kinetic term into an action and then calling them derived. We instead seek a minimal, independent set of principles capable of selecting one Theta quantum dynamics, including its observer/physical quotient and effective dimension. A user's further hypothesis is that some presumed coordinates, complex-time components, phase variables or internal dimensions may be functionally dependent. Such dependencies can remove spurious modes AND generate nontrivial induced geometry.

## 1. Reverse-engineering acceptance contract: classify, do not assume

Compare the known IR theories in terms of necessary criteria, rather than inserting their equations:

1. **Operational/relational covariance**: physical predictions under change of observer and coordinates agree on overlap. Distinguish mere covariance, which cannot determine H, from experimentally calibrated inter-point information. Source: research_tracks/fundamental_dynamics/SHARED_REALITY_FIRST_PRINCIPLES_RESTART.en.md.
2. **Independent coordinates and quotient**: identify the rank of the physically accessible distribution, integrability of dependencies, and the constraints/gauge redundancies before counting dimensionality or propagating modes.
3. **Causal, unitary local quantum dynamics**: physical positive-energy generator, observer-algebra composition, spin structure and CAR locality. These are IR acceptance conditions until a microscopic Theta derivation is established.
4. **Local frame/gauge consistency**: the locked real tetrad E=DTheta/sqrt(N0), central sharp metric, diffeomorphism and Lorentz covariance, a *distinct* internal charge generator and anomaly-free quantum correlators.
5. **Minimal low-energy derivative structure**: no higher-derivative ghost in the physical reduced theory; reproduce massless spin-two GR and massless spin-one QED only as output. Standard 4D pure metric second-order conserved equations are constrained by Lovelock's theorem to Einstein tensor and a cosmological term (subject to its assumptions), but this does NOT derive 4D, Theta or couplings.

These are a **selection programme**, not uniquely axioms or a uniqueness proof. If two inequivalent healthy Hamiltonians pass, the principles are insufficient: do NOT tune a new principle merely to match a wanted experimental number. Keep free couplings explicitly identified and count independent assumptions.

## 2. Dimension census for the current Theta matrix

A full complex biquaternion in the faithful representation has 4 complex = **8 real value components**. This is NOT eight independent spacetime coordinates. On a 4D base, its value map Theta:M4->R8 has differential rank at most 4. The 4D coframe E_mu in W_L=i Herm2 has 4x4=16 real jet values, whereas the generic real first jet dTheta has 4x8=32. In the connection-free comparator D=d, insisting that dTheta lies in i Herm2 imposes 16 real linear jet conditions: the real Hermitian part is locally constant; the remaining imaginary Hermitian component is four real functions h^a(x).

For a nondegenerate pure-gradient tetrad Theta=i h^a(x)sigma_a+constant with E_mu=i (partial_mu h^a) sigma_a,
\[
\boxed{g_{\mu\nu}=\eta_{ab}\partial_\mu h^a\,\partial_\nu h^b.}
\]
The inverse-function theorem makes h^a coordinates, so the spacetime metric is **exactly flat** on this branch. This was previously noted in THETA_DIRAC_CHARGE_CURRENT_PROJECTED_U1_SOLDERING_GATE_2026_11_15.en.md. Neither the remaining four field components nor the 10 component metric tensor should be identified directly with propagating quantum modes; their reduced count requires full constraints and an on-shell Hamiltonian.

For N=I, the one-clock normalized density \(\rho=\Theta\Theta^\dagger/\mathrm{tr}(\Theta\Theta^\dagger)\) has generic differential rank 3 as a map from 8 real entries into the open Bloch ball, giving a local five-dimensional kernel. In particular at Theta=I, delta rho = sum_{j=1}^3 delta Re(Theta_j) sigma_j. The observer may lose information without those invisible directions being physical gauge: research_tracks/information_first/INFORMATION_GRAVITY_QUOTIENT_GATE_2026_11.en.md and INFORMATION_BLOCH_ORBIT_GRAVITY_QUOTIENT_2026_11.en.md found distinct local observer records on the same reduced gravity representative. Do NOT quotient physical information until the common action and observables specify which changes are gauge.

## 3. The strongest existing warning: using the same field gradients as metric AND kinetic energy collapses the dynamics

If \(\langle E_\mu,E_\nu\rangle=N_0 g_{\mu\nu}\) is exactly the fixed canonical metric-generating pairing in dimension d, then
\[
\boxed{g^{\mu\nu}\langle E_\mu,E_\nu\rangle=dN_0.}
\]
In d=4 this is exactly \(4N_0\), regardless of the tetrad's local shape. A bare action based solely on this contraction is thus algebraically a cosmological/volume term (plus a potential), not an independent propagating Einstein graviton kinetic energy. It also cannot be rescued by merely changing the **number of value-space components** of Theta, as proven in research_tracks/action_selection/physics_closure_bare_action_2026_10.en.md and canonical/ACTION.en.md. This is a real **metric-lock dependency obstruction**. A candidate remedy must involve independently selected curvature, information transport, extrinsic geometry, nontrivial composite torsion or additional independent kinetic invariants; their exact physical variation and ghost safety must be proved, not assumed.

## 4. Proposed dependent compact phase: local vertical-extension identifiability no-go

Take a nominal fifth ANGULAR coordinate \(\psi\) with period \(2\pi\), whose metric radius is R, but hypothesize the physical submanifold satisfies \(\psi=f(x^\mu)\bmod 2\pi\). The pullback field is \(\widetilde\Theta(x)=\Theta(x,f(x))\) and satisfies
\[
\partial_\mu\widetilde\Theta
=\bigl[\partial_\mu\Theta+(\partial_\psi\Theta)\,\partial_\mu f\bigr]_{\psi=f}.
\]
For arbitrary full-matrix F(x), H(x), define two smooth periodic lifts
\[
\Theta_1(x,\psi)=F(x),\quad
\Theta_2(x,\psi)=F(x)+\sin(\psi-f(x))\,H(x).
\]
These have the **same pullback and all its tangential derivatives** but arbitrary distinct normal jets:
\[
\partial_\psi\Theta_1|_{\psi=f}=0,\qquad
\partial_\psi\Theta_2|_{\psi=f}=H(x).
\]
Therefore a hypothetical physical theory defined only on the constrained graph CANNOT reconstruct a unique independent vertical kinetic energy or KK tower without a further normal-extension law and its measure. In particular an assumed compact coordinate in Theta's phase/complex-time *values* does not establish a new independent spacetime direction. This is a sharp identifiability obstruction **conditional on dependency**; it is not a no-go for theories with a genuinely independent compact circle and bulk dynamics.

## 5. Positive geometric counterpoint: a dependent dimension can produce curved induced 4D geometry

Take flat ambient space with
\[
ds_5^2=-dt^2+dx^2+dy^2+dz^2+R^2 d\psi^2,
\quad\psi=f(x^\mu).
\]
The graph has induced metric
\[
\boxed{g_{\mu\nu}^{\rm graph}=\eta_{\mu\nu}+R^2\partial_\mu f\,\partial_\nu f.}
\]
For \(f=\kappa xy\), direct Gauss/Christoffel calculation using convention \(R^a{}_{bcd}=\partial_c\Gamma^a_{bd}-\partial_d\Gamma^a_{bc}+\ldots\) yields
\[
\boxed{R_{xyxy}=-\frac{R^2\kappa^2}{1+R^2\kappa^2(x^2+y^2)}\ne0.}
\]
The ambient 5D geometry is flat and the induced 4D geometry is not: dependent directions can encode intrinsic curvature via an embedding. However at a constant reference f=0 and f=epsilon h, \(g_{\mu\nu}^{\rm graph}-\eta_{\mu\nu}=O(\epsilon^2)\). There is no linear metric perturbation or free spin-two graviton from this simple ONE-scalar graph. Nor is \(g^{\rm graph}\) the canonical UBT central-sharp tetrad metric; treating it as such without an explicit derived identity would be an unauthorized replacement.

A full unconstrained analytic 4D metric has 10 components at a point. Classical local analytic embedding results (Janet-Cartan-Friedman, with pseudo-Riemannian variants) give a 10D FLAT ambient space as a sufficient local embedding dimension for general analytic 4D metrics, not an inevitable physical 10D spacetime or a unique minimal number for individual metrics. This is motivation to study the rank/normal bundle of proposed 8-real/10-real Theta carriers, not permission to introduce independent dimensions.

## 5b. More promising dependent-dimension route: NONINTEGRABLE circle transport generates U(1) curvature

A functional graph psi=f(x) was an INTEGRABLE dependence; it does not exhaust the user's proposal. A weaker and more interesting structure is a circle bundle over the physical 4D base, with an *angular* coordinate psi modulo 2pi and a one-form
\[
\boxed{\vartheta=d\psi+A_\mu(x)dx^\mu,\qquad \mathcal H=\ker\vartheta.}
\]
The horizontal physical directions are not required to be tangent to a 4D graph! A local reparameterization psi'=psi-chi(x) forces A'=A+dchi so theta remains unchanged; the transformation is the Abelian U1 gauge law. The curvature is \(F=dA\) and does NOT require extra physical propagating spacetime coordinates. A nonzero curvature measures the Frobenius obstruction to integrating horizontal directions into psi=f(x).

Explicitly on an x,y subpatch set \(A=B x\,dy\), so
\[
F=B\,dx\wedge dy,\quad H_x=\partial_x,\quad
H_y=\partial_y-Bx\,\partial_\psi,\quad
\boxed{[H_x,H_y]=-B\partial_\psi}.
\]
For B!=0 there is no smooth f(x,y) with df=-A on an open patch because mixed partials would disagree; this is NONHOLONOMIC dimension coupling. The correct primitive would be a constrained horizontal DISTRIBUTION/transport, not an independent scalar function or a passive extra coordinate.

As an instructive **standard Kaluza-Klein comparator** introduce an angular circle of fixed radius R and the 5D metric
\[
\boxed{ds_5^2=g_{\mu\nu}dx^\mu dx^\nu+R^2(d\psi+A_\mu dx^\mu)^2.}
\]
For fields independent of psi and constant R, its 5D Ricci scalar satisfies the standard reduction identity
\[
\boxed{\mathcal R_5=\mathcal R_4-\frac{R^2}{4}F_{\mu\nu}F^{\mu\nu}.}
\]
A direct five-dimensional Christoffel/Ricci computation for a flat base and A=Bx dy gives EXACTLY \(\mathcal R_5=-R^2B^2/2\) since F_{\mu\nu}F^{\mu\nu}=2B². Therefore a SINGLE 5D Einstein-Hilbert action would yield the Maxwell-square term after circle integration, with the sign/relative coefficient dictated by the geometry. Unlike the projected Maurer–Cartan Berry candidates, F=dA has a LINEAR perturbation about A=0 and can support a quadratic Maxwell kinetic term.

**Crucial non-adhoc qualification:** the circle-bundle connection A, fifth metric component, \(\psi\)-independence, constant R and 5D Einstein-Hilbert action were all specified in this comparator; NONE is yet selected by fundamental UBT. Promoting them to axioms would IMPORT Kaluza-Klein physics and violate the user's reverse-engineering requirement. The *research task* is instead to show an EXISTING connection/constraint of one complex Theta has precisely this nonintegrable circle-bundle quotient, or to falsify the candidate. Distinguish its internal U1 from the Lorentz SO2 stabilizer and prove the one-Theta action reduces to the needed curvature coefficient. A generic nonzero F is a genuine geometric obstruction, NOT automatically the physical photon. The known KK mechanism is an accepted external benchmark, not a new discovery.

**A sharper D2 test:** derive a candidate 1-form theta[Theta,DTheta] and compute \(d\vartheta\) restricted to \(\ker\vartheta\). If it vanishes, the graph branch is locally integrable and its vertical dynamics need separate justification. If nonzero, test a consistent nonholonomic/connection quotient, then construct the gauge-invariant action and full Hessian with no added independent photon.

## 6. Research roadmap and kill criteria

**D1 — dimension inventory.** For each proposed dimension (x^mu, compact psi, complex tau, observer phase, Theta value components) specify: independent coordinate, algebraic internal coordinate, field, or gauge-label; exhibit its covariant definition and the Jacobian rank. Reject coordinate-counting derived solely from notation.

**D2 — integrability of constraints.** Postulate NO new dimension count. Enumerate candidate relations C_I(q,Theta,dTheta)=0, compute Jacobian rank and Frobenius closure of the physical tangent distribution; test integrable vs nonintegrable (nonholonomic) dependencies. Check whether they survive the canonical Lorentz slice and UBT two-sided derivative. A nonintegrable distribution is NOT the graph psi=f(x); it needs its own mechanics.

**D3 — ghost and metric-lock selection.** Count reduced symplectic/Dirac degrees of freedom after primary and secondary constraints and gauge quotient. Measure the kinetic Hessian and principal symbols and ensure effective photon/graviton modes are not pure coordinate changes or phase redefinitions.

**D4 — matched reverse reconstruction.** Derive, rather than assume, the spin-2 causal-cone GR sector, unitary quantum operator net and CAR, first-class internal U1 photon and electroweak/colour multiplets. Record separate coupling/scale parameters without tuning measured constants by hand. Test IR QED Ward identities, GR, SM chirality/anomalies. Only a shared action with a clear pullback to all sectors qualifies.

**Immediate verdict:** the dependency idea is mathematically testable and can explain two pre-existing structural failures: (i) metric-lock contraction erases the purported kinetic term; (ii) treating a phase direction as an independent compact coordinate when its normal derivatives are not identifiable from physical data. The graph example also proves that dependencies may induce curvature. New nonintegrable phase-transport tests give a stronger U1-bundle bridge, with a direct 5D Ricci comparator, without proving this bundle is selected by Theta. Whether actual UBT's compact phase is dependent remains **OPEN**, not established.

Ten new exact small SymPy/pytest checks pass locally in tests/test_theta_dependent_dimension_reverse_principles_gate.py. These tests verify mathematical identities and counterexamples only, not the derivation of the proposed dimension constraints from the UBT action.
